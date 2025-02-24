from conta import Conta

class ContaPoupanca(Conta):
    def render_juros(self, taxa=0.05):
        self._saldo += self._saldo * taxa
        print(f"Juros de {taxa * 100:.0f}% aplicados! Novo saldo: R${self._saldo:.2f}")
