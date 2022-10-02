import random
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))