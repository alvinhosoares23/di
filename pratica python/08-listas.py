'''
Listas Em Python
'''

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'
, 'Outubro', 'Novembro', 'Dezembro']
#fatiamento de lista
#imprime apartir do sexto mes print(meses[6:12])
#os 3 ultimos meses
for m in meses:
    print(m)
print(meses[-3:])
"""

mes = int(input('Escolha um mes (1-12) :'))
if mes > 0 and mes < 13:
    print(f'o mes que escolheste eh: {meses[mes-1]}')
else:
    print('Opcao invalido')
    
"""
#funcao append adiciona um elemento no fin da lista
lista1 = [1, 2]
lista1.append(3)
lista1.extend([4, 5, 6])
lista1 += [7]
print(lista1)
#funcao extend adiciona elementos no fina da lista


#Lista iteravel
lista = list('python')
print(lista)