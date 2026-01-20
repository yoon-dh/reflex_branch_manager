import duckdb
from typing import List, Dict

DB_PATH = "mock.duckdb"


def get_conn():
    return duckdb.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.close()


def create_user(name: str, email: str):
    conn = get_conn()
    user_id = conn.execute(
        "SELECT COALESCE(MAX(id), 0) + 1 FROM users"
    ).fetchone()[0]

    conn.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (user_id, name, email),
    )
    conn.close()


def get_users() -> List[Dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, name, email FROM users ORDER BY id"
    ).fetchall()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]