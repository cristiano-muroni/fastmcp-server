import sqlite3

DB_PATH = "src/database/beneficiarios.db"


def get_beneficiario(id=None, matricula=None, nome=None):

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    if id:
        cursor.execute("SELECT * FROM beneficiarios WHERE id = ?", (id,))

    elif matricula:
        cursor.execute("SELECT * FROM beneficiarios WHERE matricula = ?", (matricula,))

    elif nome:
        cursor.execute("SELECT * FROM beneficiarios WHERE nome LIKE ?", (f"%{nome}%",))

    else:
        return {"erro": "Informe id, matrícula ou nome"}

    row = cursor.fetchone()

    conn.close()

    if not row:
        return {"erro": "Beneficiário não encontrado"}

    return dict(row)
