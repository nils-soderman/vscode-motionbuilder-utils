import tempfile
import base64
import json
import sys
import io
import os
import re

from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output

use_matplotlib = False

try:
    import matplotlib.pyplot as plt
    import matplotlib.backends.backend_agg as agg
    import matplotlib

    matplotlib.use('Agg')

    use_matplotlib = True
except ModuleNotFoundError:
    pass

TEMP_FOLDERPATH = os.path.join(
    tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")


def get_output_filepath(command_id):
    return os.path.join(TEMP_FOLDERPATH, "exec-out-%s.txt" % command_id)


class OutputRedirector():
    def __init__(self, command_id):
        self.command_id = command_id
        self.output = io.StringIO()
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
            print(f"{output_filepath = }")
            with open(output_filepath, 'w', encoding="utf-8") as out_file:
                out_file.write(output_str)
        else:
            print(output_str)


def execute(code):
    # Create an instance of InteractiveShell with the custom DisplayPublisher
    shell = InteractiveShell.instance()
    shell.colors = 'NoColor'

    with capture_output() as captured:
        shell.run_cell(code)

    response = []
    for output in captured.outputs:
        response.append(output.data)

    if use_matplotlib:
        for fignum in plt.get_fignums():
            image_buffer = io.BytesIO()
            fig = plt.figure(fignum)
            canvas = agg.FigureCanvasAgg(fig)
            canvas.draw()
            # canvas.print_png(image_buffer)
            # png_data = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
            png_data = base64.b64encode(canvas.buffer_rgba()).decode('utf-8')
            response.append({
                'image/png': png_data
            })
            plt.close(fignum)

    # This regular expression matches ANSI escape codes
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    # Use the sub method to replace the escape codes with an empty string
    no_color_stdout = ansi_escape.sub('', captured.stdout)
    if no_color_stdout:
        response.append({
            'text/plain': no_color_stdout
        })

    return json.dumps(response)


def main():
    # Define the code to be executed
    code = globals().get("vsc_code")
    if not code:
        return

    command_id = globals().get("vsc_command_id")

    with OutputRedirector(command_id):
        result = execute(code)
        print(result)


main()
