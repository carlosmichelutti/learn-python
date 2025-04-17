class Produtos:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor
        self.desconto = 0


    def imposto(self):
        if self.valor > 100:
            self.inposto = self.valor*0.05

            return self.inposto
        else:
            return self.valor
    
    def disconto(self, imposto):

        self.inposto = imposto
        self.total = self.inposto + self.valor
        if self.total > 200:
            self.desconto = self.total-(self.total*(20/100))
            return f'SEU VALOR SE ENQUADRA NO REQUERIDO PARA O DESCONTO É O TOTAL É DE {self.desconto:.2f}'
        else:
            return f'O PRODUTO NÃO SE ENQUADRA NO DESCONTO E SEU TOTAL É {self.total:.2f}'


a = Produtos('laranja',200)
b = a.imposto()
print(a.disconto(b))