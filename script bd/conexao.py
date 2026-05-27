import mysql.connector 

# Conexão

conexao = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database="signa"
    ) 

# Criar cursor

cursor = conexao.cursor()