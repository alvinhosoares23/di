def criar_arquivo():
    arquivo=open('palavra_secreta.txt', 'w')
    arquivo.write('Banana\n')
    arquivo.write('Melancia\n')
    arquivo.write('Arroz\n')
    arquivo.write('Abacate\n')
    arquivo.close()


def escrever_arquivo(palavra):
    arquivo = open('palavra_secreta.txt','a')
    arquivo.write(palavra+'\n')
    arquivo.close()


def ler_arquivo():
    arquivo = open('palavra_secreta.txt','r')
    print('_________________________________________')
    print('|       Lista de Palavras Secretas      |')
    print('_________________________________________')
    for linha in arquivo:
        print(f'   -> {linha}')
    arquivo.close()
    print('_________________________________________')


#criar_arquivo()
#pala = input('Escreva a palavra :')
#escrever_arquivo(pala)

ler_arquivo()