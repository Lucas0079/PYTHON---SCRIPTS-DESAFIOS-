import random

print('='*15 + ' DESAFIO 022 ' + '='*15)

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

lista_alunos = [nome1, nome2, nome3, nome4]
random.shuffle(lista_alunos)

print('A ordem da apresentação vai ser: ')
print(lista_alunos)