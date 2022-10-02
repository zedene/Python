tot = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi de R$ {tot:.2f}')
print(f'{totmil} custam mais de R$ 1000.')
print(f'{produto} é o produto mais barato.')
