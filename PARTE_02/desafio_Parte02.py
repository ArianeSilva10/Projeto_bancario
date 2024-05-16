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
    for usuario in lista_usuarios:
        if usuario['CPF'] == cpf:
            cpf_existente = usuario

            if cpf_existente:
                return cpf_existente
    else:
        return None


######################## CRIAR USUARIO #########################

def criar_usuario(lista_usuarios):
    # recolhe os dados para a criação do usuário(dicionario)
    usuario =  {
        "nome": input("Nome: "),
        "data_de_nascimento": input("Data de Nascimento: "),
        "CPF": input("CPF: "),
        "endereco": input("Endereço: ")
    }
    cpf_existente = filtrar_usuario(usuario["CPF"], lista_usuarios) # crio um set de CPFs já que não pode repetir,  percorrendo cada usuario na lista.

    # verifico se este usuário já está cadastrado
    if cpf_existente:
        print("Usuário já cadastrado neste CPF!")

    else:
        # se não estiver, impõe o novo usuario na lista de usuários
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!")


######################## CRIAR CONTA CORRENTE #########################

def criar_conta_corrente(AGENCIA, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, lista_usuarios)
    # faço a busca do usuário para o qual desejo criar a conta

    if usuario:
        print("Conta criada com Sucesso!")
        return {"agencia" : AGENCIA, "numero_conta":numero_conta, "usuario":usuario}
    else:
        print("Usuário não encontrado, se deseja criar um usuário, volte ao menu e escolha a opção 'Novo Usuário'.")


######################## LISTA DE CONTAS  #########################
# função para listar as contas do usuário

def listar_contas(lista_contas):
    for conta in lista_contas:
        conta_percorrida = f'''
==========================================
AGÊNCIA : {conta['agencia']}
C / CC : {conta['numero_conta']}
TITULAR : {conta['usuario']['nome']}
'''
        print(conta_percorrida)


menu = '''
================ MENU ====================

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Listar Contas
[7] Sair

=> '''


lista_contas = []
AGENCIA = "0001"
lista_usuarios = []
saldo = 0
LIMITE_VALOR_SAQUE = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao  = input(menu)

    if opcao == "1": # DEPOSITAR
        valor = float(input('''
DEPÓSITO
Qual o valor deseja depositar?
'''))
        saldo, extrato = deposito(saldo, valor, extrato)


    elif opcao == "2": # SACAR
        saldo, extrato = saque(saldo=saldo, valor_saque=0, extrato=extrato, limite=LIMITE_VALOR_SAQUE, numero_saques=numeros_saques, LIMITE_SAQUES=LIMITE_SAQUES)


    elif opcao == "3": # EXTRATO
        extrato(saldo, extrato=extrato)

    elif opcao == "4": # CRIAR USUÁRIO
        criar_usuario(lista_usuarios)


    elif opcao == "5": # CRIAR CONTA CORRENTE
        numero_conta = len(lista_contas) + 1
        conta_usuario = criar_conta_corrente(AGENCIA, numero_conta, lista_usuarios)

        if conta_usuario:
            lista_contas.append(conta_usuario)

    elif opcao == "6": # LISTAR CONTAS
        listar_contas(lista_contas)


    elif opcao == "7": # SAIR
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desjada.")