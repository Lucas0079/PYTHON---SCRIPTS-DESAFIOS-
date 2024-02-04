print('='*15 + ' DESAFIO 013 ' + '='*15)

valor_produto = float(input('Informe o valor do produto: R$'))

valor_desconto = (5/100)*valor_produto
desconto_aplicado = valor_produto - valor_desconto

print('O valor original do produto é R${}'.format(valor_produto))
print('Foi aplicado um desconto de 5%')
print('O valor com o desconto aplicado é R${}'.format(desconto_aplicado))
