"""
Build the table of contents for the online documentation, these are located under 'resources/documentation/<version>/'
"""
from __future__ import annotations

import warnings
import time
import json
import sys
import os

from importlib import reload

import pyfbsdk

# Append current site-packages path
CURRENT_DIR = os.path.dirname(__file__)
SITEPACKAGES_DIR = os.path.join(CURRENT_DIR, "site-packages")

if SITEPACKAGES_DIR not in sys.path:
    sys.path.append(SITEPACKAGES_DIR)

# pylint: disable=wrong-import-position
import requests
import js2py

import pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.table_of_contents as docScraper
from pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.page_parser import MemberItem
reload(docScraper)


# ------------------------------------------
#            Structs & Enums
# ------------------------------------------

class EIcons:
    """ 
    VSCode icons (All icons can be found here: https://microsoft.github.io/vscode-codicons/dist/codicon.html)
    """
    FUNCTION = "symbol-function"
    CLASS = "symbol-class"
    PROPERTY = "symbol-property"
    METHOD = "symbol-method"
    ENUM = "symbol-enum"
    ENUM_MEMBER = "symbol-enum-member"


class EVsCodeItemData:
    URL = "url"
    LABEL = "label"


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def get_motionbuilder_version():
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def get_output_directory():
    return os.path.join(CURRENT_DIR, "..", "..", "resources", "documentation", str(get_motionbuilder_version()))


def save_items(filename, items: list):
    directory = get_output_directory()
    if not os.path.isdir(directory):
        os.makedirs(directory)

    data = {"items": items}

    filepath = os.path.join(directory, filename)
    with open(filepath, "w+", encoding="utf-8") as file:
        json.dump(data, file)


# ------------------------------------------
#                Examples
# ------------------------------------------

def generate_examples_toc(version: int):
    examples_toc_url = f"https://help.autodesk.com/cloudhelp/{version}/ENU/MotionBuilder-SDK/py_ref/examples.js"
    examples_response = requests.get(examples_toc_url, timeout=10)
    if examples_response.status_code != 200:
        # Log a warning:
        warnings.warn(
            f"Failed to get examples table of contents from '{examples_toc_url}', status code: {examples_response.status_code}")
        return

    parsed_examples = js2py.eval_js(examples_response.text)

    items = []
    for title, url, children in parsed_examples:
        items.append({
            EVsCodeItemData.LABEL: title,
            EVsCodeItemData.URL: url
        })

    save_items("examples.json", items)


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

    items = []
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
            EVsCodeItemData.LABEL: f"$({icon}) {item.Name}",
            EVsCodeItemData.URL: item.RelativeUrl
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
                EVsCodeItemData.LABEL: f"$({child_icon}) {title}",
                EVsCodeItemData.URL: child_url
            })

    save_items("python.json", items)


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
