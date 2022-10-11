from imaplib import Int2AP


cont = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze',
        'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Digite um número: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente, ', end='')
    print(f'Você digitou o número {cont[num]}')
    conti = input('Deseja continuar? [S/N] ')
    if conti in 'Nn':
        break
print('Fim do Programa')