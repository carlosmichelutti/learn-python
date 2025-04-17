from bd import nova_conexão

sql = """SELECT * FROM contatos
order by id"""

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(registro [0] + '\t \t' + registro[1] for registro in cursor))