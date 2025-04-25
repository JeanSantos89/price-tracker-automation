import psycopg2

def salvar_no_bd(produtos):
    conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS precos (
        id TEXT PRIMARY KEY,
        titulo TEXT,
        preco NUMERIC,
        link TEXT
    )
    """)

    for p in produtos:
        cur.execute("""
        INSERT INTO precos (id, titulo, preco, link)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET preco = EXCLUDED.preco
        """, (p["id"], p["titulo"], p["preco"], p["link"]))

    conn.commit()
    cur.close()
    conn.close()
