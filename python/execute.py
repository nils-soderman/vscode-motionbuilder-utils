"""
Module for executing python code in MotionBuilder
"""

import contextlib
import traceback
import tempfile
import json
import sys
import os
import re


TEMP_FOLDERPATH = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")
OUTPUT_FILEPATH = os.path.join(TEMP_FOLDERPATH, "vscode-exec-out.txt")
INPUT_FILEPATH = os.path.join(TEMP_FOLDERPATH, 'vscode-exec.json')


def read_input_data():
    """ Read input data that was written with typescript (`writeDataFile()` in `execute-script.ts`) """
    if sys.version_info.major >= 3:
        with open(INPUT_FILEPATH, 'r', encoding='utf-8') as settings_file:
            return json.load(settings_file)
    else:
        with open(INPUT_FILEPATH, 'r') as settings_file:  # pylint: disable=unspecified-encoding
            return json.load(settings_file)


def get_exec_globals():
    """ Get globals to be used in the exec function when executing user scripts """
    if "__VsCodeVariables__" not in globals():
        globals()["__VsCodeVariables__"] = {"__builtins__": __builtins__, "__IsVsCodeExec__": True}
    return globals()["__VsCodeVariables__"]


def execute_code(code, filename, vs_code_is_debugging):
    try:
        exec(compile(code, filename, "exec"), get_exec_globals())
    except Exception as caught_exception:
        exception_type, exception, traceback_ = sys.exc_info()

        traceback_lines = []
        for line in traceback.format_exception(exception_type, exception, traceback_):
            if execute_code.__name__ in line:
                continue

            # Reformat path to include the file number, example: 'myfile.py:5'
            if re.findall(r'file ".*", line \d*, in ', line.lower()):
                components = line.split(",", 2)
                line_number = "".join(x for x in components[1] if x.isdigit())
                components[0] = '%s:%s"' %(components[0][:-1], line_number)
                line = ",".join(components)

            traceback_lines.append(line)

        traceback_message = "".join(traceback_lines).strip()
        # Color the message red (this is only supported by 'Debug Console' in VsCode, and not not 'Output' log)
        if vs_code_is_debugging:
            traceback_message = '\033[91m' + traceback_message + '\033[0m'

        print(traceback_message)


def main():
    vs_code_data = read_input_data()
    vscode_debugging = vs_code_data.get("is_debugging", False)
    additional_print_str = vs_code_data.get("additionalPrint", "")

    # Set some global variables
    exec_globals = get_exec_globals()

    target_filepath = vs_code_data.get("__file__", "")
    exec_globals["__file__"] = target_filepath
    if "__name__" in vs_code_data and vs_code_data["__name__"]:
        exec_globals["__name__"] = vs_code_data["__name__"]
    elif "__name__" in exec_globals:
        exec_globals.pop("__name__")

    # Read the code file and execute it
    if sys.version_info.major >= 3:
        # Python 3
        with open(vs_code_data["file"], 'r', encoding='utf-8') as vs_code_in_file:
            if not vscode_debugging:
                # Re-direct the output through a text file
                with open(OUTPUT_FILEPATH, 'w', encoding="utf-8") as vs_code_out_file, contextlib.redirect_stdout(vs_code_out_file):
                    execute_code(vs_code_in_file.read(), target_filepath, vscode_debugging)
            else:
                execute_code(vs_code_in_file.read(), target_filepath, vscode_debugging)

    else:
        # Python 2
        with open(vs_code_data["file"], 'r') as vs_code_in_file:  # pylint: disable=unspecified-encoding
            execute_code(vs_code_in_file.read(), target_filepath, vscode_debugging)

    if additional_print_str:
        print(additional_print_str)


main()
