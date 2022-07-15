"""
Module for executing python code in MotionBuilder
"""

# Importing these with private names to make sure they're hidden in the debug window
import tempfile as __tempfile__
import json     as __json__
import os       as __os__


# Read settings that was written by the extension (writeDataFile() in `execute-script.ts`)
__VsCodeSettingsFile__ = open(__os__.path.join(__tempfile__.gettempdir(), "VSCode-MotionBuilder-Utils", 'vscode-exec.json'), 'r')
__VsCodeData__ = __json__.load(__VsCodeSettingsFile__)
__VsCodeSettingsFile__.close()
del __VsCodeSettingsFile__

# Set __file__ & __name__ variable
__file__ = __VsCodeData__.get("__file__", "")
if "__name__" in __VsCodeData__:
    __name__ = __VsCodeData__["__name__"]

with open(__VsCodeData__["file"], 'r') as __VsCodeFile__:
    exec(compile(__VsCodeFile__.read(), __file__, "exec"))
    if "additionalPrint" in __VsCodeData__:
        print(__VsCodeData__["additionalPrint"])
