tabuada = int(input('ESCOLHA UMA NÚMERO PARA FAZER A SUA TABUADA: '))

for c in range(1, 10+1):
    print('{} x {} = {}'.format(tabuada, c, tabuada*c))
print('FIM')