# MCP Agent com Gemini, FastMCP e SQLite

Projeto de estudo e experimentação utilizando:

- FastAPI
- FastMCP
- Google Gemini
- SQLite
- MCP (Model Context Protocol)

O objetivo é permitir que o Gemini analise a solicitação do usuário, selecione a ferramenta adequada e execute consultas em APIs externas ou bancos de dados através de um servidor MCP.

---

# Arquitetura

```text
Usuário
   │
   ▼
FastAPI (/chat)
   │
   ▼
Gemini
   │
   ▼
Seleção da Tool
   │
   ▼
MCP Client
   │
   ▼
MCP Server
   │
   ├── CPF Validator
   ├── ViaCEP
   └── Beneficiary (SQLite)
   │
   ▼
Resultado
   │
   ▼
Gemini
   │
   ▼
Resposta Final