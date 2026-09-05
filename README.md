# MCP Agent com Gemini, FastMCP e SQLite

Projeto de estudo e experimentação utilizando:

- FastAPI
- FastMCP
- Google Gemini
- SQLite
- MCP (Model Context Protocol)

O objetivo é permitir que o Gemini analise a solicitação do usuário, selecione a ferramenta adequada e execute consultas em APIs externas ou bancos de dados através de um servidor MCP.

---

# Instalação
## Criar ambiente virtual
```bash
python -m venv .venv
```
Ativar:
```bash
.venv\Scripts\activate
```
# Instalar dependências
```bash
pip install -r requirements.txt
```
Ou:
```bash
uv sync
```
# Variáveis de ambiente
Criar um arquivo .env
```text
GEMINI_API_KEY=sua_chave
MCP_CLIENT_URL=http://127.0.0.1:5000/mcp
```
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
```
# Estrutura do projeto
```text
fastmcp/
│
├── api.py
│
├── src/
│   │
│   ├── database/
│   │   └── beneficiarios.db
│   │
│   ├── prompts/
│   │   └── tool_selection_prompt.py
│   │
│   ├── services/
│   │   ├── beneficiario_service.py
│   │   ├── cpf_validator.py
│   │   └── via_cep_service.py
│   │
│   └── meu_servidor_fastmcp/
│       └── my_mcp_server.py
│
├── .env
├── .gitignore
└── README.md
```
