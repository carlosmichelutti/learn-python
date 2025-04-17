
nums = []
pares = []
impares= []
par = 0
for numeros in range(1, 8):
    num = int(input('DIGITE UM NÚMERO: '))

    if num % 2 == 0:
        pares.append(num)
        
    if num % 2 == 1: 
        impares.append(num)
    
print(nums)

print('OS NÚMEROS PARES REGISTRADOS FORAM: {}'.format(pares))

print('OS NÚMEROS IMPARES REGISTRADOS FORAM: {}'.format(impares.sort()))


