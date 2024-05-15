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

def deposito( / saldo, valor, extrato):
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

######################### LISTA DE USUÁRIOS ######################
#def lista_usuario():
 #    lista = []



######################## CRIAR USUARIO #########################

def criar_usuario(lista_usuarios = []):
    usuario =  {
        "nome": input("Nome: "),
        "data_de_nascimento": input("Data de Nascimento: "),
        "CPF": input("CPF: "),
        "endereco": input("Endereço: ")
    }
    cpf_existente = {user['CPF'] for user in lista_usuarios} # crio um set de CPFs já que não pode repetir,  percorrendo cada usuario na lista.
    if usuario['CPF'] not in cpf_existente:
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!")
    else:
        print("Usuário já cadastrado neste CPF!")


######################## CRIAR CONTA CORRENTE #########################

def criar_conta_corrente(lista_de_contas = [], lista_de_usuarios = []):
    AGENCIA = 0001




menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''


while True:
    opcao  = input(menu)

####################### DEPOSITO #####################################

    if opcao == "1":
        deposito(0, 0, "")

######################## SAQUE ########################################

    elif opcao == "2":
        saque(saldo=0, valor_saque=0, extrato="", limite=500, numero_saques=0, LIMITE_SAQUES=3)

#######################################################################


########################## EXTRATO ############################

    elif opcao == "3":
        extrato(0, extrato="")


#################################################################

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desjada.")