from operator import index
from textwrap import indent


times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')
print('='*50)
print(f'Lista de times do brasileirão: {times}')
print('='*50)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('='*50)
print(f'Os 4 últimos são: {times[-4:]}')
print('='*50)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('='*50)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª posição')