print('='*15 + ' DESAFIO 016 ' + '='*15)

kms = float(input('Informe a quantidade de quilômetros rodados: '))
dias_aluguel = int(input('Informe a quantidade de dias que o carro foi alugado: '))

kms_preco = kms*0.15
dias_aluguel_preco = dias_aluguel*60
despesa_total = kms_preco + dias_aluguel_preco

print('Quantidade de quilômetros rodados: {}'.format(kms))
print('Quantidade de dias de aluguel: {}'.format(dias_aluguel))
print('Despesa total do serviço: R${:.2f}'.format(despesa_total))
