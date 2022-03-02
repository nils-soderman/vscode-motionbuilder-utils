import subprocess
import importlib
import tempfile
import json
import sys
import os

SERVER_ENV_VAR = "MB_Utils_Debug_Enabled"

PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
ATTACH_SETTINGS_FILEPATH = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils", 'vscode-attach.json')


def GetSettings():
    with open(ATTACH_SETTINGS_FILEPATH, 'r') as File:
        return json.load(File)


def InstallAndImportModule(PackageName, Target = ""):
    try:
        # Try to import it without adding anything to the sys path
        return importlib.import_module(PackageName)
    except:
        try:
            if Target not in sys.path:
                sys.path.append(Target)
            return importlib.import_module(PackageName)
        except:
            if Target:
                "--target=%s" % Target
            subprocess.check_call([PYTHON_EXECUTABLE, "-m", "pip", "install", Target, PackageName])

    return importlib.import_module(PackageName)


def IsDebugServerRunning():
    return  os.environ.get(SERVER_ENV_VAR, "") == str(True)


def EnableDebugServer():
    # Get settings
    Settings = GetSettings()
    Port = Settings.get("port")
    Target = Settings.get("target")

    # Setup server
    debugpy = InstallAndImportModule("debugpy", Target)
    debugpy.configure(python = PYTHON_EXECUTABLE)
    debugpy.listen(Port)

    os.environ[SERVER_ENV_VAR] = str(True)


def main():
    if not IsDebugServerRunning():
        EnableDebugServer()


if "builtin" in __name__:
    main()
