def soma_dos_numeros_da_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma
    
def validar_numeros_positivos(lista):
    new_lista = []
    for numero in lista:
        if numero > 0:
            new_lista.append(numero)
    return new_lista


a = [1, 2, 3, 4, -4023, -3]
print(soma_dos_numeros_da_lista(validar_numeros_positivos(a)))
