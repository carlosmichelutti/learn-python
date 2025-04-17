from bd import nova_conexão
from mysql.connector import ProgrammingError

criar_tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descrição varchar(30)
    )
"""

alterar_aletar_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""
alterar_aletar_contato_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""

with nova_conexão() as conexão:
    try:
        cursor = conexão.cursor()
        cursor.execute(criar_tabela_grupo)
        cursor.execute(alterar_aletar_contato_1)
        cursor.execute(alterar_aletar_contato_2)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
