from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = '''
    Update contatos 
    set nome = %s
    WHERE id = %s
'''
argumentos = ('DUZINHO', '10')

sql_view = '''SELECT * FROM contatos'''

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql, argumentos)
    conexao.commit()
    cursor.execute(sql_view)

    for contato in cursor:
        print(f'{contato[2]} - {contato[0]} - {contato[1]}')
