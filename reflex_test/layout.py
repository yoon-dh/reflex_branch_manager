import reflex as rx


def sidebar():
    return rx.vstack(
        rx.heading("메뉴", size="4"),
        rx.link("회원 관리", href="/"),
        rx.link("결제내역 관리", href="/payments"),
        spacing="3",
        padding="1em",
        width="100%",
    )


def layout(content):
    return rx.hstack(
        rx.box(
            sidebar(),
            width="20%",
            border_right="1px solid #ddd",
            height="100vh",
        ),
        rx.box(
            content,
            width="80%",
            padding="2em",
        ),
        width="100%",
    )