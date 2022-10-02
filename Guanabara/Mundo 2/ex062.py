print('=-='*50)
print('Progressão Aritmética')
print('=-='*50)
num = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')