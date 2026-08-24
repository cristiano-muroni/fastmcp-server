from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from fastmcp import Client
from dotenv import load_dotenv

import os
import json

load_dotenv()

app = FastAPI()

mcp_client = Client("http://localhost:5000/mcp")

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class ChatRequest(BaseModel):
    mensagem: str


@app.get("/tools")
async def tools():

    async with mcp_client:
        result = await mcp_client.list_tools()

    return result


@app.post("/chat")
async def chat(req: ChatRequest):

    async with mcp_client:

        tools = await mcp_client.list_tools()

        prompt = f"""
Você é um agente que decide quando utilizar ferramentas.

Ferramentas disponíveis:

{tools}

Pergunta do usuário:

{req.mensagem}

Se alguma ferramenta for necessária, responda APENAS JSON válido:

{{
  "tool": "nome_da_tool",
  "args": {{
  }}
}}

Caso nenhuma ferramenta seja necessária, responda:

{{
  "tool": null
}}
"""

        decision = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        decision_text = (
            decision.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            decision_data = json.loads(decision_text)

        except json.JSONDecodeError:

            response = gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=req.mensagem
            )

            return {
                "resposta": response.text
            }

        tool_name = decision_data.get("tool")

        if tool_name is None:

            response = gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=req.mensagem
            )

            return {
                "resposta": response.text
            }

        args = decision_data.get("args", {})

        tool_result = await mcp_client.call_tool(
            tool_name,
            args
        )

        final_response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
Pergunta original:

{req.mensagem}

Resultado obtido da ferramenta:

{tool_result.data}

Responda ao usuário de forma natural e amigável.
"""
        )

        return {
            "tool_utilizada": tool_name,
            "resultado_tool": tool_result.data,
            "resposta": final_response.text
        }