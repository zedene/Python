num = (int(input('Digite o primeiro número: ')),
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')),
int(input('Digite o último número: ')))
print(f'Você digitou os valores {num[0]}, {num[1]}, {num[2]} e {num[3]}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')