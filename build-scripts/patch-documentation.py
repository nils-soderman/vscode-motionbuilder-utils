import os
import re

AUTO_COMPLETION_FOLDER = os.path.join(os.path.dirname(__file__), "..", "auto_completion")
PYFBSDK_FILEPATH = os.path.join(AUTO_COMPLETION_FOLDER, "pyfbsdk.py")
PYFBSDK_ADDITIONS_FILEPATH = os.path.join(AUTO_COMPLETION_FOLDER, "pyfbsdk_additions.py")


def ReadFile(Filepath):
    with open(Filepath, 'r') as File:
        return File.read()


def SaveFile(Filepath, Text):
    with open(Filepath, "w+") as File:
        File.write(Text)


def PatchHTMLTags(Text):
    for TagName, ReplaceWith in [("b", "")]:
        Text = Text.replace("<%s>" % TagName, ReplaceWith)
        Text = Text.replace("</%s>" % TagName, ReplaceWith)
    return Text


def main():
    for Filepath in [PYFBSDK_FILEPATH, PYFBSDK_ADDITIONS_FILEPATH]: 
        Content = ReadFile(Filepath)
        Content = PatchHTMLTags(Content)
        SaveFile(Filepath, Content)


if __name__ == "__main__":
    main()