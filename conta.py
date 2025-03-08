from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, cliente, tipo):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0  
        self.__tipo = tipo  

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def get_numero(self):
        return self.__numero

    def get_cliente(self):
        return self.__cliente

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor

    def get_tipo(self):
        return self.__tipo

    def __str__(self):
        return f"Conta {self.__tipo.capitalize()} - Número: {self.__numero}, Titular: {self.__cliente.get_nome()}, Saldo: {self.__saldo}"

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente, "corrente")

    def sacar(self, valor):
        if valor > self.get_saldo():
            print("Saldo insuficiente!")
        else:
            self.set_saldo(self.get_saldo() - valor)
            print(f"Saque de R${valor} realizado com sucesso.")

    def depositar(self, valor):
        self.set_saldo(self.get_saldo() + valor)
        print(f"Depósito de R${valor} realizado com sucesso.")

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente, "poupanca")

    def sacar(self, valor):
        if valor > self.get_saldo():
            print("Saldo insuficiente!")
        else:
            self.set_saldo(self.get_saldo() - valor)
            print(f"Saque de R${valor} realizado com sucesso.")

    def depositar(self, valor):
        self.set_saldo(self.get_saldo() + valor)
        print(f"Depósito de R${valor} realizado com sucesso.")
