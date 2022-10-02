from random import randint
cont = 0
acertou = False
print('Eu sou seu computador, irei pensar em um número de 0 à 10. Você consegue acertar?')
pc = randint (0,11)
while not acertou:
    p1 = int(input('Qual o seu palpite? '))
    cont += 1
    if p1 == pc:
        acertou = True
    else:
        if p1 < pc:
            print('Mais... Tente novamente: ')
        elif p1 > pc:
            print('Menos... Tente novamente: ')
print('Você acertou com {} tentativas. Parabéns!'.format(cont))