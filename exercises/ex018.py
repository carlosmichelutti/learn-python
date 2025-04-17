from random import shuffle

aluno1 = input('Escreva o nome do 1º Aluno: ')
aluno2 = input('Escreva o nome do 2º Aluno: ')
aluno3 = input('Escreva o nome do 3º Aluno: ')
aluno4 = input('Escreva o nome do 4º Aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(f'A ordem de apresentação do trabalho será: {lista}.')
