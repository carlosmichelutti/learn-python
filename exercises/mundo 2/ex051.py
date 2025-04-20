quantidade_numeros = 0
maior_numero = 0
menor_numero = 0
resposta = 's'
soma = 0

while resposta == 's':
    numero = int(input('Escreva um número inteiro qualquer: '))
    quantidade_numeros += 1
    soma += numero

    if quantidade_numeros == 1:
        maior_numero = numero
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

    resposta =  str(input('Quer continuar? [s/n] ')).lower().strip()
    while True:
        if resposta not in 'sn':
            print('Opção inválida! Tente novamente!')
            resposta = str(input('Quer continuar? [s/n] ')).lower().strip()
            continue
        break

print(f'A média de todos os {quantidade_numeros} números digitados é igual a {soma/quantidade_numeros}.')
print(f'O maior número digitado foi o número {maior_numero}.')
print(f'O menor valor digitado foi o número {menor_numero}.')
