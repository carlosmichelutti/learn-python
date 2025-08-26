nome = str(input('Digite o nome do aluno: '))
nota1 = float(input(f'Digite a primeira nota do aluno {nome}: '))
nota2 = float(input(f'Digite a segunda nota do aluno {nome}: '))

media = float((nota1 + nota2) / 2)

if media < 5.0:
    print('Reprovado! A sua média foi abaixo da requerida.')
elif media > 5.0 and media < 6.9:
    print('Recuperação! A sua nota está razoável. Recupere-a para passar de ano.')
elif media >= 7.0:
    print('Parabéns! Você foi aprovado e passou de ano! Até o ano que vem!')
