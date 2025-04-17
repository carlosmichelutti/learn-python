from random import randint

def sorteia():
    """
    -> NÃO POSSUI PARÂMETROS
    -> FAZ UMA LISTA E ADICIONA 5 NUMEROS ALEATÓRIOS A MESMA LISTA
    -> RETORNA A LISTA
    """
    lista = []

    for c in range(0, 5):
        lista.append(int(randint(1, 10)))

    return lista


def soma(lista):
    soma = 0

    for item in lista:
        soma += item

    return soma

lista = sorteia()
somadosvalores = soma(lista)


print(lista)
print(somadosvalores)