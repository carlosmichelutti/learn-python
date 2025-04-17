from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

'''
RISCO DE SQL INJECTION
sql = """DELETE FROM contatos 
WHERE nome = 'Lucas'
"""
'''

sql = '''
    DELETE FROM contatos 
    WHERE nome = %s
'''

argumentos = ('Lucas',)

sql_view = '''SELECT * FROM contatos'''

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, argumentos)
        conexao.commit()
        #cursor.execute(sql_view)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros deletados.')
