import reflex as rx
from reflex_test.layout import layout


def dashboard_page():
    return layout(
        rx.vstack(
            rx.heading("지사 관리", size="6"),
            rx.text("아직 구현 안됨"),
        )
    )