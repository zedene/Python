from random import randint
n1 = randint (0, 5)
n2 = int(input('Digite um numero entre 0 e 5: '))
if n2 == n1:
    print('Você Acertou!')
else:
    print('Você Errou!')