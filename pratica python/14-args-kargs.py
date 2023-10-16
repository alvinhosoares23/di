'''
*args . É usado, assim como o **kwargs , em definições de
funções. *args e **kwargs permitem passar um número variável de argumentos de uma função. O
que a variável significa é que o programador ainda não sabe de antemão quantos argumentos serão
passados para sua função, apenas que são muitos. Então, neste caso usamos a palavra chave *args .
'''

def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))

teste('python', 'é', 'muito', 'legal')

lista = ["é", "muito", "legal"]
teste('python', *lista)

tupla = ("é", "muito", "legal")
teste('python', *tupla)
'''
O **kwargs permite que passemos o tamanho variável da palavra-chave dos argumentos para uma
função. Você deve usar o **kwargs se quiser manipular argumentos nomeados em uma função.
Também podemos passar um dicionário acrescido de dois asteriscos, já que se trata de chave e valor
A diferença é que o *args espera uma tupla de argumentos posicionais, enquanto o **kwargs um
dicionário com argumentos nomeados.
'''

def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

minha_funcao(nome='caelum')