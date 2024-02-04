print('='*15 + ' DESAFIO 014 ' + '='*15)

salario = float(input('Informe seu salário: R$'))

aumento = salario*(15/100)
aumento_aplicado = salario + aumento

print('Seu salário anterior era R${}'.format(salario))
print('Seu salário com aumento é R${:.2f}'.format(aumento_aplicado))
