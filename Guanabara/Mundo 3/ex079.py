lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado...')
    else:
        print('Valor existente, não será adicionado!')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Resposta errada. Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print(f'Você digitou os valores {lista}')