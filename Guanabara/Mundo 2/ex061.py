print('=-='*50)
print('10 TERMOS DE UMA PA')
print('=-='*50)
primeiro = int(input('Digite o Termo: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo),end='')
    termo += razao
    cont += 1
print('Fim')
