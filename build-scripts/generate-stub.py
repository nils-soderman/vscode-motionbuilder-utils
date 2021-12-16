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

TAB_CHAR = "    "

# Custom additions to insert at the top of the stub file
CUSTOM_ADDITIONS_FILEPATH =  os.path.join(os.path.dirname(__file__), "stub-custom-additions.py")

# --------------------------------------------------------
#                       Classes
# --------------------------------------------------------

class StubMainClass():
    def __init__(self, Name="", Indentation = 0) -> None:
        self.Name = Name
        self.DocString = ""
        self.SetIndentationLevel(Indentation)
        
    def SetIndentationLevel(self, Level:int):
        self._Indentation = Level + 1
        
    def GetAsString(self):
        return ""
    
    def GetDocString(self):
        if not self.DocString:
            return ""
        PatchedDocString = PatchGeneratedDocString(self.DocString)
        if not PatchedDocString:
            return ""
        return '"""%s"""' % PatchedDocString
    
    def Indent(self, Text):
        return "\n".join([(TAB_CHAR * self._Indentation) + Line.strip() for Line in Text.split("\n")])


class StubFunction(StubMainClass):
    def __init__(self, Name="", Indentation = 0) -> None:
        super().__init__(Name=Name, Indentation = Indentation)
        self.Params = []
        self.ReturnType = None
        self.bIsClassFunction = False
    
    def GetParamsAsString(self):
        # self.Params = [("Name", "Type")]
        ParamString = ""
        for Index, Param in enumerate(self.Params):
            if self.bIsClassFunction and Index == 0:
                ParamString += "self"
            else:
                ParamString += Param[0]
                if Param[1]:
                    ParamString += ":%s" % Param[1]
            ParamString += ","
            
        return ParamString[:-1]
    
    def GetAsString(self):
        FunctionAsString = 'def %s(%s)' %(self.Name, self.GetParamsAsString())
        
        if self.ReturnType and self.ReturnType != "None":
            FunctionAsString += '->%s' % self.ReturnType
            
        FunctionAsString += ":"
        
        DocString = self.GetDocString()
        if DocString:
            FunctionAsString += "\n%s\n%s" % (self.Indent(DocString), self.Indent("..."))
        else:
            FunctionAsString += "..."
        
        return FunctionAsString


class StubClass(StubMainClass):
    def __init__(self, Name="", Indentation = 0) -> None:
        super().__init__(Name = Name, Indentation = Indentation)
        self.Parents = []
        self.StubEnums = []
        self.StubProperties = []
        self.StubFunctions = []

    def GetAsString(self):
        ParentClassesAsString = ','.join(self.Parents)
        ClassAsString = "class %s(%s):" % (self.Name, ParentClassesAsString)
        
        ClassAsString += "..."
        
        return ClassAsString

class StubProperty(StubMainClass):
    def __init__(self, Name="", Indentation = 0) -> None:
        super().__init__(Name=Name, Indentation = Indentation)



# --------------------------------------------------------
#              Native pyfbsdk generated docs
# --------------------------------------------------------

def PatchGeneratedDocString(Text):
    # Remove HTML tags
    for TagName, ReplaceWith in [("b", "")]:
        Text = Text.replace("<%s>" % TagName, ReplaceWith)
        Text = Text.replace("</%s>" % TagName, ReplaceWith)
    Text = Text.replace("b>", "") # There are some broken HTML tags in there too
        
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
                else:
                    if Line.strip().startswith("//"):
                        Line = Line.replace("//", "#")
                    if not bFirstCodeLine:
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
    if Param == "True":
        Param = "bState"
    return Param


def GetArgumentsFromFunction(Function):
    DocString = Function.__doc__
    HelpFunction = DocString.split("->", 1)[0]
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


def GenerateStubFunction(Function, DocMembers, Indentation = 0, bIsClassFunction = False):
    FunctionName:str = Function.__name__
    
    StubFunctionInstance = StubFunction(FunctionName, Indentation = Indentation)
    StubFunctionInstance.bIsClassFunction = bIsClassFunction
    
    # Parameters
    Parameters = GetArgumentsFromFunction(Function)
    
    DocRef = None
    if FunctionName in DocMembers:
        DocRef = DocMembers[FunctionName]
        StubFunctionInstance.DocString = DocRef.__doc__
        DocArguments = inspect.getargspec(DocRef).args
        Parameters = [(PatchArgumentName(Name), Arg[1]) for Name, Arg in zip(DocArguments, Parameters)]
    StubFunctionInstance.Params = Parameters
    
    # Return Type
    ReturnType = Function.__doc__.split("->", 1)[1].strip()
    if "\n" in ReturnType:
        ReturnType = ReturnType.split("\n")[0].strip()
    StubFunctionInstance.ReturnType = ReturnType
        
    return StubFunctionInstance


def GetClassParents(Class):
    return Class.__bases__

def GetClassParentNames(Class):
    ParentClassNames = []
    for Parent in GetClassParents(Class):
        ParentClassName = Parent.__name__
        if ParentClassName == "instance":
            ParentClassName = ""

        elif ParentClassName == "enum":
            ParentClassName = "_Enum"
            
        ParentClassNames.append(ParentClassName)
    
    return ParentClassNames


