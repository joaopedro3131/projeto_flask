
from flask import Flask, render_template
import dao.aluno_dao import AlunoDAO
import dao.professor_dao import ProfessorDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/aluno')
def lista_aluno():
    dao=AlunoDAO()
    lista = dao.listar_alunos()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    dao=ProfessorDAO()
    lista = dao.listar_professores()
    return render_template('professor/lista.html', lista=lista)



@app.route('/turma')
def lista_turma():
    # Conecta ao banco de dados
    conn =db_config.get_connection()
    cursor = conn.cursor()
    # Executa consulta SQL
    cursor.execute('select turma.id, semestre, curso.nome_curso, professor.nome from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id')
    # Obtém todos os registros
    lista = cursor.fetchall()
    # Fecha conexão teste
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