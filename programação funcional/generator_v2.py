def cores_do_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índido'
    yield 'violeta'

generator = cores_do_arco_iris()

for cor in generator:
    print(cor)  
print('FIM')
    