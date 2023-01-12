"""
This module improves pyfbsdk UI building.

It provides Layout classes similar to classes found in Qt/GTK/Tcl/Tk that \\
helps to manage region handling and UI control positioning.

It also gives functions to create/destroy and manage Tools created in Python.
"""

import pyfbsdk

FBToolList: dict
FBToolListeners: list
FBToolManager = None

def FBCreateUniqueTool(name) -> pyfbsdk.FBTool:
    """Create a Tool with a unique name. \\
    Will destroy any other similarly named tool."""
    ...
    
def FBGetTools() -> dict:
    """Get the list of Python Tools instantiated in MotionBuilder"""
    ...

def FBCreateTool(name) -> pyfbsdk.FBTool:
    """Create a tool given a tool name. Notify all Tool listeners about it."""
    ...
        
def FBDestroyTool(tool):
    """Destroy a Tool."""
    ...
    
def FBDestroyToolByName(name):
    """Destroy a tool given its name. Notify all Tool listeners about it"""
    ...
    
        
def FBAddTool(tool) -> pyfbsdk.FBTool:
    """Method that can be used for custom tool deriving from FBTool to add themselves to the too list"""
    ...
    
def FBRemoveTool(tool):
    """Remove a given tool from the tool list. It won't be managed anymore by the Tool Manager"""
    ...
                
def FBAddToolListener(toollistener):
    """Add a tool listener that will be notified on new tool creation/destruction."""
    ...

def FBRemoveToolListener(toollistener):
    """Remove a tool listener."""
    ...

def _FBNotityToolListener():
    ...

# Layout mangement
class FBButtonGroup:
    """ Button group class used to manage multiple radio buttons. \\
        This class ensure that only one radio button is enabled (it does all the ClickState management)
        
        - Use the Add method to Add new radio button to the group.        
        - Use AddCallback method to register a UNIQUE callback that will be called when ANY of the registered radio buttons is clicked.
    """    
    def __init__(self):
        self.buttons: list
        self.callback: bool

    def Add(self,btn):
        """Add a radio button to group."""
        ...

    def AddCallback(self,callback):
        """Add a callback that will be call when a radiobutton in the group is clicked."""
        ...
        
    def _MultiCallback(self,control,event):
        ...


class FBTabControl(pyfbsdk.FBLayout):
    """
    A real FBTabControl that improve the behavior of the FBTabPanel.
    
    This class manage the Tabs and the 'middle region' used to display. It manages all the region 'swapping' necessary to implement a Tab behavior.
    
    - Use Add method to Add a Control to the FBTabControl. This will create a taband ensure that when that tab is clicked the Control is shown.
    - Use SetContent with a tab index To specify which tab should be displayed.
    """
    def __init__(self):
        self.TabPanel: pyfbsdk.FBTabPanel
        self.TabContents: list
                        
    def Add(self,name,content):
        """Create a tab with <name> that will display <content> when clicked."""
        ...

    def SetContent(self,index):
        """Show <content> associated with tab at <index>"""
        ...
        
    def _ChangeCallback(self,control,event):
        ...


class FBBoxLayout(pyfbsdk.FBLayout):
    """ 
    Base class for a line layout (either vertical or horizontal)
    
    This class is made to ease the creation of Tool in Python. It manages all the 'FBLayout' region stuff (no need to use FBAddRegionParam anymore!).
    
    Generally you just Add a Control to the layout specifying some parameters.
    
    There are 2 kinds of Add: Add with fixed size and AddRelative which ensure the control Added will occupy a 'percentage' of the available space AFTER the fixed space has been assigned.        
    """    
                   
    def __init__(self,floworientation):
        self.controls: list
        self.ratio: float
        self.allocatedsize: int
        self.floworientation: floworientation
        self.default_space: int
            
    def Add(self, control, size, **customparams):
        """ 
        Add a control to layout specifying its FIXED size.
    
        ### customparams:
            - space: space between previous control
            - width: fixed width if layout is vertical based
            - height: fixed height if layout is horizontal based.
        """
        ...

    def AddRelative(self, control, ratio=1.0, **customparams):
        """
        Add a control to layout specifying its RATIO. This means the control will be assigned a size based on the space left when all FIXED size have been allocated.
    
        ### customparams:
            - space: space between prev control
            - width: fixed width if layout is vertical based
            - height: fixed height if layout is horizontal based.
        """
        ...
        
    def Remove(self,control):
        """ Remove a control from the layout. """
        ...
    
    def RemoveAll(self):
        """Remove all controls from layout"""
        ...

    class ControlDesc:
        space: property
        def __init__(self,regionName, control, size, ratio, customparams):
            self.regionName: regionName
            self.size: size
            self.control: control
            self.ratio: ratio
            self.customparams: customparams
                        
        def getSpace(self) -> any: ...
            
        def setSpace(self, space): ...
            
        
    def _Resize(self,control, event): ...

    def _GetDesc(self,control) -> str: ...

    def _Add(self,control, size, ratio, customparams): ...
        
    def _Restructure(self): ...
        
    def _computeregion(self): ...

