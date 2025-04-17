class SimpleClass:
    contador = 0

    def __init__(self):
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador +=1
    

lista = [SimpleClass(), SimpleClass()]
print(SimpleClass.contador)
