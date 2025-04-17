from os import system
from datetime import datetime
from datetime import timedelta


class Projeto:
    def __init__(self, nome) -> None:
        self.nome_do_projeto = nome
        self.tarefas_a_fazer = []

    def __iter__(self):
        return self.tarefas_a_fazer.__iter__()
    
    def add_tarefa(self, tarefa, **kwargs):
        self.tarefas_a_fazer.append(tarefa)

    def add_nova_tarefa(self, nome, **kwargs):
        self.tarefas_a_fazer.append(Tarefas(nome, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento = None, **kwargs):
        função_escolhida = self.add_tarefa if isinstance(tarefa, Tarefas) \
        else self.add_nova_tarafa
        kwargs['vencimento'] = vencimento
        função_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa.nome for tarefa in self.tarefas_a_fazer if not tarefa.conclusão]

    def __str__(self) -> str:
        return f'- {self.nome_do_projeto} ({len(lista_de_tarefas.pendentes())}) TAREFA(S) PENDENTE(S)'


class Tarefas:
    def __init__(self, nome, expirção) -> None:
        self.nome = nome
        self.expiração = expirção
        self.data_de_criação = datetime.now()
        self.conclusão = False

    def feito(self, ):
        self.conclusão = True

    def __str__(self) -> str:
        if not self.conclusão and self.expiração > 0:
            return '-' + tarefa.nome + f'(EXPIRA EM {self.expiração}) DIAS'
        elif not self.conclusão and self.expiração <= 0:
            return '-' + tarefa.nome + f'(TAREFA VENCIDA)'
        else:
            return '-' + tarefa.nome + '(CONCLUIDA)'


class TarefaRecorrente(Tarefas):
    def __init__(self, nome, expirção, dias=7) -> None:
        super().__init__(nome, expirção)
        self.dias = dias

    def feito(self):
        super().feito()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.nome, novo_vencimento, self.dias)


while True:
    lista_de_tarefas = Projeto(
        str(input('DIGITE O PROJETO DE TAREFAS A FAZER: ')))

    while True:
        tarefa_digitada_pelo_usuário = Tarefas(str(input('DIGITE UMA TAREFA A SER CONCLUÍDA: ')),
                                               int(input('QUANTOS DIAS FALTAM PARA A TAREFA EXPIRAR? ')))

        lista_de_tarefas.add(tarefa_digitada_pelo_usuário)

        resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

        if resp == 'N':
            for tarefa in lista_de_tarefas.tarefas_a_fazer:
                resposta = str(
                    input(f'A TAREFA {tarefa.nome} FOI CONCLUÍDA? [S/N]: '))
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
