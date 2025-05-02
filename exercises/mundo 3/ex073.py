def contar_numeros(inicio: int, fim: int, passo: int) -> None:
    if inicio > fim:
        fim -= 1
    else:
        fim += 1
    for numero in range(inicio, fim, passo):
        print(numero, end=' - ')
    print('')

contar_numeros(inicio=1, fim=10, passo=1)
contar_numeros(inicio=10, fim=0, passo=-2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contar_numeros(inicio=inicio, fim=fim, passo=passo)
