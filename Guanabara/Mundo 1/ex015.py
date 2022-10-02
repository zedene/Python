dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantidades de KM rodados? '))
dias = dias * 60
km = km * 0.15
print('Você deverá pagar: {:.2f} R$'.format(dias+km))