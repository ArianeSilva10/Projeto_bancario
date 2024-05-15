######################## SAQUE ########################################

def saque(*, saldo,valor_saque, extrato, limite, numero_saques, LIMITE_SAQUES):
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
        return saldo, extrato


####################### DEPOSITO #####################################

def deposito(saldo, valor, extrato, /):
    valor += float(input('''
DEPÓSITO
Qual o valor deseja depositar?
'''))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito : R$ {saldo:.2f}\n"
        print("depositado com sucesso!")
        return saldo, extrato
    
    else:
         print("Valor inválido, por favor tente novamente.")


########################## EXTRATO ############################

def extrato(saldo, /,*, extrato):
    print("================= EXTRATO ==================")
    if extrato == "":
        print("Não foram realizadas movimentações.")

        print(extrato)
        print(f"Saldo atual: {saldo:.2f}\n")
        print("===========================================")
    return extrato


######################## FILTRAR USUÁRIO #########################

def filtrar_usuario(cpf, lista_usuarios):
    cpf_existente = {usuario['CPF'] == cpf for usuario in lista_usuarios}
    if cpf_existente:
        return cpf_existente[0]
    else:
        return None


######################## CRIAR USUARIO #########################

def criar_usuario(lista_usuarios):
    usuario =  {
        "nome": input("Nome: "),
        "data_de_nascimento": input("Data de Nascimento: "),
        "CPF": input("CPF: "),
        "endereco": input("Endereço: ")
    }
    cpf_existente = filtrar_usuario(usuario["CPF"], lista_usuarios) # crio um set de CPFs já que não pode repetir,  percorrendo cada usuario na lista.
    if cpf_existente:
        print("Usuário já cadastrado neste CPF!")
    else:
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!")


######################## CRIAR CONTA CORRENTE #########################

def criar_conta_corrente(AGENCIA, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, lista_usuarios)

    if usuario:
        print("Conta criada com Sucesso!")
        return {"agencia" : AGENCIA, "numero_conta":numero_conta, "usuario":usuario}
    else:
        print("Usuário não encontrado, se deseja criar um usuário, volte ao menu e escolha a opção 'Novo Usuário'.")


######################## CRIAR CONTA CORRENTE #########################

def listar_contas(lista_contas, lista_usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, lista_usuarios)


menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Sair

=> '''


lista_contas = []
AGENCIA = 0001
lista_usuarios = []

while True:
    opcao  = input(menu)

    if opcao == "1":
        deposito(0, 0, "")

    elif opcao == "2":
        saque(saldo=0, valor_saque=0, extrato="", limite=500, numero_saques=0, LIMITE_SAQUES=3)

    elif opcao == "3":
        extrato(0, extrato="")

    elif opcao == "4":
        numero_conta = len(lista_contas) + 1
        conta_usuario = criar_conta_corrente(AGENCIA, numero_conta, lista_usuarios)

        if conta_usuario:
            lista_contas.append(conta_usuario)

    elif opcao == "6":
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desjada.")