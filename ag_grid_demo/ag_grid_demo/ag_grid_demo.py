"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import pandas as pd
import reflex as rx

from custom_components.reflex_ag_grid_ce import ag_grid_ce
from custom_components.reflex_ag_grid_ce.types import multi_row_selection

df = pd.DataFrame(
    {
        "Label": ["index", "Tree", "model", "model-auth", "model-auth2"],
        "Description": ["Simple\nblablablalbala", "Aggregate", "todo", "todo", "todo"],
        "Need Pro": [
            False,
            True,
            False,
            False,
            False,
        ],
        "Link": ["/", "/tree", "/model", "/model-auth", "/model-auth2"],
    }
)

column_defs = [
    ag_grid_ce.column_group(
        group_id="TopLine1",
        header_name="Top line in a multi-level header",
        children=[
            ag_grid_ce.column_def(field="Label"),
            ag_grid_ce.column_def(field="Description", wrap_text=False),
        ],
    ),
    ag_grid_ce.column_group(
        group_id="TopLine2",
        header_name="Top line 2 in a multi-level header",
        children=[
            ag_grid_ce.column_def(field="Need Pro"),
            ag_grid_ce.column_def(
                field="Link", cell_renderer=ag_grid_ce.renderers.link
            ),
        ],
    )
]


class BasicGridState(rx.State):
    selection: list[dict[str, str]] = []


def selected_item(item: dict[str, str]) -> rx.Component:
    return rx.card(
        rx.data_list.root(
            rx.foreach(
                item,
                lambda kv: rx.data_list.item(
                    rx.data_list.label(kv[0]),
                    rx.data_list.value(kv[1]),
                ),
            ),
        ),
    )


def index():
    return rx.vstack(
        rx.vstack(
            ag_grid_ce(
                theme="balham",
                id="ag_grid_basic_1",
                row_data=df.to_dict("records"),
                column_defs=column_defs,
                row_selection=multi_row_selection(),
                on_selection_changed=lambda rows, _0, _1: BasicGridState.setvar(
                    "selection",
                    rows,
                ),
                width="100vw",
            ),
            rx.heading("Other demos"),
            rx.link("Simple ModelWrapper", href="/model"),
            rx.text(
                rx.link("Customized ModelWrapper", href="/model-auth"),
                " (Generate data)",
            ),
        ),
        rx.vstack(
            rx.heading("Selected Items"),
            rx.hstack(
                rx.foreach(
                    BasicGridState.selection,
                    selected_item,
                ),
                wrap="wrap",
            ),
            max_width="48vw",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
