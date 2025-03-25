from typing import Callable, Literal, Optional, TypedDict, Union

import reflex as rx
from reflex.utils.format import to_camel_case


class SingleRowSelection(TypedDict, total=False):
    mode: Literal["singleRow"]
    enable_click_selection: Optional[
        Union[bool, Literal["enableDeselection", "enableSelection"]]
    ]
    check_boxes: Optional[Union[bool]]  # TODO add CheckboxSelectionCallback
    hide_disabled_checkboxes: Optional[bool]

    # usage of is_row_selectable:
    # rx.vars.function.ArgsFunctionOperation.create(
    #     ("rowNode",),
    #     rx.Var("rowNode.data ? rowNode.data.year < 2007 : false"),
    # )

    is_row_selectable: Optional[rx.Var[Callable]]
    copy_selected_rows: Optional[bool]
    enable_selection_without_keys: Optional[bool]

    @staticmethod
    def default_values() -> "SingleRowSelection":
        return {
            "mode": "singleRow",
            "check_boxes": True,
            "hide_disabled_checkboxes": False,
            "enable_selection_without_keys": False,
        }

    @staticmethod
    def create(**kwargs) -> "SingleRowSelection":
        instance = SingleRowSelection.default_values()
        instance.update(kwargs)
        return {to_camel_case(k): v for k, v in instance.items()}


single_row_selection = SingleRowSelection.create


class MultiRowSelection(TypedDict, total=False):
    mode: Literal["multiRow"]
    group_selects: Optional[Literal["self", "descendants", "filteredDescendants"]]
    select_all: Optional[Literal["all", "filtered", "currentPage"]]
    header_checkbox: Optional[bool]
    enable_click_selection: Optional[
        Union[bool, Literal["enableDeselection", "enableSelection"]]
    ]
    check_boxes: Optional[Union[bool]]  # TODO add CheckboxSelectionCallback
    hide_disabled_checkboxes: Optional[bool]

    # usage of is_row_selectable:
    # rx.vars.function.ArgsFunctionOperation.create(
    #     ("rowNode",),
    #     rx.Var("rowNode.data ? rowNode.data.year < 2007 : false"),
    # )

    is_row_selectable: Optional[rx.Var[Callable]]
    copy_selected_rows: Optional[bool]
    enable_selection_without_keys: Optional[bool]

    @staticmethod
    def default_values() -> "MultiRowSelection":
        return {
            "mode": "multiRow",
            "group_selects": "self",
            "select_all": "all",
            "header_checkbox": True,
            "check_boxes": True,
            "hide_disabled_checkboxes": False,
            "enable_selection_without_keys": False,
        }

    @staticmethod
    def create(**kwargs) -> "MultiRowSelection":
        instance = MultiRowSelection.default_values()
        instance.update(kwargs)
        return {to_camel_case(k): v for k, v in instance.items()}


multi_row_selection = MultiRowSelection.create
