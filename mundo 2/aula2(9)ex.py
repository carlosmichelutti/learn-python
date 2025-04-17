from os import system

maioridade = 0
idadenova = 0
qtdmulheres = 0

for c in range (1, 5):

#questionario basico com todos os membros do grupo

    print('=+='*18)
    sexo = str(input('QUAL É O SEU SEXO? [MASCULINO/FEMININO]? ')).upper().strip()
    nome = str(input('QUAL É O SEU NOME? ')).strip().upper()
    idade = int(input('QUANTOS ANOS VOCÊ TEM {}? '.format(nome)))

#limpatela

    system('cls') or None

#verificação mulheres de menos de 20 anos

    if sexo == 'FEMININO' and idade < 20:
        qtdmulheres = qtdmulheres + 1

#verificação e armazenagem do nome do homem com maior idade dentre os 4 do grupo

    if sexo == 'MASCULINO' and idade > maioridade:
        idademaior = idade
        homemmaioridade = nome

#soma da antiga idade com a nova para calculo da média

    idadenova =  idadenova + idade


#calculando a média de idade

    media = idadenova/4

#escrevendo as informações

print('MÉDIA DE IDADE DO GRUPO: {:.1f}'.format(media))
print('HOMEM COM MAIOR IDADE: {} COM {} ANOS.'.format(homemmaioridade, idademaior))
print('MULHERES COM MENOS DE 20 ANOS: {}.'.format(qtdmulheres))




