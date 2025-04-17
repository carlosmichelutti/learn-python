class Humano:
    especie = 'homo sapiens'

    def __init__(self, nome) -> None:
        self.nome = nome
        self._idade = None

    @property
    def inteligente(self):
        raise NotImplementedError ('Propriedade não encontrada')
    
    def das_cavernas(self):
        self.especie = 'HOMO NEANDERTAL'
        return self

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError ('A IDADE DEVE SER UM NÚMERO POSITIVO.')
        self._idade = idade

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]
    
class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True

anonimo = Humano('Jack Chan')
try:
    print(anonimo.inteligente)
except NotImplementedError:
    print('Propriedade abstrata')

jose = HomoSapiens('José')
jose.idade = 40
print(f'{jose.nome} da classe {jose.__class__.__name__}, inteligente {jose.inteligente}')
grokn = Neanderthal('Grokn')
print(f'{grokn.nome} da classe {grokn.__class__.__name__}, inteligente {grokn.inteligente}')