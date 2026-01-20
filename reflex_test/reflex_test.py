import reflex as rx
import duckdb_mock
from database import init_motherduck

from reflex_test.pages.dashboard import dashboard_page
from reflex_test.pages.users import user_page
from reflex_test.pages.payments import payment_page
from reflex_test.pages.adjustments import adjustment_page

# DB 초기화
# duckdb_mock.init_db()

app = rx.App()
init_motherduck()
app.add_page(dashboard_page, route="/")
app.add_page(user_page, route="/users")
app.add_page(payment_page, route="/payments")
app.add_page(adjustment_page, route="/adjustments")