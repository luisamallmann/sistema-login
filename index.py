from flask import Flask, render_template, request
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# cria a aplicação flask

app = Flask(__name__)
app.secret_key = "123"

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if(request.method=='GET'):
        return render_template('cadastro.html')
    else:
        conexao = mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="", 
            database="signa"
            )
        
        # Criar cursor
         
        cursor = conexao.cursor()

        nome = request.form['nome']
        email = request.form['email']
        senha1 = request.form['senha1']
        senha2 = request.form['senha2']

        if senha1 != senha2:
            return render_template('cadastro.html', erro='As senhas não coincidem')
        
        senha_hash = generate_password_hash(senha1)

        sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql,(email,))

        resultados = cursor.fetchall()

        if len(resultados) > 0:
            cursor.close()
            conexao.close()
            return render_template('cadastro.html', erro='Email já cadastrado')
        
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        valores = (nome, email, senha_hash)

        # executa insert
         
        cursor.execute(sql, valores)
        
        # salva no banco
        
        conexao.commit()

        # fechar cursor e conexão

        cursor.close()
        conexao.close()

        return """<p>Cadastro realizado com sucesso<p>
        <a href="/">
        <button>Voltar para página inicial</button>
        </a>"""

if __name__=='__main__':
    app.run(debug=True)