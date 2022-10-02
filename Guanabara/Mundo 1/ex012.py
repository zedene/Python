valor = float(input('Digite o valor original? '))
desconto = float(input('Digite o valor do desconto: '))
total = valor - (valor * desconto / 100)

print('O valor original era de: {:.2f} R$ \nO desconto é de: {:.0f}% \nO valor final com desconto é: {} R$'.format(valor, desconto, total))