from bd import nova_conexão
from mysql.connector import ProgrammingError

sql =  'insert into grupos (descrição) values (%s)'

valores = (
        ('Grupo do trabalho',),
        ('Grupo escola',),
        ('Grupo da viagem',),
        ('Turminha do pagodas',),
)

#sql_2 = '''
    #insert into contatos (grupo_id)
    #values( 
        #(select id from grupos where descrição = %s),
        #where nome = %s)
#'''

#sql2_values = ('Grupo do trabalho', 'Carlos')

with nova_conexão() as conexão:
    try:
        cursor = conexão.cursor()
        cursor.executemany(sql, valores)
        conexão.commit()
        #cursor.execute(sql_2, sql2_values)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    
    for pessoa in cursor:
        print(pessoa)
