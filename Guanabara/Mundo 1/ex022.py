nome = str(input('Digite um nome: '))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Nome em maiúscula: {}'.format(nome.upper()))
print('Quantas letras sem espaço: {}'.format(len(nome.replace(" ", ""))))
print('O primeiro nome tem: {}'.format(len(nome.split()[0])))