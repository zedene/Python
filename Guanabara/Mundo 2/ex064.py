soma = cont = 0
num = int(input('Digite um número: [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: [999 para parar] '))
print('Vocé digitou {} números e a soma entre eles foi de {}.'.format(cont,soma))