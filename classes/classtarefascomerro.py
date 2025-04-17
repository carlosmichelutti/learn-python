from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criação = datetime.now()

    def concluir(self, feito=False):
        if feito:
            print(f'- {self} TAREFA CONCLUIDA! ')
        else:
            print(f'- {self} TAREFA INCOMPLETA!')

    def __str__(self):
        return self.descricao + ('(CONCLUIDA)' if self.feito else '')


casa = []
casa.append(Tarefa("PASSAR ROUPA"))
casa.append(Tarefa("LAVAR PRATO"))
casa.append("LIMPAR A CASA")
casa.append('DAR BANHO NO CACHORRO')

for tarefa in casa:
    if tarefa == "LAVAR PRATO":
        tarefa.concluir(feito=True)
    else:
        tarefa.concluir(tarefa, feito=False)
