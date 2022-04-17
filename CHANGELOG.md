# Change Log


## [1.2.0]
*(17-04-2022)*

**Important: Some configurations has been renamed!**

* `motionbuilder.autocompletion.patchOnActivated` -> `motionbuilder.stubFiles.patchPythonPathConfig`
* `motionbuilder.autocompletion.sdkCopyPath` -> `motionbuilder.stubFiles.copyPath`

If you've changed the default values of these properties your settings will have to be updated!

<br>

- MotionBuilder 2023 support for intellisense & documentation
- Added configuration `motionbuilder.version` to select what version to use for intellisense & when browsing documentation *(defaults to 2023)*
- Make sure all files created by this extension get's deleted when un-installed.
- Added configuration `motionbuilder.stubFiles.copyOnStartup` which is a bool defining if MoBu stub files should be copied to `motionbuilder.stubFiles.copyPath` on startup.
- Updated icon
- This extension is now released under the open-source MIT license.


## [1.1.0]
*(13-03-2022)*

- Added command & hotkey `motionbuilder.attach` that starts a debug session and attaches VSCode to MotionBuilder.
- Added configuration `motionbuilder.debug.port` to choose what port to run the debug server on, defaults to: `4243`.
- Improved traceback messages when executing code in MotionBuilder
- Fixed some C++ sdk pages missing when browsing the documentation
- `pyfbsdk` stub file improvements:
    - Removed `typings.List` import
    - Improved `__getitem__` typehints for FBPropertyLists
    - Added a few missing property typehints & docstrings

## [1.0.1]
*(27-02-2022)*

- <kbd>Ctrl</kbd> + <kbd>F1</kbd> now browses the C++ docs by default, instead of python.
- Improved line breaks in the pyfbsdk docstrings
- Fixed some examples not opening in the editor

## [1.0.0]
*(14-02-2022)*

- Re-wrote the pyfbsdk stub file generator. The stub file should now be feature complete with all of the contents from pyfbsdk, including overload functions.

## [0.1.5]
*(06-01-2022)*

- Improved the pyfbsdk stub file _(for improved auto-completion & linting)_
- Browsing documentation now uses the MotionBuilder 2022 documentation

## [0.1.4]
*(06-12-2021)*

- Fixed bug when executing selected indented code

## [0.1.3]
*(06-12-2021)*

- Selected indented code can now be executed
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