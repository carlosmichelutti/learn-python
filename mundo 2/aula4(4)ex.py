soma = 0
qtddeprodutos = 0
qtdmaiorque1000 = 0
valordomenor = 0
nomedomenor = ''
menor = 0
while True:
    nome = str(input('QUAL O NOME DO PRODUTO? '))
    valor = float(input('QUAL O VALOR DO PRODUTO? R$'))
    print("")

    soma = soma + valor
    qtddeprodutos = qtddeprodutos + 1
    
    if valor > 1000:
        qtdmaiorque1000 = qtdmaiorque1000 + 1
    
    if qtddeprodutos == 1:
        menor = valor

    if valor < menor:
        nomedomenor = nome
        valordomenor = valor


    resp = str(input('VOCÊ QUER CONTINUAR [S/N]? ')).upper().strip()   
    print("")

    if resp != 'N' and resp != 'S':
        print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE: ')
        print("")
        resp = str(input('VOCÊ QUER CONTINUAR [S/N]? ')) 
        print("")   

    if resp == 'N':

        print('=+='*10)
        print('FIM DO PROGRAMA')

        print('O VALOR TOTAL GASTO NA COMPRA DOS {} PRODUTOS FOI R${} REAIS'.format(qtddeprodutos, soma))
        print('FORAM DIGITADOS {} PRODUTOS QUE CUSTAM MAIS DE R$1000,00'.format(qtdmaiorque1000))
        print('O PRODUTO MAIS BARATO DIGITADO FOI O {} QUE CUSTA R${} REAIS.'.format(nomedomenor, valordomenor))

        break