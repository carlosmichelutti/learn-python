class Humano:
    especie = 'homo sapiens'

    def __init__(self, nome) -> None:
        self.nome = nome
        self._idade = None
    
    def das_cavernas(self):
        self.especie = 'HOMO NEANDERTAL'
        return self

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        if idade < 0:
            raise ValueError ('A IDADE DEVE SER UM NÚMERO POSITIVO.')
        self.idade = idade

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]
    
class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

jose = HomoSapiens('Jose')
jose.set_idade(40)
print(f'Nome: {jose.nome} Idade: {jose.idade}')