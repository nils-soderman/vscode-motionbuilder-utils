import subprocess
import importlib
import tempfile
import json
import sys
import os

VSCODE_DEBUG_SERVER_ENV_VAR = "MB_Utils_Debug_Enabled"

MOBU_PYTHON_EXECUTABLE = os.path.join(os.path.dirname(sys.executable), "mobupy.exe")
VSCODE_MOBU_TEMPDIR = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")


def GetVSCodeAttachSettings():
    """ Get a dict with settings passed along from VSCode """
    SettingsFilepath = os.path.join(VSCODE_MOBU_TEMPDIR, 'vscode-attach.json')
    with open(SettingsFilepath, 'r') as File:
        return json.load(File)


def IsModuleAvaliable(ModuleName):
    """ Check if a python module can be imported """
    try:
        exec("import %s" % ModuleName)
        return True
    except:
        return False


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
            ArgTarget = ""
            if Target:
                ArgTarget = "--target=%s" % Target

            # Ensure pip is avaliable
            if not IsModuleAvaliable("pip"):
                if not IsModuleAvaliable("ensurepip"):
                    return False
                
                TempInstallationDir = os.path.join(VSCODE_MOBU_TEMPDIR, "TempPipInstall")
                subprocess.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", TempInstallationDir])

                pipModulePath = ""
                for Root, Directory, Files in os.walk(TempInstallationDir):
                    if "__init__.py" in Files and os.path.basename(Root) == "pip":
                        pipModulePath = os.path.join(Root)
                        break

                if not pipModulePath:
                    return False

                subprocess.check_call([MOBU_PYTHON_EXECUTABLE, pipModulePath, "install", ArgTarget, PackageName])
            else: 
                subprocess.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "pip", "install", ArgTarget, PackageName])

    return importlib.import_module(PackageName)


def IsDebugServerRunning():
    """ Check if a debug server already has been started in this MB instance """
    return os.environ.get(VSCODE_DEBUG_SERVER_ENV_VAR, "") == str(True)


def EnableDebugServer():
    # Get settings
    Settings = GetVSCodeAttachSettings()
    Port = Settings.get("port")
    Target = Settings.get("target")

    # Attempt to import / install debugpy
    debugpy = InstallAndImportModule("debugpy", Target)
    if not debugpy:
        print("ERROR: Failed to import/install debugpy.")
        return

    # Start the debugpy server
    debugpy.configure(python = MOBU_PYTHON_EXECUTABLE)
    debugpy.listen(Port)

    

    os.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(True)


def main():
    if not IsDebugServerRunning():
        EnableDebugServer()


if "builtin" in __name__:
    main()