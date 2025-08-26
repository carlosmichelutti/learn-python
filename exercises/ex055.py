numeros_por_extenso = (
    'ZERO',
    'UM',
    'DOIS',
    'TRÊS',
    'QUATRO',
    'CINCO',
    'SEIS',
    'SETE',
    'OITO',
    'NOVE',
    'DEZ',
    'ONZE',
    'DOZE',
    'TREZE',
    'CATORZE',
    'QUINZE',
    'DEZESSEIS',
    'DEZESSETE',
    'DEZOITO',
    'DEZENOVE',
    'VINTE',
)

escolha_usuario = int(input('Escolha um número entre 0 e 20: '))
while True:
    if escolha_usuario > 20:
        escolha_usuario = int(input('Número invalido! Escolha um número entre 0 e 20: '))
    else:
        break

print(f'O número que você escolheu por extenso foi o número {escolha_usuario} = {numeros_por_extenso[escolha_usuario]}.')
