from bd import nova_conexão
from mysql.connector import ProgrammingError

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute('show tables')

    for  i, database in enumerate(cursor, start=1):
        print(f'Tabela {i}: table: {database[0]}')