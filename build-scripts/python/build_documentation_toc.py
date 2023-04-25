"""
Build the table of contents for the online documentation, these are located under 'resources/documentation/<version>/'
"""
import warnings
import time
import json
import sys
import os

from importlib import reload


# Append current site-packages path
CURRENT_DIR = os.path.dirname(__file__)
SITEPACKAGES_DIR = os.path.join(CURRENT_DIR, "site-packages")

if SITEPACKAGES_DIR not in sys.path:
    sys.path.append(SITEPACKAGES_DIR)

import requests
import js2py

import pyfbsdk_stub_generator.plugins.online_documentation.documentation_scraper.table_of_contents as docScraper
reload(docScraper)


# ------------------------------------------
#            Structs & Enums
# ------------------------------------------

class FDictTags:
    Url = "url"


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def get_motionbuilder_version():
    """ Get the current version of MotionBuilder """
    import pyfbsdk
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def get_output_directory():
    return os.path.join(CURRENT_DIR, "..", "..", "resources", "documentation", str(get_motionbuilder_version()))


def save_json_file(filename, content):
    directory = get_output_directory()
    if not os.path.isdir(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)
    with open(filepath, "w+", encoding="utf-8") as file:
        json.dump(content, file)


# ------------------------------------------
#                Examples
# ------------------------------------------

def generate_examples_toc(version: int):
    examples_toc_url = f"https://help.autodesk.com/cloudhelp/{version}/ENU/MotionBuilder-SDK/py_ref/examples.js"
    examples_response = requests.get(examples_toc_url, timeout = 10)
    if examples_response.status_code != 200:
        # Log a warning:
        warnings.warn(f"Failed to get examples table of contents from '{examples_toc_url}', status code: {examples_response.status_code}")
        return

    parsed_examples = js2py.eval_js(examples_response.text)

    data = {}
    for title, url, children in parsed_examples:
        data[title] = {FDictTags.Url: url}

    save_json_file("examples.json", data)


# ------------------------------------------
#                Python
# ------------------------------------------

def generate_python_toc(version: int):
    python_docs = docScraper.Documentation("pyfbsdk", version, bUseCache=True)

    data = {}
    for item in python_docs.TableOfContents:
        data[item.Name] = {FDictTags.Url: item.RelativeUrl}

        is_function = item.RelativeUrl.startswith("namespacepyfbsdk.html")
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

            child_url = item.RelativeUrl + child.RelativeUrl
            data[f"{item.Name}: {child.Name}"] = {FDictTags.Url: child_url}

    save_json_file("python.json", data)


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
    # _time_it(generate_python_toc, version)


def main():
    start_time = time.time()

    mobu_version = get_motionbuilder_version()
    generate_table_of_contents(mobu_version)

    delta_time = time.time() - start_time
    print(f"Generating docs took {delta_time:.2f} sec in total")


if "builtin" in __name__:
    main()
