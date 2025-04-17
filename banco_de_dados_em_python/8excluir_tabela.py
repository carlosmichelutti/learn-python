from bd import nova_conexão
from mysql.connector import ProgrammingError

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('Drop table if exists emails')
    except ProgrammingError as e:
        print(f'ERRO {e.msg}')