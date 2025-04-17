def mdc(numeros):
    menor_numero = min(numeros)

    while True:
        divisor = 0

        for numero in numeros:

            if menor_numero == 0:
                print('ESSA SEQUENCIA NUMERICA NAO TEM MDC.')
                break

            elif numero % menor_numero == 0:
                divisor += 1
                lista_de_mdcs = []
                lista_de_mdcs.append(menor_numero)

        if divisor == len(numeros):
            for divisor in range(len(lista_de_mdcs)):
                if lista_de_mdcs[divisor]:
                    menor_divisor = lista_de_mdcs[divisor]
                elif divisor > menor_divisor and divisor > 1:
                    menor_divisor = lista_de_mdcs[divisor]
                else:
                    menor_divisor = 1

            print(f'O MDC DOS NÚMEROS {numeros} É {menor_divisor}')

            break

        menor_numero -= 1

mdc([9, 3, 5])
mdc([123, 100, 5])
mdc([25, 5, 15])
mdc([18,60])
mdc([55, 22])
mdc([15, 150])
mdc([81, 9])
