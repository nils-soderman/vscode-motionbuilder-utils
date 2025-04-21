"""
Build the table of contents for the online documentation, these are located under 'resources/documentation/<version>/'
"""
from __future__ import annotations

import subprocess
import warnings
import typing
import enum
import time
import json
import sys
import os

try:
    import pyfbsdk
except ImportError:
    raise ImportError("pyfbsdk is not available, please run this script from within MotionBuilder")

# Append current site-packages path
CURRENT_DIR = os.path.dirname(__file__)
SITEPACKAGES_DIR = os.path.join(CURRENT_DIR, "site-packages")

if not os.path.isdir(SITEPACKAGES_DIR):
    # Install the site-packages directory
    mobupy = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
    subprocess.check_call([
        mobupy, "-m", "pip", "install", "-r", os.path.join(CURRENT_DIR, "requirements.txt"), "--target", SITEPACKAGES_DIR
    ])

if SITEPACKAGES_DIR not in sys.path:
    sys.path.append(SITEPACKAGES_DIR)

# pylint: disable=wrong-import-position
import requests
import js2py

import pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.table_of_contents as docScraper
from pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.page_parser import MemberItem
from pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.documentation_urls import DOCUMENTATION_URL, GetPythonPageContentsUrl


# ------------------------------------------
#            Types & Enums
# ------------------------------------------

class EIcons(enum.StrEnum):
    """ 
    VSCode icons (All icons can be found here: https://microsoft.github.io/vscode-codicons/dist/codicon.html)
    """
    FUNCTION = "symbol-function"
    CLASS = "symbol-class"
    PROPERTY = "symbol-property"
    METHOD = "symbol-method"
    ENUM = "symbol-enum"
    ENUM_MEMBER = "symbol-enum-member"


class ItemDataT(typing.TypedDict):
    url: str
    label: str


class TableOfContentT(typing.TypedDict):
    version: int
    base_url: str
    items: list[ItemDataT]


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def get_motionbuilder_version():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def get_output_directory(version: int):
    return os.path.join(CURRENT_DIR, "..", "toc", str(version))


def save_items(filename: str, version: int, base_url: str, items: list[ItemDataT]):
    directory = get_output_directory(version)
    if not os.path.isdir(directory):
        os.makedirs(directory)

    data: TableOfContentT = {
        "version": version,
        "base_url": base_url,
        "items": items
    }

    filepath = os.path.join(directory, filename)
    with open(filepath, "w+", encoding="utf-8") as file:
        json.dump(data, file, separators=(',', ':'))


# ------------------------------------------
#                Examples
# ------------------------------------------

def generate_examples_toc(version: int):
    examples_toc_url = GetPythonPageContentsUrl("examples.js", version)

    examples_response = requests.get(examples_toc_url, timeout=10)
    if examples_response.status_code != 200:
        # Log a warning:
        warnings.warn(
            f"Failed to get examples table of contents from '{examples_toc_url}', status code: {examples_response.status_code}")
        return

    parsed_examples = js2py.eval_js(examples_response.text)

    items: list[ItemDataT] = []
    for title, url, children in parsed_examples:
        items.append({
            "label": title,
            "url": url
        })

    save_items("examples.json",
               base_url=GetPythonPageContentsUrl("", version),
               version=version,
               items=items)


# ------------------------------------------
#                Python
# ------------------------------------------

def is_enum(item: docScraper.TableOfContentItem):
    if not hasattr(pyfbsdk, item.Name):
        if item.Name == "Enumeration":
            return True
        return False

    item_object = getattr(pyfbsdk, item.Name)
    return type(item_object) == type  # pylint: disable=unidiomatic-typecheck


def is_method(item: docScraper.TableOfContentItem, child: MemberItem):
    if not hasattr(pyfbsdk, item.Name):
        return False

    item_object = getattr(pyfbsdk, item.Name)
    if hasattr(item_object, child.Name):
        child_object = getattr(item_object, child.Name)
        return callable(child_object)

    return False


def generate_python_toc(version: int):
    python_docs = docScraper.Documentation("pyfbsdk", version, bUseCache=True)

    items: list[ItemDataT] = []
    items_name_map = set()
    for item in python_docs.TableOfContents:
        is_function = item.RelativeUrl.startswith("namespacepyfbsdk.html")

        if is_function:
            icon = EIcons.FUNCTION
        elif is_enum(item):
            icon = EIcons.ENUM
        else:
            icon = EIcons.CLASS

        if item.Name in items_name_map:
            continue

        items.append({
            "label": f"$({icon}) {item.Name}",
            "url": item.RelativeUrl
        })
        items_name_map.add(item.Name)

        if is_function:
            continue

        # Go through all children of the class
        parsed_page = item.ParsePage()
        for child in parsed_page.Members:
            # Skip private members & operators
            if child.Name.startswith(("__", "operator")):
                continue

            # Skip constructors, they are named the same as the class
            if child.Name == item.Name:
                continue

            title = f"{item.Name}: {child.Name}"
            if title in items_name_map:
                continue
            items_name_map.add(title)

            if icon == EIcons.ENUM:
                child_icon = EIcons.ENUM_MEMBER
            elif is_method(item, child):
                child_icon = EIcons.METHOD
            else:
                child_icon = EIcons.PROPERTY

            child_url = item.RelativeUrl + child.RelativeUrl
            items.append({
                "label": f"$({child_icon}) {title}",
                "url": child_url
            })

    save_items("python.json",
               base_url=GetPythonPageContentsUrl("", version),
               version=version,
               items=items)


# ------------------------------------------
#              Main functions
# ------------------------------------------

def generate_table_of_contents(version):
    def _time_it(function, *args):
        start_time = time.time()
        function(*args)
        delta_time = time.time() - start_time
        print(f"'{function.__name__}' took {delta_time:.2f} sec.")
        return delta_time

    _time_it(generate_examples_toc, version)
    _time_it(generate_python_toc, version)


def main():
    start_time = time.time()

    mobu_version = get_motionbuilder_version()
    generate_table_of_contents(mobu_version)

    delta_time = time.time() - start_time
    print(f"Generating docs took {delta_time:.2f} sec in total")


if "builtin" in __name__:
    main()
