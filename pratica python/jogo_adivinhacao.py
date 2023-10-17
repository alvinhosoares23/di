import random

def jogar():
    print('**********************************')
    print('*     Jogo da adivinhação        *')
    print('*    OBS : Numero de [0-100]     *')
    print('**********************************')

    numero_secreto = random.randrange(0,100)

    tentativa = 8

    for i in range(0, 8):

        chute = int(input('Adivinhe o numero secreto :'))
        print(f'Vc digitou {chute} ')
        if chute == numero_secreto:
            print(f'voce Acertou o numero secreto eh ({numero_secreto})')
            print('fim Do Jogo !!')
            break
        elif chute > numero_secreto:
            print(f'Errouuuuu! seu chute foi Maior que o numero secreto!')
        elif chute < numero_secreto:
            print('Erouuuuuu! seu chute foi Menor que o numero secreto!')
        else:
            print('Voce errou!')

        tentativa -= 1
        print('**********************************')
        print(f'***** {(tentativa)} tentativas Restante ******')
        print('**********************************')

        if tentativa == 0:
            print('----------------------------------------------')
            print('| Tentativas Esgotadas!!! Voce Perdeu kkkkkkk|')
            print('----------------------------------------------')