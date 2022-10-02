salario = float(input('Digite o salário: '))
aumento = float(input('Digite o aumento em %: '))
total = salario + (salario * aumento / 100)
print('Salário antigo: {:.2f} R$\nAumento Recebido: {} %\nValor do Salário com aumento: {} R$'.format(salario, aumento, total))