#funcao que calcula a velocidade
def velocidade(espaco,tempo):
    v = espaco/tempo
    print(f'Velocidade : {v} m/s')


velocidade(1000,240)


def calculadora(x, y):
    return {'soma':x+y, 'subtração':x-y}


resultados = calculadora(1, 2)

for key in resultados:
    print('{}: {}'.format(key, resultados[key]))

def calculadora(x,y):
    soma = x+y
    sub = x-y
    mult = x*y
    div = x/y
    return {'soma':soma, 'subtracao': sub, 'multiplicacao':mult, 'divisao' : div  }


calcula = calculadora(20,7)
for k in calcula:
    print(f'{k}  {calcula[k]}')

