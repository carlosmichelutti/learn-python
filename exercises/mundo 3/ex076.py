from datetime import datetime

def verificar_obrigatoriedade_voto(ano_nascimento: int) -> None:

    if (datetime.today().year - ano_nascimento) < 16:
        print(f'Com {datetime.today().year - ano_nascimento} anos: voto negado.')
        return
    elif (datetime.today().year - ano_nascimento) >= 18 and (datetime.today().year - ano_nascimento) <= 65:
        print(f'Com {datetime.today().year - ano_nascimento} anos: voto obrigatório.')
        return
    else:
        print(f'Com {datetime.today().year - ano_nascimento} anos: voto opcional.')
        return
        
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
verificar_obrigatoriedade_voto(ano_nascimento)
