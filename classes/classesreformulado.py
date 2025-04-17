class carro:
    def __init__(self, velocidade_maxima):
        self.velocidademaxima = velocidade_maxima
        self.velocidadeinicial = 0

    def acelerar(self, acelerar=8):
        velocidade_maxima = self.velocidademaxima

        if velocidade_maxima > 0:
            velocidadeincial = 8
            print(f'ACELERANDO', end=' ')
            for velocidade in range(25):
                print(f'{velocidadeincial}', end=' ')
                if velocidadeincial+8 < velocidade_maxima:
                    velocidadeincial += 8
                    quantofalta = velocidade_maxima - velocidadeincial

                elif velocidadeincial+8 > velocidade_maxima:
                    finaly = velocidadeincial + quantofalta
                    print(f'{finaly} VELOCIDADE MÁXIMA ATINGIDA!')
                    break
                else:
                    break

    def desacelerar(self,  desaceleração_maxima=20):
        velocidademaxima = self.velocidademaxima
        velocidadeatual = self.velocidadeinicial
        velocidadeinicial = self.velocidadeinicial

        if velocidademaxima > 0:
            velocidadeatual = velocidademaxima
            print(f'DESACELERANDO', end=' ')
            for velocidade in range(10):
                print(f'{velocidadeatual}', end=' ')
                if velocidadeatual-20 > velocidadeinicial:
                    velocidadeatual -= 20
                    quantofalta = velocidadeatual - velocidadeinicial

                elif velocidadeatual-20 > velocidadeinicial:
                    finaly = velocidadeatual + quantofalta
                    print(f'{finaly} VELOCIDADE MINIMA ATINGIDA!')
                    break
                else:
                    print(f'{0} VELOCIDADE MINIMA ATINGIDA!')
                    break


c1 = carro(180)
c1.acelerar()
c1.desacelerar()
