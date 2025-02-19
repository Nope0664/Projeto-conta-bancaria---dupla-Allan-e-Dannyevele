from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            raise ValueError("Saldo insuficiente considerando o limite do cheque especial.")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso! (Conta Corrente)")