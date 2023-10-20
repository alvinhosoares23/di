import datetime


class Movimento:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        print('*******************************************')
        print('*************   Transacoes  ***************')
        data = datetime.datetime.today()
        for t in self.transacoes:
            print('  + ', t, '------ Data : ', data)


class Cliente:
    def __init__(self, bi, nome, sobrenome):
        self.bi = bi
        self.nome = nome
        self.sobrenome = sobrenome


class Conta:
    cod = 101

    def __init__(self, cliente, saldo, limite=1000):
        print('Criando uma Nova Conta')
        self.__cod = Conta.cod
        self.__titular = cliente
        self.__saldo = saldo
        self.__limite = limite
        self.__movimento = Movimento()
        Conta.cod += 1

    def depositar_conta(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'{valor}$ Depositado com sucesso!')
            self.__movimento.transacoes.append(f'Deposito de {valor}')
        else:
            print(f'Valor precissa ser positivo')
    def extrato(self):
        print('*******************************************')
        print('***************  Extrato  *****************')
        print(f'  + ID      : {self.__cod}')
        print(f'  + Titular : {self.__titular.nome} {self.__titular.sobrenome}')
        print(f'  + Saldo   : {self.__saldo}')
        print('*******************************************')
        self.__movimento.transacoes.append('Extrado')

    def sacar(self, valor):
        if self.__saldo < valor:
            print('Saldo insuficiente!')
            return False
        else:
            self.__saldo -= valor
            print(f'{valor}$ Sacado com sucesso!')

            self.__movimento.transacoes.append(f'Saque de {valor}')
            return True

    def transferir(self, conta_destino, valor):
        if self.__saldo < valor:
            print('Saldo insuficiente!')
            return False
        else:
            self.__saldo -= valor
            conta_destino.depositar_conta(valor)
            print(f'{valor}$ Transferido para {conta_destino.__titular.nome} com sucesso!')
            self.extrato()
            self.__movimento.transacoes.append(f'Transferencia {valor}$ para {conta_destino.__titular.nome}')

    def imprimir_movimento(self):
        self.__movimento.imprime()


cliente = Cliente('0048', 'Joao', 'Dos Santos')
cliente2 = Cliente('0042', 'Maria', 'Brito')
conta = Conta(cliente, 120.0 )
conta.depositar_conta(900)
conta.sacar(100)

c1 = Conta(cliente2, 400)
# conta.transferir(c1,50)
c1.depositar_conta(100)
conta.transferir(c1, 50)

conta.imprimir_movimento()
c1.imprimir_movimento()
c1.extrato()
