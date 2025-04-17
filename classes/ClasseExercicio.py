class Funcionario:
    def __init__(self, nome, cpf, salário, departamento) -> None:
        self.nome = nome
        self.cpf = cpf
        self.salario = salário
        self.departamento = departamento

  
    def bonifcar(self):
        self.salario = self.salario + (self.salario*(10/100))
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salário, departamento, senha) -> None:
        super().__init__(nome, cpf, salário, departamento)
        self.numero_de_funcionarios_gerennciados = []
        self.funcionários = []
        self.senha_de_gerente = senha
    
    def add(self, funcionário):
        return self.funcionários.append(funcionário)

    def comparar(self, funcionário, senha_do_funcionário):
        if self.senha_de_gerente == senha_do_funcionário:
            self.numero_de_funcionarios_gerennciados.append(funcionário)
            return self.numero_de_funcionarios_gerennciados
        else:
            return self.numero_de_funcionarios_gerennciados

    def bonificarr(self):
        if self.numero_de_funcionarios_gerennciados > 3:
            self.salario = self.salario + (self.salario*(20/100))
        else:
            self.salario = self.salario + (self.salario*(10/100))
        return self.salario
    
    def __str__(self) -> str:
        return f'O GERENTE {self.nome} ADMINISTRA {len(self.numero_de_funcionarios_gerennciados)} FUNCIONÁRIOS E RECEBE R${self.salario} REAIS'
    

funcionário_um = Funcionario('RICARDO', 2143141233, 2900, 'FÁBRICA')
funcionário_dois = Funcionario('MARCELO', 2091248321, 3000, 'EMCARREGADO')
funcionário_três = Funcionario('FELIPE', 82983921213, 5000, 'OPERADOR DE MÁQUINA')
gerente = Gerente('Guilherme', 2143123213, 10000, 'GERENCIA', 1234)
gerente.add(funcionário_um)
gerente.add(funcionário_dois)
gerente.add(funcionário_três)
gerente.comparar(funcionário_um, 1234)
gerente.comparar(funcionário_dois, 1234)
gerente.comparar(funcionário_três, 1222)
gerente.bonifcar()
print(gerente.__str__())


