class carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def acelerar(self):
        if self.marca == 'ferrari':
            print('ACELERANDO')
        else:
            print('TÁ FRACO')
    
    def corr(self):
        print(f'QUE LINDO SEU CARRO {self.cor}')
    
    def anoo(self):
        print(f'BONITO SEU CARRO DOS ANOS {self.ano}')

carro1 = carro('FERRARI', 2018, 'VERMELHO')
print(carro1.acelerar(), carro1.corr(), carro1.anoo())