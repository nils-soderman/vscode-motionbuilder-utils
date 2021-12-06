# Change Log

## [0.1.3]
*(06-12-2021)*

- Intented code can now be executed
- Improved traceback error messages when executing code in MoBu
- Added pythonidelib to the auto-completion modules
- Make sure sdk files are writeable before copying


## [0.1.2]
*(01-12-2021)*

- AutoCompletion SDK files are now copied to APPDATA by default.
- Added Configuration:
    - `motionbuilder.autocompletion.sdkCopyPath`: Location where to copy the MoBu SDK autocompletion files



## [0.1.1]
*(25-11-2021)*

- Fixed \_\_file\_\_ variable not beeing set when executing code
- Changed extention activation event to be `onStartupFinished`
- All temp files are now placed inside a folder 'VSCode-MotionBuilder-Utils'
- Clean up temp files/folder when extension is deactivated
- `motionbuilder.execute` hotkey now has context requirements of `"editorTextFocus && editorLangId == python"`
- Added Configurations:
    - `motionbuilder.execute.showOutput`: Open up the output log when executing code from the Editor
    - `motionbuilder.execute.clearOutput`: Clear output log each time code is executed
    - `motionbuilder.documentation.openExamplesInEditor`: Open up example files from the docs in the editor instead of the web-browser
    - `motionbuilder.autocompletion.patchOnActivated`: Add auto-completion path to `python.analysis.extraPaths` when extention is activated.


## [0.1.0] 
*(21-11-2021)*

- Initial release