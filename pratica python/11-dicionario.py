'''
Dicionário é outra estrutura de dados em Python e seus elementos, sendo
estruturadas de forma não ordenada assim como os conjuntos. Ainda assim, essa não é a principal
diferença com as listas. Os dicionários são estruturas poderosas e muito utilizadas, já que podemos
acessar seus elementos através de chaves e não por sua posição.

Os dicionários são delimitados por chaves ({}) e suas chaves ('nome', 'idade' e 'cidade') por aspas. Já
os valores podem ser de qualquer tipo. No exemplo acima, temos duas strings e um int .
'''

pessoa = {'nome': 'Joao', 'idade': 25, 'cidade': 'Praia'}
pessoa['país'] = 'Cabo Verde'

print(pessoa.values)