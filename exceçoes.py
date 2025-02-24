class SaldoInsuficienteError(Exception):
    """Erro para saldo insuficiente em operações bancárias."""
    def __init__(self, mensagem="Erro: Saldo insuficiente para a operação."):
        super().__init__(mensagem)

class LoginInvalidoError(Exception):
    """Erro para login inválido."""
    def __init__(self, mensagem="Erro: CPF ou senha incorretos."):
        super().__init__(mensagem)