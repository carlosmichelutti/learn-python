valor = float(input('QUAL O VALOR NORMAL DO PRODUTO? '))
print('=+='*30)
print('''QUAL A CONDIÇÃO DE PAGAMENTO? \n
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA NO CARTÃO
[3] EM 2X NO CARTÃO
[4] EM 3X OU MAIS NO CARTÃO\n''')
condiçãodepagamento = int(input('DIGITE ALGUMA OPÇÃO: '))

if condiçãodepagamento == 1:
    print('O VALOR A SER PAGO PELO PRODUTO TERÁ UM DESCONTO DE 10% E O NOVO VALOR A SER PAGO É DE R${:.2f}.'
    .format(valor-(valor*(10/100))))

elif condiçãodepagamento == 2:
    print('O VALOR TOTAL A SER PAGO TERÁ UM DESCONTO DE 5% E SEU NOVO VALOR É DE R${:.2f}.'
    .format(valor-(valor*(5/100))))

elif condiçãodepagamento == 3:
    totparc = int(input('VOCÊ VAI PARCELAR EM QUANTAS VEZES?'))
    print('Você irá pagar {} vezes de R${:.2f} reais.'.format(totparc, valor/totparc))
    print('O VALOR NÃO TERÁ NENHUM DESCONTO NEM JUROS, SEU VALOR TOTAL A SER PAGO É DE R${:.2f}.'.format(valor))

elif condiçãodepagamento == 4:
        totparc = int(input("EM QUANTAS PARCELAS SERÁ PAGO?"))
        print('Você deverá pagar {} divido em {} vezes dará {:.2f} parcelas de R${}'
            .format(valor+(valor*(20/100)), totparc, totparc, (valor+(valor*(20/100)))/totparc))
        print('O VALOR A SER PAGO SOFRERÁ UM JUROS ACRESCIDOS DE 20% E SEU VALOR TOTAL A SER PAGO É DE R${:.2f}.'
            .format(valor+(valor*(20/100))))