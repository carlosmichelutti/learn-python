from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'ALTER TABLE contatos ADD COLUMN id int auto_increment primary key'

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')