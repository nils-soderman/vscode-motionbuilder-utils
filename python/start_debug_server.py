""" 
Script to start a debugpy server in MotionBuilder.
Will automatically install debugpy if module cannot be found.
"""

import subprocess
import importlib
import tempfile
import socket
import json
import sys
import os


VSCODE_DEBUG_SERVER_ENV_VAR = "MB_Utils_Debug_Enabled"
MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
VSCODE_MOBU_TEMPDIR = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")
SETTINGS_FILEPATH = os.path.join(VSCODE_MOBU_TEMPDIR, 'vscode-attach.json')
OUTPUT_FILEPATH = os.path.join(VSCODE_MOBU_TEMPDIR, 'vscode-attach-out.txt')


def write_output(string):
    if sys.version_info.major >= 3:
        with open(OUTPUT_FILEPATH, "w+", encoding="utf-8") as file:
            file.write(str(string))
    else:
        with open(OUTPUT_FILEPATH, "w+") as file:  # pylint: disable=unspecified-encoding
            file.write(str(string))


def get_vscode_attach_settings():
    """ Get a dict with settings passed along from VSCode """
    if sys.version_info.major >= 3:
        with open(SETTINGS_FILEPATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        with open(SETTINGS_FILEPATH, 'r') as file:  # pylint: disable=unspecified-encoding
            return json.load(file)


def try_import(module_name, path=""):
    """ Attempt to import a module, returns the module if sucessful, else None """
    should_append_path = path and path not in sys.path and os.path.isdir(path)
    if should_append_path:
        sys.path.append(path)

    module = None
    try:
        module = importlib.import_module(module_name)
    except Exception:
        pass

    if should_append_path:
        sys.path.remove(path)

    return module


def install_and_import_module(package_name, target="", version=""):
    module = try_import(package_name)

    # Append the target path and try to import again
    if not module and target not in sys.path:
        module = try_import(package_name, target)

    if not module:
        arg_target = ""
        if target:
            arg_target = "--target=%s" % target

        if version:
            package_name = "%s==%s" % (package_name, version)

        # Ensure pip is avaliable
        if not try_import("pip"):
            if not try_import("ensurepip"):
                return None

            temp_installation_dir = os.path.join(
                VSCODE_MOBU_TEMPDIR, "TempPipInstall")
            subprocess.check_call(
                [MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", temp_installation_dir])

            pip_module_path = ""
            for root, directory, files in os.walk(temp_installation_dir):
                if "__init__.py" in files and os.path.basename(root) == "pip":
                    pip_module_path = os.path.join(root)
                    break

            if not pip_module_path:
                return None

            subprocess.call(
                [MOBU_PYTHON_EXECUTABLE, pip_module_path, "install", arg_target, package_name])
        else:
            subprocess.call([MOBU_PYTHON_EXECUTABLE, "-m", "pip",
                            "install", arg_target, package_name])

        module = try_import(package_name, target)

    return module


def is_port_available(port):
    """ Check if a port is avaliable """
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.settimeout(0.05)
    response = socket_instance.connect_ex(("127.0.0.1", port))
    socket_instance.close()
    return response != 0


def is_debug_server_running():
    """ Check if a debug server already has been started in this MB instance """
    return os.environ.get(VSCODE_DEBUG_SERVER_ENV_VAR, "") == str(True)


def enable_debug_server():
    """ 
    Enable a debugpy server, make sure one is not already running using IsDebugServerRunning().
    """
    # Get settings
    settings = get_vscode_attach_settings()
    port = settings.get("port")
    target = settings.get("target")
    target = os.path.join(target, "Python%s%s" % (
        sys.version_info.major, sys.version_info.minor))

    # Attempt to import / install debugpy
    version = "1.5.1" if sys.version_info.major == 2 else None
    debugpy = install_and_import_module("debugpy", target, version)
    if not debugpy:
        return "ERROR: Failed to import/install python module 'debugpy'"

    if not is_port_available(port):
        return "ERROR: Port %s is already in use! Consider configuring VS Code: `motionbuilder.debug.port` to use another port." % port

    # Start the debugpy server
    debugpy.configure(python=MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(port)

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(True)

    return True


def main():
    if is_debug_server_running():
        write_output(True)
    else:
        response = enable_debug_server()
        write_output(response)


main()
