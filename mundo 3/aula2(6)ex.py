
aux = []

expressão = str(input("DIGITE UMA EXPRESSÃO QUALQUER: "))


for cont in (expressão):
    if cont == '(':
        aux.append('(')

    elif expressão == ')':
        if len(aux) > 0:
            aux.pop()
        else:
            aux.append(')')
            break

if len(aux) == 0:
    print('A EXPRESÃO ESTÁ CORRETA')
else:
    print('A EXPRESSÃO DIGITADA É INCORRETA.')