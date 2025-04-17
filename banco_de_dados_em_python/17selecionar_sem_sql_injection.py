from bd import nova_conexão

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexão() as conexao:
    nome = input('CONTATO A LOCALIZAR: ')
    args = (f'%{nome}%',)
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)