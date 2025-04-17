from mysql.connector import Connection

conexão = Connection(
    host = 'Localhost',
    port = 3306,
    user = 'root',
    password = 'Carlos2003!'
)

print(conexão)