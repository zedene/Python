viagem = int(input('Digite a distância da sua viagem em KM: '))
if viagem <= 200:
    print('O valor da viagem é de: {:.2f} R$'.format(viagem * 0.50))
else:
    print('O valor da viagem é de: {:.2f} R$'.format(viagem * 0.45))