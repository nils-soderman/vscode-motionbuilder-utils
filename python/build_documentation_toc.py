import json
import sys
import os

from importlib import reload

# Append current script dir to sys paths to be able to import the documentation parser
CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

import pyfbsdk_stub_generator.mobu_stub_generator.motionbuilder_documentation_parser as docParser
reload(docParser)

OUTPUT_DIR = os.path.join(CURRENT_DIR, "..", "documentation")


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def SaveJsonFile(Filename, Content):
    with open(os.path.join(OUTPUT_DIR, Filename), "w+") as File:
        json.dump(Content, File)


def GetMotionBuilderVersion():
    import pyfbsdk
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


# ------------------------------------------
#            Generate Guide TOC
# ------------------------------------------


def BuildGuideTocDict(CategoryPage: docParser.DocumentationCategory):
    ReturnDict = {}

    PageName = CategoryPage.Title
    CategoryURL = CategoryPage.GetURLRelativeToENU()
    if CategoryURL and "files/" in CategoryURL.lower():
        ReturnDict[PageName] = {"id": CategoryURL}

    for Page in CategoryPage.Pages:
        PageName = Page.Title
        PageURL = Page.GetURLRelativeToENU()
        if len(PageName) > 1 and PageURL and "files/" in PageURL.lower():
            ReturnDict[PageName] = {"id": PageURL}

    for Child in CategoryPage.SubCategories:
        if isinstance(Child, docParser.DocumentationCategory):
            ReturnDict.update(BuildGuideTocDict(Child))

    return ReturnDict


def GenerateGuideTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)
    TableOfContent = MoBuDocumentation.GetMainTableOfContents()
    Data = {}
    for Page in TableOfContent:
        Data.update(BuildGuideTocDict(Page))

    SaveJsonFile("guide.json", Data)


# ------------------------------------------
#                Examples
# ------------------------------------------

def GenerateExamplesTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)
    PythonExamples = MoBuDocumentation.GetPythonExamples()

    Data = {}
    for ExamplePage in PythonExamples.values():
        PageName = ExamplePage.Title
        Data[PageName] = {"url": ExamplePage.GetURLRelativeToENU()}

    SaveJsonFile("examples.json", Data)

# ------------------------------------------
#                Examples
# ------------------------------------------


def GeneratePythonTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)


# ------------------------------------------
#                Examples
# ------------------------------------------

def GenerateSDKTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)


# ------------------------------------------
#              Main functions
# ------------------------------------------


def GenerateTableOfContents(Version):
    GenerateGuideTOC(Version)
    GenerateExamplesTOC(Version)
    # GeneratePythonTOC(Version)
    # GenerateSDKTOC(Version)


def main():
    MotionBuilderVersion = GetMotionBuilderVersion()
    GenerateTableOfContents(MotionBuilderVersion)


if "builtin" in __name__:
    main()
