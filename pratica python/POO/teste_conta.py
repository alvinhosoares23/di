def criar_conta(id, titular, saldo, limite):
    conta = {'id': id, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta,valor):
    conta['saldo'] += valor


def sacar(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'ID: {conta["id"]}  ')
    print(f'Saldo: {conta["saldo"]}')


conta = criar_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta,500)
extrato(conta)

sacar(conta,50)
extrato(conta)