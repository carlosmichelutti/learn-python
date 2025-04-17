from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'select * from contatos LIMIT %s OFFSET %s'
args = (3, 3)

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:20s} Telefone: {contato[1]}')
