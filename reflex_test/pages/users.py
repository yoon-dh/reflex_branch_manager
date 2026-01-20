import reflex as rx
from reflex_test.layout import layout
from reflex_test.state import UserState
from reflex_test.components.data_table import data_table

def user_page():
    return layout(
        rx.vstack(
            rx.heading("회원 관리", size="6"),

            # ✅ 검색 영역
            rx.hstack(
                rx.input(
                    placeholder="이름 검색",
                    value=UserState.search_name,
                    on_change=UserState.set_search_name,
                    width="300px",
                ),
                rx.button("검색", on_click=UserState.search),
                rx.button("전체", on_click=UserState.load),
                spacing="3",
            ),

            rx.divider(),

            # 등록 영역
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

            data_table(
                UserState.users,
                columns=[
                    ("ID", "id", "80px"),
                    ("이름", "name", "1fr"),
                    ("이메일", "email", "2fr"),
                ],
                row_key="id",
                empty_text="회원 데이터가 없습니다.",
            ),

            on_mount=UserState.load,
            spacing="3",
        )
    )
