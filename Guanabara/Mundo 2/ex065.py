resp = 'S'
soma = num = media = cont = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi de {:.2f}'.format(cont, media))
print('O maior número é {} e o menor número é {}.'.format(maior,menor))