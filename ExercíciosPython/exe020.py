import math

print('='*15 + ' DESAFIO 20 ' + '='*15)

angulo = int(input('Digite um ângulo qualquer: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Ângulo fornecido: {:.2f}°'.format(angulo))
print('Valor do SENO: {:.2f}'.format(seno))
print('Valor do COSSENO: {:.2f}'.format(cosseno))
print('Valor da TANGENTE: {:.2f}'.format(tangente))