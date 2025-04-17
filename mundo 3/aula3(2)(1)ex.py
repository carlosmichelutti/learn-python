núm = [[],[]]
valor = 0

for c in range(1,8):
    valor = int(input('DIGITE UM VALOR: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()


print(núm)
print(núm[0])
print(núm[1])
