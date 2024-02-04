import random

print('='*15 + ' DESAFIO  21 ' + '='*15+'\n')

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(lista_alunos)

print('\nO aluno sorteado foi o(a) {}!'.format(aluno_sorteado))





