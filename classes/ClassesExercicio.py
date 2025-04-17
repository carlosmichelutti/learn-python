from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def é_adulto(self):
        if self.idade > 0:
            if self.idade >= 18:
                return True
            else:
                return False
        else:
            return False

    def __str__(self) -> str:
        if not self.idade:
            return self.idade
        return f'{self.nome} ({self.idade}anos)'
        
def get_data(compra):
    return compra.data

class Cliente(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)
        self.compras = []
    
    def registrar_compra(self, compra):
        self.compras.append(compra)
    
    def get_data_da_ultima_compra(self):
        if not self.compras:
            return None
        else:
            self.compras = sorted(self.compras, key=get_data)[-1].data
            return self.compras

    def total_de_compras(self):
        self.soma = 0
        for compra in self.compras:
            self.soma += compra.valor
        return self.soma.__str__()

    def __str__(self) -> str:
        return super().__str__()
    
class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario_do_vendedor) -> None:
        super().__init__(nome, idade)
        self.salário = salario_do_vendedor

class Compra:
    def __init__(self, vendedor, data, valor) -> None:
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

Cliente1 = Cliente('MARCOS', 40)
vendedor = (Vendedor('Rafael', 34, 4000))
compra_celular = Compra(vendedor, datetime.now(), 900)
compra_bolsa_escolar = Compra(vendedor, datetime.now(), 100)
Cliente1.registrar_compra(compra_celular)
Cliente1.registrar_compra(compra_bolsa_escolar)
Cliente1.total_de_compras
print(f'Cliente: {Cliente1.nome} {Cliente1.idade} anos' ' (adulto)' if Cliente1.é_adulto() else '')
print(f'Vendedor: {vendedor.nome} {vendedor.idade}')

valor_total = Cliente1.total_de_compras()
quantidade_de_compras = len(Cliente1.compras)
print(f'TOTAL: {valor_total} EM {quantidade_de_compras} COMPRAS')
print(f'DATA DA ÚLTIMA COMPRA: {Cliente1.get_data_da_ultima_compra()}')



