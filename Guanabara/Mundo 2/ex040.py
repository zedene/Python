n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado!')
elif media <= 6.9:
    print('Você está em recuperação!')
else:
   print('Você foi aprovado!')