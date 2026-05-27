from conexao import conexao, cursor
from werkzeug.security import generate_password_hash, check_password_hash

# id do user a ser excluido

print("Deletar user. Pressione 0 para cancelar.")

id = int(input("Nº de user: "))
if (id != 0):
    sql = "DELETE FROM users WHERE id = %s"

    valores = (id)

    # executa o delete

    cursor.execute(sql, valores)

    # salva no banco

    conexao.commit()

    if cursor.rowcount == 0:
        print(f"Nenhum user com id {id}")
    else:
        print("User excluido com sucesso.")
else:
    print("Operação cancelada")