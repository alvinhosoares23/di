'''
Uma tupla é uma lista imutável, ou seja, uma tupla é uma sequência que não pode ser alterada
depois de criada. Uma tupla é definida de forma parecida com uma lista com a diferença do delimitador.
Enquanto listas utilizam colchetes como delimitadores, as tuplas usam parênteses
'''

diasSemana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')

#Não é possível atribuir valores aos itens individuais de uma tupla, no entanto, é possível criar tuplas que contenham objetos mutáveis, como listas.
lista = [3, 4, 5]
tupla = (1, 2, lista)
#print(tupla)
for listar in tupla:
    print(listar)