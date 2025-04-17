from os import system
from datetime import datetime
from datetime import timedelta


'''PRIMEIRO INICIALIZAMOS O MODELO(CLASSE) PROJETO QUE RECEBERÁ NADA MAIS DO QUE O NOME DO PROJETO DE TAREFAS E CRIRARÁ UMA LISTA VAZIA PARA 
ARMAZERNAR ESSAS TAREFAS.'''

class Projeto:
    def __init__(self, nome) -> None:
        self.nome_do_projeto = nome
        self.tarefas_a_fazer = []

# USAMOS O MÉTODO __ITER__ PARA RETORNAR O ITERAVEL DA LISTA, PODENDO SER UTILIZADO DE FORMA MAIS SIMPLES EM LOOPS.
    def __iter__(self):
        return self.tarefas_a_fazer.__iter__()

# CRIAMOS O MÉTODO 'ADD' PARA RECEBER COMO PARÂMETRO APENAS A TAREFA E ADICIONÁ-LÁ NA LISTA CRIADA E INICIALIZADA PELA CLASSE PROJETO.
    def add(self, tarefa):
        self.tarefas_a_fazer.append(tarefa)

# CRIAMOS O MÉTODO PENDENTES QUE IRÁ PERCORRER O ITERÁVEL RETORNADO DA LISTA tarefaz_a_fazer E RETORNAR APENAS AS TAREFAS QUE NÃO ESTÃO
# CONCLUÍDAS(tarefa.conclusão) PARA PRINTAR ELAS COM VISUAL DE PENDENTES.
    def pendentes(self):
        return [tarefa.nome for tarefa in self.tarefas_a_fazer if not tarefa.conclusão]

    def __str__(self) -> str:
        return f'- {self.nome_do_projeto} ({len(lista_de_tarefas.pendentes())}) TAREFA(S) PENDENTE(S)'

# INICIALIZAMOS OUTRA CLASSE AGORA QUE SERÁ O MODELO DE CADA TAREFA DIGITADA PELO USUÁRIO, QUE PASSARÁ SEU NOME E O VENCIMENTO(QUANTOS DIAS
# FALTAM PARA A TAREFA EXPIRAR)
class Tarefas:
    def __init__(self, nome, expirção) -> None:
        self.nome = nome
        self.expiração = expirção
        self.data_de_criação = datetime.now()
        self.conclusão = False

# CRIAMOS O MÉTODO FEITO QUE APENAS CONCLUÍRA(COLOCARÁ TRUE NO SELF.CONCLUSÃO) A TAREFA QUE FOI DIGITADA PELO USUÁRIO COMO CONCLUIDA.

    def feito(self):
        self.conclusão = True

# CRIAMOS O MÉTODO ESPECIAL __str__ QUE RETORNARÁ CONFORME A CONCLUSÃO E O VENCIMENTO SE A TAREFA FOI CONCLUÍDA OU NÃO E SE NÃO FOI MOSTRAR SE
# ELA VENCEU OU QUANTOS DIAS FALTAM PARA ELA EXPIRAR.
    def __str__(self) -> str:
        if not self.conclusão and self.vencimento > 0:
            return '-' + tarefa.nome + f'(EXPIRA EM {self.vencimento}) DIAS'
        elif not self.conclusão and self.vencimento <= 0:
            return '-' + tarefa.nome + f'(TAREFA VENCIDA)'
        else:
            return '-' + tarefa.nome + '(CONCLUIDA)'

'''class TarefaRecorrente(Tarefas):
    def __init__(self, nome, expirção, dias=7) -> None:
        super().__init__(nome, expirção)
        self.dias = dias
    
    def feito(self):
        super().feito()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.nome, novo_vencimento, self.dias)'''

# INICIO DO PRIMEIRO LAÇO WHILE TRUE PARA CADA PROJETO DE TAREFAS DIGITADO
while True:
    lista_de_tarefas = Projeto(
        str(input('DIGITE O PROJETO DE TAREFAS A FAZER: ')))

# INICIO DO SEGUNDO LAÇO TRUE PARA CADA TAREFA DO PROJETO
    while True:

        # AQUI ONDE O USUÁRIO DIGITARÁ AS TAREFAS E O TEMPO EM DIAS PRA ELA EXPIRAR.
        tarefa_digitada_pelo_usuário = Tarefas(str(input('DIGITE UMA TAREFA A SER CONCLUÍDA: ')), int(
            input('QUANTOS DIAS FALTAM PARA A TAREFA EXPIRAR? ')))
        lista_de_tarefas.add(tarefa_digitada_pelo_usuário)

        resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

# CASO NÃO TENHA MAIS NENHUMA TAREFA A SER CADASTRADA O USUÁRIO DEVERÁ DIGITAR SE A TAREFA FOI OU NÃO CONCLUÍDA E CASO TENHA SIDO A TAREFA
# CHAMARÁ O MÉTODO FEITO() E RECEBERÁ TRUE EM SEU SELF.CONCLUSÃO
        if resp == 'N':
            for tarefa in lista_de_tarefas:
                resposta = str(
                    input(f'A TAREFA {tarefa.nome} FOI CONCLUÍDA? [S/N]: '))
                if resposta == 'S':
                    tarefa.feito()

# PRINTANDO A LISTA DE TAREFAS E CADA TAREFA COM SEU STATUS LOGO EM SEGUIDA(FEITO, EXPIRA EM OU VENCIDA)
            system('cls')
            print(f'{lista_de_tarefas}')
            for tarefa in lista_de_tarefas:
                print(f'{tarefa}')
            break

        elif resp != 'S':
            print('VALOR INVÁLIDO. TENTE NOVAMENTE: ')
            resp = str(input('QUER CONTINUAR? [S/N]: '))

    outroprojeto = str(input('TEM OUTRO PROJETO DE TAREFAS? [S/N] '))

    if outroprojeto == 'N':
        break
