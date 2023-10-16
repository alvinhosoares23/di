'''

O Python também inclui um tipo de dados para conjuntos. Um conjunto, diferente de uma sequência,
56
CONJUNTOS é uma coleção não ordenada e que não admite elementos duplicados.
Chaves ou a função set() podem ser usados para criar conjuntos.

'''
frutas = {'laranja', 'banana', 'uva', 'pera', 'laranja', 'uva', 'abacate'}

a = set('abacate')
b = set('abacaxi')

#diferenca
print(a-b)
#uniao
print(a|b)
#intersessao
print(a&b)
#diferenca simetrica
print(a^b)