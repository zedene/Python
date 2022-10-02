print('='*100)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''   O que quer fazer com os números?
    [1] Somar
    [2] Multiplicar
    [3] Maior Valor
    [4] Novos Números
    [5] Sair do Programa''')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1,n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} * {} = {}'.format(n1,n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2        
        print('O maior valor entre {} e {} é {}.'.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('='*100)
print('Fim do Programa!')
print('='*100)