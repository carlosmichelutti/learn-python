from contextlib import contextmanager
from mysql.connector import connect
from mysql.connector import ProgrammingError

parametros = dict(
    host='Localhost',
    port=3306,
    user='root',
    password='Carlos2003!',
    database='agenda'
)


@contextmanager
def nova_conexão():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
