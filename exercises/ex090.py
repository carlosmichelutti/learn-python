def calcular_minimo_divisor_comum(numeros: list[int]) -> None:

    menor_numero = min(numeros)
    lista_de_mdcs = []
    while True:
        divisor = 0
        for numero in numeros:
            if menor_numero == 0:
                print('Essa sequencia númerica não tem MDC.')
                break

            if numero % menor_numero == 0:
                divisor += 1
                lista_de_mdcs.append(menor_numero)

        if divisor == len(numeros):
            for divisor in range(len(lista_de_mdcs)):
                if lista_de_mdcs[divisor]:
                    menor_divisor = lista_de_mdcs[divisor]
                elif divisor > menor_divisor and divisor > 1:
                    menor_divisor = lista_de_mdcs[divisor]
                else:
                    menor_divisor = 1

            print(f'O MDC dos números {numeros} é {menor_divisor}')
            break

        menor_numero -= 1

calcular_minimo_divisor_comum([9, 3, 5])
calcular_minimo_divisor_comum([123, 100, 5])
calcular_minimo_divisor_comum([25, 5, 15])
calcular_minimo_divisor_comum([18,60])
calcular_minimo_divisor_comum([55, 22])
calcular_minimo_divisor_comum([15, 150])
calcular_minimo_divisor_comum([81, 9])
