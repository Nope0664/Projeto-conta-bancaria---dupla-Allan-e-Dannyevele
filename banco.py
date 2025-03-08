from conta import ContaCorrente, ContaPoupanca
from cliente import Cliente

class Banco:
    def __init__(self):
        self.__contas = {}  

    def criar_conta(self, numero_conta, tipo_conta, cliente, saldo_inicial):
        """Cria uma conta (corrente ou poupança) e armazena em memória."""
        dados_conta = {
            "titular": cliente.get_nome(),
            "cpf": cliente.get_cpf(),
            "telefone": cliente.get_telefone(),
            "email": cliente.get_email(),
            "endereco": cliente.get_endereco(),
            "tipo": tipo_conta,
            "saldo": saldo_inicial
        }
        self.__contas[numero_conta] = dados_conta

    def buscar_conta(self, numero):
        """Busca uma conta pelo número e retorna a conta correspondente."""
        numero = str(numero)  
        if numero in self.__contas:
            dados = self.__contas[numero]
            cliente = Cliente(dados["titular"], dados["cpf"], dados["telefone"], dados["email"], dados["endereco"])
            if dados["tipo"] == "corrente":
                conta = ContaCorrente(numero, cliente)
            elif dados["tipo"] == "poupanca":
                conta = ContaPoupanca(numero, cliente)
            conta.set_saldo(dados["saldo"])
            return conta
        return None

    def transferir(self, conta_origem, conta_destino, valor):
        """Realiza a transferência entre duas contas."""
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
