from pyfbsdk import *
class FBButtonGroup(object):
    """Button group class used to manage multiple radio buttons.
    This class ensure that only one radio button is enabled (it does all the ClickState management)
    
    - Use the Add method to Add new radio button to the group.
    - Use AddCallback method to register a UNIQUE callback that will be called when ANY
    of the registered radio buttons is clicked."""
    def Add(self,btn=None):
        """Add a radio button to group."""
        ...
    def AddCallback(self,callback=None):
        """Add a callback that will be call when a radiobutton in the group is clicked."""
        ...
    def _MultiCallback(self,control=None,event=None):...
class str(object):
    capitalize:str
    casefold:str
    center:str
    count:str
    encode:str
    endswith:str
    expandtabs:str
    find:str
    format:str
    format_map:str
    index:str
    isalnum:str
    isalpha:str
    isascii:str
    isdecimal:str
    isdigit:str
    isidentifier:str
    islower:str
    isnumeric:str
    isprintable:str
    isspace:str
    istitle:str
    isupper:str
    join:str
    ljust:str
    lower:str
    lstrip:str
    maketrans:str
    partition:str
    replace:str
    rfind:str
    rindex:str
    rjust:str
    rpartition:str
    rsplit:str
    rstrip:str
    split:str
    splitlines:str
    startswith:str
    strip:str
    swapcase:str
    title:str
    translate:str
    upper:str
    zfill:str
class FBBoxLayout(FBLayout):
    """Base class for a line layout (either vertical or horizontal)
    
    This class is made to ease the creation of Tool in Python. It manages
    all the 'FBLayout' region stuff (no need to use FBAddRegionParam anymore!).
    
    Generally you just Add a Control to the layout specifying some parameters.
    
    There are 2 kinds of Add: Add with fixed size and AddRelative which ensure
    the control Added will occupy a 'percentage' of the available space AFTER the
    fixed space has been assigned."""
    ControlDesc:property
    def Add(self,control=None,size=None):
        """Add a control to layout specifying its FIXED size.
        
        customparams:
        space: space between previous control
        width: fixed width if layout is vertical based
        height: fixed height if layout is horizontal based."""
        ...
    def AddRelative(self,control=None,ratio=None):
        """Add a control to layout specifying its RATIO. This means
        the control will be assigned a size based on the space left when all FIXED
        size have been allocated.
        
        customparams:
        space: space between prev control
        width: fixed width if layout is vertical based
        height: fixed height if layout is horizontal based."""
        ...
    def Remove(self,control=None):
        """Remove a control from the layout."""
        ...
    def RemoveAll(self):
        """Remove all controls from layout"""
        ...
    def _Add(self,control=None,size=None,ratio=None,customparams=None):...
    def _GetDesc(self,control=None):...
    def _Resize(self,control=None,event=None):...
    def _Restructure(self):...
    def _computeregion(self):...
class FBGridLayout(FBLayout):
    """More advance layout that allow organisation of control in a grid.
    User can place a control at specific coordinates.
    User can also setup parameters that affect whole row or column."""
    ColDesc:type
    ControlDesc:type
    RowDesc:type
    def Add(self,control=None,r=None,c=None,attachX=None,attachY=None,width=None,height=None):
        """Add control in row r and column c.
        attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
        attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
        width: fixed width of a control
        height: fixed height of a control"""
        ...
    def AddRange(self,control=None,r1=None,r2=None,c1=None,c2=None,attachX=None,attachY=None):
        """Add control in a range of coordinates. Control will span from row1 to row2 and from col1 to col2
        attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
        attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)"""
        ...
    def Remove(self,control=None):
        """Remove a control from the grid"""
        ...
    def RemoveAll(self):
        """Remove all controls from the grid"""
        ...
    def SetColRatio(self,c=None,ratio=None):
        """Set col c ratio. this col will be allocated width according to this ratio
        when all fixed width has been allocated."""
        ...
    def SetColSpacing(self,c=None,spacing=None):
        """Set col c spacing between previous col."""
        ...
    def SetColWidth(self,c=None,w=None):
        """Set col c fixed width."""
        ...
    def SetRowHeight(self,r=None,h=None):
        """Set row r fixed height"""
        ...
    def SetRowRatio(self,r=None,ratio=None):
        """Set row r ratio. this row will be allocated height according to this ratio
        when all fixed height has been allocated."""
        ...
    def SetRowSpacing(self,r=None,spacing=None):
        """Set row r spacing between previous row."""
        ...
    def _Add(self,control=None,r1=None,r2=None,c1=None,c2=None,attachX=None,attachY=None,width=None,height=None):...
    def _GetDesc(self,control=None):...
    def _GetSpace(self,element=None):...
    def _Resize(self,control=None,event=None):...
    def _Restructure(self):...
    def _Updatecols(self,c=None):...
    def _Updaterows(self,r=None):...
class FBHBoxLayout(FBBoxLayout):
    """This class manages a FBBoxLayout Horizontal (see FBBoxLayout for documentation on how to Add/Remove control).
    Add method specify the fixed width of a control."""
    ...
class FBTabControl(FBLayout):
    """A real FBTabControl that improve the behavior of the FBTabPanel.
    
    This class manage the Tabs and the 'middle region' used to display. It manages
    all the region 'swapping' necessary to implement a Tab behavior.
    
    - Use Add method to Add a Control to the FBTabControl. This will create a tab
    and ensure that when that tab is clicked the Control is shown.
    - Use SetContent with a tab index To specify which tab should be displayed."""
    def Add(self,name=None,content=None):
        """Create a tab with <name> that will display <content> when clicked."""
        ...
    def SetContent(self,index=None):
        """Show <content> associated with tab at <index>"""
        ...
    def _ChangeCallback(self,control=None,event=None):...
class FBVBoxLayout(FBBoxLayout):
    """This class manages a FBBoxLayout Vertical (see FBBoxLayout for documentation on how to Add/Remove control).
    Add method specify the fixed height of a control."""
    ...
def FBAddTool(tool=None):
    """Method that can be used for custom tool deriving from FBTool to add themselves to the too list"""
    ...
def FBAddToolListener(toollistener=None):
    """Add a tool listener that will be notified on new tool creation/destruction."""
    ...
def FBCreateTool(name=None):
    """Create a tool given a tool name. Notify all Tool listeners about it."""
    ...
def FBCreateUniqueTool(name=None):
    """Create a Tool with a unique name. Will destroy
    any other similarly named tool."""
    ...
def FBDestroyTool(tool=None):
    """Destroy a Tool."""
    ...
def FBDestroyToolByName(name=None):
    """Destroy a tool given its name. Notify all Tool listeners about it"""
    ...
def FBGetTools():
    """Get the list of Python Tools instantiated in MotionBuilder"""
    ...
def FBRemoveTool(tool=None):
    """Remove a given tool from the tool list. It won't be managed anymore by the Tool Manager"""
    ...
def FBRemoveToolListener(toollistener=None):
    """Remove a tool listener."""
    ...
def execute_file(f=None):...
def function_code(fn=None):...
def items(container=None):...
def values(container=None):...
