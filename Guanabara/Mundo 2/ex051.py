print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
cont = 0
soma = 0
ini = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for cont in range(ini, 11):
    if cont <= 10:
        soma += razao
        print('{}'.format(soma), end=' → ')
print('ACABOU')