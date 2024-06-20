
menu ="""
Sistema Bancario \n Escolha a opção que deseja relizar a operação
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair        
=>  """

erro = "Operação encerada"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        if saldo == 0:
            print("Infelizmente não possui saldo! Por favor, realize o deposito para sacar!")
            break

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print(f"\nSaldo R$ {saldo:.2f} inferior ao valor R$ {valor:.2f} desejado")
            print(erro.upper())
            break

        if excedeu_limite:
            print("Operação falhou! O valor máximo para saque por dia é de 500.00 reais.")
            print(erro.upper())
            break

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n ********* Extrato ******** ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")