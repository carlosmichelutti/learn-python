from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'select nome, tel from contatos'

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    for contato in cursor.fetchall():
        print('\t \t'.join(str(campo) for campo in contato))
