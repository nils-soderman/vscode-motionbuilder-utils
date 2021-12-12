#
#   Code to generate a pyfbsdk stub file
#

# Make sure code is running inside of MotionBuilder
try:
    import pyfbsdk
except:
    raise Exception("Code running outside of MotionBuilder. Please run this inside of the MotionBuilder version you want to generate a stub file for.")

import importlib
import inspect
import typing
import pydoc
import sys
import os
import re

# Modules to generate a doc for
import pyfbsdk_additions
import pythonidelib
import pyfbsdk

MODULES = [pyfbsdk, pyfbsdk_additions, pythonidelib]


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "auto-completion")


# --------------------------------------------------------
#       Generate file from python's Help() function
# --------------------------------------------------------

def GenerateHelpFile(filepath, moduleName):
    with open(filepath, 'w+') as File:
        sys.stdout = File
        pydoc.help(moduleName)
        sys.stdout = sys.__stdout__
    
    return filepath


def GenerateMotionBuilderHelpFiles():
    GenerateHelpFile(os.path.join(OUTPUT_DIR, "pydbsdk_help.txt"), "pyfbsdk")
    GenerateHelpFile(os.path.join(OUTPUT_DIR, "pydbsdk_additions_help.txt"), "pyfbsdk_additions")
    GenerateHelpFile(os.path.join(OUTPUT_DIR, "pythonidelib_help.txt"), "pythonidelib")


# --------------------------------------------------------
#              Native pyfbsdk generated docs
# --------------------------------------------------------

def GetMotionBuilderInstallationDirectory():
    return os.path.dirname(os.path.dirname(os.path.dirname(sys.executable)))

def GetMotionBuilderPythonConfigDir():
    return os.path.join(GetMotionBuilderInstallationDirectory(), "bin", "config", "Python")


def PatchGeneratedDocString(Text):
    # Remove HTML tags
    for TagName, ReplaceWith in [("b", "")]:
        Text = Text.replace("<%s>" % TagName, ReplaceWith)
        Text = Text.replace("</%s>" % TagName, ReplaceWith)
        
    # Patch code
    if "@code" in Text:
        NewText = ""
        bInCodeBlock = False
        bFirstCodeLine = False
        for Line in Text.split("\n"):
            Line += "\n"
            if bInCodeBlock:
                if Line.startswith("@endcode"):
                    bInCodeBlock = False
                    Line = "\n"
                elif not Line.strip():
                    continue
                elif not bFirstCodeLine:
                    Line = "    %s" % Line
                bFirstCodeLine = False
            elif Line.startswith("@code"):
                bFirstCodeLine = True
                bInCodeBlock = True
                Line = "\n>>> "
            
            NewText += Line
        Text = NewText
        
    # Remove p prefix from paramgeters, example: pVector -> Vector
    Text = re.sub(r"\s(p)([A-Z])", r"\2", Text)
        
    return Text.strip()



def PatchArgumentName(Param:str):
    if Param.startswith("p"):
        if not (len(Param) == 2 and Param[1].isdigit()):   
            Param = Param[1:]
    return Param

def GetArgumentsFromFunction(Function):
    HelpFunction = Function.__doc__.split("->", 1)[0]
    HelpArgumentString = HelpFunction.split("(", 1)[1].strip()[:-1]
    HelpArgumentString = HelpArgumentString.replace("]", "").replace("[", "")
    HelpArguments = HelpArgumentString.split(",")
    ReturnValue = []
    for Argument in HelpArguments:
        if not Argument:
            continue
        Type, ArgName = Argument.strip().split(")")
        ReturnValue.append((ArgName.strip(), Type[1:].strip()))
    return ReturnValue

def GenerateStubFunction(Function, DocMembers):
    DocFunctions = [x for x in DocMembers if type(x).__name__ == "function"]
    DocFunctionNames = [x.__name__ for x in DocFunctions]
    
    FunctionName:str = Function.__name__
    if FunctionName.startswith("_"):
        return None
    functionString = "def %s(" % (FunctionName)
    
    # Arguments
    # get args & types from the help doc
    Arguments = GetArgumentsFromFunction(Function)
    
    DocRef = None
    if FunctionName in DocFunctionNames:
        DocIndex = DocFunctionNames.index(FunctionName)
        DocRef = DocFunctions[DocIndex]
        DocArguments = inspect.getargspec(DocRef).args
        ArgumentNames = [PatchArgumentName(x) for x in DocArguments]
        Arguments = [(Name, Arg[1]) for Name, Arg in zip(ArgumentNames, Arguments)]
        
    if Arguments:
        # Get args from
        functionString += ",".join(["%s:%s" %(x[0], x[1]) for x in Arguments])
    
    functionString += ")"
    
    # Return Type
    ReturnType = Function.__doc__.split("->", 1)[1].strip()
    if "\n" in ReturnType:
        ReturnType = ReturnType.split("\n")[0].strip()
    if ReturnType != "None":
        functionString += "->%s" % ReturnType
    functionString += ":"
    
    # Doc String
    if DocRef:
        functionString += '\n\t"""%s"""\n\t' % PatchGeneratedDocString(DocRef.__doc__)
    
    functionString += "..."
    
    return functionString



def GenerateStub(Filepath: str, Module, GeneratedDocModuleName = ""):
    Functions = [x[1] for x in inspect.getmembers(Module) if type(x[1]).__name__ == "function"]
    Classes = [x for x in inspect.getmembers(Module) if type(x[1]).__name__ == "class"]
    Types = [x for x in inspect.getmembers(Module) if type(x[1]).__name__ == "type"]
    Misc = [x for x in inspect.getmembers(Module) if type(x[1]).__name__ not in ["function", "class", "type"]]
    
    StubFileContent = ""
    DocMembers = []
    if GeneratedDocModuleName:
        ImportedModule = importlib.import_module(GeneratedDocModuleName)
        DocMembers = [x[1] for x in inspect.getmembers(ImportedModule)]
    
    for Function in Functions:
        FunctionString = GenerateStubFunction(Function, DocMembers)
        if FunctionString:
            StubFileContent += "%s\n" % FunctionString
    
        
    
    with open(Filepath, "w+") as File:
        File.write(StubFileContent)

def MotionBuilderMain():
    for Module in MODULES:
        OutputFilepath = os.path.join(OUTPUT_DIR, "%s.py" % Module.__name__)
        GenerateStub(OutputFilepath, Module, "pyfbsdk_gen_doc")
        break
    # GenerateStub(os.path.join(OUTPUT_DIR, "pydbsdk_help.txt"), "")




# if "builtin" in __name__:
MotionBuilderMain()





# def GenerateStub(HelpFile, MBGeneratedStub):
#     Content = {}
#     CurrentItem = ""
#     CurrentCategory = ""
#     with open(HelpFile, "r") as File:
#         for Line in File:
#             if Line[0].isalpha():
#                 # New category
#                 CurrentCategory = Line.strip()
#                 Content[CurrentCategory] = []
#                 CurrentItem = ""
#             elif Line.isspace():
#                 # New Item
#                 Content[CurrentCategory].append(CurrentItem)
#                 CurrentItem = ""
#             else:
#                 CurrentItem += Line

#     print(Content["FUNCTIONS"][1])