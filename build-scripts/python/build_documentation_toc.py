import time
import json
import sys
import os
import re

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
#                 Guide
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
#                Python
# ------------------------------------------

def GeneratePythonTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)
    Items = MoBuDocumentation.GetPythonSDKTableOfContents()
    
    Data = {}
    for Page, Children in Items:
        PageName: str = Page.Title.strip()
        if PageName.startswith("_"):
            continue
        
        Data[PageName] = { FDictTags.Url: Page.GetURLRelativeToENU() }
        for ChildPage, ChildChildren in Children:
            ChildPageName: str = ChildPage.Title.strip()
            if ChildPageName.startswith("__") or ChildPageName == PageName:
                continue
            Data[f"{PageName}: {ChildPageName}"] = { FDictTags.Url: ChildPage.GetURLRelativeToENU() }
    
    SaveJsonFile("python.json", Data)


# ------------------------------------------
#                C++ SDK
# ------------------------------------------

def GenerateCTOC(Version):
    MoBuDocumentation = docParser.MotionBuilderDocumentation(Version)
    
    Data = {}
    for Page, Children in MoBuDocumentation.GetSDKTableOfContents():
        PageName: str = Page.Title.strip()
        if PageName.startswith("_") or PageName.isupper():
            continue
        
        Data[PageName] = { FDictTags.Url: Page.GetURLRelativeToENU() }
        for ChildPage, ChildChildren in Children:
            ChildPageName: str = ChildPage.Title.strip()
            # Skip page names with special characters (except underscores) or private names
            if ChildPageName.startswith("__") or not re.match(r'^\w+$', ChildPageName) or ChildPageName == PageName:
                continue
            Data[f"{PageName}: {ChildPageName}"] = { FDictTags.Url: ChildPage.GetURLRelativeToENU() }
    
    SaveJsonFile("c.json", Data)


# ------------------------------------------
#              Main functions
# ------------------------------------------

def GenerateTableOfContents(Version):
    def _TimeIt(Function, *args):
        StartTime = time.time()
        Function(*args)
        DeltaTime = time.time() - StartTime
        print(f"'{Function.__name__}' took {DeltaTime:.2f} sec.")
        return DeltaTime
    
    _TimeIt(GenerateGuideTOC, Version)
    _TimeIt(GenerateExamplesTOC, Version)
    _TimeIt(GeneratePythonTOC, Version)
    _TimeIt(GenerateCTOC, Version)


def main():
    StartTime = time.time()

    MotionBuilderVersion = GetMotionBuilderVersion()
    GenerateTableOfContents(MotionBuilderVersion)

    DeltaTime = time.time() - StartTime
    print(f"Generating docs took {DeltaTime:.2f} sec in total")


if "builtin" in __name__:
    main()
