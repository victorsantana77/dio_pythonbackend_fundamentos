import textwrap



    
def menu():
     menu = """\n

    d8888b.  .d8b.  d8b   db  .o88b.  .d88b.    d8888b. d88888b db    db d888888b 
    88  `8D d8' `8b 888o  88 d8P  Y8 .8P  Y8.   88  `8D 88'     `8b  d8' `~~88~~' 
    88oooY' 88ooo88 88V8o 88 8P      88    88   88   88 88ooooo  `8bd8'     88    
    88~~~b. 88~~~88 88 V8o88 8b      88    88   88   88 88~~~~~  .dPYb.     88    
    88   8D 88   88 88  V888 Y8b  d8 `8b  d8'   88  .8D 88.     .8P  Y8.    88    
    Y8888P' YP   YP VP   V8P  `Y88P'  `Y88P'    Y8888D' Y88888P YP    YP    YP    
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

    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de {valor:.2f}\n"
            
    else:
        print("Valor inválido")
            
    return saldo, extrato
    
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
        
    excedeu_limite = valor > limite
        
    excedeu_saques = numero_saques >= limite_saques
        
    if excedeu_saldo:
            print("Saldo insuficiente, Verifique o saldo de sua conta.")
        
    elif excedeu_limite:
            print("Valor do saque maior que o limite.")
            
    elif excedeu_saques:
            print("Número de saques excedeu o limite.")
            
        
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque de {valor:.2f}\n"
            numero_saques += 1
            
    else:
            print("Valor informado inválido.")
            
    return saldo, extrato


def exibir_extrato(saldo, extrato):  
    
    print("\n=======================EXTRATO=======================")
    print("Não foram realizadas movimenttações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=====================================================")  
    

def criar_usuario(usuarios):
    cpf = input("Informme o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF!@@@")
        return
        
    nome = input("Informe o nome completo:")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouron, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado!!!")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
       print("\nConta criada!!!")
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado!!!")
    
def exibir_contas(contas):
    for conta in contas:
        linha = f"""\
            Agêencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
    
    
def main():  
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        
        if opcao == "d":
            valor = float(input("informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
                        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "lc":
            exibir_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("Opção inválida, por favor selecione uma das operações.")
        
main()