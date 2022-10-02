num = 0
while True:
    num = int(input('Digite o número: '))
    for cont in range (1,11):
        if num < 0:
            break
        if cont < 10:
            print(f'{num} x {cont} = {num * cont}')
print('Acabou')