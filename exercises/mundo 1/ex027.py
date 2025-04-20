resposta = str(input('Você deseja fazer um empréstimo? [S/N] ')).upper().strip()
 
if resposta == 'S':
    valor_total = float(input('Qual o valor total da casa? R$'))
    salario =  float(input('Qual é o seu salário? R$'))
    anos = int(input('Em quantos anos você quer realizar o pagamento total? '))
    prestacao_mensal = valor_total / anos / 12

    if prestacao_mensal > (salario * 0.30):
        print('Erro! Você não pode realizar esse emprestimo, pois ele ultrapassa 30% do seu salário mensal.')
    else:
        print(f'Você pode realizar esse empréstimo, e terá de pagar R${prestacao_mensal:.2f} reais por mês durante {anos} anos.')
else: 
    print('Obrigado, até mais!')
