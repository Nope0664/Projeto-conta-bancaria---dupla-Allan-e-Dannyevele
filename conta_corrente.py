from conta import Conta
from exceçoes import SaldoInsuficienteError

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self._limite = limite

    def sacar(self, valor):
        if valor > (self._saldo + self._limite):
            raise SaldoInsuficienteError("Erro: Saque maior que o saldo e limite disponíveis.")
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso! (Conta Corrente)")
