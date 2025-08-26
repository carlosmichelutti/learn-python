from datetime import datetime

year = datetime.today().year
sexo = str(input('Digite o seu gênero [M/F]: ')).upper()

if sexo == 'F':
    print('Você não é obrigada a se alistar no exercito. Até mais!')
else:
    ano_nascimento = int(input('Em que ano você nasceu? '))
    diferença = year - ano_nascimento
    if year - ano_nascimento < 18:
        print(f'Você ainda não tem idade para se alistar ao exercito. Só poderá se alistar em {abs(diferença - 18)} anos. Seu alistamento será em {ano_nascimento + 18}.')
    elif year - ano_nascimento == 18:
        print('Você está em idade de se alistar ao exercito. Não esqueça.')
    elif year - ano_nascimento > 18:
        print(f'Aliste-se já! Você está atrasado com seu seriviço militar em {diferença - 18} anos. O seu alistamento obrigatório foi em {ano_nascimento + 18}.')
