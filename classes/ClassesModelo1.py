class Tarefas:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.conclusão = False
    
    def feito(self, ):
        self.conclusão = True
    
    def __str__(self) -> str:
        return '-' + tarefs.nome + ('(CONCLUIDA)' if self.conclusão else '(TAREFA PENDENTE)')

listadetarefas = []   
while True: 
    tarefa_digitada_pelo_usuário = Tarefas(str(input('DIGITE UMA TAREFA A SER CONCLUÍDA: ')))
    print(tarefa_digitada_pelo_usuário.nome)
    listadetarefas.append(tarefa_digitada_pelo_usuário)
    resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
    
    if resp == 'N':
        for tarefa in listadetarefas:
            resposta = str(input(f'A TAREFA {tarefa.nome} FOI CONCLUÍDA? [S/N]: '))
            if resposta == 'S':
                tarefa.feito()

        for tarefs in listadetarefas:
            print(f'{tarefs}')
        break

    if resp != 'S':
        print('VALOR INVÁLIDO. TENTE NOVAMENTE: ')
        resp = str(input('QUER CONTINUAR? [S/N]: '))



    

