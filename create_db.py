# create_db.py
import sqlite3

conn = sqlite3.connect("src/database/beneficiarios.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS beneficiarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL,
    cpf TEXT NOT NULL,
    beneficiario TEXT NOT NULL,
    plano TEXT NOT NULL
)
""")

cursor.executemany(
    """
INSERT INTO beneficiarios (
    nome,
    matricula,
    cpf,
    beneficiario,
    plano
)
VALUES (?, ?, ?, ?, ?)
""",
    [
        ("João Silva", "1001", "12345678901", "Titular", "Premium"),
        ("Maria Silva", "1002", "98765432100", "Dependente", "Premium"),
        ("Carlos Souza", "1003", "11122233344", "Titular", "Empresarial"),
    ],
)

conn.commit()
conn.close()
