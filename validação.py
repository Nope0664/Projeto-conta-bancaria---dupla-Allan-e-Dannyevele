import re

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def validar_telefone(telefone):
    return len(telefone) >= 8 and telefone.isdigit()

def validar_email(email):
    return re.match(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", email)

def validar_endereco(endereco):
    return len(endereco) >= 5
