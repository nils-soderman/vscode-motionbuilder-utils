from __future__ import annotations

import typing
import enum

import pyfbsdk


class EItemType(enum.StrEnum):
    ENUM = "enum"
    ENUM_MEMBER = "enum-member"
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    PROPERTY = "property"


class DocumentationItemT(typing.TypedDict):
    label: str
    type: EItemType
    children: typing.NotRequired[list["DocumentationItemT"]]


SORT_ORDER_ENUM = {
    EItemType.ENUM_MEMBER: 0,
    EItemType.METHOD: 1,
}


SORT_OREDER_CLASS = {
    EItemType.ENUM: 0,
    EItemType.PROPERTY: 1,
    EItemType.METHOD: 2,
}


def construct_enum_type(ref: type) -> DocumentationItemT:
    children: list[DocumentationItemT] = []
    for enum_name, enum_value in ref.__dict__.items():
        if enum_name.startswith('__'):
            continue

        children.append({
            "label": enum_name,
            "type": EItemType.ENUM_MEMBER if isinstance(enum_value, ref) else EItemType.METHOD,
        })

    children.sort(key=lambda x: (SORT_ORDER_ENUM.get(x["type"], 2)))

    return {
        "label": ref.__name__,
        "type": EItemType.ENUM,
        "children": children,
    }


def construct_class_type(ref: type) -> DocumentationItemT:
    children: list[DocumentationItemT] = []
    for attr_name, attr_value in ref.__dict__.items():
        if attr_name.startswith('__') and not attr_name == '__init__':
            continue

        if type(attr_value) == type:
            children.append(construct_enum_type(attr_value))

        elif callable(attr_value):
            children.append({
                "label": attr_name,
                "type": EItemType.METHOD,
            })
        else:
            children.append({
                "label": attr_name,
                "type": EItemType.PROPERTY,  # Properties are treated as methods for documentation
            })

    children.sort(key=lambda x: (SORT_OREDER_CLASS.get(x["type"], 2), x["label"]))

    return {
        "label": ref.__name__,
        "type": EItemType.CLASS,
        "children": children,
    }


def get_content():
    functions: list[DocumentationItemT] = []
    classes: list[DocumentationItemT] = []
    enums: list[DocumentationItemT] = []

    for name, ref in pyfbsdk.__dict__.items():
        if name.startswith('__'):
            continue

        # ENUM
        if type(ref) == type:
            enums.append(construct_enum_type(ref))

        # CLASS
        elif isinstance(ref, type):
            classes.append(construct_class_type(ref))

        # FUNCTION
        elif callable(ref):
            functions.append({
                "label": name,
                "type": EItemType.FUNCTION
            })

        else:
            print("Unknown type for", name, ":", type(ref))

    functions.sort(key=lambda x: x["label"])
    classes.sort(key=lambda x: x["label"])
    enums.sort(key=lambda x: x["label"])

    return functions + classes + enums


a = get_content()
