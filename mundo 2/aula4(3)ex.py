maioresde18 = 0
qtdmulheres = 0
qtdhomens = 0

#INICIO DA CONDIÇÃO INFINITA=================================================================================

while True:
        idade = int(input('QUANTOS ANOS VOCÊ TEM? '))
        while True: 
            sexo = str(input('QUAL É O SEU SEXO [M/F]? ')).upper().strip()
            if sexo == 'M' or sexo == 'F':
                break
            
        print('=+='*10)

    #VALIDANDO AS INFORMAÇÕES =================================================================================

        if idade > 18:
            maioresde18 = maioresde18 + 1

        if sexo == 'M':
            qtdhomens =  qtdhomens + 1

        if sexo == 'F' and idade < 20:
            qtdmulheres = qtdmulheres + 1

    #CONDIÇÃO PARA O LOOP INFINITO CONTINUAR OU PARAR ============================================================================

        resp = str(input('VOCÊ QUER CONTINUAR [S/N]? ')).upper().strip()
        print('=+='*10)

    #VERIFICANDO SE O LOOP DEVE TERMINAR OU NÃO =================================================================================

        if resp == "N":

    #ESCREVENDO AS INFORMAÇÕES COLETADAS ATÉ O MOMENTO ===========================================================================
            
            print('FORAM DIGITADOS {} HOMENS COM MAIS DE 18 ANOS.'.format(maioresde18))
            print('FORAM DIGITADOS {} HOMENS.'.format(qtdhomens))
            print('FORAM DIGITADOS {} MULHERES QUE TEM MENOS DE 20 ANOS.'.format(qtdmulheres))
            break

    #VERIFICANDO SE A RESPOSTA PRO LOOP FOI DIFERENTE DE 'S' PARA QUE SEJA DADA RESPOSTA INVALIDA ===========================================================================

        elif resp != 'S':
            print('RESPOSTA INVALIDA! TENTE NOVAMENTE.')
            print('=+='*10)
            resp = str(input('VOCÊ QUER CONTINUAR [S/N]? ')).upper().strip()
            print('=+='*10)
