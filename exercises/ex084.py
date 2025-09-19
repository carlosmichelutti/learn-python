def cores_do_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índido'
    yield 'violeta'

generator = cores_do_arco_iris()
while True:
    print(next(generator))
