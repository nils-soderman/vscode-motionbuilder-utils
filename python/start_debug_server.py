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

def GetVSCodeAttachSettings():
    """ Get a dict with settings passed along from VSCode """
    with open(SETTINGS_FILEPATH, 'r') as File:
        return json.load(File)


def TryImport(ModuleName, Path = ""):
    """ Attempt to import a module, returns the module if sucessful, else None """
    bAppendPath = Path and Path not in sys.path
    if bAppendPath:
        sys.path.append(Path)

    Module = None
    try:
        Module = importlib.import_module(ModuleName)
    except:
        pass

    if bAppendPath:
        sys.path.remove(Path)

    return Module


def InstallAndImportModule(PackageName, Target = ""):
    Module = TryImport(PackageName)

    # Append the target path and try to import again
    if not Module and Target not in sys.path:
        Module = TryImport(PackageName, Target)

    if not Module:
        ArgTarget = ""
        if Target:
            ArgTarget = "--target=%s" % Target

        # Ensure pip is avaliable
        if not TryImport("pip"):
            if not TryImport("ensurepip"):
                return None

            TempInstallationDir = os.path.join(VSCODE_MOBU_TEMPDIR, "TempPipInstall")
            subprocess.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", TempInstallationDir])

            pipModulePath = ""
            for Root, Directory, Files in os.walk(TempInstallationDir):
                if "__init__.py" in Files and os.path.basename(Root) == "pip":
                    pipModulePath = os.path.join(Root)
                    break

            if not pipModulePath:
                return None

            subprocess.check_call([MOBU_PYTHON_EXECUTABLE, pipModulePath, "install", ArgTarget, PackageName])
        else:
            subprocess.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "pip", "install", ArgTarget, PackageName])

        Module = TryImport(PackageName, Target)

    return Module


def IsPortAvailable(Port):
    """ Check if a port is avaliable """
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.settimeout(0.05)
    Response = Socket.connect_ex(("127.0.0.1", Port))
    Socket.close()
    return Response != 0


def IsDebugServerRunning():
    """ Check if a debug server already has been started in this MB instance """
    return os.environ.get(VSCODE_DEBUG_SERVER_ENV_VAR, "") == str(True)


def EnableDebugServer():
    """ 
    Enable a debugpy server, make sure one is not already running using IsDebugServerRunning().
    """
    # Get settings
    Settings = GetVSCodeAttachSettings()
    Port = Settings.get("port")
    Target = Settings.get("target")

    # Attempt to import / install debugpy
    debugpy = InstallAndImportModule("debugpy", Target)
    if not debugpy:
        print("ERROR: Failed to import/install python module 'debugpy'")
        return False

    if not IsPortAvailable(Port):
        print("ERROR: Port %s is already in use! Consider configuring VSCode: `motionbuilder.debug.port` to use another port." % Port)
        return False

    # Start the debugpy server
    debugpy.configure(python = MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(Port)

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(True)

    return True


def main():
    if not IsDebugServerRunning():
        EnableDebugServer()


main()
