from mysql.connector import connect

conexão = connect(
    host='Localhost',
    port=3306,
    user='root',
    password='Carlos2003!'
)

cursor = conexão.cursor()
cursor.execute('Create Database IF NOT EXISTS agenda')
