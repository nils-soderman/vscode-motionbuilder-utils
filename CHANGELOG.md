# Change Log

## [2025.1.0] - UNRELEASED

### Fixed:
- `motionbuilder.setupCodeCompletion` will now correctly insert the path in the correct setting scope _(user/workspace/folder)_


## [2025.0.1] - 2024-04-17

### Fixed:
- `motionbuilder.setupCodeCompletion` failing to create the default directory for the stub files [#9](https://github.com/nils-soderman/vscode-motionbuilder-utils/issues/9)

## [2025.0.0] - 2024-04-13

### Changed:
- Renamed setting:
    - `motionbuilder.debug.port` -> `motionbuilder.attach.port`
    - `motionbuilder.debug.autoPort` -> `motionbuilder.attach.autoPort`
- `motionbuilder.setupCodeCompletion` now downloads the latest stubs from [pyfbsdk-stub-generator/generated-stub-files](https://github.com/nils-soderman/pyfbsdk-stub-generator/tree/main/generated-stub-files)
- The documentation & examples now browses the 2025 docs
- Extension appdata is now stored in VS Code's user-data folder

### Fixed:
- Bug preventing VS Code from attaching to MoBu 2025
- Folder settings potentially being ignored when a workspace is opened.
- Python 2.7 support for `motionbuilder.attach`

## [2024.1.0] - 2024-01-01

### Added:
- Command `motionbuilder.reloadModules` which reloads all imported python modules (excluding default site-packages).
- Setting `motionbuilder.reload.ignore`, a list of glob patterns of files to ignore when reloading modules.

### Changed:
- Renamed output channel to "MotionBuilder Output"
- Updated 2024 stub files


## [2024.0.0] - 2023-07-21

### Changed:
- Versioning scheme to match the currently latest version of MotionBuilder that the extension officially supports
- Bundle the compiled code using esbuild for faster startup time & smaller file size


## [1.4.0] - 2023-07-18

### Changed:
- Updated stub files
- If trying to attach without `debugpy` being installed, the extension will now ask before installing the module
- How data is handled between the extension and MotionBuilder
  - Most data is now sent through the socket instead of being written to disk
  - [motionbuilder-socket](https://www.npmjs.com/package/motionbuilder-socket) is now a standalone NodeJS module

### Fixed:
- Running multiple commands too fast either resulting in an error or output not correctly shown.


## [1.3.1] - 2023-04-29

### Added:
- Icons to items when browsing the documentation

### Fixed:
- Opening examples in the editor not working


## [1.3.0] - 2023-04-25

### Added: 
- MotionBuilder 2024 stub files & documentation _(Use the new command "MotionBuilder: Setup Code Completion" to update your stub files)_ 
- Added command "MotionBuilder: Setup Code Completion" `motionbuilder.setupCodeCompletion` which can be used setup code completion.

### Changed:
- Stub files are no longer automatically copied on startup.
- Extension is now enabled when a MotionBuilder command is used, instead of on startup.
- Renamed command title "Browse Documentation (Examples)" -> "Browse Examples"

### Fixed:
- Execution of selected code failing if first line is empty and second line is indented.
- Browse examples not working with 2022 & 2023 due to examples missing from those documentation versions.

### Removed:
- Removed Configurations:
    - `motionbuilder.execute.enableShortcut`
    - `motionbuilder.stubFiles.copyOnStartup`
    - `motionbuilder.stubFiles.patchPythonPathConfig`
    - `motionbuilder.stubFiles.copyPath`
- Removed Commands:
    - `motionbuilder.browseDocumentation` 
    - `motionbuilder.browseDocumentationC`


## [1.2.5] - 2023-02-12

### Changed:
- Stub files are now named .pyi
- Improved pyfbsdk stub file
- "MotionBuilder: Browse Documentation (Python)" is now the default command mapped to <kbd>Ctrl</kbd> + <kbd>F1</kbd>


## [1.2.4] - 2022-11-28

### Fixed:
- Encode/decode text sent between MotionBuilder & VS Code using UTF-8
- Folder settings beeing ignored


## [1.2.3] - 2022-10-02

### Added: 
- Added configuration `motionbuilder.execute.enableShortcut` which can be used to disable the `motionbuilder.execute` shortcut in spesific workspaces
- Added a _"Help"_ button when VS Code fails to connect to MotionBuilder, that will take the user to a troubleshooting web page

### Changed:
- The command `motionbuilder.execute` is now only enabled when a Python file is opened
- Sorted the configurations into categories

### Fixed:
- Mac & Linux support for opening documentation in web-browser


## [1.2.2] - 2022-09-18

- Fixed bug when executing selected indented code

- Updated the scope of most of the configurations to be at "resource" level


## [1.2.1] - 2022-07-25

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


## [1.2.0] - 2022-04-17

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


## [1.1.0] - 2022-03-13

- Added command & hotkey `motionbuilder.attach` that starts a debug session and attaches VS Code to MotionBuilder.

- Added configuration `motionbuilder.debug.port` to choose what port to run the debug server on, defaults to: `4243`.

- Improved traceback messages when executing code in MotionBuilder

- Fixed some C++ sdk pages missing when browsing the documentation

- `pyfbsdk` stub file improvements:
    - Removed `typings.List` import

    - Improved `__getitem__` typehints for FBPropertyLists
    
    - Added a few missing property typehints & docstrings


## [1.0.1] - 2022-02-27

- <kbd>Ctrl</kbd> + <kbd>F1</kbd> now browses the C++ docs by default, instead of python.

- Improved line breaks in the pyfbsdk docstrings

- Fixed some examples not opening in the editor


## [1.0.0] - 2022-02-14

- Re-wrote the pyfbsdk stub file generator. The stub file should now be feature complete with all of the contents from pyfbsdk, including overload functions.


## [0.1.5] - 2022-01-06

- Improved the pyfbsdk stub file _(for improved auto-completion & linting)_

- Browsing documentation now uses the MotionBuilder 2022 documentation


## [0.1.4] - 2021-12-06

- Fixed bug when executing selected indented code


## [0.1.3] - 2021-12-06

- Selected indented code can now be executed

- Improved traceback error messages when executing code in MoBu

- Added pythonidelib to the auto-completion modules

- Make sure sdk files are writeable before copying


## [0.1.2] - 2021-12-01

- AutoCompletion SDK files are now copied to APPDATA by default.

- Added Configuration:
    - `motionbuilder.autocompletion.sdkCopyPath`: Location where to copy the MoBu SDK autocompletion files


## [0.1.1] - 2021-11-25

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


## [0.1.0] - 2021-11-21

- Initial release