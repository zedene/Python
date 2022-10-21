from math import radians


listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{"Listagem de Preço":^40}')
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')