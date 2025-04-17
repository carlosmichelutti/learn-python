from bd import nova_conexão

sql = "SELECT * FROM contatos WHERE nome like '%a%'" #and 'lu%'

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
