largura = float(input('Digite a largura da parede em m: '))
altura = float(input('Digite a altura da parede em m: '))
total = (largura * altura)
print('Você precisará de {:.2f} litros de tintas para pintar a parede.'.format(total/2))