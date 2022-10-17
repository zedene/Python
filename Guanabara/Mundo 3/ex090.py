"""Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""
aluno = dict ()
aluno ['Nome'] = str(input('Digite o nome do aluno: '))
aluno ['Média'] = float(input('Digite a média: '))

#Impressão na tela
print(f'O nome do aluno é {aluno["Nome"]}')
print(f'A média é {aluno["Média"]}')
if aluno['Média'] <= 7:
    print('O aluno está reprovado')
else:
    print('O aluno está aprovado!')
    
#Solução de impressão alternativa

#for k, v in aluno.items():
#   print(f'{k} é igual a {v}')