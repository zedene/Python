num = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal:''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é: {}'.format(num, hex(num).upper()[2:]))
else:
    print('Opção Inválida! Digite novamente: ')