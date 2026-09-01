import requests


def get_address_by_cep(cep: str) -> dict:
    cep = cep.replace("-", "").strip()

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)

    response.raise_for_status()

    data = response.json()

    if data.get("erro"):
        return {"erro": "CEP não encontrado"}

    return data
