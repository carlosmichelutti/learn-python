resp = input('QUAL É O SEU SEXO [M/F]? ').upper().strip()

while resp not in 'MmFf':
    print("VALOR INCORRETO, TENTE NOVAMENTE!")
    resp = input('QUAL É O SEU SEXO [M/F]? ').upper().strip

print('OBRIGADO POR REGISTRAR O SEU SEXO. FIM')
