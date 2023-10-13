print('**********************************')
print('*     Jogo da adivinhação        *')
print('**********************************')

numero_secreto = 42

chute = 0
tentativa = 5

for i in range(0, 5):

    chute = int(input('Adivinhe o numero secreto :'))
    print(f'Vc digitou {chute} ')
    if chute == numero_secreto:
        print(f'voce Acertou o numero secreto eh ({numero_secreto})')
        print('fim Do Jogo !!')
        break
    elif chute > numero_secreto:
        print('Errouuuuu! seu foi Maior que o numero secreto!')
    elif chute < numero_secreto:
        print('Erouuuuuu! seu chute foi Menor que o numero secreto!')
    else:
        print('Voce errou!')

    tentativa -= 1
    print('**********************************')
    print(f'***** {(tentativa)} tentativas Restante ******')
    print('**********************************')

    if tentativa ==0:
        print('----------------------------------------------')
        print('| Tentativas Esgotadas!!! Voce Perdeu kkkkkkk|')
        print('----------------------------------------------')

print('fim Do Jogo !!')
