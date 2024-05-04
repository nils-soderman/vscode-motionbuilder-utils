"""
Module for executing python code in MotionBuilder
"""

import traceback
import tempfile
import sys
import os
import re

from io import StringIO


TEMP_FOLDERPATH = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")


class OutputRedirector():
    def __init__(self, command_id):
        self.command_id = command_id
        self.output = StringIO()
        self.original_output = sys.stdout

    def __enter__(self):
        sys.stdout = self.output

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.original_output
        output_str = self.output.getvalue().rstrip()

        # If output is larger than 955 bytes, it'll get corruped when transfered over the socket, so write to a file instead
        # MotionBuilder 2023 (Python 3.9) also has a bug where the output isn't transfered unless the Python Editor window is open.
        if sys.getsizeof(output_str) >= 950 or (sys.version_info.major == 3 and sys.version_info.minor == 9):
            output_filepath = get_output_filepath(self.command_id)
            with open(output_filepath, 'w', encoding="utf-8") as out_file:
                out_file.write(output_str)
        else:
            print(output_str)


def get_output_filepath(command_id):
    return os.path.join(TEMP_FOLDERPATH, "exec-out-%s.txt" % command_id)


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
            # This is to make VS Code recognize this as a link to a spesific line number
            if re.findall(r'file ".*", line \d*, in ', line.lower()):
                file_desc, _, number_and_module = line.partition(",")
                line_number = "".join(x for x in number_and_module.partition(",")[0] if x.isdigit())
                file_desc = '%s:%s"' % (file_desc[:-1], line_number)
                line = file_desc + "," + number_and_module

            traceback_lines.append(line)

        traceback_message = "".join(traceback_lines).strip()
        # Color the message red (this is only supported by 'Debug Console' in VsCode, and not not 'Output' log)
        if vs_code_is_debugging:
            traceback_message = '\033[91m' + traceback_message + '\033[0m'

        print(traceback_message)


def main():
    filepath = globals().get("vsc_file")
    filename = globals().get("vsc_filename")
    command_id = globals().get("vsc_id")
    name = globals().get("vsc_name", None)
    vscode_debugging = globals().get("vsc_is_debugging", False)
    additional_sys_paths = globals().get("vsc_paths", [])

    if additional_sys_paths:
        for path in additional_sys_paths:
            if path not in sys.path:
                sys.path.append(path)

    # Set some global variables
    exec_globals = get_exec_globals()

    exec_globals["__file__"] = filename

    if name:
        exec_globals["__name__"] = name
    elif "__name__" in exec_globals:
        exec_globals.pop("__name__")

    # Read the code file and execute it
    if sys.version_info.major >= 3:  # Python 3
        with open(filepath, 'r', encoding='utf-8') as vs_code_in_file:
            if not vscode_debugging:
                with OutputRedirector(command_id):
                    execute_code(vs_code_in_file.read(), filename, vscode_debugging)
            else:
                execute_code(vs_code_in_file.read(), filename, vscode_debugging)
                print(">>>")

    else:  # Python 2
        with open(filepath, 'r') as vs_code_in_file:  # pylint: disable=unspecified-encoding
            execute_code(vs_code_in_file.read(), filename, vscode_debugging)


main()
