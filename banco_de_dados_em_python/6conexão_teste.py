from bd import nova_conexão

with nova_conexão() as conexão:
    if conexão.is_connected():
        print('Conectado')
