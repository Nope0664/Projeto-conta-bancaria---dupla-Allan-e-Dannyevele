

from banco import Banco
from cliente import Cliente
from validação import validar_cpf, validar_telefone, validar_email, validar_endereco

def menu():
    banco = Banco()

    while True:
        print("\n=== Banco Interativo ===")
        print("1 - Criar Conta")
        print("2 - Acessar Conta")
        print("3 - Transferir entre Contas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta(banco)
        elif opcao == "2":
            acessar_conta(banco)
        elif opcao == "3":
            transferir_contas(banco)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def criar_conta(banco):
    print("\n--- Criar Conta ---")
    
    nome = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF (somente números): ")
    telefone = input("Digite o telefone (somente números): ")
    email = input("Digite o e-mail: ")
    endereco = input("Digite o endereço (rua, número, cidade): ")
    
    
    erros = []
    if not validar_cpf(cpf):
        erros.append("CPF inválido! Deve conter exatamente 11 números.")
    if not validar_telefone(telefone):
        erros.append("Telefone inválido! Deve conter pelo menos 8 dígitos numéricos.")
    if not validar_email(email):
        erros.append("E-mail inválido! Deve conter um '@' e um domínio válido.")
    if not validar_endereco(endereco):
        erros.append("Endereço inválido! Deve conter pelo menos 5 caracteres.")
    
    if erros:
        print("\nErro ao criar conta:")
        for erro in erros:
            print(erro)
    else:
        tipo_conta = input("Tipo de conta (corrente/poupanca): ").lower()
        if tipo_conta not in ["corrente", "poupanca"]:
            print("Tipo de conta inválido.")
            return
        
        numero_conta = str(len(banco.contas) + 1000)  
        cliente = Cliente(nome, cpf, telefone, email, endereco)
        
        # Perguntar o saldo inicial
        saldo_inicial = input("Digite o saldo inicial da conta: R$")
        saldo_inicial = float(saldo_inicial.replace(",", "."))  # Substitui vírgula por ponto e converte para float
        
        banco.criar_conta(numero_conta, tipo_conta, cliente, saldo_inicial)
        
        print(f"\nConta {tipo_conta} criada com sucesso para {nome}!")
        print(f"Número da conta: {numero_conta}")
        print(f"Saldo inicial: R${saldo_inicial:.2f}")

def acessar_conta(banco):
    print("\n--- Acessar Conta ---")
    numero_conta = input("Digite o número da conta: ")
    conta = banco.buscar_conta(numero_conta)
    
    if conta:
        print(f"Conta encontrada! Titular: {conta.cliente.nome}")
        print(f"Tipo de conta: {conta.tipo}")
        print(f"Saldo: R${conta.saldo:.2f}")
    else:
        print("Conta não encontrada.")

def transferir_contas(banco):
    print("\n--- Transferir entre Contas ---")
    numero_conta_origem = input("Digite o número da conta de origem: ")
    numero_conta_destino = input("Digite o número da conta de destino: ")
    valor = input("Digite o valor da transferência: R$")
    valor = float(valor.replace(",", "."))  
    
    conta_origem = banco.buscar_conta(numero_conta_origem)
    conta_destino = banco.buscar_conta(numero_conta_destino)
    
    if conta_origem and conta_destino:
        if conta_origem.saldo >= valor:
            banco.transferir(conta_origem, conta_destino, valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
            print(f"Novo saldo de {conta_origem.cliente.nome}: R${conta_origem.saldo:.2f}")
            print(f"Novo saldo de {conta_destino.cliente.nome}: R${conta_destino.saldo:.2f}")
        else:
            print("Saldo insuficiente na conta de origem.")
    else:
        print("Uma ou ambas as contas não foram encontradas.")

if __name__ == "__main__":
    menu()
