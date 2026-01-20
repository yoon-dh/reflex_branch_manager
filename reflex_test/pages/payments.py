import reflex as rx
from reflex_test.layout import layout


def payment_page():
    return layout(
        rx.vstack(
            rx.heading("결제내역 관리", size="6"),
            rx.text("아직 구현 안됨"),
        )
    )