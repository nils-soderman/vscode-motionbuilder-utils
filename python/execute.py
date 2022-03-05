import tempfile
import os
import json

with open(os.path.join(tempfile.gettempdir(), "VSCode-MotionBuilder-Utils", 'vscode-exec.json'), 'r') as _VsCodeFile:
    _VsCodeData = json.load(_VsCodeFile)
    __file__ = _VsCodeData.get("__file__", "")
    with open(_VsCodeData["file"], 'r') as _VsCodeFile: 
        exec(compile(_VsCodeFile.read(), __file__, "exec"))