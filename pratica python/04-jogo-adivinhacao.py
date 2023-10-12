#header
print('**********************************')
print('*     Jogo da adivinhação        *')
print('**********************************')

numero_secreto = 42
chute = int(input('Adivinhe o numero secreto :'))
print(f'Vc digitou {chute} ')

if chute == numero_secreto:
    print(f'voce Acertou o numero secreto eh ({numero_secreto})')
elif chute > numero_secreto:
    print('Errouuuuu! seu foi Maior que o numero secreto!')
elif chute < numero_secreto:
    print('Erouuuuuu! seu chute foi Menor que o numero secreto!')
else:
    print('Voce errou!')