def GetClassMembers(Class):
    IgnoreMembers = ["names", "values", "__slots__", "__instance_size__"]
    Members = inspect.getmembers(Class)
    ParentClass = GetClassParent(Class)
    UniqueMemebers = [x for x in Members if not hasattr(ParentClass, x[0]) and x[0] not in IgnoreMembers and not x[0].startswith("__")]
    return UniqueMemebers

def GenerateStubClass(Class, DocMembers):
    ClassName:str = Class.__name__
    DocClasses = [x for x in DocMembers if type(x).__name__ in ["class", "type"]]
    DocMemberNames = [x.__name__ for x in DocClasses]
    
    StubClassInstance = StubClass(ClassName)
    StubClassInstance.Parents = GetClassParentNames(Class)
    
    
    return StubClassInstance
    
    
    ClassString = "class %s(%s):\n    " % (ClassName, GetClassParentName(Class))
    
    # Docs
    DocGenRef = FindDocGenRef(DocMembers, ClassName)
    DocGenMembers = {}
    if DocGenRef:
        DocString = PatchGeneratedDocString(DocGenRef.__doc__)
        if DocString:
            ClassString += '"""%s"""\n    ' % DocString
            
        DocGenMembers = dict(GetClassMembers(DocGenRef))
    
    # Class Memebers, functions & properties
    ClassMemebers = GetClassMembers(Class)
    
    # TODO: Sort by types, generate in order of Enum, Property, Function
    for ClassMemeber in ClassMemebers:
        MemberType = type(ClassMemeber[1]).__name__
        bGeneratedDocString = False
        
        if MemberType == "function":
            bGeneratedDocString = True
            try:
                FunctionString = GenerateStubFunction(ClassMemeber[1], DocGenMembers, Indentation = TAB_CHAR + TAB_CHAR, bIsClassFunction = True)
                ClassString += "%s\n%s" % (FunctionString, TAB_CHAR)
            except:
                print("Failed for %s" % ClassMemeber[0])
        elif MemberType == "property":
            ClassString += "%s:%s\n%s" % (ClassMemeber[0], "property", TAB_CHAR)
        else:
            ClassString += "%s:%s\n%s" % (ClassMemeber[0], ClassName, TAB_CHAR)
        
        if not bGeneratedDocString and ClassMemeber[0] in DocGenMembers:
            DocString = PatchGeneratedDocString(DocGenMembers.get(ClassMemeber[0]).__doc__)
            if DocString:
                ClassString += '"""%s"""\n%s' %(DocString, TAB_CHAR) 
    
    if len(ClassMemebers) > 0:
        ClassString = ClassString.strip()
    else:
        ClassString += "..."
    
    return ClassString

def FindDocGenRef(DocMembers:dict, RefName):
    # if RefName in DocMembers:
        # return DocMembers[RefName]
    for Mebmer in DocMembers.values():
        if hasattr(Mebmer, "__name__") and Mebmer.__name__ == RefName:
            return Mebmer

def SortClasses(Classes):
    """ 
    Sort classes based on their parent class
    """
    i = 0
    ClassNames = [x.__name__ for x in Classes]
    while (i < len(Classes)):
        ParentClassName = GetClassParentName(Classes[i])
        if ParentClassName:
            ParentClassIndex = ClassNames.index(ParentClassName)
            if ParentClassIndex >= i:
                Classes.insert(ParentClassIndex + 1, Classes.pop(i))
                ClassNames.insert(ParentClassIndex + 1, ClassNames.pop(i))
                i -= 1
        
        i += 1
        
    return Classes

def GenerateStub(Filepath: str, Module, GeneratedDocModuleName = ""):
    Functions = [x[1] for x in inspect.getmembers(Module) if type(x[1]).__name__ == "function" and not x[1].__name__.startswith("_")]
    Classes = [x[1] for x in inspect.getmembers(Module) if type(x[1]).__name__ == "class"]
    Enums = [x[1] for x in inspect.getmembers(Module) if type(x[1]).__name__ == "type"]
    Misc = [x for x in inspect.getmembers(Module) if type(x[1]).__name__ not in ["function", "class", "type"]]
    
    DocMembers = []
    if GeneratedDocModuleName:
        ImportedModule = importlib.import_module(GeneratedDocModuleName)
        DocMembers = dict(inspect.getmembers(ImportedModule))
    
    # Collect all of the data
    StubFunctions = [GenerateStubFunction(x, DocMembers) for x in Functions]
    StubClasses = [GenerateStubClass(x, DocMembers) for x in Classes]
    StubEnums = [GenerateStubClass(x, DocMembers) for x in Enums]
    
    
    # TODO: Sort the classes here instead
        #Classes = SortClasses(Classes)
    
    # Generate the stub file content as a string 
    StubFileContent = ""
    if os.path.isfile(CUSTOM_ADDITIONS_FILEPATH):
        with open(CUSTOM_ADDITIONS_FILEPATH, 'r') as File:
            StubFileContent += "%s\n" % File.read()        
    
    for ListOfStubItems in [StubEnums, StubClasses, StubFunctions]:
        StubFileContent += "%s\n" % "\n".join([x.GetAsString() for x in ListOfStubItems])
    
    # Write content into the file
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
