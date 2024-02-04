import math

print('='*15 + ' DESAFIO 019 ' + '='*15)

cateto_oposto = float(input('Informe o valor do cateto oposto: '))
cateto_adjacente = float(input('Informe o valor do cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print('O valor do cateto oposto é {}'.format(cateto_oposto))
print('O valor do cateto adjacente é {}'.format(cateto_adjacente))
print('O valor da hipotenusa é {}'.format(math.ceil5(hipotenusa)))
