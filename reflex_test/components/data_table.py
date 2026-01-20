import reflex as rx
from typing import Any, Callable, Dict, List, Optional, Tuple

# 컬럼 정의: (헤더명, dict_key, width optional)
Column = Tuple[str, str, Optional[str]]

def data_table(
    rows: rx.Var[List[Dict[str, Any]]],
    columns: List[Column],
    *,
    row_key: str = "id",
    empty_text: str = "데이터가 없습니다.",
) -> rx.Component:
    """재사용 가능한 심플 테이블(그리드) 컴포넌트.

    - rows: List[Dict] 형태의 데이터
    - columns: [("ID","id","80px"), ("이름","name",None), ...]
    - row_key: 각 row의 고유 key로 사용할 dict 키 (기본 id)
    """
    # grid template columns 문자열 만들기: "80px 1fr 2fr" 같은 형태
    template = " ".join([(c[2] if c[2] else "1fr") for c in columns])

    header = rx.grid(
        *[
            rx.text(col[0], font_weight="600")
            for col in columns
        ],
        grid_template_columns=template,
        gap="3",
        padding_y="0.5em",
        padding_x="0.75em",
        border_bottom="1px solid #e5e7eb",
        bg="#f9fafb",
        width="100%",
    )

    def render_row(r: Dict[str, Any]) -> rx.Component:
        return rx.grid(
            *[
                rx.text(r.get(col[1], ""))
                for col in columns
            ],
            grid_template_columns=template,
            gap="3",
            padding_y="0.5em",
            padding_x="0.75em",
            border_bottom="1px solid #f1f5f9",
            width="100%",
            key=r.get(row_key, ""),
            align_items="center",
        )

    body = rx.cond(
        rows.length() == 0,
        rx.box(
            rx.text(empty_text, color="#64748b"),
            padding="1em",
        ),
        rx.vstack(
            rx.foreach(rows, render_row),
            spacing="0",
            width="100%",
        ),
    )

    return rx.box(
        header,
        body,
        border="1px solid #e5e7eb",
        border_radius="10px",
        overflow="hidden",
        width="100%",
    )
