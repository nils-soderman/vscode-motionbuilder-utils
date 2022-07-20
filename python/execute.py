"""
Module for executing python code in MotionBuilder
"""

import contextlib
import traceback
import tempfile
import json
import sys
import os

TEMP_FOLDERPATH = os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils")
OUTPUT_FILEPATH = os.path.join(TEMP_FOLDERPATH, "vscode-exec-out.txt")
INPUT_FILEPATH = os.path.join(TEMP_FOLDERPATH, 'vscode-exec.json')


def ReadInputData():
    """ Read input data that was written with typescript (`writeDataFile()` in `execute-script.ts`) """
    with open(INPUT_FILEPATH, 'r') as VsCodeSettingsFile:
        return json.load(VsCodeSettingsFile)


def GetExecGlobals():
    """ Get globals to be used in the exec function when executing user scripts """
    if "__VsCodeVariables__" not in globals():
        globals()["__VsCodeVariables__"] = {"__builtins__": __builtins__, "__IsVsCodeExec__": True}
    return globals()["__VsCodeVariables__"]


def VsCodeExecuteCode(Code, Filename, bVsCodeIsDebugging):
    try:
        exec(compile(Code, Filename, "exec"), GetExecGlobals())
    except Exception as e:
        TracebackLines = traceback.format_exception(None, e, e.__traceback__)

        # TODO: Reformat the file URL lines to be clickable line numbers as well

        TracebackMessage = "".join(x for x in TracebackLines if VsCodeExecuteCode.__name__ not in x).strip()
        # Color the message red (this is only supported by 'Debug Console' in VsCode, and not not 'Output' log)
        if bVsCodeIsDebugging:
            TracebackMessage = '\033[91m' + TracebackMessage + '\033[0m'

        print(TracebackMessage)


def main():
    VsCodeData = ReadInputData()
    bVsCodeDebugging = VsCodeData.get("is_debugging", False)
    AdditionalPrintStr = VsCodeData.get("additionalPrint", "")

    # Set some global variables
    ExecGlobals = GetExecGlobals()
    
    TargetFilepath = VsCodeData.get("__file__", "")
    ExecGlobals["__file__"] = TargetFilepath
    
    if "__name__" in VsCodeData and VsCodeData["__name__"]:
        ExecGlobals["__name__"] = VsCodeData["__name__"]

    # Read the code file and execute it
    with open(VsCodeData["file"], 'r') as VsCodeInFile:
        if not bVsCodeDebugging and sys.version_info.major >= 3:
            # Re-direct the output through a text file
            with open(OUTPUT_FILEPATH, 'w') as VsCodeOutFile, contextlib.redirect_stdout(VsCodeOutFile):
                VsCodeExecuteCode(VsCodeInFile.read(), TargetFilepath, bVsCodeDebugging)
        else:
            VsCodeExecuteCode(VsCodeInFile.read(), TargetFilepath, bVsCodeDebugging)

        if AdditionalPrintStr:
            print(AdditionalPrintStr)


main()
