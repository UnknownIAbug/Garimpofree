import sqlite3

BANCO = "garimpofree.db"


def conectar():
    return sqlite3.connect(BANCO)


def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS oportunidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        descricao TEXT,
        categoria TEXT,
        cidade TEXT,
        fonte TEXT,
        link TEXT,
        preco REAL,
        score INTEGER,
        nivel TEXT,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def salvar_oportunidade(
    titulo,
    descricao,
    categoria,
    cidade,
    fonte,
    link,
    preco,
    score,
    nivel
):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO oportunidades(
        titulo,
        descricao,
        categoria,
        cidade,
        fonte,
        link,
        preco,
        score,
        nivel
    )
    VALUES(?,?,?,?,?,?,?,?,?)
    """, (
        titulo,
        descricao,
        categoria,
        cidade,
        fonte,
        link,
        preco,
        score,
        nivel
    ))

    conn.commit()
    conn.close()
