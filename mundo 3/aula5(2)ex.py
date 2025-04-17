def contagem(a, b, c):
    print('='*40)
    for cont in range(a, b, c):
        print(cont, end=' - ')
    print('')


contagem(1, 10, 1)
contagem(10, 0, -2)
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contagem(inicio, fim, passo)
