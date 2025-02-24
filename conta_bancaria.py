from usuario import Usuario
from conta_corrente import ContaCorrente
from conta_poupança import ContaPoupanca
from exceçoes import SaldoInsuficienteError, LoginInvalidoError

usuarios = {}

def criar_conta(usuario):
    print("\n=== Criar Conta ===")
    saldo = float(input("Digite o saldo inicial: "))

    print("\nEscolha o tipo de conta:")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")

    tipo = input("Opção: ")

    if tipo == "1":
        conta = ContaCorrente(usuario.nome, saldo)
    elif tipo == "2":
        conta = ContaPoupanca(usuario.nome, saldo)
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
        print("3 - Transferir")
        print("4 - Mostrar Saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            try:
                conta.sacar(valor)
            except SaldoInsuficienteError as e:
                print(e)

        elif opcao == "3":
            cpf_destino = input("Digite o CPF do destinatário: ")
            if cpf_destino in usuarios:
                valor = float(input("Digite o valor da transferência: "))
                try:
                    conta.transferir(usuarios[cpf_destino], valor)
                except SaldoInsuficienteError as e:
                    print(e)
            else:
                print("Conta destinatária não encontrada.")

        elif opcao == "4":
            print(conta)

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def main():
    print("=== Bem-vindo ao Sistema Bancário ===")

    while True:
        print("\n1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = Usuario.cadastrar()
            if usuario:
                usuarios[usuario.cpf] = usuario

        elif opcao == "2":
            try:
                usuario = Usuario.login()
                conta = criar_conta(usuario)
                if conta:
                    operacoes_conta(conta)
            except LoginInvalidoError as e:
                print(e)

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
