print('='*15 + ' DESAFIO 011 ' + '='*15)

quantidade_reais = float(input('Digite quantos reais você tem: R$'))

preco_dolar = 4.97

quantidade_dolar = quantidade_reais/preco_dolar

print('Com R${} você conseguiu U${:.2f}!'.format(quantidade_reais,quantidade_dolar))


