class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem="Saldo insuficiente para a operação."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)