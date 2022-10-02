num = int(input('Digite um número: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número \033[33m{}\033[m foi divisível \033[33m{}\033[m vezes'.format(num, tot))
if tot == 2:
    print('Logo, ele é primo.')
elif tot > 2:
    print('Logo, ele não é primo.')