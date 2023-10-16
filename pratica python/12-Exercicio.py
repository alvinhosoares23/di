'''
5.5 EXERCÍCIOS: ESTRUTURA DE DADOS
Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,
-52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
print(lista)
#------------------------------------------------------------------------------------------
#a) imprima o maior elemento
maior = lista[0]
for l in lista:
    if maior <= l:
        maior = l

print('Maior : ', maior)
# ------------------------------------------------------------------------------------------
# b) imprima o menor elemento
menor = lista[0]
for j in lista:
    if menor >= j:
        menor = j

print('Menor: ', menor)
# ------------------------------------------------------------------------------------------
# c) imprima os elementos pares
print('Elementos Pares:')
for par in lista:
    if par % 2 == 0:
        print(par)

# ------------------------------------------------------------------------------------------
# d) imprima o número de ocorrências do primeiro elemento da lista
primeiroElemento = lista[0]
cont=0
for o in lista:
    if o == primeiroElemento:
        cont += 1

print(f'A ocorencia de {primeiroElemento} eh de :  {cont} vezes')

# ------------------------------------------------------------------------------------------
# e) imprima a média dos elementos
numElemento = len(lista)
somatorio = 0
for i in lista:
    somatorio = somatorio + i
media = somatorio/numElemento
print(f'A media dos elemntos eh de {media}')

# ------------------------------------------------------------------------------------------
# f) imprima a soma dos elementos de valor negativo
negaElemento = len(lista)
somaNega = 0
for n in lista:
    if n < 0:
        somaNega += n
print(f'A Soma dos elemntos Negativos eh de {somaNega}')