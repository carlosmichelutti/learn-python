class Carro:
    def __init__(self, nome, velocidade_maxima=180, velocidade_inicial=0) -> None:
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_inicial = velocidade_inicial
        self.velocidade_minima = velocidade_inicial
    
    def acelerar(self, aceleração = 5):

        self.acelerarção = aceleração

        print(f'{self.nome} ACELERANDO ',end='')

        for _ in range(25):
            if self.velocidade_inicial < self.velocidade_maxima:
                print(self.velocidade_inicial, end=' ')
                self.velocidade_inicial += self.acelerarção
            else:
                self.velocidade_inicial = self.velocidade_maxima
                print(f'{self.velocidade_inicial} VELOCIDADE MÁXIMA ATINGIDA')
                break

    def desacelerar(self, desaceleração=20):

        self.desaceleraração = desaceleração
        self.desacelerar_inicial = self.velocidade_inicial

        print(f'{self.nome} DESACELERANDO', end=' ')
        for _ in range(10):
            if self.desacelerar_inicial > self.velocidade_minima+self.desaceleraração:
                self.desacelerar_inicial -= self.desaceleraração
                print(f'{self.desacelerar_inicial}', end=' ')
            else:
                self.velocidade_inicial = 0
                print(f'{self.velocidade_inicial} VELOCIDADE MÁXIMA ATINGIDA')
                break
                
corvete = Carro("CORVETE")
corvete.acelerar(8)
corvete.desacelerar(20)
print('')
ferrari = Carro('Ferrari', 300)
ferrari.acelerar(20)
ferrari.desacelerar(40)