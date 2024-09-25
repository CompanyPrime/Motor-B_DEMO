import mysql.connector
from mysql.connector import errorcode

# Defina as credenciais de conexão
config = {
    'user': 'root',
    'password': 'motorbmgNqg77',  # Substitua pela sua senha
    'host': 'localhost',
}

# Inicializar a variável de conexão
connection = None

try:
    # Estabelecer conexão com o MySQL
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Comando SQL para criar um novo banco de dados
    database_name = 'novo_banco_de_dados'  # Substitua pelo nome desejado
    create_database_query = f"CREATE DATABASE {database_name};"

    # Executar o comando
    cursor.execute(create_database_query)
    print(f"Banco de dados '{database_name}' criado com sucesso.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha inválidos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não encontrado.")
    else:
        print(f"Erro: {err}")
finally:
    # Fechar a conexão se ela foi estabelecida
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
