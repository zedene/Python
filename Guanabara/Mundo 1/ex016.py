from math import trunc
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: DIgite um número: 6.127
#O número 6.127 tem a parte inteira 6.
num = float(input('Digite um número real(ex: 6.127): '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))