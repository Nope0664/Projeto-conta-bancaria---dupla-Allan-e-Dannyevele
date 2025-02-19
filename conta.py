#Interface base para contas
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

    def __eq__(self, other):
        return self.saldo == other.saldo

    def __lt__(self, other):
        return self.saldo < other.saldo
