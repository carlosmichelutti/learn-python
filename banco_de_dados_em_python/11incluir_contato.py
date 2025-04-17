from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = ('Lucas', '98765-4321')

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()    
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        print('1 registro incluido, ID:', cursor.lastrowid)