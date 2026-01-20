import duckdb
import os
from typing import List, Dict

# MotherDuck 설정
# 보안을 위해 실제 서비스 시에는 .env 파일에 저장하고 os.getenv("MOTHERDUCK_TOKEN")으로 읽으세요.
TOKEN = ""
MD_CONNECTION = f"md:my_db?motherduck_token={TOKEN}"


def get_conn():
    """MotherDuck 클라우드에 연결합니다."""
    return duckdb.connect(MD_CONNECTION)


def init_motherduck():
    """테이블을 초기화합니다. (기존 테이블 삭제 후 재생성)"""
    try:
        with get_conn() as conn:
            # 1. 기존 테이블 삭제 (컬럼명 변경 반영을 위해)
            # conn.execute("DROP TABLE IF EXISTS users")
            # print("🗑️ 기존 users 테이블 삭제 완료")

            # 2. 새로운 테이블 생성 (name 컬럼 사용)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)
            print("✅ MotherDuck 테이블 생성 및 연결 성공!")
    except Exception as e:
        print(f"❌ MotherDuck 초기화 실패: {e}")


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


if __name__ == "__main__":
    # 이 파일을 직접 실행하면 DB 테이블이 초기화됩니다.
    init_motherduck()