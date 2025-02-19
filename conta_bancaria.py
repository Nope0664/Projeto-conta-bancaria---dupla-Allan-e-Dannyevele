from conta_corrente import ContaCorrente
from conta_poupança import ContaPoupanca

def criar_conta():
    print("\n=== Criar Nova Conta ===")
    titular = input("Digite o nome do titular: ")
    saldo = float(input("Digite o saldo inicial: "))
    
    print("\nEscolha o tipo de conta:")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    
    tipo = input("Opção: ")

    if tipo == "1":
        conta = ContaCorrente(titular, saldo)
    elif tipo == "2":
        conta = ContaPoupanca(titular, saldo)
    else:
        print("Opção inválida!")
        return None

    print("\nConta criada com sucesso!")
    print(conta)
    return conta

def operacoes_conta(conta):
    while True:
        print("\n=== Operações Disponíveis ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Mostrar Saldo")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            try:
                conta.sacar(valor)
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            print(conta)

        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

def main():
    print("=== Bem-vindo ao Sistema Bancário ===")
    
    conta = criar_conta()
    
    if conta:
        operacoes_conta(conta)

if __name__ == "__main__":
    main()