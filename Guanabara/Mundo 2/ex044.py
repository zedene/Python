preco = float(input('Digite o valor do produto: '))
print('''[ 1 ] - Dinheiro ou Pix
[ 2 ] - Cartão à vista
[ 3 ] - Cartão em 2x
[ 4 ] - Cartão em 3x ou mais''')
form = int(input('Digite a forma de pagamento: '))
if form == 1:
    print('O valor total será de: {:.2f} R$'.format (preco - (preco * 0.1)))
elif form == 2:
    print('O valor total será de: {:.2f} R$'.format(preco - (preco *0.05)))
elif form == 3:
    print('O valor total será de: {:.2f} R$'.format(preco))
elif form == 4:
    print('O valor total será de: {:.2f} R$'.format(preco + (preco * 0.2)))