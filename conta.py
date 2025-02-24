from exceçoes import SaldoInsuficienteError

class Conta:
    def __init__(self, titular, saldo=0):
        self._titular = titular  
        self._saldo = saldo  

    def sacar(self, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente.")
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def transferir(self, destino, valor):
        if valor > self._saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para a transferência.")
        self._saldo -= valor
        destino._saldo += valor
        print(f"Transferência de R${valor:.2f} realizada com sucesso!")

    def __str__(self):
        return f"Titular: {self._titular} | Saldo: R${self._saldo:.2f}"
