import jogo_da_forca
import jogo_adivinhacao


def menu():
    print('*********************************')
    print('**********MENU DE JOGOS**********')
    print('*********************************')
    print("*    1->  Adivinhação           *")
    print("*    2->    Forca               *")
    print("*    3->    Sair                *")
    print('*********************************')


menu()
escolha = int(input("Qual jogo quer jogar? Digite o número: "))

while escolha > 0 and escolha < 3:

    if escolha == 1:
        jogo_adivinhacao.jogar()
    elif escolha == 2:
        jogo_da_forca.jogar()
    menu()
    escolha = int(input("Qual jogo quer jogar? Digite o número: "))