from dao.db_config import get_connection

class alunoDAO:

    sqlSelect = "SELECT id, nome, idade, cidade FROM aluno"

    def listar_alunos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista