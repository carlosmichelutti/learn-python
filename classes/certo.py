class carro:
    def __init__(self, velocidade_maxima=180, velocidade_inicial=0, aceleração_maxima=8, desaceleração_maxima=20):
        self.velocidademaxima = velocidade_maxima
        self.velocidadeinerciamaxima = velocidade_inicial
        self.velocidadeinicial = velocidade_inicial
        self.aceleraçãomaxima = aceleração_maxima
        self.desaceleraçãomaxima = desaceleração_maxima

    def acelerar(self, acelerar=8):
        velocidade_maxima = self.velocidade_maxima
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

                    return finaly
                    break
                else:
                    return velocidadeincial
                    break

    def desacelerar(velocidade_maxima=180, velocidade_atual=0, velocidademinima=0, desaceleração_maxima=20):
        if velocidade_maxima > 0:
            velocidadeincial = velocidade_atual
            print(f'DESACELERANDO', end=' ')
            for velocidade in range(10):
                print(f'{velocidadeincial}', end=' ')
                if velocidadeincial-20 > velocidademinima:
                    velocidadeincial -= 20
                    quantofalta = velocidadeincial - velocidademinima

                elif velocidadeincial-20 > velocidademinima:
                    finaly = velocidadeincial + quantofalta
                    print(f'{finaly} VELOCIDADE MINIMA ATINGIDA!')
                    break
                else:
                    print(f'{0} VELOCIDADE MINIMA ATINGIDA!')
                    break


carro.desacelerar(velocidade_atual=carro.acelerar())
