nome = str(input('Escreva o nome do aluno: '))
nota1 = float(input(f'Escreva a primeira nota do aluno {nome}: '))
nota2 = float(input(f'Escreva a segunda nota do aluno {nome}: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Parabéns {nome}, você passou de ano.')
else:
    print(f'Infelizmente {nome}, você não passou de ano.')
