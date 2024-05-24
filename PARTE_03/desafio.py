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

    def adicionar_conta(conta):
        pass


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


class Transacao(Cliente):
    def registrar(Conta):
        pass


class Historico:
    def adicionar_transacao(transacao):
        pass
