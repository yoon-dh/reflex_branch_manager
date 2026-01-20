import reflex as rx
from reflex_test.layout import layout
from reflex_test.state import UserState


def user_page():
    return layout(
        rx.vstack(
            rx.heading("회원 관리", size="6"),

            rx.input(
                placeholder="이름",
                value=UserState.name,
                on_change=UserState.set_name,
            ),
            rx.input(
                placeholder="이메일",
                value=UserState.email,
                on_change=UserState.set_email,
            ),
            rx.button("회원 등록", on_click=UserState.create),

            rx.divider(),

            rx.foreach(
                UserState.users,
                lambda u: rx.hstack(
                    rx.text(f"{u.id}"),
                    rx.text(u.name),
                    rx.text(u.email),
                    spacing="4",
                ),
            ),

            on_mount=UserState.load,
            spacing="3",
        )
    )