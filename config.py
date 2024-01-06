import mysql.connector

conf = {
    'host' : "localhost",
    'user' : "banko",
    'password' : "BankoDev2024",
    'database' : "banking_system",
    'port' : "3306"
}

try:
    connection = mysql.connector.connect(**conf)
    if connection.is_connected():
        print('Conexion exitosa')

except mysql.connector.Error as err:
    print(f'Error: {err}')

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Conexion cerrada')