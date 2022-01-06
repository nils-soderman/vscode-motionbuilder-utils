"""
This module improves pyfbsdk UI building.

It provides Layout classes similar to classes found in Qt/GTK/Tcl/Tk that
helps to manage region handling and UI control positioning.

It also gives functions to create/destroy and manage Tools created in Python.

"""

from pyfbsdk23 import *
import pyfbsdk

# Tool Management
FBToolList = {}
FBToolListeners = []
FBToolManager = None

def FBCreateUniqueTool(name):
    """Create a Tool with a unique name. Will destroy 
    any other similarly named tool."""
    
    FBDestroyToolByName(name)
    return FBCreateTool(name)
    
def FBGetTools():
    """Get the list of Python Tools instantiated in MotionBuilder"""
    return FBToolList

def FBCreateTool(name):
    """Create a tool given a tool name. Notify all Tool listeners about it."""
    t = pyfbsdk.FBTool(name)
    return FBAddTool(t)
        
def FBDestroyTool(tool):
    """Destroy a Tool."""
    if tool:
        FBDestroyToolByName(tool.Name)
    
def FBDestroyToolByName(name):
    """Destroy a tool given its name. Notify all Tool listeners about it"""
    if name in FBToolList:
        FBRemoveTool(FBToolList[name])
    pyfbsdk._DestroyToolByName(name)
    
        
def FBAddTool(tool):
    """Method that can be used for custom tool deriving from FBTool to add themselves to the too list"""
    FBToolList[tool.Name] = tool
    # notify about new tool
    _FBNotityToolListener()
    return tool
    
def FBRemoveTool(tool):
    """Remove a given tool from the tool list. It won't be managed anymore by the Tool Manager"""
    if tool.Name in FBToolList:
        del FBToolList[tool.Name]
        _FBNotityToolListener()
                
def FBAddToolListener(toollistener):
    """Add a tool listener that will be notified on new tool creation/destruction."""
    if not toollistener in FBToolListeners:
        FBToolListeners.append(toollistener)
    else:
        print("Already in tool listener list")

def FBRemoveToolListener(toollistener):
    """Remove a tool listener."""
    if toollistener in FBToolListeners:
        FBToolListeners.remove(toollistener)
    else:
        print("not in toollistener list")

def _FBNotityToolListener():
    for l in FBToolListeners:
        l(FBToolList)

# Layout mangement
class FBButtonGroup:
    """ Button group class used to manage multiple radio buttons. 
        This class ensure that only one radio button is enabled (it does all the ClickState management)
        
        - Use the Add method to Add new radio button to the group.        
        - Use AddCallback method to register a UNIQUE callback that will be called when ANY
          of the registered radio buttons is clicked.
    """    
    def __init__(self):
        self.buttons = []
        self.callback = False

    def Add(self,btn):
        """Add a radio button to group."""
        self.buttons.append(btn)
        btn.OnClick.Add(self._MultiCallback)

    def AddCallback(self,callback):
        """Add a callback that will be call when a radiobutton in the group is clicked."""
        self.callback = callback
        
    def _MultiCallback(self,control,event):
        for b in self.buttons:
            if b != control:
                b.State = False
        if self.callback:
            self.callback(control,event)


