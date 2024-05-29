from abc import ABC,  abstractclassmethod, abstractproperty


class Pessoa:
    def __init__(self, cpf, nome, data_nascimento) -> None:
        self._cpf = cpf 
        self._nome = nome 
        self._data_nascimento = data_nascimento 


class Cliente(Pessoa):
    def __init__(self, endereco,**kw) -> None:
        super().__init__(**kw)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        conta.nova_conta(Cliente, numero=0)


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    

    def sacar(self, valor):
        saldo = self._saldo
        limite_saldo = valor > saldo

        if limite_saldo:
            print("Valor acima do saldo!")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        else:
            print("Valor inválido!")
            return False


    def  depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"{valor} depositado com sucesso!")
            return True
        
        else:
            print("Valor inválido!")
            return False


class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, LIMITE=500, LIMITE_SAQUE=3) -> None:
        super().__init__(numero, cliente)
        self.limite = LIMITE
        self.limite_saques = LIMITE_SAQUE


    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        acima_limite = valor > self.limite
        acima_limite_saque = numero_saque >= self.limite_saques

        if acima_limite:
            print("Valor acima do saldo!")

        elif acima_limite_saque:
            print("Número máximo de saques diário atingido! Por favor, tente outro dia")

        else:
            return super().sacar(valor)
        

    def __str__(self) -> str:
        return f'''
            Agência:      {self._agencia}
            C/C:          {self._numero}
            Titular:      {self._cliente.nome}
        '''


class Transacao(Cliente):
    def registrar(self,Conta):
        pass

class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, Transacao):
        self._transacoes.append(
            {
                "tipo": Transacao.__class__.__name__,
                "Valor": Transacao.valor
                }
            )

class Saque(Transacao):
    def __init__(self, valor) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        concluida_transacao = conta.sacar(self.valor)

        if concluida_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        super().__init__()
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        concluida_transacao = conta.depositar(self.valor)
        if concluida_transacao:
            conta.historico.adicionar_transacao(self)
    