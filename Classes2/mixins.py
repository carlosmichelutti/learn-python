class HtmlToStringMixin:
    def __str__(self) -> str:
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def __str__(self) -> str:
        return self.nome

class Animal:
    def __init__(self, nome, pet=True) -> None:
        self.nome = nome
        self.pet = pet
    
    def __str__(self) -> str:
        return self.nome + '(pet)' if self.pet else ''
    
class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass

class AnimalHtml(HtmlToStringMixin, Animal):
    pass

p1 = Pessoa('Maria Eduarda')
print(p1)

p2 = PessoaHtml('Roberto Carlos')
print(p2)

dog = AnimalHtml('Thor')
print(dog)
