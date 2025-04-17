from datetime import date

anoatual = date.today().year
maioridade = 0
menoridade= 0
for c in range (0, 7):
    yearnasc =int(input('DIGITE A DATA DE NASCIMENTO DA {}º PESSOA: '.format(c+1)))
    if anoatual - yearnasc >= 18:
        maioridade = maioridade + 1
    else: 
        menoridade = menoridade + 1

print('')
print('NO GRUPO EXISTEM {} PESSOAS QUE SÃO MAIOR DE IDADE.'.format(maioridade))
print('NO GRUPO EXISTEM {} PESSOAS QUE SÃO MENORES DE IDADE.'.format(menoridade))


