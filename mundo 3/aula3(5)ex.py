
listaalunosenotas = []
auxiliar = []
notas = []


while True: 

#PERGUNTANDO O NOME DO ALUNO E COLOCANDO NA LISTA AUXILIAR ----------------------------------------------------

    auxiliar.append(str(input('QUAL O NOME DO ALUNO? ')).upper().strip())

#PERGUNTANDO AS DUAS NOTAS DO ALUNO E GUARDANDO NA LISTA AUXILIAR E PASSANDO DA AUXILIAR PARA A PRINCIPAL ----

    for c in range (0, 2):
        notas.append(float(input(f'NOTA {c}: ')))
    auxiliar.append(notas[:])
    listaalunosenotas.append(auxiliar[:])
    auxiliar.clear()
    notas.clear()
    
#VERIFICANDO SE A PESSOA QUER CADASTRAR MAIS OUTRO ALUNO OU NÃO --------------------------------------------

    resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()

#MOSTRANDO O CABEÇALHO DO BOLETIM ---------------------------------------------------------------------------

    if resp == 'N':
            
        print('='*30)
        print('{:<10}'.format('Nº ALUNO: '), end='')
        print('{:^10}'.format('NOME: '), end='')
        print('{:>10}'.format('MÉDIA:  '))
        print('='*30)
        print('')
    

#MOSTRANDO O NÚMERO, O NOME E A MÉDIA DE CADA ALUNO USANDO UM FOR INDO DE 0 ATÉ O LEN DA LISTA, OU SEJA, ATÉ O 
#TANTO DE ALUNOS QUE TEM NA LISTA CADASTRADOS

        for aluno in range(0, len(listaalunosenotas)):
            print(f'{aluno:<10}', end='')
            print(f'{listaalunosenotas[aluno][0]:^10}', end='')

#CHAMANDO DA LISTA PRIMARIA O PRIMEIRO ALUNO E DELE CHAMANDO SUA SEGUNDA LISTA QUE SÃO SUAS NOTAS E ASSIM 
#CHAMANDO SUA NOTA 1(0) E SUA NOTA 2 (1)

            media = (listaalunosenotas[aluno][1][0] + listaalunosenotas[aluno][1][1]) /2
            print(f'{media:>10}')
    break

#PERGUNTANDO DE QUAL ALUNO A PESSOA QUER MOSTRAR AS NOTAS ----------------------------------------------

while True:
    mostrarnota = int(input('QUER MOSTRAR NOTA DE QUAL ALUNO? [999 INTERROMPE]: '))

#SE A RESPOSTA FOR IGUAL A 999 O LOOP ENCERRA --------------------------------------------------------

    if mostrarnota == 999:
        print('FINALIZANDO...')
        break
        

#PRINTANDO PUXANDO DA LISTA DIRETO O NÚMERO QUE O USUARIO DIGITOU E MOSTRANDO DESSE ALUNO O SEU NOME LISTA [0]
#E SUAS NOTAS LISTA [1]

    elif mostrarnota <= len(listaalunosenotas) - 1:
        print(f'AS NOTAS DO ALUNO {listaalunosenotas[mostrarnota][0]} FORAM {listaalunosenotas[mostrarnota][1]}')
            
    elif mostrarnota > len(listaalunosenotas) - 1:
        print('O ALUNO REQUERIDO NÃO EXISTE, TENTE NOVAMENTE.')
        

#CASO A CONTINUAÇÃO DE CADASTRO TENHA ALGUM MISSCLICK OU VALOR INVALIDO ------------------------------------

    elif resp != 'S':
        print('RESPOSTA INVÁLIDA! TENTE NOVAMENTE.')
        resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()
        




