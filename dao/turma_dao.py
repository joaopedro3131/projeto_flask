from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = "SELECT * from turma order by id desc"

    def listar_turmas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso, nome):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute(
                    "UPDATE turma SET semestre = %s, curso = %s, nome = %s WHERE id = %s", 
                    (semestre, curso, nome, id)
                )
            else:
                cursor.execute(
                    "INSERT INTO turma (semestre, curso, nome) VALUES (%s, %s, %s)", 
                    (semestre, curso, nome)
                )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, semestre, curso, nome FROM turma WHERE id = %s", (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM turma WHERE id = %s", (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
