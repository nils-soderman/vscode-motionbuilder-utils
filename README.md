# MotionBuilder Utils (VSCode)

<b>
Please Note: This extention is currently in early development!
</b>

<br>

Editor features to assist when writing Python code for Autodesk MotionBuilder.

<br>

# Features

## Run code in MotionBuilder directly from the editor

You no longer need to leave the editor to execute code inside of MotionBuilder.
Now VSCode can act just like MotionBuilder's Python Editor.

![execute code in MB demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/demo-exec.gif?raw=true)

Command: `MotionBuilder: Execute` <br>
Keyboard Shortcut: <kbd>Ctrl</kbd> + <kbd>Enter</kbd>

The selected text will be executed, if nothing is selected the entire document will be executed.

<br>

## Auto-Completion

This extention automatically sets up Python auto-completion for the MotionBuilder sdk.

This assumes PyLance is installed as it'll add an additional path to `python.analysis.extraPaths`

<br>

## Browse the Documentation

Quickly search through the official sdk documentation from within the editor, and open the page in a new web-browser tab.

![Browse docs demo](https://github.com/nils-soderman/vscode-motionbuilder-utils/blob/main/media/demo/demo-docs.gif?raw=true)

Commands: 
- `MotionBuilder: Browse Documentation`
- `MotionBuilder: Browse Documentation (Python)`
- `MotionBuilder: Browse Documentation (Examples)`
- `MotionBuilder: Browse Documentation (C++)`

Keyboard Shortcut _(to browse the Python docs)_: <kbd>Ctrl</kbd> + <kbd>F1</kbd>


<br><br>

# Contact

If you have any questions, feature requests or run into any bugs, don't hesitate to get in contact with me:

[Personal Website](https://nilssoderman.com)<br>
[Twitter](https://twitter.com/nilssoderman "@nilssoderman")<br>
[Report an issue](https://github.com/nils-soderman/vscode-motionbuilder/issues "Report a bug on the GitHub repository")

<br>

<i>*This extention is not associated with Autodesk or MotionBuilder in any way. This is a third-party extension.</i>