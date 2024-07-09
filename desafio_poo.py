import textwrap
from datetime import datetime

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self.cliente = cliente
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            print("Saldo insuficiente para saque.")

    def exibir_extrato(self):
        print("\n=======================EXTRATO=======================")
        if not self.historico:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico:
                print(transacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=====================================================")

def menu():
    menu = """\n
    *   *    *     *                                                                    
    * 24 HORAS *
    *    *   *    *
    __________________________
    !     MENU DE OPÇÕES      !
    __________________________
    ![d]\tDepositar           !
    ![s]\tSacar               !
    ![e]\tExtrato             ! 
    ![nu]\tNovo Usuário       !
    ![nc]\tNova Conta         !
    ![lc]\tListar Contas      !               
    ![q]\tSair                !
    __________________________

    => """
    return input(textwrap.dedent(menu))

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    endereco = input("Informe o endereço: ")
    return cpf, nome, endereco

def criar_conta(cliente):
    agencia = "0001"  # Agência padrão
    numero = len(cliente.contas) + 1  # Número de conta sequencial
    return Conta(cliente, numero, agencia)

def exibir_contas(cliente):
    print("\n=================== LISTA DE CONTAS ===================")
    if cliente.contas:
        for conta in cliente.contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero}")
    else:
        print("Nenhuma conta encontrada para este cliente.")
    print("=======================================================")

def main():
    clientes = []

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                valor = float(input("Informe o valor do depósito: "))
                cliente.contas[0].depositar(valor)  # Simula depósito na primeira conta do cliente
            else:
                print("Cliente não encontrado.")

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                valor = float(input("Informe o valor do saque: "))
                cliente.contas[0].sacar(valor)  # Simula saque na primeira conta do cliente
            else:
                print("Cliente não encontrado.")

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                cliente.contas[0].exibir_extrato()  # Exibe extrato da primeira conta do cliente
            else:
                print("Cliente não encontrado.")

        elif opcao == "nu":
            cpf, nome, endereco = criar_usuario()
            novo_cliente = Cliente(cpf, nome, endereco)
            clientes.append(novo_cliente)
            print("Usuário criado com sucesso!")

        elif opcao == "nc":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                nova_conta = criar_conta(cliente)
                cliente.adicionar_conta(nova_conta)
                print("Conta criada com sucesso!")
            else:
                print("Cliente não encontrado.")

        elif opcao == "lc":
            cpf = input("Informe o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                exibir_contas(cliente)
            else:
                print("Cliente não encontrado.")

        elif opcao == "q":
            break

        else:
            print("Opção inválida. Por favor, selecione uma das operações disponíveis.")

if __name__ == "__main__":
    main()
