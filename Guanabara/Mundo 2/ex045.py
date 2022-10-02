from random import randint
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
p1 = int(input('Digite sua escolha: '))
pc = randint(1, 3)
if p1 == pc:
    print('Empate!')
elif p1 == 1 and pc == 2:
    print('Você Perdeu: Pedra x Papel')
elif p1 == 1 and pc == 3:
    print('Você Ganhou: Pedra x Tesoura')
elif p1 == 2 and pc == 1:
    print('Você Ganhou: Papel x Pedra')
elif p1 == 2 and pc == 3:
    print('Você Perdeu: Papel x Tesoura')
elif p1 == 3 and pc == 1:
    print('Você Perdeu: Tesoura x Pedra')
else:
    print('Você ganhou: Tesoura x Papel')