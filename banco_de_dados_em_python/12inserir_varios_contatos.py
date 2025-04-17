from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = (
    ('Lucas', '98765-4321'),
    ('Marcola', '92365-4321'),
    ('Felipe', '92234-4321'),
    ('Carlos', '91325-4321'),
    ('Lucas', '98765-4230'),
    ('Joao', '99023-4321'),
    ('Jonathas', '92365-4221'),
    ('Kaike', '98123-4311'),
)
'''sql1 = 'insert into contatos (id, nome, tel) values (%s, %s, %s)'
outros_argumentos = (
    (333, 'JULIOS', '21049124124'),
)
'''

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        #cursor.execute(sql1, outros_argumentos)
        conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        print(f'Foram incluidos {cursor.rowcount} registro incluido')
