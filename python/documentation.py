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


def get_content():
    enums: list[DocumentationItemT] = []
    classes: list[DocumentationItemT] = []
    functions: list[DocumentationItemT] = []

    for name, ref in pyfbsdk.__dict__.items():
        if name.startswith('__'):
            continue

        is_enum = type(ref) == type
        if is_enum:
            children: list[DocumentationItemT] = []
            for enum_name, enum_value in ref.__dict__.items():
                if enum_name.startswith('__'):
                    continue

                children.append({
                    "label": enum_name,
                    "type": EItemType.ENUM_MEMBER if isinstance(enum_value, ref) else EItemType.METHOD,
                })

            enums.append({
                "label": name,
                "type": EItemType.ENUM,
                "children": children,
            })

        elif isinstance(ref, type):
            children: list[DocumentationItemT] = []
            for attr_name, attr_value in ref.__dict__.items():
                if attr_name.startswith('__') and not attr_name == '__init__':
                    continue

                if callable(attr_value):
                    children.append({
                        "label": attr_name,
                        "type": EItemType.METHOD,
                    })
                elif isinstance(attr_value, property):
                    children.append({
                        "label": attr_name,
                        "type": EItemType.PROPERTY,  # Properties are treated as methods for documentation
                    })

            order = {
                EItemType.PROPERTY: 0,
                EItemType.METHOD: 1,
            }
            children.sort(key=lambda x: (order.get(x["type"], 2), x["label"]))

            classes.append({
                "label": name,
                "type": EItemType.CLASS,
                "children": children,
            })

        elif callable(ref):
            functions.append({
                "label": name,
                "type": EItemType.FUNCTION
            })

        else:
            print(f"Skipping {name} of type {type(ref)}")

    enums.sort(key=lambda x: x["label"])
    classes.sort(key=lambda x: x["label"])
    functions.sort(key=lambda x: x["label"])

    return functions + classes + enums
