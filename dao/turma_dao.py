from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = "select turma.id, semestre, curso.nome_curso, professor.nome from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id"

    def listar_turmas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista