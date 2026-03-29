from __future__ import annotations

import traceback
import json
import sys

from io import StringIO


class CaptureOutputContext():
    def __init__(self):
        self.output = StringIO()
        self.original_output = sys.stdout
        self.original_stderr = sys.stderr

    def __enter__(self):
        sys.stdout = self.output
        sys.stderr = self.output
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.original_output
        sys.stderr = self.original_stderr

    def get_value(self):
        return self.output.getvalue().rstrip()


def vsc_eval(filepath: str, function_name: str, **kwargs) -> str:
    """
    Evaluate a function in a Python file, and return the function's return value
    This function is used to evaluate VS Code python files and return the result to the Extension
    """
    with open(filepath, 'r', encoding="utf8") as file:
        code = file.read()

    # MotionBuilder 2023 (Python 3.9) has a bug where the output isn't transfered unless the Python Editor window is open.
    if sys.version_info[:2] == (3, 9):
        import pyfbsdk
        pyfbsdk.ShowToolByName("Python Editor")

    # Find the function
    exec_globals = {}
    try:
        exec(compile(code, filepath, 'exec'), exec_globals)
    except Exception as e:
        error_traceback = traceback.format_exc()
        return json.dumps({"error": str(error_traceback)}, separators=(',', ':'))

    if function_name in exec_globals:
        function = exec_globals[function_name]
    else:
        raise ValueError(f"Function '{function_name}' not found in file '{filepath}'")

    with CaptureOutputContext() as output:
        try:
            return_value = function(**kwargs)
        except Exception as e:
            error_traceback = traceback.format_exc()
            return json.dumps({"error": str(error_traceback), "output": output.get_value()}, separators=(',', ':'))

        return json.dumps({"result": return_value, "output": output.get_value()}, separators=(',', ':'))
