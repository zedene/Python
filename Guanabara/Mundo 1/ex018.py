import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ang, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}.'.format(ang, tan))