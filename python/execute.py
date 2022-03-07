import tempfile
import json
import os


# Read settings
_VsCodeSettingsFile = open(os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils", 'vscode-exec.json'), 'r')
_VsCodeData = json.load(_VsCodeSettingsFile)
_VsCodeSettingsFile.close()
del _VsCodeSettingsFile

# Set __file__
__file__ = _VsCodeData.get("__file__", "")

with open(_VsCodeData["file"], 'r') as _VsCodeFile:
    del _VsCodeData
    exec(compile(_VsCodeFile.read(), __file__, "exec"))
