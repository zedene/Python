def linha():
    print('*-' * 30)
    print(f'{"Python Calculator":^60}')
    print('*-' * 30)
    

linha()
print('''1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
opcao = int(input('Digite o número da operação desejada: '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#operações
if opcao == 1:
     print(f'O resultado da soma de [{num1} + {num2}] = {num1 + num2}')
elif opcao == 2:
    print(f'O resultado da subtração de [{num1} - {num2}] = {num1 - num2}')
elif opcao == 3:
    print(f'O resultado da multiplicação de [{num1} * {num2}] = {num1 * num2}')
elif opcao == 4:
    print(f'O resultado da divisão de [{num1} / {num2}] = {num1 / num2}')
print('Volte Sempre!')