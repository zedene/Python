sal = float(input('Digite o valor do salário: '))
if sal > 1250:
    print('O seu salário será de {:.2f} R$.'.format(sal + (sal * 10 / 100)))
else:
    print('O seu salário será de {:.2f} R$.'.format(sal + (sal * 15 / 100)))