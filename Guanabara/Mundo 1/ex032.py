print('------É ano bissexto?------')
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é ano bissexto.'.format(ano))