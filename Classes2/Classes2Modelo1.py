class Humano:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'HOMO NEANDERTAL'
        return self
    
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]
    pass
    
class Neanderthal(Humano):
    especie = Humano.especies()[-2]
    pass
class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
    pass

jose = HomoSapiens('Jose')
grokn = Neanderthal('Grokn')
print(f'EVOLUÇÃO A PARTIR DA CLASSE: {", " .join(HomoSapiens.especies())}')
print(f'EVOLUÇÃO A PARTIR DA CLASSE: {", " .join(Humano.especies())}')
print(f'EVOLUÇÃO A PARTIR DA CLASSE: {", ".join(jose.especies())}')
print(f'HOMO SAPIENS EVOLUIDO? {HomoSapiens.is_evoluido()}')
print(f'NEANDERTAL EVOLUÍDO? {Neanderthal.is_evoluido()}')
print(f'JOSÉ EVOLUÍDO? {jose.is_evoluido()}')
print(f'GROKN EVOLUÍDO? {grokn.is_evoluido()}')