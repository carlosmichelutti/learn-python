from bd import nova_conexão
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(nome varchar(50), tel varchar(40))
"""

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id int auto_increment primary key,
        dono varchar(50)
    )
"""

with nova_conexão() as conexão:
    try:
        cursor = conexão.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

    