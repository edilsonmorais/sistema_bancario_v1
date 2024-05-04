menu = """
--------- MENU ---------------    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
==>
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
opcao = ""

def depositar(valor):
    global extrato

    if valor > 0:
        global saldo 
        saldo = saldo + valor
        deposito = str(valor)       
        extrato.append(f"Deposito de R$ {deposito}")
    else:
        print("\nValor inválido para depósito.")

def sacar(valor):
    global numero_saques, saldo, extrato

    if valor > 500:
        print("\nSaque não permitido. Limite de saque é R$ 500,00.")
    elif valor <= saldo and valor > 0:
        if numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1      
            saque = str(valor)       
            extrato.append(f"Sacou R$ {saque}")                  
            print('\nSaque realizado com sucesso!')
        else:
            print('\nVocê já fez o número máximo de saques diários. Tente novamente amanhã!')
    elif valor <= 0:
        print("\nValor inválido para saque.")
    elif valor > saldo:
        print('\nSaldo insuficiente para saques')

def extrato_conta():
    global extrato
    print("Exibindo extrato...\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:           
            print(movimentacao)
    print(f"\nSaldo Total R$ {saldo:.2f}")
             
while True:   
    opcao = input(menu).lower()
    
    if opcao == "d":        
        print("Insira o valor a ser depositado: ", end="")
        valor = float(input())
        depositar(valor)        
    elif opcao == "s":
        print("Saque de quanto: ", end="")
        v = float(input())
        sacar(v)        
    elif opcao == "e":        
        extrato_conta()        
    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Operação inválida!")

print(f"\n\nSaldo Total R$ {saldo:.2f}")