"""
Module for executing python code in MotionBuilder
"""

# Importing these with private names to make sure they're hidden in the debug window
import traceback as __traceback__
import tempfile  as __tempfile__
import json      as __json__
import sys       as __sys__
import os        as __os__


def __VsCodeExecuteCode__(Code, Filename, __bVsCodeIsDebugging__):
    try:
        exec(compile(Code, Filename, "exec"))
    except Exception as e:
        TracebackLines = __traceback__.format_exception(None, e, e.__traceback__)

        # TODO: Reformat the file URL lines to be clickable line numbers as well

        TracebackMessage = "".join(x for x in TracebackLines if __VsCodeExecuteCode__.__name__ not in x).strip()
        if __bVsCodeIsDebugging__:
            TracebackMessage = '\033[91m' + TracebackMessage + '\033[0m'

        print(TracebackMessage)


# Read settings that was written by the extension (writeDataFile() in `execute-script.ts`)
__FolderPath__ = __os__.path.join(__tempfile__.gettempdir(), "VSCode-MotionBuilder-Utils")
__OutputFilePath__ = __os__.path.join(__FolderPath__, "vscode-exec-out.txt")
__VsCodeSettingsFile__ = open(__os__.path.join(__FolderPath__, 'vscode-exec.json'), 'r')
__VsCodeData__ = __json__.load(__VsCodeSettingsFile__)
__VsCodeSettingsFile__.close()
del __VsCodeSettingsFile__

__bVsCodeIsDebugging__ = __VsCodeData__.get("is_debugging", False)
__VsCodeAdditionalPrint__ = __VsCodeData__.get("additionalPrint")

# Set __file__ & __name__ variable
__file__ = __VsCodeData__.get("__file__", "")
if "__name__" in __VsCodeData__:
    __name__ = __VsCodeData__["__name__"]

with open(__VsCodeData__["file"], 'r') as __VsCodeInFile__:
    if not __bVsCodeIsDebugging__ and __sys__.version_info.major >= 3:
        from contextlib import redirect_stdout as __redirect_stdout__
        with open(__OutputFilePath__, 'w') as __VsCodeOutFile__:
            with __redirect_stdout__(__VsCodeOutFile__):
                __VsCodeExecuteCode__(__VsCodeInFile__.read(), __file__, __bVsCodeIsDebugging__)
    else:
        __VsCodeExecuteCode__(__VsCodeInFile__.read(), __file__, __bVsCodeIsDebugging__)

    if __VsCodeAdditionalPrint__:
        print(__VsCodeAdditionalPrint__)