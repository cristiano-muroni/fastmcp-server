from fastmcp import FastMCP
from services.cpf_validator import validate_cpf
from services.via_cep_service import get_address_by_cep
from services.beneficiario_service import get_beneficiario

mcp = FastMCP("My MCP Server")


@mcp.tool
def greet(name: str) -> str:
    """
    Retorna uma saudação.
    """
    return f"Hello, {name}!"


@mcp.tool
def to_check_cpf(texto: str) -> dict:
    """
    Extrai e valida um CPF a partir de qualquer texto informado.
    """

    return validate_cpf(texto)


@mcp.tool
def postal_code(cep: str) -> dict:
    """
    Consulta um CEP brasileiro utilizando a API ViaCEP.
    Retorna logradouro, bairro, cidade, estado, DDD e demais informações.
    Use quando o usuário pedir informações de endereço ou informar um CEP.
    """

    return get_address_by_cep(cep)


@mcp.tool
def beneficiary(id: int = None, matricula: str = None, nome: str = None) -> dict:
    """
    Consulta beneficiários por id,
    matrícula ou nome.
    """

    return get_beneficiario(id=id, matricula=matricula, nome=nome)


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=5000)
