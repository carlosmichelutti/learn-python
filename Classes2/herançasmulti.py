class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')
    
class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')

class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teias entre prédios')
    
jonh = Homem()
print(f'Jonh pode: {jonh.capacidades}')

aranha = Aranha()
print(f'Aranha pode: {aranha.capacidades}')

homemaranha = SpiderMan()
print(f'O Homem aranha pode: {homemaranha.capacidades}')