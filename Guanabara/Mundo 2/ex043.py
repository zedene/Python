# IMC = peso / (altura * altura)
alt = float(input('Digite a sua altura (ex: 1.80): '))
peso = float(input('Digite o seu peso em KG (ex: 71): '))
imc = peso / alt**2
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc <= 30:
    print('Você está com sobrepeso.')
elif 30 <= imc <= 40:
    print('Você está com Obesidade.')
else:
    print('Obesidade Mórbida.')