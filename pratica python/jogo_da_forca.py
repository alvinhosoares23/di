import random


def imprime_msg():
    print('**********************************')
    print('*     Jogo da adivinhação        *')
    print('**********************************')


def carrega_palavra_secreta():
    arquivo = open('palavra_secreta.txt', 'r')
    palavra_secreta = []
    for linha in arquivo:
        linha = linha.strip()
        palavra_secreta.append(linha.lower())

    numero = random.randrange(0, len(palavra_secreta))
    palavra_s = palavra_secreta[numero]
    return palavra_s


def msg_perdeu():
    print('**********************************')
    print('*     Voce foi Enforcado :-)     *')
    print('*          GAME OVER             *')
    print('**********************************')
    print("          _______________        ")
    print("         /               \       ")
    print("        /                 \      ")
    print("     /\/                   \/\   ")
    print("     \ |   xxx       xxx   | /   ")
    print("      \|   xxx       xxx   |/    ")
    print("       |   xx         xx   |     ")
    print("       |                   |     ")
    print("       \__      xxx      __/     ")
    print("       |  \     xxx     /  |     ")
    print("       |   |           |   |     ")
    print("       |   I I I  I  I I   |     ")
    print("       |     I I  I  I     |     ")
    print("       \__               __/     ")
    print("          \__         __/     ")
    print("             \_______/     ")


def imprime_mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("      ___________          ")
    print("     '._==_==_=_.'         ")
    print("     .-\\:      /-.        ")
    print("    | (|:.      |) |       ")
    print("     '-|:.      |-'        ")
    print("       \\::.   /           ")
    print("        '::. .'            ")
    print("          ) (              ")
    print("        _.' '._            ")
    print("       '-------'           ")


def jogar():
    #impreme mensagem de boas-vindas
    imprime_msg()
    #carrega uma palavra secreta da arquivo txt
    palavra_secreta = carrega_palavra_secreta()
    #pega a palavra secreta e substitui por [-]
    palavra_adivinhada = ['-'] * len(palavra_secreta)
    tentativas = 6
    print(f'Descubra A Palavra-Secreta : {palavra_adivinhada}')
    while True:
        chute = input("Digite uma letra: ").lower()
        if chute in palavra_secreta:
            posicao = 0

            for letra in palavra_secreta:
                if chute == letra:
                    print(f' Encontadoa a letra({letra}) na posicao ({posicao + 1})')
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
            imprime_mensagem_vencedor()
            break
        if tentativas == 0:
            msg_perdeu()
            break
        print('******************************************************')
        print('            tic-tac, tic-tac...   ')
        print('******************************************************')
        print('')
        print(f'Palavras Acertadas: {palavra_adivinhada}')

