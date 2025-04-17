primeirotermo = int(input('QUAL O PRIMEIRO TERMO DESSA PROGRESÃO ARITIMETICA? '))
razão = int(input('QUAL A RAZÃO DA PROGESSÃO? '))
cont = 1
próximotermo = primeirotermo
resp = 1

while cont < 11:
    print("{}...".format(próximotermo), end="")
    próximotermo = próximotermo + razão
    cont = cont + 1
print('')

resp = int(input('QUER MOSTRAR MAIS QUANTOS TERMOS? '))

while resp != 0: 
    while resp != 0:
        print("{}...".format(próximotermo), end=" ")
        próximotermo = próximotermo + razão
        resp = resp - 1
    print('')
    resp = int(input('QUER MOSTRAR MAIS QUANTOS TERMOS? '))


    

    
