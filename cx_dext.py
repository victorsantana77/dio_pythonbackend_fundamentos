menu = """

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
!     MENU DE OPÇÕES     !
__________________________
![d] Depositar           !
![s] Sacar               !
![e] Extrato             !               
![q] Sair                !
__________________________

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    opcao = input(menu)
    
    
    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))
        
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de {valor:.2f}\n"
            
        else:
            print("Valor inválido")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo 
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente.")
        
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
            
    elif opcao == "e":
        print("\n=======================EXTRATO=======================")
        print("Não foram realizadas movimenttações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=====================================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione uma das operações.")