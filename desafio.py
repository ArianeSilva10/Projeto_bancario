menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao  = input(menu)

    if opcao == "1":
        saldo += float(input('''
DEPÓSITO
Qual o valor deseja depositar?
'''))
        extrato += f"Depósito : R$ {saldo:.2f}\n"
        print("Valor desejado depositado com sucesso!")

    elif opcao == "2":
        print("SAQUE",end="")
        if numero_saques == LIMITE_SAQUES:
                print("\nLimite de Saque atingido. Tente novamente no dia seguinte.")
        else:
            valor_saque = float(input('''
Qual o valor que deseja sacar?
'''))
            if saldo >= valor_saque:
                if valor_saque <= limite:
                    print("Saque realizado com sucesso!")
                    numero_saques += 1
                    saldo -= valor_saque
                    extrato += f"Saque : R$ {valor_saque:.2f}\n"
                else:
                    print("Valor acima do limite! Por favor tente novamente.")
            else:
                print("Não foi possível realizar o saque por falta de saldo.")

    elif opcao == "3":
        print("EXTRATO")
        if extrato == "":
            print("Não foram realizadas movimentações.")

        extrato += f"Saldo atual: {saldo:.2f}\n"
        print(extrato)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desjada.")