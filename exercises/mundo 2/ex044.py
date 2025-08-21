frase =  str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
frase_ao_contrario = frase[::-1].strip().lower().replace(' ', '')

if frase == frase_ao_contrario:
    print(f'A frase {frase} é um políndromo e ela é completamente igual de frente para trás como de trás para frente.')
    print(f'Frase normal: {frase}.')
    print(f'Frase ao contrário: {frase_ao_contrario}.')
else:
    print(f'A frase {frase} não é um políndromo.')
