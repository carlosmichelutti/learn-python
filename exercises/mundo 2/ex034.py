peso = float(input('Escreva o seu peso (kg): '))
altura = float(input('Escreva a sua altura (cm): '))

altura = altura / 100
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso.')
elif imc >= 30 and imc < 40:
    print('Você está obeso.')
elif imc >= 40:
    print('Você está com obesidade mórbida.')
