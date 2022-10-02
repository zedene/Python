r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
    if r1 == r2 == r3:
       print('Tipo: Equilátero')
    elif r1 == r2 or r3 and r2 == r3:
        print('Tipo: Isósceles')
    else:
        print('Tipo: Escaleno')
#elif r1 != r2 != r3 != r1:
#print('Tipo: Escaleno)
#else:
#print('Tipo: Isósceles)
else:
    print('Não pode formar um triângulo')