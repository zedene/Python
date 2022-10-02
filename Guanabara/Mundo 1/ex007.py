nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média é: ',media)
if media >= 7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')