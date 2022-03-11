""" 
Script to start a debugpy server in MotionBuilder.
Will automatically install debugpy if module cannot be found.
"""

# Import with private names to exclude them from the debug window
import subprocess as __subprocess__
import importlib  as __importlib__
import tempfile   as __tempfile__
import socket     as __socket__
import json       as __json__
import sys        as __sys__
import os         as __os__


# Place everything inside a function to avoid creating variables/functions that show up in the debug window
def __StartMotionBuilderDebugServer__():
    VSCODE_DEBUG_SERVER_ENV_VAR = "MB_Utils_Debug_Enabled"
    MOBU_PYTHON_EXECUTABLE = __os__.path.join(__os__.path.dirname(__sys__.executable), "mobupy.exe")
    VSCODE_MOBU_TEMPDIR = __os__.path.join(__tempfile__.gettempdir(), "VSCode-MotionBuilder-Utils")

    def GetVSCodeAttachSettings():
        """ Get a dict with settings passed along from VSCode """
        SettingsFilepath = __os__.path.join(VSCODE_MOBU_TEMPDIR, 'vscode-attach.json')
        with open(SettingsFilepath, 'r') as File:
            return __json__.load(File)


    def TryImport(ModuleName, Path = ""):
        """ Attempt to import a module, returns the module if sucessful, else None """
        bAppendPath = Path and Path not in __sys__.path
        if bAppendPath:
            __sys__.path.append(Path)
        
        Module = None
        try:
            Module = __importlib__.import_module(ModuleName)
        except:
            pass
        
        if bAppendPath:
            __sys__.path.remove(Path)
        
        return Module


    def InstallAndImportModule(PackageName, Target = ""):
        Module = TryImport(PackageName)
        
        # Append the target path and try to import again
        if not Module and Target not in __sys__.path:
            Module = TryImport(PackageName, Target)

        if not Module:
            ArgTarget = ""
            if Target:
                ArgTarget = "--target=%s" % Target

            # Ensure pip is avaliable
            if not TryImport("pip"):
                if not TryImport("ensurepip"):
                    return None
                
                TempInstallationDir = __os__.path.join(VSCODE_MOBU_TEMPDIR, "TempPipInstall")
                __subprocess__.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "ensurepip", "--root", TempInstallationDir])

                pipModulePath = ""
                for Root, Directory, Files in __os__.walk(TempInstallationDir):
                    if "__init__.py" in Files and __os__.path.basename(Root) == "pip":
                        pipModulePath = __os__.path.join(Root)
                        break

                if not pipModulePath:
                    return None

                __subprocess__.check_call([MOBU_PYTHON_EXECUTABLE, pipModulePath, "install", ArgTarget, PackageName])
            else:
                __subprocess__.check_call([MOBU_PYTHON_EXECUTABLE, "-m", "pip", "install", ArgTarget, PackageName])

            Module = TryImport(PackageName, Target)

        return Module


    def IsPortAvailable(Port):
        """ Check if a port is avaliable """
        Socket = __socket__.socket(__socket__.AF_INET, __socket__.SOCK_STREAM)
        Socket.settimeout(0.05)
        Response = Socket.connect_ex(("127.0.0.1", Port))
        Socket.close()
        return Response != 0


    def IsDebugServerRunning():
        """ Check if a debug server already has been started in this MB instance """
        return __os__.environ.get(VSCODE_DEBUG_SERVER_ENV_VAR, "") == str(True)


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
            print("ERROR: Port %s is already in use! Consider configuring VSCode: `motionbuilder.debug.port` to use another port.")
            return False

        # Start the debugpy server
        debugpy.configure(python = MOBU_PYTHON_EXECUTABLE)
        debugpy.listen(Port)

        __os__.environ[VSCODE_DEBUG_SERVER_ENV_VAR] = str(True)
        
        return True


    # Main entry
    if not IsDebugServerRunning():
        EnableDebugServer()


__StartMotionBuilderDebugServer__()

# Clean up global function to not have them shown in the debug window
del __StartMotionBuilderDebugServer__