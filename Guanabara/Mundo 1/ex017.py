#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
cat1 = float(input('Digite o comprimento do cateto oposto: '))
cat2 = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da Hipotenusa é de: {:.2f}'.format(hypot(cat1, cat2)))