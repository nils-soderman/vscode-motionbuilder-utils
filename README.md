# MotionBuilder Utils (Visual Studio Code)

Editor features to assist when writing Python code for Autodesk MotionBuilder.

<br>

# Features

## Execute Code

Run code in MotionBuilder directly from within the editor

![execute code in MotionBuilder demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/demo-exec.gif?raw=true)

Command: `MotionBuilder: Execute` <br>
Keyboard Shortcut: <kbd>Ctrl</kbd> + <kbd>Enter</kbd>

The selected text will be executed, if nothing is selected the entire document will be executed.

<br>

## Code Completion

This extention comes with improved stub files for the `pyfbsdk` module.  

![Better auto-completion demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/auto-completion.jpg?raw=true)

* Feature complete _(contains all of the functions & classes that can be accessed in the pyfbsdk module)_
* Variable type annotations
* Readable descriptions

Command _(to setup code completion)_: `MotionBuilder: Setup Code Completion` <br>

<br>

## Debugging

Attach VS Code to MotionBuilder to debug your scripts, set breakpoints & step through the code.

![Debugging MotionBuilder Python demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/demo-debug.gif?raw=true)

Command: `MotionBuilder: Attach`

<br>

## Browse the Documentation

Quickly search through the official sdk documentation from within the editor, and open the page in a new web-browser tab.

![Browse MotionBuilder sdk documentation demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/demo-docs.gif?raw=true)

Commands: 
- `MotionBuilder: Browse Documentation`
- `MotionBuilder: Browse Examples`

Keyboard Shortcut _(to browse the Python docs)_: <kbd>Ctrl</kbd> + <kbd>F1</kbd>

<br>

#### Note:
Commands can be run from VS Code's command palette, `Show All Commands` _(Default shortcut: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)_

<br>

# Contact

If you have any questions, suggestions or run into issues, please [open an issue](https://github.com/nils-soderman/vscode-motionbuilder/issues "GitHub issues") on the GitHub repository.

<br>

<i>*This is a third-party extension and is not associated with Autodesk or MotionBuilder in any way.</i>