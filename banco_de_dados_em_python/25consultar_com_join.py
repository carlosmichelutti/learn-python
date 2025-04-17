from bd import nova_conexão
from mysql.connector.errors import ProgrammingError

sql = '''
    select
        grupos.descrição as grupo,
        contatos.nome as contato
    from contatos
    inner join grupos on contatos.grupo_id = grupos.id
    order by grupo, contato
'''

with nova_conexão() as conexão:
    try:
        cursor = conexão.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contato"]}')

