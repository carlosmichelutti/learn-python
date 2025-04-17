from os import system

class Projeto:
    def __init__(self, nome) -> None:
        self.nome_do_projeto = nome
        self.tarefas_a_fazer = []
    
    def add(self, tarefa):
        self.tarefas_a_fazer.append(tarefa)
    
    def pendentes(self):
        return [tarefa.nome for tarefa in self.tarefas_a_fazer if not tarefa.conclusão]

    
    def __str__(self) -> str:
        return f'- {self.nome_do_projeto} ({len(lista_de_tarefas.pendentes())}) TAREFA(S) PENDENTE(S)'

class Tarefas:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.conclusão = False

    def feito(self, ):
        self.conclusão = True

    def __str__(self) -> str:
        return '-' + tarefa.nome + ('(CONCLUIDA)' if self.conclusão else '(TAREFA PENDENTE)')

while True:
    lista_de_tarefas = Projeto(str(input('DIGITE O PROJETO DE TAREFAS A FAZER: ')))

    while True:
        tarefa_digitada_pelo_usuário = Tarefas(str(input('DIGITE UMA TAREFA A SER CONCLUÍDA: ')))
        lista_de_tarefas.add(tarefa_digitada_pelo_usuário)

        resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

        if resp == 'N':
            for tarefa in lista_de_tarefas.tarefas_a_fazer:
                resposta = str(input(f'A TAREFA {tarefa.nome} FOI CONCLUÍDA? [S/N]: '))
                if resposta == 'S':
                    tarefa.feito()

            system('cls')
            print(f'{lista_de_tarefas}')
            for tarefa in lista_de_tarefas.tarefas_a_fazer:
                print(f'{tarefa}')
            break

        elif resp != 'S':
            print('VALOR INVÁLIDO. TENTE NOVAMENTE: ')
            resp = str(input('QUER CONTINUAR? [S/N]: '))


    outroprojeto = str(input('TEM OUTRO PROJETO DE TAREFAS? [S/N] '))
        
    if outroprojeto == 'N':
            break

