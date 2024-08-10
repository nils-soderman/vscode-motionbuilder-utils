"""
Module for executing python code in MotionBuilder
"""

import traceback
import tempfile
import sys
import os
import re

if sys.version_info[0] >= 3:
    from io import StringIO
else:
    from StringIO import StringIO
    from codecs import open

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
        globals()["__VsCodeVariables__"] = {
            "__builtins__": __builtins__,
            "__IsVsCodeExec__": True
        }
    return globals()["__VsCodeVariables__"]


def find_package(filepath):
    """ Find the expected __package__ value for the executed file, so relative imports work """
    normalized_filepath = os.path.normpath(filepath).lower()

    valid_packages = []
    for path in sys.path:
        normalized_path = os.path.normpath(path).lower()
        if normalized_filepath.startswith(normalized_path):
            package = os.path.relpath(os.path.dirname(filepath), path).replace(os.sep, ".")
            if package != ".":
                valid_packages.append(package)

    # If there are multiple valid packages, choose the shortest one
    if valid_packages:
        return min(valid_packages, key=len)

    return ""


def format_exception(exception, code):
    messages = []

    seen_exceptions = set()
    while exception:
        if id(exception) in seen_exceptions:
            break
        seen_exceptions.add(id(exception))

        if isinstance(exception, SyntaxError):
            exception.text = code.splitlines()[exception.lineno - 1]
            exception.filename += ":%s" % exception.lineno

        # For each traceback, we want to append the exception message
        traceback_stack = []
        for frame_summary in traceback.extract_tb(exception.__traceback__):
            if frame_summary.filename == "<string>" and frame_summary.name == execute_code.__name__:
                continue

            if frame_summary.filename.endswith(".ipynb"):
                linenum = frame_summary.lineno

                code_lines = code.splitlines()
                code_line = code_lines[linenum - 1]

                frame_summary._line = code_line + "\n"

            else:
                frame_summary.filename += ":%s" % frame_summary.lineno

            traceback_stack.append(frame_summary)

        text = "Traceback (most recent call last):\n"
        text += "".join(traceback.format_list(traceback_stack))
        text += "".join(traceback.format_exception_only(type(exception), exception))

        messages.append(text)

        exception = exception.__context__

    return "\nDuring handling of the above exception, another exception occurred:\n\n".join(reversed(messages))


def execute_code(code, filename, use_colors):
    try:
        exec(compile(code, filename, "exec"), get_exec_globals())
    except Exception as caught_exception:
        if sys.version_info.major >= 3:
            traceback_message = format_exception(caught_exception, code)
        else:
            traceback_message = traceback.format_exc()

        # Color the message red (this is only supported by 'Debug Console' in VsCode, and not not 'Output' log)
        if use_colors:
            traceback_message = '\033[91m' + traceback_message + '\033[0m'

        print(traceback_message)


def main():
    filepath = globals().get("vsc_file")
    filename = globals().get("vsc_filename")
    command_id = globals().get("vsc_id")
    name = globals().get("vsc_name", None)
    vscode_debugging = globals().get("vsc_is_debugging", False)
    use_colors = globals().get("vsc_use_colors", False)

    # Set some global variables
    exec_globals = get_exec_globals()

    exec_globals["__file__"] = filename

    if name:
        exec_globals["__name__"] = name
    elif "__name__" in exec_globals:
        exec_globals.pop("__name__")

    exec_globals["__package__"] = find_package(filename)

    # Read the code file and execute it
    with open(filepath, 'r', encoding='utf-8') as vs_code_in_file:
        if not vscode_debugging:
            with OutputRedirector(command_id):
                execute_code(vs_code_in_file.read(), filename, use_colors)
        else:
            execute_code(vs_code_in_file.read(), filename, use_colors)
            print(">>>")


main()
