class Cliente:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco
