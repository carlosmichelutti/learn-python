def verificar_maior_valor(numeros: list):
    maior_valor = 0
    for numero in numeros:
        if numero > maior_valor:
            maior_valor = numero
    print(f'O maior valor encontrado na lista {numeros} foi o número {maior_valor}.')
    
verificar_maior_valor(numeros=[4, 5, 6, 9, 15])
verificar_maior_valor(numeros=[1, 4, 5, 7, 3])
verificar_maior_valor(numeros=[1, 10])
