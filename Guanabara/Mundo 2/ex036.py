val = float(input('Digite o valor da casa: '))
sal =  float(input('Digite o valor do seu salário: '))
ano =  float(input('Digite em quantos anos você irá pagar: '))
mensCasa = (val / (ano * 12))
mensParcela = (sal * 0.30)
if mensCasa <= mensParcela:
    print('Emprestimo Aprovado!')
else:
    print('Emprestimo Negado!')
