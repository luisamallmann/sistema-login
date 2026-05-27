from conexao import conexao, cursor
from werkzeug.security import generate_password_hash, check_password_hash

# --- UPDATE ---

print("Atualizar usuário. Digite 0 para cancelar")

id = int(input("Nº de user: "))
if (id != 0):
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    senha_crip = generate_password_hash(senha)
    
    sql = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"
    
    valores = (nome, email, senha_crip, id)
    
    # executa update
    
    cursor.execute(sql, valores)
    
    # salva no banco
     
    conexao.commit()
    
    if cursor.rowcount == 0:
        print(f"Nenhum user encontrado com id {id}")
else:
    print("Operação cancelada.")