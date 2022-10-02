cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if  num % 2 == 0:
        soma += num
        cont += 1
print('O valor dos {} números pares é: {}'.format(cont, soma))