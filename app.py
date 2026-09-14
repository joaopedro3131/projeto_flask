
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/aluno')
def lista_aluno():
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    return render_template('professor/lista.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)