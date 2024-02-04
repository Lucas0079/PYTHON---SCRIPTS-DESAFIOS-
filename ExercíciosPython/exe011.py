print('='*15 + ' DESAFIO 011 ' + '='*15)

quantidade_reais = float(input('Digite quantos reais você tem: R$'))

preco_dolar = 4.97
preco_euro = 5.37

quantidade_dolar = quantidade_reais/preco_dolar
quantidade_euro = quantidade_reais/preco_euro

print('Com R${} você conseguiu U${:.2f}!'.format(quantidade_reais,quantidade_dolar))
print('Com R${} você conseguiu €{:.2f}!'.format(quantidade_reais,quantidade_euro))



