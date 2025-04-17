def voto(idade):
    import datetime

    if datetime.date.today().year - idade < 16:
        return print(f'COM {datetime.date.today().year - idade} ANOS: VOTO NEGADO.')

    elif datetime.date.today().year - idade > 18:
        return print(f'COM {datetime.date.today().year - idade} ANOS: VOTO OBRIGATÓRIO.')

    elif datetime.date.today().year - idade > 65 or datetime.date.today().year - idade < 18:
        return print(f'COM {datetime.date.today().year - idade} ANOS: VOTO OPCIONAL.')
        
idade = int(input('QUAL O SEU ANO DE NASCIMENTO? '))
voto(idade)
