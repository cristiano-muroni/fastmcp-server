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

@app.post("/chat")
async def chat(req: ChatRequest):

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=req.mensagem
    )

    return {
        "pergunta": req.mensagem,
        "resposta": response.text
    }