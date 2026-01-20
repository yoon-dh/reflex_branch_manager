import reflex as rx
from typing import List
from pydantic import BaseModel
import database  # 수정: 만들어둔 database.py를 가져옵니다.

class User(BaseModel):
    id: int = 0
    name: str
    email: str

class UserState(rx.State):
    users: List[User] = []
    name: str = ""
    email: str = ""

    def load(self):
        """database.py의 get_users 함수를 사용하여 목록을 불러옵니다."""
        # database.get_users()는 리스트 안에 딕셔너리가 들어있는 형태이므로 그대로 변환 가능합니다.
        self.users = [User(**u) for u in database.get_users()]

    def create(self):
        """database.py의 create_user 함수를 사용하여 사용자를 생성합니다."""
        if not self.name or not self.email:
            return

        # database.py 내부에 ID 자동 계산 로직이 있으므로 이를 호출합니다.
        database.create_user(self.name, self.email)

        self.name = ""
        self.email = ""
        self.load()

    def on_load(self):
        self.load()