num = int(input('Digite o número para ver sua tabuada: '))
for cont in range(1, 11):
    if cont <=10:
        print('[ {} * {} ] = [ {} ]'.format(num, cont, num*cont))