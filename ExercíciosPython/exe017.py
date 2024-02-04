import math

print('='*15 + ' DESAFIO 17 ' + '='*15)

numero_usuario = float(input('Digite um número real qualquer: '))

numero_quebrado = math.trunc(numero_usuario)

print('O valor real fornecido foi {}'.format(numero_usuario))
print('O valor inteiro é {}'.format(numero_quebrado))

