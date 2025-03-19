from typing import Any
import reflex as rx

from custom_components.reflex_ag_grid_ce import ag_grid_ce
from custom_components.reflex_ag_grid_ce.types import multi_row_selection

human_size = rx.vars.FunctionStringVar("""
(params) => {
    const sizeInKb = params.value / 1024;

    if (sizeInKb > 1024) {
        return `${+(sizeInKb / 1024).toFixed(2)} MB`;
    } else {
        return `${+sizeInKb.toFixed(2)} KB`;
    }
}""")


class TreeDisplayState(rx.State):
    data: list[dict[str, Any]] = [
        {
            "host": "vali",
            "path": ["Desktop", "ProjectAlpha", "Proposal.docx"],
            "size": 512000,
            "created": "2023-07-10",
            "modified": "2023-08-01",
        },
        {
            "host": "vali",
            "path": ["Desktop", "ProjectAlpha", "Timeline.xlsx"],
            "size": 1048576,
            "created": "2023-07-12",
            "modified": "2023-08-03",
        },
        {
            "host": "vali",
            "path": ["Desktop", "ToDoList.txt"],
            "size": 51200,
            "created": "2023-08-05",
            "modified": "2023-08-10",
        },
        {
            "host": "vali",
            "path": ["Desktop", "MeetingNotes_August.pdf"],
            "size": 460800,
            "created": "2023-08-15",
            "modified": "2023-08-15",
        },
        {
            "host": "vidar",
            "path": ["Desktop", "LaunchCodes.txt"],
            "size": 32500,
            "created": "1973-08-05",
            "modified": "2023-08-10",
        },
        {
            "host": "vidar",
            "path": ["Desktop", "funtime.pdf"],
            "size": 460800,
            "created": "2023-08-15",
            "modified": "2023-08-15",
        },
        {
            "host": "vali",
            "path": ["Documents", "Work", "ProjectAlpha", "Proposal.docx"],
            "size": 512000,
            "created": "2023-07-10",
            "modified": "2023-08-01",
        },
        {
            "host": "vali",
            "path": ["Documents", "Work", "ProjectAlpha", "Timeline.xlsx"],
            "size": 1048576,
            "created": "2023-07-12",
            "modified": "2023-08-03",
        },
        {
            "host": "vali",
            "path": ["Documents", "Work", "ProjectBeta", "Report.pdf"],
            "size": 1024000,
            "created": "2023-06-22",
            "modified": "2023-07-15",
        },
        {
            "host": "vali",
            "path": ["Documents", "Work", "ProjectBeta", "Budget.xlsx"],
            "size": 1048576,
            "created": "2023-06-25",
            "modified": "2023-07-18",
        },
        {
            "host": "vidar",
            "path": ["Documents", "Work", "Meetings", "TeamMeeting_August.pdf"],
            "size": 512000,
            "created": "2023-08-20",
            "modified": "2023-08-21",
        },
        {
            "host": "vidar",
            "path": ["Documents", "Work", "Meetings", "ClientMeeting_July.pdf"],
            "size": 1048576,
            "created": "2023-07-15",
            "modified": "2023-07-16",
        },
        {
            "host": "vali",
            "path": ["Documents", "Personal", "Taxes", "2022.pdf"],
            "size": 1024000,
            "created": "2023-04-10",
            "modified": "2023-04-10",
        },
        {
            "host": "vali",
            "path": ["Documents", "Personal", "Taxes", "2021.pdf"],
            "size": 1048576,
            "created": "2022-04-05",
            "modified": "2022-04-06",
        },
        {
            "host": "vali",
            "path": ["Documents", "Personal", "Taxes", "2020.pdf"],
            "size": 1024000,
            "created": "2021-04-03",
            "modified": "2021-04-03",
        },
        {
            "host": "vali",
            "path": ["Pictures", "Vacation2019", "Beach.jpg"],
            "size": 1048576,
            "created": "2019-07-10",
            "modified": "2019-07-12",
        },
        {
            "host": "vali",
            "path": ["Pictures", "Vacation2019", "Mountain.png"],
            "size": 2048000,
            "created": "2019-07-11",
            "modified": "2019-07-13",
        },
        {
            "host": "vali",
            "path": ["Pictures", "Family", "Birthday2022.jpg"],
            "size": 3072000,
            "created": "2022-12-15",
            "modified": "2022-12-20",
        },
        {
            "host": "vali",
            "path": ["Pictures", "Family", "Christmas2021.png"],
            "size": 2048000,
            "created": "2021-12-25",
            "modified": "2021-12-26",
        },
        {
            "host": "vali",
            "path": ["Videos", "Vacation2019", "Beach.mov"],
            "size": 4194304,
            "created": "2019-07-10",
            "modified": "2019-07-12",
        },
        {
            "host": "vali",
            "path": ["Videos", "Vacation2019", "Hiking.mp4"],
            "size": 4194304,
            "created": "2019-07-15",
            "modified": "2019-07-16",
        },
        {
            "host": "vali",
            "path": ["Videos", "Family", "Birthday2022.mp4"],
            "size": 6291456,
            "created": "2022-12-15",
            "modified": "2022-12-20",
        },
        {
            "host": "vali",
            "path": ["Videos", "Family", "Christmas2021.mov"],
            "size": 6291456,
            "created": "2021-12-25",
            "modified": "2021-12-26",
        },
        {
            "host": "vidar",
            "path": ["Downloads", "SoftwareInstaller.exe"],
            "size": 2097152,
            "created": "2023-08-01",
            "modified": "2023-08-01",
        },
        {
            "host": "vidar",
            "path": ["Downloads", "Receipt_OnlineStore.pdf"],
            "size": 1048576,
            "created": "2023-08-05",
            "modified": "2023-08-05",
        },
        {
            "host": "vali",
            "path": ["Downloads", "Ebook.pdf"],
            "size": 1048576,
            "created": "2023-08-08",
            "modified": "2023-08-08",
        },
    ]
    combine_hosts: rx.Field[bool] = rx.field(True)

    host_filter: rx.Field[bool] = rx.field(True)
    host_value = 'vali'

    parent_select: rx.Field[bool] = rx.field(True)



