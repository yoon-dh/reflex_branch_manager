import reflex as rx
import duckdb_mock

from reflex_test.pages.users import user_page
from reflex_test.pages.payments import payment_page

# DB 초기화
duckdb_mock.init_db()

app = rx.App()
app.add_page(user_page, route="/")
app.add_page(payment_page, route="/payments")