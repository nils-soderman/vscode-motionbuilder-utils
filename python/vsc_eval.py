import json  # Needs to be here to ensure the json module is available in remote-handler.ts `evaluateFunction`
import sys


if sys.version_info.major < 3:
    from StringIO import StringIO
    from codecs import open
else:
    from io import StringIO
    from contextlib import redirect_stdout


def vsc_eval(filepath, function_name, **kwargs):
    """
    Evaluate a function in a Python file, and return the function's return value
    This function is used to evaluate VS Code python files and return the result to the Extension
    """
    with open(filepath, 'r', encoding="utf8") as file:
        code = file.read()

    # Find the function
    function = None
    exec_globals = {}
    exec(code, exec_globals)
    if function_name in exec_globals:
        function = exec_globals[function_name]
    else:
        raise ValueError(f"Function '{function_name}' not found in file '{filepath}'")

    output_buffer = StringIO()
    try:
        if sys.version_info.major < 3:
            orignal_stdout = sys.stdout
            sys.stdout = output_buffer
            try:
                return_value = function(**kwargs)
            finally:
                sys.stdout = orignal_stdout
        else:
            with redirect_stdout(output_buffer):
                return_value = function(**kwargs)

    except Exception as e:
        return json.dumps({"error": str(e), "output": output_buffer.getvalue()}, separators=(',', ':'))

    return json.dumps({"result": return_value, "output": output_buffer.getvalue()}, separators=(',', ':'))
