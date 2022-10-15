num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break
    while resp != 'S':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
for i, v, in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('*-'*30)
print(f'A lista completa é {num}')
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')