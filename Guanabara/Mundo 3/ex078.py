lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i,v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posições ',end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')
print()