# Change Log


## [0.1.1]
*(23-11-2021)*

- Changed extention activation event to be `onStartupFinished`
- `motionbuilder.execute` hotkey now has context requirements of `"editorTextFocus && editorLangId == python"`
- All temp files are now placed inside a folder 'VSCode-MotionBuilder-Utils'
- Added Configurations:
    - `execute.showOutput`: Open up the output log when executing code from the Editor
    - `execute.clearOutput`: Clear output log each time code is executed
    - `documentation.openExamplesInEditor`: Open up example files from the docs in the editor instead of the web-browser
    - `autocompletion.patchOnActivated`: Add auto-completion path to `python.analysis.extraPaths` when extention is activated.


## [0.1.0] 
*(21-11-2021)*

- Initial release