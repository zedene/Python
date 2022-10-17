from datetime import datetime
dados = dict ()
dados ['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados ['cpts'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Digite o seu salário: '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('*-' * 30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')