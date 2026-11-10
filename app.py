
from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO


app = Flask(__name__)
app.secret_key = 'uma_chave_muito_secreta_e_unica'

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/aluno')
def lista_aluno():
    dao=AlunoDAO()
    lista = dao.listar_alunos()
    return render_template('aluno/lista.html', lista=lista)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html',aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])
@app.route('/aluno/salvar/<int:id>', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade= request.form['idade']
    cidade= request.form['cidade']
    dao = AlunoDAO()
    result=dao.salvar(id, nome, idade, cidade)
    if result["status"] == "ok":
        flash("Aluno cadastrado com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')



@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)



@app.route('/aluno/remover/<int:id>')
def remover_aluno(id):
    dao = AlunoDAO()
    result = dao.remover(id)
    if result["status"] == "ok":
        flash("Aluno removido com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/aluno')



@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista = dao.listar_professores()
    return render_template('professor/lista.html', lista=lista)

@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor=None)

@app.route('/professor/salvar/', methods=['POST'])
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina)
    
    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
        
    return redirect('/professor')

@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form.html', professor=professor)

@app.route('/professor/remover/<int:id>')
def remover_professor(id):
    dao = ProfessorDAO()
    result = dao.remover(id)
    if result["status"] == "ok":
        flash("Professor removido com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/professor')




@app.route('/turma')
def listar_todas_turmas():
    lista = TurmaDAO().listar_turmas()
    return render_template('turma/lista.html', lista=lista)

# --- SEU CÓDIGO DA ROTA FORM (Adaptado para a segunda opção e turma=None) ---
@app.route('/turma/form')
def lista_turma():
    # Usando o nome correto do seu método do ProfessorDAO (Segunda Opção)
    lista_professores = ProfessorDAO().listar_professores()
    
    # Lista de cursos criada manualmente aqui para suprir a falta do CursoDAO
    lista_cursos = [
        (1, "Informática"),
        (2, "Administração"),
        (3, "Enfermagem"),
        (4, "Eletrotécnica")
    ]
    return render_template('turma/form.html', turma=None, lista_professores=lista_professores, lista_cursos=lista_cursos)

# --- SEU CÓDIGO DA ROTA SALVAR ---
@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']

    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso_id, professor_id)

    if resultado["status"] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
        
    return redirect('/turma')

# --- SEU CÓDIGO DA ROTA EDITAR (Adaptado com a segunda opção) ---
@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    lista_professores = ProfessorDAO().listar_professores()
    
    lista_cursos = [
        (1, "Informática"),
        (2, "Administração"),
        (3, "Enfermagem"),
        (4, "Eletrotécnica")
    ]
    
    turma = TurmaDAO().buscar_por_id(id)
    return render_template('turma/form.html', turma=turma, lista_professores=lista_professores, lista_cursos=lista_cursos)

# --- SEU CÓDIGO DA ROTA REMOVER ---
@app.route('/turma/remover/<int:id>')
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Turma removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')






@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome=request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/desafio1/')
def desafio1():
    nome=request.args.get('nome')
    return render_template('desafio/desafio1.html', valor_recebido=nome)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    nome_mae = request.form['nome_mae']
    dados = f"Nome: {nome}, Data de Nascimento: {data_nascimento}, CPF: {cpf}, Nome da Mãe: {nome_mae}"
    
    return render_template('desafio/desafio1.html', valor_recebido=dados)



    


@app.route('/contato')
def contato():
    return render_template('contato.html')



@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run(debug=True)