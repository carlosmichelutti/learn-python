from bd import nova_conexão
from mysql.connector import ProgrammingError

selecionar_grupo = '''
    select id from grupos where descrição = %s
'''

atualizar_contato = '''
    update contatos set grupo_id = %s where nome = %s
'''

contato_grupo = {
    'PEDRO YUKI': 'Grupo escola',
    'Felipe': 'Grupo escola',
    'Carlos': 'turminha do pagodas',
    'Joao': 'Grupo do trabalho',
    'DUZINHO': 'Grupo do trabalho',
    'Kaike': 'turminha do pagodas',
    'JULIOS': 'Grupo da viagem',
}

with nova_conexão() as conexão:
    try:
        cursor = conexão.cursor()

        for nome, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo, ))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, nome))
            conexão.commit()
        # cursor.execute(sql_2, sql2_values)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('CONTATOS ASSOCIADOS COM SUCESSO')
