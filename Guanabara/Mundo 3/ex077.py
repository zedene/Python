palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar', 
            'Trabalhar', 'Mercado','Programador','Futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
