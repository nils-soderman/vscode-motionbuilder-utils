import json
import sys
import os

from importlib import reload

# Append current site-packages path
CURRENT_DIR = os.path.dirname(__file__)
SITEPACKAGES_DIR = os.path.join(CURRENT_DIR, "site-packages")

if SITEPACKAGES_DIR not in sys.path:
    sys.path.append(SITEPACKAGES_DIR)


import pyfbsdk_stub_generator.motionbuilder_documentation_parser as docParser
reload(docParser)


# ------------------------------------------
#            Structs & Enums
# ------------------------------------------

class FDictTags:
    Url = "url"


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def GetMotionBuilderVersion():
    import pyfbsdk
    """ Get the current version of MotionBuilder """
    return int(2000 + pyfbsdk.FBSystem().Version / 1000)


def GetOutputDirectory():
    return os.path.join(CURRENT_DIR, "..", "..", "resources", "documentation", str(GetMotionBuilderVersion()))


def SaveJsonFile(Filename, Content):
    Directory = GetOutputDirectory()
    if not os.path.isdir(Directory):
        os.makedirs(Directory)
    
    Filepath = os.path.join(Directory, Filename)
    with open(Filepath, "w+") as File:
        json.dump(Content, File)


# ------------------------------------------
#            Generate Guide TOC
# ------------------------------------------

def BuildGuideTocDict(CategoryPage: docParser.DocumentationCategory):
    ReturnDict = {}

    PageName = CategoryPage.Title.strip()
    CategoryURL = CategoryPage.GetURLRelativeToENU()
    if CategoryURL and "files/" in CategoryURL.lower():
        ReturnDict[PageName] = {FDictTags.Url: CategoryURL}

    for Page in CategoryPage.Pages:
        PageName = Page.Title.strip()
        PageURL = Page.GetURLRelativeToENU()
        if len(PageName) > 1 and PageURL and "files/" in PageURL.lower():
            ReturnDict[PageName] = {FDictTags.Url: PageURL}

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
        PageName = ExamplePage.Title.strip()
        Data[PageName] = {FDictTags.Url: ExamplePage.GetURLRelativeToENU()}

    SaveJsonFile("examples.json", Data)


# ------------------------------------------
#                Examples
# ------------------------------------------

def GeneratePythonTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)

    Data = {}
    for Page in MoBuDocumentation.GetPythonSDKTableOfContents().values():
        PageName = Page.Title.strip()
        Data[PageName] = {FDictTags.Url: Page.GetURLRelativeToENU()}

    SaveJsonFile("python.json", Data)


# ------------------------------------------
#                Examples
# ------------------------------------------

def GenerateSDKTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)

    Data = {}
    for Page in MoBuDocumentation.GetSDKTableOfContents().values():
        PageName = Page.Title.strip()
        Data[PageName] = {FDictTags.Url: Page.GetURLRelativeToENU()}

    SaveJsonFile("c.json", Data)


# ------------------------------------------
#              Main functions
# ------------------------------------------

def GenerateTableOfContents(Version):
    GenerateGuideTOC(Version)
    GenerateExamplesTOC(Version)
    GeneratePythonTOC(Version)
    GenerateSDKTOC(Version)


def main():
    MotionBuilderVersion = GetMotionBuilderVersion()
    GenerateTableOfContents(MotionBuilderVersion)


if "builtin" in __name__:
    main()
