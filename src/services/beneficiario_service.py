import sqlite3

DB_PATH = "src/database/beneficiarios.db"


def get_beneficiario(
    id: int | None = None, matricula: str | None = None, nome: str | None = None
) -> dict | list:

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    if id is not None:
        cursor.execute("SELECT * FROM beneficiarios WHERE id = ?", (id,))

        row = cursor.fetchone()

        conn.close()

        if not row:
            return {"erro": "Beneficiário não encontrado"}

        return dict(row)

    elif matricula:
        cursor.execute("SELECT * FROM beneficiarios WHERE matricula = ?", (matricula,))

        row = cursor.fetchone()

        conn.close()

        if not row:
            return {"erro": "Beneficiário não encontrado"}

        return dict(row)

    elif nome:
        cursor.execute("SELECT * FROM beneficiarios WHERE nome LIKE ?", (f"%{nome}%",))

        rows = cursor.fetchall()

        conn.close()

        if not rows:
            return {"erro": "Beneficiário não encontrado"}

        return [dict(row) for row in rows]

    else:
        conn.close()

        return {"erro": "Informe id, matrícula ou nome"}
