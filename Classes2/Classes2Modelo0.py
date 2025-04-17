class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
object


jose = Humano('José')
grokn = Humano('Grokn').das_cavernas()

print(f'Humano.especie: {Humano.especie}')
print(f'jose.especie: {jose.especie}')
print(f'grokn.especie: {grokn.especie}')
