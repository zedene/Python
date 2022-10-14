lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado!')
else:
    print(f'O valor 5 não foi encontrado!')