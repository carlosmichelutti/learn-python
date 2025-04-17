from mysql.connector import Connection

conexão = Connection(
    host='Localhost',
    port=3306,
    user='root',
    password='Carlos2003!'
)

cursor = conexão.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor):
    print(f'BANCO DE DADOS {i}: {database[0]}')