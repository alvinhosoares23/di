print('**********************************')
print('*     Jogo da adivinhação        *')
print('**********************************')

palavra_secreta = 'banana'
palavra_adivinhada = ['-'] * len(palavra_secreta)
tentativas = 6
print(f'Descubra A Palavra-Secreta : {palavra_adivinhada}')
while True:
    chute = input("Digite uma letra: ").lower()
    if chute in palavra_secreta:
        posicao = 0

        for letra in palavra_secreta:
            if chute == letra:
                print(f' Encontadoa a letra({letra}) na posicao ({posicao+1})')
                palavra_adivinhada[posicao] = letra

            posicao += 1
    else:
        tentativas -= 1
        print()
        print('******************************************************')
        print(f'A letra ({chute}) nao esta na palavra secreta hahahahahah....')
        print(f'({tentativas}) tentativas Restantes ')
    if not '-' in palavra_adivinhada:
        print('**********************************')
        print(f'   palavra-Secreta :{palavra_secreta}')
        print('**********************************')
        print('*     Voce foi Poupado :-)       *')
        print('*          Fim Do Jogo           *')
        print('**********************************')
        break
    if tentativas == 0:
        print('**********************************')
        print(f'*   Voce Perdeu hahahahaha       *')
        print('**********************************')
        print('*     Voce foi Enforcado :-)     *')
        print('*          GAME OVER             *')
        print('**********************************')
        break
    print('******************************************************')
    print('            tic-tac, tic-tac...   ')
    print('******************************************************')
    print('')
    print(f'Palavras Acertadas: {palavra_adivinhada}')

