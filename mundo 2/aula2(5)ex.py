primeirotermo = int(input('QUAL O PRIMEIRO TERMO DESSA PROGRESÃO ARITIMETICA? '))
razão = int(input('QUAL A RAZÃO DA PROGESSÃO? '))

for c in range(primeirotermo, (primeirotermo + (11-1)*razão), razão):
    print('{}'.format(c), end="-> ")
