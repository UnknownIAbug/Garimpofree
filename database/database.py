import sqlite3

def conectar():
    return sqlite3.connect("garimpofree.db")


def criar_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS oportunidades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT,
        descricao TEXT,
        valor TEXT,
        link TEXT
    )
    """)

    conexao.commit()
    conexao.close()
