import reflex as rx
from typing import List
import duckdb_mock


class User(rx.Base):
    id: int
    name: str
    email: str


class UserState(rx.State):
    users: List[User] = []
    name: str = ""
    email: str = ""

    def load(self):
        self.users = [User(**u) for u in duckdb_mock.get_users()]

    def create(self):
        if not self.name or not self.email:
            return
        duckdb_mock.create_user(self.name, self.email)
        self.name = ""
        self.email = ""
        self.load()