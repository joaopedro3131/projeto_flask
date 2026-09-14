
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
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('SELECT id, nome, disciplina FROM professor')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('professor/lista.html', lista=lista)



@app.route('/turma')
def lista_turma():
    # Conecta ao banco de dados
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('select turma.id, semestre, curso.nome_curso, professor.nome from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id')
    # Obtém todos os registros
    lista = []
    #cursor.fetchall()
    # Fecha conexão
    conn.close()
    return render_template('turma/lista.html', lista=lista)



@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)