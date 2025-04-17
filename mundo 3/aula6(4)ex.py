def notas(*num, show=False):
    """
    *NUM -> PARAMETRO ADAPTÁVEL, QUE RECEBE VÁRIAS VARIÁVEIS SEM PRÉ EXPECIFICAÇÃO DE QUANTIDADE.
    SHOW -> VALOR BOOLEANO DIZENDO SE MOSTRA OU NÃO A SITUAÇÃO.
    NOTAS DICIONARIO -> DICIONARIO ONDE SERÁ GUARDADA AS INFORMAÇÕES.
    QTD DE NOTAS -> QUANTIDADE DE NOTAS AO TOTAL REGISTRADAS.
    MAIORNOTA -> MAIOR NOTA REGISTRADA.
    MENORNOTA -> MENOR NOTA REGISTRADA.
    MÉDIA -> MÉDIA DE TODAS AS NOTAS DIVIDIDO PELA QUANTIDADE DE NOTAS.

    """
    media = 0

    notasdicionario = {}

    notasdicionario['QtdNotas: '] = len(num)
    notasdicionario['MaiorNota: '] = 0
    notasdicionario['MenorNota: '] = 0
    notasdicionario['Média'] = 0

    for notaindv in num:
        if notasdicionario['MaiorNota: '] == 0 and notasdicionario['MenorNota: '] == 0:
            notasdicionario['MaiorNota: '] = notaindv
            notasdicionario['MenorNota: '] = notaindv

        elif notaindv > notasdicionario['MaiorNota: ']:
            notasdicionario['MaiorNota: '] = notaindv
        
        elif notaindv < notasdicionario['MenorNota: ']:
            notasdicionario['MenorNota: '] = notaindv
    
    for notas in num:
        media += notas
    media = media/len(num)
    notasdicionario['Média'] = media

    if show:

        if notasdicionario['Média'] > 7:
            notasdicionario['Situação'] = 'BOA'
        
        elif notasdicionario['Média'] > 5:
            notasdicionario['Situação'] = 'RAZOÁVEL'

        else:
            notasdicionario['Situação'] = 'RUIM'

        print(notasdicionario)

    else:

        print(notasdicionario)


notax = notas( 9, 4.5, 10, 7, show=True)