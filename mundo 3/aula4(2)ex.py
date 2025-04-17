
from datetime import date

pessoas =  {}

pessoas['NOME: '] = str(input('QUAL É O SEU NOME? '))
nasc = int(input('INFORME O ANO DE NASCIMENTO: '))
pessoas['IDADE: '] = date.today().year - nasc
pessoas ['NÚMERO DA CARTEIRA DE TRABALHO: '] = int(input('INFORME O NÚMERO DA CARTEIRA DE TRABALHO [0] CASO NÃO TENHA: '))

if pessoas['NÚMERO DA CARTEIRA DE TRABALHO: '] == 0:
    print(f'O SEU NOME É {pessoas["NOME: "]} \nVOCÊ TEM {pessoas["IDADE: "]}\n E VOCÊ NÃO POSSUI CARTEIRA DE TRABALHO.')
else:
    pessoas['ANO DE CONTRATAÇÃO: '] = int(input('EM QUAL ANO VOCÊ FOI CONTRATADO? '))
    pessoas['SALÁRIO: '] = float(input('QUAL O SEU SALÁRIO? '))
    pessoas['ANO DA APOSENTADORIA: '] = (pessoas['ANO DE CONTRATAÇÃO: '] + 35) - pessoas['ANO DE NASCIMENTO: ']

for k, v in pessoas.items():
    print(f'O {k} É IGUAL A {v}')