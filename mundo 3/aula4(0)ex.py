aluno = {}

aluno['Nome: '] = str(input('DIGITE O NOME DO ALUNO: ')).upper().strip()
aluno['Media'] = float(input(f'DIGITE A MÉDIA DE {aluno["Nome: "]}: '))

if aluno["Media"] >= 7.0:
    aluno['Situacao: '] = 'APROVADO'
elif aluno ['Media'] >= 5:
    aluno['Situacao: '] = 'RECUPERAÇÃO'
else:
    aluno['Situacao: '] = 'REPROVADO'

print(f'O {aluno["Nome: "]} TEM A MÉDIA {aluno["Media"]} E ESTÁ {aluno["Situacao: "]}.')


