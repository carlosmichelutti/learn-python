def notas(*num, show=False):

    media = 0
    notas = {}
    notas['quantidade_provas'] = len(num)
    notas['maior_nota'] = 0
    notas['menor_nota'] = 0
    notas['media'] = 0

    for nota in num:
        media += nota
        if notas['maior_nota'] == 0 and notas['menor_nota'] == 0:
            notas['maior_nota'] = nota
            notas['menor_nota'] = nota
        elif nota > notas['maior_nota']:
            notas['maior_nota'] = nota
        elif nota < notas['menor_nota']:
            notas['menor_nota'] = nota

    media = media/len(num)
    notas['media'] = media

    if show:
        if notas['media'] > 7:
            notas['Situação'] = 'BOA'
        elif notas['media'] > 5:
            notas['Situação'] = 'RAZOÁVEL'
        else:
            notas['Situação'] = 'RUIM'
        print(notas)
    else:
        print(notas)

notas = notas(9, 4.5, 10, 7, show=True)
