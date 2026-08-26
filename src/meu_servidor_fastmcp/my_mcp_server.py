from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    Retorna uma saudação.
    """
    return f"Hello, {name}!"


@mcp.tool
def consultar_cliente(codigo: int) -> dict:
    """
    Retorna um cliente pelo código.
    """
    return {
        "codigo": codigo,
        "nome": "Ford",
        "cidade": "Mogi-Guaçu"
    }


@mcp.tool
def postal_code(cep: str) -> dict:
    """
    Consulta a API ViaCEP e retorna os dados do endereço.
    """

    cep = cep.replace("-", "").strip()

    response = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if data.get("erro"):
        return {
            "erro": "CEP não encontrado"
        }

    return data


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=5000
    )