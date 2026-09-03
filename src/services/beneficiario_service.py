import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "beneficiarios.db"


def get_beneficiario(
    id: int | None = None, matricula: str | None = None, nome: str | None = None
) -> dict | list:

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        if id is not None:
            cursor.execute("SELECT * FROM beneficiarios WHERE id = ?", (id,))

            row = cursor.fetchone()

        elif matricula:
            cursor.execute(
                "SELECT * FROM beneficiarios WHERE matricula = ?", (matricula,)
            )

            row = cursor.fetchone()

        elif nome:
            cursor.execute(
                "SELECT * FROM beneficiarios WHERE nome LIKE ?", (f"%{nome}%",)
            )

            rows = cursor.fetchall()

            if not rows:
                return {"erro": "Beneficiário não encontrado"}

            return [dict(row) for row in rows]

        else:
            return {"erro": "Informe id, matrícula ou nome"}

        if not row:
            return {"erro": "Beneficiário não encontrado"}

        return dict(row)