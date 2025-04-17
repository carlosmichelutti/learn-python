def fatorial(nome, goals):
    print(f'O JOGADOR {nome} FEZ {goals} GOL(s).')

nome = str(input('QUAL O NOME DO JOGADOR? '))
goals = str(input(f'QUANTOS GOLS O JOGADOR FEZ? '))

if nome == '':
    nome = '<DESCONHECIDO>'

if goals.isnumeric():
    goals = int(goals)

else:
    goals = 0

if nome.strip() == '':
    nome = '<DESCONHECIDO>'

fatorial(nome, goals)

