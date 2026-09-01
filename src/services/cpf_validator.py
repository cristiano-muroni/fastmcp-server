import re

INVALID_CPFS = {
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
}


def validate_cpf(cpf: str) -> dict:

    cpf = re.sub(r"\D", "", cpf)
    cpf = cpf[:11]

    if len(cpf) != 11:
        return {"valid": False, "cpf": None}

    if cpf in INVALID_CPFS:
        return {"valid": False, "cpf": None}

    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11

    if resto in (10, 11):
        resto = 0

    if resto != int(cpf[9]):
        return {"valid": False, "cpf": None}

    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto in (10, 11):
        resto = 0

    if resto != int(cpf[10]):
        return {"valid": False, "cpf": None}

    return {"valid": True, "cpf": cpf}
