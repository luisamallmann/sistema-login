from conexao import conexao, cursor
from werkzeug.security import generate_password_hash, check_password_hash

# --- INSERT ---

print("Criar usuário")

nome = input("Nome: ")
email = input("Email: ")
senha = input("Senha: ")

senha_crip = generate_password_hash(senha)
    
sql = "INSERT INTO users SET name = %s, email = %s, password = %s"
    
valores = (nome, email, senha_crip)
    
# executa insert
    
cursor.execute(sql, valores)
    
# salva no banco
     
conexao.commit()