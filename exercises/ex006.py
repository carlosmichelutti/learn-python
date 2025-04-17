real = float(input('Quanto de dinheiro você tem na sua carteira? R$'))
dolares = real / 5.21
euros = real / 5.67
ienes =  real * 25.01

print(f'Com R$ {real} você tem U${dolares:.2F} em dolares, {euros:.2f} em euro e {ienes:.2f} em ienes.')
