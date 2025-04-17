def fatorial(num, show=False):

    numero = 1

    for c in range(1, num+1):
        numero *= c

        if show:
            print(c, end='')

            if c < num:
                print(' x ',end=' ')
            else:
                print(' = ', end='')

    return numero

'''número = int(input('DIGITE UM NÚMERO: '))
condição = str(input('QUER MOSTRAR O CÁLCULO DO FATORIAL? [S/N]: ')).upper().strip()

if condição == 'S':
    print(' = ', fatorial(número))

else:
    print(' = ', fatorial(número))'''


print((fatorial(5, show=False)))
