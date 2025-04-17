#criação da classe com a palavra reservada CLASS

class Funções:
#INICIALIZANDO O CONSTRUTOR DO OBJETO ---------------------------------------------
    def __init__(self, a=0, b=0) -> None:
        self.a: int = a
        self.b: int = b

#CHAMANDO O PRIMEIRO METÓDO DENTRO DA CLASSE PASSANDO SEMPRE O SELF ENTRE PARENTESES E CASO PRECISE DE OUTRO PARÂMETRO, PASSAR ELE APOS A VIRUGLA.
    
    def soma(self):
        return self.a + self.b

#CHAMANDO O SEGUNDO METODO DA NOSSA CLASSE QUE É UMA SIMPLES VERIFICAÇÃO SE O PRIMEIRO NÚMERO É MAIOR QUE 5 E PASSANDO O SELF E MAIS NENHUM
#PARÂMETRO    

    def verifica(self):
        self.valor = self.a
        if self.valor > 5:
            print('MAIOR QUE 5')
        else:
            print('NÃO É MAIOR QUE 5')

#CHAMANDO O TERCEIRO METODO CHAMADO POTENCIA, ONDE PASSAMOS O SELF E MAIS O EXPONENCIAL DO CÁLCULO QUE SE NAO FOR PASSADO SEU VALOR DEFALUT É 0
#E RETORNANDO O RESULTADO DESSE CÁLCULO

    def potencia(self, exponencial=0):
        self.exponencial = self.a ** exponencial
        return self.exponencial

#CHAMAMOS MAIS UMA FUNÇÃO CHAMADA DE ÁREA, ONDE RECEBEMOS O SELF COMO PARÂMETRO E CHAMAMOS OS 2 ARGUMENTOS INICIAIS CONSTRUIDOS COM O __INIT__
#E RETORNAMOS A MULTIPLICAÇÃO DESSES 2 NÚMEROS

    def area(self):
        self.ladoa = self.a
        self.ladob = self.b

        return f'A ÁREA DO LOCAL É DE {self.ladoa*self.ladob}M²'

#CHAMAMOS UMA CLASSE FILHO HERDADA DA FUNÇÃO PRIMARIA FUNÇÕES, HERDANDO TODO SEU CONSTRUTOR IGUALMENTE E INICIALIZANDO ELES IGUAL

class FunçõesFilho(Funções):
    def __init__(self, d, a=0, b=0) -> None:
        super().__init__(a, b)
        self.divisor = d

    def divisão(self):
        self.aa = self.a
        self.bb = self.b
        soma = self.aa+self.bb
        division = self.aa+self.bb/self.divisor
        return f'{division:.2f}'

a= Funções(11, 10)
a.verifica()
print(a.soma())
print(a.potencia(3))
print(a.area())
ab = FunçõesFilho(10, 11, 10)
print(ab.divisão())



