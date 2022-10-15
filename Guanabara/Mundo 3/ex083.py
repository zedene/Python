expr = str(input('Digite a expressão: '))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len (pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')