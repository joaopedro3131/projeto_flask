from dao.db_config import get_connection

class MatriculaDAO:

    def listar_matriculas(self):
        conn = get_connection()
        cursor = conn.cursor()
        # Faz o JOIN entre matricula, aluno, turma, curso e professor para exibir todos os dados da tabela da foto
        sql = """
            SELECT 
                matricula.id, 
                turma.semestre, 
                aluno.nome, 
                curso.nome_curso, 
                professor.nome, 
                professor.disciplina 
            FROM matricula
            JOIN aluno ON matricula.aluno_id = aluno.id
            JOIN turma ON matricula.turma_id = turma.id
            JOIN curso ON turma.curso_id = curso.id
            JOIN professor ON turma.professor_id = professor.id
            ORDER BY matricula.id DESC
        """
        cursor.execute(sql)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute("""
                    UPDATE matricula SET aluno_id = %s, turma_id = %s WHERE id = %s
                """, (aluno_id, turma_id, id))
            else:
                cursor.execute("""
                    INSERT INTO matricula (aluno_id, turma_id) VALUES (%s, %s)
                """, (aluno_id, turma_id))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, aluno_id, turma_id FROM matricula WHERE id = %s", (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM matricula WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
