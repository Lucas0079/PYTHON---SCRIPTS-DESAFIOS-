print('===== DESAFIO 05 =====')
tecla = input('Digite alguma coisa: ')


print('O tipo do que informou é {}'.format(type(tecla)))
print('É um número ? Resposta({})'.format(tecla.isnumeric()))
print('É um número,letra ou os dois? Resposta({})'.format(tecla.isalnum()))
print('É uma letra? Resposta({})'.format(tecla.isalpha()))
print('Ta em maiúsculo? Resposta({})'.format(tecla.isupper()))
print('Ta em minúsculo? Resposta({})'.format(tecla.islower()))
print('Tem apenas espaço? Resposta({})'.format(tecla.isspace()))
print('É capatalizada? Resposta({})'.format(tecla.istitle()))





