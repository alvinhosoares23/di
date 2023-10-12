"""
Aula 01 Modulo 01
"""
print('qual eh seu Nome?')
nome = input()

print('seja bem-vindo {0}.'.format(nome))

idade = input('Qual a sua idade : ')

#exemplo de print recente
print(f'O {nome} tem {idade} anos de idade!')

#exemplo de print Moderno
print('O {0} tem {1} anos de idade!'.format(nome, idade))


