aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).capitalize().strip()
aluno['media'] = float(input(f'Digite a média do aluno {aluno["nome"]}: '))

if aluno['media'] >= 7.0:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'

print(f'O {aluno["nome"]} tem a média {aluno["media"]} e está {aluno["situacao"]}.')
