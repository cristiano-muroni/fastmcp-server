from fastmcp import FastMCP
import requests
import re

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    Retorna uma saudação.
    """
    return f"Hello, {name}!"


@mcp.tool
def get_client(codigo: int) -> dict:
    """
    Retorna um cliente pelo código.
    """
    return {
        "codigo": codigo,
        "nome": "Ford",
        "cidade": "Mogi-Guaçu"
    }

@mcp.tool
def to_check_cpf(texto: str) -> dict:
    """
    Extrai e valida um CPF a partir de qualquer texto informado.
    """

    cpf = re.sub(r"\D", "", texto)

    cpf = cpf[:11]

    if len(cpf) != 11:
        return {
            "valid": False,
            "cpf": None
        }

    if cpf in {
        "00000000000",
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999",
    }:
        return {
            "valid": False,
            "cpf": None
        }

    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11

    if resto in (10, 11):
        resto = 0

    if resto != int(cpf[9]):
        return {
            "valid": False,
            "cpf": None
        }

    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto in (10, 11):
        resto = 0

    if resto != int(cpf[10]):
        return {
            "valid": False,
            "cpf": None
        }

    return {
        "valid": True,
        "cpf": cpf
    }


@mcp.tool
def postal_code(cep: str) -> dict:
    """
    Consulta um CEP brasileiro utilizando a API ViaCEP.
    Retorna logradouro, bairro, cidade, estado, DDD e demais informações.
    Use quando o usuário pedir informações de endereço ou informar um CEP.
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