class FBTabControl(pyfbsdk.FBLayout):
    """ A real FBTabControl that improve the behavior of the FBTabPanel.
        
        This class manage the Tabs and the 'middle region' used to display. It manages
        all the region 'swapping' necessary to implement a Tab behavior.
        
        - Use Add method to Add a Control to the FBTabControl. This will create a tab
          and ensure that when that tab is clicked the Control is shown.
        - Use SetContent with a tab index To specify which tab should be displayed.
    """    
    def __init__(self):
        from pyfbsdk import FBAddRegionParam
        from pyfbsdk import FBAttachType
        
        pyfbsdk.FBLayout.__init__(self)
        self.TabPanel = pyfbsdk.FBTabPanel()
        self.TabContents = []
        self.TabPanel.OnChange.Add(self._ChangeCallback)
        
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")

        self.AddRegion("TabPanel","TabPanel", x, y, w, h)
        self.SetControl("TabPanel",self.TabPanel)

        # create Main region where tab change of layout will occur
        x = FBAddRegionParam(5,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(5,FBAttachType.kFBAttachBottom,"TabPanel")
        w = FBAddRegionParam(-5,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(-5,FBAttachType.kFBAttachBottom,"")

        self.AddRegion("mainlyt","mainlyt", x, y, w, h)
                        
    def Add(self,name,content):
        """Create a tab with <name> that will display <content> when clicked."""
        self.TabPanel.Items.append(name)
        self.TabContents.append(content)
        self.SetContent(len(self.TabPanel.Items) - 1)

    def SetContent(self,index):
        """Show <content> associated with tab at <index>"""
        self.TabPanel.ItemIndex = index
        self.SetControl("mainlyt",self.TabContents[index])
        
    def _ChangeCallback(self,control,event):
        self.SetContent(control.ItemIndex)


class FBBoxLayout(pyfbsdk.FBLayout):
    """ Base class for a line layout (either vertical or horizontal)
    
        This class is made to ease the creation of Tool in Python. It manages
        all the 'FBLayout' region stuff (no need to use FBAddRegionParam anymore!).
        
        Generally you just Add a Control to the layout specifying some parameters.
        
        There are 2 kinds of Add: Add with fixed size and AddRelative which ensure
        the control Added will occupy a 'percentage' of the available space AFTER the 
        fixed space has been assigned.        
    """    
                   
    def __init__(self,floworientation):
        pyfbsdk.FBLayout.__init__(self)
        self.controls = []
        self.ratio = 0.0
        self.allocatedsize = 0
        self.floworientation = floworientation
        self.default_space = 5
        self.OnResize.Add(self._Resize)
            
    def Add(self, control, size, **customparams):
        """ Add a control to layout specifying its FIXED size.
        
            customparams:
            space: space between previous control
            width: fixed width if layout is vertical based
            height: fixed height if layout is horizontal based.
            """
        self._Add(control,size,0.0,customparams)

    def AddRelative(self, control, ratio=1.0, **customparams):
        """ Add a control to layout specifying its RATIO. This means
            the control will be assigned a size based on the space left when all FIXED
            size have been allocated.
        
            customparams:
            space: space between prev control
            width: fixed width if layout is vertical based
            height: fixed height if layout is horizontal based.
            """
        self._Add(control,0,ratio,customparams)
        
    def Remove(self,control):
        """ Remove a control from the layout.
        """
        desc = self._GetDesc(control)
        if desc:
            # Remove and destroy the control and the region
            self.controls.remove(desc)
            self.RemoveRegion(control.RegionName)
            self._Restructure()
    
    def RemoveAll(self):
        """Remove all controls from layout
        """
        for c in self.controls:
            # Remove and destroy the control and the region
            self.RemoveRegion(c.control.RegionName)
        self.controls = []
        self._Restructure()

    class ControlDesc:
        def __init__(self,regionName, control, size, ratio, customparams):
            self.regionName = regionName
            self.size = size
            self.control= control
            self.ratio= ratio
            self.customparams= customparams
                        
        def getSpace(self):
            return self.customparams['space']
            
        def setSpace(self, space):
            self.customparams['space'] = space
            
        space = property(getSpace, setSpace)
        
    def _Resize(self,control, event):
        self._Restructure()

    def _GetDesc(self,control):
        for desc in self.controls:
            if desc.control == control:
                return desc
        return None

    def _Add(self,control, size, ratio, customparams):
        from pyfbsdk import FBAddRegionParam, FBAttachType, FBLabel
        
        # create region for newly added control        
        regionName = "region%d" % (len(self.controls))        
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        
        if 'width' in customparams:
            w = FBAddRegionParam(customparams['width'],FBAttachType.kFBAttachNone,"")
        else:
            w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        
        if 'height' in customparams:
            h = FBAddRegionParam(customparams['height'],FBAttachType.kFBAttachNone,"")
        else:
            h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        
        self.AddRegion(regionName, regionName, x, y, w, h)
        if not control:
            control = FBLabel()
            control.Caption = ""
            
        control.Name = regionName
        self.SetControl(regionName, control)
        
        space = customparams.setdefault('space',self.default_space)
        self.ratio += ratio
        self.allocatedsize += space + size
        self.controls.append( FBBoxLayout.ControlDesc( regionName, control, size, ratio, customparams ) )
        
        self._Restructure()
        
    def _Restructure(self):                
        self.SetAutoRestructure(False)
        
        self._computeregion()
            
        # replace all our layout
        self.SetAutoRestructure(True)
        self.Restructure(False)
        
    def _computeregion(self):
        raise RuntimeError("Must be reimplemented!" )
        

class FBHBoxLayout(FBBoxLayout):
    """ This class manages a FBBoxLayout Horizontal (see FBBoxLayout for documentation on how to Add/Remove control).
        Add method specify the fixed width of a control.
    """
    def __init__(self,floworientation = pyfbsdk.FBAttachType.kFBAttachLeft):
        """ floworientation: 
            FBAttachType.kFBAttachLeft : all controls added from left to right ->
            FBAttachType.kFBAttachRight: all controls added from right to left <-
        """
        FBBoxLayout.__init__(self,floworientation)
        
    def _computeregion(self):
        from pyfbsdk import FBAttachType
        
        spaceAvailable = self.RegionPosMaxX - self.RegionPosMinX - self.allocatedsize
        
        if self.floworientation == FBAttachType.kFBAttachLeft:
            relativeAttachType = FBAttachType.kFBAttachRight
        else:
            relativeAttachType = FBAttachType.kFBAttachLeft
            
        attachType = self.floworientation
        anchor = None
        for c in self.controls:
            if c.size > 0:
                size = c.size
            else:
                size = int((c.ratio / self.ratio) * spaceAvailable)
            c.control.RegionOffsetWidth = size
            c.control.RegionAttachTypeWidth = FBAttachType.kFBAttachNone
                                    
            if self.floworientation == FBAttachType.kFBAttachLeft:
                offset = c.space
            else:
                offset = -size - c.space
            
            c.control.RegionOffsetX = offset
            c.control.RegionAttachTypeX = attachType
            if anchor:
                c.control.RegionAttachToX = anchor
            
            attachType = relativeAttachType
            anchor = c.control
            
class FBVBoxLayout(FBBoxLayout):
    """ This class manages a FBBoxLayout Vertical (see FBBoxLayout for documentation on how to Add/Remove control).
        Add method specify the fixed height of a control.
    """
    def __init__(self,floworientation = pyfbsdk.FBAttachType.kFBAttachTop):
        """ floworientation: 
            FBAttachType.kFBAttachTop : all controls added from top to bottom 
            FBAttachType.kFBAttachBottom: all controls added from bottom to top
        """
        FBBoxLayout.__init__(self,floworientation)
        
    def _computeregion(self):
        from pyfbsdk import FBAttachType
        
        spaceAvailable = self.RegionPosMaxY - self.RegionPosMinY - self.allocatedsize
        
        if self.floworientation == FBAttachType.kFBAttachTop:
            relativeAttachType = FBAttachType.kFBAttachBottom
        else:
            relativeAttachType = FBAttachType.kFBAttachTop
            
        attachType = self.floworientation
        anchor = None
        for c in self.controls:
            if c.size > 0:
                size = c.size
            else:
                size = int((c.ratio / self.ratio) * spaceAvailable)
            c.control.RegionOffsetHeight = size
            c.control.RegionAttachTypeHeight = FBAttachType.kFBAttachNone
            
            if self.floworientation == FBAttachType.kFBAttachTop:
                offset = c.space
            else:
                offset = -size - c.space
            
            c.control.RegionOffsetY = offset
            c.control.RegionAttachTypeY = attachType
            if anchor:
                c.control.RegionAttachToY = anchor
            
            attachType = relativeAttachType
            anchor = c.control
            
class FBGridLayout(pyfbsdk.FBLayout):
    """ More advance layout that allow organisation of control in a grid. 
        User can place a control at specific coordinates. 
        User can also setup parameters that affect whole row or column.
    """
    def __init__(self,spacing = 5):
        pyfbsdk.FBLayout.__init__(self)
        self.defaultspacing = spacing
        self.controls = []
        self.rows = []
        self.cols = []
        self.OnResize.Add(self._Resize)
            
            
    def Add(self,control,r,c,attachX = pyfbsdk.FBAttachType.kFBAttachLeft,attachY = pyfbsdk.FBAttachType.kFBAttachTop,width = None,height = None):
        """ Add control in row r and column c.
            attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
            attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
            width: fixed width of a control
            height: fixed height of a control
        """
        self._Add(control,r,r,c,c,attachX,attachY,width,height)
                
    def AddRange(self,control,r1,r2,c1,c2,attachX = pyfbsdk.FBAttachType.kFBAttachLeft,attachY = pyfbsdk.FBAttachType.kFBAttachTop):
        """ Add control in a range of coordinates. Control will span from row1 to row2 and from col1 to col2        
            attachX: specifies a control horizontal attachment in a column (kFBAttachLeft, kFBAttachRight)
            attachY: specifies a control veritcal attachment in a row (kFBAttachTop, kFBAttachBottom)
        """
        self._Add(control,r1,r2,c1,c2,attachX,attachY,None,None)
        
    def Remove(self,control):
        """Remove a control from the grid"""
        desc = self._GetDesc(control)
        if desc:
            self.controls.remove(desc)
            # Remove and destroy the control and the region
            self.RemoveRegion(control.Name)
            self._Restructure()
        
    def RemoveAll(self):
        """Remove all controls from the grid"""
        for c in self.controls:
            # Remove and destroy the control and the region
            self.RemoveRegion(c.control.RegionName)            
        self._Restructure()
        
    def SetRowHeight(self,r,h):
        """ Set row r fixed height"""
        self._Updaterows(r)
        self.rows[r].height = h
        self._Restructure()
        
    def SetRowRatio(self,r,ratio):
        """ Set row r ratio. this row will be allocated height according to this ratio
            when all fixed height has been allocated.
        """
        self._Updaterows(r)
        self.rows[r].ratio = ratio
        self._Restructure()

        
    def SetRowSpacing(self,r,spacing):
        """ Set row r spacing between previous row.
        """
        self._Updaterows(r)
        self.rows[r].spacing = spacing
        self._Restructure()
        
    def SetColWidth(self,c,w):
        """ Set col c fixed width.
        """
        self._Updatecols(c)
        self.cols[c].width = w
        self._Restructure()
            
    def SetColRatio(self,c,ratio):
        """ Set col c ratio. this col will be allocated width according to this ratio
            when all fixed width has been allocated.
        """
        self._Updatecols(c)
        self.cols[c].ratio = ratio
        self._Restructure()
        
    def SetColSpacing(self,c,spacing):
        """ Set col c spacing between previous col.
        """
        self._Updatecols(c)
        self.cols[c].spacing = spacing
        self._Restructure()
    
    def _GetDesc(self,control):
        for desc in self.controls:
            if desc.control == control:
                return desc
        return None

    class ColDesc:
        def __init__(self):
            # user define value
            self.width = None
            self.ratio = 1.0
            self.spacing = None
            # computed values for region placement
            self.x = 0
            self.w = 0
        def Right(self):
            return self.x + self.w

            
    class RowDesc:
        def __init__(self):
            # user define value
            self.height = None
            self.ratio = 1.0
            self.spacing = None
            # computed values for region placement
            self.y = 0
            self.h = 0
        def Bottom(self):
            return self.y + self.h
            
    class ControlDesc:
        def __init__(self,control,regionName,r1,r2,c1,c2,attachX,attachY,w,h):
            self.control = control
            self.regionName= regionName
            self.ratio = 1.0
            self.r1 = r1
            self.r2 = r2
            self.c1 = c1
            self.c2 = c2
            self.attachX = attachX
            self.attachY = attachY
            self.w = w
            self.h = h
        
    def _Resize(self,control, event):
        self._Restructure()
        
    def _Add(self,control,r1,r2,c1,c2,attachX,attachY,width,height):
        self._Updaterows(r2)
        self._Updatecols(c2)
                
        from pyfbsdk import FBAddRegionParam
        from pyfbsdk import FBAttachType
        
        # create region for newly added control        
        regionName = "region(%d,%d,%d,%d)" % (r1,r2,c1,c2)
        control.name = regionName
        x = FBAddRegionParam(0,attachX,"")
        y = FBAddRegionParam(0,attachY,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        
        self.AddRegion(regionName, regionName, x, y, w, h)
        
        if not control:
            control = FBLabel()
            control.Caption = ""
        self.SetControl(regionName, control)
                
        self.controls.append(FBGridLayout.ControlDesc(control,regionName,r1,r2,c1,c2,attachX,attachY,width,height))
        
        self._Restructure()
                
    def _Updaterows(self,r):
        while len(self.rows) <= r:
            self.rows.append(FBGridLayout.RowDesc())
        
    def _Updatecols(self,c):
        while len(self.cols) <= c:
            self.cols.append(FBGridLayout.ColDesc())
        
    def _GetSpace(self,element):
        if element.spacing:
            return element.spacing
        else:
            return self.defaultspacing

    def _Restructure(self):                
        from pyfbsdk import FBAttachType
        
        self.SetAutoRestructure(False)
                
        width = self.RegionPosMaxX - self.RegionPosMinX
        height = self.RegionPosMaxY - self.RegionPosMinY
                
        # check if in our controls, we need to update our row/col fixed size        
        for c in self.controls:
            if c.h and self.rows[c.r1].height and self.rows[c.r1].height < c.h:
                self.rows[c.r1].height = c.h
                    
            if c.w and self.cols[c.c1].width and self.cols[c.c1].width < c.w:
                self.cols[c.c1].width = c.w
                
        # compute the size of each col/rows        
        wfixed = 0
        wspace = 0
        wratio = 0.0
        for col in self.cols:
            wspace += self._GetSpace(col)
            if col.width:
                wfixed += col.width
            else:
                wratio += col.ratio
            
        wavailable = width - wspace - wfixed
        x = 0
        for col in self.cols:
            col.x = x + self._GetSpace(col)
            if col.width:
                col.w = col.width
            else:
                col.w = int((col.ratio / wratio) * wavailable)
            x = col.Right()
                  
        hfixed = 0
        hspace = 0
        hratio = 0.0
        for row in self.rows:
            hspace += self._GetSpace(row)
            if row.height:
                hfixed += row.height
            else:
                hratio += row.ratio
                
        havailable = height - hspace - hfixed
        y = 0
        for row in self.rows:
            row.y = y + self._GetSpace(row)
            if row.height:
                row.h = row.height
            else:
                row.h = int((row.ratio / hratio) * havailable)
            y = row.Bottom()
        
        # update all our control's region
        for c in self.controls:
            # compute width of control
            if c.w:
                woffset = c.w
            else:
                woffset = self.cols[c.c2].Right() - self.cols[c.c1].x

            # compute x pos of control
            if c.attachX == FBAttachType.kFBAttachLeft:
                x = self.cols[c.c1].x
            else:
                x = self.cols[c.c2].Right() - woffset - width
                        
            c.control.RegionOffsetX = x
            c.control.RegionAttachTypeWidth = FBAttachType.kFBAttachNone
            c.control.RegionOffsetWidth = woffset
            
            # compute height of control
            if c.h:
                hoffset = c.h
            else:
                hoffset = self.rows[c.r2].Bottom() - self.rows[c.r1].y
                        
            # compute y pos of control
            if c.attachY == FBAttachType.kFBAttachTop:
                y = self.rows[c.r1].y
            else:
                y = self.rows[c.r2].Bottom() - hoffset - height

            c.control.RegionOffsetY = y
            c.control.RegionAttachTypeHeight = FBAttachType.kFBAttachNone
            c.control.RegionOffsetHeight = hoffset
        
        # replace all our layout
        self.SetAutoRestructure(True)
        self.Restructure(False)
