"""
Module for executing python code in MotionBuilder
"""

import traceback
import tempfile
import sys
import os

if sys.version_info.major >= 3:
    from io import StringIO
    import ast
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

        # If output is larger than 955 bytes, it'll get corrupted when transferred over the socket, so write to a file instead
        # MotionBuilder 2023 (Python 3.9) also has a bug where the output isn't transfered unless the Python Editor window is open.
        if sys.getsizeof(output_str) >= 950 or sys.version_info[:2] == (3, 9):
            if sys.version_info.major == 2:
                output_str = output_str.decode("utf-8")
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


def format_exception(exception_in, filename, code, num_ignore_tracebacks=0):
    seen_exceptions = set()
    messages = []
    lines = code.splitlines()

    exception = exception_in
    while exception:
        if id(exception) in seen_exceptions:
            break
        seen_exceptions.add(id(exception))

        traceback_stack = []
        for frame_summary in traceback.extract_tb(exception.__traceback__):
            if num_ignore_tracebacks > 0:
                num_ignore_tracebacks -= 1
                continue

            if frame_summary.filename == filename and \
                    (frame_summary.lineno is not None and 0 < frame_summary.lineno <= len(lines)):
                line = lines[frame_summary.lineno - 1]
            else:
                line = frame_summary.line

            # These attributes were added in Python 3.11
            if sys.version_info >= (3, 11):
                col_info = {
                    "end_lineno": frame_summary.end_lineno,
                    "colno": frame_summary.colno,
                    "end_colno": frame_summary.end_colno,
                }
            else:
                col_info = {}

            traceback_stack.append(
                traceback.FrameSummary(
                    "%s:%s" % (frame_summary.filename, frame_summary.lineno),
                    frame_summary.lineno,
                    frame_summary.name,
                    lookup_line=False,
                    locals=frame_summary.locals,
                    line=line,
                    **col_info
                )
            )

        if isinstance(exception, SyntaxError):
            if exception.filename == filename:
                exception.filename = "%s:%s" % (exception.filename, exception.lineno)
                if exception.lineno is not None and 0 < exception.lineno <= len(lines):
                    line = lines[exception.lineno - 1]
                    exception.text = line

        text = "Traceback (most recent call last):\n"
        text += "".join(traceback.format_list(traceback_stack))
        text += "".join(traceback.format_exception_only(type(exception), exception))

        messages.append(text)

        exception = exception.__context__

    return "\nDuring handling of the above exception, another exception occurred:\n\n".join(reversed(messages))


def handle_exception(exception, filename, code, use_colors, num_ignore_tracebacks=0):
    if sys.version_info.major >= 3:
        traceback_message = format_exception(exception, filename, code, num_ignore_tracebacks)
    else:
        traceback_message = traceback.format_exc()

    # Color the message red (this is only supported by 'Debug Console' in VsCode, and not 'Output' log)
    if use_colors:
        traceback_message = '\033[91m' + traceback_message + '\033[0m'

    print(traceback_message)


def add_print_for_last_expr(parsed_code):
    """
    Modify the ast to print the last expression if it isn't None.
    """
    if parsed_code.body:
        last_expr = parsed_code.body[-1]
        if isinstance(last_expr, ast.Expr):
            temp_var = "_"

            line_info = {
                "lineno": last_expr.lineno,
                "col_offset": last_expr.col_offset
            }

            if sys.version_info >= (3, 8):
                line_info["end_lineno"] = last_expr.end_lineno
                line_info["end_col_offset"] = last_expr.end_col_offset

            # Assign the last expression to a temporary variable
            temp_var_assign = ast.Assign(
                targets=[ast.Name(id=temp_var, ctx=ast.Store(), **line_info)],
                value=last_expr.value,
                **line_info
            )

            # If the temporary variable isn't None, print it
            print_stmt = ast.IfExp(
                test=ast.Compare(
                    left=ast.Name(id=temp_var, ctx=ast.Load(), **line_info),
                    ops=[ast.IsNot()],
                    comparators=[ast.Constant(value=None, **line_info)],
                    **line_info
                ),
                body=ast.Call(
                    func=ast.Name(id='print', ctx=ast.Load(), **line_info),
                    args=[ast.Name(id=temp_var, ctx=ast.Load(), **line_info)],
                    keywords=[],
                    **line_info
                ),
                orelse=ast.Constant(value=None, **line_info),
                **line_info
            )

            parsed_code.body[-1] = temp_var_assign
            parsed_code.body.append(ast.Expr(value=print_stmt, **line_info))

    return parsed_code


def execute_code(code, filename, use_colors):
    if sys.version_info.major >= 3:
        try:
            parsed_code = ast.parse(code, filename)
        except (SyntaxError, ValueError) as caught_exception:
            handle_exception(caught_exception, filename, code, use_colors, num_ignore_tracebacks=2)
            return

        parsed_code = add_print_for_last_expr(parsed_code)
    else:
        parsed_code = code

    try:
        exec(compile(parsed_code, filename, "exec"), get_exec_globals())
    except Exception as caught_exception:
        handle_exception(caught_exception, filename, code, use_colors, num_ignore_tracebacks=1)


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
