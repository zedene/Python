vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado, você deverá pagar {:.2f} R$ por {:.0f} KM/h excedido.'.format(multa, vel - 80))
print('Velocidade dentro do permitido.')