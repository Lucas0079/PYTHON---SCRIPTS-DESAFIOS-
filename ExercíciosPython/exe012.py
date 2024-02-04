print('='*15 + ' DESAFIO 012 ' + '='*15)

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura
quantidade_tinta = area/2

print('A parede tem  {} x {}'.format(largura, altura))
print('Sua área é {}'.format(area))
print('A quantidade de tinta necessária pra pinta-la é {} litros'.format(quantidade_tinta))



