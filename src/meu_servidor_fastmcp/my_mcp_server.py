from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def consultar_cliente(codigo: int) -> dict:
    """
    Retorna um cliente pelo código
    """
    return {
        "codigo": codigo,
        "nome": "Ford",
        "cidade": "Mogi-Guaçu"
    }

@mcp.tool
def soma(a: int, b: int) -> int:
    """
    Soma dois números inteiros
    """
    return a + b


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=5000
    )