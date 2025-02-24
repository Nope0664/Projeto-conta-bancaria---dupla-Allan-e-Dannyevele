from exceçoes import LoginInvalidoError


class Usuario:
    usuarios_registrados = {}

    def __init__(self, nome, cpf, telefone, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha

    @classmethod
    def cadastrar(cls):
        print("\n=== Cadastro de Usuário ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Crie uma senha: ")

        if cpf in cls.usuarios_registrados:
            print("Erro: CPF já cadastrado!")
            return None

        usuario = cls(nome, cpf, telefone, email, senha)
        cls.usuarios_registrados[cpf] = usuario
        print("Cadastro realizado com sucesso!")
        return usuario

    @classmethod
    def login(cls):
        print("\n=== Login ===")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        usuario = cls.usuarios_registrados.get(cpf)
        if usuario and usuario.senha == senha:
            print(f"Bem-vindo, {usuario.nome}!")
            return usuario
        else:
            raise LoginInvalidoError  # Lança um erro se o login for inválido