class FBHBoxLayout(FBBoxLayout):
    """ This class manages a FBBoxLayout Horizontal (see FBBoxLayout for documentation on how to Add/Remove control). \\
        Add method specify the fixed width of a control.
    """
    def __init__(self,floworientation = pyfbsdk.FBAttachType.kFBAttachLeft):
        """ 
        ### floworientation: 
            - FBAttachType.kFBAttachLeft : all controls added from left to right ->
            - FBAttachType.kFBAttachRight: all controls added from right to left <-
        """
        ...
        
    def _computeregion(self): ...
            
class FBVBoxLayout(FBBoxLayout):
    """ This class manages a FBBoxLayout Vertical (see FBBoxLayout for documentation on how to Add/Remove control). \\
        Add method specify the fixed height of a control.
    """
    def __init__(self,floworientation = pyfbsdk.FBAttachType.kFBAttachTop):
        """ floworientation: 
            FBAttachType.kFBAttachTop : all controls added from top to bottom 
            FBAttachType.kFBAttachBottom: all controls added from bottom to top
        """
        ...
        
    def _computeregion(self): ...
            
class FBGridLayout(pyfbsdk.FBLayout):
    """ More advance layout that allow organisation of control in a grid. \\
        User can place a control at specific coordinates. \\
        User can also setup parameters that affect whole row or column. \\
    """
    def __init__(self,spacing = 5):
        self.defaultspacing: int
        self.controls: list
        self.rows: list
        self.cols: list

    def Add(self,control,r,c,attachX = pyfbsdk.FBAttachType.kFBAttachLeft,attachY = pyfbsdk.FBAttachType.kFBAttachTop,width = None,height = None):
        """ Add control in row r and column c.
            attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
            attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
            width: fixed width of a control
            height: fixed height of a control
        """
        ...
                
    def AddRange(self,control,r1,r2,c1,c2,attachX = pyfbsdk.FBAttachType.kFBAttachLeft,attachY = pyfbsdk.FBAttachType.kFBAttachTop):
        """ Add control in a range of coordinates. Control will span from row1 to row2 and from col1 to col2        
            attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
            attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
        """
        ...
        
    def Remove(self,control):
        """Remove a control from the grid"""
        ...
        
    def RemoveAll(self):
        """Remove all controls from the grid"""
        ...
        
    def SetRowHeight(self,r,h):
        """ Set row r fixed height"""
        ...
        
    def SetRowRatio(self,r,ratio):
        """ Set row r ratio. this row will be allocated height according to this ratio when all fixed height has been allocated."""
        ...

        
    def SetRowSpacing(self,r,spacing):
        """ Set row r spacing between previous row. """
        ...
        
    def SetColWidth(self,c,w):
        """ Set col c fixed width. """
        ...
            
    def SetColRatio(self,c,ratio):
        """ Set col c ratio. this col will be allocated width according to this ratio when all fixed width has been allocated. """
        ...
        
    def SetColSpacing(self,c,spacing):
        """ Set col c spacing between previous col."""
        ...
    
    def _GetDesc(self,control) -> str:
        ...

    class ColDesc:
        def __init__(self):
            self.width: None
            self.ratio: float
            self.spacing: None
            self.x: float
            self.w: float
        def Right(self) -> float: ...
            
    class RowDesc:
        def __init__(self):
            self.height: None
            self.ratio: float
            self.spacing: None
            self.y: float
            self.h: float
        def Bottom(self) -> float: ...
        
            
    class ControlDesc:
        def __init__(self,control,regionName,r1,r2,c1,c2,attachX,attachY,w,h):
            self.control: control
            self.regionName: regionName
            self.ratio: float
            self.r1: r1
            self.r2: r2
            self.c1: c1
            self.c2: c2
            self.attachX: attachX
            self.attachY: attachY
            self.w: w
            self.h: h
        
    def _Resize(self,control, event): ...
        
    def _Add(self,control,r1,r2,c1,c2,attachX,attachY,width,height): ...
                
    def _Updaterows(self,r): ...
        
    def _Updatecols(self,c): ...
        
    def _GetSpace(self,element): ...

    def _Restructure(self): ...
