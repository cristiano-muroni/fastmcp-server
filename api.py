from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from fastmcp import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

mcp_client = Client("http://localhost:5000/mcp")

@app.get("/tools")
async def tools():

    async with mcp_client:
        result = await mcp_client.list_tools()

    return result

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class ChatRequest(BaseModel):
    mensagem: str

@app.get("/teste")
async def teste():
    async with mcp_client:
        result = await mcp_client.call_tool(
            "soma",
            {
                "a": 10,
                "b": 20
            }
        )
    return result

@app.post("/chat")
async def chat(req: ChatRequest):
    mensagem = req.mensagem.lower()

    if "somar" in mensagem:
        
        async with mcp_client:
            result = await mcp_client.call_tool(
                "soma",
                {"a": 10, "b": 20}
            )

        return result

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=req.mensagem
    )

    return response.text