@rx.page("/tree")
def tree_example():
    return rx.box(
        rx.hstack(
            "Combine Hosts",
            rx.switch(
                checked=TreeDisplayState.combine_hosts,
                on_change=TreeDisplayState.set_combine_hosts,
            ),
            "Filter Hosts",
            rx.switch(
                checked=TreeDisplayState.host_filter,
                on_change=TreeDisplayState.set_host_filter,
            ),
            "Parent Select",
            rx.switch(
                checked=TreeDisplayState.parent_select,
                on_change=TreeDisplayState.set_parent_select,
            ),
            align="center",
        ),
        ag_grid_ce.root(
            id="ag_grid_tree_1",
            row_data=TreeDisplayState.data,
            auto_group_column_def=ag_grid_ce.column_def(
                field="",
                header_name="File Explorer",
                min_width=280,
                cell_renderer_params={"suppressCount": False},
            ),
            column_defs=[
                ag_grid_ce.column_def(field="created"),
                ag_grid_ce.column_def(field="modified"),
                ag_grid_ce.column_def(
                    field="size",
                    agg_func="sum",
                    value_formatter=human_size,
                ),
                ag_grid_ce.column_def(
                    field="host",
                    hide=~TreeDisplayState.combine_hosts,
                    agg_func=rx.vars.FunctionStringVar(
                        "(params) => params.values.join(', ').split(', ').filter((value, index, self) => self.indexOf(value) === index).join(', ')"
                    ),
                ),
            ],
            row_selection=multi_row_selection(
                hide_disabled_checkboxes=False,
                enable_click_selection=True,
                group_selects=rx.cond(
                    TreeDisplayState.parent_select,
                    "descendants",
                    "all",
                ),
                select_all="filtered",
                is_row_selectable=rx.cond(
                    TreeDisplayState.host_filter,
                    rx.vars.function.ArgsFunctionOperation.create(
                        ("rowNode",),
                        rx.Var(
                            f"""
                        return rowNode.data ? rowNode.data.host === {TreeDisplayState.host_value} : false
                        """),
                        explicit_return=True,
                    ),
                    rx.vars.function.ArgsFunctionOperation.create(
                        ("rowNode",),
                        rx.Var(
                            f"""
                            return true
                            """),
                        explicit_return=True,
                    ),
                ),
            ),
            default_column_def={"flex": 1},
            group_default_expanded=10,
            tree_data=True,
            # get_data_path is an Initial option, it cannot be set after initialization.
            get_data_path=rx.cond(
                TreeDisplayState.combine_hosts,
                rx.vars.FunctionStringVar(
                    "(data) => data.path",
                ),
                rx.vars.FunctionStringVar(
                    "(data) => [data.host, ...data.path]",
                ),
            ),
            # This key causes the grid to re-initialize when `combine_hosts` var changes
            key=f"ag_grid_{TreeDisplayState.combine_hosts}",
        ),
        width="100vw",
        height="100vh",
    )
