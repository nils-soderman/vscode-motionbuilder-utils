# Change Log

## [1.2.2]
*(xx-08-2022)*

- Updated the scope of all of the configurations to be at "resource" level


## [1.2.1]
*(25-07-2022)*

- Fixed characters missing from the output when printing large amounts of data _(MotionBuilder 2022+)_

- Fixed output not appearing in the output console in MB 2023 if a "Python Editor" window hadn't been spawned

- Added config `motionbuilder.execute.name` which can be used to set the python variable `__name__` to something unique when executing code through VS Code

- Added a global variable `__IsVsCodeExec__` which is `True` while executing code through VS Code. Example usage:
    ```python
    bIsRunningFromVsCode = globals().get('__IsVsCodeExec__', False)
    ```

- Traceback messages now include the line numbers in the clickable filepath URLs 

- It's now possible to attach to MotionBuilder even if another debug session is already active

- Fixed debugy installation for Python 2.7 when attaching to MotionBuilder

- The documentation now includes class methods and properties

- pyfbsdk stub file improvements

___

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

___

## [1.1.0]
*(13-03-2022)*

- Added command & hotkey `motionbuilder.attach` that starts a debug session and attaches VS Code to MotionBuilder.

- Added configuration `motionbuilder.debug.port` to choose what port to run the debug server on, defaults to: `4243`.

- Improved traceback messages when executing code in MotionBuilder

- Fixed some C++ sdk pages missing when browsing the documentation

- `pyfbsdk` stub file improvements:
    - Removed `typings.List` import

    - Improved `__getitem__` typehints for FBPropertyLists
    
    - Added a few missing property typehints & docstrings

___

## [1.0.1]
*(27-02-2022)*

- <kbd>Ctrl</kbd> + <kbd>F1</kbd> now browses the C++ docs by default, instead of python.

- Improved line breaks in the pyfbsdk docstrings

- Fixed some examples not opening in the editor

___

## [1.0.0]
*(14-02-2022)*

- Re-wrote the pyfbsdk stub file generator. The stub file should now be feature complete with all of the contents from pyfbsdk, including overload functions.

___

## [0.1.5]
*(06-01-2022)*

- Improved the pyfbsdk stub file _(for improved auto-completion & linting)_

- Browsing documentation now uses the MotionBuilder 2022 documentation

___

## [0.1.4]
*(06-12-2021)*

- Fixed bug when executing selected indented code

___

## [0.1.3]
*(06-12-2021)*

- Selected indented code can now be executed

- Improved traceback error messages when executing code in MoBu

- Added pythonidelib to the auto-completion modules

- Make sure sdk files are writeable before copying

___

## [0.1.2]
*(01-12-2021)*

- AutoCompletion SDK files are now copied to APPDATA by default.

- Added Configuration:
    - `motionbuilder.autocompletion.sdkCopyPath`: Location where to copy the MoBu SDK autocompletion files

___

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

___

## [0.1.0] 
*(21-11-2021)*

- Initial release