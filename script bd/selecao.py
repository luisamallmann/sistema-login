from conexao import conexao, cursor
from werkzeug.security import generate_password_hash, check_password_hash

# -- SELECT -- 

email = input("Email: ")
senha = input("Senha: ")

sql = "SELECT * FROM users WHERE email = %s"

valores = (email,);

cursor.execute(sql, valores)
resultado = cursor.fetchone()

if resultado:
 #   senha_crip = resultado[3]
    
    if check_password_hash(resultado[3], senha):
        print("Login realizado.")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")

# Fechar cursor e conexão

cursor.close()
conexao.close()