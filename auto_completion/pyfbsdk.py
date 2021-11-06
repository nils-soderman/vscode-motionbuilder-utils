"""
pyfbsdk
"""
def FBAdd(pResult,pV1,pV2):
    """
    Add two vectors together (<b>pResult</b> = <b>pV1</b> <b>+</b> <b>pV2</b>)

    pResult : Resulting vector. 
    pV1 : 1st vector. 
    pV2 : 2nd vector. 
    """
    pass

def FBAudioFmt_AppendFormat(pFormat,pChannels,pBits,pRate):
    """
    Append the rendering audio format using the specified settings.
    For example, to set audio format to 2 channels, 16 bit, 44100 rate, use the following function: AudioFormat = FBAudioFmt_AppendFormat(0, 2, 16, 44100) Python sample code: 
@code
from pyfbsdk import *

def printFormat( AudioFormat ):
    print 'Audio Render Format: ', AudioFormat
    print 'Audio Channels: ', FBAudioFmt_GetChannelValue( AudioFormat )
    print 'Audio Bit Depth: ', FBAudioFmt_GetBitsValue( AudioFormat )
    print 'Audio Rate: ', FBAudioFmt_GetRateValue( AudioFormat )
    print ''

# Given an AudioFormat, modify the rate from the old rate to 48000 while
# keeping the other settings intact
AudioFormat = FBAudioFmt_GetDefaultFormat()
print 'Old Format:'
printFormat( AudioFormat )

oldrate = FBAudioFmt_GetRateValue( AudioFormat )
AudioFormat = FBAudioFmt_RemoveFormat(AudioFormat, 0, 0, oldrate)
print 'Format after removing Audio Rate:'
printFormat( AudioFormat )

AudioFormat = FBAudioFmt_AppendFormat(AudioFormat, 0, 0, 48000)
print 'New Format after modifying Audio Rate to 48000'
printFormat( AudioFormat )
@endcode

    pFormat : Audio format to use. Set this to 0 if there is no audio format to be appended. 
    pChannels : Number of channels. Valid values are 0, 1, 2, 4, 8. 
    pBits : Bit depth. Valid values are 0, 8, 16, 24, 32. 
    pRate : Audio rate. Valid values are 0, 8000, 11025, 12000, 12500, 16000, 22050, 24000, 25000, 32000, 44100, 48000, 50000, 64000, 88200, 96000, 100000. 
    return : An audio format object with the specified format. 
    """
    pass

def FBAudioFmt_AppendFormat(pFormat,pSrcFormat):
    """
    Append the rendering audio format with another audio format.

    pFormat : Audio format to use. 
    pSrcFormat : Audio format to be appended. 
    return : An audio format object with the specified format. 
    """
    pass

def FBAudioFmt_ConvertBitDepthMode(pBitDepthMode):
    """
    Converts an FBAudioBitDepthMode enum value to its FBAudioFmt object equivalent.

    pBitDepthMode : The bit depth mode enum value. 
    return : The FBAudioFmt object equivalent to the input bit depth mode enum value. 
    """
    pass

def FBAudioFmt_ConvertChannelMode(pChannelMode):
    """
    Converts an FBAudioChannelMode enum value to its FBAudioFmt object equivalent.

    pChannelMode : The channel mode enum value. 
    return : The FBAudioFmt object equivalent to the input channel mode enum value. 
    """
    pass

def FBAudioFmt_ConvertRateMode(pRateMode):
    """
    Converts an FBAudioRateMode enum value to its FBAudioFmt object equivalent.

    pRateMode : The rate mode enum value. 
    return : The FBAudioFmt object equivalent to the input rate mode enum value. 
    """
    pass

def FBAudioFmt_GetBitsValue(pFormat):
    """
    Get the bit depth value of the Audio format object.

    pFormat : Audio format to use. 
    return : Bit depth value as an integer value. 
    """
    pass

def FBAudioFmt_GetBytesValue(pFormat):
    """
    Get the bytes value of the Audio format object.

    pFormat : Audio format to use. 
    return : Bytes value as an integer value. 
    """
    pass

def FBAudioFmt_GetChannelValue(pFormat):
    """
    Get the channel value of the Audio format object.

    pFormat : Audio format to use. 
    return : Channel value as an integer value. 
    """
    pass

def FBAudioFmt_GetDefaultFormat():
    """
    Get default audio format.

    return : An audio format object. 
    """
    pass

def FBAudioFmt_GetRateValue(pFormat):
    """
    Get the rate value of the Audio format object.

    pFormat : Audio format to use. 
    return : Audio rate value as an integer value. 
    """
    pass

def FBAudioFmt_RemoveFormat(pFormat,pChannels,pBits,pRate):
    """
    Remove channels, bit depth, or rate from the specified audio format object.
    Please refer to python example in FBAudioFmt_AppendFormat.

    pFormat : Audio format to use. 
    pChannels : Number of channels to remove. Set this to 0 if you don't want to remove the channel. 
    pBits : Bit depth to remove. Set this to 0 if you don't want to remove bit depth. 
    pRate : Audio rate to remove. Set this to 0 if you don't want to remove audio rate. 
    return : An audio format object without the specified format settings passed in parameter. 
    """
    pass

def FBAudioFmt_RemoveFormat(pFormat,pSrcFormat):
    """
    Remove audio format from another audio format object.

    pFormat : Audio format to use. 
    pSrcFormat : Audio format to remove. 
    return : An audio format object without the specified format settings passed in parameter. 
    """
    pass

def FBAudioFmt_TestFormat(pSrcFormat,pChannels,pBits,pRate):
    """
    Test if the given audio format object contains the channel, bit depth, and rate.

    pSrcFormat : Audio format to test. 
    pChannels : Number of channels to test. 
    pBits : Bit depth to test. 
    pRate : Audio rate to test. 
    return : True if the given audio format object contains the channel, bit depth, and rate. 
    """
    pass

def FBBeginChangeAllModels():
    """
    Call begin change to all models (need to be closed).
    Useful for selection of many models that can trigger many related callbacks)

    """
    pass

def FBClamp(pV,pL,pH):
    """
    Clamp value.

    pV : Value to clamp. 
    pL : Low limit. 
    pH : High limit. 
    return : Clamped value. 
    """
    pass

def FBCreateObject(pGroupName,pEntryName,pName,p3,nth):
    """
    FBCreateObject.

    pGroupName : Set the name of the Group. 
    pEntryName : Set the name of the Entry. 
    pName : Set the name of the Object to create. 
    p3 : Data to pass to object creator function. 
    nth : Set the occurrence of the object to remove.
    """
    pass

def FBDeleteCharacterPinningPreset(pPresetName):
    """
    Deletes a pinning preset from the Character Controls Tool.

    pPresetName : The preset name to delete (not the file path nor the filename of the preset). 
    return : True if the operation is successful, false otherwise. 
    """
    pass

def FBDeleteObjectsByName(pNamePattern,pNameSpace,pGroupName):
    """
    FBDeleteObjectsByName.
    This function will query the system for objects fulfilling a particular name pattern and delete them. specify a namespace preferred, delete all objects with the group name without specified a namespace specified may lead to inconsistent in scene. Wrap multiple calls to FBDeleteObjectsByName() inside pair of FBPreventUIUpdateBegin() / FBPreventUIUpdateEnd() could improve application's performance.

    pNamePattern : if not NULL, indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ). if is NULL or Empty string, * will be used for match all. 
    pNameSpace : if not NULL, the objects must be inside the given namespace. 
    pGroupName : if not NULL, indicate the object group name (type). 
    return : the count of objects found and deleted. 
    """
    pass

def FBDot(pV1,pV2):
    """
    Calculate the dot product of two vectors.

    pV1 : 1st vector. 
    pV2 : 2nd vector. 
    return : Dot product. 
    """
    pass

def FBEndChangeAllModels():
    """
    Call end change to all models (should be first open).

    """
    pass

def FBFindModelByLabelName(pModelLabelName):
    """
    Find a model in the scene by its label name.
    Searches the scene for a model, based on the model's label name. Label name is 'NameSpaceName:ObjectName'. also known as 'PrefixName::ObjectName' Full name is 'GroupName::NameSpaceName:ObjectName'.

    pModelLabelName : LabelName of model to search for. Specify it with schema like "NameSpaceName:ObjectName",or "ObjectName" if no NameSpaceName. 
    return : A handle onto the model with Label name matching, returns NULL if no model was found by the search.
    """
    pass

def FBFindModelByUniqueColorId(pColor,pSubItemIndex):
    """
    Find a model in the scene by its unique color id.
    A model could have a single unique ColorID, but SDK plugin user could request additional ColorID per model to support multi sub items picking. see FBModel::SetAdditionalUniqueColorIDCount().

    pColor : Color channel values are in range of [0,1] with precision 1.0/255  
    pSubItemIndex : Pass out SubImtem index value if not null. In pyfbsdk no such parameter. 
    return : A handle onto the model with unique color id matching, returns NULL if no model was found by the search. In pyfbsdk return tuple [model, subItemIndex] 
    """
    pass

def FBFindObjectByFullName(pObjectFullName):
    """
    FBFindObjectByFullName.
    This function will query the system for an object with its FullName matching. Full name is 'GroupName::NameSpaceName:ObjectName'. Label name is 'NameSpaceName:ObjectName'. also known as 'PrefixName::ObjectName'

    pObjectFullName : Full Name of object to search for. Specify it with schema like "GroupName::NameSpaceName:ObjectName",or "GroupName::ObjectName" if no NameSpaceName. 
    return : A handle onto the object with Full name matching pObjectFullName, returns NULL if no object was found by the search. 
    """
    pass

def FBFindObjectsByName(pNamePattern,pList,pIncludeNamespace,pModelsOnly):
    """
    FBFindObjectsByName.
    This function will query the system for objects fulfilling a particular name pattern

    pNamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ) 
    pList : List that contains the objects 
    pIncludeNamespace : Does the search use the complete name (with namespace) 
    pModelsOnly : Is the search on models or all types of objects
    """
    pass

def FBGetActorMarkerSetVisibility():
    """
    Queries visibility of the marker set of the current actor.

    return : True if the marker set of the current actor are visible, or false if it is hidden. 
    """
    pass

def FBGetCharacterExternalSolverCount():
    """
    Get character external solver count.

    return : Number of external character solver available. 
    """
    pass

def FBGetCharacterExternalSolverIndex(pName):
    """
    Get character external solver index.

    pName : Name of external solver. 
    return : Index of external solver specified at the provided name. 
    """
    pass

def FBGetCharacterExternalSolverName(pIndex):
    """
    Get character external solver name.

    pIndex : Index of external solver. 
    return : Name of the external solver specified at the provided index. 
    """
    pass

def FBGetCharacterFingerTipsVisibility():
    """
    Queries visibility of the finger-tips of the current character.

    return : True if finger-tips of the current character are visible, or false if they are hidden. 
    """
    pass

def FBGetCharacterFloorContactsVisibility():
    """
    Queries visibility of the floor contacts of the current character.

    return : True if floor contacts of the current character are visible, or false if they are hidden. 
    """
    pass

def FBGetCharactersKeyingMode():
    """
    return Character Manipulation/Keying Mode

    return : Keying Mode 
    """
    pass

def FBGetConstantKeyReducerThresholdValue(pThresholdType):
    """
    Return a specific threshold value used by the Constant Key Reducer filter.

    pThresholdType : The threshold type to retrieve its value. 
    return : The threshold value. 
    """
    pass

def FBGetContinuousRotation(pROut,pR0,pR1):
    """
    Get a continuous rotation in Euler space.
    This routine will help to avoid gimble locks due to interpolation.

    pROut : Successful continuous rotation (gimble-lock free). 
    pR0 : Suggested next rotation. 
    pR1 : Previous rotation. 
    """
    pass

def FBGetDisplayInfo():
    """
    Get the displays evaluation information structure.
    This function can be used in order to call real-time functions based on the current display evalution state.

    return : The display evalution structure. 
    """
    pass

def FBGetEffectorBodyPart(pEffectorId):
    """
    return BodyPart ID from Effector.

    pEffectorId : Effector ID. 
    return : ID of the BodyPart the effector is in. 
    """
    pass

def FBGetEvaluationTaskCycle():
    """
    Get evaluation task cycle.

    """
    pass

def FBGetGlobalMatrix(pMatrix,pMatrixParent,pLocalMatrix):
    """
    Get global matrix from parent and child matrices.
    From an input referential, this function will calculate the global matrix corresponding to the input local matrix (which is with respect to the parent matrix).

    pMatrix : Calculated local matrix. 
    pMatrixParent : Parent matrix. 
    pLocalMatrix : Local matrix. 
    """
    pass

def FBGetLastSelectedModel():
    """
    Get the last selected model, which is the one having the manipulator in the viewer.

    return : The last selected model or nullptr (C++) or None (Python) if no model is selected. 
    """
    pass

def FBGetLocalMatrix(pMatrix,pMatrixParent,pMatrixChild):
    """
    Get local matrix from parent and child matrices.
    Will calculate the local matrix from two global matrices. The resulting matrix will be a local matrix containing the local transformations to go from the parent referentialto the child referential.

    pMatrix : Calculated local matrix. 
    pMatrixParent : Parent matrix (new base referential). 
    pMatrixChild : Child matrix. 
    """
    pass

def FBGetMainThreadTaskCycle():
    """
    Get root task cycle.

    """
    pass

def FBGetMainWindow():
    """
    Return the MotionBuilder main window.
    The following Python snippet shows how to get the MotionBuilder main window. 
@code
from PySide2 import QtWidgets
import shiboken2

def getMainWindow():
    ptr = FBGetMainWindow()
    if ptr is not None:
        return shiboken2.wrapInstance(ptr, QtWidgets.QWidget)

mainWindow = getMainWindow()
if mainWindow is not None:
    print( mainWindow.windowTitle() )
else:
    print( 'MotionBuilder main window not found!' )
@endcode

    return : The MotionBuilder main window. 
    """
    pass

def FBGetMultiLangText(pContext,pKey,pFlagReturnKey):
    """
    Name lookup in the context of an object.
    Most application objects have an internal name which differs from the name shown by the GUI. This will often be the case for the names of an object's properties.The way that support for multiple languages has been implemented is using conversion tables that will map the internal name to a localized name. Since the same internal name might mean different things for different objects, we can provide a context to help the lookup process.In this case, the context is a class object instance. When the lookup fails within a context, we sucessively try a lookup using the parent classes in the object hierarchy.It is important to note that for given property, it only knows about its internal name. The localized name is not attached to the property object itself as it resides elsewhere, in a lookup table. This is also the case for any other application object.The lookup table used to find the localized, or GUI name, of an object is dependent on the current language used. This information is available via the class FBMultiLangManager, which can indicate which language are availables and provides methode to query and change the current language.Python sample code: 
@code
from pyfbsdk import *

# Let's pick the first camera present in the system.
lCamera = FBSystem().Cameras[0]

# We know that cameras have a property named 'LockMode'.
lPropInternalName = lCamera.PropertyList.Find( 'LockMode' )
if lPropInternalName:
    print 'Actual property name, as defined internally: '%s'' % lPropInternalName.GetName()
    print 'Property name as shown by the GUI: '%s'' % FBGetMultiLangText( lCamera, lPropInternalName.GetName())

    lPropLocalizedName = lCamera.PropertyList.Find( FBGetMultiLangText( lCamera, lPropInternalName.GetName()))
    if lPropLocalizedName and lPropInternalName.GetName() == lPropLocalizedName.GetName():
        print 'Found the same property using both the internal (%s) and localized name (%s).' % (
            lPropLocalizedName.GetName(),
            FBGetMultiLangText( lCamera, lPropInternalName.GetName()))
@endcode

C++ sample code: 
@code
// Let's pick the first camera present in the system.
FBCamera* lCamera = FBSystem().Cameras[0];

// We know that cameras have a property named 'LockMode'.
FBProperty* lPropInternalName = lCamera->PropertyList.Find( 'LockMode' );
if( lPropInternalName )
{
    FBTrace( 'Actual property name, as defined internally: '%s'\n', lPropInternalName->GetName());
    FBTrace( 'Property name as shown by the GUI: '%s'\n', FBGetMultiLangText( lCamera, lPropInternalName->GetName()));

    FBProperty* lPropLocalizedName = lCamera->PropertyList.Find( FBGetMultiLangText( lCamera, lPropInternalName->GetName()));
    if( lPropLocalizedName && stricmp( lPropInternalName->GetName(), lPropLocalizedName->GetName()) == 0 )
    {
        FBTrace( 'Found the same property using both the internal (%s) and localized name (%s).\n',
            lPropLocalizedName->GetName(),
            FBGetMultiLangText( lCamera, lPropInternalName->GetName()));
    }
}
@endcode

    pContext : Object which dictates the context of the lookup. 
    pKey : String to look up. 
    pFlagReturnKey : Should the lookup fail, will return the key instead of an empty string. 
    return : The corresponding string if the lookup was succesfull. If not will return an empty string if pFlagReturnKey was false. Otherwise will return the key string. 
    """
    pass

def FBGetMultiLangText(pContext,pKey,pFlagReturnKey):
    """
    Name lookup in a user defined context context.
    This version of the function is a little less useful as the context string, if not empty, will usually refer to internal class names of objects which is not easily available to the outside world.As a general rule, an SDK object whose class is 'FBObject' will be wrapping an internal object of class 'KObject'. For example an 'FBCamera' is a wrapper around a 'KCamera' object. Similarily an 'FBConstraint' wll wrap a 'KConstraint'. This pattern is not universal and may differ at times, so it will not always be applicable. There are also cases where an 'FB' objects has no corresponding 'K' object, such as in the case of an 'FBSystem' object.On lookup there are potentially two searches made: a first one, using the context if one was provided. Should the first search fail, a second search will be done without using the context.Again the lookup result is dependant on the current language selected, as indicated by the class FBMultiLangManager.The following sample code shows 2 cases that do not use context, and 2 cases that are using a context which are internal class names.Python sample code: 
@code
from pyfbsdk import *

print FBGetMultiLangText( '', 'CharacterExtension' )            # Will return 'Character Extension'.
print FBGetMultiLangText( '', 'TranslationMax' )                # Will return 'Max Freedom'.
print FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ) # Will return 'Parent/Child'.
print FBGetMultiLangText( 'KCamera', 'FieldOfView' )            # Will return 'Field Of View'.
@endcode

C++ sample code: 
@code
// Will return 'Character Extension'.
FBTrace( '%s\n', FBGetMultiLangText( '', 'CharacterExtension' ));

// Will return 'Max Freedom'.
FBTrace( '%s\n', FBGetMultiLangText( '', 'TranslationMax' ));

// Will return 'Parent/Child'.
FBTrace( '%s\n', FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ));

// Will return 'Field Of View'.
FBTrace( '%s\n', FBGetMultiLangText( 'KCamera', 'FieldOfView' ));
@endcode

    pContext : String which dictates the context of the lookup. 
    pKey : String to look up. 
    pFlagReturnKey : Should the lookup fail, will return the key instead of an empty string. 
    return : The corresponding string if the lookup was succesfull. If not will return an empty string if pFlagReturnKey was false. Otherwise will return the key string. 
    """
    pass

def FBGetRenderingTaskCycle():
    """
    Get rendering task cycle.

    """
    pass

def FBGetSelectedModels(pList,pParent,pSelected,pSortBySelectOrder):
    """
    Find all models that are selected (if pSelected is true) Searches recursively from a root model for models that are selected, and adds them to a list of models.

    pList : List to add found models to. 
    pParent : Root model to look from (default=NULL(root)). 
    pSelected : true to find selected models, false to find unselected models(default=true). 
    pSortBySelectOrder : true to sort the result by selection order, first selected model in the first part of the list; false to sort the result by scene graph order
    """
    pass

def FBInterpolateRotation(pROut,pR0,pR1,pU):
    """
    Interpolate a rotation in Euler space.

    pROut : Resulting, interpolated rotation. 
    pR0 : 1st rotation. 
    pR1 : 2nd rotation. 
    pU : Interpolation ratio. 
    """
    pass

def FBInterpolateRotation(pQOut,pQ0,pQ1,pU):
    """
    Interpolate a rotation in Quaternion.

    pQOut : Resulting, interpolated rotation. 
    pQ0 : 1st rotation. 
    pQ1 : 2nd rotation. 
    pU : Interpolation ratio. 
    """
    pass

def FBLength(pV):
    """
    Get the length of a vector.

    pV : Vector to calculate length for. 
    return : Length of vector <b>pV</b>. 
    """
    pass

def FBLength(pV):
    """
    Get the length of a vertex (from origin)

    pV : Vertex for which length is to be measured. 
    return : Length of vertex (from origin). 
    """
    pass

def FBLoadCharacterPinningPreset(pPresetName):
    """
    Loads a pinning preset in the Character Controls Tool.

    pPresetName : The preset name to load (not the file path nor the filename of the preset). 
    return : True if the operation is successful, false otherwise. 
    """
    pass

def FBLoadFbxPrimitivesModel(pModelName):
    """
    Load a model.

    pModelName : Name of primitive model to load. 
    return : A handle onto the model that was loaded, returns NULL if no model was found. 
    """
    pass

def FBMatrixInverse(pMatrix,pSrc):
    """
    Invert a matrix.

    pMatrix : Calculated inverse matrix. 
    pSrc : Source matrix to invert. 
    """
    pass

def FBMatrixMult(pMatrix,pA,pB):
    """
    Multiply two matrices.

    pMatrix : Calculated resulting matrix. 
    pA : 1st matrix. 
    pB : 2nd matrix. 
    """
    pass

def FBMatrixOrthogonalize(pMatrix):
    """
    Make sure that rotation vectors are orthogonal and normalized (fast way for removing scaling from matrix)

    pMatrix : Rotation Matrix to Orthogonalize. 
    """
    pass

def FBMatrixToQuaternion(pQuaternion,pMatrix):
    """
    Get a quaternion from a matrix (potential ).

    pQuaternion : Calculated quaternion. 
    pMatrix : Input matrix. 
    """
    pass

def FBMatrixToRotation(pVector,pMatrix,pRotationOrder):
    """
    Obtain rotation vector from a matrix.

    pVector : Extracted rotation vector, ordered the same way as the rotation order specified by pRotationOrder. 
    pMatrix : Input matrix. 
    pRotationOrder : Rotation order. 
    """
    pass

def FBMatrixToRotationWithPrecision(pVector,pMatrix,pRotationOrder,pPrecision):
    """
    Obtain rotation vector from a matrix.

    pVector : Extracted rotation vector. 
    pMatrix : Input matrix. 
    pRotationOrder : Rotation Order. 
    pPrecision : Indicate the precision level (pow(10.0, -pPrecision)) used when calculating the threshold value for gimble lock. 
    """
    pass

def FBMatrixToScaling(pVector,pMatrix):
    """
    Obtain scaling vector from a matrix.

    pVector : Extracted scaling vector. 
    pMatrix : Input matrix. 
    """
    pass

def FBMatrixToTQS(pTVector,pQuaternion,pSVector,pMatrix):
    """
    Obtain translation vector, rotation quaternion, and scaling vector from a matrix.

    pTVector : Extracted translation vector. 
    pQuaternion : Extracted rotation quaternion. 
    pSVector : Extracted scaling vector. 
    pMatrix : Input matrix. 
    """
    pass

def FBMatrixToTRS(pTVector,pRVector,pSVector,pMatrix):
    """
    Obtain translation, rotation, and scaling vectors from a matrix.

    pTVector : Extracted translation vector. 
    pRVector : Extracted rotation vector. 
    pSVector : Extracted scaling vector. 
    pMatrix : Input matrix. 
    """
    pass

def FBMatrixToTranslation(pVector,pMatrix):
    """
    Obtain translation vector from a matrix.

    pVector : Extracted translation vector. 
    pMatrix : Input matrix. 
    """
    pass

def FBMatrixTranspose(pMatrix,pSrc):
    """
    Transpose a matrix.

    pMatrix : Calculated transpose matrix. 
    pSrc : Source matrix to transpose. 
    """
    pass

def FBMergeTransactionBegin():
    """
    Call to begin the transaction for merging multiple files.
    Useful to consecutively merge multiple files into scene.

    """
    pass

def FBMergeTransactionEnd():
    """
    Call to end the merge transaction.

    """
    pass

def FBMergeTransactionFileRefEditBegin():
    """
    Call to begin the transaction for merging multiple files and applying File Reference edit at the same time.
    Useful to consecutively merge multiple files into scene with FileRef edit operation in between.

    """
    pass

def FBMergeTransactionFileRefEditEnd():
    """
    Call to end merge transaction with File Reference edit.

    """
    pass

def FBMergeTransactionFileRefEditIsOn():
    """
    Call to tell if system is during File Reference Edit Merge transaction.

    """
    pass

def FBMergeTransactionIsOn():
    """
    Call to tell if system is during Merge transaction.

    """
    pass

def FBMessageBox(pBoxTitle,pMessage,pButton1Str,pButton2Str,pButton3Str,pDefaultButton,pScrolledMessage):
    """
    Dialog popup box.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pButton1Str : String for first button (Cannot be NULL). 
    pButton2Str : String for second button (NULL will not create a button). 
    pButton3Str : String for third button (NULL will not create a button). 
    pDefaultButton : Indicates the default (pre-selected) button (default is 0). 
    pScrolledMessage : Scroll message (default is 0). 
    return : The number of the button selected.
    """
    pass

def FBModelTransactionBegin():
    """
    FBModelTransactionBegin.
    This set of functions speeds up the process of batch operations on models.

    """
    pass

def FBModelTransactionEnd():
    """
    FBModelTransactionEnd.
    This set of functions speeds up the process of batch operations on models.

    """
    pass

def FBMult(pResult,pV1,pV2):
    """
    Multiply <b>pV2</b> from <b>pV1</b> (<b>pResult</b> = <b>pV1</b> <b>*</b> <b>pV2</b>)

    pResult : Resulting vector. 
    pV1 : 1st vector. 
    pV2 : 2nd vector. 
    """
    pass

def FBMult(pResult,pV1,pV2):
    """
    Calculate the cross product of two vectors.

    pResult : Resulting vector. 
    pV1 : 1st vector. 
    pV2 : 2nd vector. 
    """
    pass

def FBMult(pResult,pM,pV):
    """
    Calculate the cross product of a Matrix and Scale Vector.

    pResult : Resulting Matrix. 
    pM : Matrix. 
    pV : vector. 
    """
    pass

def FBObjectGetGlobalUniqueId():
    """
    Get the global static object unique ID counter.
    Each new created object will be assigned this global unique ID. Object.UniqueID = GlobalUniqueID++

    """
    pass

def FBObjectGetLivingCount():
    """
    Get current total living object count.

    """
    pass

def FBObjectLifeLogEnable(pEnable):
    """
    Enable object creation / deletion logging.
    Default logging if off This logging may hurt performance slightly. use it only for debug purpose.

    pEnable : true to enable logging. 
    """
    pass

def FBObjectPrintLivings(pStartUniqueId):
    """
    Print those living objects created when logging is enabled.

    pStartUniqueId : Any living object has been logged and with its uniqueId no less than pStartUniqueId will be printed out. 
    """
    pass

def FBObject_GetEntryCount(pGroupIndex):
    """
    pGroupIndex : int
    """
    pass

def FBObject_GetEntryDLLName(pGroupIndex,pIndex,nth):
    """
    pGroupIndex : int
    pIndex : int
    nth : int
    """
    pass

def FBObject_GetEntryDescription(pGroupIndex,pIndex,nth):
    """
    pGroupIndex : int
    pIndex : int
    nth : int
    """
    pass

def FBObject_GetEntryName(pGroupIndex,pIndex):
    """
    pGroupIndex : int
    pIndex : int
    """
    pass

def FBObject_GetGroupCount():
    """
    A set of functions to query the registration table.

    """
    pass

def FBObject_GetGroupName(pGroupIndex):
    """
    pGroupIndex : int
    """
    pass

def FBObject_GetIconName(pGroupIndex,pIndex,nth):
    """
    pGroupIndex : int
    pIndex : int
    nth : int
    """
    pass

def FBObject_GetMultiplicity(pGroupIndex,pIndex,nth):
    """
    pGroupIndex : int
    pIndex : int
    nth : int
    """
    pass

def FBPopNormalTool(pToolName,pSetFocus):
    """
    This function is used to bring up a specific tool in the GUI.

    pToolName : The name of the tool as shown in the Open Reality menu. 
    pSetFocus : Indicate if the tool will have the focus. 
    return : If the tool was brought up successfully. 
    """
    pass

def FBPreventUIUpdateBegin():
    """
    Call to prevent UI updates when creating/deleting/renaming objects.
    Useful to speed up script operations. Previously, FBMergeTransactionBegin()/ FBMergeTransactionEnd() could be used to do this kind of optimization, even if no merge operations were done. However, using FBMergeTransactionBegin()/ FBMergeTransactionEnd() with non-merge operation could lead to issues, like objects with invalid namespaces. FBPreventUIUpdateBegin()/FBPreventUIUpdateEnd() fix this issue, while giving the same speed increase.

    """
    pass

def FBPreventUIUpdateEnd():
    """
    Call to end blocking the UI updates.

    """
    pass

def FBPreventUIUpdateIsOn():
    """
    Call to tell if UI updates are blocked.

    """
    pass

def FBQAdd(pResult,pQ1,pQ2):
    """
    Add two quaternions together (<b>pResult</b> = <b>pQ1</b> <b>+</b> <b>pQ2</b>)

    pResult : Resulting quaternion. 
    pQ1 : 1st quaternion. 
    pQ2 : 2nd quaternion. 
    """
    pass

def FBQDot(pQ1,pQ2):
    """
    Calculate the dot product of two quaternions.

    pQ1 : 1st quaternion. 
    pQ2 : 2nd quaternion. 
    return : Dot product. 
    """
    pass

def FBQLength(pQ):
    """
    Get the length of a quaternion.

    pQ : Quaternion to calculate length for. 
    return : Length of quaternion <b>pQ</b>. 
    """
    pass

def FBQMult(pResult,pQ1,pQ2):
    """
    Multiply <b>pQ2</b> from <b>pQ1</b> (<b>pResult</b> = <b>pQ1</b> <b>*</b> <b>pQ2</b>)

    pResult : Resulting quaternion. 
    pQ1 : 1st quaternion. 
    pQ2 : 2nd quaternion. 
    """
    pass

def FBQMult(pResult,pQ1,pQ2):
    """
    Calculate the cross product of two quaternions.

    pResult : Resulting quaternion. 
    pQ1 : 1st quaternion. 
    pQ2 : 2nd quaternion. 
    """
    pass

def FBQSub(pResult,pQ1,pQ2):
    """
    Subtract <b>pQ2</b> from <b>pQ1</b> (<b>pResult</b> = <b>pQ1</b> <b>-</b> <b>pQ2</b>)

    pResult : Resulting quaternion. 
    pQ1 : 1st quaternion. 
    pQ2 : 2nd quaternion. 
    """
    pass

def FBQuaternionToMatrix(pMatrix,pQuaternion):
    """
    Get a rotation matrix from a quaternion vector.

    pMatrix : Calculated rotation matrix. 
    pQuaternion : Input quaternion. 
    """
    pass

def FBQuaternionToRotation(pVector,pQuaternion,pRotationOrder):
    """
    Get a rotation vector from a quaternion vector.

    pVector : Calculated rotation vector, ordered the same way as the rotation order specified by pRotationOrder. 
    pQuaternion : Input quaternion. 
    pRotationOrder : Rotation order. 
    """
    pass

def FBQuaternionToRotationWithPrecision(pVector,pQuaternion,pRotationOrder,pPrecision):
    """
    Get a rotation vector from a quaternion vector.

    pVector : Calculated rotation vector. 
    pQuaternion : Input quaternion. 
    pRotationOrder : Rotation order of the rotation vector. 
    pPrecision : Indicate the precision level (pow(10.0, -pPrecision)) used when calculating the threshold value for gimble lock. 
    """
    pass

def FBRotationToMatrix(pMatrix,pVector,pRotationOrder):
    """
    Convert a rotation vector to a matrix.

    pMatrix : Calculated resulting matrix. 
    pVector : Rotation vector, ordered the same way as the rotation order specified by pRotationOrder. 
    pRotationOrder : Rotation order. 
    """
    pass

def FBRotationToQuaternion(pQuaternion,pVector,pRotationOrder):
    """
    Get a quaternion from a rotation vector.

    pQuaternion : Calculated quaternion. 
    pVector : Input rotation vector, ordered the same way as the rotation order specified by pRotationOrder. 
    pRotationOrder : Rotation order. 
    """
    pass

def FBSaveCharacterPinningPreset(pPresetName,pAllowOverwriting):
    """
    Saves a pinning preset from the current pinning values in the Character Controls Tool.

    pPresetName : The preset name to save (not the file path nor the filename of the preset). 
    pAllowOverwriting : True to allow overwriting an existing preset having the same name as the one provided, false otherwise. 
    return : True if the operation is successful, false otherwise. 
    """
    pass

def FBScalingToMatrix(pMatrix,pVector):
    """
    Convert a scaling vector to a matrix.

    pMatrix : Calculated resulting matrix. 
    pVector : Scaling vector. 
    """
    pass

def FBSchedulingDependencyOutput(pEnable):
    """
    Debug function for MT dependency debug.
    When enabled log file will be created and updated each time MultiThreaded scheduling is happening (scene rebuild)

    pEnable : ON/OFF switch. This is not stored in config (should be changed only for debug purpose, because slow down rebuild process ) 
    """
    pass

def FBSetActorMarkerSetVisibility(pShow):
    """
    Sets visibility of the marker set of the current actor.

    pShow : Specifies if the market of the current actor should be visible. 
    return : True if the operation is successful, false otherwise. 
    """
    pass

def FBSetCharacterFingerTipsVisibility(pShow):
    """
    Sets visibility of the finger-tips of the current character.

    pShow : Specifies if finger-tips of the current character should be visible. 
    """
    pass

def FBSetCharacterFloorContactsVisibility(pShow):
    """
    Sets visibility of the floor contacts of the current character.

    pShow : Specifies if floor contacts of the current character should be visible. 
    """
    pass

def FBSetConstantKeyReducerThresholdValue(pThresholdType,pValue):
    """
    Set a specific threshold value used by the Constant Key Reducer filter.

    pThresholdType : The threshold type to set its value. 
    pValue : The new threshold value to set. 
    """
    pass

def FBSetLastSelectedModel(pModel):
    """
    Set the given model as the last one selected, so the manipulator in the viewer will then be on that particular model.
    If the model is not selected, it will also be selected.

    pModel : Model that will be flagged as the last selected model. 
    """
    pass

def FBSleep(MilliSeconds):
    """
    Sleep function Puts system to sleep for specified time.

    MilliSeconds : Time to sleep for.
    """
    pass

def FBSub(pResult,pV1,pV2):
    """
    Subtract <b>pV2</b> from <b>pV1</b> (<b>pResult</b> = <b>pV1</b> <b>-</b> <b>pV2</b>)

    pResult : Resulting vector. 
    pV1 : 1st vector. 
    pV2 : 2nd vector. 
    """
    pass

def FBTQSToMatrix(pMatrix,pTVector,pQuaternion,pSVector):
    """
    Convert translation vector, rotation quaternion, and scaling vector to a matrix.

    pMatrix : Calculated resulting matrix. 
    pTVector : Translation vector. 
    pQuaternion : Rotation quaternion. 
    pSVector : Scaling vector. 
    """
    pass

def FBTRSToMatrix(pMatrix,pTVector,pRVector,pSVector):
    """
    Convert translation, rotation, and scaling vectors to a matrix.

    pMatrix : Calculated resulting matrix. 
    pTVector : Translation vector. 
    pRVector : Rotation vector. 
    pSVector : Scaling vector. 
    """
    pass

def FBTrace(pFormatString,p1):
    """
    This function prints useful debugging strings in the console with kFBNORMAL_TRACE output detailed level.

    pFormatString : A printf-style format string, to use the following arguments in the list. 
    p1 : ...
    """
    pass

def FBTraceGetLevel():
    """
    Get Global Trace Detailed Level which affects all the output targets.

    return : Current global trace detailed level. 
    """
    pass

def FBTraceSetLevel(pNewLevel):
    """
    Set Global Trace Detailed Level which affects all the output targets.

    pNewLevel : Any trace message with detailed level higher than this new level will be ignored, valid value range [kFBNO_TRACE, kFBALL_TRACE] 
    """
    pass

def FBTraceWithLevel(pLevel,pFormatString,p2):
    """
    This function prints useful debugging strings in the console.

    pLevel : to control trace output detailed level, valid value range [kFBCRITICAL_TRACE, kFBALL_TRACE] 
    pFormatString : A printf-style format string, to use the following arguments in the list. 
    p2 : ...
    """
    pass

def FBTranslationToMatrix(pMatrix,pVector):
    """
    Convert a translation vector to a matrix.

    pMatrix : Calculated resulting matrix. 
    pVector : Translation vector. 
    """
    pass

def FBVectorMatrixMult(pOutVector,pMatrix,pVector):
    """
    Multiply a vector by a matrix.

    pOutVector : Resulting vector. 
    pMatrix : Matrix to affect the vector with. 
    pVector : Source vector. 
    """
    pass

def FBVertexMatrixMult(pOutVertex,pMatrix,pVertex):
    """
    Multiply a vertex by a matrix.

    pOutVertex : Resulting vertex. 
    pMatrix : Matrix to affect the vertex with. 
    pVertex : Source vertex. 
    """
    pass

def FBMessageBoxWithCheck(pBoxTitle,pMessage,pButton1Str,pButton2Str,pButton3Str,pCheckBoxStr,pCheckBoxValue,pDefaultButton,pScrolledMessage):
    """
    Dialog popup box with 'don't show again' option.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button. This dialog also gives the user the option of never showing the dialog again.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pButton1Str : String for first button (Cannot be None). 
    pButton2Str : String for second button (None will not create a button). 
    pButton3Str : String for third button (None will not create a button). 
    pCheckBoxStr : Check box string (Cannot be None). 
    pCheckBoxValue : Check box value. 
    pDefaultButton : Indicates the default (pre-selected) button (default is 0). 
    pScrolledMessage : Scroll message (default is False). 
    return : A tuple containing the index of the button selected and the boolean value of the check box. 
    """
    pass

def FBMessageBoxGetUserValue(pBoxTitle,pMessage,pValue,pValueType,pButton1Str,pButton2Str,pButton3Str,pDefaultButton):
    """
    Dialog popup box to get user input.
    Opens a message box, with up to three buttons, asking the user to enter data. The type of data to be entered is specified by the <b>pValue</b> and <b>pValueType</b> parameters.

    pBoxTitle : Title of message box. 
    pMessage : Message to place in box. 
    pValue : Value entered by user (must correspond with pValueType). 
    pValueType : Type of pointer specified in pValue. 
    pButton1Str : String for first button (Cannot be None). 
    pButton2Str : String for second button (None will not create a button). 
    pButton3Str : String for third button (None will not create a button). 
    pDefaultButton : Indicates the default (pre-selected) button(default=0). 
    return : A tuple containing the index of the button selected and the value entered by the user, if any. 
    """
    pass

def FBConnect(pSrc,pDst,pConnectionType):
    """
    Request the connection two FBPlug objects.

    pSrc : Source plug. 
    pDst : Destination plug. 
    pConnectionType : Type of connection, taken from FBConnectionType. 
    return : A boolean indicating success (True) or failure (False). 
    """
    pass

def FBDisconnect(pSrc,pDst):
    """
    Connect two FBPlug objects.

    pSrc : Source plug. 
    pDst : Destination plug. 
    return : A boolean indicating success (True) or failure (False). 
    """
    pass

class object:
    """
    object
    """
    pass

class Enumeration (object):
    """
    Enumeration mapping.     
    The way our C++ enumerations have been exposed in python is to use the enumerated type name as a class name, and having each of the possible enum values as a separate data member. For example, with FBTimeMode's enum named 'kFBTimeModePAL', you would instead use FBTimeMode.kFBTimeModePAL in Python. We have exposed all the enumerated types of the Open Reality SDK from C++ to Python, even those that may not be relevant.     
    """
    pass

class FBAddRegionParam (object):
    """
    This class provide a placeholder to put values necessary to create a Region with FBLayout.AddRegion.     
    Each region components: X, Y, Width and Height needs its own FBAddRegionParam. ex: x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,'') y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,'') w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,'') h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,'') mainLyt.AddRegion('main','main', x, y, w, h)     
    """
    def FBAddRegionParam(self,pPos,pType,pRelative,pMult):
        """
        Initialize a region params.

        pPos : Offset in pixel according depending on the use of FBAddRegionParam (X, Y, W or H) 
        pType : Type of Attachment. 
        pRelative : Name of Region to attach relative to. 
        pMult : Multiplier of relative value. 
        """
        pass

    mPos=property(doc="<b>Read Property:</b> Offset in pixel according depending on the use of FBAddRegionParam (X, Y, W or H).         ")
    mType=property(doc="<b>Read Property:</b> Type of Attachment.         ")
    mRelative=property(doc="<b>Read Property:</b> Name of Region to attach relative to.         ")
    mMult=property(doc="<b>Read Property:</b> Multiplier of relative value.         ")
    pass

class FBAudioRenderOptions (object):
    """
    Audio Render Options structure.     
     Contain options to control how the audio rendering will occur. See sample: AudioRendering.py.     
    """
    def FBAudioRenderOptions(self):
        """
        Constructor.

        """
        pass

    BitDepthMode=property(doc="<b>Property:</b> Bit depth for one sample of audio. 8, 16 and 24 bits available for audio render, 16 bits default.          ")
    ChannelMode=property(doc="<b>Property:</b> Audio render channel number, 1 for Mono(left channel right channel render mixed to one channel), 2 for Stereo(left channel right channel render separately).          ")
    OutputFileName=property(doc="<b>Property:</b> Audio Render destination file.          ")
    RateMode=property(doc="<b>Property:</b> Rate mode for number of samples per second. 44100 hz default,8000, 11025,12000,16000,22050,24000,32000,44100,48000,64000,88200,96000 available for audio render.          ")
    TimeSpan=property(doc="<b>Property:</b> Start and stop selection time to render.          ")
    pass

class FBBatchOptions (object):
    """
    Option parameters for the batch process.     
         
    """
    def FBBatchOptions(self):
        """
        Constructor.

        """
        pass

    InputFileFormat=property(doc="<b>Read Write Property:</b> File format of the input files.         ")
    OutputFileFormat=property(doc="<b>Read Write Property:</b> File format of the output files.         ")
    ProcessType=property(doc="<b>Read Write Property:</b> What process should be done? Load, Save or Both.         ")
    InputDirectory=property(doc="<b>Read Write Property:</b> The directory containning the input files.         ")
    OutputDirectory=property(doc="<b>Read Write Property:</b> The directory containning the output files.         ")
    SkeletonFile=property(doc="<b>Read Write Property:</b> The Skeleton file (for Acclaim AMC files).         ")
    Character=property(doc="<b>Read Write Property:</b> The character to receive the animation.         ")
    StartAnimationAtZero=property(doc="<b>Read Write Property:</b> Set the time of all loaded files to 0.         ")
    FrameAnimation=property(doc="<b>Read Write Property:</b> Set timeline start and end time to corespond with the start and end of animation.         ")
    OverwriteScaling=property(doc="<b>Read Write Property:</b> Set the scaling to a default setting of 1.0.         ")
    KeepDummyBones=property(doc="<b>Read Write Property:</b> To keep dummy bones.         ")
    WriteRate=property(doc="<b>Read Write Property:</b> Write frame rate in Acclaim AMC files.         ")
    WriteTranslation=property(doc="<b>Read Write Property:</b> Write translation animation data included with Acclaim AMC files.         ")
    PlotToCharacter=property(doc="<b>Read Write Property:</b> To plot the animation on the character.         ")
    PlotToControlSet=property(doc="<b>Read Write Property:</b> To plot the animation on the control set.         ")
    UseSingleTake=property(doc="<b>Read Write Property:</b> Use only one take to convert all files.         ")
    UseBatchSuffix=property(doc="<b>Read Write Property:</b> Add a batch suffix to the name of the files.         ")
    KeepCharacterConstraint=property(doc="<b>Read Write Property:</b> To keep the character constaint when saving.         ")
    OnTakeExistAction=property(doc="<b>Read Write Property:</b> Action to perform when a take already exist while in a batch process.         ")
    OnContainsBatchTakesAction=property(doc="<b>Read Write Property:</b> Action to perform when a scene already contains batch takes while in a batch process.         ")
    pass

class FBCallback (object):
    """
    This class is used for the internal callback framework and is not meant to be used by clients.     
        
    """
    Wrapper=property(doc="<b>Read Property:</b> Pyfbsdk Wrapper that is the owner of the callback.         ")
    EventType=property(doc="<b>Read Property:</b> Event type to which this callback is connected.         ")
    Callback=property(doc="<b>Read Property:</b> Python callback that will called when the FBCallback is executed.         ")
    pass

class FBCharacterPoseOptions (object):
    """
    Stores options for operations on poses.     
     This class exposes the object used to store the options for operations on object poses. Before using a FBCharacterPoseOptions, you need to specify the various members of the object. Here are the default values of a FBCharacterPoseOptions object: mCharacterPoseKeyingMode = kFBCharacterPoseKeyingModeFullBody mModelToMatch = NULL mMirrorPlaneType = kFBMirrorPlaneTypeAuto mMirrorPlaneEquation = 1.0, 0.0, 0.0, 0.0 mMirrorPlaneTiltAngle = 90.0 mMirrorPlanePanAngle = 0.0 Flag = kFBCharacterPoseNoFlag You need to change at least the Flag value by using SetFlag() to set how the pose will be pasted; see the FBCharacterPoseFlag enum for the various options.      
    """
    def FBCharacterPoseOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mCharacterPoseKeyingMode=property(doc="CharacterPoseKeyingMode (FullBody or BodyPart).          ")
    mMirrorPlaneEquation=property(doc="Mirror plane equation (used when mMirrorPlaneType = kFBMirrorPlaneTypeEquation).          ")
    mMirrorPlanePanAngle=property(doc="Mirror plane pan angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser).          ")
    mMirrorPlaneTiltAngle=property(doc="Mirror plane tilt angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser).          ")
    mMirrorPlaneType=property(doc="Mirror plane type.          ")
    mModelToMatch=property(doc="Model to match.          ")
    pass

class FBCharacterSolver (object):
    """
    Constraint class.     
         
    """
    def FBCharacterSolver(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def GetParentRotationOffset(self,pR,pIndex):
        """
        Get the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.

        pR : Offset Rotation between the Bone and is parent at Stance Pose. 
        pIndex : Index of extra Bone to get. 
        """
        pass

    def SetParentRotationOffset(self,pR,pIndex):
        """
        Set the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.

        pR : Offset Rotation between the Bone and is parent at Stance Pose. 
        pIndex : Index of extra Bone to get. 
        """
        pass

    ExtraFK=property(doc="<b>Read Property:</b> List of Extra FK in character         ")
    ExtraBones=property(doc="<b>Read Property:</b> List of Extra Bones in character         ")
    Source=property(doc="<b>Read Write Property:</b> Source character when doing a character retarget.          ")
    pass

class FBColor (object):
    """
    FBColor class.     
    Color vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
# Supported list protocol methods:
color = FBColor()
len(color)
print color[0]
color[0] = 1.0
@endcode

 Slicing is not supported by this object.See samples: LayeredTexture.py, SetAllCamerasBackgroundColor.py, SetAllCamerasBackgroundColorFromCurrentCamera.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py.     
    """
    def FBColor(self):
        """
        Constructor.
        Default constructor, all values within are set to 0.0, except for the Alpha value which is set to 1.0.

        """
        pass

    def FBColor(self,pColor):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pColor : FBColor
        """
        pass

    def FBColor(self,pR,pG,pB):
        """
        Constructor.
        Explicitely construct a vector by specifying its RGBA values. Should the Alpha value not be relevant, just set it to 1.0.

        pR : float
        pG : float
        pB : float
        """
        pass

    def FBColor(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 3.

        p0 : tuple< float, float, float >
        """
        pass

    def FBColor(self):
        """
        Constructor.

        """
        pass

    def FBColor(self,pValue):
        """
        Constructor from array.

        pValue : Array to take values from. 
        """
        pass

    def FBColor(self,pRed,pGreen,pBlue):
        """
        Constructor.

        pRed : Red component. 
        pGreen : Green component. 
        pBlue : Blue component. 
        """
        pass

    def FBColor(self,pVector):
        """
        Copy Constructor.

        pVector : FBColor
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print color[1].

        pIndex : Index of the components to get (0:Red, 1:Green, 2:Blue) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0:Red, 1:Green, 2:Blue) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBColorAndAlpha (object):
    """
    FBColorAndAlpha class.     
    Color and alpha vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
# Supported list protocol methods:
color = FBColorAndAlpha()
len(color)
print color[0]
color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBColorAndAlpha(self):
        """
        Constructor.
        Default constructor, all values within are set to 0.0, except for the Alpha value which is set to 1.0.

        """
        pass

    def FBColorAndAlpha(self,pColor):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pColor : FBColor
        """
        pass

    def FBColorAndAlpha(self,pR,pG,pB,pAlpha):
        """
        Constructor.
        Explicitely construct a vector by specifying its RGBA values. Should the Alpha value not be relevant, just set it to 1.0.

        pR : float
        pG : float
        pB : float
        pAlpha : float
        """
        pass

    def FBColorAndAlpha(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 4.

        p0 : tuple< float, float, float, float >
        """
        pass

    def FBColorAndAlpha(self):
        """
        Constructor.

        """
        pass

    def FBColorAndAlpha(self,pValue):
        """
        Constructor from array.

        pValue : Array to take values from. 
        """
        pass

    def FBColorAndAlpha(self,pRed,pGreen,pBlue,pAlpha):
        """
        Constructor.

        pRed : Red component. 
        pGreen : Green component. 
        pBlue : Blue component. 
        pAlpha : Alpha component(default=1.0). 
        """
        pass

    def FBColorAndAlpha(self,pValue):
        """
        Constructor from FBColor.

        pValue : FBColor to take values from. 
        """
        pass

    def FBColorAndAlpha(self,pValue):
        """
        Constructor from FBColorF.

        pValue : FBColorF to take values from. 
        """
        pass

    def FBColorAndAlpha(self,pVector):
        """
        Copy Constructor.

        pVector : FBColorAndAlpha
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print color[1].

        pIndex : Index of the components to get (0:Red, 1:Green, 2:Blue) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0:Red, 1:Green, 2:Blue) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBComponentList (object):
    """
    FBComponentList class.     
    This class implements a special sort of list that can only contain instances of FBComponent objects. To users it behaves as a tuple, since it is not possible to add new objects in the list. Only methods or function that uses FBComponentList as argument can insert new objects. Users can query the content of the list with the bracket operator. 
@code
# Supported list protocol methods:
l = FBComponentList()
len(l)
print l[0]
@endcode

     
    """
    def FBComponentList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : FBComponent element value 
        """
        pass

    pass

class FBConfigFile (object):
    """
    Interface to the application config files.     
     This class allows client code to generate, modify and query configuration files. Config files will be automatically created when needed. They will be located in the /bin/config folder or an explicitly specified folder depending on the constructor used. See samples: FBConfigFile.py, ActionScriptMgr.py, ActionScriptMgr.py, KeyboardMapper.py, ShotTrackSetupTool.py.     
    """
    def FBConfigFile(self,pConfigFileName,pVirtualMode,pClearFile):
        """
        Constructor.
        This will open the desired config file from the [APPLICATION]/bin/config folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.

        pConfigFileName : Name the config file to use. 
        pVirtualMode : Enable this to limit disk access, file will only be read at construction and written at destruction. 
        pClearFile : Remove all existing content from the config file. 
        """
        pass

    def FBConfigFile(self,pConfigFileName,pConfigFilePath,pVirtualMode,pClearFile):
        """
        Constructor.
        This will open the desired config file in the designed folder. The file will be created if it does not exists. By prefixing the character '@' to the file name, this will automatically prepend the current machine name to the config file, the way it is done for the other config files of the application.

        pConfigFileName : Name the config file to use. 
        pConfigFilePath : Location where the file should reside. Missing directories will not be created. 
        pVirtualMode : Enable this to limit disk access, file will only be read at construction and written at destruction. 
        pClearFile : Remove all existing content from the config file. 
        """
        pass

    def ClearFile(self):
        """
        Remove all content from the config file.

        """
        pass

    def Get(self,pSectionName,pItemName,pDefaultValue):
        """
        Get an item's value.
        Get an item's value by looking inside a specific section of the config file.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pDefaultValue : Default value that will be returned if the item is not found. 
        return : The value assigned to the item in the specified section of the config file, or the default value if not found. 
        """
        pass

    def GetOrSet(self,pSectionName,pItemName,pValue,pComment):
        """
        Get a value from the config file and set it if it was not found.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pValue : Reference the the string that will contain the value of the item. If the item is not found in the file, it will be added with the initial value in this string. 
        pComment : Optional parameter that can be used to add a comment. 
        return : <b>true</b> if the value was found or added, or false if the item was not found and could not be added to the file. 
        """
        pass

    def Set(self,pSectionName,pItemName,pValue,pComment):
        """
        Set an item's value.
        Assign a value to an item in the config file. If the item does not exist, it will be created.

        pSectionName : Name of the section. 
        pItemName : Name of the item. 
        pValue : Value assigned to the item. 
        pComment : Optional parameter that can be used to add a comment. 
        return : <b>true</b> if the item was written to the config file, <b>false</b> otherwise. 
        """
        pass

    pass

class FBConstraintInfo (object):
    """
    Constraint information class.     
     This data structure is passed to the real-time evaluation callback for a constraint (AnimationNodeNotify()).      
    """
    def GetSnapRequested(self):
        """
        Was a 'snap' requested?

        return : <b>true</b> if 'snap' was requeststed. 
        """
        pass

    def GetZeroRequested(self):
        """
        Was a 'zero' requested?

        return : <b>true</b> if 'zero' was requeststed. 
        """
        pass

    pass

class FBConstraintRelation (object):
    """
    ConstraintRelation class.     
     This class exposes the relation constraint and allows addition of new boxes and removal of existing ones. See sample: TraversingRelationConstraint.py.     
    """
    def FBConstraintRelation(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def GetBoxPosition(self):
        """
        Get a box position in the GUI.
        Get the position of a box within the constraint layout view.

        return : A tuple containing: the result of operation (bool), X value (int), and Y value(int) 
        """
        pass

    def ConstrainObject(self,pConstrainedObject):
        """
        Create a receiver box.
        Use an existing FBBox object to create a receiver in the relation.

        pConstrainedObject : Destination box to insert in the constraint. 
        return : A place holder box for the object. 
        """
        pass

    def CreateFunctionBox(self,pGroup,pName):
        """
        Create a function box.
        Ask the constraint to create new function box.

        pGroup : Name of the group under which the function is located in the Constraint Relation GUI (case-sensitive!). 
        pName : Name of the function, as seen in the GUI (case-sensitive!). 
        return : The newly created function box, or NULL if the name/group combination was invalid. 
        """
        pass

    def SetAsSource(self,pSource):
        """
        Create a sender box.
        Use an existing FBBox object to create a sender in the relation.

        pSource : Source box to insert in the constraint. 
        return : A place holder box for the object. 
        """
        pass

    def SetBoxPosition(self,pBox,pX,pY):
        """
        Set a box position in the GUI.
        Set the position of a box within the constraint layout view.

        pBox : Box which needs to be moved. 
        pX : New X position. 
        pY : New Y position. 
        return : A boolean value indicating success (True) or failure (False). 
        """
        pass

    Boxes=property(doc="<b>List:</b> Boxes used in this constraint.          ")
    pass

class FBConstructionOperation (object):
    """
    FBConstructionOperation is used to represent an operation in the construction history.     
     The operation can be any valid script. Currently, only python scripts are supported.An instance of this class defaults to the correct value in order to add a new construction history. If the workgroup plugin is loaded, the operation will be replicated on all machine within a session.      
    """
    def FBConstructionOperation(self):
        """
        Constructor.

        """
        pass

    def FBConstructionOperation(self,pOperation):
        """
        pOperation : FBConstructionOperation
        """
        pass

    def GetCommandId(self):
        """
        """
        pass

    def GetExecuteAsLocalOperation(self):
        """
        """
        pass

    def GetLanguage(self):
        """
        """
        pass

    def GetLanguageVersion(self):
        """
        """
        pass

    def GetOrigin(self):
        """
        """
        pass

    def GetScript(self):
        """
        """
        pass

    def SetCommandId(self,commandId):
        """
        SetCommandId Set the operation's Id so that operation transactions can be resolved properly (eg: command 1 should go before command 2).
        Set this to -1 for new operations.

        commandId : Command Id. Defaults to -1. 
        """
        pass

    def SetExecuteAsLocalOperation(self,bIsLocal):
        """
        SetExecuteAsLocalOperation Whether to execute this operation as local or remote.
        If this is set to false (remote) and an operation is sent to the construction history, it will also execute locally on this motionbuilder.

        bIsLocal : Defaults to true (local). 
        """
        pass

    def SetLanguage(self,language):
        """
        SetLanguage Set the script language for this operation.
        Currently only 'python' is supported.

        language : Langugage string. Default to construction history's code generator's language (Currently "python"). 
        """
        pass

    def SetLanguageVersion(self,version):
        """
        SetLanguageVersion Set the script language interpreter's version that this operation should be interpreted with.

        version : Version number. Defaults to construction history's code generator's version (Currently 1). 
        """
        pass

    def SetOrigin(self,origin):
        """
        SetOrigin Set operation's original creator.
        For instance 'localhost' or . Should mostly be 'localhost' for new operations.

        origin : Operation's Origin. Defaults to "localhost". 
        """
        pass

    def SetScript(self,script):
        """
        SetScript Set the script content for this operation.

        script : Script content as a string. Defaults to empty. 
        """
        pass

    pass

class FBDeviceNotifyInfo (object):
    """
    Device Input and Output Notification information structure.     
     This structure is passed to the real-time device IO callback DeviceIONotify. It furnishes the device callback with the system time, local time, and sync counts for the current device cycle.      
    """
    def GetLocalTime(self):
        """
        Get local time.

        return : Current local time. 
        """
        pass

    def GetSyncCount(self):
        """
        Return the wanted timer sync count (internal or external)

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetSystemTime(self):
        """
        Get system time.

        return : Current system time. 
        """
        pass

    pass

class FBDirMap (object):
    """
        
        
    """
    def Add(self,pSourceDir,pTargetDir):
        """
        Adds an entry in the map.
        Environment variables can be specified for the target path using the syntax. Environment variables are expanded before the paths get added to the map. An error in the formatting of the paths (environment variable tokens) will abort the expansion and both given paths will remained unchanged.

        pSourceDir : str
        pTargetDir : str
        """
        pass

    def Clear(self):
        """
        Clears the map.

        """
        pass

    def GetCount(self):
        """
        Returns the number of items in the map.

        """
        pass

    def GetSource(self,pIndex):
        """
        Returns the source directory for the element at specified index.

        pIndex : int
        """
        pass

    def GetTarget(self,pIndex):
        """
        Returns the target directory for the element at specified index.

        pIndex : int
        """
        pass

    def Map(self,pPath):
        """
        Iterates through all the mapped directories.
        If one of the mapped directory's source is found in the given path, that part of the path will be replaced by the mapped directory's target. Only the first occurrence is processed.

        pPath : The path to process 
        """
        pass

    pass

class FBEvaluateInfo (object):
    """
    AnimationNodeNotify evaluation information.     
     This structure is passed to the AnimationNodeNotify calls (in Constraints, Devices, and Boxes), giving the connectors information with regards to the start or stop times of the evaluation. In general, only the start time is of interest for the current evaluation cycle. The advantage of the structure is to have a common time for the evaluation of all the elements in the scene.      
    """
    def GetEvaluationID(self):
        """
        Return the wanted timer sync count (internal or external).

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetLocalTime(self):
        """
        Return local (scene) time.

        return : Local time. 
        """
        pass

    def GetSyncCount(self):
        """
        Return the wanted timer sync count (internal or external).

        return : sync count or <b>-1</b> if no sync is present 
        """
        pass

    def GetSystemTime(self):
        """
        Return system time.

        return : System time. 
        """
        pass

    def IsStop(self):
        """
        Is local time stopped? (ie: no animation).

        return : <b>true</b> if local time is stopped. 
        """
        pass

    pass

class FBEvent (object):
    """
    Base Event class.     
         
    """
    def FBEvent(self,pEvent):
        """
        Constructor.
        Receives an object of type HKEvent that the corresponding callback will receive as a parameter.

        pEvent : Internal event to obtain information from. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of event.          ")
    pass

class FBEventDragAndDrop (object):
    """
    Drag and drop interface.b>Event: Global Evaluation pipeline critical timing callback event.     
         
    """
    def FBEventDragAndDrop(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    def Accept(self):
        """
        Accept a drag and drop sequence.
        This will cause the region in question to accept a drag and drop action when this event occurs.

        """
        pass

    def Add(self,pComponent,pId):
        """
        Add an item to the drag and drop list.

        pComponent : Item to add to the list. 
        pId : User-defined reference for the item (default = 0 ). 
        """
        pass

    def Clear(self):
        """
        Clear drag and drop list.

        """
        pass

    def Get(self,pIndex):
        """
        Get the FBComponent specified by <b>pIndex</b> from the Drag and Drop list.

        pIndex : Index in list where to get FBComponent. 
        return : Handle to FBComponent in list at <b>pIndex</b>. 
        """
        pass

    def GetCount(self):
        """
        Get the number of items in the DragAndDrop list.

        return : Number of items in DragAndDrop list. 
        """
        pass

    Components=property(doc="<b>Read Property:</b> List of components drop. (it acces the same data as FBEventDragAndDrop.Get)         ")
    Data=property(doc="<b>Property:</b> User specified reference. (for example, FBSpread:row)          ")
    PosX=property(doc="<b>Property:</b> X position of mouse.          ")
    PosY=property(doc="<b>Property:</b> Y position of mouse.          ")
    State=property(doc="<b>Property:</b> Drag and drop sub-event.          ")
    pass

class FBEventName (object):
    """
    These events are used internally by the Python Callback mecanism.     
    These are not meant to be manipulated by a user.     
    """
    kFBEventActivate=property(doc="        ")
    kFBEventShow=property(doc="        ")
    kFBEventDragAndDrop=property(doc="        ")
    kFBEventInput=property(doc="        ")
    kFBEventMenu=property(doc="        ")
    kFBEventTreeSelect=property(doc="        ")
    kFBEventExpose=property(doc="        ")
    kFBEventResize=property(doc="        ")
    kFBEventTransaction=property(doc="        ")
    kFBEventDoubleClick=property(doc="        ")
    kFBEventOnClick=property(doc="        ")
    kFBEventEnter=property(doc="        ")
    kFBEventExit=property(doc="        ")
    kFBEventIdle=property(doc="        ")
    kFBEventChange=property(doc="        ")
    kFBEventCellChange=property(doc="        ")
    kFBEventRowClick=property(doc="        ")
    kFBEventColumnClick=property(doc="        ")
    kFBEventTreeExpanding=property(doc="        ")
    kFBEventTreeExpanded=property(doc="        ")
    kFBEventTreeCollapsing=property(doc="        ")
    kFBEventTreeCollapsed=property(doc="        ")
    kFBEventFileNewCompleted=property(doc="        ")
    kFBEventFileNew=property(doc="        ")
    kFBEventFileOpenCompleted=property(doc="        ")
    kFBEventFileOpen=property(doc="        ")
    kFBEventFileSaveCompleted=property(doc="        ")
    kFBEventFileSave=property(doc="        ")
    kFBEventFileExit=property(doc="        ")
    kFBEventUnbindSDK=property(doc="        ")
    pass

class FBFCurveKey (object):
    """
    KeyFrame for an FCurve.     
    See sample: StartKeysAtCurrentTime.py.     
    """
    def FBFCurveKey(self,pFCurve,pKeyIndex):
        """
        Constructor.

        pFCurve : Parent FCurve (default is NULL). 
        pKeyIndex : Key frame index (default is 1). 
        """
        pass

    def FBFCurveKey(self,pFCurveKey):
        """
        Constructor.

        pFCurveKey : FCurveKey to copy information from. 
        """
        pass

    Bias=property(doc="<b>Read Write Property:</b> Bias (TCB).          ")
    Continuity=property(doc="<b>Read Write Property:</b> Continuity (TCB).          ")
    ExtrapolationMode=property(doc="<b>Read Write Property:</b> Extrapolation mode          ")
    Interpolation=property(doc="<b>Read Write Property:</b> Type of interpolation.          ")
    LeftBezierTangent=property(doc="<b>Read Write Property:</b> Left bezier tangent          ")
    LeftDerivative=property(doc="<b>Read Write Property:</b> Left derivative, in units/seconds.          ")
    LeftTangentWeight=property(doc="<b>Read Write Property:</b> Left tangent weight          ")
    MarkedForManipulation=property(doc="<b>Read Write Property:</b> Is the key marked for manipulation.          ")
    RightBezierTangent=property(doc="<b>Read Write Property:</b> Right bezier tangent          ")
    RightDerivative=property(doc="<b>Read Write Property:</b> Right derivative, in units/seconds.          ")
    RightTangentWeight=property(doc="<b>Read Write Property:</b> Right tangent weight          ")
    Selected=property(doc="<b>Read Write Property:</b> Is the key selected.          ")
    TangentBreak=property(doc="<b>Read Write Property:</b> Tangent's break status          ")
    TangentClampMode=property(doc="<b>Read Write Property:</b> Tangent's clamp method.          ")
    TangentConstantMode=property(doc="<b>Read Write Property:</b> Tangent's constant mode          ")
    TangentCustomIndex=property(doc="<b>Read Write Property:</b> Tangent's custom index          ")
    TangentMode=property(doc="<b>Read Write Property:</b> Tangent calculation method.          ")
    TangentWeightMode=property(doc="<b>Read Write Property:</b> Tangent's weight mode. Setting the value for LeftTangentWeight/RightTangentWeight will also activate the weight for that part. Please see the note provided with FBTangentWeightMode for the left weight of a key.          ")
    Tension=property(doc="<b>Read Write Property:</b> Tension (TCB).          ")
    Time=property(doc="<b>Read Write Property:</b> Time of key.          ")
    Value=property(doc="<b>Read Write Property:</b> Value of Key          ")
    pass

class FBFilterManager (object):
    """
    Filter manager.     
     This class provides list of all available filter types and a factory method in order to create an instance of the desired filter type.This manager will list both built-in and plug-in filters.See the class FBFilter for more details.Filter type names are not localised, and are the same as presented in the GUI.The following sample code shows how to use C++ or Python to create an instance of the orfilter_template filter and set one of its property. For the sample code to work, the plugin must have been compiled and copied in the plugins folder prior to the application startup.Sample C++ code: 
@code
// Create a filter of a known type. In this case the sample filter
// provided with the samples: orfilter_template.

FBFilterManager lFilterManager;

FBFilter* lFilter = lFilterManager.CreateFilter( 'OR - Filter Template' );

// Set one of the filter property:
FBPropertyDouble* lPropDouble = (FBPropertyDouble*)lFilter->PropertyList.Find( 'Test Double' );
if( lPropDouble )
{
    (*lPropDouble) = 2.0;
}

// Now we can apply the filter on an FCurve.
// ...

// And when we are done, destroy it.
lFilter->FBDelete();
lFilter = NULL;
@endcode

Sample Python code: 
@code
from pyfbsdk import *

# Create a filter of a known type. In this case the sample filter
# provided with the samples: orfilter_template.

lFilterManager = FBFilterManager()

lFilter = lFilterManager.CreateFilter( 'OR - Filter Template' );

# Set one of the filter property:
lPropDouble = lFilter.PropertyList.Find( 'Test Double' );
if lPropDouble: lPropDouble.Data = 2.0

# Now we can apply the filter on an FCurve.
# ...

# And when we are done, destroy it.
lFilter.FBDelete()
@endcode

     
    """
    def FBFilterManager(self):
        """
        Constructor.

        """
        pass

    def CreateFilter(self,pFilterTypeName):
        """
        Create a filter instance according to the filter type requested.

        pFilterTypeName : String describing the type of the desired filter, as obtained from list FilterTypeNames. 
        return : A pointer to a filter instance, or a NULL if the type name was invalid. 
        """
        pass

    FilterTypeNames=property(doc="List of available filters.          ")
    pass

class FBMatrix (object):
    """
    FBMatrix class.     
    Four x Four (double) Matrix.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 16 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator. 
@code
# Supported list protocol methods:
mat = FBMatrix()
len(mat)
print mat[13]
mat[12] = 1.0
@endcode

 The implementation of this 4x4 matrix uses a simple list of 16 elements, not a list of 4 vectors of 4 elements.* Slicing is not supported by this object.See sample: Matrix.py.     
    """
    def FBMatrix(self,pValue):
        """
        Constructor.

        pValue : Array to intialize matrix from. 
        """
        pass

    def FBMatrix(self,pMatrix):
        """
        Copy Constructor.

        pMatrix : Matrix to copy. 
        """
        pass

    def FBMatrix(self):
        """
        Constructor Initializes matrix to identity.

        """
        pass

    def FBMatrix(self,pValue):
        """
        Constructor.

        pValue : Array to intialize matrix from. 
        """
        pass

    def FBMatrix(self,pMatrix):
        """
        Copy Constructor.

        pMatrix : Matrix to copy. 
        """
        pass

    def Identity(self):
        """
        Load identity matrix.

        """
        pass

    def Set(self,pValue):
        """
        Set matrix from an array.

        pValue : Array to intialize matrix from. 
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print matrix[1].

        pIndex : Index of the components to get (0 to 15) 
        return : Matrix element value 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: color[1] = 0.5.

        pIndex : Index of the components to set (0 to 15) 
        pComponentValue : Value of component to set 
        """
        pass

    def Inverse(self):
        """
        Get Inversed matrix.

        return : the matrix Inversed. 
        """
        pass

    def InverseProduct(self,pMatrix):
        """
        InverseProduct Matrix.

        pMatrix : Matrix to Product. 
        return : result matrix. 
        """
        pass

    def Transpose(self):
        """
        Get Transposed matrix.

        return : the matrix Transposed. 
        """
        pass

    def Validate(self):
        """
        Validated matrix.

        return : true if matrix Validated. 
        """
        pass

    pass

class FBModelList (object):
    """
    FBModelList class.     
    This class implements a special sort of list that can only contain instances of FBModel objects. Users can query the content of the list with the bracket operator. 
@code
# Supported list protocol methods:
l = FBModelList()
len(l)
print l[0]
@endcode

     
    """
    def FBModelList(self):
        """
        Constructor.

        """
        pass

    def GetCount(self):
        """
        Get number of models in list.

        """
        pass

    def count(self):
        """
        Get number of models in list.

        """
        pass

    def GetModel(self,pIndex):
        """
        Get the ith model in list.

        pIndex : index of modle to get (0 based). 
        return : The pIndex model 
        """
        pass

    def Add(self,pModel):
        """
        Append a new modle at the end of the list.

        pModel : model to add to the list. 
        """
        pass

    def append(self,pModel):
        """
        Append a new modle at the end of the list.

        pModel : model to add to the list. 
        """
        pass

    def Clear(self):
        """
        Empty the list from all models.

        """
        pass

    def removeAll(self):
        """
        Empty the list from all models.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : Model element value 
        """
        pass

    pass

class FBMultiLangManager (object):
    """
    Language manager.     
     The class FBMultiLangManager indicates the supported languages and allows to query and change the current language.The support for localization is done using conversion tables from internal names to language specific names, so that they can be used in the GUI and other human readable contexts.At this time, changing the current language will not affect the GUI. Only calls to functions 'FBGetMultiLangText()' will be affected.The following sample code lists the names of the supported languages:Python sample code: 
@code
from pyfbsdk import *

lManager = FBMultiLangManager()
print 'Current localization language: ', lManager.GetCurrentLanguage()
print 'Supported languages:'
for lLanguage in lManager.Languages:
    print '  ', lLanguage
@endcode

C++ sample code: 
@code
FBMultiLangManager lManager;
FBTrace( 'Current localization language: %s\n', lManager.GetCurrentLanguage());
FBTrace( 'Supported languages:\n' );

int lIdx = 0;
while( lIdx < lManager.Languages.GetCount())
{
    FBTrace( '  %s\n', lManager.Languages[lIdx++] );
}
@endcode

     
    """
    def FBMultiLangManager(self):
        """
        Constructor.

        """
        pass

    def GetCurrentLanguage(self):
        """
        Obtain the current language.
        Query the current language used for the GUI.

        return : Will return the string associated with the current language used. 
        """
        pass

    def SetCurrentLanguage(self,pLanguage):
        """
        Set the current language.
        Change the current language to another available language.

        pLanguage : The string corresponding to the desired language, as defined in property Languages. 
        return : Indicate if the change of language was successful. 
        """
        pass

    Languages=property(doc="List of available languages.          ")
    pass

class FBObjectPoseMirrorOptions (object):
    """
    FBObjectPoseMirrorOptions class.     
     This class exposes the object used to store the options for the mirror of an object pose.      
    """
    def FBObjectPoseMirrorOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mMirrorPlaneEquation=property(doc="Equation of the mirror plane.          ")
    pass

class FBObjectPoseOptions (object):
    """
    FBObjectPoseOptions class.     
     This class exposes the object used to store the options for operations on object poses.      
    """
    def FBObjectPoseOptions(self):
        """
        Constructor.

        """
        pass

    def ClearFlag(self):
        """
        Clear all flags.

        """
        pass

    def GetFlag(self,pFlag):
        """
        Get a flag value.

        pFlag : Flag to get. 
        return : Value of the flag. 
        """
        pass

    def SetFlag(self,pFlag,pValue):
        """
        Set a flag value.

        pFlag : Flag to set. 
        pValue : Value to set. 
        """
        pass

    mPoseTransformType=property(doc="Transform type (Local, Global or LocalRef).          ")
    mReferenceGRM=property(doc="Global rotation matrix of reference object.          ")
    mReferenceGSM=property(doc="Global scaling matrix of reference object.          ")
    mReferenceGT=property(doc="Global translation vector of reference object.          ")
    pass

class FBPickInfosList (object):
    """
    FBPickInfosList class.     
    This class implements a special sort of list that can only contains a pick info which is a tuple<FBModel, FBVector3d>. A pick info give the position (FBVector3d) and the model (FBModel) that was pick on screen.To users FBPickInfosList behave like a typle, since it is not possible to add new objects in the list. Only methods or function that uses FBPickInfosList as argument can insert new objects. Users can query the content of the list with the bracket operator. 
@code
# Supported list protocol methods:
l = FBPickInfosList()
len(l)

# tuple unpacking of pick infos.
model, vector = l[0]
@endcode

     
    """
    def FBPickInfosList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : PickInfos element value. A Pick info is a tuple<FBModel, FBVector3d> 
        """
        pass

    pass

class FBPlotOptions (object):
    """
    Option parameters for plotting.     
    See samples: PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py.     
    """
    def FBPlotOptions(self):
        """
        Constructor.

        """
        pass

    PlotAllTakes=property(doc="<b>Read Write Property:</b> Should we plot all takes?         ")
    PlotOnFrame=property(doc="<b>Read Write Property:</b> Should we plot on frame?         ")
    PlotPeriod=property(doc="<b>Read Write Property:</b> The plot period (1/fps).         ")
    RotationFilterToApply=property(doc="<b>Read Write Property:</b> The rotation filter to apply.         ")
    UseConstantKeyReducer=property(doc="<b>Read Write Property:</b> Should we use a constant key reducer with the filter?         ")
    ConstantKeyReducerKeepOneKey=property(doc="<b>Read Write Property:</b> Should the constant key reducer keep at least one key?         ")
    PlotTranslationOnRootOnly=property(doc="<b>Read Write Property:</b> Should we plot the translation on root only?         ")
    PreciseTimeDiscontinuities=property(doc="<b>Read Write Property:</b> Should we use precise time discontinuities?         ")
    PlotLockedProperties=property(doc="<b>Read Write Property:</b> Should we plot locked properties?         ")
    PlotTangentMode=property(doc="<b>Read Write Property:</b> The tangent mode for plotted curve.         ")
    PlotAuxEffectors=property(doc="<b>Read Write Property:</b> Should we plot aux effectors?         ")
    EvaluateDeformation=property(doc="<b>Read Write Property:</b> Should we evaluate deformation while plotting? This is useful when there is a dependency with the deformation. Disabled by default.         ")
    pass

class FBPlug (object):
    """
    Connections Basic Open Reality SDK Element.     
     Most elements that are available in the SDK inherit from this base class since FBComponent and FBProperty inherit from FBPlug. Basically, all objects can be connected together because they are all 'plugs'. To simplify the graph, you can think of a 'source' connection as a child, and a 'destination' connection as a parent. Also, it is correct to assume that a source affect/work on its destination. For example, a shader applied on an object would be seen as the source while the object is the destination. So FBPlug is a set of functions that enables you to control those connections with flexibility and ease. See samples: FBConstraintManager.py, FBFolder.py.     
    """
    ClassGroupName=property(doc="ClassGroupName of the object.          ")
    TypeInfo=property(doc="TypeInfo.          ")
    pass

class FBProfileTaskCycle (object):
    """
    FBProfileTaskCycle.     
     Real-time profiling information for a specific task. Profiling information can be collected for:Evaluation: models, constraints, characters, story tracksDevices: DeviceIONotify, DeviceEvaluationNotifyRendering: renderer, render passes (like: Translucent, TranslucentZSort, Selected, OtherPrimitive, SelectiveLighting, etc)SDKInternal synchronization (idle callback, buffer swap, waiting on evaluation to finish before starting new rendering)When profiling a scene within a MotionBuilder session you can discover what tasks are being performed when and for how long. You can use this information to troubleshoot lengthy or repetitive actions, and use MotionBuilder more efficiently.A task is defined as a definite piece of work within MotionBuilder such as the evaluation of a character. If the same task is run numerous times it is called a task cycle. From within a scene, the hierary and dependents of the scene make up the task cycles. A task cycle spends its time computing a specific task within a task parent cycle.A task parent cycle is a hierarchy of individual task cycles, where the parent and child relationship is known to MotionBuilder and displayed in the profiling center.For example, these are all task cycles which are all parented to each other; Eval is parent of TransformNode_Active, which is a parent of Constraint, which is a parent of Character, which is in turn a parent of TransformNode_Active.This is because the evaluation is called for one model which triggers evaluation of the character which then calls the evaluation of the rest of IK/FK models.When an evaluation starts, it calls the evaluation of the character, the time will be computed for time spent on the sample. Then possibly another character is evaluated, so again the time will be computed for the time spent on this sample. This time will be added to the previous sample since that evaluation has not finished yet. The evaluation here is parented, since they both have started but not finished, all children samples are summed. When the evaluation stops, you change the sample for the children.Note: The evaluation dependency/order will be different for each scene.As you can see profiling of task cycles is done by collecting samples. Samples are added to one inside parent sample. The number of samples collected is controlled by the profiler buffer size property.Here are the steps to add profiling into a constraint, a device, or any other class that uses real-time evaluation: 1) Declare FBProfiler_CreateTaskCycle( MyConstraint, 0.5, 0.5, 0.5 ) in MyConstraint.cxx, before the constructor and AnimationNodeNotify function. 2) Set up FBProfiling_SetupTaskCycle( MyConstraint ) in the constuctor MyConstraint::MyConstraint(). 3) At the beginning of MyConstraint::AnimationNodeNotify create the variable: FBProfilerHelper lProfiling( FBProfiling_TaskCycleIndex( MyConstraint ), pEvaluateInfo ); The sample for task will start at the creation of FBProfilerHelper object and stop at the destruction of this object, when returning from AnimationNodeNotify will be done.      
    """
    def GetAvgMinMaxUsage(self,pAvg,pMin,pMax):
        """
        Get the task cycle's average, minimum and maximum usage.
        Results will vary on buffer size. When profiling is disabled all values are set to 1.

        pAvg : Average time spend for computation of task (in micro seconds). 
        pMin : Minimum time spend for computation of task (in micro seconds). 
        pMax : Maximum time spend for computation of task (in micro seconds). 
        """
        pass

    def GetChild(self,pIndex):
        """
        Get child task based on specific index.
        Can return NULL if child index is not used.

        pIndex : Child index. 
        return : Child at given index. 
        """
        pass

    def GetChildCount(self):
        """
        Get number of child tasks.
        Task cycles are organized in a hierarchy which is dependent on the scene. Samples can be cumulative in the parent task cycle, or independent. For example, all character evaluation samples will be cumulated in one evaluation cycle.

        return : Number of child tasks. 
        """
        pass

    def GetColor(self):
        """
        Get the color of the task cycle.
        Used in profiling Center for drawing.

        """
        pass

    def GetIndex(self):
        """
        Get the unique registration index for each cycle.

        """
        pass

    def GetName(self):
        """
        Get the name of task cycle.

        """
        pass

    def IsStarted(self):
        """
        Test to see if sampling has started.

        """
        pass

    pass

class FBProfileTimeEvent (object):
    """
    FBProfileTimeEvent.     
     Time event information is collected during sampling (activated with a property in FBProfiler ActiveSampling). Events that can be collected are: render, evaluation, model evaluation, model deformation, synchronization of evaluation and rendering, playback commands, etc.Sampling will stop when the buffers maximum size is reached (maximum is 10MB).Currently users are not able to register any new events from ORSDK/python      
    """
    def GetColor(self):
        """
        Get the color assigned to the event.

        """
        pass

    def GetComment(self):
        """
        Get the comment for the event.
        Comments are not editable.

        """
        pass

    def GetThreadID(self):
        """
        Get the thread ID used in the event execution.

        """
        pass

    def GetTime(self):
        """
        Get the time when the event occurred.

        """
        pass

    def GetTypeName(self):
        """
        Get the event registered type name.

        """
        pass

    def IsSingleEvent(self):
        """
        Three types of events exits: single, start and end.
        Some actions that takes more time to execute or when other events can occur inbetween are collected with start time event at begin and end time event at finish.

        """
        pass

    pass

class FBProperty (object):
    """
    Generic application property.     
    b>Property: Action Action property to trigger function.FBProperty objects cannot be instantiated by the user. Reference to a property can be obtained either via an instance of a FBComponent object, or by calling the method 'Find()' of a FBPropertyManager. The class FBComponent has a FBPropertyManager data member named 'PropertyList'.When accessing a FBProperty object via its containing object, you can get or set (assuming it is not read-only) its value directly:    lObject.Visibility = TrueWhen accessing a property reference directly, its value is obtained via it's 'Data' member.    lProp = lObject.PropertyList.Find( 'Visibility' )   if lProp: lProp.Data = TrueThe methods 'PropertyCreate()' and 'PropertyRemove' of the class FBComponent can be used to modify an object's set of properties.     
    """
    def FBProperty(self):
        """
        Constructor.

        """
        pass

    def AllowsLocking(self):
        """
        AllowsLocking.

        return : <b>true</b> if property can be locked 
        """
        pass

    def AsString(self,pFlag):
        """
        Get the property value as a string.

        pFlag : Indicates the returned string to be used for UI or storage. It defaults to kFBDataAsStringUI. 
        return : The string version of the property. 
        """
        pass

    def EnumList(self,pIndex):
        """
        Return the string of an enum value.

        pIndex : Enum value to get string for. 
        return : String value of enum specified by pIndex. 
        """
        pass

    def GetEnumStringList(self,pCreateIt):
        """
        String list for enum properties.

        pCreateIt : Create a new list if necessary. 
        return : the pointer to the string list.. 
        """
        pass

    def GetMax(self):
        """
        GetMax.

        return : Maximum value for the property. 
        """
        pass

    def GetMin(self):
        """
        GetMin.

        return : Minimum value for the property. 
        """
        pass

    def GetName(self):
        """
        Get the property's name.

        return : The property's name. 
        """
        pass

    def GetPropertyFlag(self,pFlag):
        """
        GetPropertyFlag.

        pFlag : Flag to test if it is True or False. 
        return : If the flag is True, the function returns True and vice-versa. 
        """
        pass

    def GetPropertyFlags(self):
        """
        GetPropertyFlags.

        return : Return all flags at once. 
        """
        pass

    def GetPropertyType(self):
        """
        Get the property's type.

        return : The property's type. 
        """
        pass

    def GetPropertyTypeName(self):
        """
        Get the property's type name.

        return : The property's type name. 
        """
        pass

    def GetReferencedProperty(self):
        """
        Get the referenced property, in the case of this property is a reference property (see the IsReferenceProperty() method).

        return : The referenced property, or a null pointer if this property is not a reference property. 
        """
        pass

    def GetSubMemberCount(self):
        """
        GetSubMemberCount.

        return : Number of sub-members. 
        """
        pass

    def HasSomethingLocked(self):
        """
        HasSomethingLocked.

        return : <b>true</b> if property or any of its members is locked 
        """
        pass

    def IsAnimatable(self):
        """
        """
        pass

    def IsInternal(self):
        """
        """
        pass

    def IsList(self):
        """
        Verify if property is of this type.

        return : <b>true</b> if property is of type. 
        """
        pass

    def IsLocked(self):
        """
        IsLocked.

        return : <b>true</b> if property is locked 
        """
        pass

    def IsMaxClamp(self):
        """
        Indicate if maximum value clamping will be applied on user input value.

        return : <b>true</b> if property the value will be clamped to a maximum value. 
        """
        pass

    def IsMemberLocked(self,pIndex):
        """
        IsMemberLocked.

        pIndex : Index of the sub-member of the property to check. 
        return : <b>true</b> if property sub-member is locked 
        """
        pass

    def IsMinClamp(self):
        """
        Indicate if minimum value clamping will be applied on user input value.

        return : <b>true</b> if property the value will be clamped to a minimum value. 
        """
        pass

    def IsObjectList(self):
        """
        Indicate if is an instance of FBPropertyListObject.

        """
        pass

    def IsReadOnly(self):
        """
        Is property read-only?

        return : <b>true</b> if property is read-only. 
        """
        pass

    def IsReferenceProperty(self):
        """
        """
        pass

    def IsTextureConnectableProperty(self):
        """
        """
        pass

    def IsUserProperty(self):
        """
        """
        pass

    def ModifyPropertyFlag(self,pFlag,pValue):
        """
        ModifyPropertyFlag.

        pFlag : The flag to switch to True or False. 
        pValue : The value to set about this flag. 
        """
        pass

    def NotifyEnumStringListChanged(self):
        """
        Notify system that the enum list was modified.

        """
        pass

    def OriValueAsString(self):
        """
        Get the property original value (before any modification) as string.

        return : returns the original value of the property in string with format same as AsString(kDataAsStringPersistence) 
        """
        pass

    def SetLocked(self,pLocked):
        """
        SetLocked.

        pLocked : True if the property is to be locked, false if it is to be unlocked. 
        """
        pass

    def SetMax(self,pMax,pForceMaxClamp):
        """
        SetMax.

        pMax : Maximum value of the property. 
        pForceMaxClamp : Force clamping to maximum value of the property. 
        """
        pass

    def SetMemberLocked(self,pIndex,pLocked):
        """
        SetMemberLocked.

        pIndex : Index of the sub-member of the property to lock or unlock. 
        pLocked : True if the sub-member is to be locked, false if it is to be unlocked. 
        """
        pass

    def SetMin(self,pMin,pForceMinClamp):
        """
        SetMin.

        pMin : Minimum value of the property. 
        pForceMinClamp : Force clamping to minimum value of the property. 
        """
        pass

    def SetName(self,pName):
        """
        Set the property's name.

        pName : New name for the property. 
        """
        pass

    def SetString(self,pString):
        """
        Set the property value from a string.

        pString : String to set property value from, with format same as AsString(kFBDataAsStringPersistence) 
        return : True if it was possible. 
        """
        pass

    Name=property(doc="<b>Read Property:</b> The property's name.         ")
    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int).         ")
    pass

class FBPropertyList (object):
    """
    Tuple-like structure for system elements.     
    These list objects are used to expose system wide or instance specific list of objects. Two examples of this are FBSystem's list of Cameras and a FBModel's list of Shaders. These lists have been exposed to Python as tuple, whose content cannot be modified directly. This is due to the specific nature of each type of list and the access control required by the owner of the list. For example, creating a new FBCamera object will automatically add it to the list of FBSystem's Cameras. The user does not have to add it to the list. The same being true for the destruction of the camera which should be done by calling 'FBDelete()' on the object itself. Not by atempting to remove it from the list of cameras. 
@code
# Supported list operations:
len(propertyList)
print propertyList[0]
@endcode

     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print l[1].

        pIndex : Index of the components to get 
        return : Element contain in property list 
        """
        pass

    pass

class FBPropertyListDeviceOpticalMarker (object):
    """
        
        
    """
    def FBPropertyListDeviceOpticalMarker(self):
        """
        """
        pass

    pass

class FBPropertyListManipulator (object):
    """
    b>PropertyList: Device optical marker      
        
    """
    pass

class FBPropertyListMarkerSegment (object):
    """
    b>PropertyList: MarkerSet.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListMarkerSegment(self):
        """
        """
        pass

    pass

class FBPropertyListModelMarkerOptical (object):
    """
    b>PropertyList: ModelOptical.     
         
    """
    def FBPropertyListModelMarkerOptical(self):
        """
        """
        pass

    pass

class FBPropertyListOpticalGap (object):
    """
    b>PropertyList: Device optical marker      
        
    """
    def FBPropertyListOpticalGap(self):
        """
        """
        pass

    pass

class FBPropertyListOpticalSegment (object):
    """
    b>PropertyList: Physical properties      
        
    """
    def FBPropertyListOpticalSegment(self):
        """
        """
        pass

    pass

class FBPropertyListRigidBody (object):
    """
    b>PropertyList: Device optical marker      
        
    """
    def FBPropertyListRigidBody(self):
        """
        """
        pass

    pass

class FBPropertyListRigidBodyMarkers (object):
    """
    b>List: Set      
        
    """
    def FBPropertyListRigidBodyMarkers(self):
        """
        """
        pass

    pass

class FBPropertyListTreeNode (object):
    """
    PropertyList of nodes in the tree view.b>PropertyList: UserObject.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListTreeNode(self):
        """
        """
        pass

    pass

class FBPropertyManager (object):
    """
    Property Manager.     
     The property manager exists in all FBComponent objects, and contains an array of all the registered properties. These properties may be SDK properties, internal properties or both.      
    """
    def FBPropertyManager(self):
        """
        Constructor.

        """
        pass

    def Find(self,pPropertyName,pMultilangLookup):
        """
        Find a property, based on its name.

        pPropertyName : Name of property to look for. 
        pMultilangLookup : When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true) 
        return : Handle to property found. 
        """
        pass

    def FindPropertiesByName(self,pPropertyNamePattern,pPropList,pMultilangLookup):
        """
        This function will query the property list for properties fulfilling a particular name pattern.

        pPropertyNamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ) 
        pPropList : List that contains the resulting properties matching the pattern 
        pMultilangLookup : When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true) 
        """
        pass

    pass

class FBPropertyViewDefinition (object):
    """
    FBProperty View.     
     View definition for one property.      
    """
    def IsFolder(self):
        """
        Is view a folder.

        """
        pass

    def IsOpen(self):
        """
        Is property view open at run time.

        """
        pass

    def IsSaved(self):
        """
        Is property view saved on view manager store.

        """
        pass

    def SetOpen(self,pTrue,pApplyUpHierarchy):
        """
        Set view open/closed at run time.

        pTrue : bool
        pApplyUpHierarchy : bool
        """
        pass

    def SetSaved(self,pTrue,pApplyUpHierarchy):
        """
        Set view to be saved on view manager store.

        pTrue : bool
        pApplyUpHierarchy : bool
        """
        pass

    pass

class FBPropertyViewList (object):
    """
    FBProperty View List.     
     Hold list of description for view set.      
    """
    def AddPropertyView(self,pProperty,pHierarchy):
        """
        Add property view.

        pProperty : Property to add. 
        pHierarchy : Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation"). 
        return : created object (should not be called on non editable view list). 
        """
        pass

    def FindPropertyView(self,pPropertyName):
        """
        Find property view for pPropertyName in this list.

        pPropertyName : str
        """
        pass

    def IsEditable(self):
        """
        Is property view list editable.

        """
        pass

    def RemovePropertyView(self,pPropertyViewDefinition):
        """
        Remove property view from view list.

        pPropertyViewDefinition : Property view definition to destroy. 
        return : true when pPropertyViewDefinition got removed and free (should not be called on non editable view list). 
        """
        pass

    pass

class FBPythonWrapper (object):
    """
    Base class of FBPlug in Python.     
    This class act as a bridge between the ORSDK C++ world and the Python world. Since each Python objects wrap a ORSDK object we need a way to notify Python if the ORSDK object is destroyed.OnUnbind is used in this way: it notifies the user when the wrapped ORSDK objects is destroyed.     
    """
    OnUnbind=property(doc="<b>Event:</b> Will notifier the user when the corresponding ORSDK objects is unbound from the PythonObject.         ")
    pass

class FBRenderOptions (object):
    """
        
        
    """
    def FBRenderOptions(self,pOptions):
        """
        pOptions : HKRenderOptions
        """
        pass

    def GetIDBufferPickingAlphaThreshold(self):
        """
        Get IDBuffer Picking Alpha threshold.

        return : ID Buffer picking alpha threshold value. 
        """
        pass

    def GetRenderFrameId(self):
        """
        Get Render Frame ID.

        return : This return a new ID each time a new frame is drawn. 
        """
        pass

    def GetRenderingCamera(self):
        """
        Get the rendering camera.

        """
        pass

    def GetViewerOptions(self):
        """
        """
        pass

    def IsIDBufferRendering(self):
        """
        Get IDBuffer Rendering request status (for display or picking)

        return : true if need to render Model (or subitem)'s UniqueColorID into GL Color Buffer. 
        """
        pass

    def IsOfflineRendering(self):
        """
        Check if the render request comes from offline render mode (as opposed to viewport refresh).

        return : true if the render comes from offline render mode. 
        """
        pass

    pass

class FBScrollBox (object):
    """
    Scroll Box.     
     This class provides a layout that will be automatically managed with a scrollbar according to the specified width and height. This provides a way to add dynamic UI control. See sample: Scrollbox.py.     
    """
    def FBScrollBox(self):
        """
        Constructor.

        """
        pass

    Content=property(doc="<b>Read Property:</b> an empty layout in which you can add scrollable content.         ")
    pass

class FBShaderManager (object):
    """
    Shader manager.     
     This class provides access to the list of available shaders, both system shaders and user shaders. The list comes in two versions:ShaderTypeNames : which gives the internal names of the shaders,ShaderTypeNamesLocalized : uses the GUI names of the shaders.Both of these lists will have the same number of elements. The strings at position i in the lists refer to the same shader type. In cases where there is no localized version of the shader name, the internal name will be used in ShaderTypeNamesLocalized, thus ensuring consistency between the two lists.It also provides a generic shader creation method that uses the shader type name, internal or localized, to create the new shader instance.The destruction of shaders is achieved by calling the FBDelete method of a shader instance.The list of all the instantiated shaders can be obtained from instances of classes FBSystem or FBScene. Both classes have a Shaders property which lists the existing shader instances.Strings are used instead of enum, define or typedef values to refer to shader types as this proves to be more flexible.The system has a default shader of type 'Lighted'. Do not attempt to destroy it.The use of localized names in shader creation is non portable as it is dependent of the current language used by the application. The name may also change from one version to another. Using the internal name is the only way to ensure portable shader creation.Sample C++ code: 
@code
// This could be a constant value in the code, coming from a custom
// registry or simply coming from one of the list ShaderTypeNames
// or ShaderTypeNamesLocalized.
const char* lDesiredShaderTypeName = 'MyShader';

// Shader creation.
FBShader* lShader = NULL;
FBShaderManager lShaderManager;

if( lShaderManager.ShaderTypeNames.Find( lDesiredShaderTypeName ) != -1 ||
lShaderManager.ShaderTypeNamesLocalized.Find( lDesiredShaderTypeName ) != -1 )
{
lShader = lShaderManager.CreateShader( lDesiredShaderTypeName );

// Change its name, as the default name will be the type name.
if( lShader )
{
lShader->Name = 'My new shader';
}
else
{
// Warn about creation failure on a correctly registered
// shader type.
}
}
else
{
// Warn about an unknown shader type.
}

//
// Do some work with the shader...
// 

if( lShader )
{
lShader->FBDelete();
}
@endcode

In the previous code sample, the lookup in the manager list is not necessary, as the call to CreateShader would have failed nonetheless and returned a NULL pointer.Sample Python code: 
@code
from pyfbsdk import *

lShaderManager = FBShaderManager()

# This code will create one instance of each of the
# available shader type, changing its name to add the
# 'My ' prefix.
for lShaderTypeName in lShaderManager.ShaderTypeNames:
lShader = lShaderManager.CreateShader( lShaderTypeName )
if lShader:
lShader.Name = 'My %s' % lShader.Name
print 'Created new shader '%s'' % lShader.Name
else:
print 'Unable to create shader of type '%s'' % lShaderTypeName
@endcode

See sample: VertexArrayManipulation.py.     
    """
    def FBShaderManager(self):
        """
        Constructor.

        """
        pass

    def CreateShader(self,pShaderTypeName):
        """
        Creates a shader according to the shader type provided.
        This method provides a generic way of creating shaders using the type name, internal or localized. The name of the new shader will be the same as the type name used, subject to changes according to the system's unique name policy.

        pShaderTypeName : Name of the type of shader desired. 
        return : A pointer to the newly created shader object, or a NULL pointer if the type name was not recognised. 
        """
        pass

    ShaderTypeNames=property(doc="List of available shaders.          ")
    ShaderTypeNamesLocalized=property(doc="List of available shaders.          ")
    pass

class FBShaderModelInfo (object):
    """
        
        
    """
    def FBShaderModelInfo(self,pShader,pInfo,pSubRegionIndex):
        """
        pShader : FBShader
        pInfo : HKModelRenderInfo
        pSubRegionIndex : int
        """
        pass

    Model_Version=property(doc="<b>Read Write Property:</b> Shader version informations         ")
    Model=property(doc="<b>Read Write Property:</b> Shader mModel         ")
    pass

class FBSkeletonState (object):
    """
        
        
    """
    def GetNodeMatrix(self,pSkeletonId,pSkeletonGlobalMatrix):
        """
        Returned global matrix associated to the given Index.

        pSkeletonId : Index of the skeleton Node 
        pSkeletonGlobalMatrix : returned global matrix of the index Given 
        """
        pass

    pass

class FBSplitStyle (object):
    """
    Type of split style (sub-division) for layout.     
        
    """
    kFBNoSplit=property(doc="No split.         ")
    kFBHSplit=property(doc="Horizontal split.         ")
    kFBVSplit=property(doc="Vertical split.         ")
    kFBHVSplit=property(doc="Horizontal and Vertical split.         ")
    pass

class FBStringList (object):
    """
    String list.     
    See sample: Memo.py.     
    """
    def FBStringList(self):
        """
        Constructor.

        """
        pass

    def FBStringList(self,pString,pSeparator):
        """
        Constructor.

        pString : String to set for list. 
        pSeparator : the string list separator. 
        """
        pass

    def FBStringList(self,pOther):
        """
        Copy constructor.

        pOther : FBStringList
        """
        pass

    def Add(self,S,pRef):
        """
        Add a string to the list.

        S : String to add to list. 
        pRef : Reference to store with string (default = 0) 
        return : Index where item was stored. 
        """
        pass

    def AsString(self,pSeparator):
        """
        Get as string.

        pSeparator : the string list separator. 
        return : String list. 
        """
        pass

    def Clear(self):
        """
        Clear the list (remove all the items).

        """
        pass

    def Find(self,pRef):
        """
        Find the index where <b>pRef</b> is stored.

        pRef : Reference to look for. 
        return : Index at which <b>pRef</b> can be found. 
        """
        pass

    def Find(self,pString,pCaseSensitive,pStartWith):
        """
        Find the index with the string <b>pString</b> (or start with <b>pString</b>)

        pString : String to search for. 
        pCaseSensitive : true if considering case. 
        pStartWith : true if to find the index of the string which start with pString. 
        return : Index where <b>S</b> is stored. 
        """
        pass

    def GetAt(self,pIndex):
        """
        Get the string at <b>pIndex</b>.

        pIndex : Index to get string at. 
        return : String at <b>pIndex</b>. 
        """
        pass

    def GetReferenceAt(self,pIndex):
        """
        Get the reference store with the string at <b>pIndex</b>.

        pIndex : Index to get reference at. 
        return : Reference stored with value at <b>pIndex</b>. 
        """
        pass

    def IndexOf(self,S):
        """
        Get the index of a string.

        S : String to look for. 
        return : Index where string <b>S</b> was found. 
        """
        pass

    def InsertAt(self,pIndex,S,pRef):
        """
        Insert an entry at <b>pIndex</b>.

        pIndex : Index where item is to be inserted. 
        S : String to insert. 
        pRef : Reference to store with string(default=0). 
        """
        pass

    def Remove(self,S):
        """
        Remove a string from the list.

        S : String to remove from the list. 
        return : Index where item was found. 
        """
        pass

    def RemoveAt(self,pIndex):
        """
        Remove an entry at <b>pIndex</b>.

        pIndex : Index where item is to be removed from. 
        """
        pass

    def SetAt(self,pIndex,pString):
        """
        Set the string at <b>pIndex</b>.

        pIndex : Index where string is to be set. 
        pString : String to set value at <b>pIndex</b> with. 
        """
        pass

    def SetReferenceAt(self,pIndex,pRef):
        """
        Set the reference stored with the string at <b>pIndex</b>.

        pIndex : Index to store reference at. 
        pRef : Reference to store at <b>pIndex</b>. 
        """
        pass

    def SetString(self,pString,pSeparator):
        """
        Set string for list.

        pString : String to set for list. 
        pSeparator : the string list separator. 
        """
        pass

    def Sort(self):
        """
        Sort the string list (ascending)

        """
        pass

    pass

class FBSVector (object):
    """
    Three dimensional scaling vector.     
    See sample: Vectors.py.     
    """
    def FBSVector(self):
        """
        Constructor.

        """
        pass

    def FBSVector(self,pValue):
        """
        Constructor from array.

        pValue : Array to take values from. 
        """
        pass

    def FBSVector(self,p1,p2,p3):
        """
        Constructor.

        p1 : First element 
        p2 : Second element. 
        p3 : Third element(default=1.0). 
        """
        pass

    pass

class FBSystem (object):
    """
    Provides access to the underlying system, and the MotionBuilder scene.     
     Use this class to access system properties such as the computer name, the system time, and the MotionBuilder application version.It is also used to get access to the scene (FBScene) and the current take (FBTake), as in the following Python snippet: 
@code
myScene = FBSystem().Scene
for take in myScene.Takes:
    print take.Name
@endcode

The Python sample FBSystemEvents.py shows how to register a callback to FBSystem. See samples: FBSystemEvents.py, CameraSwitcher.py, BatchExportCharacterAnimationTool.py, ExportAnimationLibrary.py.     
    """
    def FBSystem(self):
        """
        Constructor.

        """
        pass

    def CurrentDirectory(self):
        """
        Get current work directory.

        return : current work directory. 
        """
        pass

    def GetCommandLineArgs(self):
        """
        Returns the command line arguments for SDK.
        This function returns portion of the command line arguments within a pair of delimiters (sdk-begin & sdk-end). Example:Note that '-console', '-G500,500', '-suspendMessages' and 'C:/temp/sample.fbx' are for MotionBuilder itself hence are consumed accordingly. Only those arguments between sdk-begin and sdk-end are accessible with this function. In this example, they will be '--department mocap --usage on-stage'This SDK command line argument is useful for plugin deployment and management in large production facility, where different department or different workflow may require a different set of plugins or functionality/behavior dynamically.Python users also have access to this through official built-in module sys.argv which could be parsed easily via argparse module.

        return : the command line arguments 
        """
        pass

    def GetLoadedPluginItemGroups(self,pPluginItemName):
        """
        Returns a string list containing the groups list in which the specified plug-in item's name belongs to.

        pPluginItemName : str
        return : the groups list in which the specified plug-in item's name belongs to. 
        """
        pass

    def GetLoadedPluginItemInfo(self,pPluginItemName):
        """
        Returns a string list containing the information of the specified plug-in item's name.
        A specific plug-in item information can be retrieved from the returned string list with a EPluginItemInfo enum value.

        pPluginItemName : str
        return : the information of the specified plug-in item's name. 
        """
        pass

    def GetLoadedPluginItemsName(self):
        """
        Returns a string list containing the names of all the loaded plug-in.

        return : the names of all the loaded plug-in. 
        """
        pass

    def GetPluginPath(self):
        """
        Returns the plugin path.
        By default, MotionBuilder searches C++ plug-ins and load them at start-up. Users could provide additional plugin paths by setting environment variable 'MOTIONBUILDER_PLUGIN_PATH' before running MotionBuilder.

        return : the plugin path 
        """
        pass

    def GetPythonStartupPath(self):
        """
        Returns the python startup path.
        User could put python script in the startup folders, and MotionBuilder will search scripts from those folders and run them at startup. By default, there are two startup folders: /config/PythonStartup and /bin/config/PythonStartup. Users could append additional paths by setting environment variable 'MOTIONBUILDER_PYTHON_STARTUP' before launching application.

        return : the python startup path 
        """
        pass

    def MakeFullPath(self,pRelativeFilePath):
        """
        Return the full path.

        pRelativeFilePath : The relative file path 
        return : Full file path based on combining the current directory 
        """
        pass

    Cameras=property(doc="        ")
    Materials=property(doc="        ")
    Shaders=property(doc="        ")
    Textures=property(doc="        ")
    Takes=property(doc="        ")
    Lights=property(doc="        ")
    Devices=property(doc="        ")
    ApplicationPath=property(doc="<b>Read Only Property:</b> Location where the application is installed.          ")
    AreMessageBoxesSuspended=property(doc="<b>Read Only Property:</b> While true, the system is suspending the messages boxes that would normally be displayed.          ")
    AssetManager=property(doc="<b>Read Only Property:</b> Current asset manager.          ")
    AudioInputs=property(doc="<b>List:</b> Available audio inputs.          ")
    AudioOutputs=property(doc="<b>List:</b> Available audio outputs.          ")
    BuildId=property(doc="<b>Read Only Property:</b> Unique build Id string.          ")
    BuildVersion=property(doc="<b>Read Only Property:</b> Unique build version string. The format of the build version information is: Major.Minor.Revision.BuildNumber. All sub-parts of the build version string are containing only numeric characters.          ")
    ComputerName=property(doc="<b>Read Only Property:</b> Computer name. See sample: ShowMachineNameAndCameraNamePlusResolution.py.         ")
    ConfigPath=property(doc="        ")
    ConstructionHistory=property(doc="<b>Read Only Property:</b> Construction History.          ")
    CurrentTake=property(doc="<b>Read Write Property:</b> Current take. See samples: GoToNextTake.py,         ")
    DesktopSize=property(doc="<b>Read Only Property:</b> The width and height of the desktop.          ")
    FrameRate=property(doc="<b>Read Only Property:</b> The frame rate of the viewer.          ")
    FullScreenViewer=property(doc="<b>Read Write Property:</b> Indicates that the viewer is in full screen mode.          ")
    LocalTime=property(doc="<b>Read Only Property:</b> Local time in take.          ")
    Manipulators=property(doc="<b>List:</b> of manipulators.          ")
    OnConnectionDataNotify=property(doc="<b>Event:</b> A data event occurred between objects in the system.          ")
    OnConnectionKeyingNotify=property(doc="<b>Event:</b> A keying event occurred when objects are being keyed.          ")
    OnConnectionNotify=property(doc="<b>Event:</b> A connection event occurred between objects in the system. See sample: FBSystemEvents.py.         ")
    OnConnectionStateNotify=property(doc="<b>Event:</b> A state change event occurred between objects in the system.          ")
    OnUIIdle=property(doc="<b>Event:</b> User-interface idle event. Useful callback for less frequent GUI refresh and etc. lightweight tasks (occur once per several frames).          ")
    OnVideoFrameRendering=property(doc="<b>Event:</b> A video frame rendering event occurred when the scene is being off-line rendered into video files.          ")
    PathImages=property(doc="<b>Read Only Property:</b> Path to images.          ")
    PathMeshs=property(doc="<b>Read Only Property:</b> Path to meshes          ")
    ProcessMemory=property(doc="<b>Read Only Property:</b> The size (MB) of process's working set memory.          ")
    ProcessMemoryPeak=property(doc="<b>Read Only Property:</b> The size (MB) of process's peak memory.          ")
    PythonVersion=property(doc="<b>Read Only Property:</b> The Python interpreter version being used. The value is either 27 or 37.          ")
    Renderer=property(doc="<b>Read Only Property:</b> Default renderer.          ")
    RootModel=property(doc="<b>Read Only Property:</b> Root model.          ")
    Scene=property(doc="<b>Read Only Property:</b> Scene.          ")
    SceneRootModel=property(doc="<b>Read Only Property:</b> Scene root model.          ")
    SuspendMessageBoxes=property(doc="<b>Read Write Property:</b> While true, all the message boxes, that would normally be displayed, are suspended.          ")
    SystemTime=property(doc="<b>Read Only Property:</b> System time.          ")
    UserConfigPath=property(doc="        ")
    Version=property(doc="<b>Read Only Property:</b> Application version.          ")
    VideoInputs=property(doc="<b>List:</b> Available video inputs.          ")
    VideoOutputs=property(doc="<b>List:</b> Available video outputs.          ")
    pass

class FBTime (object):
    """
    Time data structure.     
    See samples: FBTime.py, CameraSwitcher.py, ExportAnimationLibrary.py, StartKeysAtCurrentTime.py.     
    """
    def FBTime(self,pTime):
        """
        pTime : long
        """
        pass

    def FBTime(self,pHour,pMinute,pSecond,pFrame,pField,pTimeMode):
        """
        Constructor.

        pHour : Hour value. 
        pMinute : Minute value. 
        pSecond : Second value. 
        pFrame : Frame value. 
        pField : Field value. 
        pTimeMode : Time mode(default=kFBTimeModeDefault). 
        """
        pass

    def Get(self):
        """
        Get time value (long)

        return : Time value as long. 
        """
        pass

    def Get(self):
        """
        Get time value (long)

        return : Time value as long. 
        """
        pass

    def GetFrame(self,pTimeMode):
        """
        Get the frame count.
        With this function, it is possible to obtain the cumulative and local frame counts.

        pTimeMode : Time mode to get the constant (default is kFBTimeModeDefault). 
        return : Frames per second constant for the specified time mode. 
        """
        pass

    def GetMilliSeconds(self):
        """
        Get milliseconds for time.

        return : MilliSeconds value. 
        """
        pass

    def GetSecondDouble(self):
        """
        Get seconds as double.

        return : Seconds in double form. 
        """
        pass

    def GetTimeString(self,pMode,pFormat):
        """
        Get time as a string.

        pMode : Time mode (default=kFBTimeModeDefault) to use (call FBSystem().GetTransportFps() to the the current UI displayed mode). 
        pFormat : Format to use for the returned string(default=FBTime::eDefaultFormat). 
        return : String value of time. 
        """
        pass

    def Set(self,pTime):
        """
        Set time value from a long.

        pTime : Time value to set. 
        """
        pass

    def SetFrame(self,pFrames,pTimeMode):
        """
        Set time in frame format.

        pFrames : The number of frames. 
        pTimeMode : The time mode identifier which will dictate the extraction algorithm. 
        """
        pass

    def SetMilliSeconds(self,pMilliSeconds):
        """
        Set milliseconds time.

        pMilliSeconds : MilliSeconds value. 
        """
        pass

    def SetSecondDouble(self,pTime):
        """
        Set seconds from double.

        pTime : Time to set seconds from. 
        """
        pass

    def SetTime(self,pHour,pMinute,pSecond,pFrame,pField,pTimeMode):
        """
        Set time (from separate values)

        pHour : Hour value. 
        pMinute : Minute value(default=0). 
        pSecond : Second value(default=0). 
        pFrame : Frame value(default=0). 
        pField : Field value(default=0). 
        pTimeMode : Time mode to get time as(default=kFBTimeModeDefault). 
        """
        pass

    def SetTimeString(self,pTime):
        """
        Set time from string.

        pTime : String to set time from. 
        """
        pass

    Infinity=property(doc="Time constant: Infinity, the largest time value.          ")
    MinusInfinity=property(doc="Time constant: Minus Infinity, the lowest negative time value.          ")
    OneHour=property(doc="Time constant: One Hour.          ")
    OneMinute=property(doc="Time constant: One Minute.          ")
    OneSecond=property(doc="Time constant: One Second.          ")
    Zero=property(doc="Time constant: Zero.          ")
    pass

class FBTimeCode (object):
    """
    TimeCode data structure.     
    See sample: TimeCodeKeying.py.     
    """
    def FBTimeCode(self,pRate):
        """
        Constructor.

        pRate : Framerate value. 
        """
        pass

    def GetRawFrame(self):
        """
        Get the raw value for the frame.

        return : raw value for the frame. 
        """
        pass

    def GetRawRate(self):
        """
        Get the raw value for the rate.

        return : raw value for the rate. 
        """
        pass

    def GetRawSecond(self):
        """
        Get the raw value for the second.

        return : raw value for the second. 
        """
        pass

    def GetTime(self):
        """
        Return a Time corresponding to the timecode.

        """
        pass

    def GetTimeCodeString(self,pFormat):
        """
        Get time as a string.

        pFormat : Format to use for the returned string(default=FBTime::eDefaultFormat). 
        return : String value of time. 
        """
        pass

    def SetTime(self,pTime):
        """
        Set TimeCode according to the given time.

        pTime : Time value to set. 
        """
        pass

    def SetTimeCode(self,pHour,pMinute,pSecond,pFrame):
        """
        Set timecode.

        pHour : Hour value. 
        pMinute : Minute value. 
        pSecond : Second value. 
        pFrame : Frame value. 
        """
        pass

    def SetTimeCodeString(self,pTime,pFormat):
        """
        Set time from string.

        pTime : String to set time from. 
        pFormat : Format to use for the string(default=FBTime::eDefaultFormat). 
        """
        pass

    FILM_23976=property(doc="-23.976f          ")
    FILM_24=property(doc="-24.0f          ")
    FRAMES_11988=property(doc="-119.88f          ")
    FRAMES_30=property(doc="-30.0f          ")
    FRAMES_5994=property(doc="-59.94f          ")
    MPAL_30=property(doc="-29.971f Currently not supported : '1' is added just to differentiate from NTSC_FULL(-29.97f)          ")
    NTSC_DROP=property(doc="Rates.          ")
    NTSC_FULL=property(doc="-29.97f          ")
    PAL_25=property(doc="-25.0f          ")
    pass

class FBTimeSpan (object):
    """
    TimeSpan class.     
         
    """
    def FBTimeSpan(self,pStart,pStop):
        """
        Constructor.

        pStart : Start time(default=0). 
        pStop : Stop time(default=0). 
        """
        pass

    def GetDirection(self):
        """
        Get the direction of the timespan.
        Returns 1 if positive, -1 otherwise.

        return : Direction of timespan. 
        """
        pass

    def GetDuration(self):
        """
        Get the unsigned duration value of a timespan.

        return : <b>Unsigned</b> duration of the timespan. 
        """
        pass

    def GetSignedDuration(self):
        """
        Get the signed duration value of a timespan.

        return : <b>Signed</b> duration of the timespan. 
        """
        pass

    def GetStart(self):
        """
        Get the start/stop time.

        return : Start/Stop time. 
        """
        pass

    def GetStart(self):
        """
        """
        pass

    def GetStop(self):
        """
        """
        pass

    def GetStop(self):
        """
        """
        pass

    def Set(self,pStart,pStop):
        """
        Set the TimeSpan.

        pStart : Start time. 
        pStop : Stop time. 
        """
        pass

    pass

class FBVector2d (object):
    """
    Vector2d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 2 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
# Supported list protocol methods:
color = FBColor()
len(color)
print color[0]
color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector2d(self):
        """
        Constructor.
        Default constructor, both values within are set to 0.0.

        """
        pass

    def FBVector2d(self,pVector2d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector2d : FBVector2d
        """
        pass

    def FBVector2d(self,pX,pY):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        """
        pass

    def FBVector2d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 2.

        p0 : tuple< float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBVector3d (object):
    """
    Vector3d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
# Supported list protocol methods:
color = FBColor()
len(color)
print color[0]
color[0] = 1.0
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector3d(self):
        """
        Constructor.
        Default constructor, all 3 values within are set to 0.0.

        """
        pass

    def FBVector3d(self,pVector3d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector3d : FBVector3d
        """
        pass

    def FBVector3d(self,pX,pY,pZ):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        pZ : float
        """
        pass

    def FBVector3d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 3.

        p0 : tuple< float, float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 2) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBVector4d (object):
    """
    Vector4d class.     
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
@code
# Supported list protocol methods:
color = FBColor()
len(color)
print color[0]
color[0] = 1.0    
@endcode

 Slicing is not supported by this object.     
    """
    def FBVector4d(self):
        """
        Constructor.
        Default constructor, all 4 values within are set to 0.0.

        """
        pass

    def FBVector4d(self,pVector4d):
        """
        Constructor.
        Copy constructor. Copy values from another instance.

        pVector4d : FBVector4d
        """
        pass

    def FBVector4d(self,pX,pY,pZ,pA):
        """
        Constructor.
        Explicitely construct a vector by specifying its values.

        pX : float
        pY : float
        pZ : float
        pA : float
        """
        pass

    def FBVector4d(self,p0):
        """
        Constructor.
        A vector can be built from any python object with supports the tuple interface and is of a lenght of 4.

        p0 : tuple< float, float, float, float >
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 3) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 3) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBVertex (object):
    """
    Vertex class.     
    Similar in use to FBVector4d 
@code
# Supported list protocol methods:
v = FBVertex()
len(v)
print v[0]
v[0] = 1.0
@endcode

Slicing is not supported by this object.     
    """
    def FBVertex(self):
        """
        """
        pass

    def FBVertex(self,p0):
        """
        p0 : FBVertex
        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    pass

class FBVideoCodecManager (object):
    """
    Video Codec manager class.     
     Use to set or get codec used and codec params See samples: codecExamples.py, render.py.     
    """
    def GetCodecIdList(self,pFileFormatInfo,pCodecList):
        """
        GetCodecIdList.
        Get all codec id available for a given file format.

        pFileFormatInfo : file format description string (AVI, MOV...) 
        pCodecList : Codec list id 
        """
        pass

    def GetDefaultCodec(self,pFileFormatInfo):
        """
        GetDefaultCodec.
        Get the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault

        pFileFormatInfo : file format description string (AVI, MOV...)  
        """
        pass

    def RegisterExternalVideoFormat(self,pFormatSuffix):
        """
        Register external video format suffix.
        Only alphabetic and number is allowed in provided suffix, and can not be empty suffix or the system exist suffixes. This will allow this suffix to be appeared in the filters of file dialog when importing video, also allow to create a texture/video object with a path containing this suffix via SDK. However it will the custom SDK plug-in developer's responsibility to load the file into memory.

        pFormatSuffix : Suffix/File extension of external video file format 
        return : true if register successful 
        """
        pass

    def SetDefaultCodec(self,pFileFormatInfo,pCodecId):
        """
        SetDefaultCodec.
        Set the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault

        pFileFormatInfo : file format description string (AVI, MOV...) 
        pCodecId : the codec id to set as default 
        """
        pass

    VideoCodecMode=property(doc="<b>Read Write Property:</b> This decide how the system behaves when ask to render a file (codec dialog, uncompress, use default codec)         ")
    pass

class FBVideoGrabOptions (object):
    """
    Video Grabbing Options.     
    Contain options to control how the grabbing process will occur.     
    """
    TimeSpan=property(doc="<b>Read Write Property:</b> Start and stop selection time to grab.         ")
    TimeSteps=property(doc="<b>Read Write Property:</b> Time step length between each grab.         ")
    CameraResolution=property(doc="<b>Read Write Property:</b> Camera Resolution.         ")
    BitsPerPixel=property(doc="<b>Read Write Property:</b> Video grab color depth.         ")
    FieldMode=property(doc="<b>Read Write Property:</b> Video grab field mode.         ")
    ViewingMode=property(doc="<b>Read Write Property:</b> Video grab viewing mode.         ")
    OutputFileName=property(doc="<b>Read Write Property:</b> Grabbing destination file.         ")
    ShowSafeArea=property(doc="<b>Read Write Property:</b> If true, display safe area.         ")
    ShowTimeCode=property(doc="<b>Read Write Property:</b> If true, display time code information.         ")
    ShowCameraLabel=property(doc="<b>Read Write Property:</b> If true, display camera label information.         ")
    AntiAliasing=property(doc="<b>Read Write Property:</b> If true, video frames will be anti-aliased.         ")
    RenderAudio=property(doc="<b>Read Write Property:</b> If true and there's audio in the scene, render the audio as well.         ")
    AudioRenderFormat=property(doc="<b>Read Write Property:</b> Audio render format.         ")
    StillImageCompression=property(doc="<b>Property:</b> Compression ratio for image(jpg) 0-100 where 0=Greatest compression, 100=Least Compression.         ")
    AudioOutputLocation=property(doc="Audio output location when rendering using a video format (for still image formats & SWF (Flash) format, the audio is always rendered in a standalone file).         ")
    AudioUseCustomStandaloneFileName=property(doc="If true and if the audio is rendered in a standalone output file, the audio file is generated at the file location specified by mAudioCustomStandaloneFileName, otherwise the audio file is generated in the same directory as the rendered images/video files based on their names.         ")
    AudioCustomStandaloneFileName=property(doc="Destination for the custom audio standalone file, if mAudioUseCustomStandaloneFileName is set to true.         ")
    pass

class FBViewingOptions (object):
    """
    Viewing options for rendering.     
     The FBRenderer allows to get and set those options.      
    """
    def IsInColorBufferPicking(self):
        """
        Is the rendering routine during picking status with GL color buffer method.

        """
        pass

    def IsInSelectionBufferPicking(self):
        """
        Is the rendering routine during picking status with GL selection buffer method.

        """
        pass

    def PaneIndex(self):
        """
        Current Viewer Pane being rendered.

        return : Index of the pane being rendered. 
        """
        pass

    def RenderCallbackPrefIndex(self):
        """
        Current Render callback Settings Index.

        """
        pass

    def StereoDisplayMode(self):
        """
        Get a reference to the stereo display mode.

        return : Reference to the current stereo display mode. 
        """
        pass

    DisplayMode=property(doc="<b>Read Write Property:</b> Current Shading mode         ")
    DisplayWhat=property(doc="<b>Read Write Property:</b> current display mask.         ")
    PickingMode=property(doc="<b>Read Write Property:</b> Reference to the current picking mode.         ")
    ShowTimeCode=property(doc="<b>Read Write Property:</b> Show Time Code when rendering.         ")
    ShowSafeArea=property(doc="<b>Read Write Property:</b> Show Safe Area when rendering.         ")
    ShowCameraLabel=property(doc="<b>Read Write Property:</b> Show Camera Label when rendering.         ")
    pass

class FBVisualComponent (object):
    """
    Visual Component base class.     
     All of the user interface elements available in the SDK derive from this class.      
    """
    def FBVisualComponent(self):
        """
        Constructor.

        """
        pass

    def AddChild(self,pChild,pId):
        """
        Add a child component.

        pChild : Visual component to add as a child. 
        pId : User reference number to associate with <b>pChild</b>(default=0). 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def GetChild(self,pId):
        """
        Get a child component.

        pId : User reference number to look for child with(default=0). 
        return : Handle to child (NULL if not found). 
        """
        pass

    def GetQWidgetAddress(self):
        """
        Get internal QWidget.

        return : Handle to internal QWidget object. 
        """
        pass

    def IsView(self):
        """
        Is component a view?

        return : <b>true</b> if component is a view. 
        """
        pass

    def Refresh(self,pNow):
        """
        Refresh component.

        pNow : Refresh immediately if <b>true</b> (default = <b>false</b>). 
        """
        pass

    def ViewExpose(self):
        """
        Exposed view callback function.

        """
        pass

    def ViewInput(self,pMouseX,pMouseY,pAction,pButtonKey,pModifier):
        """
        Input callback function.

        pMouseX : Mouse X position. 
        pMouseY : Mouse Y position. 
        pAction : Mouse action. 
        pButtonKey : Keyboard input. 
        pModifier : Keyboard input modifier. 
        """
        pass

    RegionName=property(doc="<b>Read Write Property:</b> Region name.         ")
    RegionOffsetX=property(doc="<b>Read Write Property:</b> Region X offset.         ")
    RegionOffsetY=property(doc="<b>Read Write Property:</b> Region Y offset.         ")
    RegionOffsetWidth=property(doc="<b>Read Write Property:</b> Region width offset.         ")
    RegionOffsetHeight=property(doc="<b>Read Write Property:</b> Region height offset.         ")
    RegionRatioX=property(doc="<b>Read Write Property:</b> Ratio for X attachment.         ")
    RegionRatioY=property(doc="<b>Read Write Property:</b> Ratio for Y attachment.         ")
    RegionRatioWidth=property(doc="<b>Read Write Property:</b> Ratio for Width attachment.         ")
    RegionRatioHeight=property(doc="<b>Read Write Property:</b> Ratio for Height attachment.          ")
    RegionAttachTypeX=property(doc="<b>Read Write Property:</b> X Attachment type.         ")
    RegionAttachTypeY=property(doc="<b>Read Write Property:</b> Y Attachment type.         ")
    RegionAttachTypeWidth=property(doc="<b>Read Write Property:</b> Width Attachment type.         ")
    RegionAttachTypeHeight=property(doc="<b>Read Write Property:</b> Height Attachment type.         ")
    RegionAttachToX=property(doc="<b>Read Write Property</b> X Attachment source.         ")
    RegionAttachToY=property(doc="<b>Read Write Property:</b> Y Attachment source.         ")
    RegionAttachToWidth=property(doc="<b>Read Write Property:</b> Width Attachment source.         ")
    RegionAttachToHeight=property(doc="<b>Read Write Property:</b> Height Attachment source.          ")
    RegionPosMaxX=property(doc="<b>Read Write Property:</b> Region X position Max         ")
    RegionPosMinX=property(doc="<b>Read Write Property:</b> Region X position Min         ")
    RegionPosMaxY=property(doc="<b>Read Write Property:</b> Region Y position Max         ")
    RegionPosMinY=property(doc="<b>Read Write Property:</b> Region Y position Min         ")
    BorderCaption=property(doc="<b>Read Write Property:</b> Caption to display in border.         ")
    BorderShowCaption=property(doc="<b>Read Write Property:</b> Show caption?         ")
    BorderStyle=property(doc="<b>Read Write Property:</b> Style of border.         ")
    BorderInSet=property(doc="<b>Read Write Property:</b> Is border inset?         ")
    BorderWidth=property(doc="<b>Read Write Property:</b> Width of border.         ")
    BorderSpacing=property(doc="<b>Read Write Property:</b> Spacing of border.         ")
    BorderMaxAngle=property(doc="<b>Read Write Property:</b> Max angle for rounding.         ")
    BorderCornerRadius=property(doc="<b>Read Write Property:</b> Corner radius (rounded).          ")
    Caption=property(doc="<b>Property:</b> Widget caption.          ")
    Enabled=property(doc="<b>Read Write Property:</b> Is visual enabled?          ")
    Height=property(doc="<b>Read Write Property:</b> Height.          ")
    Hint=property(doc="<b>Read Write Property:</b> Hint to show.          ")
    Left=property(doc="<b>Read Write Property:</b> Left coordinate.          ")
    ReadOnly=property(doc="<b>Read Write Property:</b> Is visual component read only?          ")
    Top=property(doc="<b>Read Write Property:</b> Top coordinate.          ")
    Visible=property(doc="<b>Read Write Property:</b> Is visual component visible?          ")
    Width=property(doc="<b>Read Write Property:</b> Width.          ")
    pass

class FBAccessMode (Enumeration):
    """
    pyfbsdk     
    Data access modes.      
    """
    kFBAccessModeDisk=property(doc="Access data directly to disk using a cache system.          ")
    kFBAccessModeMemory=property(doc="Access data from memory, which means that it will copyed entirely into it.          ")
    pass

class FBAlphaSource (Enumeration):
    """
    Shader transparency computation.     
     There are different way to compute transparency, and this lists the supported options.      
    """
    kFBAlphaSourceNoAlpha=property(doc="No transparency.          ")
    kFBAlphaSourceAccurateAlpha=property(doc="Accurate Transparency.          ")
    kFBAlphaSourceTransluscentAlpha=property(doc="Translucent.          ")
    kFBAlphaSourceMatteAlpha=property(doc="Matte.          ")
    kFBAlphaSource2DTransparency=property(doc="2D Transparency.          ")
    kFBAlphaSourceAdditiveAlpha=property(doc="Additive Transparency.          ")
    kFBAlphaSourceTransluscentZSortAlpha=property(doc="Translucent(Models Z Sort).          ")
    pass

class FBAnimationLayerMergeOptions (Enumeration):
    """
    Merge option for animation layers.     
         
    """
    kFBAnimLayerMerge_SelectedLayers_SelectedProperties=property(doc="Merge the animation of the selected properties of the selected models from the selected layers to the selected layer with the lowest index.          ")
    kFBAnimLayerMerge_AllLayers_SelectedProperties=property(doc="Merge the animation of the selected properties of the selected models from all the layers to the BaseAnimation layer.          ")
    kFBAnimLayerMerge_SelectedLayers_AllProperties=property(doc="Merge the animation of all properties of the selected models from the selected layers to the selected layer with the lowest index.          ")
    kFBAnimLayerMerge_AllLayers_AllProperties=property(doc="Merge the animation of all properties of the selected models from all the layers to the BaseAnimation layer.          ")
    kFBAnimLayerMerge_SelectedLayers_CompleteScene=property(doc="Merge the animation of all properties from the selected layers to the selected layer with the lowest index.          ")
    kFBAnimLayerMerge_AllLayers_CompleteScene=property(doc="Merge the animation of all properties from all the layers to the BaseAnimation layer.          ")
    pass

class FBAnimationNodeConnectorType (Enumeration):
    """
    Different types for the animation node connectors.     
         
    """
    kFBAnimationNodeConnectorTypeNone=property(doc="The animation node connector is not connected and doesn't have a constant value set to it.          ")
    kFBAnimationNodeConnectorTypeConnectedIn=property(doc="The animation node input connector is connected to an animation node output connector (valid for input connector only).          ")
    kFBAnimationNodeConnectorTypeConnectedOut=property(doc="The animation node output connector is connected to at least one animation node input connector (valid for output connector only).          ")
    kFBAnimationNodeConnectorTypeConstantIn=property(doc="The animation node input connector has a constant value set to it (valid for input connector only).          ")
    pass

class FBArrangeMode (Enumeration):
    """
    Modes for arranging objects in schematic view.     
         
    """
    kHorizontalMode=property(doc="Arrange all objects horizontally.          ")
    kVerticalMode=property(doc="Arrange all objects vertically.          ")
    pass

class FBArrowButton (FBVisualComponent):
    """
    Creates a button which opens a layout to display content.     
     When pushed a layout to display content (another control or a layout) is opened. A small arrow to the left of the button title, shows whether the content is shown (points down) or not (points to the title). See samples: ArrowButton.py, FBCamera.py.     
    """
    def FBArrowButton(self):
        """
        Constructor.

        """
        pass

    def SetContent(self,pTitle,pContent,pContentWidth,pContentHeight):
        """
        Sets the content to be hidden/shown by button.
        The FBArrowButton must already have been added to a layout before calling this method.

        pTitle : Title of the content managed by the FBArrowButton 
        pContent : Content that the FBArrowButton displays or hides 
        pContentWidth : Width of the content 
        pContentHeight : Height of the content 
        """
        pass

    pass

class FBAssetMngFileOptions (Enumeration):
    """
    Behavior of the application when working with managed files.     
         
    """
    kFileCheckOutOnLoad=property(doc="Check out file automatically on load.          ")
    kFileCheckOutOnLoad_Ask=property(doc="Ask for checkout on load.          ")
    kFileUploadOnSave=property(doc="Upload file automatically on save.          ")
    kFileUploadOnSave_Ask=property(doc="Ask for upload on save.          ")
    kFileAddOnNewSave=property(doc="Add new file automatically on save.          ")
    kFileAddOnNewSave_Ask=property(doc="Ask for adding new file on save.          ")
    kFileCheckInOnClose=property(doc="Check in file automatically when closing it.          ")
    kFileCheckInOnClose_Ask=property(doc="Ask for check in file when closing it.          ")
    kFileOptionsAll=property(doc="        ")
    pass

class FBAssetMngMenuOptions (Enumeration):
    """
    Show or hide version control menu items.     
     Let you specify which functionalities will be available from the menus.      
    """
    kMenuOpenFromDatabase=property(doc="File -> Open from database.          ")
    kMenuAddToDatabase=property(doc="File -> Add to database.          ")
    kMenuUploadToDatabase=property(doc="File -> Upload to database.          ")
    kMenuGetLatest=property(doc="Version Control -> Get Latest.          ")
    kMenuCheckIn=property(doc="Version Control -> Check In.          ")
    kMenuCheckOut=property(doc="Version Control -> Check Out.          ")
    kMenuUndoCheckOut=property(doc="Version Control -> Undo Check Out.          ")
    kMenuShowHistory=property(doc="Version Control -> Show History.          ")
    kMenuShowProperties=property(doc="Version Control -> Show Properties.          ")
    kMenuShowExplorer=property(doc="Version Control -> Show Explorer.          ")
    kMenuShowReferenceMng=property(doc="Version Control -> Show Reference Manager.          ")
    kMenuShowSettings=property(doc="Version Control -> Show Settings.          ")
    kMenuEnable=property(doc="Version Control -> Disable Version Control Integration.          ")
    kMenuFileAll=property(doc="Support all elements from the File menu.          ")
    kMenuSourceControlAll=property(doc="Support all elements from the Version Control menu.          ")
    kMenuSourceControlMin=property(doc="Support only the basics functionalities.          ")
    kMenuAll=property(doc="Support everything.          ")
    pass

class FBAttachType (Enumeration):
    """
    Types of attachments between UI regions.     
    See samples: Attach.py, BoxLayout.py, RadioButton.py.     
    """
    kFBAttachLeft=property(doc="Attach to left [min(x1,x2)]          ")
    kFBAttachRight=property(doc="Attach to right [max(x1,x2)]          ")
    kFBAttachTop=property(doc="Attach to top [min(y1,y2)]          ")
    kFBAttachBottom=property(doc="Attach to bottom [max(y1,y2)]          ")
    kFBAttachWidth=property(doc="Attach to width [abs(x2-x1)]          ")
    kFBAttachHeight=property(doc="Attach to height [abs(y2-y1)]          ")
    kFBAttachCenter=property(doc="Attach to center [center(x1,y1,x2,y2)]          ")
    kFBAttachNone=property(doc="No attachment.          ")
    pass

class FBAttenuationType (Enumeration):
    """
    Light attenuation types.     
         
    """
    kFBAttenuationNone=property(doc="No attenuation.          ")
    kFBAttenuationLinear=property(doc="Linear attenuation.          ")
    kFBAttenuationQuadratic=property(doc="Quadratic attenuation.          ")
    kFBAttenuationCubic=property(doc="Cubic attenuation.          ")
    pass

class FBAudioBitDepthMode (Enumeration):
    """
    Enum FBAudioBitDepthMode.     
         
    """
    kFBAudioBitDepthMode_8=property(doc="8 bits, Wave file render support.          ")
    kFBAudioBitDepthMode_16=property(doc="16 bits, Wave file render support.          ")
    kFBAudioBitDepthMode_24=property(doc="24 bits, Wave file render support.          ")
    kFBAudioBitDepthMode_FP=property(doc="FP type audio, Wave file render not support.          ")
    pass

class FBAudioChannelMode (Enumeration):
    """
    Enum FBAudioChannelMode.     
         
    """
    kFBAudioChannelModeMono=property(doc="1 channel, Wave file render support.          ")
    kFBAudioChannelModeStereo=property(doc="2 channels, Wave file render support.          ")
    kFBAudioChannelMode_4=property(doc="4 channels, Wave file render not support.          ")
    kFBAudioChannelMode_8=property(doc="8 channels, Wave file render not support.          ")
    pass

class FBAudioOutputLocation (Enumeration):
    """
    Type of locations where the audio is rendered when rendering a scene using a video format.     
         
    """
    FBAudioOutputLocationEmbedded=property(doc="The audio is embedded within the video output file.          ")
    FBAudioOutputLocationStandalone=property(doc="The audio is rendered in a standalone output file.          ")
    FBAudioOutputLocationEmbeddedAndStandalone=property(doc="The audio is embedded within the video output file and is also rendered in a standalone output file.          ")
    FBAudioOutputLocationCount=property(doc="Count.          ")
    pass

class FBAudioRateMode (Enumeration):
    """
    Enum FBAudioRateMode.     
         
    """
    kFBAudioRateMode_8000=property(doc="8000 hz, Wave file render support.          ")
    kFBRAudioateMode_11025=property(doc="11025 hz, Wave file render support.          ")
    kFBAudioRateMode_12000=property(doc="12000 hz, Wave file render support.          ")
    kFBAudioRateMode_12500=property(doc="12500 hz, Wave file render not support.          ")
    kFBAudioRateMode_16000=property(doc="16000 hz, Wave file render support.          ")
    kFBAudioRateMode_22050=property(doc="22050 hz, Wave file render support.          ")
    kFBAudioRateMode_24000=property(doc="24000 hz, Wave file render support.          ")
    kFBAudioRateMode_25000=property(doc="25000 hz, Wave file render not support.          ")
    kFBAudioRateMode_32000=property(doc="32000 hz, Wave file render support.          ")
    kFBAudioRateMode_44100=property(doc="44100 hz, Wave file render support.          ")
    kFBAudioRateMode_48000=property(doc="48000 hz, Wave file render support.          ")
    kFBAudioRateMode_50000=property(doc="50000 hz, Wave file render not support.          ")
    kFBAudioRateMode_64000=property(doc="64000 hz, Wave file render support.          ")
    kFBAudioRateMode_88200=property(doc="88200 hz, Wave file render support.          ")
    kFBAudioRateMode_96000=property(doc="96000 hz, Wave file render support.          ")
    kFBAudioRateMode_100000=property(doc="100000 hz, Wave file render not support.          ")
    pass

class FBBatchFileFormat (Enumeration):
    """
    Different file formats for the batch.     
         
    """
    kFBBatchFileFormatTRC=property(doc="File format for Motion Analysis TRC.          ")
    kFBBatchFileFormatC3D=property(doc="File format for Vicon C3D.          ")
    kFBBatchFileFormatAMC=property(doc="File format for Acclaim AMC.          ")
    kFBBatchFileFormatBVH=property(doc="File format for Biovision BVH.          ")
    kFBBatchFileFormatHTR=property(doc="File format for Motion Analysis HTR.          ")
    kFBBatchFileFormatFBX=property(doc="File format for FBX (animation only).          ")
    pass

class FBBatchOnContainsBatchTakes (Enumeration):
    """
    Different actions to perform when a scene already contains batch takes while in a batch process.     
         
    """
    kFBBatchOnContainsBatchTakesSaveBatchTakesOnly=property(doc="Save only the batch takes.          ")
    kFBBatchOnContainsBatchTakesSaveAllTakes=property(doc="Save all the takes.          ")
    pass

class FBBatchOnTakeExist (Enumeration):
    """
    Different actions to perform when a take already exist while in a batch process.     
         
    """
    kFBBatchOnTakeExistOverwrite=property(doc="Overwrite the take.          ")
    kFBBatchOnTakeExistSkip=property(doc="Skip the take.          ")
    pass

class FBBatchProcessType (Enumeration):
    """
    Different process type for the batch.     
         
    """
    kFBBatchProcessTypeLoad=property(doc="Load the files and plot the character with every take.          ")
    kFBBatchProcessTypeSave=property(doc="Save the takes in different files.          ")
    kFBBatchProcessTypeConvert=property(doc="Does the load and save.          ")
    pass

class FBBatchStatus (Enumeration):
    """
    Different return values of the Batch process.     
         
    """
    kFBBatchStatusSuccess=property(doc="        ")
    kFBBatchStatusError=property(doc="        ")
    kFBBatchStatusCharacterNotSpecified=property(doc="        ")
    kFBBatchStatusCharacterNotCharacterized=property(doc="        ")
    kFBBatchStatusCharacterHasNoReference=property(doc="        ")
    kFBBatchStatusInputActorNotSpecified=property(doc="        ")
    kFBBatchStatusActorInputMarkersetNotSpecified=property(doc="        ")
    kFBBatchStatusActorInputMarkersetHasNoReferenceModel=property(doc="        ")
    kFBBatchStatusActorInputMarkersetNotCorrectlyAssociated=property(doc="        ")
    kFBBatchStatusInputCharacterNotCharacterized=property(doc="        ")
    kFBBatchStatusInputCharacterHasNoReference=property(doc="        ")
    kFBBatchStatusInputDirectoryNotValid=property(doc="        ")
    kFBBatchStatusAsfSkeletonFileNotSpecified=property(doc="        ")
    kFBBatchStatusCantOpenAsfSkeletonFile=property(doc="        ")
    kFBBatchStatusOutputDirectoryNotValid=property(doc="        ")
    pass

class FBBodyNodeId (Enumeration):
    """
    All body nodes.     
    See sample: ExportAnimationLibrary.py.     
    """
    kFBInvalidNodeId=property(doc="        ")
    kFBHipsNodeId=property(doc="Required.          ")
    kFBLeftHipNodeId=property(doc="Required.          ")
    kFBLeftKneeNodeId=property(doc="Required.          ")
    kFBLeftAnkleNodeId=property(doc="Required.          ")
    kFBLeftFootNodeId=property(doc="        ")
    kFBRightHipNodeId=property(doc="Required.          ")
    kFBRightKneeNodeId=property(doc="Required.          ")
    kFBRightAnkleNodeId=property(doc="Required.          ")
    kFBRightFootNodeId=property(doc="        ")
    kFBWaistNodeId=property(doc="Required, Spine 0.          ")
    kFBChestNodeId=property(doc="Spine 1.          ")
    kFBLeftCollarNodeId=property(doc="        ")
    kFBLeftShoulderNodeId=property(doc="Required.          ")
    kFBLeftElbowNodeId=property(doc="Required.          ")
    kFBLeftWristNodeId=property(doc="Required.          ")
    kFBRightCollarNodeId=property(doc="        ")
    kFBRightShoulderNodeId=property(doc="Required.          ")
    kFBRightElbowNodeId=property(doc="Required.          ")
    kFBRightWristNodeId=property(doc="Required.          ")
    kFBNeckNodeId=property(doc="        ")
    kFBHeadNodeId=property(doc="Required.          ")
    kFBLeftHipRollNodeId=property(doc="        ")
    kFBLeftKneeRollNodeId=property(doc="        ")
    kFBRightHipRollNodeId=property(doc="        ")
    kFBRightKneeRollNodeId=property(doc="        ")
    kFBLeftShoulderRollNodeId=property(doc="        ")
    kFBLeftElbowRollNodeId=property(doc="        ")
    kFBRightShoulderRollNodeId=property(doc="        ")
    kFBRightElbowRollNodeId=property(doc="        ")
    kFBSpine2NodeId=property(doc="        ")
    kFBSpine3NodeId=property(doc="        ")
    kFBSpine4NodeId=property(doc="        ")
    kFBSpine5NodeId=property(doc="        ")
    kFBSpine6NodeId=property(doc="        ")
    kFBSpine7NodeId=property(doc="        ")
    kFBSpine8NodeId=property(doc="        ")
    kFBSpine9NodeId=property(doc="        ")
    kFBLeftThumbANodeId=property(doc="        ")
    kFBLeftThumbBNodeId=property(doc="        ")
    kFBLeftThumbCNodeId=property(doc="        ")
    kFBLeftIndexANodeId=property(doc="        ")
    kFBLeftIndexBNodeId=property(doc="        ")
    kFBLeftIndexCNodeId=property(doc="        ")
    kFBLeftMiddleANodeId=property(doc="        ")
    kFBLeftMiddleBNodeId=property(doc="        ")
    kFBLeftMiddleCNodeId=property(doc="        ")
    kFBLeftRingANodeId=property(doc="        ")
    kFBLeftRingBNodeId=property(doc="        ")
    kFBLeftRingCNodeId=property(doc="        ")
    kFBLeftPinkyANodeId=property(doc="        ")
    kFBLeftPinkyBNodeId=property(doc="        ")
    kFBLeftPinkyCNodeId=property(doc="        ")
    kFBRightThumbANodeId=property(doc="        ")
    kFBRightThumbBNodeId=property(doc="        ")
    kFBRightThumbCNodeId=property(doc="        ")
    kFBRightIndexANodeId=property(doc="        ")
    kFBRightIndexBNodeId=property(doc="        ")
    kFBRightIndexCNodeId=property(doc="        ")
    kFBRightMiddleANodeId=property(doc="        ")
    kFBRightMiddleBNodeId=property(doc="        ")
    kFBRightMiddleCNodeId=property(doc="        ")
    kFBRightRingANodeId=property(doc="        ")
    kFBRightRingBNodeId=property(doc="        ")
    kFBRightRingCNodeId=property(doc="        ")
    kFBRightPinkyANodeId=property(doc="        ")
    kFBRightPinkyBNodeId=property(doc="        ")
    kFBRightPinkyCNodeId=property(doc="        ")
    kFBReferenceNodeId=property(doc="        ")
    kFBLeftThumbInNodeId=property(doc="        ")
    kFBLeftThumbDNodeId=property(doc="        ")
    kFBLeftIndexInNodeId=property(doc="        ")
    kFBLeftIndexDNodeId=property(doc="        ")
    kFBLeftMiddleInNodeId=property(doc="        ")
    kFBLeftMiddleDNodeId=property(doc="        ")
    kFBLeftRingInNodeId=property(doc="        ")
    kFBLeftRingDNodeId=property(doc="        ")
    kFBLeftPinkyInNodeId=property(doc="        ")
    kFBLeftPinkyDNodeId=property(doc="        ")
    kFBRightThumbInNodeId=property(doc="        ")
    kFBRightThumbDNodeId=property(doc="        ")
    kFBRightIndexInNodeId=property(doc="        ")
    kFBRightIndexDNodeId=property(doc="        ")
    kFBRightMiddleInNodeId=property(doc="        ")
    kFBRightMiddleDNodeId=property(doc="        ")
    kFBRightRingInNodeId=property(doc="        ")
    kFBRightRingDNodeId=property(doc="        ")
    kFBRightPinkyInNodeId=property(doc="        ")
    kFBRightPinkyDNodeId=property(doc="        ")
    kFBLeftExtraFingerInNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFingerANodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFingerBNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFingerCNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFingerDNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFingerInNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFingerANodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFingerBNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFingerCNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFingerDNodeId=property(doc="New extra finger bone.          ")
    kFBLeftFootThumbInNodeId=property(doc="        ")
    kFBLeftFootThumbANodeId=property(doc="        ")
    kFBLeftFootThumbBNodeId=property(doc="        ")
    kFBLeftFootThumbCNodeId=property(doc="        ")
    kFBLeftFootThumbDNodeId=property(doc="        ")
    kFBLeftFootIndexInNodeId=property(doc="        ")
    kFBLeftFootIndexANodeId=property(doc="        ")
    kFBLeftFootIndexBNodeId=property(doc="        ")
    kFBLeftFootIndexCNodeId=property(doc="        ")
    kFBLeftFootIndexDNodeId=property(doc="        ")
    kFBLeftFootMiddleInNodeId=property(doc="        ")
    kFBLeftFootMiddleANodeId=property(doc="        ")
    kFBLeftFootMiddleBNodeId=property(doc="        ")
    kFBLeftFootMiddleCNodeId=property(doc="        ")
    kFBLeftFootMiddleDNodeId=property(doc="        ")
    kFBLeftFootRingInNodeId=property(doc="        ")
    kFBLeftFootRingANodeId=property(doc="        ")
    kFBLeftFootRingBNodeId=property(doc="        ")
    kFBLeftFootRingCNodeId=property(doc="        ")
    kFBLeftFootRingDNodeId=property(doc="        ")
    kFBLeftFootPinkyInNodeId=property(doc="        ")
    kFBLeftFootPinkyANodeId=property(doc="        ")
    kFBLeftFootPinkyBNodeId=property(doc="        ")
    kFBLeftFootPinkyCNodeId=property(doc="        ")
    kFBLeftFootPinkyDNodeId=property(doc="        ")
    kFBRightFootThumbInNodeId=property(doc="        ")
    kFBRightFootThumbANodeId=property(doc="        ")
    kFBRightFootThumbBNodeId=property(doc="        ")
    kFBRightFootThumbCNodeId=property(doc="        ")
    kFBRightFootThumbDNodeId=property(doc="        ")
    kFBRightFootIndexInNodeId=property(doc="        ")
    kFBRightFootIndexANodeId=property(doc="        ")
    kFBRightFootIndexBNodeId=property(doc="        ")
    kFBRightFootIndexCNodeId=property(doc="        ")
    kFBRightFootIndexDNodeId=property(doc="        ")
    kFBRightFootMiddleInNodeId=property(doc="        ")
    kFBRightFootMiddleANodeId=property(doc="        ")
    kFBRightFootMiddleBNodeId=property(doc="        ")
    kFBRightFootMiddleCNodeId=property(doc="        ")
    kFBRightFootMiddleDNodeId=property(doc="        ")
    kFBRightFootRingInNodeId=property(doc="        ")
    kFBRightFootRingANodeId=property(doc="        ")
    kFBRightFootRingBNodeId=property(doc="        ")
    kFBRightFootRingCNodeId=property(doc="        ")
    kFBRightFootRingDNodeId=property(doc="        ")
    kFBRightFootPinkyInNodeId=property(doc="        ")
    kFBRightFootPinkyANodeId=property(doc="        ")
    kFBRightFootPinkyBNodeId=property(doc="        ")
    kFBRightFootPinkyCNodeId=property(doc="        ")
    kFBRightFootPinkyDNodeId=property(doc="        ")
    kFBLeftExtraFootFingerInNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFootFingerANodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFootFingerBNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFootFingerCNodeId=property(doc="New extra finger bone.          ")
    kFBLeftExtraFootFingerDNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFootFingerInNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFootFingerANodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFootFingerBNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFootFingerCNodeId=property(doc="New extra finger bone.          ")
    kFBRightExtraFootFingerDNodeId=property(doc="New extra finger bone.          ")
    kFBLeftHandNodeId=property(doc="        ")
    kFBRightHandNodeId=property(doc="        ")
    kFBNeck1NodeId=property(doc="        ")
    kFBNeck2NodeId=property(doc="        ")
    kFBNeck3NodeId=property(doc="        ")
    kFBNeck4NodeId=property(doc="        ")
    kFBNeck5NodeId=property(doc="        ")
    kFBNeck6NodeId=property(doc="        ")
    kFBNeck7NodeId=property(doc="        ")
    kFBNeck8NodeId=property(doc="        ")
    kFBNeck9NodeId=property(doc="        ")
    kFBHipsTranslationNodeId=property(doc="        ")
    kFBLastNodeId_Old=property(doc="        ")
    kFBLeftHipRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBLeftKneeRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBRightHipRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBRightKneeRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBLeftShoulderRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBLeftElbowRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBRightShoulderRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBRightElbowRollNode1Id=property(doc="New leaf roll bone.          ")
    kFBLeftHipRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBLeftKneeRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBRightHipRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBRightKneeRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBLeftShoulderRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBLeftElbowRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBRightShoulderRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBRightElbowRollNode2Id=property(doc="New leaf roll bone.          ")
    kFBLeftHipRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBLeftKneeRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBRightHipRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBRightKneeRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBLeftShoulderRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBLeftElbowRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBRightShoulderRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBRightElbowRollNode3Id=property(doc="New leaf roll bone.          ")
    kFBLeftHipRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBLeftKneeRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBRightHipRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBRightKneeRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBLeftShoulderRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBLeftElbowRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBRightShoulderRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBRightElbowRollNode4Id=property(doc="New leaf roll bone.          ")
    kFBLeftHipRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBLeftKneeRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBRightHipRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBRightKneeRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBLeftShoulderRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBLeftElbowRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBRightShoulderRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBRightElbowRollNode5Id=property(doc="New leaf roll bone.          ")
    kFBLastNodeId=property(doc="        ")
    pass

class FBBodyPartId (Enumeration):
    """
    Body part for character.     
         
    """
    kFBCtrlSetPartNone=property(doc="No part selected.          ")
    kFBCtrlSetPartHips=property(doc="Hips Body Part.          ")
    kFBCtrlSetPartChest=property(doc="Chest Body Part.          ")
    kFBCtrlSetPartLeftArm=property(doc="Left Arm Body Part.          ")
    kFBCtrlSetPartRightArm=property(doc="Right Arm Body Part.          ")
    kFBCtrlSetPartLeftLeg=property(doc="Left Leg Body Part.          ")
    kFBCtrlSetPartRightLeg=property(doc="Right Leg Body Part.          ")
    kFBCtrlSetPartHead=property(doc="Head Body Part.          ")
    kFBCtrlSetPartLeftHand=property(doc="Left Hand Body Part.          ")
    kFBCtrlSetPartRightHand=property(doc="Right Hand Body Part.          ")
    kFBCtrlSetPartLeftFoot=property(doc="Left Foot Body Part.          ")
    kFBCtrlSetPartRightFoot=property(doc="Right Foot Body Part.          ")
    kFBLastCtrlSetPartIndex=property(doc="Part count.          ")
    pass

class FBBorderStyle (Enumeration):
    """
    Different border types available.     
    See samples: Border.py, TabPanel.py.     
    """
    kFBNoBorder=property(doc="No border.          ")
    kFBStandardBorder=property(doc="Standard border.          ")
    kFBEmbossBorder=property(doc="Embossed border.          ")
    kFBEmbossSmoothBorder=property(doc="Smooth border.          ")
    kFBEmbossEdgeSmoothBorder=property(doc="Edged smooth border.          ")
    kFBEmbossSmoothEdgeBorder=property(doc="Smoothed edges border.          ")
    kFBStandardSmoothBorder=property(doc="Standard smooth border.          ")
    kFBStandardEdgeSmoothBorder=property(doc="Standard edged smooth border.          ")
    kFBStandardSmoothEdgeBorder=property(doc="Standard smoothed edges border.          ")
    kFBHighlightBorder=property(doc="Highlight border.          ")
    kFBPickingBorder=property(doc="Picking border.          ")
    pass

class FBBrowsingProperty (FBVisualComponent):
    """
    Property browsing.     
    See sample: BrowsingProperty.py.     
    """
    def FBBrowsingProperty(self):
        """
        Constructor.

        """
        pass

    def AddObject(self,pObject):
        """
        Add an object whose properties will be displayed.

        pObject : Object whose properties will be displayed in the property brwoser. 
        """
        pass

    def ObjectGet(self,pIndex):
        """
        Return the object at the specified index.

        pIndex : Index of the object to get. 
        return : Object at the index specified currently displayed in the property browser. 
        """
        pass

    def ObjectGetCount(self):
        """
        Get the number of object displayed in the property browser.

        return : Object currently displayed in the property browser. 
        """
        pass

    def RemoveObject(self,pObject):
        """
        Remove an object from the property browser.

        pObject : Object to remove. 
        """
        pass

    pass

class FBButton (FBVisualComponent):
    """
    Used to create and manage buttons in a user interface.     
     This class includes functionality to create buttons in a user interface and add a callback. In MotionBuilder, buttons are created within regions, which are in turn created in layouts with FBLayout. For usage, see the Python sample Button.py. See also: FBButtonStyle, FBTextJustify, FBButtonLook. See samples: Button.py, Popup.py, RadioButton.py.     
    """
    def FBButton(self):
        """
        Constructor.

        """
        pass

    def GetStateColor(self,pState):
        """
        Queries the color associated with a button state.
        This method is only useful for buttons of style kFB2States.

        pState : The state to be queried. 
        return : The color vector. 
        """
        pass

    def SetImageFileNames(self,pUpImage,pDownImage,pThirdImage,pFromResources):
        """
        Sets the image used to generate a kFBBitmap2States.

        pUpImage : The image used when button is unpushed 
        pDownImage : The image used when button is pushed 
        pThirdImage : str
        pFromResources : Add resource path to image path. 
        """
        pass

    def SetStateColor(self,pState,pColor):
        """
        Returns whether or not the item <b>pIndex</b> is currently selected.

        pState : The state to be set. 
        pColor : The desired color vector. 
        """
        pass

    Justify=property(doc="<b>Read Write Property:</b> Current state of button.          ")
    Look=property(doc="<b>Read Write Property:</b> Current state of button.          ")
    OnClick=property(doc="<b>Event:</b> Button clicked.          ")
    State=property(doc="<b>Read Write Property:</b> Current state of button.          ")
    Style=property(doc="<b>Read Write Property:</b> Button style.          ")
    pass

class FBButtonLook (Enumeration):
    """
    Button look.     
    See sample: Button.py.     
    """
    kFBLookNormal=property(doc="        ")
    kFBLookColorChange=property(doc="        ")
    kFBLookPush=property(doc="        ")
    kFBLookFlat=property(doc="        ")
    kFBLookAlphaBackground=property(doc="        ")
    pass

class FBButtonState (Enumeration):
    """
    Possible button states.     
     Currently, only two button states are possible.      
    """
    kFBButtonState0=property(doc="State is 0, usually meaning not active.          ")
    kFBButtonState1=property(doc="State is 1, usually meaning active.          ")
    pass

class FBButtonStyle (Enumeration):
    """
    Style of buttons.     
     Not all button styles are completely functional. See samples: Button.py, RadioButton.py.     
    """
    kFBPushButton=property(doc="Normal button.          ")
    kFBBitmapButton=property(doc="Button with bitmap on it.          ")
    kFBRadioButton=property(doc="Radio button.          ")
    kFB2States=property(doc="2 state button (2 colors).          ")
    kFBCheckbox=property(doc="Check box.          ")
    kFBBitmap2States=property(doc="2 state button with 2 bitmaps.          ")
    pass

class FBCameraAntiAliasingMethod (Enumeration):
    """
    Antialiasing methods.     
         
    """
    kFBAntiAliasingSoftware=property(doc="Antaliasing in software.          ")
    kFBAntialiasingMultiSamplingOnyx=property(doc="Multisampling (only on Onyx).          ")
    pass

class FBCameraApertureMode (Enumeration):
    """
    Aperture modes.     
         
    """
    kFBApertureVertical=property(doc="Vertical aperture varies.          ")
    kFBApertureHorizontal=property(doc="Horizontal aperture varies.          ")
    kFBApertureVertHoriz=property(doc="Vertical and horizontal aperture varies.          ")
    kFBApertureFocalLength=property(doc="Focal Length aperture varies.          ")
    pass

class FBCameraDistanceMode (Enumeration):
    """
    Camera plane distance modes.     
         
    """
    kFBDistModeRelativeToInterest=property(doc="Camera plane distance relative to interest.          ")
    kFBDistModeAbsoluteFromCamera=property(doc="Camera plane distance absolute from camera.          ")
    pass

class FBCameraFilmBackType (Enumeration):
    """
    Filmback types.     
         
    """
    kFBFilmBackCustom=property(doc="Custom Filmback.          ")
    kFBFilmBack16mmTheatrical=property(doc="16mm Theatrical.          ")
    kFBFilmBackSuper16mm=property(doc="Super16mm.          ")
    kFBFilmBack35mmAcademy=property(doc="35mm Academy.          ")
    kFBFilmBack35mmTVProjection=property(doc="35mm TV Projection.          ")
    kFBFilmBack35mmFullAperture=property(doc="35mm Full Aperture.          ")
    kFBFilmBack35mm185Projection=property(doc="35mm 185 Projection.          ")
    kFBFilmBack35mmAnamorphic=property(doc="35mm Anamorphic.          ")
    kFBFilmBack70mmProjection=property(doc="70mm Projection.          ")
    kFBFilmBackVistaVision=property(doc="Vista Vision.          ")
    kFBFilmBackDynavision=property(doc="Dynavision.          ")
    kFBFilmBackIMAX=property(doc="IMAX.          ")
    pass

class FBCameraFocusDistanceSource (Enumeration):
    """
    Focus distance sources.     
         
    """
    kFBFocusDistanceCameraInterest=property(doc="Interest as source.          ")
    kFBFocusDistanceSpecificDistance=property(doc="Specific distance as source.          ")
    kFBFocusDistanceModel=property(doc="Another model's position as source.          ")
    pass

class FBCameraFrameSizeMode (Enumeration):
    """
    Frame size modes.     
         
    """
    kFBFrameSizeWindow=property(doc="Frame size of window.          ")
    kFBFrameSizeFixedRatio=property(doc="Fixed ratio.          ")
    kFBFrameSizeFixedResolution=property(doc="Fixed resolution.          ")
    kFBFrameSizeFixedWidthResolution=property(doc="Fixed width resolution.          ")
    kFBFrameSizeFixedHeightResolution=property(doc="Fixed height resolution.          ")
    pass

class FBCameraMatrixType (Enumeration):
    """
    Camera matrix types in OpenGL convention.     
         
    """
    kFBProjection=property(doc="Camera's Projection matrix.          ")
    kFBModelView=property(doc="Camera's combined Model-View matrix.          ")
    kFBModelViewProj=property(doc="Camera's combined Model-View-Projection matrix.          ")
    kFBProjInverse=property(doc="Camera's Projection Inverse matrix.          ")
    pass

class FBCameraResolutionMode (Enumeration):
    """
    Resolution modes.     
         
    """
    kFBResolutionCustom=property(doc="Custom resolution mode or From Camera as a render setting.          ")
    kFBResolutionD1NTSC=property(doc="D1 NTSC.          ")
    kFBResolutionNTSC=property(doc="NTSC.          ")
    kFBResolutionPAL=property(doc="PAL.          ")
    kFBResolutionD1PAL=property(doc="D1 PAL.          ")
    kFBResolutionHD=property(doc="HD 1920x1080.          ")
    kFBResolution640x480=property(doc="640x480.          ")
    kFBResolution320x200=property(doc="320x200.          ")
    kFBResolution320x240=property(doc="320x240.          ")
    kFBResolution128x128=property(doc="128x128.          ")
    kFBResolutionFullScreen=property(doc="FullScreen.          ")
    pass

class FBCameraSafeAreaMode (Enumeration):
    """
    Safe area modes.     
         
    """
    kFBSafeAreaSquare=property(doc="Square safe area.          ")
    kFBSafeAreaRound=property(doc="Round safe area.          ")
    pass

class FBCameraSamplingType (Enumeration):
    """
    Antialiasing sampling types.     
         
    """
    kFBSamplingUniform=property(doc="Uniform sampling.          ")
    kFBSamplingStochastic=property(doc="Stochastic sampling.          ")
    pass

class FBCameraStereoType (Enumeration):
    """
        
        
    """
    kFBCameraStereoNone=property(doc="        ")
    kFBCameraStereoConverged=property(doc="        ")
    kFBCameraStereoOff_Axis=property(doc="        ")
    kFBCameraStereoParallel=property(doc="        ")
    pass

class FBCameraType (Enumeration):
    """
    Focus distance types.     
         
    """
    kFBCameraTypePerspective=property(doc="Interest as source.          ")
    kFBCameraTypeOrthogonal=property(doc="Specific distance as source.          ")
    pass

class FBCameraViewPlaneMode (Enumeration):
    """
    Camera plane viewing modes.     
         
    """
    kFBViewPlaneDisabled=property(doc="Camera plane disabled.          ")
    kFBViewPlaneAlways=property(doc="Always draw camera plane.          ")
    kFBViewPlaneWhenMedia=property(doc="Camera plane when media.          ")
    pass

class FBCellStyle (Enumeration):
    """
    Different styles of spreadsheet cell styles.     
         
    """
    kFBCellStyleDefault=property(doc="Default cell style.          ")
    kFBCellStyleString=property(doc="String.          ")
    kFBCellStyleDouble=property(doc="Double.          ")
    kFBCellStyleInteger=property(doc="Integer.          ")
    kFBCellStyleButton=property(doc="Button.          ")
    kFBCellStyle2StatesButton=property(doc="2 state button.          ")
    kFBCellStyle3StatesButton=property(doc="3 state button.          ")
    kFBCellStyleMenu=property(doc="Menu.          ")
    kFBCellStyleVoid=property(doc="Void (no value).          ")
    kFBCellStyleView=property(doc="View (user definable, you need to specify the view using FBSpread::SetCellView()).          ")
    kFBCellStyleTime=property(doc="Time.          ")
    pass

class FBCharacterContactBehaviour (Enumeration):
    """
    Character Contact Behaviour.     
         
    """
    kFBParamContactNeverSync=property(doc="        ")
    kFBParamContactSyncOnKey=property(doc="        ")
    kFBParamContactAlwaysSync=property(doc="        ")
    kFBLastContactBehaviour=property(doc="        ")
    pass

class FBCharacterExtensionRetargetMode (Enumeration):
    """
    Character extension Retarget Mode      
        
    """
    kFBRetargetModeOff=property(doc="        ")
    kFBRetargetModeAuto=property(doc="        ")
    kFBRetargetModeManual=property(doc="        ")
    pass

class FBCharacterExtensionStancePoseMode (Enumeration):
    """
    Character Extension Stance Pose mode when the stance pose is activated on a character.     
         
    """
    kFBStancePose_Never=property(doc="        ")
    kFBStancePose_Selected=property(doc="        ")
    kFBStancePose_Reference_Selected=property(doc="        ")
    kFBStancePose_Self_Or_Reference_Selected=property(doc="        ")
    kFBStancePose_Always=property(doc="        ")
    pass

class FBCharacterHipsTranslationMode (Enumeration):
    """
    Character Hips Translation modes.     
         
    """
    kFBParamHipsTranslationWorldRigid=property(doc="        ")
    kFBParamHipsTranslationBodyRigid=property(doc="        ")
    kFBLastHipsTranslationMode=property(doc="        ")
    pass

class FBCharacterInputType (Enumeration):
    """
    Character Input/Output types.     
         
    """
    kFBCharacterInputActor=property(doc="        ")
    kFBCharacterInputCharacter=property(doc="        ")
    kFBCharacterInputMarkerSet=property(doc="        ")
    kFBCharacterOutputMarkerSet=property(doc="        ")
    kFBCharacterInputStance=property(doc="        ")
    kFBCharacterInputMoCap=property(doc="        ")
    pass

class FBCharacterKeyingMode (Enumeration):
    """
    Character keying modes.     
         
    """
    kFBCharacterKeyingFullBody=property(doc="        ")
    kFBCharacterKeyingBodyPart=property(doc="        ")
    kFBCharacterKeyingSelection=property(doc="        ")
    kFBCharacterKeyingFullBodyNoPull=property(doc="        ")
    pass

class FBCharacterLoadAnimationMethod (Enumeration):
    """
    This enumeration is used to choose how to load an animation file on a character.     
         
    """
    kFBCharacterLoadConnect=property(doc="Only connect the loaded character as an input.          ")
    kFBCharacterLoadCopy=property(doc="Copy keys from loaded character to target character.          ")
    kFBCharacterLoadRetarget=property(doc="Retarget (copy and correct) keys from loaded character to target character.          ")
    kFBCharacterLoadPlotIfSampled=property(doc="If loaded animation seems sampled, plot animation from loaded character to target character; else retarget.          ")
    kFBCharacterLoadPlot=property(doc="Plot animation from loaded character to target character.          ")
    pass

class FBCharacterPlotWhere (Enumeration):
    """
    Where to plot a character.     
         
    """
    kFBCharacterPlotOnControlRig=property(doc="        ")
    kFBCharacterPlotOnSkeleton=property(doc="        ")
    pass

class FBCharacterPoseFlag (Enumeration):
    """
    Character Pose Options flags.     
         
    """
    kFBCharacterPoseNoFlag=property(doc="        ")
    kFBCharacterPoseMirror=property(doc="        ")
    kFBCharacterPoseGravity=property(doc="        ")
    kFBCharacterPoseMatchTX=property(doc="        ")
    kFBCharacterPoseMatchTY=property(doc="        ")
    kFBCharacterPoseMatchTZ=property(doc="        ")
    kFBCharacterPoseMatchR=property(doc="        ")
    kFBCharacterPoseMatchPivot=property(doc="        ")
    kFBCharacterPoseUseKeyingGroup=property(doc="        ")
    kFBCharacterPoseMatchFKTranslation=property(doc="        ")
    pass

class FBCharacterPoseKeyingMode (Enumeration):
    """
    Character Pose Keying Mode.     
         
    """
    kFBCharacterPoseKeyingModeInvalid=property(doc="        ")
    kFBCharacterPoseKeyingModeFullBody=property(doc="        ")
    kFBCharacterPoseKeyingModeBodyPart=property(doc="        ")
    kFBCharacterPoseKeyingModeCount=property(doc="        ")
    pass

class FBCharacterResetProperties (Enumeration):
    """
    Character Reset Properties Type.     
         
    """
    kFBCharacterResetPropertiesAll=property(doc="        ")
    kFBCharacterResetPropertiesSolving=property(doc="        ")
    kFBCharacterResetPropertiesDefinition=property(doc="        ")
    pass

class FBCharacterRollSolver (Enumeration):
    """
    Character Roll Solver version.     
         
    """
    kFBParamRollSolver70=property(doc="        ")
    kFBParamRollSolver75=property(doc="        ")
    kFBLastRollSolver=property(doc="        ")
    pass

class FBClipEnd (Enumeration):
    """
    Clip end actions.     
         
    """
    kFBClipEndEnd=property(doc="On clip end stop clip.          ")
    kFBClipEndLoop=property(doc="On clip end loop clip.          ")
    pass

class FBClusterMode (Enumeration):
    """
    Different clustering modes.     
         
    """
    kFBClusterNormalize=property(doc="Normalize (values between 0.0 and 1.0 )          ")
    kFBClusterAdditive=property(doc="Add the values together.          ")
    kFBClusterTotal100=property(doc="The balanced values will add up to 100 percent.          ")
    pass

class FBCommandState (Enumeration):
    """
    FBCommandState.     
         
    """
    kFBCommandStateStandard=property(doc="Standard.          ")
    kFBCommandStateMute=property(doc="Mute.          ")
    kFBCommandStateSolo=property(doc="Solo.          ")
    kFBCommandStateMuteBecauseSolo=property(doc="Mute because of solo.          ")
    pass

class FBCommPortType (Enumeration):
    """
    Communication port type.     
         
    """
    kFBPhysical=property(doc="Physical.          ")
    kFBVirtual=property(doc="Virtual.          ")
    kFBInternal=property(doc="Internal.          ")
    pass

class FBCommType (Enumeration):
    """
    Communications type.     
     Different base types of communications. There is always the 'other' type in order to use another type of communication.      
    """
    kFBCommTypeNone=property(doc="A non-communicating device.          ")
    kFBCommTypeSerial=property(doc="Serial communications.          ")
    kFBCommTypeNetworkTCP=property(doc="Network (TCP) device.          ")
    kFBCommTypeNetworkUDP=property(doc="Network (UDP) device.          ")
    kFBCommTypeSharedMemory=property(doc="Accessing shared memory.          ")
    kFBCommTypeSimulator=property(doc="Software simulator.          ")
    kFBCommTypeOther=property(doc="Any other type of communications.          ")
    pass

class FBComponent (FBPlug):
    """
    MotionBuilder SDK base class.     
     FBComponent defines common object characteristics, including creation and destruction methods. It is used to encapsulate internal application objects so they can be exposed to the SDK. It is also used as the base class to encapsulate objects with FBProperty data members and provides a scheme for property management. You cannot instantiate FBProperty objects. To reference a property, use an instance of an FBComponent object. The methods FBComponent::PropertyCreate and FBComponent::PropertyRemove can be used to modify an object's properties. Basic operators are overloaded in FBComponent. The constructor and destructor are created and defined with macros in the header files. Objects inheriting from FBComponent must define FBComponent::FBCreate(), and FBComponent::FBDestroy(). All memory management issues for the component should also be addressed here. Destroy an object with FBDelete(). The code sample FBComponent.py shows how to get a handle on a scene object via its name. See sample: ReplaceNamespace.py.     
    """
    def FBComponent(self):
        """
        Constructor.

        """
        pass

    def ClassName(self):
        """
        Get the class name.

        return : The class name (i.e. "FBComponent").
        """
        pass

    def DisableObjectFlags(self,pFlags):
        """
        Disable a specific Object Flags.

        pFlags : Flags to disable. 
        """
        pass

    def EnableObjectFlags(self,pFlags):
        """
        Enable a specific Object Flags.

        pFlags : Flags to enable. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def FBDelete(self):
        """
        Open Reality deletion function.

        """
        pass

    def FBDestroy(self):
        """
        Open Reality destruction function.

        """
        pass

    def GetObjectFlags(self):
        """
        Get all Object Flags (concatenated).

        return : Get all object flags in one call. Flags can be concatenated. 
        """
        pass

    def GetObjectStatus(self,pStatus):
        """
        Check to see if an object status is enabled.

        pStatus : Status to query. 
        """
        pass

    def GetOwnerFileReference(self,p0):
        """
        Get the owner FileReference object.

        p0 : p0
        return : the owner FileReference object 
        """
        pass

    def HardSelect(self):
        """
        HardSelect.
        Selects the object, and emits a hard select event for UI update notification.

        """
        pass

    def HasObjectFlags(self,pFlags):
        """
        Check whether a specific object flag is enabled.

        pFlags : Flags to check if they are present. 
        return : True if all flags in pFlags are enabled. 
        """
        pass

    def Is(self,pTypeId):
        """
        Returns true if object is of type TypeId.

        pTypeId : TypeId to compare object to. 
        return : Result of the comparison. 
        """
        pass

    def ProcessNamespaceHierarchy(self,pNamespaceAction,pNamespaceName,pReplaceTo,pAddRight):
        """
        ProcessNamespaceHierarchy.
        New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This recursive function goes through the whole hierarchy (children) to add/replace the prefix. If you need to work on a single object, use the ProcessObjectPrefix function.

        pNamespaceAction : Which operation to do on the hierarchy (children). 
        pNamespaceName : The Namespace name on Add/Delete or the prefix to replace in case of replace. 
        pReplaceTo : The new Namespace Name or NULL in case of add or delete. 
        pAddRight : Whether to add the namespace on right-most or left-most side or other namespace. 
        return : return true if process successful. 
        """
        pass

    def ProcessObjectNamespace(self,pNamespaceAction,pNamespaceName,pReplaceTo,pAddRight):
        """
        ProcessObjectNamespace.
        New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This function is the same as ProcessNamespaceHierarchy except that it applies only on the current object and not to the object's children.

        pNamespaceAction : Which operation to do on the hierarchy (children). 
        pNamespaceName : The Namespace name on Add/Delete or the prefix to replace in case of replace. 
        pReplaceTo : The new Namespace Name or NULL in case of add or delete. 
        pAddRight : Whether to add the namespace on right-most or left-most side or other namespace. 
        return : return true if process successful. 
        """
        pass

    def PropertyAdd(self,pProperty):
        """
        Add a property to the component's property manager.

        pProperty : The property to add to the property manager. 
        return : Index in the property array where property was inserted. 
        """
        pass

    def PropertyAddReferenceProperty(self,pReferenceProperty):
        """
        Add a reference property to the component's property manager.

        pReferenceProperty : The property to from an other object to add a reference to (property cannot be a custom ORSDK property). 
        return : True if the reference property could be added. 
        """
        pass

    def PropertyCreate(self,pName,pType,pDataType,pAnimatable,pIsUser,pReferenceSource):
        """
        Create user or dynamic property.

        pName : The name of the property. 
        pType : Type of the property. See enum FBPropertyType. 
        pDataType : DataType of the property. 
        pAnimatable : To specify if the property can be animated. 
        pIsUser : To specify if the property is available as a custom property or dynamic and attached to the object. 
        pReferenceSource : Specifies the property that a reference refers to. 
        """
        pass

    def PropertyGetModifiedList(self,pPropList,pModificationFlags):
        """
        Get list of properties which have been modified since last loading.

        pPropList : property list to hold the modified properties. 
        pModificationFlags : type of modification to query. 
        """
        pass

    def PropertyRemove(self,pProperty):
        """
        Remove a Property from the component's Property manager.
        If the property was dynamically allocated, it is deleted.

        pProperty : The property to remove from the property manager. 
        """
        pass

    def SetObjectFlags(self,pFlags):
        """
        SetObjectFlags.

        pFlags : Set flag values. Note: this function overwrites all flags with those passed in parameter. 
        """
        pass

    def SetObjectStatus(self,pStatus,pValue):
        """
        Enable/Disable a specific Object Status.

        pStatus : Status to change. 
        pValue : Value to change the status to. 
        """
        pass

    Components=property(doc="<b>List:</b> List of components.          ")
    LongName=property(doc="<b>Read Write Property:</b> Name and namespace for object.          ")
    Name=property(doc="<b>Read Write Property:</b> Unique name of object. See sample: RemoveSuffixFromNameOfSceneElements.py.         ")
    Parents=property(doc="<b>List:</b> Parents.          ")
    PropertyList=property(doc="<b>Read Only Property:</b> Manages all of the properties for the component.          ")
    Selected=property(doc="<b>Read Write Property:</b> Selected property.          ")
    TypeInfo=property(doc="Contains the Type information of the object.          ")
    pass

class FBConnectionAction (Enumeration):
    """
    Possible actions when a notify plug event occurs.     
         
    """
    kFBRequestConnectSrc=property(doc="Request connection of source to destination.          ")
    kFBRequestConnectDst=property(doc="Request connection of destination to source.          ")
    kFBConnectSrc=property(doc="Connect source to destination.          ")
    kFBConnectDst=property(doc="Connect destination to source.          ")
    kFBConnectedSrc=property(doc="Connected source to destination.          ")
    kFBConnectedDst=property(doc="Connected destination to source.          ")
    kFBRequestDisconnectSrc=property(doc="Request disconnection of source to destination.          ")
    kFBRequestDisconnectDst=property(doc="Request disconnection of destination to source.          ")
    kFBDisconnectSrc=property(doc="Disconnect source from destination.          ")
    kFBDisconnectDst=property(doc="Disconnect destination from source.          ")
    kFBDisconnectedSrc=property(doc="Disconnected source from destination.          ")
    kFBDisconnectedDst=property(doc="Disconnected destination from source.          ")
    kFBBeginReplaceSrc=property(doc="Begin replace source during merge.          ")
    kFBEndReplaceSrc=property(doc="End replace source during merge.          ")
    kFBBeginReplaceDst=property(doc="Begin replace destination during merge.          ")
    kFBEndReplaceDst=property(doc="End replace destination during merge.          ")
    kFBReorderSrc=property(doc="Reorder of source.          ")
    kFBReorderedSrc=property(doc="Source has been reordered.          ")
    kFBBeginChange=property(doc="Begin change on destination.          ")
    kFBEndChange=property(doc="End change on destination.          ")
    kFBConnectedOwner=property(doc="Connected owner to destination.          ")
    kFBDisconnectOwner=property(doc="Disconnect owner from destination.          ")
    kFBCandidate=property(doc="Data candidate event, before the data is set.          ")
    kFBCandidated=property(doc="Data candidate event, after the data is set.          ")
    kFBCandidateGlobal=property(doc="Data candidate event, global candidate.          ")
    kFBDetached=property(doc="Component detached from scene.          ")
    kFBDestroy=property(doc="Component destroy.          ")
    kFBSelect=property(doc="Component selection.          ")
    kFBUnselect=property(doc="Component de-selection.          ")
    kFBReselect=property(doc="Component re-selection.          ")
    kFBRequestRename=property(doc="Component request rename.          ")
    kFBRename=property(doc="Component is going to be renamed.          ")
    kFBRenamed=property(doc="Component has been renamed.          ")
    kFBRequestPrefixRename=property(doc="Compoent request Prefix Rename.          ")
    kFBPrefixRename=property(doc="Component prefix is going to be renamed.          ")
    kFBPrefixRenamed=property(doc="Component prefix has been renamed.          ")
    kFBDescription=property(doc="Component description event.          ")
    kFBKeyingKey=property(doc="Component keying add event.          ")
    kFBKeyingDeleteKey=property(doc="Component keying delete event.          ")
    kFBKeyingCandidate=property(doc="Component keying candidate event.          ")
    kFBKeyingCurveChange=property(doc="Component curve has changed.          ")
    kFBKeyingCurveEndChange=property(doc="Component curve changes in Dopesheet completed.          ")
    kFBConnect=property(doc="        ")
    kFBConnected=property(doc="        ")
    kFBDisconnect=property(doc="        ")
    kFBDisconnected=property(doc="        ")
    pass

class FBConnectionType (Enumeration):
    """
    Connection types available between plugs.     
         
    """
    kFBConnectionTypeNone=property(doc="Default connection type.          ")
    kFBConnectionTypeSystem=property(doc="System connection type.          ")
    pass

class FBConsoleChannelType (Enumeration):
    """
    Console channel types.     
         
    """
    kFBConsoleNull=property(doc="Generic type.          ")
    kFBConsoleButton=property(doc="Button.          ")
    kFBConsoleSlider=property(doc="Slider.          ")
    kFBConsoleTransport=property(doc="Transport.          ")
    kFBConsoleEncoder=property(doc="Generic encoder.          ")
    kFBConsoleKey=property(doc="Key.          ")
    kFBConsoleDisplay=property(doc="Display.          ")
    kFBConsoleJoystick=property(doc="Joystick.          ")
    pass

class FBConstantKeyReducerThresholdType (Enumeration):
    """
    Different threshold types for the Constant Key Reducer filter.     
         
    """
    kFBTranslationThreshold=property(doc="Translation threshold.          ")
    kFBRotationThreshold=property(doc="Rotation threshold.          ")
    kFBScalingThreshold=property(doc="Scaling threshold.          ")
    kFBDefaultThreshold=property(doc="All other curves threshold.          ")
    pass

class FBConstructionHistoryState (Enumeration):
    """
    Construction history manager state.     
         
    """
    kFBConstructionHistory_Listening=property(doc="Construction history is currently listening and recording operations.          ")
    kFBConstructionHistory_Replaying=property(doc="Construction history is currently replaying an operation.          ")
    pass

class FBControllerMode (Enumeration):
    """
    Controller modes for optical model.     
         
    """
    kFBControllerNone=property(doc="No controller mode.          ")
    kFBControllerLabelling=property(doc="Labelling controller.          ")
    kFBControllerSegment=property(doc="Segment controller.          ")
    kFBControllerRigidBody=property(doc="Rigid body controller.          ")
    pass

class FBControlSetType (Enumeration):
    """
    Character ControlSet type.     
         
    """
    kFBControlSetTypeNone=property(doc="        ")
    kFBControlSetTypeFKIK=property(doc="        ")
    kFBControlSetTypeIKOnly=property(doc="        ")
    pass

class FBDataAsStringFlag (Enumeration):
    """
    FBDataAsStringFlag.     
         
    """
    kFBDataAsStringUI=property(doc="Convert data to string type for UI display.          ")
    kFBDataAsStringPersistence=property(doc="Convert data to string type for storage.          ")
    pass

class FBDeckTransportMode (Enumeration):
    """
    FBDeckTransportMode.     
         
    """
    kFBDeckTransportNone=property(doc="No transport interaction.          ")
    kFBDeckTransportSync=property(doc="Sync to transport controls.          ")
    kFBDeckTransportSlave=property(doc="K_DEPRECATED_2021, use kFBDeckTransportSync.          ")
    kFBDeckTransportMain=property(doc="Transport main.          ")
    kFBDeckTransportMaster=property(doc="K_DEPRECATED_2021, use kFBDeckTransportMain.          ")
    pass

class FBDeformerType (Enumeration):
    """
    Determine the deformer type.     
     kFBDeformerSkeleton Skeleton (Bone) driven skinning deformer.kFBDeformerPointCache Pre-recorded point cache deformer.kFBGeometryMapping_BY_POLYGON_VERTEX There will be one mapping coordinate for each vertex, for each polygon/strip it is part of. This means that a vertex will have as many mapping coordinates as polygons it is part of.kFBGeometryMapping_BY_POLYGON There can be only one mapping coordinate for the whole polygon/strip.kFBGeometryMapping_BY_EDGE There will be one mapping coordinate for each unique edge in the mesh. This is meant to be used with smoothing layer elements.kFBGeometryMapping_ALL_SAME There can be only one mapping coordinate for the whole surface.      
    """
    kFBDeformerUnkown=property(doc="        ")
    kFBDeformerSkeleton=property(doc="        ")
    kFBDeformerPointCache=property(doc="        ")
    pass

class FBDeviceKeyboardKey (Enumeration):
    """
    Keyboard keys (for input).     
         
    """
    kFBDKeyPageUp=property(doc="Page Up.          ")
    kFBDKeyPageDown=property(doc="Page Down.          ")
    kFBDKeyEnd=property(doc="End.          ")
    kFBDKeyHome=property(doc="Home.          ")
    kFBDKeyArrowLeft=property(doc="Left.          ")
    kFBDKeyArrowUp=property(doc="Up.          ")
    kFBDKeyArrowRight=property(doc="Right.          ")
    kFBDKeyArrowDown=property(doc="Down.          ")
    kFBDKeyReturn=property(doc="Return.          ")
    kFBDKeyEscape=property(doc="Escape.          ")
    kFBDKeySpace=property(doc="Space bar.          ")
    kFBDKey1=property(doc="'1'.          ")
    kFBDKey2=property(doc="'2'.          ")
    kFBDKey3=property(doc="'3'.          ")
    kFBDKey4=property(doc="'4'.          ")
    kFBDKey5=property(doc="'5'.          ")
    kFBDKey6=property(doc="'6'.          ")
    kFBDKey7=property(doc="'7'.          ")
    kFBDKey8=property(doc="'8'.          ")
    kFBDKey9=property(doc="'9'.          ")
    kFBDKey0=property(doc="'0'.          ")
    kFBDKeyF1=property(doc="'F1'.          ")
    kFBDKeyF2=property(doc="'F2'.          ")
    kFBDKeyF3=property(doc="'F3'.          ")
    kFBDKeyF4=property(doc="'F4'.          ")
    kFBDKeyF5=property(doc="'F5'          ")
    kFBDKeyF6=property(doc="'F6'.          ")
    kFBDKeyF7=property(doc="'F7'.          ")
    kFBDKeyF8=property(doc="'F8'.          ")
    kFBDKeyF9=property(doc="'F9'.          ")
    kFBDKeyF10=property(doc="'F10'.          ")
    kFBDKeyF11=property(doc="'F11'.          ")
    kFBDKeyF12=property(doc="'F12'.          ")
    pass

class FBDeviceSamplingMode (Enumeration):
    """
    Recording types.     
     The different values for this will control the way the keys are added when the device is being recorded. There are four different types of recording keys for devices:Hardware Timestamping. This case is when the hardware provides timestamps with each packet.Hardware Frequency. The hardware is guaranteed to provide packets at a given frequency.Auto Frequency Packets are coming in at a fixed, unknown frequency. The recorded data will be resampled to be equidistant.Software Timestamping. The application will provide a timestamp for each packet depending on when it receives the data.      
    """
    kFBHardwareTimestamp=property(doc="Device supplies timestamp.          ")
    kFBHardwareFrequency=property(doc="Device is running at known, fixed frequency.          ")
    kFBAutoFrequency=property(doc="Device is running at unknown, fixed frequency.          ")
    kFBSoftwareTimestamp=property(doc="The software will timestamp packets as they arrive.          ")
    pass

class FBDisplayMode (Enumeration):
    """
    Model display options.     
         
    """
    kFBDisplayModeDefault=property(doc="Use default display mode.          ")
    kFBDisplayModeTexture=property(doc="Textures are displayed.          ")
    kFBDisplayModeHardShade=property(doc="Hard shading.          ")
    kFBDisplayModeFlatShade=property(doc="Flat shading.          ")
    kFBDisplayModeWireFrame=property(doc="Wire-frame rendering.          ")
    kFBDisplayModeCount=property(doc="End of enum, this value indicates the number of display modes available.          ")
    pass

class FBDisplayWhat (Enumeration):
    """
    Model display mask This mask determines what types of models are displayed by the renderer.     
         
    """
    kFBDisplayNone=property(doc="Nothing is displayed.          ")
    kFBDisplayNull=property(doc="Null models are displayed.          ")
    kFBDisplayMarker=property(doc="Markers are displayed.          ")
    kFBDisplaySkeleton=property(doc="Skeletons and bones are displayed.          ")
    kFBDisplayCenter=property(doc="Centers are displayed.          ")
    kFBDisplayLight=property(doc="Lights are displayed.          ")
    kFBDisplayCamera=property(doc="Cameras are displayed.          ")
    kFBDisplay3dIcon=property(doc="3D icons are displayed (3D icons are 3D elements that do not exist in the scene).          ")
    kFBDisplayAll=property(doc="Everything is displayed.          ")
    pass

class FBDragAndDropState (Enumeration):
    """
    State of Drag and Drop.     
    See samples: PropertyDrop.py, Spread.py.     
    """
    kFBDragAndDropBegin=property(doc="Begin a drag and drop sequence.          ")
    kFBDragAndDropDrag=property(doc="Dragging.          ")
    kFBDragAndDropDrop=property(doc="Dropping.          ")
    kFBDragAndDropEnd=property(doc="End of drag and drop.          ")
    kFBDragOnEmpty=property(doc="Empty the drag and drop stack.          ")
    kFBDragOnEmptyDrop=property(doc="Dropping empty stack.          ")
    pass

class FBEdit (FBVisualComponent):
    """
    Text edit box.     
         
    """
    def FBEdit(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Text changed.          ")
    PasswordMode=property(doc="<b>Read Write Property:</b> Set password mode for this edit box.          ")
    Text=property(doc="<b>Read Write Property:</b> Text displayed.          ")
    pass

class FBEditColor (FBVisualComponent):
    """
    Color edit widget.     
         
    """
    def FBEditColor(self):
        """
        Constructor.

        """
        pass

    ColorMode=property(doc="<b>Read Write Property:</b> 3 for RGB, 4 for RGBA (Default = 3)          ")
    OnChange=property(doc="<b>Event:</b> Color changed.          ")
    Value=property(doc="<b>Read Write Property:</b> Current value of color.          ")
    pass

class FBEditNumber (FBVisualComponent):
    """
    Number edit box.     
         
    """
    def FBEditNumber(self):
        """
        Constructor.

        """
        pass

    LargeStep=property(doc="<b>Read Write Property:</b> Large step value.          ")
    Max=property(doc="<b>Read Write Property:</b> Maximum value.          ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.          ")
    OnChange=property(doc="<b>Event:</b> Number changed.          ")
    Precision=property(doc="<b>Read Write Property:</b> Precision of value.          ")
    SmallStep=property(doc="<b>Read Write Property:</b> Small step value.          ")
    Value=property(doc="<b>Read Write Property:</b> Current value.          ")
    pass

class FBEditProperty (FBVisualComponent):
    """
    Property editor widget.     
     This widget allows users to edit the values of a property without having to manually customize the GUI depending on the type of the property being edited.SDK objects can have three types of properties:An internal property which maps to an actual property that can be seen in the property editor tool of the application. This type of property is usually obtained from the PropertyList data member.SDK-only property which does not maps onto an existing property of the encapsulated object. The existence of these types of property is often to make the object interface simpler. All the FBPropertyList-types will fall into this category, except for FBPropertyListObjects.SDK property which maps onto an existing object property, but does so indirectly using function calls instead of direct property access. This is usually for historical reason. In this case the property will usually be present twice in the PropertyList: once as an SDK-Only property and another time as an internal property.Another limitation of this widget is that it can only display non hidden internal properties. To get around this issue, the property flag can be changed to unhide it. Doing so will also cause the property to be visible via the property tool. 
@code
// In a tool header file...
FBEditProperty mEditProperty;

// In a tool source file...
FBModel* lModel = FBFindModelByLabelName( 'ModelName' );
if( lModel )
{
    FBProperty* lProperty = lModel->PropertyList.Find( 'RotationOrder' );
    if( lProperty &&
        lProperty->IsInternal() &&
        !lProperty->GetPropertyFlag( kFBPropertyFlagHideProperty ))
    {
        mEditProperty.Property = lProperty;
    }
}
@endcode

See sample: PropertyDrop.py.     
    """
    def FBEditProperty(self):
        """
        Constructor.

        """
        pass

    LargeInc=property(doc="<b>Read Write Property:</b> Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)          ")
    Precision=property(doc="<b>Read Write Property:</b> Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals.          ")
    Property=property(doc="<b>Read Write Property:</b> Property to edit. Set to NULL to disable.          ")
    SliderMax=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the maximum value atainable with the slider.          ")
    SliderMin=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the minimum value atainable with the slider.          ")
    SmallInc=property(doc="<b>Read Write Property:</b> Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)          ")
    pass

class FBEditPropertyModern (FBVisualComponent):
    """
    Property editor widget.     
     This is a more modern version of the widget FBEditProperty which is used in the property editor tool of the application.See class FBEditProperty for more details. See sample: PropertyDrop.py.     
    """
    def FBEditPropertyModern(self):
        """
        Constructor.

        """
        pass

    def SetBackgroundColorIndex(self,pIndex):
        """
        Set the background color index.
        Use the system-defined color palette to set the backgound color. By default the color used is kFBColorIndexStdListBg1

        pIndex : FBColorIndex
        """
        pass

    LargeInc=property(doc="<b>Read Write Property:</b> Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)          ")
    Precision=property(doc="<b>Read Write Property:</b> Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals.          ")
    Property=property(doc="<b>Read Write Property:</b> Property to edit. Set to NULL to disable.          ")
    SliderMax=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the maximum value atainable with the slider.          ")
    SliderMin=property(doc="<b>Read Write Property:</b> Should the property be editable using a slider, set the minimum value atainable with the slider.          ")
    SmallInc=property(doc="<b>Read Write Property:</b> Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)          ")
    pass

class FBEditTimeCode (FBVisualComponent):
    """
        
        
    """
    def FBEditTimeCode(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Timecode changed.          ")
    Value=property(doc="<b>Read Write Property:</b> Current timecode value.          ")
    pass

class FBEditVector (FBVisualComponent):
    """
    Vector edit widget.     
         
    """
    def FBEditVector(self):
        """
        Constructor.

        """
        pass

    OnChange=property(doc="<b>Event:</b> Vector value changed.          ")
    Value=property(doc="<b>Read Write Property:</b> Current value of vector.          ")
    pass

class FBEffectorId (Enumeration):
    """
    All effector nodes.     
         
    """
    kFBInvalidEffectorId=property(doc="        ")
    kFBHipsEffectorId=property(doc="        ")
    kFBLeftAnkleEffectorId=property(doc="        ")
    kFBRightAnkleEffectorId=property(doc="        ")
    kFBLeftWristEffectorId=property(doc="        ")
    kFBRightWristEffectorId=property(doc="        ")
    kFBLeftKneeEffectorId=property(doc="        ")
    kFBRightKneeEffectorId=property(doc="        ")
    kFBLeftElbowEffectorId=property(doc="        ")
    kFBRightElbowEffectorId=property(doc="        ")
    kFBChestOriginEffectorId=property(doc="        ")
    kFBChestEndEffectorId=property(doc="        ")
    kFBLeftFootEffectorId=property(doc="        ")
    kFBRightFootEffectorId=property(doc="        ")
    kFBLeftShoulderEffectorId=property(doc="        ")
    kFBRightShoulderEffectorId=property(doc="        ")
    kFBHeadEffectorId=property(doc="        ")
    kFBLeftHipEffectorId=property(doc="        ")
    kFBRightHipEffectorId=property(doc="        ")
    kFBLeftHandEffectorId=property(doc="        ")
    kFBRightHandEffectorId=property(doc="        ")
    kFBLeftHandThumbEffectorId=property(doc="        ")
    kFBLeftHandIndexEffectorId=property(doc="        ")
    kFBLeftHandMiddleEffectorId=property(doc="        ")
    kFBLeftHandRingEffectorId=property(doc="        ")
    kFBLeftHandPinkyEffectorId=property(doc="        ")
    kFBLeftHandExtraFingerEffectorId=property(doc="        ")
    kFBRightHandThumbEffectorId=property(doc="        ")
    kFBRightHandIndexEffectorId=property(doc="        ")
    kFBRightHandMiddleEffectorId=property(doc="        ")
    kFBRightHandRingEffectorId=property(doc="        ")
    kFBRightHandPinkyEffectorId=property(doc="        ")
    kFBRightHandExtraFingerEffectorId=property(doc="        ")
    kFBLeftFootThumbEffectorId=property(doc="        ")
    kFBLeftFootIndexEffectorId=property(doc="        ")
    kFBLeftFootMiddleEffectorId=property(doc="        ")
    kFBLeftFootRingEffectorId=property(doc="        ")
    kFBLeftFootPinkyEffectorId=property(doc="        ")
    kFBLeftFootExtraFingerEffectorId=property(doc="        ")
    kFBRightFootThumbEffectorId=property(doc="        ")
    kFBRightFootIndexEffectorId=property(doc="        ")
    kFBRightFootMiddleEffectorId=property(doc="        ")
    kFBRightFootRingEffectorId=property(doc="        ")
    kFBRightFootPinkyEffectorId=property(doc="        ")
    kFBRightFootExtraFingerEffectorId=property(doc="        ")
    kFBLastEffectorId=property(doc="        ")
    pass

class FBEffectorSetID (Enumeration):
    """
    Effector ID identifier.     
         
    """
    FBEffectorSetDefault=property(doc="        ")
    FBEffectorSetAux1=property(doc="        ")
    FBEffectorSetAux2=property(doc="        ")
    FBEffectorSetAux3=property(doc="        ")
    FBEffectorSetAux4=property(doc="        ")
    FBEffectorSetAux5=property(doc="        ")
    FBEffectorSetAux6=property(doc="        ")
    EFBffectorSetAux7=property(doc="        ")
    FBEffectorSetAux8=property(doc="        ")
    FBEffectorSetAux9=property(doc="        ")
    FBEffectorSetAux10=property(doc="        ")
    FBEffectorSetAux11=property(doc="        ")
    FBEffectorSetAux12=property(doc="        ")
    FBEffectorSetAux13=property(doc="        ")
    FBEffectorSetAux14=property(doc="        ")
    FBLastEffectorSetIndex=property(doc="        ")
    pass

class FBElementAction (Enumeration):
    """
    Enumeration that describe the different actions available on a scene element depending on the current context.     
         
    """
    kFBElementActionSave=property(doc="Save the element (when saving).          ")
    kFBElementActionAppend=property(doc="Append the elements to the current scene elements (when loading or merging).          ")
    kFBElementActionMerge=property(doc="Merge the elements from the file in the current scene (when merging).          ")
    kFBElementActionDiscard=property(doc="Do not consider the element (when loading, merging and saving).          ")
    pass

class FBEventActivate (FBEvent):
    """
    Activation event.     
         
    """
    def FBEventActivate(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> Generic data of event.          ")
    pass

class FBEventAnimationNodeType (Enumeration):
    """
    Event based on animation node.     
     Types of transformation.      
    """
    kFBEventAnimationNodeDataChange=property(doc="        ")
    kFBEventAnimationNodeConstraintChange=property(doc="        ")
    kFBEventAnimationNodeNone=property(doc="        ")
    pass

class FBEventClipChange (FBEvent):
    """
        
        
    """
    def FBEventClipChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of event.          ")
    pass

class FBEventConnectionDataNotify (FBEvent):
    """
    Connection notify event class.     
         
    """
    def FBEventConnectionDataNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.          ")
    Plug=property(doc="<b>Read Only Property:</b> The plug involved in the action.          ")
    pass

class FBEventConnectionKeyingNotify (FBEvent):
    """
        
        
    """
    def FBEventConnectionKeyingNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    pass

class FBEventConnectionNotify (FBEvent):
    """
    Connection notify event class.     
         
    """
    def FBEventConnectionNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.          ")
    ConnectionType=property(doc="<b>Read Only Property:</b> Connection's type.          ")
    DstPlug=property(doc="<b>Read Only Property:</b> The destination plug involved in the action.          ")
    NewPlug=property(doc="<b>Read Only Property:</b> New plug created by the action. (Mostly used by merge/replace)          ")
    SrcIndex=property(doc="<b>Read Only Property:</b> Index of the source in the destination component.          ")
    SrcPlug=property(doc="<b>Read Only Property:</b> The source plug involved in the action.          ")
    pass

class FBEventConnectionStateNotify (FBEvent):
    """
    Connection notify event class.     
         
    """
    def FBEventConnectionStateNotify(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Connection's action performed.          ")
    Plug=property(doc="<b>Read Only Property:</b> The plug involved in the action.          ")
    pass

class FBEventDblClick (FBEvent):
    """
    Input event class.     
         
    """
    def FBEventDblClick(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Selection=property(doc="<b>Read Only Property:</b> Id of selection.          ")
    pass

class FBEventEvalGlobalCallback (FBEvent):
    """
        
        
    """
    def FBEventEvalGlobalCallback(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    pass

class FBEventExpose (FBEvent):
    """
    Event sent when a control needs to be displayed.     
         
    """
    def FBEventExpose(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    pass

class FBEventFileChange (FBEvent):
    """
    File change event class.     
     This event occurs every time a monitored file changed:      
    """
    def FBEventFileChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Path=property(doc="<b>Read Only Property:</b> The path of changed file.          ")
    Type=property(doc="<b>Read Only Property:</b> Type of file change event.          ")
    pass

class FBEventInput (FBEvent):
    """
    Input event class.     
         
    """
    def FBEventInput(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    InputType=property(doc="<b>Read Only Property:</b> Input type.          ")
    Key=property(doc="<b>Read Only Property:</b> Input key.          ")
    KeyState=property(doc="<b>Read Only Property:</b> State of key.          ")
    MouseButton=property(doc="<b>Read Only Property:</b> Mouse Button.          ")
    X=property(doc="<b>Read Only Property:</b> Mouse X Position.          ")
    Y=property(doc="<b>Read Only Property:</b> Mouse Y Position.          ")
    pass

class FBEventMenu (FBEvent):
    """
    Menu event.     
         
    """
    def FBEventMenu(self,pEvent):
        """
        Constructor.

        pEvent : Base event object. 
        """
        pass

    Id=property(doc="<b>Read Write Property:</b> Id number for menu item.          ")
    Name=property(doc="<b>Read Write Property:</b> Name of menu item.          ")
    pass

class FBEventOverrideFileOpen (FBEvent):
    """
    Event that is called before a file open/merge.     
         
    """
    def FBEventOverrideFileOpen(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    FilePath=property(doc="<b>Read Only Property:</b> Path to the file that will be opened/merged.          ")
    WillOverride=property(doc="<b>Read Write Property:</b> Set to true for handling the file load, false by default. If the return value is false, MotionBuilder will proceed with the normal file open/merge process.          ")
    pass

class FBEventPlayerControlChange (FBEvent):
    """
        
        
    """
    def FBEventPlayerControlChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of event.          ")
    pass

class FBEventResize (FBEvent):
    """
    Event sent to a control that resizes.     
         
    """
    def FBEventResize(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Height=property(doc="<b>Property:</b> New Height of the window.          ")
    Width=property(doc="<b>Property:</b> New Width of the window.          ")
    pass

class FBEventSceneChange (FBEvent):
    """
    Select model event class.     
     This event occurs every time a model is:(un)selectedaddeddestroyedrenamed, etc..      
    """
    def FBEventSceneChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    ChildComponent=property(doc="<b>Read Only Property:</b> Child component of the event.          ")
    Component=property(doc="<b>Read Only Property:</b> Modified component          ")
    Type=property(doc="<b>Read Only Property:</b> Type of selection event.          ")
    pass

class FBEventShow (FBEvent):
    """
    Show event class.     
         
    """
    def FBEventShow(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Shown=property(doc="<b>Read Only Property:</b> Was layer just shown?          ")
    pass

class FBEventSpread (FBEvent):
    """
    Spreadsheet event.     
         
    """
    def FBEventSpread(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Action=property(doc="<b>Read Only Property:</b> Action associated to the spread event.          ")
    Column=property(doc="<b>Read Only Property:</b> Column of event.          ")
    Row=property(doc="<b>Read Only Property:</b> Row of event.          ")
    pass

class FBEventTakeChange (FBEvent):
    """
    Take change event class.     
     This event occurs every time a take is:addeddestroyedrenamedselected, etc.      
    """
    def FBEventTakeChange(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Take=property(doc="<b>Read Only Property:</b> The take modified.          ")
    Type=property(doc="<b>Read Only Property:</b> Type of take change event.          ")
    pass

class FBEventTransaction (FBEvent):
    """
    Transaction event.     
         
    """
    def FBEventTransaction(self,pEvent):
        """
        Constructor.

        pEvent : Base event object. 
        """
        pass

    IsBeginTransaction=property(doc="<b>Read Only Property:</b> Tells if the transaction is at begin.          ")
    pass

class FBEventTree (FBEvent):
    """
    FBTree node event.     
         
    """
    def FBEventTree(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    TreeNode=property(doc="<b>Read Write Property:</b> Tree node.          ")
    Why=property(doc="<b>Read Write Property:</b> Reason of the event.          ")
    pass

class FBEventTreeSelect (FBEvent):
    """
    FBTree selection event.b>Event: Video Frame offline Rendering Event.     
         
    """
    def FBEventTreeSelect(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    TreeNode=property(doc="<b>Read Write Property:</b> Selected tree node.          ")
    pass

class FBEventVideoFrameRendering (FBEvent):
    """
        
        
    """
    def FBEventVideoFrameRendering(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    pass

class FBExistingClipAction (Enumeration):
    """
    Action to perform, when preparing an Audio In object to record, when the action clip associated to the recording path is already in the scene.     
         
    """
    kFBExistingClipAskUser=property(doc="Ask the user for desired operation via a dialog.          ")
    kFBExistingClipRemove=property(doc="Remove the action clip from the scene.          ")
    kFBExistingClipAbortOperation=property(doc="Cancel preparing the audio in to record.          ")
    pass

class FBExistingFileAction (Enumeration):
    """
    Action to perform, when preparing an Audio In object to record, when the action clip associated to the recording path already exists on disk and is not empty.     
         
    """
    kFBExistingFileAskUser=property(doc="Ask the user for desired operation via a dialog.          ")
    kFBExistingFileOverwrite=property(doc="Overwrite the existing file on disk.          ")
    kFBExistingFileAppend=property(doc="Append the new recording to existing recording. Warning: Be sure that the current file format match your recording option!          ")
    kFBExistingFileAbortOperation=property(doc="Cancel preparing the audio in to record.          ")
    pass

class FBExtrapolationMode (Enumeration):
    """
    Modes for pre / post extrapolation.     
         
    """
    kFCurveExtrapolationConst=property(doc="        ")
    kFCurveExtrapolationRepetition=property(doc="        ")
    kFCurveExtrapolationMirrorRepetition=property(doc="        ")
    kFCurveExtrapolationKeepSlope=property(doc="        ")
    kFCurveExtrapolationRelativeRepetition=property(doc="        ")
    pass

class FBFCurveEditor (FBVisualComponent):
    """
    FCurve editor.     
    See sample: FCurveEditor.py.     
    """
    def FBFCurveEditor(self):
        """
        Constructor.

        """
        pass

    def AddAnimationNode(self,pNode):
        """
        Add an animation node to the editor.

        pNode : Animation node to show in the editor. 
        """
        pass

    def AddProperty(self,pProperty):
        """
        Add an animatable property to the editor.

        pProperty : Property to show in the editor. 
        """
        pass

    def Clear(self):
        """
        Clear the editor.

        """
        pass

    def RemoveAnimationNode(self,pNode):
        """
        Remove an animation node from the editor.

        pNode : Animation node to hide from editor. 
        """
        pass

    pass

class FBFCurveEvent (FBEvent):
    """
    This class is used when a modification is made on a FCurve.     
    It contains the necessary information to identify the owner of the curve and what modification was made.      
    """
    def FBFCurveEvent(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    Curve=property(doc="<b>Read Only Property:</b> Curve that will receive the new key.          ")
    CurveIndex=property(doc="<b>Read Only Property:</b> Index of curve.          ")
    CurveName=property(doc="<b>Read Only Property:</b> Name of curve.          ")
    EventType=property(doc="<b>Read Only Property:</b> Type of fcurve event.          ")
    KeyIndexStart=property(doc="<b>Read Only Property:</b> Index of the first key which is involved in the event.          ")
    KeyIndexStop=property(doc="<b>Read Only Property:</b> Index of the last key which is involved in the event.          ")
    pass

class FBFCurveEventType (Enumeration):
    """
    This enum indicates what modification was made to a tracked FCurve.     
         
    """
    kFBFCurveEventTypeUnknownOperation=property(doc="Invalid event.          ")
    kFBFCurveEventTypeKeyAdded=property(doc="A new key was added.          ")
    kFBFCurveEventTypeKeyRemoved=property(doc="A key was removed.          ")
    kFBFCurveEventTypeKeyTimeChanged=property(doc="A key time was changed.          ")
    kFBFCurveEventTypeKeyValueChanged=property(doc="A key value was changed.          ")
    kFBFCurveEventTypeDerivativedChanged=property(doc="A key left/right/both derivative was changed, please note that this event can affect the key specified in the event index and the following key.          ")
    kFBFCurveEventTypeKeyInterpolationChanged=property(doc="A key interpolation mode was changed.          ")
    kFBFCurveEventTypeKeyTangentChanged=property(doc="A key tangent was changed.          ")
    kFBFCurveEventTypeKeyTangentBreakChanged=property(doc="A key break mode was changed.          ")
    kFBFCurveEventTypeKeyTangentClampModeChanged=property(doc="A key clamping mode was changed.          ")
    kFBFCurveEventTypeKeyTangentConstantChanged=property(doc="A key constant mode was changed.          ")
    kFBFCurveEventTypeKeyVelocityChanged=property(doc="A key velocity was changed.          ")
    kFBFCurveEventTypeKeyWeightChanged=property(doc="A key left/right weight was changed, please note that this event can affect the key specified in the event index and the following key.          ")
    kFBFCurveEventTypeKeyTensionChanged=property(doc="A key tension was changed (only valid on TCB key)          ")
    kFBFCurveEventTypeKeyContinuityChanged=property(doc="A key continuity was changed (only valid on TCB key)          ")
    kFBFCurveEventTypeKeyBiasChanged=property(doc="A key bias was changed (only valid on TCB key)          ")
    kFBFCurveEventTypeKeyPreExtrapolationChanged=property(doc="A curve pre-extrapolation value was changed.          ")
    kFBFCurveEventTypeKeyPostExtrapolationChanged=property(doc="A curve post-extrapolation value was changed.          ")
    kFBFCurveEventTypeKeyMassOperation=property(doc="An operation affecting multiple keys was made.          ")
    pass

class FBFileFormatAndVersion (Enumeration):
    """
        
        
    """
    kFBFBX2010=property(doc="It's FBX Version 6. Note: it's not equivalent to MotionBuilder 2010 Native FBX format.          ")
    kFBFBX2011=property(doc="FBX Version 2011.          ")
    kFBFBX2012=property(doc="FBX Version 2012.          ")
    kFBFBX2013=property(doc="FBX Version 2013.          ")
    kFBFBX2014_2015=property(doc="FBX Version 2014/2015.          ")
    kFBFBX2016=property(doc="FBX Version 2016.          ")
    kFBFBX2018=property(doc="FBX Version 2018.          ")
    kFBFBX2019=property(doc="FBX Version 2019.          ")
    kFBFBX2020=property(doc="FBX Version 2020.          ")
    kFBDefaultFormatAndVersion=property(doc="Default Format and Version.          ")
    pass

class FBFileMonitoringType (Enumeration):
    """
    File Monitoring Type.     
         
    """
    kFBFileMonitoring_InvalidIndex=property(doc="Invalid value.          ")
    kFBFileMonitoring_MAINSCENE=property(doc="Main Scene change monitoring.          ")
    kFBFileMonitoring_ANIMATIONCLIP=property(doc="Animation clip change monitoring.          ")
    kFBFileMonitoring_FILEREFERENCE=property(doc="File Reference change monitoring.          ")
    kFBFileMonitoring_PYTHONEDITORSCRIPT=property(doc="Python Editor Script change monitoring.          ")
    pass

class FBFilePopup (FBVisualComponent):
    """
    File Popup (for open/save).     
    See samples: AudioTrackSetupTool.py, FBFilePopup.py.     
    """
    def FBFilePopup(self):
        """
        Constructor.

        """
        pass

    def Execute(self):
        """
        Execute file popup.

        return : <b>true</b> if <b>OK</b> is clicked by user. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to put in popup window.          ")
    FileName=property(doc="<b>Read Write Property:</b> File selected.          ")
    Filter=property(doc="<b>Read Write Property:</b> Filter to use for popup window file selection.          ")
    FullFilename=property(doc="<b>Read Only Property:</b> Full filename (path and file).          ")
    Path=property(doc="<b>Read Write Property:</b> Path of file selected.          ")
    Style=property(doc="<b>Read Write Property:</b> Style of file popup.          ")
    pass

class FBFilePopupStyle (Enumeration):
    """
    Different types of file popup windows.     
    See samples: FBFilePopup.py, FBFolderPopup.py.     
    """
    kFBFilePopupOpen=property(doc="Open file popup (Shows 'Open Directory').          ")
    kFBFilePopupSave=property(doc="Save file popup (Shows 'Save Directory').          ")
    pass

class FBFilterType (Enumeration):
    """
    Filter types.     
     A filter can be of one or both types in order to process data on single or multiple curves of data. Ex: a gimble killer filter needs to be of type vector because the three curves are inter-dependant.      
    """
    kFBFilterNumber=property(doc="Filter single FCurves.          ")
    kFBFilterVector=property(doc="Filter a vector (3 FCurves).          ")
    pass

class FBFloorContactID (Enumeration):
    """
    Floor contact for the given index.     
         
    """
    FBLeftHandMemberIndex=property(doc="        ")
    FBRightHandMemberIndex=property(doc="        ")
    FBLeftFootMemberIndex=property(doc="        ")
    FBRightFootMemberIndex=property(doc="        ")
    FBLastCharacterMember=property(doc="        ")
    pass

class FBFogMode (Enumeration):
    """
    Fog falloff modes.     
         
    """
    kFBFogModeLinear=property(doc="Linear falloff.          ")
    kFBFogModeExponential=property(doc="Exponential falloff.          ")
    kFBFogModeSquareExponential=property(doc="Squared exponential falloff.          ")
    pass

class FBFolderPopup (FBVisualComponent):
    """
    Folder Popup (for selecting a directory).     
    See samples: RenderLayers.py, BatchExportCharacterAnimationTool.py, RenameFirstTakeOnMultipleFiles.py, FBFolderPopup.py.     
    """
    def FBFolderPopup(self):
        """
        Constructor.

        """
        pass

    def Execute(self):
        """
        Execute folder popup.

        return : <b>true</b> if <b>OK</b> is clicked by user. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to put in popup window.          ")
    Path=property(doc="<b>Read Write Property:</b> Path of folder selected.          ")
    pass

class FBGapMode (Enumeration):
    """
    Gap interpolation modes.     
         
    """
    kFBGapRigidBody=property(doc="Use rigid body information.          ")
    kFBGapConstant=property(doc="Constant interpolation.          ")
    kFBGapLinear=property(doc="Linear interpolation.          ")
    kFBGapBezier=property(doc="Bezier interpolation.          ")
    kFBGapCurve=property(doc="Cubic/curve interpolation.          ")
    kFBGapSample=property(doc="Sampled data.          ")
    pass

class FBGenerationMode (Enumeration):
    """
    Generation modes for optical model.     
         
    """
    kFBGenerationNone=property(doc="No re-generation.          ")
    kFBGenerationFast=property(doc="Fast re-generation.          ")
    pass

class FBGeometryArrayElementType (Enumeration):
    """
    Type of data when requesting an array.     
         
    """
    kFBGeometryArrayElementType_Unknown=property(doc="        ")
    kFBGeometryArrayElementType_Integer=property(doc="        ")
    kFBGeometryArrayElementType_Float=property(doc="        ")
    kFBGeometryArrayElementType_Float2=property(doc="        ")
    kFBGeometryArrayElementType_Float3=property(doc="Each element is an array of 3 float.          ")
    kFBGeometryArrayElementType_Float4=property(doc="Each element is an array of 4 float.          ")
    kFBGeometryArrayElementType_FloatMatrix4x4=property(doc="        ")
    kFBGeometryArrayElementType_IntegerArrayPointer=property(doc="        ")
    pass

class FBGeometryArrayID (Enumeration):
    """
    ID to use when requesting a specific array of data for a model.     
    See sample: VertexArrayManipulation.py.     
    """
    kFBGeometryArrayID_Point=property(doc="ID to the Point array.          ")
    kFBGeometryArrayID_Normal=property(doc="ID to the Normal by Point array.          ")
    kFBGeometryArrayID_Tangent=property(doc="ID to the Tangent array.          ")
    kFBGeometryArrayID_Binormal=property(doc="ID to the Binormal array.          ")
    kFBGeometryArrayID_Color=property(doc="ID to the Vertex Color Array.          ")
    pass

class FBGeometryMappingMode (Enumeration):
    """
    Determine how the element is mapped on a surface.     
     kFBGeometryMapping_NONE The mapping is undetermined.kFBGeometryMapping_BY_CONTROL_POINT There will be one mapping coordinate for each surface control point/vertex.kFBGeometryMapping_BY_POLYGON_VERTEX There will be one mapping coordinate for each vertex, for each polygon/strip it is part of. This means that a vertex will have as many mapping coordinates as polygons it is part of.kFBGeometryMapping_BY_POLYGON There can be only one mapping coordinate for the whole polygon/strip.kFBGeometryMapping_BY_EDGE There will be one mapping coordinate for each unique edge in the mesh. This is meant to be used with smoothing layer elements.kFBGeometryMapping_ALL_SAME There can be only one mapping coordinate for the whole surface.      
    """
    kFBGeometryMapping_NONE=property(doc="        ")
    kFBGeometryMapping_BY_CONTROL_POINT=property(doc="        ")
    kFBGeometryMapping_BY_POLYGON_VERTEX=property(doc="        ")
    kFBGeometryMapping_BY_POLYGON=property(doc="        ")
    kFBGeometryMapping_BY_EDGE=property(doc="        ")
    kFBGeometryMapping_ALL_SAME=property(doc="        ")
    pass

class FBGeometryPrimitiveType (Enumeration):
    """
        
        
    """
    kFBGeometry_POINTS=property(doc="        ")
    kFBGeometry_LINES=property(doc="        ")
    kFBGeometry_LINE_LOOP=property(doc="        ")
    kFBGeometry_LINE_STRIP=property(doc="        ")
    kFBGeometry_TRIANGLES=property(doc="        ")
    kFBGeometry_TRIANGLE_STRIP=property(doc="        ")
    kFBGeometry_TRIANGLE_FAN=property(doc="        ")
    kFBGeometry_QUADS=property(doc="        ")
    kFBGeometry_QUADS_STRIP=property(doc="        ")
    kFBGeometry_POLYGON=property(doc="        ")
    pass

class FBGeometryReferenceMode (Enumeration):
    """
    Determine how the mapping information is stored in the array of coordinate.     
     kFBGeometryReference_DIRECT This indicates that the mapping information for the n'th element is found in the n'th place of DirectArray.kFBGeometryReference_INDEX, This indicates that the mapping information for the n'th element is found in the n'th place of IndexArray.kFBGeometryReference_INDEX_TO_DIRECT This indicates that the KLayerElementTemplate::mIndexArray contains, for the n'th element, an index in the KLayerElementTemplate::mDirectArray array of mapping elements. eINDEX_TO_DIRECT is usually useful to store coordinates for eBY_POLYGON_VERTEX mapping mode elements. Since the same coordinates are usually repeated a large number of times, it saves spaces to store the coordinate only one time and refer to them with an index. Materials and Textures are also referenced with this mode and the actual Material/Texture can be accessed via the KLayerElementTemplate::mDirectArray      
    """
    kFBGeometryReference_DIRECT=property(doc="        ")
    kFBGeometryReference_INDEX=property(doc="        ")
    kFBGeometryReference_INDEX_TO_DIRECT=property(doc="        ")
    pass

class FBGlobalEvalCallbackTiming (Enumeration):
    """
    Global Evaluation callback timing.     
     Let the user to register callback function at different stage of background evaluation.      
    """
    kFBGlobalEvalCallbackBeforeDAG=property(doc="Invoked before any DAG (Transformation & Deformation) evaluation tasks started in evaluation pipeline / thread.          ")
    kFBGlobalEvalCallbackAfterDAG=property(doc="Invoked after all DAG (Transformation & Deformation) evaluation tasks finished in evaluation pipeline / thread.          ")
    kFBGlobalEvalCallbackAfterDeform=property(doc="Invoked after all deformation tasks finished in evaluation pipeline / thread.          ")
    kFBGlobalEvalCallbackSyn=property(doc="Invoked when both evaluation & rendering pipelines / threads are stopped. Useful for some complicated scene change tasks to avoid race condition.          ")
    kFBGlobalEvalCallbackBeforeRender=property(doc="Invoked in rendering pipeline, before any rendering tasks start (immediately after clearing GL back buffer).          ")
    kFBGlobalEvalCallbackAfterRender=property(doc="Invoked in rendering pipeline, after any rendering tasks finish (just before swapping GL back/front buffer).          ")
    kFBGlobalEvalCallbackBeforePlottingFrame=property(doc="Invoked before plotting a frame.          ")
    kFBGlobalEvalCallbackAfterPlottingFrame=property(doc="Invoked after plotting a frame.          ")
    pass

class FBHUDElementHAlignment (Enumeration):
    """
        
        
    """
    kFBHUDLeft=property(doc="Left alignment.          ")
    kFBHUDRight=property(doc="Right alignment.          ")
    kFBHUDCenter=property(doc="Center.          ")
    pass

class FBHUDElementVAlignment (Enumeration):
    """
        
        
    """
    kFBHUDBottom=property(doc="Bottom alignment.          ")
    kFBHUDTop=property(doc="Top alignment.          ")
    kFBHUDVCenter=property(doc="Center.          ")
    pass

class FBIconPosition (Enumeration):
    """
    Different icon positions possible.     
         
    """
    kFBIconLeft=property(doc="Icon on left of text.          ")
    kFBIconTop=property(doc="Icon on top of text.          ")
    pass

class FBImageContainer (FBVisualComponent):
    """
    Image.     
    See sample: ImageContainer.py.     
    """
    def FBImageContainer(self):
        """
        Constructor.

        """
        pass

    Filename=property(doc="<b>Read Write Property:</b> Filename for image.          ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop.          ")
    pass

class FBImageFormat (Enumeration):
    """
    Image formats.     
         
    """
    kFBImageFormatRGBA32=property(doc="        ")
    kFBImageFormatRGB24=property(doc="        ")
    kFBImageFormatBGRA32=property(doc="        ")
    kFBImageFormatBGR24=property(doc="        ")
    kFBImageFormatBGR16=property(doc="        ")
    kFBImageFormatABGR32=property(doc="        ")
    kFBImageFormatARGB32=property(doc="        ")
    kFBImageFormatUnknown=property(doc="        ")
    pass

class FBImageInterleaveType (Enumeration):
    """
    Image field interleave types.     
         
    """
    kFBImageInterleaveTypeFullFrame=property(doc="        ")
    kFBImageInterleaveTypeOdd=property(doc="        ")
    kFBImageInterleaveTypeEven=property(doc="        ")
    kFBImageInterleaveTypeAverage=property(doc="        ")
    pass

class FBImageInterpolationType (Enumeration):
    """
    Image interpolation types.     
         
    """
    kFBImageInterpolationTypeNone=property(doc="        ")
    kFBImageInterpolationTypeDuplicate=property(doc="        ")
    kFBImageInterpolationTypeLinear=property(doc="        ")
    pass

class FBImageType (Enumeration):
    """
    Image types.     
         
    """
    kFBImageTypeFrame=property(doc="        ")
    kFBImageTypeField=property(doc="        ")
    pass

class FBInputKey (Enumeration):
    """
    Keyboard inputs.     
         
    """
    kFBKeyReturn=property(doc="Return.          ")
    kFBKeyBackSpace=property(doc="Backspace.          ")
    kFBKeyTab=property(doc="Tab.          ")
    kFBKeyEscape=property(doc="Escape.          ")
    kFBKeyPageUp=property(doc="Page Up.          ")
    kFBKeyPageDown=property(doc="Page Down.          ")
    kFBKeyEnd=property(doc="End.          ")
    kFBKeyHome=property(doc="Home.          ")
    kFBKeyLeft=property(doc="Left.          ")
    kFBKeyUp=property(doc="Up.          ")
    kFBKeyRight=property(doc="Right.          ")
    kFBKeyDown=property(doc="Down.          ")
    kFBKeyIns=property(doc="Insert.          ")
    kFBKeyDel=property(doc="Delete.          ")
    kFBKeyF1=property(doc="F1.          ")
    kFBKeyF2=property(doc="F2.          ")
    kFBKeyF3=property(doc="F3.          ")
    kFBKeyF4=property(doc="F4.          ")
    kFBKeyF5=property(doc="F5.          ")
    kFBKeyF6=property(doc="F6.          ")
    kFBKeyF7=property(doc="F7.          ")
    kFBKeyF8=property(doc="F8.          ")
    kFBKeyF9=property(doc="F9.          ")
    kFBKeyF10=property(doc="F10.          ")
    kFBKeyF11=property(doc="F11.          ")
    kFBKeyF12=property(doc="F12.          ")
    pass

class FBInputModifier (Enumeration):
    """
    Input Modifiers (Ctrl, Alt, Shift).     
         
    """
    kFBKeyNone=property(doc="No modifier.          ")
    kFBKeyShift=property(doc="Shift was pressed.          ")
    kFBKeyCtrl=property(doc="Control was pressed.          ")
    kFBKeyAlt=property(doc="Alt was pressed.          ")
    pass

class FBInputType (Enumeration):
    """
    Types of input events.     
    See sample: KeyboardMapper.py.     
    """
    kFBKeyPress=property(doc="A keyboard key was pressed.          ")
    kFBKeyRelease=property(doc="A keyboard key was released.          ")
    kFBButtonPress=property(doc="A mouse button was pressed.          ")
    kFBButtonRelease=property(doc="A mouse button was released.          ")
    kFBMotionNotify=property(doc="The mouse has been moved.          ")
    kFBButtonDoubleClick=property(doc="A mouse button was double clicked.          ")
    kFBMouseEnter=property(doc="The mouse pointer is entering the window.          ")
    kFBMouseLeave=property(doc="The mouse pointer is leaving the window.          ")
    kFBMouseWheelNotify=property(doc="The mouse wheel has moved.          ")
    kFBDragging=property(doc="The mouse is dragging items.          ")
    kFBDropping=property(doc="The mouse is dropping items.          ")
    kFBKeyPressRaw=property(doc="A keyboard key was pressed.          ")
    kFBKeyReleaseRaw=property(doc="A keyboard key was released.          ")
    kFBUnknownInput=property(doc="The internal event could not be translated.          ")
    pass

class FBInsertSegmentMode (Enumeration):
    """
    Insert segment modes.     
         
    """
    kFBInsertSegmentWhole=property(doc="Insert whole.          ")
    kFBInsertSegmentToEnd=property(doc="Insert to end.          ")
    kFBInsertSegmentFromStart=property(doc="Insert from start.          ")
    pass

class FBInterpolation (Enumeration):
    """
    Types of interpolation for an FCurve.     
         
    """
    kFBInterpolationConstant=property(doc="Constant interpolation.          ")
    kFBInterpolationLinear=property(doc="Linear interpolation.          ")
    kFBInterpolationCubic=property(doc="Cubic interpolation.          ")
    kFBInterpolationCustom=property(doc="Custom interpolation.          ")
    pass

class FBInterpolatorCurveType (Enumeration):
    """
    Types of interpolator for an FCurve.     
         
    """
    kFBInterpolatorCurveLinearIn=property(doc="        ")
    kFBInterpolatorCurveLinearOut=property(doc="        ")
    kFBInterpolatorCurveSmoothIn=property(doc="        ")
    kFBInterpolatorCurveSmoothOut=property(doc="        ")
    kFBInterpolatorCurveSlowIn=property(doc="        ")
    kFBInterpolatorCurveSlowOut=property(doc="        ")
    kFBInterpolatorCurveFastIn=property(doc="        ")
    kFBInterpolatorCurveFastOut=property(doc="        ")
    kFBInterpolatorCurveLast=property(doc="        ")
    pass

class FBKeyingGroupType (Enumeration):
    """
    Keying group types.     
         
    """
    kFBKeyingGroupGlobal=property(doc="All selected objects with the same properties as those defined in the keying group will be keyed.          ")
    kFBKeyingGroupObjectType=property(doc="All selected objects of the specified type in the keying group with the same properties as those defined in the keying group will be keyed.          ")
    kFBKeyingGroupLocal=property(doc="Only properties of objects specified in the keying group will be keyed.          ")
    pass

class FBLabel (FBVisualComponent):
    """
    Text label.     
    See sample: Label.py.     
    """
    def FBLabel(self):
        """
        Constructor.

        """
        pass

    Justify=property(doc="<b>Read Write Property:</b> Text justification for label.          ")
    Style=property(doc="<b>Read Write Property:</b> Text style appearance.          ")
    WordWrap=property(doc="<b>Read Write Property:</b> Enable wordwrap on text drawing.          ")
    pass

class FBLayerMode (Enumeration):
    """
    Layer mode.     
         
    """
    kFBLayerModeInvalidIndex=property(doc="Invalid value.          ")
    kFBLayerModeAdditive=property(doc="Layer value will be added to the other layers to computed the final value.          ")
    kFBLayerModeOverride=property(doc="Layer value will override the value of the other precedent layers.          ")
    kFBLayerModeOverridePassthrough=property(doc="If the layer has a weight of 75%, the precedent layers will have a combined effect of 25% on the final value. Setting the weight to 100% is similar to setting the layer in override.          ")
    pass

class FBLayerRotationMode (Enumeration):
    """
    Rotation mode for layer.     
         
    """
    kFBLayerRotationModeInvalidIndex=property(doc="Invalid value.          ")
    kFBLayerRotationModeEulerRotation=property(doc="The rotation will be computed component by component.          ")
    kFBLayerRotationModeQuaternionRotation=property(doc="The rotation will be computed using quaternion.          ")
    pass

class FBLayout (FBVisualComponent):
    """
    Used to build the user interface.     
     Layouts manage areas of the screen called regions. Regions contain UI components such as buttons, viewers, and edit boxes. Regions are added to layouts. When a UI component is bound to a region, the region defines how big it is and how it behaves when the layout is resized.<b>Types of Layouts</b> Device Constraint Manipulator Shader A region is first defined using the FBLayout::AddRegion() function. Once a region is defined and the corresponding UI component is created, and the component is bound to its region with FBLayout::SetControl(). You can use the FBSystem::OnUIIdle() in your layout to update real-time UI components such as guages and status indicators. In Python, FBBoxLayout and FBGridLayout take care of most of the region handling. They are used to create basic control layouts for simple tools. If you have a lot of content you can use FBScrollBox to manage it. For an example, see the Python sample Scrollbox.py.* Also see the Python sample Layout.py, and the C++ sample ortooluidemo. See samples: KeyboardMapper.py, ShotTrackSetupTool.py, Attach.py, Border.py, Layout.py.     
    """
    def FBLayout(self):
        """
        Constructor.

        """
        pass

    def AddRegion(self,pName,pTitle,pX,pXType,pXRelative,pMultX,pY,pYType,pYRelative,pMultY,pW,pWType,pWRelative,pMultW,pH,pHType,pHRelative,pMultH):
        """
        Add a region to the layout.

        pName : Name of region. 
        pTitle : Title to display. 
        pX : X: Position. 
        pXType : X: Type of attachment. 
        pXRelative : X: Item to attach to. 
        pMultX : X: Multiplier of relative value. 
        pY : Y: Position. 
        pYType : Y: Type of attachment. 
        pYRelative : Y: Item to attach to. 
        pMultY : Y: Multiplier of relative value. 
        pW : W: Width of region. 
        pWType : W: Type of attachment. 
        pWRelative : W: Item to attach to. 
        pMultW : W: Multiplier of relative value. 
        pH : H: Height of region. 
        pHType : H: Type of attachment. 
        pHRelative : H: Item to attach to. 
        pMultH : H: Multiplier of relative value. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ClearControl(self,pName):
        """
        Remove a control from a region in a visual component.

        pName : Name of region to remove control. 
        """
        pass

    def GetControl(self,pName):
        """
        Get control of a region in a visual component.

        pName : Name of region to find. 
        return : The component if it is found. 
        """
        pass

    def GetRegion(self,pName):
        """
        Verify if a region with pName exists.

        pName : Name of region to check. 
        return : Operation was successful (true or false). 
        """
        pass

    def GetRegionPositions(self,pName,pComputed,pX,pY,pW,pH):
        """
        Get region <b>pName</b> information (position and size)

        pName : Name of region. 
        pComputed : Is the information retrieved relative or absolute? 
        pX : Position in X of the region. 
        pY : Position in Y of the region. 
        pW : Width of the region. 
        pH : Height of the region. 
        return : Operation was successful (true or false). 
        """
        pass

    def GetSplitStyle(self,pName):
        """
        Get a region's splitstyle.

        pName : Name of Region to get splitstyle from. 
        return : Split style of specified region. 
        """
        pass

    def MoveRegion(self,pName,pX,pY):
        """
        Move a region.

        pName : Name of region to move. 
        pX : New X position. 
        pY : New Y position. 
        return : Operation was successful (true or false). 
        """
        pass

    def RemoveRegion(self,pName):
        """
        Remove a region.

        pName : Name of region to remove. 
        return : Operation was successful (true or false). 
        """
        pass

    def RenameRegion(self,pOldName,pNewName):
        """
        Rename a region.

        pOldName : Region's old name. 
        pNewName : Region's new name. 
        return : Operation was successful (true or false). 
        """
        pass

    def Restructure(self,pNoMove):
        """
        Force a recomputation of all region placements in the layout.

        pNoMove : bool
        """
        pass

    def SetAutoRestructure(self,pAutoRestructure):
        """
        Suspend all automatic layout recomputation.

        pAutoRestructure : If true, Suspend all automatic layout recomputation, else restore it. 
        """
        pass

    def SetBorder(self,pName,pType,pShowTitle,pInSet,pWidth,pSpacing,pMaxAngle,pCornerRadius):
        """
        Set border properties for a region.

        pName : Name of Region to change border properties. 
        pType : Border style to use. 
        pShowTitle : Show region title? 
        pInSet : Is region inset? 
        pWidth : Border width. 
        pSpacing : Border spacing. 
        pMaxAngle : Max angle for rounding. 
        pCornerRadius : Corner radius for rounding. 
        return : Operation was successful (true or false). 
        """
        pass

    def SetControl(self,pName,pComponent):
        """
        Set control of a region to a visual component.

        pName : Name of region to affect. 
        pComponent : Component to control region. 
        return : Operation was successful (true or false). 
        """
        pass

    def SetControl(self,pName,pComponent):
        """
        pName : str
        pComponent : FBVisualComponent
        """
        pass

    def SetRegionTitle(self,pName,pTitle):
        """
        Set a region's title.

        pName : Name of region to change title. 
        pTitle : New title for region. 
        return : Operation was successful (true or false). 
        """
        pass

    def SetSplitStyle(self,pName,pRegionType):
        """
        Set a region's splitstyle.

        pName : Name of Region to set splitstyle. 
        pRegionType : Split style give to region. 
        return : Operation was successful (true or false). 
        """
        pass

    def SetView(self,pName,pComponent):
        """
        Set view.

        pName : Name of Region. 
        pComponent : Component to set as view. 
        return : Operation was successful (true or false). 
        """
        pass

    def SetView(self,pName,pComponent):
        """
        pName : str
        pComponent : FBVisualComponent
        """
        pass

    def SizeRegion(self,pName,pW,pH):
        """
        Change a region's size.

        pName : Name of region to resize. 
        pW : New region width. 
        pH : New region height. 
        return : Operation was successful (true or false). 
        """
        pass

    OnIdle=property(doc="<b>Event:</b> Idle.          ")
    OnInput=property(doc="<b>Event:</b> Input.          ")
    OnPaint=property(doc="<b>Event:</b> Paint layout.          ")
    OnResize=property(doc="<b>Event:</b> Resize layout.          ")
    OnShow=property(doc="<b>Event:</b> Show layout.          ")
    pass

class FBLayoutRegion (FBVisualComponent):
    """
    Layout region.     
         
    """
    def FBLayoutRegion(self):
        """
        Constructor.

        """
        pass

    pass

class FBLightType (Enumeration):
    """
    Light types.     
         
    """
    kFBLightTypePoint=property(doc="Point light.          ")
    kFBLightTypeInfinite=property(doc="Infinite light (plane).          ")
    kFBLightTypeSpot=property(doc="Spot light.          ")
    kFBLightTypeArea=property(doc="Area light.          ")
    pass

class FBList (FBVisualComponent):
    """
    List of items.     
    See samples: List.py, ToolCommunicationReceiver.py.     
    """
    def FBList(self):
        """
        Constructor.

        """
        pass

    def IsSelected(self,pIndex):
        """
        Returns whether or not the item <b>pIndex</b> is currently selected.

        pIndex : Index to see if select or not. 
        return : <b>true</b> if item at <b>pIndex</b> is selected. 
        """
        pass

    def Selected(self,pIndex,pSelected):
        """
        Set the current selected state of item at <b>pIndex</b> to <b>pSelected</b>.

        pIndex : Index to affect item at. 
        pSelected : State to set item at <b>pIndex</b> to. 
        """
        pass

    ExtendedSelect=property(doc="<b>Read Write Property:</b> Extended selection state?          ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current item index.          ")
    Items=property(doc="<b>List:</b> Names of items in list.          ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Can multiple items be selected?          ")
    OnChange=property(doc="<b>Event:</b> List changed.          ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop event.          ")
    Style=property(doc="<b>Read Write Property:</b> Style or direction of list.          ")
    pass

class FBListStyle (Enumeration):
    """
    List style or direction.     
    See samples: List.py, ToolCommunicationReceiver.py.     
    """
    kFBDropDownList=property(doc="Drop down list.          ")
    kFBVerticalList=property(doc="Vertical list.          ")
    pass

class FBManipulatorPickType (Enumeration):
    """
    Types of manipulator picking.     
         
    """
    FBPickObjects=property(doc="Pick objects.          ")
    FBPickPoints=property(doc="Pick points.          ")
    FBPickSurfaces=property(doc="Pick surfaces.          ")
    pass

class FBManipulatorTransformType (Enumeration):
    """
    Manipulator transform stles.     
         
    """
    kFBManipulatorTransformNone=property(doc="No manipulator.          ")
    kFBManipulatorTransformTranslation=property(doc="Translation manipulator.          ")
    kFBManipulatorTransformRotation=property(doc="Rotation manipulator.          ")
    kFBManipulatorTransformScaling=property(doc="Scaling manipulator.          ")
    pass

class FBMarkerLook (Enumeration):
    """
    Look of the marker.     
         
    """
    kFBMarkerLookCube=property(doc="Cube.          ")
    kFBMarkerLookHardCross=property(doc="Thick cross.          ")
    kFBMarkerLookLightCross=property(doc="Wireframe cross.          ")
    kFBMarkerLookSphere=property(doc="Sphere.          ")
    kFBMarkerLookCapsule=property(doc="Capsule.          ")
    kFBMarkerLookSquare=property(doc="Square.          ")
    kFBMarkerLookCircle=property(doc="Circle.          ")
    kFBMarkerLookBone=property(doc="Bone.          ")
    kFBMarkerLookStick=property(doc="Box with a sphere on one end.          ")
    kFBMarkerLookBox=property(doc="Box.          ")
    kFBMarkerLookNone=property(doc="None.          ")
    kFBMarkerLookRigidGoal=property(doc="Rigid goal.          ")
    kFBMarkerLookRotationGoal=property(doc="Rotation goal.          ")
    kFBMarkerLookAimRollGoal=property(doc="Aim & Roll goal.          ")
    pass

class FBMarkerResolutionLevel (Enumeration):
    """
    Resolution of marker mesh sphere and capsule (Quality).     
         
    """
    kFBMarkerLowResolution=property(doc="Lowest resolution.          ")
    kFBMarkerMediumResolution=property(doc="Medium resolution.          ")
    kFBMarkerHighResolution=property(doc="Highest resolution.          ")
    pass

class FBMarkerType (Enumeration):
    """
    Type of the marker.     
         
    """
    kFBMarkerTypeStandard=property(doc="Standard.          ")
    kFBMarkerTypeOptical=property(doc="Optical.          ")
    kFBMarkerTypeFKEffector=property(doc="FK effector.          ")
    kFBMarkerTypeIKEffector=property(doc="IK effector.          ")
    pass

class FBMaterialTextureType (Enumeration):
    """
    Various Material texture channels' type.     
    See samples: LayeredTexture.py, MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py.     
    """
    kFBMaterialTextureEmissive=property(doc="        ")
    kFBMaterialTextureEmissiveFactor=property(doc="        ")
    kFBMaterialTextureAmbient=property(doc="        ")
    kFBMaterialTextureAmbientFactor=property(doc="        ")
    kFBMaterialTextureDiffuse=property(doc="        ")
    kFBMaterialTextureDiffuseFactor=property(doc="        ")
    kFBMaterialTextureSpecular=property(doc="        ")
    kFBMaterialTextureSpecularFactor=property(doc="        ")
    kFBMaterialTextureShiness=property(doc="        ")
    kFBMaterialTextureBump=property(doc="        ")
    kFBMaterialTextureNormalMap=property(doc="        ")
    kFBMaterialTextureTransparent=property(doc="        ")
    kFBMaterialTextureTransparentFactor=property(doc="        ")
    kFBMaterialTextureReflection=property(doc="        ")
    kFBMaterialTextureReflectionFactor=property(doc="        ")
    pass

class FBMenuItemType (Enumeration):
    """
    Types of menu items available.     
         
    """
    kFBMenuItemMotionImport=property(doc="Motion Files->Import.          ")
    kFBMenuItemSceneImport=property(doc="Scenes->Import.          ")
    kFBMenuItemMotionExport=property(doc="Motion Files->Export.          ")
    kFBMenuItemSceneExport=property(doc="Scenes->Export.          ")
    pass

class FBMergeLayerMode (Enumeration):
    """
    Merge layer mode for animation layers.     
    This will specify the mode of the resulting merged layer, if applicable (To BaseAnimation layer mode cannot be modified).      
    """
    kFBMergeLayerModeAutomatic=property(doc="The resulting layer will be in override mode if one of the source layer is in override, otherwise, it will be in additive mode.          ")
    kFBMergeLayerModeAdditive=property(doc="The resulting layer will be in additive mode, if possible.          ")
    kFBMergeLayerModeOverride=property(doc="The resulting layer will be in override mode, if possible.          ")
    pass

class FBMirrorPlaneType (Enumeration):
    """
    Mirror Plane Type.     
         
    """
    kFBMirrorPlaneTypeInvalid=property(doc="        ")
    kFBMirrorPlaneTypeAuto=property(doc="        ")
    kFBMirrorPlaneTypeZY=property(doc="        ")
    kFBMirrorPlaneTypeXY=property(doc="        ")
    kFBMirrorPlaneTypeXZ=property(doc="        ")
    kFBMirrorPlaneTypeUser=property(doc="        ")
    kFBMirrorPlaneTypeEquation=property(doc="        ")
    kFBMirrorPlaneTypeCount=property(doc="        ")
    pass

class FBModelCullingMode (Enumeration):
    """
    Model Culling Mode.     
         
    """
    kFBCullingOff=property(doc="Culling Off.          ")
    kFBCullingOnCCW=property(doc="Culling with Counter Clock Wise.          ")
    kFBCullingOnCW=property(doc="Culling with Clock Wise.          ")
    pass

class FBModelEvaluationTaskType (Enumeration):
    """
        
        
    """
    kFBModelEvaluationTransform=property(doc="Model's transformation evaluation task (Global )          ")
    kFBModelEvaluationBBox=property(doc="Model's bouding box computation task (approximately for deformable model)          ")
    kFBModelEvaluationDeform=property(doc="Model's deformation task (for deformable model)          ")
    pass

class FBModelHiercharyTraverserType (Enumeration):
    """
    Types of hierarchy traverser search type.     
         
    """
    kModelTraverserDepthFirst=property(doc="Depth-first search.          ")
    kModelTraverserBreadthFirst=property(doc="Breadth-first search.          ")
    pass

class FBModelRotationOrder (Enumeration):
    """
    Ways to apply Rotation.     
         
    """
    kFBEulerXYZ=property(doc="XYZ Euler Order.          ")
    kFBEulerXZY=property(doc="XZY Euler Order.          ")
    kFBEulerYZX=property(doc="YZX Euler Order.          ")
    kFBEulerYXZ=property(doc="YXZ Euler Order.          ")
    kFBEulerZXY=property(doc="ZXY Euler Order.          ")
    kFBEulerZYX=property(doc="ZYX Euler Order.          ")
    kFBSphericXYZ=property(doc="Spheric XYZ Order.          ")
    pass

class FBModelSelection (Enumeration):
    """
    Different model selection available.     
         
    """
    kFBNone=property(doc="No selection mode specified.          ")
    kFBCreateModels=property(doc="Will create the models in the motion file, used when there is no model to match in the scene.          ")
    kFBSelectedModels=property(doc="Will Merges data with only the selected nodes or models.          ")
    kFBSelectedModelAndChildren=property(doc="Will try to match the models from the file to those selected in the scene, as well as the children of the selected models.          ")
    kFBPrefixGroupContainingModel=property(doc="Will finds the top node with the same prefix and imports the motion as if you selected kFBInHierarchy. If the selected node has the prefix, this merge option is the same as selecting kFBSelectedModelAndChildren. If no nodes are found with the prefix, this merge option operates the same as kFBSelectedModels. Only available when one model is selected.          ")
    kFBInHierarchy=property(doc="Will find the root node and will try to merge the data on the hierarchy, only useful if one model is selected.          ")
    kFBAllModels=property(doc="Will imports motion into the hierarchies of all models in your scene. This is the only merge option when nothing is selected.          ")
    pass

class FBModelShadingMode (Enumeration):
    """
    Modes for model shading.     
    See samples: FBModelCube.py, GeometryInstancing.py, VertexArrayManipulation.py, VertexColor.py.     
    """
    kFBModelShadingDefault=property(doc="Default shading.          ")
    kFBModelShadingWire=property(doc="Wireframe shading.          ")
    kFBModelShadingFlat=property(doc="Flat shading.          ")
    kFBModelShadingLight=property(doc="Lighted shading.          ")
    kFBModelShadingHard=property(doc="Hard shading.          ")
    kFBModelShadingTexture=property(doc="Textured shading.          ")
    kFBModelShadingAll=property(doc="Lighted, shaded, textured shading.          ")
    pass

class FBModelTemplateStyle (Enumeration):
    """
    Model template styles When creating model templates, this parameter will affect the actual model created (associated with the model template).     
         
    """
    kFBModelTemplateNone=property(doc="No style.          ")
    kFBModelTemplateNull=property(doc="Null.          ")
    kFBModelTemplateMarker=property(doc="Marker.          ")
    kFBModelTemplateRoot=property(doc="Root (3 axes).          ")
    kFBModelTemplateSensor=property(doc="Yellow magnetic sensor.          ")
    kFBModelTemplateSkeleton=property(doc="Skeleton limb.          ")
    kFBModelTemplateCamera=property(doc="Camera.          ")
    kFBModelTemplateGeometry=property(doc="Generic geometry.          ")
    kFBModelTemplateCameraInterest=property(doc="Camera interest.          ")
    kFBModelTemplateLight=property(doc="Light.          ")
    kFBModelTemplateOptical=property(doc="Optical model (not supported yet).          ")
    pass

class FBModelTransformationType (Enumeration):
    """
    Types of transformation vector/matrices possible.     
    See samples: FBModelCube.py, GeometryInstancing.py, VertexArrayManipulation.py.     
    """
    kModelTransformation=property(doc="Transformation.          ")
    kModelRotation=property(doc="Rotation.          ")
    kModelTranslation=property(doc="Translation.          ")
    kModelScaling=property(doc="Scaling.          ")
    kModelTransformation_Geometry=property(doc="Transformation plus geometry offset          ")
    kModelInverse_Transformation=property(doc="Inverse transformation.          ")
    kModelInverse_Rotation=property(doc="Inverse rotation.          ")
    kModelInverse_Translation=property(doc="Inverse translation.          ")
    kModelInverse_Scaling=property(doc="Inverse scaling.          ")
    kModelInverse_Transformation_Geometry=property(doc="Inverse of transformation plus geometry offset.          ")
    pass

class FBNamespaceAction (Enumeration):
    """
    Namespace flags.     
    See samples: FBGetSelectedModels.py, FBGroup.py.     
    """
    kFBConcatNamespace=property(doc="Use to add a namespace name to object.          ")
    kFBReplaceNamespace=property(doc="Use to replace a define namespace.          ")
    kFBRemoveAllNamespace=property(doc="Remove all the namespace name.          ")
    pass

class FBNewKeyInterpolationType (Enumeration):
    """
    Key Interpolation Type to use when creating new keys.     
         
    """
    kFBNewKeyInterpolation_None=property(doc="Invalid interpolation type, could be returned by the system if it is in an uninitialized state. Don't use this mode.          ")
    kFBNewKeyInterpolation_Auto=property(doc="Auto interpolation type.          ")
    kFBNewKeyInterpolation_Spline=property(doc="Spline interpolation type.          ")
    kFBNewKeyInterpolation_SplineClamp=property(doc="Spline Clamp interpolation type.          ")
    kFBNewKeyInterpolation_Linear=property(doc="Linear interpolation type.          ")
    kFBNewKeyInterpolation_Step=property(doc="Step interpolation type.          ")
    kFBNewKeyInterpolation_TCB=property(doc="TCB interpolation type.          ")
    kFBNewKeyInterpolation_Smooth=property(doc="Smooth interpolation type.          ")
    kFBNewKeyInterpolation_SmoothClamp=property(doc="Smooth Clamp interpolation type.          ")
    kFBNewKeyInterpolation_Fixed=property(doc="Fixed interpolation type.          ")
    kFBNewKeyInterpolation_Custom0=property(doc="Custom 0 interpolation type.          ")
    kFBNewKeyInterpolation_Custom1=property(doc="Custom 1 interpolation type.          ")
    kFBNewKeyInterpolation_Custom2=property(doc="Custom 2 interpolation type.          ")
    pass

class FBNurbType (Enumeration):
    """
    Surface types.     
         
    """
    kFBNurbTypePeriodic=property(doc="Periodic Type Nurb.          ")
    kFBNurbTypeClosed=property(doc="Closed Type Nurb.          ")
    kFBNurbTypeOpen=property(doc="Open Type Nurb.          ")
    pass

class FBObjectFlag (Enumeration):
    """
    Available flags for any component.     
         
    """
    kFBFlagSelectable=property(doc="Can be selected. If disabled, representation of the object, like in the navigator, can still be selected and can still affect the original object.          ")
    kFBFlagDeletable=property(doc="Can be deleted.          ")
    kFBFlagSavable=property(doc="Can be saved.          ")
    kFBFlagVisible=property(doc="Can be visible. If disabled, the object will still be available in the navigator, it is only hidden in the viewer.          ")
    kFBFlagClonable=property(doc="Can be cloned. If disabled, the 'Duplicate' option will be removed in the contextual menu.          ")
    kFBFlagSystem=property(doc="Created from System (not from user)          ")
    kFBFlagNewable=property(doc="Deleted on File->New.          ")
    kFBFlagRenamable=property(doc="Can be renamed.          ")
    kFBFlagMergeable=property(doc="Can be merged.          ")
    kFBFlagBrowsable=property(doc="Visible in the Scene Navigator/Schematic View/Property View/Model View. If disabled, the object representation in the navigator will not be visible. In the Schematic View, system object are not shown and other objects will still be visible, but a red X will be drawn on them. It is not possible to select the object in the Schematic View. After disabling that flag of a selected object, it will still be selected to allow a script based on selection to work. It will then be possible for a user to deselect the object, but it will not be possible to select it.          ")
    kFBFlagParentable=property(doc="Object (model) can be 'parented'. Used by the apply manager contextual menu.          ")
    kFBFlagDetachable=property(doc="Object can be 'detached'. Used by the apply manager contextual menu.          ")
    kFBFlagUndoable=property(doc="Object can undo its actions and states, in a global Undo Stack.          ")
    kFBFlagUndoableSeparately=property(doc="Object which has kFlagUndoableSeparately flag turned on will have a separate Undo Stack.          ")
    kFBFlagKeyable=property(doc="Object can Key his property. (System Camera can't)          ")
    kFBFlagAllocated=property(doc="Object is allocated, so it must call 'delete this' on destroy.          ")
    kFBFlagStory=property(doc="Object created/used by the Story tool. Useful flag for filtering Story objects.          ")
    kFBFlagStorable6=property(doc="System/Obsolete.          ")
    kFBFlagStorableData6=property(doc="System/Obsolete.          ")
    kFBFlagUniqueName=property(doc="< Used in FBX SDK native IO, force bindary format for the bindary data.          ")
    kFBFlagNamespaceEditable=property(doc="Allow editing on the namespace objects. If disabled, the 'Add/Remove Namespace...' option is removed from the contextual menu.          ")
    pass

class FBObjectPoseMirrorOptionsFlag (Enumeration):
    """
    ObjectPoseMirrorOptions flags.     
         
    """
    kFBObjectPoseMirrorOptionsNoFlag=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocal=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalMirrorParent=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalRef=property(doc="        ")
    kFBObjectPoseMirrorOptionsUpdateLocalRefMirrorRef=property(doc="        ")
    pass

class FBObjectPoseOptionsFlag (Enumeration):
    """
    ObjectPoseOptions flags.     
         
    """
    kFBObjectPoseOptionsNoFlag=property(doc="        ")
    kFBObjectPoseOptionsTranslationX=property(doc="        ")
    kFBObjectPoseOptionsTranslationY=property(doc="        ")
    kFBObjectPoseOptionsTranslationZ=property(doc="        ")
    kFBObjectPoseOptionsRotation=property(doc="        ")
    kFBObjectPoseOptionsScaling=property(doc="        ")
    pass

class FBObjectStatus (Enumeration):
    """
    Available lifetime status for any component.     
         
    """
    kFBStatusCreating=property(doc="Object is in creation operations.          ")
    kFBStatusStoring=property(doc="Object is in storing operations.          ")
    kFBStatusRetrieving=property(doc="Object is in retrieving operations.          ")
    kFBStatusMerging=property(doc="Object is in Merging operations.          ")
    kFBStatusDestroying=property(doc="Object is in destruction operations.          ")
    kFBStatusClearing=property(doc="Object is in clearing operations (File new).          ")
    pass

class FBOneClickApplication (Enumeration):
    """
    Possible application for One-Click interop with MotionBuilder.     
         
    """
    kFBOneClickNone=property(doc="No application.          ")
    kFBOneClickMaya=property(doc="Maya.          ")
    kFBOneClick3dsMax=property(doc="3ds Max.          ")
    kFBOneClickSoftimage=property(doc="Softimage.          ")
    pass

class FBOrientation (Enumeration):
    """
    General directions for UI components.b> DEPRICATED use ParallelEvaluation on FBEvaluateManager insteadAvailable DAG parallel schedule algorithm      
    See samples: Container.py, Slider.py.     
    """
    kFBHorizontal=property(doc="Horizontal.          ")
    kFBVertical=property(doc="Vertical          ")
    pass

class FBParallelScheduleType (Enumeration):
    """
        
        
    """
    kFBParallelScheduleSerial=property(doc="No parallel schedule, use sequential evaluation order instead.          ")
    kFBParallelScheduleSimple=property(doc="Simple parallel schedule, mainly analyze the task dependency based on Motion Hierarchy (scene graph), but don't across active constraint.          ")
    kFBParallelScheduleAdvanced=property(doc="Advanced parallel schedule, task dependency analyzation will be able to across ative constraint, and plus motion hierarchy.          ")
    pass

class FBParity (Enumeration):
    """
    Parity modes.     
         
    """
    kFBParityNone=property(doc="No parity.          ")
    kFBParityOdd=property(doc="Odd parity.          ")
    kFBParityEven=property(doc="Even parity.          ")
    pass

class FBPickingMode (Enumeration):
    """
    3D picking mode.     
         
    """
    kFBPickingModeStandard=property(doc="Standard picking mode.          ")
    kFBPickingModeXRay=property(doc="X-Ray picking mode (obstructed models are displayed in overlay).          ")
    kFBPickingModeModelsOnly=property(doc="Models-only mode (no nulls or skeletons are displayed).          ")
    kFBPickingModeCount=property(doc="End of enum, this valued indicates the number of picking modes available.          ")
    pass

class FBPlayerControlChangeType (Enumeration):
    """
    Types of player control change events.     
         
    """
    kFBPlayerControlNone=property(doc="None.          ")
    kFBPlayerControlPlay=property(doc="Play.          ")
    kFBPlayerControlPlayReverse=property(doc="Play reverse.          ")
    kFBPlayerControlStop=property(doc="Stop.          ")
    kFBPlayerControlStepForward=property(doc="Step forward.          ")
    kFBPlayerControlStepBackward=property(doc="Step backward.          ")
    kFBPlayerControlGoto=property(doc="Goto.          ")
    kFBPlayerControlRecordModeOn=property(doc="Record mode on.          ")
    kFBPlayerControlRecordModeOff=property(doc="Record mode off.          ")
    pass

class FBPlayMode (Enumeration):
    """
    Play modes.     
         
    """
    kFBPlayModeNoPlay=property(doc="No play (most common).          ")
    kFBPlayModePreviewToEnd=property(doc="Preview clip until end.          ")
    kFBPlayModePlay=property(doc="Play clip.          ")
    kFBPlayModeLoop=property(doc="Loop clip.          ")
    kFBPlayModePlayToEnd=property(doc="Play clip to end.          ")
    pass

class FBPlotAllowed (Enumeration):
    """
    FBPlotAllowed      
        
    """
    kFBPlotAllowed_None=property(doc="        ")
    kFBPlotAllowed_Skeleton=property(doc="        ")
    kFBPlotAllowed_ControlRig=property(doc="        ")
    kFBPlotAllowed_Both=property(doc="        ")
    pass

class FBPlotPopup (FBVisualComponent):
    """
    Plot Popup (for setting options only).     
    See sample: FBPlotPopup.py.     
    """
    def FBPlotPopup(self):
        """
        Constructor.

        """
        pass

    def GetPlotOptions(self):
        """
        Get plot options.

        return : plot options. 
        """
        pass

    def Popup(self,pWindowName):
        """
        Execute plot popup.

        pWindowName : str
        return : <b>true</b> if <b>OK</b> is clicked by user. 
        """
        pass

    def SetPlotOptions(self,pPlotOptions):
        """
        Set plot options.

        pPlotOptions : Set the plot options that will be used when displaying the plot popup. First use the GetPlotOptions(), change the options and use the SetPlotOptions() to set them before calling the Popup() function. 
        """
        pass

    EnableEvaluateDeformation=property(doc="<b>Read Write Property:</b> Enable Evaluate Deformation option for popup.          ")
    EnablePlotAuxEffectors=property(doc="<b>Read Write Property:</b> Enable Plot Aux Effectors option for popup.          ")
    EnablePlotCharacterExtension=property(doc="<b>Read Write Property:</b> Enable Plot Character Extension option for popup.          ")
    EnablePlotLockedProperties=property(doc="<b>Read Write Property:</b> Enable Plot Locked Properties option for popup.          ")
    EnablePlotTranslationOnRootOnly=property(doc="<b>Read Write Property:</b> Enable Plot Translation On Root Only option for popup.          ")
    EnableSmartPlotControls=property(doc="<b>Read Write Property:</b> Enable Smart Plot option for popup.          ")
    pass

class FBPlotTangentMode (Enumeration):
    """
    The tangent mode for plotted curve.     
         
    """
    kFBPlotTangentModeSmooth=property(doc="        ")
    kFBPlotTangentModeSmoothClamp=property(doc="        ")
    kFBPlotTangentModeSpline=property(doc="        ")
    kFBPlotTangentModeSplineClamp=property(doc="        ")
    kFBPlotTangentModeAuto=property(doc="        ")
    pass

class FBPlugModificationFlag (Enumeration):
    """
        
        
    """
    kFBPlugAllContent=property(doc="None Modified.          ")
    kFBSelfDataModified=property(doc="Object/Property itself has been dirty, in case of property get dirty, its owner object will be set dirty as well.          ")
    kFBContentDataModified=property(doc="Owner object/Namespace has data dirty property/objects.          ")
    kFBAllDataModified=property(doc="        ")
    kFBSelfKeyingModified=property(doc="Object/Property itself has been dirty, in case of property get dirty, its owner object will be set dirty as well.          ")
    kFBContentKeyingModified=property(doc="Owner object/Namespace has data dirty property/objects.          ")
    kFBAllKeyingModified=property(doc="        ")
    kFBSelfStateModified=property(doc="Object/Property naming change.          ")
    kFBContentStateModified=property(doc="Owner object/Namespace has state dirty property/objects.          ")
    kFBAllStateModified=property(doc="        ")
    kFBSelfConnectionSrcObjectModified=property(doc="The src object of this plug has been modified.          ")
    kFBSelfConnectionSrcPropertyModified=property(doc="The src property of this plug has been modified.          ")
    kFBSelfConnectionDstObjectModified=property(doc="The dst object of this plug has been modified.          ")
    kFBSelfConnectionDstPropertyModified=property(doc="The dst property of this plug has been modified.          ")
    kFBSelfConnectionModifiedMask=property(doc="        ")
    kFBContentConnectionModified=property(doc="Owner object/namespace has connection modified property/objects.          ")
    kFBAllConnectionModified=property(doc="        ")
    kFBSelfCustomPropertyModified=property(doc="Object custom property change.          ")
    kFBContentCustomPropertyModified=property(doc="Owner object/Namespace has dirty property/objects.          ")
    kFBAllCustomPropertyModified=property(doc="        ")
    kFBSelfAllModifiedMask=property(doc="        ")
    kFBContentAllModifiedMask=property(doc="        ")
    kFBAllModifiedMask=property(doc="        ")
    pass

class FBPlugStatusFlag (Enumeration):
    """
        
        
    """
    kFBPlugStatusFlagNone=property(doc="Plug has no status set.          ")
    kFBOwnedByUndo=property(doc="Plug is owned by undo framework.          ")
    pass

class FBPopupInputType (Enumeration):
    """
    User input types for a popup.     
    See samples: RePrefixAllMarkers.py, SelectModelsWithNameContainingSubstring.py, FBMessageBoxGetUserValue.py.     
    """
    kFBPopupBool=property(doc="Boolean input.          ")
    kFBPopupChar=property(doc="Character input.          ")
    kFBPopupString=property(doc="String input.          ")
    kFBPopupInt=property(doc="Integer input.          ")
    kFBPopupFloat=property(doc="Float input.          ")
    kFBPopupDouble=property(doc="Double input.          ")
    kFBPopupPassword=property(doc="Password input (String with '*'s).          ")
    pass

class FBPoseTransformType (Enumeration):
    """
    Transform mode of pose.     
         
    """
    kFBPoseTransformInvalid=property(doc="        ")
    kFBPoseTransformLocal=property(doc="        ")
    kFBPoseTransformGlobal=property(doc="        ")
    kFBPoseTransformLocalRef=property(doc="        ")
    kFBPoseTransformTypeCount=property(doc="        ")
    pass

class FBPoseType (Enumeration):
    """
    Types of pose.     
         
    """
    kFBBindPose=property(doc="Bind pose.          ")
    kFBRestPose=property(doc="Rest pose.          ")
    pass

class FBProfilingMode (Enumeration):
    """
    Available Profiling modes.     
         
    """
    kFBProfilingModeDisabled=property(doc="All profiling disabled, this include Viewer profiling. For the other modes, when EvaluationDepth is 0, only base information is profiled, such as FPS and evaluation rate.          ")
    kFBProfilingModeEvaluation=property(doc="Collect profiling for all known evaluation tasks (default mode).          ")
    kFBProfilingModeRendering=property(doc="Collect profiling for all known rendering tasks.          ")
    kFBProfilingModeDevices=property(doc="Collect profiling for device Input/Output and Device Evaluation.          ")
    kFBProfilingModeSDK=property(doc="Collect profiling for SDK.          ")
    kFBProfilingModeAllLow=property(doc="Collect profiling for all known tasks that doesn't increase remarkably with scene size. For large scenes this will not influence performance.          ")
    kFBProfilingModeAllHi=property(doc="Collect profiling for all known tasks . For large scenes there should be an influence on performance.          ")
    pass

class FBProgress (FBVisualComponent):
    """
    Progress bar.b>Property: Base property class.     
    See samples: 3dsMaxBipedTemplate.py, MirrorPoseOverTime.py, FBProgress.py. A property is a holder for function callbacks into the internals of the application.You cannot instantiate FBProperty objects. To reference a property: Use an instance of an FBComponent object. The methods FBComponent::PropertyCreate and FBComponent::PropertyRemove can be used to modify an object's set of properties. When accessing a FBProperty object via its containing object, you can get or set (assuming it is not read-only) its value directly, for example in Python: myObject.Visibility = True. FBPropertyManager exists in all FBComponent objects, and contains an array of all the registered properties. Use FBProperty::Find to find a property by name. When accessing a property reference directly, its value is obtained via its 'Data' member. 
@code
myProp = myObject.PropertyList.Find( 'Visibility' )
if myProp: myProp.Data = True
@endcode

To see how to create a custom property in Python, see CustomProperty.py. See samples: CustomProperty.py, SetAllToDoneInAllTakes.py.     
    """
    def FBProgress(self):
        """
        Constructor.

        """
        pass

    def ProgressBegin(self):
        """
        Start progress, must be called before set Text & Percent property.

        """
        pass

    def ProgressDone(self):
        """
        End progress, must be called to reset progress bar UI to normal status after finishing the task.

        """
        pass

    def UserRequestCancell(self):
        """
        Return true if User is pressing and holding 'ESC' key to request the cancellation.
        Must be called in between ProgressBegin()/ProgressDone().

        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to be displayed for progress bar.          ")
    Percent=property(doc="<b>Read Write Property:</b> Percent completed for the operation. Must be used called in between ProgressBegin()/ProgressDone()          ")
    Text=property(doc="<b>Read Write Property:</b> Text to display on progress bar. Must be used in between ProgressBegin()/ProgressDone()          ")
    pass

class FBPropertyAction (FBProperty):
    """
        
        
    """
    def FBPropertyAction(self):
        """
        Constructor.

        """
        pass

    pass

class FBPropertyAnimatable (FBProperty):
    """
    Animatable property base class.     
         
    """
    def FBPropertyAnimatable(self):
        """
        Constructor.

        """
        pass

    def GetAnimationNode(self):
        """
        Get the animation node for the property.

        return : Animation node for property. None is returned if property is not animated. 
        """
        pass

    def AllowsMuting(self):
        """
        AllowsMuting.

        return : <b>true</b> if property can be muted 
        """
        pass

    def GetBox(self):
        """
        Get the owner box.

        return : Handle to the owning box (i.e. model). 
        """
        pass

    def GetColor(self,pIndex):
        """
        Get the color of a particular FCurve of the property.

        pIndex : Index of the FCurve to get the color. 
        return : The color of the FCurve at the specified index, a default FBColor object if the index is invalid. 
        """
        pass

    def GetDataTypeName(self):
        """
        Get the property datatype name.

        return : Datatype of property as a character string. 
        """
        pass

    def HasSomethingMuted(self):
        """
        HasSomethingMuted.

        return : <b>true</b> if property or any of its members is muted 
        """
        pass

    def IsAnimated(self):
        """
        Is the property animated.
        This is true if the property has an FCurve associated to it.

        return : <b>true</b> if animated, <b>false</b> if not animated. 
        """
        pass

    def IsFocused(self):
        """
        Is the property focused (keyable).

        return : Current focus (keyable) state for the property. 
        """
        pass

    def IsFocusedChild(self,pIndex):
        """
        Get the focus (keyable) state of child component.

        pIndex : Index of the child FCurve component. 
        return : <b>true</b> if the component is in focus, false otherwise 
        """
        pass

    def IsMemberMuted(self,pIndex):
        """
        IsMemberMuted.

        pIndex : Index of the sub-member of the property to check. 
        return : <b>true</b> if property sub-member is muted 
        """
        pass

    def IsMuted(self):
        """
        IsMuted.

        return : <b>true</b> if property is muted 
        """
        pass

    def Key(self):
        """
        Key the property.

        """
        pass

    def KeyAt(self,pTime):
        """
        Key the property at time (t).

        pTime : Time at which to insert the key. 
        """
        pass

    def KeyRemoveAt(self,pTime):
        """
        Remove the key at time (t).

        pTime : Time at which to insert the key. 
        """
        pass

    def ResetColor(self,pIndex):
        """
        Revert the FCurves to their default color.

        pIndex : Index of the FCurve to reset the color, use -1 to reset the color for all FCurves of the property. 
        return : <b>true</b> if the color was reverted to its default value, false otherwise 
        """
        pass

    def SetAnimated(self,pState,pCheckLocked):
        """
        Set the animation state of the property.

        pState : State of animation for property, true to animate, false to remove curves. 
        pCheckLocked : Decides whether to check the locked status. 
        """
        pass

    def SetColor(self,pColor,pIndex):
        """
        Set the color of the FCurves for the property.

        pColor : Color to set for the FCurve(s). 
        pIndex : Index of the FCurve to set the new color, use -1 to set the color for all FCurves. 
        return : <b>true</b> if the color was changed, false otherwise 
        """
        pass

    def SetFocus(self,pState):
        """
        Set the property's focus (keyable) state.

        pState : Focus (keyable) state to set for the property. 
        """
        pass

    def SetFocusChild(self,pIndex,pState):
        """
        Set the focus (keyable) state of child component.

        pIndex : Index of the child FCurve component. 
        pState : Focus (keyable) state to set for the property component. 
        return : <b>true</b> if the operation was successful, false otherwise 
        """
        pass

    def SetMemberMuted(self,pIndex,pMuted):
        """
        SetMemberMuted.

        pIndex : Index of the sub-member of the property to mute or unmute. 
        pMuted : True if the sub-member is to be muted, false if it is to be unmuted. 
        """
        pass

    def SetMuted(self,pMuted):
        """
        SetMuted.

        pMuted : True if the property is to be muted, false if it is to be unmuted. 
        """
        pass

    Data=property(doc="<b>Read Write Property:</b> The property data value. Type of this depends on the subclass of FBPropertyAnimatable (ex: in a FBPropertyAnimatableInt, Data is of type int).         ")
    pass

class FBPropertyBool (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyColor (FBProperty):
    """
    FBPropertyColor class.     
    Similar in use to FBPropertyVector3d 
@code
# Supported list protocol methods:
c = FBPropertyColor()
len(c)
print c[0]
c[0] = 1.0
print c.Data
c.Data=FBColor(1.0,0.5,0.5)
@endcode

Slicing is not supported by this object.     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print c[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: c[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    Data=property(doc="        ")
    pass

class FBPropertyColorAndAlpha (FBProperty):
    """
    FBPropertyColorAndAlpha class.     
    Similar in use to FBPropertyColor 
@code
# Supported list protocol methods:
c = FBPropertyColorAndAlpha()
len(c)
print c[0]
c[0] = 1.0
print c.Data
c.Data=FBColorAndAlpha(1.0,0.5,0.5,1.0)
@endcode

Slicing is not supported by this object.     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print c[1].

        pIndex : Index of the components to get (0 to 1) 
        return : Color component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: c[1] = 0.5.

        pIndex : Index of the components to set (0 to 1) 
        pComponentValue : Value of component to set 
        """
        pass

    Data=property(doc="        ")
    pass

class FBPropertyComponent (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyComponents (Enumeration):
    """
    Property Components Bit Field (XYZ, RGB, RGBA, UV, XYZW, etc.).     
         
    """
    kFBPropertyComponent0=property(doc="First component (e.g.: X, Red, etc.).          ")
    kFBPropertyComponent1=property(doc="Second component (e.g.: Y, Green, etc.).          ")
    kFBPropertyComponent2=property(doc="Third component (e.g.: Z, Blue, etc.).          ")
    kFBPropertyComponent3=property(doc="Fourth component (e.g.: W, Alpha, etc.).          ")
    kFBPropertyComponentAll=property(doc="All components.          ")
    pass

class FBPropertyConnectionEditor (FBVisualComponent):
    """
    Property Connection Editor.     
         
    """
    def FBPropertyConnectionEditor(self):
        """
        Constructor.

        """
        pass

    def PopupList(self):
        """
        Launch a list of connected objects.

        """
        pass

    def PopupTree(self):
        """
        Launch a tree of object connections.

        """
        pass

    Property=property(doc="<b>Read Write Property:</b> Property to edit connections. Set to NULL to disable.          ")
    pass

class FBPropertyDouble (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyEnum (FBProperty):
    """
    Enumeration property.     
    Certain properties have strings associated with the integer values they may possess. FBModel's ShadingMode property is one of those example. The actual underlying value of the property is numerical, but it is represented by a string value in the GUI. User can create this type of property via the GUI by creating a list property. The names added to the list can be obtained via the 'EnumList()' method.     
    """
    Data=property(doc="Return the string associated with the index. Will return None when no value is associated.         ")
    pass

class FBPropertyFlag (Enumeration):
    """
    Available flags for FBProperty objects.b>PropertyList: Actor.     
     Property flags are not saved into FBX files. See sample: PropertyDrop.py. <b>These classes are under development and may change dramatically between versions.</b>      
    """
    kFBPropertyFlagNotSet=property(doc="        ")
    kFBPropertyFlagHideProperty=property(doc="This flag is used to show/hide the property in the propertiview. However, when turn on/off HidePropertry flag, this property won't show/hide unless you reload the UI. The nodes hidden by this flag are removed from UI.          ")
    kFBPropertyFlagForceStaticProperty=property(doc="        ")
    kFBPropertyFlagDisableProperty=property(doc="        ")
    kFBPropertyFlagDrivenProperty=property(doc="This is property is connected and driven by other same type of main property, and it always ask value from its main property.          ")
    kFBPropertyFlagAnimated=property(doc="        ")
    kFBPropertyFlagNotSavable=property(doc="Should not be saved to or loaded from an FBX file.          ")
    kFBPropertyFlagReadOnly=property(doc="        ")
    kFBPropertyFlagNotUserDeletable=property(doc="        ")
    kFBValueAllocated=property(doc="The value has been allocated and must be delete in destructor.          ")
    kFBDynamicHidden=property(doc="This flag is used to show/hide the property in the propertiview. When turn on/ff DynamicHidden flag, this property will show/hide. The nodes hidden by this flag still exist in UI.          ")
    kFBDrivenSetByMain=property(doc="Driven property can be modified, valid only when the main property is modified.          ")
    kFBSlaveSetByMaster=property(doc="K_DEPRECATED_2021, use kFBDrivenSetByMain.          ")
    kFBLoadedUserProperty=property(doc="This property is loaded from file.          ")
    pass

class FBPropertyFloat (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyInt (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyListActor (FBPropertyList):
    """
    b>PropertyList: Actor face.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListActor(self):
        """
        """
        pass

    pass

class FBPropertyListActorFace (FBPropertyList):
    """
        
        
    """
    def FBPropertyListActorFace(self):
        """
        """
        pass

    pass

class FBPropertyListAnimationNode (FBPropertyList):
    """
    List of animation nodes.b>List: AudioClip      
         
    """
    def FindByLabel(self,pNodeLabel):
        """
        Returns the animation node from its label.

        pNodeLabel : Label of the searched animation node. 
        return : AnimationNode found. 
        """
        pass

    pass

class FBPropertyListAudioClip (FBPropertyList):
    """
    b>List: AudioIn      
        
    """
    def FBPropertyListAudioClip(self):
        """
        """
        pass

    pass

class FBPropertyListAudioIn (FBPropertyList):
    """
    b>List: AudioOut      
        
    """
    def FBPropertyListAudioIn(self):
        """
        """
        pass

    pass

class FBPropertyListAudioOut (FBPropertyList):
    """
    b>List: Box informations for constraint relation.     
         
    """
    def FBPropertyListAudioOut(self):
        """
        """
        pass

    pass

class FBPropertyListBox (FBPropertyList):
    """
    b>PropertyList: Camera      
        
    """
    pass

class FBPropertyListCamera (FBPropertyList):
    """
    b>PropertyList: Character.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListCamera(self):
        """
        """
        pass

    pass

class FBPropertyListCharacter (FBPropertyList):
    """
        
        
    """
    def FBPropertyListCharacter(self):
        """
        """
        pass

    pass

class FBPropertyListCharacterFace (FBPropertyList):
    """
    b>PropertyList: CharacterMarkerSet.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListCharacterFace(self):
        """
        """
        pass

    pass

class FBPropertyListComponent (FBPropertyList):
    """
    b>PropertyList: Contraint      
    
@code
# Supported list protocol methods:    
 len(propertyListComponent)
 component= propertyListComponent[0]
 propertyListComponent[0] = my_component

 if my_component in propertyListComponent:
    print 'it is contained!'

 del propertyListComponent[0]
@endcode

     
    """
    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        return : number of elements in list. 
        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : FBComponent component value. 
        """
        pass

    def __setitem__(self,pIndex,pComponentValue):
        """
        Sets the ith components Corresponds to python: v[1] = my_component.

        pIndex : Index of the components to set 
        pComponentValue : a FBComponent to set 
        """
        pass

    def __contains__(self,pComponent):
        """
        Check if a FCComponent is already in PropertyList Corresponds to python: if object in propertyList:

        pComponent : Component to check for inclusion 
        return : Is the Component contain or not? 
        """
        pass

    def append(self,pComp):
        """
        Append new FBComponent at end of list.

        pComp : to append 
        """
        pass

    def count(self):
        """
        Returns the number of elements.
        Corresponds to python: del propertyList[2]

        return : number of elements in list. 
        """
        pass

    def insert(self,pIndex,pComp):
        """
        Insert a new element in list.

        pIndex : Index where to insert component 
        pComp : Component to append 
        """
        pass

    def remove(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        """
        pass

    def removeAll(self):
        """
        Remove all elements of list

        """
        pass

    def pop(self):
        """
        Remove last element of list.

        return : Returns the element that was removed. 
        """
        pass

    def pop(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        return : Returns the element that was removed. 
        """
        pass

    pass

class FBPropertyListDeck (FBPropertyList):
    """
        
        
    """
    def FBPropertyListDeck(self):
        """
        """
        pass

    pass

class FBPropertyListDevice (FBPropertyList):
    """
        
        
    """
    def FBPropertyListDevice(self):
        """
        """
        pass

    pass

class FBPropertyListDeviceInstrument (FBPropertyList):
    """
    List of instruments.b>PropertyList: Device optical marker      
         
    """
    pass

class FBPropertyListFCurveKey (FBPropertyList):
    """
    List of FCurveKey.b>List: FileReference      
         
    """
    pass

class FBPropertyListGroup (FBPropertyList):
    """
    b>PropertyList: Handle.     
         
    """
    def FBPropertyListGroup(self):
        """
        """
        pass

    pass

class FBPropertyListHandle (FBPropertyList):
    """
    b>PropertyList: KeyingGroup.     
         
    """
    def FBPropertyListHandle(self):
        """
        """
        pass

    pass

class FBPropertyListLight (FBPropertyList):
    """
    b>PropertyList: Manipulator.     
         
    """
    def FBPropertyListLight(self):
        """
        """
        pass

    pass

class FBPropertyListMarkerSet (FBPropertyList):
    """
    b>PropertyList: Material      
        
    """
    def FBPropertyListMarkerSet(self):
        """
        """
        pass

    pass

class FBPropertyListMaterial (FBPropertyList):
    """
    b>List: Model      
        
    """
    def FBPropertyListMaterial(self):
        """
        """
        pass

    pass

class FBPropertyListModel (FBPropertyList):
    """
    b>PropertyList: Device optical marker      
        
    """
    pass

class FBPropertyListModelTemplate (FBPropertyList):
    """
    b>PropertyList: ModelTemplateBinding.     
         
    """
    pass

class FBPropertyListModelTemplateBinding (FBPropertyList):
    """
    b>List: MotionClip  <b>PropertyList:</b> MotionClip      
        
    """
    pass

class FBPropertyListNote (FBPropertyList):
    """
    b>List of scene objects.     
     This list is a more generic container often used as object properties. The types of actual object that it can contain can be specialized.      
    """
    def FBPropertyListNote(self):
        """
        """
        pass

    pass

class FBPropertyListObject (FBProperty):
    """
    List-like structure fo system elements.     
    b>PropertyList: ObjectPose.This container supports most of the list interface, but is limited to contain only FBComponent objects. New objects can be added, or objects in the list can be removed. The cardinality of the list and the use of the contained object will vary according the container object type. This class supports slice access for query, but not for assignment.     
    """
    def FBPropertyListObject(self):
        """
        Constructor.

        """
        pass

    def SetSingleConnect(self,pSingleConnect):
        """
        Set if the connection is single or multiple.

        pSingleConnect : set to true for only one connection allowed. 
        """
        pass

    def GetSingleConnect(self):
        """
        Get if the connection support only one connection.

        return : true is the connection support only one connection. 
        """
        pass

    pass

class FBPropertyListPivot (FBPropertyList):
    """
    b>List: Model      
        
    """
    pass

class FBPropertyListPose (FBPropertyList):
    """
    b>PropertyList: Texture      
        
    """
    def FBPropertyListPose(self):
        """
        """
        pass

    pass

class FBPropertyListSet (FBPropertyList):
    """
    b>PropertyList: Shader      
        
    """
    def FBPropertyListSet(self):
        """
        """
        pass

    pass

class FBPropertyListShader (FBPropertyList):
    """
    b>List: StoryClip      
        
    """
    def FBPropertyListShader(self):
        """
        """
        pass

    pass

class FBPropertyListStoryClip (FBPropertyList):
    """
    b>List: Story track Details      
        
    """
    pass

class FBPropertyListStoryDetails (FBPropertyList):
    """
    b>List: StoryFolder      
        
    """
    pass

class FBPropertyListStoryFolder (FBPropertyList):
    """
    b>List: StorySubTrack      
        
    """
    pass

class FBPropertyListStorySubTrack (FBPropertyList):
    """
    b>List: StoryTrack      
        
    """
    pass

class FBPropertyListStoryTrack (FBPropertyList):
    """
    b>List: Take      
        
    """
    pass

class FBPropertyListTake (FBPropertyList):
    """
    b>PropertyList: Texture      
        
    """
    def FBPropertyListTake(self):
        """
        """
        pass

    pass

class FBPropertyListTexture (FBPropertyList):
    """
        
        
    """
    def FBPropertyListTexture(self):
        """
        """
        pass

    pass

class FBPropertyListUserObject (FBPropertyList):
    """
    b>PropertyList: VideoClip      
        
    """
    def FBPropertyListUserObject(self):
        """
        """
        pass

    pass

class FBPropertyListVideoIn (FBPropertyList):
    """
    b>PropertyList: VideoOut      
        
    """
    def FBPropertyListVideoIn(self):
        """
        """
        pass

    pass

class FBPropertyListVideoOut (FBPropertyList):
    """
        
        
    """
    def FBPropertyListVideoOut(self):
        """
        """
        pass

    pass

class FBPropertyStateEvent (FBEvent):
    """
    This class is used when the state of a property tracked by the FBFCurveEventManager is changed.     
         
    """
    def FBPropertyStateEvent(self,pEvent):
        """
        Constructor.

        pEvent : Base event (internal) to obtain information from. 
        """
        pass

    EventType=property(doc="<b>Read Only Property:</b> Event type, please see the FBPropertyStateEventType for the possible types.          ")
    pass

class FBPropertyStateEventType (Enumeration):
    """
    This enum indicates what modification was made to the animation of a tracked property.b>Property class: const char * (String).     
         
    """
    kFBPropertyStateEventTypeUnknownOperation=property(doc="Invalid event.          ")
    kFBPropertyStateEventTypeAttached=property(doc="Property connector was added (can happen when undoing a delete operation, which set back the property active in the scene)          ")
    kFBPropertyStateEventTypeDetached=property(doc="Property connector was detached (property animation was delete from the scene, but it still keep in case an undo operation is done)          ")
    kFBPropertyStateEventTypeDestroyed=property(doc="Property connector was destroyed (property animation was deleted)          ")
    kFBPropertyStateEventTypeMassOperation=property(doc="Property was heavily modified (switching to story tool, story clip deleted...)          ")
    pass

class FBPropertyString (FBProperty):
    """
    b>Property: StringList      
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyStringList (FBPropertyList):
    """
        
    
@code
# Supported list protocol methods:    
 len(propertyStringList)
 component= propertyStringList[0]
 propertyStringList[0] = my_string

 if my_string in propertyStringList:
    print 'it is contained!'

 del propertyStringList[0]
@endcode

     
    """
    def FBPropertyStringList(self):
        """
        Constructor.

        """
        pass

    def __len__(self):
        """
        Returns the number of elements.
        Corresponds to python: len(object)

        return : number of elements in list. 
        """
        pass

    def __getitem__(self,pIndex):
        """
        Returns the ith component Corresponds to python: print v[1].

        pIndex : Index of the components to get (0 to 2) 
        return : str component value. 
        """
        pass

    def __setitem__(self,pIndex,pValue):
        """
        Sets the ith components Corresponds to python: v[1] = my_component.

        pIndex : Index of the components to set 
        pValue : a str to set 
        """
        pass

    def __contains__(self,pValue):
        """
        Check if a FCComponent is already in PropertyList Corresponds to python: if object in propertyList:

        pValue : Component to check for inclusion 
        return : Is the String contained or not? 
        """
        pass

    def append(self,pValue):
        """
        Append new str at end of list.

        pValue : to append  
        """
        pass

    def count(self):
        """
        Returns the number of elements.
        Corresponds to python: del propertyList[2]

        return : number of elements in list. 
        """
        pass

    def insert(self,pIndex,pValue):
        """
        Insert a new element in list.

        pIndex : Index where to insert string 
        pValue : String to append 
        """
        pass

    def remove(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        """
        pass

    def removeAll(self):
        """
        Remove all elements of list

        """
        pass

    def pop(self):
        """
        Remove last element of list.

        return : Returns the element that was removed. 
        """
        pass

    def pop(self,pIndex):
        """
        Remove an element in list.

        pIndex : Index where to remove element. 
        return : Returns the element that was removed. 
        """
        pass

    def findFromReference(self,pReference):
        """
        Find the index of an element from its attached reference.

        pReference : Reference of searched object. 
        return : Returns the index of the element corresponding to reference. 
        """
        pass

    def setReferenceAt(self,pReference):
        """
        Sets the reference value of an object.

        pReference : Reference of the object. 
        """
        pass

    def getReferenceAt(self,pIndex):
        """
        Retrieve the reference of an object at ith position.

        pIndex : Index of the object to find reference. 
        return : Returns the reference of the object. 
        """
        pass

    pass

class FBPropertyTime (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyType (Enumeration):
    """
    Property types.     
    See sample: CustomProperty.py.     
    """
    kFBPT_unknown=property(doc="unknow.          ")
    kFBPT_int=property(doc="int.          ")
    kFBPT_bool=property(doc="bool.          ")
    kFBPT_float=property(doc="float.          ")
    kFBPT_double=property(doc="double.          ")
    kFBPT_charptr=property(doc="charptr.          ")
    kFBPT_enum=property(doc="enum.          ")
    kFBPT_Time=property(doc="time.          ")
    kFBPT_TimeCode=property(doc="timecode.          ")
    kFBPT_object=property(doc="object.          ")
    kFBPT_event=property(doc="event.          ")
    kFBPT_stringlist=property(doc="stringlist.          ")
    kFBPT_Vector4D=property(doc="vector4d.          ")
    kFBPT_Vector3D=property(doc="vector3d.          ")
    kFBPT_ColorRGB=property(doc="colorrgb.          ")
    kFBPT_ColorRGBA=property(doc="colorrgba.          ")
    kFBPT_Action=property(doc="action.          ")
    kFBPT_Reference=property(doc="reference.          ")
    kFBPT_TimeSpan=property(doc="timespan.          ")
    kFBPT_kReference=property(doc="kReference.          ")
    kFBPT_Vector2D=property(doc="vector2d.          ")
    pass

class FBPropertyVector2d (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyVector3d (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyVector4d (FBProperty):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyViewType (Enumeration):
    """
    Property view set type.     
         
    """
    kFBViewGlobal=property(doc="Global property view.          ")
    kFBViewByObjectType=property(doc="Class type property view.          ")
    kFBViewByObject=property(doc="Object property view.          ")
    pass

class FBRecalcMarkerSetOffset (Enumeration):
    """
    Recalculate MarkerSet offset for?      
        
    """
    kFBRecalcMarkerSetOffsetTR=property(doc="Recalculate MarkerSet offset for TR.          ")
    kFBRecalcMarkerSetOffsetROnly=property(doc="Recalculate MarkerSet offset for R Only.          ")
    pass

class FBRenderingPass (Enumeration):
    """
    Rendering Pass.     
     Use with FBShader::RenderingPass properties to make the shader be called at any pass. Passes will be called in the order of the enum.      
    """
    kFBPassInvalid=property(doc="No pass selected.          ")
    kFBPassPreRender=property(doc="Before anything.          ")
    kFBPassFlat=property(doc="Lighting off.          ")
    kFBPassLighted=property(doc="Lighting on.          ")
    kFBPassMatte=property(doc="Alpha > 0.5 will show up.          ")
    kFBPassZTranslucent=property(doc="Writes to depth buffer.          ")
    kFBPassZTranslucentAlphaTest=property(doc="Writes to depth buffer where Alpha > 0.5.          ")
    kFBPassTranslucent=property(doc="Models are blended.          ")
    kFBPassAddColor=property(doc="Models are blended additively.          ")
    kFBPassTranslucentZSort=property(doc="Models are sorted and blended.          ")
    kFBPassPostRender=property(doc="After everything.          ")
    pass

class FBRigidBodyMode (Enumeration):
    """
    Rigid body modes.     
         
    """
    kFBRigidBodyFast=property(doc="Fast rigid body mode.          ")
    kFBRigidBodyBest=property(doc="Best rigid body mode.          ")
    pass

class FBRootHMode (Enumeration):
    """
        
        
    """
    kFBRootHAbsoluteDifference=property(doc="        ")
    kFBRootHRelativeDifference=property(doc="        ")
    pass

class FBRootRMode (Enumeration):
    """
        
        
    """
    kFBRootRAbsoluteDifference=property(doc="        ")
    kFBRootRRelativeDifference=property(doc="        ")
    pass

class FBRootSpeedMode (Enumeration):
    """
        
        
    """
    kFBRootSpeedAbsoluteDifference=property(doc="        ")
    kFBRootSpeedRelativeDifference=property(doc="        ")
    pass

class FBRootXZMode (Enumeration):
    """
        
        
    """
    kFBRootXZAbsoluteDifference=property(doc="        ")
    kFBRootXZRelativeDifference=property(doc="        ")
    pass

class FBRotationFilter (Enumeration):
    """
    Rotation filters.     
         
    """
    kFBRotationFilterNone=property(doc="        ")
    kFBRotationFilterGimbleKiller=property(doc="        ")
    kFBRotationFilterUnroll=property(doc="        ")
    pass

class FBRotationOrder (Enumeration):
    """
    Specify the Euler rotation order.     
         
    """
    kFBXYZ=property(doc="XYZ          ")
    kFBXZY=property(doc="XZY.          ")
    kFBYXZ=property(doc="YXZ.          ")
    kFBYZX=property(doc="YZX          ")
    kFBZXY=property(doc="ZXY          ")
    kFBZYX=property(doc="ZYX.          ")
    pass

class FBRSType (Enumeration):
    """
    RS type for serial port.     
         
    """
    kFBRS232=property(doc="RS-232 serial protocol.          ")
    kFBRS422=property(doc="RS-422 serial protocol.          ")
    pass

class FBSceneChangeType (Enumeration):
    """
    Types of model selection events.     
    See sample: PropertyDrop.py.     
    """
    kFBSceneChangeNone=property(doc="Unknown event.          ")
    kFBSceneChangeDestroy=property(doc="Object destroyed.          ")
    kFBSceneChangeAttach=property(doc="Object attached.          ")
    kFBSceneChangeDetach=property(doc="Object detached.          ")
    kFBSceneChangeAddChild=property(doc="Child added.          ")
    kFBSceneChangeRemoveChild=property(doc="Child removed.          ")
    kFBSceneChangeSelect=property(doc="Object selection.          ")
    kFBSceneChangeUnselect=property(doc="Object deselection.          ")
    kFBSceneChangeRename=property(doc="Before object rename.          ")
    kFBSceneChangeRenamePrefix=property(doc="Before object rename prefix.          ")
    kFBSceneChangeRenameUnique=property(doc="Before object rename unique.          ")
    kFBSceneChangeRenameUniquePrefix=property(doc="Before object rename unique prefix.          ")
    kFBSceneChangeRenamed=property(doc="After object rename.          ")
    kFBSceneChangeRenamedPrefix=property(doc="After object rename prefix.          ")
    kFBSceneChangeRenamedUnique=property(doc="After object rename unique.          ")
    kFBSceneChangeRenamedUniquePrefix=property(doc="After object rename unique prefix.          ")
    kFBSceneChangeSoftSelect=property(doc="Soft selection.          ")
    kFBSceneChangeSoftUnselect=property(doc="Soft deselection.          ")
    kFBSceneChangeHardSelect=property(doc="Hard selection.          ")
    kFBSceneChangeActivate=property(doc="Activate.          ")
    kFBSceneChangeDeactivate=property(doc="Deactivate.          ")
    kFBSceneChangeLoadBegin=property(doc="Begin loading file.          ")
    kFBSceneChangeLoadEnd=property(doc="End loading file.          ")
    kFBSceneChangeClearBegin=property(doc="Begin clearing file (file new)          ")
    kFBSceneChangeClearEnd=property(doc="End clearing file (file new)          ")
    kFBSceneChangeTransactionBegin=property(doc="Begin transaction.          ")
    kFBSceneChangeTransactionEnd=property(doc="End transaction.          ")
    kFBSceneChangeMergeTransactionBegin=property(doc="Begin merge transaction.          ")
    kFBSceneChangeMergeTransactionEnd=property(doc="End merge transaction.          ")
    kFBSceneChangeReSelect=property(doc="Re-selection.          ")
    kFBSceneChangeChangeName=property(doc="Object change name.          ")
    kFBSceneChangeChangedName=property(doc="Object changed name.          ")
    kFBSceneChangePreParent=property(doc="Before object parenting.          ")
    kFBSceneChangePreUnparent=property(doc="Before object unparenting.          ")
    kFBSceneChangeFocus=property(doc="Object have focus.          ")
    kFBSceneChangeChangedParent=property(doc="Object changed parent.          ")
    kFBSceneChangeReorder=property(doc="Object reorder.          ")
    kFBSceneChangeReordered=property(doc="Object reordered.          ")
    pass

class FBSegmentMode (Enumeration):
    """
    Segment modes.     
         
    """
    kFBSegmentMarker=property(doc="Use marker.          ")
    kFBSegmentRigidBody=property(doc="Use rigid body.          ")
    kFBSegmentAll=property(doc="Use all.          ")
    pass

class FBShadowFrameType (Enumeration):
    """
    Shadow calculation methods.     
         
    """
    kFBShadowFrameTypeShadowReceiver=property(doc="Bases the shadow calculation on the shadow of the receiver.          ")
    kFBShadowFrameTypeShadowCaster=property(doc="Bases the shadow calculation on the shadow of the caster.          ")
    kFBShadowFrameTypeShadowCubeMap=property(doc="Undocumented or unsupported.          ")
    pass

class FBShadowType (Enumeration):
    """
    Shadow types.     
     The different types of shadow mapping.      
    """
    kFBShadowTypeShadowTranslucentPlanar=property(doc="Use this shadow type to create darkened shadow areas only on planar surfaces.          ")
    kFBShadowTypeShadowProjectiveTexture=property(doc="Uses a texture projection to create a shadow.          ")
    kFBShadowTypeLightMapProjectiveTexture=property(doc="Uses a texture projection as a shadow.          ")
    kFBShadowTypeZShadowProjectiveTexture=property(doc="Similar to the Projective Shadow, except that it uses a boolean algorithm to create a self-shadow.          ")
    kFBShadowTypeZLightMapProjectiveTexture=property(doc="Similar to the Projective Light Map except that it uses a boolean algorithm to create a self-shadow.          ")
    kFBShadowTypeShadowOpaquePlanar=property(doc="Similar to the Planar Shadow, except that it treats all objects as opaque.          ")
    pass

class FBSkeletonLook (Enumeration):
    """
    Look of the skeleton.     
         
    """
    kFBSkeletonLookBone=property(doc="Bone.          ")
    kFBSkeletonLookCube=property(doc="Cube.          ")
    kFBSkeletonLookHardCross=property(doc="Thick cross.          ")
    kFBSkeletonLookLightCross=property(doc="Wireframe cross.          ")
    kFBSkeletonLookSphere=property(doc="Sphere.          ")
    kFBSkeletonLookCapsule=property(doc="Capsule.          ")
    kFBSkeletonLookBox=property(doc="Box.          ")
    kFBSkeletonLookCircle=property(doc="Circle.          ")
    kFBSkeletonLookSquare=property(doc="Square.          ")
    kFBSkeletonLookStick=property(doc="Box with a sphere on one end.          ")
    pass

class FBSkeletonNodeId (Enumeration):
    """
    All Skeleton nodes      
        
    """
    kFBSkeletonInvalidIndex=property(doc="        ")
    kFBSkeletonHipsIndex=property(doc="        ")
    kFBSkeletonLeftHipIndex=property(doc="        ")
    kFBSkeletonLeftKneeIndex=property(doc="        ")
    kFBSkeletonLeftAnkleIndex=property(doc="        ")
    kFBSkeletonLeftFootIndex=property(doc="        ")
    kFBSkeletonRightHipIndex=property(doc="        ")
    kFBSkeletonRightKneeIndex=property(doc="        ")
    kFBSkeletonRightAnkleIndex=property(doc="        ")
    kFBSkeletonRightFootIndex=property(doc="        ")
    kFBSkeletonWaistIndex=property(doc="        ")
    kFBSkeletonChestIndex=property(doc="        ")
    kFBSkeletonLeftCollarIndex=property(doc="        ")
    kFBSkeletonLeftShoulderIndex=property(doc="        ")
    kFBSkeletonLeftElbowIndex=property(doc="        ")
    kFBSkeletonLeftWristIndex=property(doc="        ")
    kFBSkeletonRightCollarIndex=property(doc="        ")
    kFBSkeletonRightShoulderIndex=property(doc="        ")
    kFBSkeletonRightElbowIndex=property(doc="        ")
    kFBSkeletonRightWristIndex=property(doc="        ")
    kFBSkeletonNeckIndex=property(doc="        ")
    kFBSkeletonHeadIndex=property(doc="        ")
    kFBSkeletonLeftThumbAIndex=property(doc="        ")
    kFBSkeletonLeftThumbBIndex=property(doc="        ")
    kFBSkeletonLeftThumbCIndex=property(doc="        ")
    kFBSkeletonLeftIndexAIndex=property(doc="        ")
    kFBSkeletonLeftIndexBIndex=property(doc="        ")
    kFBSkeletonLeftIndexCIndex=property(doc="        ")
    kFBSkeletonLeftMiddleAIndex=property(doc="        ")
    kFBSkeletonLeftMiddleBIndex=property(doc="        ")
    kFBSkeletonLeftMiddleCIndex=property(doc="        ")
    kFBSkeletonLeftRingAIndex=property(doc="        ")
    kFBSkeletonLeftRingBIndex=property(doc="        ")
    kFBSkeletonLeftRingCIndex=property(doc="        ")
    kFBSkeletonLeftPinkyAIndex=property(doc="        ")
    kFBSkeletonLeftPinkyBIndex=property(doc="        ")
    kFBSkeletonLeftPinkyCIndex=property(doc="        ")
    kFBSkeletonRightThumbAIndex=property(doc="        ")
    kFBSkeletonRightThumbBIndex=property(doc="        ")
    kFBSkeletonRightThumbCIndex=property(doc="        ")
    kFBSkeletonRightIndexAIndex=property(doc="        ")
    kFBSkeletonRightIndexBIndex=property(doc="        ")
    kFBSkeletonRightIndexCIndex=property(doc="        ")
    kFBSkeletonRightMiddleAIndex=property(doc="        ")
    kFBSkeletonRightMiddleBIndex=property(doc="        ")
    kFBSkeletonRightMiddleCIndex=property(doc="        ")
    kFBSkeletonRightRingAIndex=property(doc="        ")
    kFBSkeletonRightRingBIndex=property(doc="        ")
    kFBSkeletonRightRingCIndex=property(doc="        ")
    kFBSkeletonRightPinkyAIndex=property(doc="        ")
    kFBSkeletonRightPinkyBIndex=property(doc="        ")
    kFBSkeletonRightPinkyCIndex=property(doc="        ")
    kFBSkeletonReferenceIndex=property(doc="        ")
    kFBSkeletonLastIndex=property(doc="        ")
    pass

class FBSkeletonResolutionLevel (Enumeration):
    """
    Resolution of skeleton sphere, capsule and stick (Quality).     
         
    """
    kFBSkeletonLowResolution=property(doc="Lowest resolution.          ")
    kFBSkeletonMediumResolution=property(doc="Medium resolution.          ")
    kFBSkeletonHighResolution=property(doc="Highest resolution.          ")
    pass

class FBSlider (FBVisualComponent):
    """
    Slider.     
    See samples: BlendShape_Editor.py, Slider.py.     
    """
    def FBSlider(self):
        """
        Constructor.

        """
        pass

    Max=property(doc="<b>Read Write Property:</b> Maximum value.          ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.          ")
    OnChange=property(doc="<b>Event:</b> Slider value changed.          ")
    OnTransaction=property(doc="<b>Event:</b> Transaction begin/end (continuous value changes). This event property doesn't exist in pyfbsdk.          ")
    Orientation=property(doc="<b>Read Write Property:</b> Slider orientation.          ")
    Value=property(doc="<b>Read Write Property:</b> Current value.          ")
    pass

class FBSpread (FBVisualComponent):
    """
    Base spreadsheet class.     
    See samples: ActionScriptMgr.py, KeyboardMapper.py, Spread.py.     
    """
    def FBSpread(self):
        """
        Constructor.

        """
        pass

    def GetCellValue(self,pRow,pColumn):
        """
        Get a cell's value.

        pRow : Row of cell. 
        pColumn : Column of cell. 
        """
        pass

    def SetCellValue(self,pRow,pColumn,pValue):
        """
        Set a cell's value.
        This will also set the FBSpreadCell.Style to the type of pValue (kFBCellStyleInteger if pValue is an int, kFBCellStyleDouble if pValue is a float, kFBCellStyleString if pValue is a str).

        pRow : Row of cell. 
        pColumn : Column of cell. 
        pValue : Value of the cell (can be str, int or float) 
        """
        pass

    def GetSpreadCell(self,pRef,pColumn):
        """
        Get a cell from row and column numbers.

        pRef : Row reference. 
        pColumn : Column number. 
        return : A copy of the cell. 
        """
        pass

    def Clear(self):
        """
        Clear spreadsheet This function will empty spreadsheet of all its rows, columns and cells.

        """
        pass

    def ColumnAdd(self,pString,pRef):
        """
        Add a column.

        pString : Text to display with column. 
        pRef : User-define column reference number(default=0). 
        """
        pass

    def GetCellView(self,pRef,pColumn,pView):
        """
        Get a cell's internal toolkit view.

        pRef : Row of cell. 
        pColumn : Column of cell. 
        pView : Handle of view. 
        """
        pass

    def GetColumn(self,pColumn):
        """
        Get a column from a column number.

        pColumn : Column number. 
        return : A copy of column. 
        """
        pass

    def GetCurrentCell(self):
        """
        Get the current cell.

        return : A copy of the the current cell. 
        """
        pass

    def GetRow(self,pRef):
        """
        Get a row from a row reference.

        pRef : Reference to a row. 
        return : A copy of the row. 
        """
        pass

    def RowAdd(self,pString,pRef):
        """
        Add a row.

        pString : Text to display with row. 
        pRef : User-defined reference for row(default=0). 
        """
        pass

    def RowSort(self,pAscending):
        """
        Sort rows.

        pAscending : If <b>true</b>, sort ascending. 
        """
        pass

    def SetCellView(self,pRef,pColumn,pView):
        """
        Set a cell's internal toolkit view.

        pRef : Row of cell. 
        pColumn : Column of cell. 
        pView : View to use to set cell's view. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display for spreadsheet.          ")
    Column=property(doc="<b>Read Write Property:</b> Current column.          ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Can there be multiple selections?          ")
    OnCellChange=property(doc="<b>Event:</b> Cell value changed.          ")
    OnColumnClick=property(doc="<b>Event:</b> Column clicked.          ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop event.          ")
    OnRowClick=property(doc="<b>Event:</b> Row clicked.          ")
    Row=property(doc="<b>Read Write Property:</b> Current row.          ")
    pass

class FBStereoDisplayMode (Enumeration):
    """
        
        
    """
    kFBStereoDisplayCenterEye=property(doc="Display in Center Eye Camera, No Stereo effect.          ")
    kFBStereoDisplayLeftEye=property(doc="Display in Left Eye Caerma, No Stereo effect.          ")
    kFBStereoDisplayRightEye=property(doc="Display in Right Eye Caerma, No Stereo effect.          ")
    kFBStereoDisplayActive=property(doc="Display in active mode. User must enable OpenGL quad stereo buffer, and choose approriate stereo mode in video card hardware's config app.          ")
    kFBStereoDisplayHorizontalInterlace=property(doc="Display in Horizontal Interlace stereo mode.          ")
    kFBStereoDisplayCheckerboard=property(doc="Display in Checkboard Interlace stereo mode.          ")
    kFBStereoDisplayAnaglyph=property(doc="Display in Analygh stereo mode.          ")
    kFBStereoDisplayAnaglyphLuminance=property(doc="Display in Luminance Analygh stereo mode.          ")
    kFBStereoDisplayFreeviewParallel=property(doc="Display in parallel free view stereo mode.          ")
    kFBStereoDisplayFreeviewCrossed=property(doc="Display in crossed free view stereo mode.          ")
    kFBStereoDisplayModeCount=property(doc="update this count value when add new mode          ")
    pass

class FBStoryClipAlignmentType (Enumeration):
    """
    Alignment Types when aligning clips.     
         
    """
    kFBStoryClipAlignmentCurrentTimeline=property(doc="Align all selected clips with the current time.          ")
    kFBStoryClipAlignmentEndPrevious=property(doc="Align selected clips to the end of the previous clip.          ")
    kFBStoryClipAlignmentEndPreviousAllAligned=property(doc="Align selected clips to the end of the previous clip, all clips will be align to the selected clip position.          ")
    kFBStoryClipAlignmentBeginningNext=property(doc="Align selected clips to the beginning of the next clip.          ")
    kFBStoryClipAlignmentBeginningNextAllAligned=property(doc="Align selected clips to the beginning of the next clip, all clips will be align to the selected clip position.          ")
    kFBStoryClipAlignmentCurrentTimelineWithOffset=property(doc="Align all selected clips with the current time, while keeping the relative offset.          ")
    kFBStoryClipAlignmentEndPreviousWithOffset=property(doc="Align selected clips to the end of the previous clip, while keeping the relative offset.          ")
    kFBStoryClipAlignmentBeginningNextWithOffset=property(doc="Align selected clips to the beginning of the next clip, while keeping the relative offset.          ")
    pass

class FBStoryClipChangeType (Enumeration):
    """
    Types of clip change events, matching KEventClip.eType Expose only kFBStoryClipMoveClip and kFBStoryClipRemoved for now.     
         
    """
    kFBStoryClipNotSet=property(doc="Clip none.          ")
    kFBStoryClipMoveClip=property(doc="Clip moved.          ")
    kFBStoryClipMoveData=property(doc="Clip data moved.          ")
    kFBStoryClipMoveBlend=property(doc="Clip move blend.          ")
    kFBStoryClipUpdateUI=property(doc="Clip UI update.          ")
    kFBStoryClipRemoved=property(doc="Clip removed.          ")
    pass

class FBStoryClipCompMode (Enumeration):
    """
    Compensation Modes for story character clips.     
         
    """
    kFBStoryClipOff=property(doc="No compensation.          ")
    kFBStoryClipAuto=property(doc="Automatic compensation.          ")
    kFBStoryClipUser=property(doc="User defined compensation.          ")
    pass

class FBStoryClipGhostTimeMode (Enumeration):
    """
    Time mode to display ghost.     
         
    """
    kFBStoryClipGhostCurrent=property(doc="Show the ghost at current time of the clip.          ")
    kFBStoryClipGhostStart=property(doc="Show the ghost at start time of the clip.          ")
    kFBStoryClipGhostStop=property(doc="Show the ghost at stop time of the clip.          ")
    kFBStoryClipGhostCustom=property(doc="Show the ghost at custom time of the clip. See GhostManipulatorCustomTime property.          ")
    pass

class FBStoryClipMatchingRotationType (Enumeration):
    """
    Matching Rotation Types, when matching clips to each other.     
         
    """
    kFBStoryClipMatchingRotationNone=property(doc="The clip's match object is not rotated to match another clip's animation.          ")
    kFBStoryClipMatchingRotationXYZ=property(doc="Rotates a selected clip's match object to the same orientation as the previous clip's match object.          ")
    kFBStoryClipMatchingRotationGravityXZ=property(doc="Rotates a selected clip's match object around the global Y axis.          ")
    kFBStoryClipMatchingRotationDefault=property(doc="Uses the matching translation type stored in the Application configuration file: [Story] > MatchRotation. This value, in the configuration file, is update each time a matching is done, with the selected value.          ")
    pass

class FBStoryClipMatchingTimeType (Enumeration):
    """
    Matching Time Types, when matching clips to each other.     
         
    """
    kFBStoryClipMatchingTimeCurrentTime=property(doc="Matches the start of the selected clip to the previous/next clip at the current time.          ")
    kFBStoryClipMatchingTimeStartOfSelectedClip=property(doc="Matches the start of the selected clip to the start of the blend with the previous clip.          ")
    kFBStoryClipMatchingTimeBetweenPreviousAndSelectedClip=property(doc="Matches the selected clip and the previous clip at the middle of the blend.          ")
    kFBStoryClipMatchingTimeEndOfPreviousClip=property(doc="Matches the end of the blend with the selected clip to the end of the previous clip.          ")
    kFBStoryClipMatchingTimeStartOfNextClip=property(doc="Matches the start of the blend with the selected clip to the start of the next clip.          ")
    kFBStoryClipMatchingTimeBetweenSelectedAndNextClip=property(doc="Matches the selected clip and the next clip at the middle of the blend.          ")
    kFBStoryClipMatchingTimeEndOfSelectedClip=property(doc="Matches the end of the selected clip to the end of the blend with the previous clip.          ")
    kFBStoryClipMatchingTimeDefault=property(doc="Uses the matching time type stored in the Application configuration file: [Story] > MatchWhen. This value, in the configuration file, is update each time a matching is done, with the selected value.          ")
    pass

class FBStoryClipMatchingTranslationType (Enumeration):
    """
    Matching Translation, Types when matching clips to each other.     
         
    """
    kFBStoryClipMatchingTranslationNone=property(doc="The clip's match object is not translated to match another clip's animation.          ")
    kFBStoryClipMatchingTranslationXYZ=property(doc="Translates a selected clip's match object to the same location as the previous clip's match object.          ")
    kFBStoryClipMatchingTranslationGravityXZ=property(doc="Translates a selected clip's match object along the global X and Z axes.          ")
    kFBStoryClipMatchingTranslationDefault=property(doc="Uses the matching translation type stored in the Application configuration file: [Story] > MatchTranslation. This value, in the configuration file, is update each time a matching is done, with the selected value.          ")
    pass

class FBStoryClipMirrorPlane (Enumeration):
    """
    Several mirror planes to mirror animation.     
         
    """
    kFBStoryClipMirrorPlaneXY=property(doc="X-Y plane.          ")
    kFBStoryClipMirrorPlaneZY=property(doc="Z-Y plane.          ")
    kFBStoryClipMirrorPlaneXZ=property(doc="X-Z plane.          ")
    pass

class FBStoryClipNodeFunction (Enumeration):
    """
    Node function.     
         
    """
    kFBStoryClipNodeAverage=property(doc="Average.          ")
    kFBStoryClipNodeFloorProjection=property(doc="Project on XZ plane.          ")
    kFBStoryClipNodeNone=property(doc="None.          ")
    pass

class FBStoryClipShowGhostMode (Enumeration):
    """
    Show Ghost Modes for story animation clips.     
         
    """
    kFBStoryClipAlways=property(doc="Always show the ghost.          ")
    kFBStoryClipTimeCursor=property(doc="Show the ghost only on time cursor.          ")
    kFBStoryClipTimeCustom=property(doc="Show the ghost for custom time frame.          ")
    pass

class FBStoryClipSolveMode (Enumeration):
    """
    Solve Modes for story character clips.     
         
    """
    kFBStoryClipRetargetSkeleton=property(doc="Solve retarget skeleton.          ")
    kFBStoryClipAnimSkeleton=property(doc="Solve skeleton animation.          ")
    kFBStoryClipAnimFkIk=property(doc="Solve forward and inverse kinematic animation.          ")
    kFBStoryClipAnimSkeletonIk=property(doc="Solve skeleton inverse kinematic animation.          ")
    pass

class FBStoryClipTimeWarpInterpolatorType (Enumeration):
    """
    Types of TimeWrap Interpolator for Story Clips.     
         
    """
    kFBStoryClipTimeWarpInterpolatorCustom=property(doc="'Custom' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorLinear=property(doc="'Normal' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorSmoothedEnds=property(doc="'Smoothed Ends' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorGoingFaster=property(doc="'Going Faster' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorSlowingDown=property(doc="'Slowing Down' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorLinearReversed=property(doc="'Reversed' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorSmoothedEndsReversed=property(doc="'Reversed, Smoothed Ends' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorGoingFasterReversed=property(doc="'Reversed, Going Faster' TimeWarp Interpolation          ")
    kFBStoryClipTimeWarpInterpolatorSlowingDownReversed=property(doc="'Reversed, Slowing Down' TimeWarp Interpolation          ")
    pass

class FBStoryGroupClipAlignmentType (Enumeration):
    """
    Alignment Types when aligning groups.     
         
    """
    kFBStoryGroupClipAlignmentCurrentTimeline=property(doc="Align the clips contained in the group clip with the current time.          ")
    kFBStoryGroupClipAlignmentEndPreviousWithOffset=property(doc="Align the clips contained in the group clip to the end of the previous clip, while keeping the relative offset.          ")
    kFBStoryGroupClipAlignmentBeginningNextWithOffset=property(doc="Align the clips contained in the group clip to the beginning of the next clip, while keeping the relative offset.          ")
    pass

class FBStoryTrackBodyPart (Enumeration):
    """
    Body Parts for story track character.     
         
    """
    kFBStoryTrackBodyPartNone=property(doc="        ")
    kFBStoryTrackBodyPartHead=property(doc="        ")
    kFBStoryTrackBodyPartLeftShoulder=property(doc="        ")
    kFBStoryTrackBodyPartLeftHand=property(doc="        ")
    kFBStoryTrackBodyPartLeftArm=property(doc="        ")
    kFBStoryTrackBodyPartRightShoulder=property(doc="        ")
    kFBStoryTrackBodyPartRightHand=property(doc="        ")
    kFBStoryTrackBodyPartRightArm=property(doc="        ")
    kFBStoryTrackBodyPartLeftFoot=property(doc="        ")
    kFBStoryTrackBodyPartLeftLeg=property(doc="        ")
    kFBStoryTrackBodyPartRightFoot=property(doc="        ")
    kFBStoryTrackBodyPartRightLeg=property(doc="        ")
    kFBStoryTrackBodyPartProps=property(doc="        ")
    kFBStoryTrackBodyPartExtensions=property(doc="        ")
    kFBStoryTrackBodyPartSpine=property(doc="        ")
    kFBStoryTrackBodyPartUpperBody=property(doc="        ")
    kFBStoryTrackBodyPartLowerBody=property(doc="        ")
    kFBStoryTrackBodyPartAll=property(doc="        ")
    pass

class FBStoryTrackGhostShowMode (Enumeration):
    """
    Ghost Show Modes for story animation tracks.     
         
    """
    kFBStoryTrackShowAllClips=property(doc="Show the ghosts for all the clips on the track.          ")
    kFBStoryTrackShowCurrentTimeAdjacentClips=property(doc="Show the ghosts only for the previous clip, current clip, and next clip relative to current time.          ")
    pass

class FBStoryTrackRefMode (Enumeration):
    """
    References Modes for story animation tracks.     
         
    """
    kFBStoryTrackOverride=property(doc="Override track.          ")
    kFBStoryTrackAdditive=property(doc="Additive track.          ")
    pass

class FBStoryTrackType (Enumeration):
    """
    Types for new story tracks.     
    See samples: CreateShotClip.py, AudioTrackSetupTool.py.     
    """
    kFBStoryTrackAnimation=property(doc="Animation track.          ")
    kFBStoryTrackCamera=property(doc="Camera animation track.          ")
    kFBStoryTrackCharacter=property(doc="Character animation track.          ")
    kFBStoryTrackConstraint=property(doc="Constraint track.          ")
    kFBStoryTrackCommand=property(doc="Command track.          ")
    kFBStoryTrackShot=property(doc="Shot track.          ")
    kFBStoryTrackAudio=property(doc="Audio track.          ")
    kFBStoryTrackVideo=property(doc="Video track.          ")
    pass

class FBSurfaceMode (Enumeration):
    """
    Surface modes.     
         
    """
    kFBSurfaceModeRaw=property(doc="Raw data.          ")
    kFBSurfaceModeLowNoNormals=property(doc="Low quality, no normals.          ")
    kFBSurfaceModeLow=property(doc="Low quality.          ")
    kFBSurfaceModeHighNoNormals=property(doc="High quality, no normals.          ")
    kFBSurfaceModeHigh=property(doc="High quality.          ")
    pass

class FBSurfaceType (Enumeration):
    """
    Surface types.     
         
    """
    kFBSurfaceTypeBezier=property(doc="Bezier surface.          ")
    kFBSurfaceTypeBezierQuadric=property(doc="Bezier Quadric surface.          ")
    kFBSurfaceTypeCardinal=property(doc="Cardinal surface.          ")
    kFBSurfaceTypeBspline=property(doc="BSpline surface.          ")
    kFBSurfaceTypeLinear=property(doc="Linear surface.          ")
    pass

class FBSyncActivationAndVisibilityMode (Enumeration):
    """
    Sync mode for Constraints' Activeness and Models' visibility belonging to the Character Extension.     
         
    """
    kFBSyncMode_None=property(doc="        ")
    kFBSyncMode_WithContolRig=property(doc="        ")
    kFBSyncMode_WithOthersThanControlRig=property(doc="        ")
    pass

class FBTabPanel (FBVisualComponent):
    """
    Tab panel.     
    See sample: TabPanel.py.     
    """
    def FBTabPanel(self):
        """
        Constructor.

        """
        pass

    ItemIndex=property(doc="<b>Read Write Property:</b> Current tab panel.          ")
    Items=property(doc="<b>List:</b> Names for tab panels.          ")
    Layout=property(doc="<b>Read Write Property:</b> Layout for current tab panel.          ")
    OnChange=property(doc="<b>Event:</b> Tab panel change.          ")
    TabStyle=property(doc="<b>Read Write Property:</b> Style of the tab panel, 0 creates normal tabs, 1 creates buttons to activate tabs.          ")
    pass

class FBTakeChangeType (Enumeration):
    """
    Types of take change events.     
         
    """
    kFBTakeChangeAdded=property(doc="        ")
    kFBTakeChangeRemoved=property(doc="        ")
    kFBTakeChangeOpened=property(doc="        ")
    kFBTakeChangeClosed=property(doc="        ")
    kFBTakeChangeRenamed=property(doc="        ")
    kFBTakeChangeUpdated=property(doc="        ")
    kFBTakeChangeMoved=property(doc="        ")
    kFBTakeChangeNone=property(doc="        ")
    pass

class FBTakeSpanOnLoad (Enumeration):
    """
    This enumeration indicate the how to set the take start and end points on after a load.     
         
    """
    kFBLeaveAsIs=property(doc="Use the current take's start and end point as defined before the load.          ")
    kFBImportFromFile=property(doc="Set the current take's span according what is set in the loaded file.          ")
    kFBFrameAnimation=property(doc="Have the take's span match the first and last key in the take.          ")
    pass

class FBTangentClampMode (Enumeration):
    """
    Different clamping modes for the tangents.     
         
    """
    kFBTangentClampModeNone=property(doc="The tangent will act normally.          ")
    kFBTangentClampModeClamped=property(doc="The tangent will be flattened when the key is placed at the same value as an adjacent key.          ")
    pass

class FBTangentConstantMode (Enumeration):
    """
    Different constant modes for the tangents.     
         
    """
    kFBTangentConstantModeNormal=property(doc="The tangent will contain the value of the current keyframe until the next keyframe.          ")
    kFBTangentConstantModeNext=property(doc="The tangent will contain the value of the next keyframe.          ")
    pass

class FBTangentCustomIndex (Enumeration):
    """
    Custom tangent index for the tangents.     
         
    """
    kFBTangentCustomIndex0=property(doc="First custom tangent type registered in the system.          ")
    kFBTangentCustomIndex1=property(doc="Second custom tangent type registered in the system.          ")
    kFBTangentCustomIndex2=property(doc="Third custom tangent type registered in the system.          ")
    pass

class FBTangentMode (Enumeration):
    """
    Methods of tangent calculation.     
     This is only relevant when interpolation is CUBIC.      
    """
    kFBTangentModeAuto=property(doc="This is the equivalent to a cardinal spline with no parametrization. In the UI, it is identified as Smooth.          ")
    kFBTangentModeTCB=property(doc="TCB spline (3 parameters: TENSION, CONTINUITY, BIAS)          ")
    kFBTangentModeUser=property(doc="Used to represent all splines with no lost data (HERMITE, BEZIER, CATMUL, etc.)          ")
    kFBTangentModeBreak=property(doc="Like USER but left slope may differ from right.          ")
    kFBTangentModeTimeIndependent=property(doc="Time independent, is calculated based upon the slope between the previous and next key values. In the UI, it is identified as Spline.          ")
    kFBTangentModeClampProgressive=property(doc="Time independent, will flatten the tangent handles when the key value goes over or under the previous and next key values. In the UI, it is identified as Auto.          ")
    pass

class FBTangentWeightMode (Enumeration):
    """
    Active tangent weight, no/one/both side are active on a key.     
     Please note, the left value is for the next key, as the current key contains the tangent weight information for the next key. To disable the weight on the left side of a key at index 'i', you need to disable 'kFBTangentWeightModeNextLeft' the 'i-1' key.      
    """
    kFBTangentWeightModeNone=property(doc="Tangent weight disabled.          ")
    kFBTangentWeightModeRight=property(doc="Right tangent weight active.          ")
    kFBTangentWeightModeNextLeft=property(doc="Next key left tangent weight active.          ")
    kFBTangentWeightModeBoth=property(doc="Right tangent and next key left tangent weight are active.          ")
    pass

class FBTCPIPSocketType (Enumeration):
    """
    Types of TCP/IP Sockets.     
         
    """
    kFBTCPIP_Stream=property(doc="Streaming data (TCP).          ")
    kFBTCPIP_DGRAM=property(doc="Datagrams (UDP).          ")
    kFBTCPIP_RAW=property(doc="Raw data (TCP).          ")
    pass

class FBTextJustify (Enumeration):
    """
    Text justification styles.     
    See samples: Button.py, Label.py.     
    """
    kFBTextJustifyLeft=property(doc="Left justify.          ")
    kFBTextJustifyRight=property(doc="Right justify.          ")
    kFBTextJustifyCenter=property(doc="Center alignment.          ")
    pass

class FBTextStyle (Enumeration):
    """
    Text appearance styles.     
    See sample: Label.py.     
    """
    kFBTextStyleNone=property(doc="Normal.          ")
    kFBTextStyleBold=property(doc="Bold.          ")
    kFBTextStyleItalic=property(doc="Italic.          ")
    kFBTextStyleUnderlined=property(doc="Underlined.          ")
    pass

class FBTextureBlendMode (Enumeration):
    """
    Texture blend modes.     
     How the texture is blended with another. See samples: LayeredTexture.py, TextureAnimation.py.     
    """
    kFBTextureBlendTranslucent=property(doc="Layer transparency.          ")
    kFBTextureBlendAdditive=property(doc="Layer addition.          ")
    kFBTextureBlendModulate=property(doc="Layer multiplication.          ")
    kFBTextureBlendModulate2=property(doc="Layer multiplication + brightness.          ")
    pass

class FBTextureMapping (Enumeration):
    """
    Texture mapping modes.     
     How the texture is mapped.      
    """
    kFBTextureNoMapping=property(doc="No mapping.          ")
    kFBTextureMappingUV=property(doc="UV mapping.          ")
    kFBTextureMappingXY=property(doc="XY mapping.          ")
    kFBTextureMappingYZ=property(doc="YZ mapping.          ")
    kFBTextureMappingXZ=property(doc="XZ mapping.          ")
    kFBTextureMappingSpherical=property(doc="Spherical mapping.          ")
    kFBTextureMappingCylindrical=property(doc="Cylindrical mapping.          ")
    kFBTextureMappingEnvironment=property(doc="Environment mapping.          ")
    kFBTextureMappingProjection=property(doc="Projection mapping.          ")
    pass

class FBTextureUseType (Enumeration):
    """
    Texture Use Type.     
     How the texture is used.      
    """
    kFBTextureUseAll=property(doc="All textures.          ")
    kFBTextureUseColor=property(doc="standard color type, work with material.          ")
    kFBTextureUseShadowMap=property(doc="Shadow Map, work with model.          ")
    kFBTextureUseLightMap=property(doc="Light Map, work with model.          ")
    kFBTextureUseSphericalReflexionMap=property(doc="Spherical Reflexion Map, work with model.          ")
    kFBTextureUseSphereReflexionMap=property(doc="Sphere Reflexion Map, work with model.          ")
    kFBTextureUseBumpNormalMap=property(doc="Bump Normal Map, work with model.          ")
    pass

class FBThermometer (FBVisualComponent):
    """
    Thermometer.     
    See sample: Thermometer.py.     
    """
    def FBThermometer(self):
        """
        Constructor.

        """
        pass

    def Clear(self):
        """
        Reset bounds and value.

        """
        pass

    Max=property(doc="<b>Read Write Property:</b> Maximum value.          ")
    Min=property(doc="<b>Read Write Property:</b> Minimum value.          ")
    Value=property(doc="<b>Read Write Property:</b> Current value.          ")
    pass

class FBTimeMarkAction (Enumeration):
    """
    Time (Global & Take) Mark assigned action.     
         
    """
    kFBTimeMarkAction_None=property(doc="No action. The mark is just visual hint.          ")
    kFBTimeMarkAction_Stop=property(doc="When reaching the mark, the playback stops.          ")
    kFBTimeMarkAction_Loop=property(doc="When reaching the mark, the playback loops to previous global mark (or start frame if any).          ")
    pass

class FBTimeMode (Enumeration):
    """
    Different time modes available.     
         
    """
    kFBTimeModeDefault=property(doc="Default Time Mode.          ")
    kFBTimeMode1000Frames=property(doc="1000 : 1 millisecond          ")
    kFBTimeMode120Frames=property(doc="120          ")
    kFBTimeMode11988Frames=property(doc="~119.88          ")
    kFBTimeMode100Frames=property(doc="100          ")
    kFBTimeMode96Frames=property(doc="96          ")
    kFBTimeMode72Frames=property(doc="72          ")
    kFBTimeMode60Frames=property(doc="60          ")
    kFBTimeMode5994Frames=property(doc="~59.94          ")
    kFBTimeMode50Frames=property(doc="50          ")
    kFBTimeMode48Frames=property(doc="48          ")
    kFBTimeMode30Frames=property(doc="30          ")
    kFBTimeMode2997Frames_Drop=property(doc="~29.97 drop          ")
    kFBTimeMode2997Frames=property(doc="~29.97 full          ")
    kFBTimeMode25Frames=property(doc="25          ")
    kFBTimeMode24Frames=property(doc="24          ")
    kFBTimeMode23976Frames=property(doc="~23.976          ")
    kFBTimeModeCustom=property(doc="Custom framerate.          ")
    pass

class FBTimeReferential (Enumeration):
    """
    FBCommandState.     
         
    """
    kFBTimeReferentialAction=property(doc="Action.          ")
    kFBTimeReferentialShot=property(doc="Shot.          ")
    kFBTimeReferentialEdit=property(doc="Edit.          ")
    pass

class FBToolPossibleDockPosition (Enumeration):
    """
        
        
    """
    kFBToolPossibleDockPosNone=property(doc="        ")
    kFBToolPossibleDockPosTop=property(doc="        ")
    kFBToolPossibleDockPosLeft=property(doc="        ")
    kFBToolPossibleDockPosRight=property(doc="        ")
    kFBToolPossibleDockPosBottom=property(doc="        ")
    pass

class FBTransportLoopMode (Enumeration):
    """
    Available loop modes for the transport control.     
         
    """
    kFBTransportNoLoop=property(doc="Playback not looping.          ")
    kFBTransportLoopCurrentTake=property(doc="Playback looping the current take.          ")
    kFBTransportLoopThroughAllTakes=property(doc="Playback from the current take through all takes in order then stops.          ")
    pass

class FBTransportMode (Enumeration):
    """
    Transport modes.     
         
    """
    kFBTransportPlay=property(doc="        ")
    kFBTransportPlayPrepare=property(doc="!< Play mode          ")
    kFBTransportPlayReady=property(doc="        ")
    kFBTransportStop=property(doc="        ")
    kFBTransportStopPost=property(doc="!< Stop mode          ")
    kFBTransportStopReady=property(doc="        ")
    kFBTransportShuttle=property(doc="        ")
    kFBTransportShuttlePrepare=property(doc="!< Shuttle mode          ")
    kFBTransportShuttleReady=property(doc="        ")
    kFBTransportPlayReverse=property(doc="        ")
    kFBTransportPlayReversePrepare=property(doc="!< Play reverse.          ")
    kFBTransportPlayReverseReady=property(doc="        ")
    kFBTransportJog=property(doc="        ")
    kFBTransportJogPrepare=property(doc="!< Jog.          ")
    kFBTransportJogReady=property(doc="        ")
    kFBTransportGoto=property(doc="        ")
    kFBTransportGotoPrepare=property(doc="!< Goto.          ")
    kFBTransportGotoReady=property(doc="        ")
    kFBTransportStepForward=property(doc="        ")
    kFBTransportStepForwardPrepare=property(doc="!< Step forward          ")
    kFBTransportStepForwardReady=property(doc="        ")
    kFBTransportStepBackward=property(doc="        ")
    kFBTransportStepBackwardPrepare=property(doc="!< Step backward.          ")
    kFBTransportStepBackwardReady=property(doc="        ")
    pass

class FBTransportPlaySpeed (Enumeration):
    """
    Available transport control play speed.     
         
    """
    kFBSpeed_1_10x=property(doc="0.10x          ")
    kFBSpeed_1_5x=property(doc="0.20x          ")
    kFBSpeed_1_4x=property(doc="0.25x          ")
    kFBSpeed_1_3x=property(doc="0.33x          ")
    kFBSpeed_1_2x=property(doc="0.50x          ")
    kFBSpeed_1x=property(doc="1x          ")
    kFBSpeed_ALL_FR=property(doc="All frames.          ")
    kFBSpeed_2x=property(doc="2x          ")
    kFBSpeed_3x=property(doc="3x          ")
    kFBSpeed_4x=property(doc="4x          ")
    kFBSpeed_5x=property(doc="5x          ")
    kFBSpeed_10x=property(doc="10x          ")
    kFBSpeed_Custom=property(doc="Custom speed.          ")
    pass

class FBTransportSnapMode (Enumeration):
    """
    Available snap methods for the transport control.     
         
    """
    kFBTransportSnapModeNoSnap=property(doc="No snapping is applied.          ")
    kFBTransportSnapModeSnapOnFrames=property(doc="Snaps to an exact frame when modifying the current time.          ")
    kFBTransportSnapModePlayOnFrames=property(doc="When playing, plays to exact frames.          ")
    kFBTransportSnapModeSnapAndPlayOnFrames=property(doc="Combines both Snap and Play on frames modes.          ")
    pass

class FBTransportTimeFormat (Enumeration):
    """
    Available transport control time display.     
         
    """
    kFBTimeFormatTimecode=property(doc="Timecode time display mode.          ")
    kFBTimeFormatFrame=property(doc="Frame time display mode.          ")
    pass

class FBTree (FBVisualComponent):
    """
    Tree list view.     
    See sample: Tree.py.     
    """
    def FBTree(self):
        """
        Constructor.

        """
        pass

    def Clear(self):
        """
        Clear the tree (remove all nodes).

        """
        pass

    def GetRoot(self):
        """
        Get the root node.

        return : the root node of the tree. 
        """
        pass

    def InsertLast(self,pNode,pName):
        """
        Insert node at the end.

        pNode : Node under which the new node will appear. 
        pName : Text to display for this node. 
        return : the newly created node. 
        """
        pass

    AllowCollapse=property(doc="<b>Read Write Property:</b> When OnCollapsing occurs, set this to true to allow collapse.          ")
    AllowExpansion=property(doc="<b>Read Write Property:</b> When OnExpanding occurs, set this to true to allow expansion.          ")
    AutoExpandOnDblClick=property(doc="<b>Read Write Property:</b> Allow automatic expand on double click, default is false.          ")
    AutoExpandOnDragOver=property(doc="<b>Read Write Property:</b> Allow automatic expand on drag over, default is false.          ")
    AutoScroll=property(doc="<b>Read Write Property:</b> If AutoScroll property is True then the tree window will be automatically scrolled when the user drags item(s) over the boundaries of the tree.          ")
    AutoScrollOnExpand=property(doc="<b>Read Write Property:</b> Allow automatic scroll on expand, default is true.          ")
    CheckBoxes=property(doc="<b>Read Write Property:</b> Draw check boxe for each node.          ")
    DeselectOnCollapse=property(doc="<b>Read Write Property:</b> Tells whether node are deselected if parent node is collapsed.          ")
    EditNodeOn2Select=property(doc="<b>Read Write Property:</b> Set to true, to allow automatic node editing on second select.          ")
    HighlightOnRightClick=property(doc="<b>Read Write Property:</b> Hightlight node on right click.          ")
    Indent=property(doc="<b>Read Write Property:</b> Use Indent to determine how far child nodes are indented from their parent nodes when the parent is expanded.          ")
    ItemHeight=property(doc="<b>Read Write Property:</b> Height of an item.          ")
    MultiDrag=property(doc="<b>Read Write Property:</b> Tells whether multiple drag/drop is allowed or not.          ")
    MultiSelect=property(doc="<b>Read Write Property:</b> Tells whether multiple selection is allowed or not.          ")
    NoSelectOnDrag=property(doc="<b>Read Write Property:</b> Tells whether node are selected if drag is start and node is not already selected.          ")
    NoSelectOnRightClick=property(doc="<b>Read Write Property:</b> Tells whether node are selected if right click on node.          ")
    OnChange=property(doc="<b>Event:</b> Change of the selection.          ")
    OnClick=property(doc="<b>Event:</b> Click on a node of the tree. Use OnSelect.          ")
    OnClickCheck=property(doc="<b>Event:</b> Click on a node checkbox of the tree.          ")
    OnCollapsed=property(doc="<b>Event:</b> Click on the '-' sign before a non-leaf node.          ")
    OnCollapsing=property(doc="<b>Event:</b> Fired before the node collapse. To refuse collapsing, set AllowCollapse to false.          ")
    OnDblClick=property(doc="<b>Event:</b> Double-Click on a node of the tree. Use FBEventTreeSelect to cast event.          ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and drop of an element.          ")
    OnExpanded=property(doc="<b>Event:</b> Click on the '+' sign before a non-leaf node          ")
    OnExpanding=property(doc="<b>Event:</b> Is fired before the node expand. To refuse expanding set AllowExpansion to false.          ")
    OnSelect=property(doc="<b>Event:</b> A node was selected. Use FBEventTreeSelect to cast event.          ")
    SelectedCount=property(doc="<b>Read Only Property:</b> Count of selected items.          ")
    SelectedNodes=property(doc="<b>Read Only Property:</b> List of selected nodes.          ")
    SelectionActive=property(doc="<b>Read Write Property:</b> Tells whether selection is allowed or not.          ")
    ShowLines=property(doc="<b>Read Write Property:</b> On node selection, will draw entire line selected          ")
    TreeHeight=property(doc="<b>Read Only Property:</b> Height of the tree.          ")
    TreeWidth=property(doc="<b>Read Only Property:</b> Width of the tree.          ")
    VisibleItemCount=property(doc="<b>Read Only Property:</b> Count of visible items.          ")
    pass

class FBTriggerStyle (Enumeration):
    """
    Audio clips' trigger styles.     
         
    """
    kFBTriggerStyleContinue=property(doc="Previously triggered clips that are still playing won't be stopped and mixing will occur.          ")
    kFBTriggerStyleCut=property(doc="Previously triggered clips that are still playing will be stopped.          ")
    kFBTriggerStyleToggle=property(doc="If a previously triggered clip is playing, it will only be stopped, otherwise a new starts playing. No mixing and no loop.          ")
    pass

class FBUpAxis (Enumeration):
    """
    This enumeration indicates which up axis is used in the motion file (so far, only effective when loading c3d files).     
         
    """
    kFBUpAxisY=property(doc="Use the Y-axis as the up axis.          ")
    kFBUpAxisZ=property(doc="Use the Z-axis as the up axis.          ")
    pass

class FBUseChnMode (Enumeration):
    """
    Use Channel modes.     
         
    """
    kFBUseChannelLeftOnly=property(doc="Left channel will be played in both speakers.          ")
    kFBUseChannelRightOnly=property(doc="Right channel will be played in both speakers.          ")
    kFBUseChannelBoth=property(doc="Default mode, where each channel play in its respective speaker.          ")
    pass

class FBVideoCodecMode (Enumeration):
    """
    Enum FBVideoRenderDepth.     
    See sample: render.py.     
    """
    FBVideoCodecAsk=property(doc="Pop codec selection dialog each render.          ")
    FBVideoCodecUncompressed=property(doc="Assume uncompressed codec.          ")
    FBVideoCodecStored=property(doc="Pop dialog and stored its value          ")
    pass

class FBVideoFormat (Enumeration):
    """
    Video color modes.     
         
    """
    kFBVideoFormat_Any=property(doc="        ")
    kFBVideoFormat_Other=property(doc="        ")
    kFBVideoFormat_RGBA_32=property(doc="        ")
    kFBVideoFormat_RGB_24=property(doc="        ")
    kFBVideoFormat_BGRA_32=property(doc="        ")
    kFBVideoFormat_BGR_24=property(doc="        ")
    kFBVideoFormat_BGR_16=property(doc="        ")
    kFBVideoFormat_ABGR_32=property(doc="        ")
    kFBVideoFormat_ARGB_32=property(doc="        ")
    kFBVideoFormat_422=property(doc="        ")
    pass

class FBVideoInterlaceMode (Enumeration):
    """
    Video interlace modes.     
         
    """
    kFBVideoInterlaceNone=property(doc="No interacling.          ")
    kFBVideoInterlaceHalfFrameEven=property(doc="Half frame (even field).          ")
    kFBVideoInterlaceHalfFrameOdd=property(doc="Half frame (odd field).          ")
    kFBVideoInterlaceFullFrameEven=property(doc="Full frame (even field).          ")
    kFBVideoInterlaceFullFrameOdd=property(doc="Full frame (odd field).          ")
    pass

class FBVideoLiveType (Enumeration):
    """
    Video Live type.     
         
    """
    kFBVideoLiveDefault=property(doc="Generic video input, type not specified.          ")
    kFBVideoLiveBasic=property(doc="Basic video input, like webcam and dv camera.          ")
    pass

class FBVideoProxyMode (Enumeration):
    """
    Video proxy modes.     
         
    """
    kFBVideoProxyNone=property(doc="No video proxy.          ")
    kFBVideoProxyOnPlay=property(doc="Video proxy on play.          ")
    kFBVideoProxyAlways=property(doc="Always video proxy.          ")
    pass

class FBVideoRenderDepth (Enumeration):
    """
    Enum FBVideoRenderDepth.     
    See samples: render.py, render.py.     
    """
    FBVideoRender24Bits=property(doc="24 bits          ")
    FBVideoRender32Bits=property(doc="32 bits          ")
    FBVideoRenderDepthCount=property(doc="Depth Count.          ")
    pass

class FBVideoRenderFieldMode (Enumeration):
    """
    Enum FBVideoRenderFieldMode.     
         
    """
    FBFieldModeNoField=property(doc="No Field.          ")
    FBFieldModeField0=property(doc="Field 0.          ")
    FBFieldModeField1=property(doc="Field 1.          ")
    FBFieldModeHalfField0=property(doc="Half Field 0.          ")
    FBFieldModeHalfField1=property(doc="Half Field 1.          ")
    FBFieldModeCount=property(doc="Count.          ")
    pass

class FBVideoRenderViewingMode (Enumeration):
    """
    Enum FBVideoRenderViewingMode.     
         
    """
    FBViewingModeStandard=property(doc="Standard.          ")
    FBViewingModeModelsOnly=property(doc="Model Only.          ")
    FBViewingModeXRay=property(doc="X-Ray.          ")
    FBViewingModeCurrent=property(doc="Current.          ")
    FBViewingModeCount=property(doc="Count.          ")
    pass

class FBVideoResolution (Enumeration):
    """
    Video Resolution (1D)      
        
    """
    kFBVideo_RES_FULL=property(doc="        ")
    kFBVideo_RES_1=property(doc="        ")
    kFBVideo_RES_2=property(doc="        ")
    kFBVideo_RES_4=property(doc="        ")
    kFBVideo_RES_8=property(doc="        ")
    kFBVideo_RES_16=property(doc="        ")
    kFBVideo_RES_32=property(doc="        ")
    kFBVideo_RES_64=property(doc="        ")
    kFBVideo_RES_128=property(doc="        ")
    kFBVideo_RES_256=property(doc="        ")
    kFBVideo_RES_512=property(doc="        ")
    kFBVideo_RES_1K=property(doc="        ")
    kFBVideo_RES_2K=property(doc="        ")
    kFBVideo_RES_4K=property(doc="        ")
    kFBVideo_RES_8K=property(doc="        ")
    pass

class FBVideoStorageMode (Enumeration):
    """
    Video storage modes.     
         
    """
    kFBVideoStorageDisk=property(doc="Storage on disk.          ")
    kFBVideoStorageMemory=property(doc="Storage in memory.          ")
    kFBVideoStorageDiskAsync=property(doc="Storage on disk async access.          ")
    pass

class FBView (FBVisualComponent):
    """
    Generic view.     
         
    """
    def FBView(self):
        """
        Constructor.

        """
        pass

    def DrawString(self,pText,pX,pY,pEnable):
        """
        Draw a string in the view.

        pText : Text to draw. 
        pX : X position of string. 
        pY : Y position of string. 
        pEnable : Is string enabled? (default =-1) 
        """
        pass

    def IsView(self):
        """
        Checks if object is a view.

        return : Is object a view? (<b>true</b> or <b>false</b>) 
        """
        pass

    def Refresh(self,pNow):
        """
        Refresh view.

        pNow : If <b>true</b>, refresh immediately (default = <b>false</b>). 
        """
        pass

    def SetViewport(self,pX,pY,pW,pH):
        """
        Set view's viewport.

        pX : Viewport X value. 
        pY : Viewport Y value. 
        pW : Viewport W (width) value. 
        pH : Viewport H (height) value. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    DoubleBuffer=property(doc="<b>Read Only Property:</b> Indicates if the view is double buffered.          ")
    GraphicOGL=property(doc="<b>Read Only Property:</b> Indicates if the view is OpenGL.          ")
    pass

class FBViewerMode (Enumeration):
    """
    Different viewer modes for the 3D viewer.     
         
    """
    kFBViewerModeOneWindow=property(doc="View one pane.          ")
    kFBViewerModeTwoWindow=property(doc="View two panes.          ")
    kFBViewerModeThreeWindow=property(doc="View three panes.          ")
    kFBViewerModeFourWindow=property(doc="View four panes.          ")
    kFBViewerModeSchematic=property(doc="Schematic view.          ")
    pass

class FBVisibilityState (Enumeration):
    """
    Visibility state.     
         
    """
    kFBVisibilityAny=property(doc="Any object requested is visible.          ")
    kFBVisibilityAll=property(doc="All objects requested are visible.          ")
    kFBVisibilitySome=property(doc="Some objects (at least one, but not all) requested are visible.          ")
    kFBVisibilityInvalid=property(doc="Invalid visibility request.          ")
    pass

class FBVisualContainer (FBVisualComponent):
    """
    Used to create a container for a tool UI.     
    See samples: Container.py, PropertyDrop.py, TutorialBox.py.     
    """
    def FBVisualContainer(self):
        """
        Constructor.

        """
        pass

    def GetSelection(self):
        """
        Get the selected item.

        return : Index of current selection. 
        """
        pass

    def ItemIconSet(self,pRef,pImage,pUseACopyOfTheImage):
        """
        Set an item's icon.

        pRef : Reference to item in container. 
        pImage : Handle to image to use. 
        pUseACopyOfTheImage : Create a copy of the image?(default=true) 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ItemIconSet(self,pRef,pFilename):
        """
        Set an item's icon.

        pRef : Reference to item in container. 
        pFilename : Name of file where image is located. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def ItemNameEdit(self,pRef):
        """
        Edit a container item.

        pRef : Reference of container to edit. 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    IconPosition=property(doc="<b>Read Write Property:</b> Where the icon is positioned for the items.          ")
    ItemHeight=property(doc="<b>Read Write Property:</b> Item height.          ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current item selected.          ")
    ItemWidth=property(doc="<b>Read Write Property:</b> Item width.          ")
    ItemWrap=property(doc="<b>Read Write Property:</b> Are items wrapped when enough space is available?          ")
    Items=property(doc="<b>List:</b> Names of items in container.          ")
    OnChange=property(doc="<b>Event:</b> Container contents changed.          ")
    OnDblClick=property(doc="<b>Event:</b> Double click.          ")
    OnDragAndDrop=property(doc="<b>Event:</b> Drag and Drop event.          ")
    Orientation=property(doc="<b>Read Write Property:</b> Orientation of container.          ")
    pass

class FBWebView (FBVisualComponent):
    """
    Web viewer.     
    See sample: WebView.py.     
    """
    def FBWebView(self):
        """
        Constructor.

        """
        pass

    def Load(self,pURL):
        """
        Load the specified Url.

        pURL : url to load in the WebView. 
        """
        pass

    pass

class FBWidgetHolder (FBVisualComponent):
    """
    Native Widget Holder (can be used to embed native Qt Widget inside MoBu UI elements) A Widget holder provides a bridge to instantiate a Native Qt widget into MB framework.     
     This will be used to allow user to create UI with QT designer and hook their created UI into MB. To allow a FBWidgetHolder to work properly, you need to specify a Creator function. This function will be called when needed to instantiate the native Widget.Or override WidgetCreate(QWidget* pParent) function in the subclass./bin/config/Scripts/UI/ToolNativeWidgetHolder.py for python usage example. See samples: MBFileRefDemo.py, ToolNativeWidgetHolder.py.     
    """
    def FBWidgetHolder(self):
        """
        Constructor.

        """
        pass

    pass

class FBActionManager (FBComponent):
    """
    Action Manager class.     
     <b>This class is introduced to enable users to access to the actions related functions. between versions.</b>      
    """
    pass

class FBActorFace (FBComponent):
    """
    Used to plot actor face animation.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBActorFace(self,pName):
        """
        Constructor.

        pName : Name of new actor face. 
        """
        pass

    def FBDelete(self):
        """
        Actual Actor Face destructor.
        This method is used to delete the actual actor face object represented by an instance of FBActorFace.

        """
        pass

    def PlotAnimation(self):
        """
        Plot the animation of the actor face.

        return : True if the operation completed successfully. 
        """
        pass

    pass

class FBAnimationLayer (FBComponent):
    """
    Used to access animation layer properties and modify them.     
     Changing the various properties of the layers will modify how the animation will be interpreted. For example, muting a layer will mute all the animation contained on the layer. You can access the animation layer object from the take, usign the FBTake::GetLayer() and FBTake::GetLayerByName(). See the FBTake class for more details. See samples: AnimationLayers.py, MergeAnimationLayers.py.     
    """
    def FBAnimationLayer(self,pName,pLayerID):
        """
        Constructor.

        pName : Name of the animation layer. 
        pLayerID : ID to set for the new layer. 
        """
        pass

    def AddChildLayer(self,pAnimationLayer):
        """
        Add a child to the layer.
        Layer ID of the new child layer might change after parenting depending where the child layer was originally located.

        pAnimationLayer : Layer to set as a child. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetChildCount(self):
        """
        Get the child layer count of this layer.
        The count will only includes direct child of the layer.

        return : Child layer count, or -1 if unsuccessful 
        """
        pass

    def GetChildLayer(self,pIndex):
        """
        Get the nth child layer of this layer.

        pIndex : Index of the child layer to get. 
        return : Child animation layer located at pIndex 
        """
        pass

    def GetCompleteChildHierarchy(self,pChildArray):
        """
        Get the all the children hierarchy of the layer, including children not directly connected to this layer.

        pChildArray : Array of child layers, will be filled by the function. 
        """
        pass

    def GetLayerIndex(self):
        """
        Get the layer index.

        return : The layer index in the current layer hierarchy. This value will change if the hierarchy is modified. Return -1 if unsuccessful. 
        """
        pass

    def GetParentLayer(self):
        """
        Get the parent layer.

        return : A pointer to the parent layer or NULL if the layer doesn't have a parent. 
        """
        pass

    def IsSelected(self):
        """
        Verify if the layer is selected.

        return : True if the layer is selected, false otherwise. 
        """
        pass

    def SelectLayer(self,pValue,pExclusiveSelect):
        """
        Select the layer.
        This is the equivalent of selecting the layer in the UI in the Animation Layer Editor tool

        pValue : True if the layer will be selected, false otherwise. 
        pExclusiveSelect : If pValue is true, passing true will deselect all the other layers, creating an exclusive selection, it will also set the layer as the current layer. 
        """
        pass

    def SetParentLayer(self,pParentLayer):
        """
        Set the parent layer.

        pParentLayer : A pointer to the parent layer or NULL if you want to unparent the layer. 
        """
        pass

    LayerMode=property(doc="<b>Read Write Property:</b> Layer mode. By default, the layer is in kFBLayerModeAdditive mode. Cannot be applied to the BaseAnimation Layer.          ")
    LayerRotationMode=property(doc="<b>Read Only Property:</b> Layer rotation mode. Cannot be applied to the BaseAnimation Layer.          ")
    Lock=property(doc="<b>Read Write Property:</b> If true, the layer is locked. You cannot modify keyframes on a locked layer.          ")
    Mute=property(doc="<b>Read Write Property:</b> If true, the layer is muted. A muted layer is not included in the result animation. Cannot be applied to the BaseAnimation Layer.          ")
    Solo=property(doc="<b>Read Write Property:</b> If true, the layer is soloed. When you solo a layer, you mute other layers that are at the same level in the hierarchy, as well as the children of those layers. Cannot be applied to the BaseAnimation Layer.          ")
    Weight=property(doc="<b>Read Write Property:</b> The weight value of a layer determines how much it is present in the result animation. Takes a value from 0 (the layer is not present) to 100. The weighting of a parent layer is factored into the weighting of its child layers, if any. BaseAnimation Layer always has a Weight of 100.          ")
    pass

class FBAnimationNode (FBComponent):
    """
    See samples: CopyAnimation.py, ClearKeysOnSelectedModels.py, TraversingRelationConstraint.py, FCurveEditor.py.     
        
    """
    def FBAnimationNode(self,pName):
        """
        Constructor.

        pName : Name of animation node (default is NULL). 
        """
        pass

    def ConvertGlobalToNodeTime(self,pKeyTime):
        """
        Convert global time to node time.
        (NOTE: Only used in the context of a story clip)

        pKeyTime : Time of the key to convert. 
        """
        pass

    def ConvertNodeToGlobalTime(self,pKeyTime):
        """
        Convert node time to global time.
        (NOTE: Only used in the context of a story clip)

        pKeyTime : Time of the key to convert. 
        """
        pass

    def GetAnimationToPlay(self):
        """
        Get animation node to play from.

        return : Animation node to be played. 
        """
        pass

    def GetAnimationToRecord(self):
        """
        Get animation node to record to.

        return : Animation node to record to. 
        """
        pass

    def GetDataDoubleArrayCount(self):
        """
        If the DataPtr is of numeric value type ...
        get the size of the array ex: Light Intensity:1, Translation 3

        return : Size of DataPtr array. 
        """
        pass

    def GetSizeOfData(self):
        """
        Get sizeof void Data Ptr.

        """
        pass

    def IsKey(self):
        """
        Verifies if there is a key at the current.

        return : <b>true</b> if there is a key at the current time. 
        """
        pass

    def KeyAdd(self,pTime,pData,pInterpolation,pTangentMode):
        """
        Add a key to the animation node.

        pTime : Time to add key at. 
        pData : Value of data to add at <b>pTime</b>. 
        pInterpolation : Interpolation type of the inserted key, default value is Cubic interpolation. 
        pTangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth). 
        """
        pass

    def KeyAdd(self,pData,pInterpolation,pTangentMode):
        """
        Add a key to the animation node at current time.

        pData : Value of data to add. 
        pInterpolation : Interpolation type of the inserted key, default value is Cubic interpolation. 
        pTangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth). 
        """
        pass

    def KeyCandidate(self,pTime):
        """
        Keys the current candidate values if no time is specified, at current time.

        pTime : Time at which to insert the key. 
        """
        pass

    def KeyRemove(self):
        """
        Remove key at current time.

        """
        pass

    def KeyRemoveAt(self,pTime):
        """
        Remove key at the specified time.

        pTime : Time for the key 
        """
        pass

    def ReadData(self,Data,pEvaluateInfo,pConvertGlobalToLocal):
        """
        Read data from animation node.

        Data : Data to read from animation node. 
        pEvaluateInfo : Node evaluation information (access to system and local time). 
        pConvertGlobalToLocal : If global transform data is read, convert it to local data. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReadData(self,Data,pTime,pConvertGlobalToLocal):
        """
        Read data from animation node.
        This will launch a new evaluation buffer to read the data and therefore this call is only safe if it is executed from the main thread, e.g. within a tool. In all other cases, you should use ReadData( double <b>Data, FBEvaluateInfo</b> pEvalInfo );

        Data : Data to read from animation node. 
        pTime : Time to read. 
        pConvertGlobalToLocal : If global transform data is read, convert it to local data. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReadData(self,Data):
        """
        Read the last data evaluated for this animation node ...
        this call doesn't generate a pull on the connection attached to this AnimationNode. No validation is done on the pointer size. You must provide a buffer that is at least GetSizerOfData() size.

        Data : Data to read from animation node. 
        return : <b>true</b> if successful. 
        """
        pass

    def SetBufferType(self,pGlobal):
        """
        Set buffer type for ANIMATIONNODE_TYPE_LOCAL_TRANSLATION, ANIMATIONNODE_TYPE_LOCAL_ROTATION and ANIMATIONNODE_TYPE_LOCAL_SCALE.

        pGlobal : Is buffer local or global. 
        """
        pass

    def SetCandidate(self,Data,pCheckLocked):
        """
        Set the current candidate values for current time.

        Data : float
        pCheckLocked : Decides whether to check the locked status. 
        return : <b>true</b> if successful. 
        """
        pass

    def WriteData(self,Data,pEvaluateInfo):
        """
        Write data to animation node.

        Data : Data to write to animation node. 
        pEvaluateInfo : Node evaluation information (access to system and local time). 
        return : <b>true</b> if successful. 
        """
        pass

    ConnectorType=property(doc="<b>Read Only Property:</b> Animation node connector type.          ")
    DefaultInterpolation=property(doc="<b>Read Write Property:</b> Default type of interpolation.          ")
    FCurve=property(doc="<b>Read Write Property:</b> FCurve for animation. See sample: StartKeysAtCurrentTime.py.         ")
    KeyCount=property(doc="<b>Read Only Property:</b> Number of keys.          ")
    Label=property(doc="<b>Read Write Property:</b> Label (UI Name).          ")
    Live=property(doc="<b>Read Write Property:</b> Is animation live?          ")
    Nodes=property(doc="<b>List:</b> List of animation nodes.          ")
    RecordMode=property(doc="<b>Read Write Property:</b> Is the node in recording mode (device connectors)?          ")
    UserName=property(doc="<b>Read Only Property:</b> Name of animation node.          ")
    pass

class FBApplication (FBComponent):
    """
    FBApplication is used mainly to manage files.     
     It provides functionality like that in the MotionBuilder file menu, for example, open file, save file.Note that event registration is instanced-based. When an FBApplication object is destroyed, all the event callbacks are unregistered. If you want to have a tool to be notified of events, it needs to have a FBApplication data member. See samples: FBFbxOptions.py, FBSystemEvents.py, ImportWithNamespace.py, BatchExportCharacterAnimationTool.py, ExportAnimationLibrary.py, SaveOneTakePerFile.py.     
    """
    def FBApplication(self):
        """
        Constructor.

        """
        pass

    def AudioRender(self,pAudioRenderOptions):
        """
        Render audio of current scene to media file, currently WAV file only.

        pAudioRenderOptions : The options used when rendering audio of the scene. Default value: 2 channels, 16 bits, 44100 hz, the begin and end time span for current time referential, Default file name is "Output.wav" in the last audio output path, ro the default document path if the last path doesn't exist. 
        return : True if the file was rendered successfully 
        """
        pass

    def ExecuteScript(self,pFilename):
        """
        Execute a python script file.

        pFilename : The script file to execute. 
        return : True if the script file was found and executed. 
        """
        pass

    def FileAppend(self,pFilename,pShowUIMsg,pOptions):
        """
        Append one or multiple files to the current scene.
        Same as File->Merge in the menus with all options set to append. In earlier versions of MotionBuilder, a namespace could be specified with a parameter in this function, or FBFbxOptions::CustomImportNamespace, Now this is now done with FBFbxOptions::NamespaceList.

        pFilename : File(s) to merge. For multiple files, use a list of files separated by '~'. 
        pShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false). 
        pOptions : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and pShowUIMsg are true. It is possible to append multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored. 
        return : true if successful. 
        """
        pass

    def FileBatch(self,pBatchOptions,pPlotOptions):
        """
        Start a batch.
        Command File->Batch... in the menus.

        pBatchOptions : The options for the batch process (same as in the batch UI). 
        pPlotOptions : The options for plotting (same as in the plot UI)(default=NULL). 
        return : The status of the operation. 
        """
        pass

    def FileExit(self,pSave,pExitCode):
        """
        Quit application.
        Command File->Exit in the menus.

        pSave : true if file is saved on exit(default=false). 
        pExitCode : Exit code of the application(default=0). 
        """
        pass

    def FileExport(self,pFilename):
        """
        Export a motion file.
        Command File->Motion File Export... in the menus.

        pFilename : The file to create. To create two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2"). 
        return : True if the export succeeded. 
        """
        pass

    def FileExportBatch(self,pName,pTake,pBatchOptions,pExportModels):
        """
        Export a motion file using batch options.
        Export used for saving files in batch process.

        pName : The name of the file without extension. Extension and path will be taken from batch options. 
        pTake : Animation take to the export. 
        pBatchOptions : The options for the export. 
        pExportModels : Models to the export. 
        return : True if the export succeeded. 
        """
        pass

    def FileImport(self,pFilename,pMatchModels,pCreateUnmatchedModels):
        """
        Import a motion file.
        Command File->Motion File Import... in the menus.

        pFilename : The file to import. To import two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2"). 
        pMatchModels : If there is already a model in the scene with the same name, the model will not be created and we replace the animation of the given model. 
        pCreateUnmatchedModels : Whether unmatched models will be created. This flag matters only when pMatchModels is true. when pMatchModels is false, all the models are created. 
        return : True if the import succeeded. 
        """
        pass

    def FileImportBatch(self,pName,pBatchOptions,pReference):
        """
        Import a motion file using batch options.
        Import used for loading files in batch process.

        pName : The name of the file without extension. Extension and path will be taken from batch options. 
        pBatchOptions : The options for the import. 
        pReference : Reference model for the import. 
        return : True if the import succeeded. 
        """
        pass

    def FileImportWithOptions(self,pOptions):
        """
        Import a motion file with the ability to specify options.
        Command File->Motion File Import... in the menus.

        pOptions : A FBMotionFileOptions object that contains the path to the files, as well as the options to load those motion files. 
        return : True if the import succeeded. 
        """
        pass

    def FileMerge(self,pFilename,pShowUIMsg,pOptions):
        """
        Merge one or multiple files with the current scene.
        Command File->Merge in the menus.

        pFilename : File(s) to merge. For multiple files, use a list of files separated by '~'. 
        pShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false). 
        pOptions : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and pShowUIMsg are true. It is possible to merge multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored. 
        return : true if successful. 
        """
        pass

    def FileMerge(self,pPathlist,pShowUIMsg,pOptions):
        """
        Merge multiple files with the current scene.
        Command File->Merge in the menus.

        pPathlist : Files to merge. 
        pShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false). 
        pOptions : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and pShowUIMsg are true. It is possible to merge multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored. 
        return : true if successful. 
        """
        pass

    def FileNew(self,pAskUser,pClearSceneName):
        """
        Command File->New in the menus.

        pAskUser : Set to true to cause a save dialog to popup. Default is false. 
        pClearSceneName : Set to true to clear the scene name, set to false to retain it. Default is true. 
        return : true if successful. 
        """
        pass

    def FileOpen(self,pFilename,pShowUIMsg,pOptions):
        """
        Open a file, replacing the current scene.
        Command File->Open in the menus.

        pFilename : File to open. 
        pShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false). 
        pOptions : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property and pShowUIMsg are true. 
        return : true if file open successfully.
        """
        pass

    def FileOpen(self,p0,pBufferLength):
        """
        Open a file from memory.

        p0 : the memory buffer for the file. Raw memory address is expected in pyfbsdk. 
        pBufferLength : the memory buffer size. 
        return : true if file opened successfully. 
        """
        pass

    def FileRender(self,pRenderOptions):
        """
        Render current scene to media file.
        Command File->Render in the menus.

        pRenderOptions : The options used when rendering the scene. If you don't specify them, current one are used. 
        return : True if the file was rendered successfully otherwise False and FBVideoGrabber.GetLastErrorMsg() contains the description of the error. 
        """
        pass

    def FileSave(self,pFilename,pOptions):
        """
        Save the file under another name.
        Command File->SaveAs in the menus.

        pFilename : Save file as pFilename. A value of NULL will use the current file name. 
        pOptions : Provide finer control on file save options (default=NULL) 
        return : true if successful.
        """
        pass

    def FlushEventQueue(self):
        """
        Flush event queue.
        Processes all pending events for the calling thread until there are no more events to process. You can call this function occasionally when your code is busy performing a long operation (e.g. copying a file).

        """
        pass

    def GetMaxFrameCount(self,p0,pBufferLength,pFrameCount,pTimeScale):
        """
        Get max frame count from a scene file in memory.

        p0 : the memory buffer for the file. Raw memory address is expected in pyfbsdk. 
        pBufferLength : the memory buffer size. 
        pFrameCount : out parameter to hold max frame count. this parameter is not needed in pyfbsdk. 
        pTimeScale : Time scale. 
        return : true if file opened successfully. In pyfbsdk, a tuple (bool, kLong) will return instead, the first one is ORSDK function return value, the second is for max frame count. 
        """
        pass

    def GetSceneAuthor(self):
        """
        Return the scene author from the scene properties.

        """
        pass

    def GetSceneComment(self):
        """
        Return the scene comment from the scene properties.

        """
        pass

    def GetSceneKeywords(self):
        """
        Return the scene keywords from the scene properties.

        """
        pass

    def GetSceneRevisionNumber(self):
        """
        Return the scene revision number from the scene properties.

        """
        pass

    def GetSceneSubject(self):
        """
        Return the scene subject from the scene properties.

        """
        pass

    def GetSceneTitle(self):
        """
        Return the scene title from the scene properties.

        """
        pass

    def IsSceneModified(self):
        """
        Is the scene modified since last save / new scene creation?

        return : True if the scene is modified since last save / new scene creation, false otherwise. 
        """
        pass

    def IsValidBatchFile(self,pFilename):
        """
        Verify motion file readability.

        pFilename : The file to test. 
        return : True if file was opened successfully (file is closed at the end). 
        """
        pass

    def LoadAnimationOnCharacter(self,pFileName,pCharacter,pFbxOptions,pPlotOptions):
        """
        Load a rig and its animation from a file.

        pFileName : File name. 
        pCharacter : Target character. 
        pFbxOptions : The options for the character rig and animation load 
        pPlotOptions : If the animation should be plotted on the target rig, these plot options will be used. Set to NULL if animation will not be plotted. 
        return : <b>true</b> if successful. 
        """
        pass

    def Maximize(self):
        """
        Maximize window (minimized).

        return : Operation was successful (true or false). 
        """
        pass

    def Minimize(self,pBlocking):
        """
        Minimize window.

        pBlocking : Is the minimization blocking operation (default = true). 
        return : Operation was successful (true or false). 
        """
        pass

    def OneClickAddToCurrentScene(self):
        """
        Send the scene and add it to the current scene in the specified application.

        return : True if transfer successful. 
        """
        pass

    def OneClickIsConnectedTo(self):
        """
        Return the other application that MotionBuilder is connected to.

        return : The application that MotionBuilder is connected to. 
        """
        pass

    def OneClickSelectPreviouslySentObject(self):
        """
        Select, in MotionBuilder, the object that were sent.

        """
        pass

    def OneClickSendAsNewScene(self,pApplication):
        """
        Send the current scene as a new scene in the specified application.

        pApplication : The application that will receive the scene. 
        return : True if transfer successful. 
        """
        pass

    def OneClickUpdateCurrentScene(self):
        """
        Send the scene to update the current scene in the specified application.

        return : True if transfer successful. 
        """
        pass

    def SaveCharacterRigAndAnimation(self,pFileName,pCharacter,pFbxOptions):
        """
        Save the rig and its animation in a file.

        pFileName : File name. 
        pCharacter : Character to save. 
        pFbxOptions : The options for the character rig and animation export 
        """
        pass

    def SetSceneAuthor(self,pAuthor):
        """
        Set the scene author.

        pAuthor : The author to set in the scene properties. 
        """
        pass

    def SetSceneComment(self,pComment):
        """
        Set the scene comment.

        pComment : The comment to set in the scene properties. 
        """
        pass

    def SetSceneKeywords(self,pKeywords):
        """
        Set the scene keywords.

        pKeywords : The keywords to set in the scene properties. 
        """
        pass

    def SetSceneRevisionNumber(self,pRevNumber):
        """
        Set the scene revision number.

        pRevNumber : The revision number to set in the scene properties. 
        """
        pass

    def SetSceneSubject(self,pSubject):
        """
        Set the scene subject.

        pSubject : The subject to set in the scene properties. 
        """
        pass

    def SetSceneTitle(self,pTitle):
        """
        Set the scene title.

        pTitle : The title to set in the scene properties. 
        """
        pass

    def UpdateAllWidgets(self):
        """
        Request to refresh display of all UI widgets.

        """
        pass

    CurrentActor=property(doc="<b>Read Write Property:</b> Indicate the current actor, as used by the character tool. Can be NULL. If not null, CurrentCharacter must be null, as the character tool works on only one item at a time.          ")
    CurrentCharacter=property(doc="<b>Read Write Property:</b> Indicate the current character, as used by the character tool. Can be NULL. If not null, CurrentActor must be null, as the character tool works on only one item at a time. See sample: CurrentCharacterGoToStancePose.py.         ")
    FBXFileName=property(doc="<b>Read Write Property:</b> Current scene filename.          ")
    OnFileExit=property(doc="<b>Event:</b> A File Exit as been requested, nothing has been destroyed yet.          ")
    OnFileMerge=property(doc="<b>Event:</b> A File Merge has been requested, nothing has been loaded yet.          ")
    OnFileNew=property(doc="<b>Event:</b> A File New has been requested, nothing has been destroyed yet.          ")
    OnFileNewCompleted=property(doc="<b>Event:</b> A File New has been completed.          ")
    OnFileOpen=property(doc="<b>Event:</b> A File Open has been requested, nothing has been loaded yet.          ")
    OnFileOpenCompleted=property(doc="<b>Event:</b> A File Open has been completed.          ")
    OnFileSave=property(doc="<b>Event:</b> A File Save has been requested, nothing has been saved yet.          ")
    OnFileSaveCompleted=property(doc="<b>Event:</b> A File Save has been completed.          ")
    OnOverrideFileOpen=property(doc="<b>Event:</b> Called when a file is about to be opened/merged. The user can override the process with his own file import system.          ")
    pass

class FBAssetItem (FBComponent):
    """
    Base class for all managed assets.     
         
    """
    def FBAssetItem(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def CheckIn(self,pComment,pKeepCheckedOut,pSilent):
        """
        Checks in this item and all its children (if this is a folder item).

        pComment : Comment to be applied for the check in. 
        pKeepCheckedOut : Flag that indicates whether the item will be kept checked out. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def CheckOut(self,pComment,pDontGetLocal,pSilent):
        """
        Checks out this item and it's childs (if this is a folder item) and makes them writeable on the local disk.

        pComment : Comment to be applied for the check out. 
        pDontGetLocal : Indicate if local copy should retrieved or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def GetLatest(self,pReplaceCheckedOut,pSilent):
        """
        Obtain the latest version of the item from the server.

        pReplaceCheckedOut : Whether to replace the checked out file or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    def GetLocalPath(self):
        """
        Get the path to this item on the local hard disk.

        return : The path as an <b>FBString</b>. 
        """
        pass

    def GetName(self):
        """
        Get the name of this item (file name or folder name).

        return : The name of the item, as an FBString. 
        """
        pass

    def GetParent(self):
        """
        Get the parent folder of this item.

        return : An <b>FBAssetFolder*</b> if the parent was found, or NULL if this is the root item. 
        """
        pass

    def GetServerPath(self):
        """
        Get the path to this item on the database.

        return : The server path as an <b>FBString</b>. 
        """
        pass

    def ShowHistory(self):
        """
        Display a dialog with this item history.

        """
        pass

    def ShowProperties(self):
        """
        Display a dialog showing the properties of this item.

        """
        pass

    def UndoCheckOut(self,pReplaceLocalFile,pSilent):
        """
        Cancel the last check out operation.

        pReplaceLocalFile : Flag indicating if the local item(s) should be replaced by the server version. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : A boolean indicating if the operation was successful. 
        """
        pass

    LastError=property(doc="Last error string.          ")
    pass

class FBAssetMng (FBComponent):
    """
    Used to access asset manager functionity to get files locally or from a server.     
         
    """
    def FBAssetMng(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def BrowseForFile(self):
        """
        Let the user browse the asset database to select a file.

        return : A file object representing the file that was selected, or NULL if none. 
        """
        pass

    def BrowseForFolder(self):
        """
        Let the user browse the asset database to select a folder.

        return : A FBAssetFolder* object representing the folder that was selected, or NULL if none. 
        """
        pass

    def CheckAvailability(self):
        """
        Check if this manager can be used on the computer.

        """
        pass

    def CreateServerPath(self,pServerPath):
        """
        Create a folder path on the server side by adding each missing folders.

        pServerPath : The path to create on the server side. 
        return : A FBAssetFolder* object representing the deepest folder of the path. 
        """
        pass

    def FileIsManaged(self,pFilename):
        """
        Is the specified local file managed (ie.
        also present in the database).

        pFilename : Path to the file on the local disk. 
        return : A boolean indicating if the file is managed or not. 
        """
        pass

    def GetAssetFile(self,pServerFilename):
        """
        Get a file object using it's server path.

        pServerFilename : Path to the file on the server. 
        return : An FBAssetFile* object, or NULL if the file was not found. 
        """
        pass

    def GetAssetFileFromLocalPath(self,pLocalFilename):
        """
        Get a file object using it's local path.

        pLocalFilename : Path to the file on the local disk. 
        return : An FBAssetFile* object, or NULL if the file was not found or no mapping could be done. 
        """
        pass

    def GetAssetFolder(self,pServerPath):
        """
        Get a folder object using it's server path.

        pServerPath : Path the the folder on the server. 
        return : An FBAssetFolder* object, or NULL if the folder was not found. 
        """
        pass

    def GetAssetFolderFromLocalPath(self,pLocalPath):
        """
        Get a folder object using it's local path.

        pLocalPath : Path to the folder on the local disk. 
        return : An FBAssetFolder* object, or NULL if the folder was not found or no mapping could be done. 
        """
        pass

    def GetFileOptions(self):
        """
        Get the file options (i.e.
        what to do when loading, saving or closing managed files).

        return : The options. 
        """
        pass

    def Initialize(self):
        """
        Initialize the connection to the server.

        return : <b>True</b> if the connection was established, <b>false</b> otherwise. 
        """
        pass

    def MapLocalPathToServerPath(self,pLocalPath):
        """
        Convert the local path to a server path by using managed paths mapping.

        pLocalPath : Local path to be mapped. 
        return : A string with the resulting server path, will be empty if the mapping fail. 
        """
        pass

    def ShowSettings(self):
        """
        Display a dialog that let the user changes settings.

        """
        pass

    def WithinManagedPath(self,pLocalPath):
        """
        Is the specified local path below a managed path.

        pLocalPath : Local path to be checked. 
        return : A boolean indicating if the path is within a managed path or not. 
        """
        pass

    Description=property(doc="<b>Read Write Property:</b> Description of the manager.          ")
    LastError=property(doc="Last error string.          ")
    MenuFlags=property(doc="<b>Read Write Property:</b> Flags specifing which menu items are added by the manager.          ")
    Name=property(doc="<b>Read Write Property:</b> Unique Name.          ")
    pass

class FBAudioClip (FBComponent):
    """
    Used to play audio clips and access their properties.     
     This class permits you to access audio clip's properties to read or change them. See sample: AudioTrackSetupTool.py.     
    """
    def FBAudioClip(self,pFileName,pSetToDefaultDest):
        """
        Constructor.

        pFileName : The complete file path of the media file to access. 
        pSetToDefaultDest : If true and the media file open successfully, it will automatically be connected to an output device. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def IsMediaReady(self):
        """
        Check if the audio clip constructed properly.

        return : true if the audio clip was constructed properly. 
        """
        pass

    def Play(self,pStyle,pDestination):
        """
        Play audio clip now.

        pStyle : How the audio clip should be triggered. 
        pDestination : Where the audio clip should be played. If NULL, it will play on the default destination. 
        return : Return true if the buffer for the audio clip was successfully allocated so that you can hear the sound. 
        """
        pass

    def Stop(self,pDestination):
        """
        Stop any playing triggered audio clip on a specified destination.

        pDestination : Where the audio clip is playing. If NULL, the default destination will be used. 
        """
        pass

    AccessMode=property(doc="<b>Read Write Property:</b> Specify the media data access mode between disk or memory.          ")
    Bits=property(doc="<b>Read Only Property:</b> the bits of media.          ")
    Channels=property(doc="<b>Read Only Property:</b> the number of channels in use.          ")
    ClipSpeed=property(doc="<b>Read Write Property:</b> The speed of the media when being played.          ")
    ConstrainDstToTake=property(doc="<b>Read Write Property:</b> Indicates whether to constrain the EndPoint to the end of the take.          ")
    CurrentTake=property(doc="<b>Read Write Property:</b> The take this media belongs to.          ")
    Destination=property(doc="<b>Read Write Property:</b> The audio output destination where the clip will be played.          ")
    DstDuration=property(doc="<b>Read Write Property:</b> When not used in the Story, this specify when the clips stops playing.          ")
    DstEnd=property(doc="<b>Read Write Property:</b> Total duration of this audio clip.          ")
    DstIn=property(doc="<b>Read Write Property:</b> When not used in the Story, this specify when the clips begin to play.          ")
    Duration=property(doc="<b>[Deprecated]Read Write Property:</b> Refer to DstDuration.          ")
    EndPoint=property(doc="<b>[Deprecated]Read Write Property:</b> Refer to DstEnd.          ")
    Filename=property(doc="<b>[Deprecated]Read Only Property:</b> Refer to Path          ")
    Format=property(doc="<b>Read Only Property:</b> Data format of media, including rate, bits and channels count. You can typecast it to a FBAudioFmt.          ")
    InPoint=property(doc="<b>[Deprecated]Read Write Property:</b> Refer to DstIn.          ")
    LockClipSpeed=property(doc="<b>Read Write Property:</b> Indicates whether to lock the current playing speed.          ")
    LockPitchToSpeed=property(doc="<b>Read Write Property:</b> Time stretch enabled factor.          ")
    Path=property(doc="<b>Read Only Property:</b> Full Path of the media.          ")
    Pitch=property(doc="<b>Read Write Property:</b> The audio clip pitch value. To write to this property, you must first set LockPitchToSpeed property to false.          ")
    Rate=property(doc="<b>Read Only Property:</b> the rate of media.          ")
    RelativePath=property(doc="<b>Read Only Property:</b> Relative path of media.          ")
    Scrubbing=property(doc="<b>Read Write Property:</b> Control which clip (one at a time) can shuttle when playing a various speeds.          ")
    SrcDuration=property(doc="<b>Read Only Property:</b> The duration time of media.          ")
    SrcEnd=property(doc="<b>Read Only Property:</b> The end time of media.          ")
    SrcIn=property(doc="<b>Read Only Property:</b> The begin time of media.          ")
    TakeSetsInPoint=property(doc="<b>[Deprecated]Read Write Property:</b> Indicates whether to lock the InPoint to the start of the take.          ")
    UseChannel=property(doc="<b>Read Write Property:</b> Enables you to control which track are used with stereo clips.          ")
    UseChannelMode=property(doc="<b>[Deprecated]Read Write Property:</b> Enables you to control which track are used with stereo clips.          ")
    pass

class FBAudioIn (FBComponent):
    """
    Audio In class.     
     Used to control Audio In objects (like a Microphone Audio Device). 
@code
# This example shows how to prepare an FBAudioIn object for recording
# by redirecting the audio to an FBAudioOut object and
# by specifying a desired audio format and target audio file

from pyfbsdk import *

# Let's see how many FBAudioIn objects are available
lAudioIns = FBSystem().AudioInputs
print 'The number of Audio Inputs:', len( lAudioIns )
if len( lAudioIns ) > 0:
    # Work with the first Audio In object available
    lAudioIn = lAudioIns[0]
    print 'Audio Input Name:', lAudioIn.Name
    
    # Let's turn it offline, if not already
    if lAudioIn.IsOnline():
        print 'Turned offline successful?', lAudioIn.SetOnline( False )
    
    # Let's set the first AudioOut available as the Audio In destination
    # if any destination is set yet
    # (Windows Only)
    if lAudioIn.GetDestination() == None:
        lAudioOuts = FBSystem().AudioOutputs
        print 'The number of Audio Outputs:', len( lAudioOuts )
        if len( lAudioOuts ) > 0:
            # Work with the first Audio Out object available
            lAudioOut = lAudioOuts[0]
            print 'Audio Output Name:', lAudioOut.Name
            print 'Setting destination successful?', lAudioIn.SetDestination( lAudioOut )
        else:
            print 'No available Audio Out object available for destination'
    else:
        print 'Audio Output <', lAudioIn.GetDestination().Name, '> already set for destination'
    
    # Let's try to record an audio file in 8-bit, 22060 hz and in stereo
    # Make sure this Audio In object supports this format
    lSupportedFormats = lAudioIn.GetSupportedFormats()
    if lSupportedFormats & FBAudioFmt_ConvertBitDepthMode( FBAudioBitDepthMode.kFBAudioBitDepthMode_8 ) != 0 and \
       lSupportedFormats & FBAudioFmt_ConvertRateMode( FBAudioRateMode.kFBAudioRateMode_22050 ) != 0 and \
       lSupportedFormats & FBAudioFmt_ConvertChannelMode( FBAudioChannelMode.kFBAudioChannelModeStereo ) != 0:
        
        # This format is supported, let's set it now
        lNewFormat  = FBAudioFmt_ConvertBitDepthMode( FBAudioBitDepthMode.kFBAudioBitDepthMode_8 )
        lNewFormat |= FBAudioFmt_ConvertRateMode( FBAudioRateMode.kFBAudioRateMode_22050 )
        lNewFormat |= FBAudioFmt_ConvertChannelMode( FBAudioChannelMode.kFBAudioChannelModeStereo )
        print 'Setting recording format successful?', lAudioIn.SetRecordingFormat( lNewFormat )
        
        # Let's add a delay of 3 frames
        # (Windows only)
        print 'Setting delay successful?', lAudioIn.SetDelay( FBTime( 0, 0, 0, 3 ) )
        
        # Let's turn it online now
        print 'Turned online successful?', lAudioIn.SetOnline( True )
        
        # Now, prepare the Audio In object for recording
        # To turn it off first, if already in 'Record' state
        if lAudioIn.IsReadyToRecord():
            print 'Turned Off Recording?', lAudioIn.TurnOffRecording()
        
        lAudioFilePath = 'C:\\temp\\myRecordedAudioFile.wav'
        
        # Note: To remove pop-ups that may occurs, if required, 
        # look at the optional parameters of the PrepareToRecord method
        print 'Preparing to record successful?', lAudioIn.PrepareToRecord( lAudioFilePath )
        
        if lAudioIn.IsReadyToRecord():
            print 'You are now ready to start recording and playback!'
        else:
            print 'Something failed while preparing to record! Tip: Do you have a C:\temp folder?'
        
    else:
        print 'This format (8-bit, 22060 hz, stereo) is not supported!'
else:
    print 'No available Audio In object available'
@endcode

     
    """
    def FBAudioIn(self):
        """
        Constructor.

        """
        pass

    def GetDelay(self):
        """
        Returns the delay currently set.
        (Windows only).

        return : The delay currently set. 
        """
        pass

    def GetDestination(self):
        """
        Returns the Audio Out object currently used as the destination.
        (Windows only).

        return : The Audio Out object currently used as the destination. Returns a NULL pointer (None in Python) if any Audio Out object is currently set. 
        """
        pass

    def GetRecordingFormat(self):
        """
        Returns the recording format (i.e.
        Bit Depth, Rate and Channel(s)) currently set.

        return : The audio format currently set for recording. 
        """
        pass

    def GetSupportedFormats(self):
        """
        Returns all the Audio In supported formats (i.e.
        Bit Depths, Rates and Channels).

        return : The Audio In supported formats. 
        """
        pass

    def IsOnline(self):
        """
        Is the Audio In online?

        return : True if the Audio In is online, false if it is offline. 
        """
        pass

    def IsReadyToRecord(self):
        """
        Is the Audio In ready to record (has it been prepared properly)?

        return : True if the audio is ready to record, false otherwise. 
        """
        pass

    def PrepareToRecord(self,pRecordingPath,pExistingClipAction,pExistingFileAction):
        """
        Prepares the Audio In for recording (similar as checking the 'Record' checkbox in the UI).
        If the Audio In is not already online, it will turn it online automatically. If the Audio In is already ready to record, it will turn it off first automatically.

        pRecordingPath : The file path for the desired output wav file. The file must have the .wav extension. 
        pExistingClipAction : The action to perform when the action clip associated to the recording path is already in the scene. 
        pExistingFileAction : The action to perform when the file associated to the recording path already exists on disk and it not empty. 
        return : True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified file is not a WAV file or is invalid, the operation is abort by the user, etc.). 
        """
        pass

    def SetDelay(self,pDelay):
        """
        Sets the delay to use.
        The Audio In must be offline when this method is called. (Windows only).

        pDelay : The delay to use. To mimic the UI, the FBTime should refer to a frame number. 
        return : True if operation is successful, false otherwise. 
        """
        pass

    def SetDestination(self,pAudioOut):
        """
        Sets the Audio Out object to be used as the destination.
        The Audio In must be offline when this method is called. (Windows only).

        pAudioOut : The Audio Out object to be used as the destination. Use a NULL pointer (None in Python) to unset the destination. 
        return : True if operation is successful, false otherwise. 
        """
        pass

    def SetOnline(self,pOnline):
        """
        Turns Audio In online or offline.

        pOnline : True to turn the Audio In online, false to turn it offline. 
        return : True if operation is successful, false otherwise. 
        """
        pass

    def SetRecordingFormat(self,pAudioFormat):
        """
        Sets the recording format (i.e.
        Bit Depth, Rate and Channel(s)) to use. The Audio In must be offline when this method is called.

        pAudioFormat : The audio format to use for recording. It must specify a unique Bit Depth, Rate and Channels. 
        return : True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified audio format is not supported, more than one Bit Depth is specified, etc.). 
        """
        pass

    def TurnOffRecording(self):
        """
        Turns off the Audio In recording (similar as un-checking the 'Record' checkbox in the UI).

        return : True if operation is successful, false otherwise. 
        """
        pass

    pass

class FBAudioOut (FBComponent):
    """
    Audio Out class.     
     Properties of this class are work in progress, but you can still list them and get their names.      
    """
    def FBAudioOut(self):
        """
        Constructor.

        """
        pass

    pass

class FBBox (FBComponent):
    """
    A box is a fundamental building block in the application architecture.     
     All animatable elements are derived in some way from the main box class, either by deriving directly or owning a box.      
    """
    def FBBox(self,pName):
        """
        Constructor.

        pName : Box name. 
        """
        pass

    def AnimationNodeDestroy(self,pAnimationNode):
        """
        Destroy an animation node.

        pAnimationNode : Handle to the animation node to be destroyed. 
        return : <b>true</b> if destruction was successful. 
        """
        pass

    def AnimationNodeInGet(self):
        """
        Get the (IN/OUT) animation node for this box.

        return : A handle to the animation node for this box. 
        """
        pass

    def AnimationNodeIsUserData(self,pAnimationNode):
        """
        Is the animation node user data?

        pAnimationNode : Handle to the animation to be queried. 
        return : <b>true</b> if node is user data. 
        """
        pass

    def AnimationNodeOutGet(self):
        """
        """
        pass

    def GetInConnector(self,pIndex):
        """
        Get the animation node input associated with the given index.

        pIndex : The animation node input associated with the given index. 
        return : The animation node input, or NULL if the pIndex value is invalid. 
        """
        pass

    def GetInConnectorCount(self):
        """
        Get the number of animation node inputs for this box.

        return : The number of animation node inputs for this box. 
        """
        pass

    def GetOutConnector(self,pIndex):
        """
        Get the animation node output associated with the given index.

        pIndex : The animation node output associated with the given index. 
        return : The animation node output, or NULL if the pIndex value is invalid. 
        """
        pass

    def GetOutConnectorCount(self):
        """
        Get the number of animation node outputs for this box.

        return : The number of animation node outputs for this box. 
        """
        pass

    Animatable=property(doc="<b>Read Write Property:</b> Is the box animatable.          ")
    Live=property(doc="<b>Read Write Property:</b> Is live?          ")
    RecordMode=property(doc="<b>Read Write Property:</b> Is recording?          ")
    UniqueName=property(doc="internal Unique name.          ")
    pass

class FBCameraSwitcherAudioManager (FBComponent):
    """
    Camera Switcher Audio Manager class.     
     <b>This class allows users to interact with the Audio Manager of the Camera Switcher.</b>      
    """
    def GetAudioClip(self):
        """
        Get the Audio Clip displayed on the Camera Switcher.

        return : The Audio Clip displayed, nullptr (C++) / None (Python) if any. 
        """
        pass

    def GetAudioTrack(self):
        """
        Get the Audio Track displayed on the Camera Switcher.

        return : The Audio Track displayed, nullptr (C++) / None (Python) if any. 
        """
        pass

    def GetLockPitchToSpeed(self):
        """
        Get the 'Lock Pitch to Speed' state.

        return : True if the 'Lock Pitch to Speed' state is set, false otherwise. 
        """
        pass

    def GetShowAudio(self):
        """
        Get the 'Show Audio' state.

        return : True if the 'Show Audio' state is set, false otherwise. 
        """
        pass

    def GetShowLeftChannel(self):
        """
        Get the 'Show Left Channel' state.

        return : True if the 'Show Left Channel' state is set, false otherwise. 
        """
        pass

    def GetShowRightChannel(self):
        """
        Get the 'Show Right Channel' state.

        return : True if the 'Show Right Channel' state is set, false otherwise. 
        """
        pass

    def RemoveAudio(self):
        """
        Remove the audio clip or audio track currently displayed on the Camera Switcher.

        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetAudioClip(self,pAudioClip):
        """
        Set the Audio Clip to display on the Camera Switcher.

        pAudioClip : The Audio Clip to display. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetAudioTrack(self,pAudioTrack):
        """
        Set the Audio Track to display on the Camera Switcher.

        pAudioTrack : The Audio Track to display. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetLockPitchToSpeed(self,pLock):
        """
        Set the 'Lock Pitch to Speed' state.

        pLock : True to lock pitch to speed, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowAudio(self,pShow):
        """
        Set the 'Show Audio' state.

        pShow : True to show the Audio waveform, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowLeftChannel(self,pShow):
        """
        Set the 'Show Left Channel' state.

        pShow : True to show the left channel, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowRightChannel(self,pShow):
        """
        Set the 'Show Right Channel' state.

        pShow : True to show the right channel, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    pass

class FBCharacterMarkerSet (FBComponent):
    """
    Character marker set class.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBCharacterMarkerSet(self,pName):
        """
        Constructor.

        pName : Name of new character marker set. 
        """
        pass

    def GetExtractionProperty(self,pNodeId):
        """
        Get the extraction property associated with each body part of the character.

        pNodeId : FBBodyNodeId
        return : The property associated with given pNodeId. 
        """
        pass

    def GetMarkersProperty(self,pNodeId):
        """
        Get the marker property associated with each body part of the character.

        pNodeId : FBBodyNodeId
        return : The property associated with given pNodeId. 
        """
        pass

    def GetSnapProperty(self,pNodeId,pWhat):
        """
        Get the snap property associated with each body part of the character for given transformation.
        Current version snap only translation and rotation.

        pNodeId : FBBodyNodeId
        pWhat : FBModelTransformationType
        return : The property associated with given pNodeId and pWhat. 
        """
        pass

    pass

class FBCluster (FBComponent):
    """
    Weighting interface for meshes.     
     This class is experimental. See sample: FBClusterTransactions.py.     
    """
    def ClusterBegin(self,pIndex):
        """
        Begin cluster definition.

        pIndex : Link index. 
        return : Index of last item(default=-1). 
        """
        pass

    def ClusterEnd(self):
        """
        End cluster definition.

        return : 0, (Not implemented). 
        """
        pass

    def LinkClearUnused(self,pThreshold):
        """
        Remove all unused links.

        pThreshold : Weight value under which links are considered unused (default=-1). 
        """
        pass

    def LinkGetAssociateModel(self,pLinkNumber):
        """
        Get model associated with link.

        pLinkNumber : Number value of link to get associated model from. 
        return : Model associated to link number pLinkNumber. 
        """
        pass

    def LinkGetCount(self):
        """
        Get number of links.

        return : Number of links. 
        """
        pass

    def LinkGetModel(self,pLinkNumber):
        """
        Get model from a link.

        pLinkNumber : Number value of link to get model from. 
        return : Model at link number pLinkNumber. 
        """
        pass

    def LinkGetName(self,pLinkNumber):
        """
        Get the name of a link.

        pLinkNumber : Number value of link to get name from. 
        return : Name of link number pLinkNumber. 
        """
        pass

    def LinkGetVertexIndex(self,pIndex):
        """
        Get current vertex at link.

        pIndex : Index of link to get vertex from. 
        return : Index value of the current vertex associated to link at index number pIndex 
        """
        pass

    def LinkRemove(self,pLinkNumber):
        """
        Remove a link.

        pLinkNumber : Number value of link to rename. 
        """
        pass

    def LinkSetCurrentVertex(self,pLinkIndex,pPointIndex):
        """
        Link at current vertex.

        pLinkIndex : Index of link to add vertex to. 
        pPointIndex : Index of vertex to add. 
        """
        pass

    def LinkSetModel(self,pModel):
        """
        Set model to a link.

        pModel : Model to set. 
        """
        pass

    def LinkSetName(self,pName,pLinkNumber):
        """
        Set the name of a link.

        pName : Name of the link. 
        pLinkNumber : Number value of link to name. 
        """
        pass

    def VertexAdd(self,pVertexIndex,pWeight):
        """
        Add a vertex to a cluster.

        pVertexIndex : Index of vertex to add. 
        pWeight : Weight to give to vertex. 
        """
        pass

    def VertexClear(self):
        """
        Clear all linked vertices.

        """
        pass

    def VertexGetCount(self):
        """
        Get the number of vertices.

        return : Number of vertices in a cluster. 
        """
        pass

    def VertexGetNumber(self,pIndex):
        """
        Get vertex number.

        pIndex : Index of link to get vertex from. 
        return : Number value of vertex at link number pIndex 
        """
        pass

    def VertexGetTransform(self,pPosition,pRotation,pScaling):
        """
        Get transform of a cluster set.

        pPosition : Position transform. 
        pRotation : Rotation transform. 
        pScaling : Scaling transform. 
        """
        pass

    def VertexGetWeight(self,pIndex):
        """
        Get vertex weight.

        pIndex : Index of link to get vertex from. 
        return : Weight of vertex found at link number pIndex. 
        """
        pass

    def VertexRemove(self,pVertexIndex):
        """
        Remove a vertex from a cluster.

        pVertexIndex : Index of vertex to remove. 
        """
        pass

    def VertexSetTransform(self,pPosition,pRotation,pScaling):
        """
        Set transform of a cluster set.

        pPosition : Position transform. 
        pRotation : Rotation transform. 
        pScaling : Scaling transform. 
        """
        pass

    def VertexSetWeight(self,pWeight,pIndex):
        """
        Set vertex weight.

        pWeight : Weight to give to vertex. 
        pIndex : Index of link to get vertex from. 
        """
        pass

    ClusterAccuracy=property(doc="<b>Read Write Property:</b> Cluster accuracy.          ")
    ClusterMode=property(doc="<b>Read Write Property:</b> Cluster mode.          ")
    pass

class FBConstraintManager (FBComponent):
    """
    Constraint manager.     
    See sample: FBConstraintManager.py.     
    """
    def TypeCreateConstraint(self,pTypeIndex):
        """
        Create a constraint by index.
        Given the index in the registry, this function create an instance of this constraint. The newly created constraint will be automatically added to the scene.

        pTypeIndex : Index of constraint type, must in range [0, TypeGetCount() ). 
        return : The newly created constraint, or NULL if pIndex is out of range. 
        """
        pass

    def TypeCreateConstraint(self,pName):
        """
        Create a constraint by name.
        Given the constraint type name in the registry, this function create an instance of this constraint. The newly created constraint will be automatically added to the scene.

        pName : the name of the constraint to be created. 
        return : The newly created constraint, or NULL if pName doesn't match any registered constraints. 
        """
        pass

    def TypeGetCount(self):
        """
        Get the number of registered constraint types.

        return : Number of registered constraint types. 
        """
        pass

    def TypeGetName(self,pTypeIndex):
        """
        Get the name of a registered type of constraint.
        This will search in the registry for a constraint at the index <b>pTypeIndex</b>.

        pTypeIndex : Index of a constraint type. 
        return : Name of constraint type. 
        """
        pass

    pass

class FBConstructionHistory (FBComponent):
    """
    Access to global construction history functionality.     
         
    """
    def FBConstructionHistory(self):
        """
        Constructor.

        """
        pass

    def GetDeltaOperations(self,pOperations,sinceCommandId):
        """
        GetDeltaOperations Get the list of delta operations in the construction history.

        pOperations : Array of operations, will be filled by the function. 
        sinceCommandId : int
        """
        pass

    def GetScriptOutput(self,script,errors):
        """
        GetScriptOutput Returns the output from the scripting engine.

        script : the script text 
        errors : the error outputted from the scripting engine 
        """
        pass

    def GetState(self):
        """
        GetState returns the current state of the construction history manager.

        return : returns a FBConstructionHistoryState indicating the state 
        """
        pass

    def NetDelete(self,component,key):
        """
        NetDelete Network delete with support for Network Undo.

        component : FBComponent
        key : A key that uniquely identifies the operation 
        """
        pass

    def NetUndo(self,key):
        """
        NetUndo Perform network undo operation.

        key : The operation to undo 
        """
        pass

    def RunOperation(self,operation,out_errors):
        """
        RunOperation Runs an operation.

        operation : The operation to run 
        out_errors : A string containing the text of errors generated by running the operations (if any) 
        """
        pass

    OnChange=property(doc="<b>Event:</b> History changed.          ")
    pass

class FBControlSet (FBComponent):
    """
    Control set class.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBControlSet(self,pName):
        """
        Constructor.

        pName : Name of new control set. 
        """
        pass

    def GetFKIndex(self,pModel):
        """
        Return The Index of the Given Model.

        pModel : Given Model to obtain Index 
        return : The Index of the Given Model. 
        """
        pass

    def GetFKModel(self,pIndex):
        """
        Return the object associated to the given Index.

        pIndex : Given Index to obtain Model 
        return : return the model at the specified Index. 
        """
        pass

    def GetFKName(self,pIndex):
        """
        return the name of FK Effector at the given index

        pIndex : Given Index 
        return : return the name of IK Effector Slot 
        """
        pass

    def GetIKEffectorIndex(self,pModel):
        """
        Return the Index of the Given Model.

        pModel : Given Model to Obtain Index 
        return : The Index of the Given Model. 
        """
        pass

    def GetIKEffectorModel(self,pEffectorIndex,pPivotIndex):
        """
        Return the object associated to the given Index.

        pEffectorIndex : Given Index to obtain Model 
        pPivotIndex : Index of effector pivot 
        return : return the model at the specified Index. 
        """
        pass

    def GetIKEffectorName(self,pEffectorIndex):
        """
        return the name of IK Effector

        pEffectorIndex : Given Index to obtain Name 
        return : the name of IK Effector 
        """
        pass

    def GetIKEffectorPivotCount(self,pEffectorIndex):
        """
        return the number of IK Effector Slot

        pEffectorIndex : FBEffectorId
        return : return the number of IK Effector Slot 
        """
        pass

    def GetReferenceModel(self):
        """
        Get the reference model associated with this Control Set.

        return : The reference model associated with the Control Set. 
        """
        pass

    def GetReferenceName(self):
        """
        Get the reference name associated with this Control Set.

        return : The reference name associated with the Control Set. 
        """
        pass

    ControlSetType=property(doc="<b>Read Property:</b> the control Set Type (FKIK or IK).          ")
    UseAxis=property(doc="<b>Read Write Property:</b> is using axis.          ")
    pass

class FBCycleCreator (FBComponent):
    """
    See sample: CycleCreator.py.     
        
    """
    def FBCycleCreator(self):
        """
        Constructor.

        """
        pass

    def CreateCycle(self,pStartTime,pEndTime,pChar,pMoveStartToZero,pAddZeroKey,pNewTakeName,pReferencedIK,pPasteTx,pPasteTy,pPasteTz,pPasteR,pPasteG):
        """
        Create animation cycle for current character if pChar is NULL, else for the character assigned by pChar; during the time scope between pStartTime and pEndTime.

        pStartTime : Start time of the cycle 
        pEndTime : End time of the cycle 
        pChar : Target character, if it is NULL, try to use current character 
        pMoveStartToZero : Whether move start time to zero time 
        pAddZeroKey : Whether add zero key 
        pNewTakeName : The name used to create the new take. 
        pReferencedIK : The IK that used as referenced object in pose pasting. 
        pPasteTx : Whether consider Translation X on referenced IK when doing pose pasting 
        pPasteTy : Whether consider Translation Y on referenced IK when doing pose pasting 
        pPasteTz : Whether consider Translation Z on referenced IK when doing pose pasting 
        pPasteR : Whether consider Rotation on referenced IK when doing pose pasting 
        pPasteG : Whether respect Gravity when doing pose pasting (Translation = Global XZ / Rotation = Global Y). Note: if G is true then Ty will be forced changed to false. 
        return : true if successful. 
        """
        pass

    pass

class FBDeck (FBComponent):
    """
    Interface to a tape deck.     
         
    """
    def FBDeck(self,pName):
        """
        Constructor.

        pName : Name of deck. 
        """
        pass

    def CueAt(self,pTime):
        """
        Cue deck at a given time.

        pTime : Time to cue deck at. 
        """
        pass

    def DeckAutoCommandsNotify(self):
        """
        Deck auto commands notification.

        """
        pass

    def DeckStatusUpdateNotify(self):
        """
        Interface to IObject.
        Deck status update notification.

        """
        pass

    def Eject(self):
        """
        Eject tape.

        """
        pass

    def Forward(self):
        """
        Fast forward.

        """
        pass

    def GetTime(self):
        """
        Get the deck's time.

        return : Time of deck. 
        """
        pass

    def Play(self,pSpeed):
        """
        Play forwards.

        pSpeed : Playback speed (default is 1.0). 
        """
        pass

    def ReversePlay(self,pSpeed):
        """
        Play backwards.

        pSpeed : Playback speed(default is 1.0). 
        """
        pass

    def Rewind(self):
        """
        Rewind.

        """
        pass

    def StepBack(self):
        """
        Step backwards.

        """
        pass

    def StepForward(self):
        """
        Step forwards.

        """
        pass

    def Stop(self):
        """
        Stop.

        """
        pass

    def ThreadSync(self):
        """
        """
        pass

    CassetteInside=property(doc="<b>Read Only Property:</b> Is the cassette inside?          ")
    EE=property(doc="<b>Read Write Property:</b> Is EE on?          ")
    IconFilename=property(doc="<b>Read Write Property:</b> Filename of icon for deck.          ")
    Latency=property(doc="<b>Read Write Property:</b> Latency of response for the deck;          ")
    Offset=property(doc="<b>Read Write Property:</b> Current offset for the TC.          ")
    Online=property(doc="<b>Read Write Property:</b> Is deck online?          ")
    PlayingBackward=property(doc="<b>Read Only Property:</b> Playing backwards?          ")
    PlayingForward=property(doc="<b>Read Only Property:</b> Playing forward?          ")
    PostRoll=property(doc="<b>Read Write Property:</b> Post-Roll.          ")
    PreRoll=property(doc="<b>Read Write Property:</b> Pre-Roll.          ")
    StandBy=property(doc="<b>Read Write Property:</b> In standby mode?          ")
    TransportControl=property(doc="<b>Read Write Property:</b> Mode w/r to TC (None, Sync, Main );          ")
    UniqueName=property(doc="internal Unique name.          ")
    pass

class FBDeformer (FBComponent):
    """
    Base Model deformer class.     
         
    """
    def FBDeformer(self,pName):
        """
        Constructor.

        pName : Name of deformer. 
        """
        pass

    DeformerType=property(doc="<b>Read Only Property:</b> Deformer Type.          ")
    pass

class FBDeviceInstrument (FBComponent):
    """
    Instrument abstraction layer.     
         
    """
    def FBDeviceInstrument(self,pDevice):
        """
        Constructor.

        pDevice : Parent device. 
        """
        pass

    def InstrumentRecordFrame(self,pRecordTime,pNotifyInfo):
        """
        Record the data to the function curves for the instrument.

        pRecordTime : Time to record data at. 
        pNotifyInfo : Device notification information structure. 
        """
        pass

    def InstrumentWriteData(self,pEvaluateInfo):
        """
        Write data to instrument's connectors.
        In the evaluation engine callback, this will take the data in the instrument's temporary data holders and write it to the connectors.

        pEvaluateInfo : Evaluation information structure. 
        return : <b>true</b> if successful. 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Is instrument active?          ")
    Device=property(doc="<b>Read Write Property:</b> Handle to owner device.          ")
    ModelTemplate=property(doc="<b>Read Write Property:</b> Model template to build instruments' structure.          ")
    pass

class FBDeviceOpticalMarker (FBComponent):
    """
    Device optical marker.     
     A device optical marker represents the input locations for interfacing optical hardware. This type of marker corresponds uniquely to the input (from the hardware) and will be represented on-screen by a <b>FBModelMarkerOptical</b>.      
    """
    def FBDeviceOpticalMarker(self,pName):
        """
        Constructor.

        pName : Name of optical marker. 
        """
        pass

    def SetData(self,pX,pY,pZ,pOcclusion):
        """
        Set data for optical marker.

        pX : X position for marker. 
        pY : Y position for marker. 
        pZ : Z position for marker(default=0.0). 
        pOcclusion : Occulsion information for marker(default=0.0). 
        """
        pass

    IsUsed=property(doc="<b>Property:</b> Is marker used?          ")
    Model=property(doc="<b>Property:</b> Model marker access.          ")
    Occlusion=property(doc="<b>Property:</b> Occulsion data for marker.          ")
    pass

class FBEvaluateManager (FBComponent):
    """
        
        
    """
    def InvalidateDAG(self):
        """
        Invalidate the DAG and trigger parallel scheduling at the next frame.

        """
        pass

    def IsInteractiveMode(self):
        """
        Check if the application main loop is in interactive or offline render mode.

        return : true if is application is is interactive mode. 
        """
        pass

    DeviceCount=property(doc="<b>Read only Property:</b> Number of devices to evaluate.          ")
    DualQuaternionSkinning=property(doc="<b>Read/Write Property:</b> Using state of the Dual Quaternion for skinning (CPU Skinning or GPU Skinning).          ")
    FrameSkipOptimization=property(doc="<b>Read/Write Property:</b> if true, apply frame skip optimization during playback. off-line rendering don't use frame skip optimization.          ")
    NodeCount=property(doc="<b>Read only Property:</b> Number of nodes to evaluate.          ")
    OnRenderingPipelineEvent=property(doc="<b> For callback events at rendering pipeline.</b>          ")
    OnSynchronizationEvent=property(doc="<b> For callback events at synchronization point.</b>          ")
    ParallelDeformation=property(doc="<b>Read/Write Property:</b> true if deformation is evaluated in parallel.          ")
    ParallelEvaluation=property(doc="<b>Read/Write Property:</b> true if parallel DAG schedule algorithm is being used. false when serial algorithm is being used.          ")
    ParallelPipeline=property(doc="<b>Read/Write Property:</b> true if transformation is evaluated in parallel.          ")
    ParallelScheduleType=property(doc="<b> DEPRICATED </b><b>Read/Write Property:</b> choose between serial and parallel DAG schedule algorithm. kFBParallelScheduleSimple and kFBParallelScheduleAdvanced will set ParallelEvalution to true. kFBParallelScheduleSerial will set ParallelEvalution to false          ")
    UseGPUDeformation=property(doc="<b>Read/Write Property:</b> true if GPU deformation is used.          ")
    pass

class FBFbxOptions (FBComponent):
    """
    Customize file loading and saving.     
    See samples: FBFbxOptions.py, ImportWithNamespace.py, BatchExportCharacterAnimationTool.py.     
    """
    def FBFbxOptions(self,pLoad,pFilePathToLoad):
        """
        Constructor.
        Create a FBFbxOption to be used in FBApplication Save/Load with default settings.

        pLoad : If true, will init option for a default Load (Append all elements and animation). If false will initialized options for a default Save (Save all elements and animation).  
        pFilePathToLoad : If pLoad is true, the client code should pass the file path to load to collect the take info; ignore when pLoad is false. 
        """
        pass

    def GetMultiLoadNamespaceList(self):
        """
        Returns the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge).
        This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored.

        return : The multi load namespace list currently set. 
        """
        pass

    def GetTakeCount(self):
        """
        Return the count of takes in the scene to saved or the file to loaded.

        """
        pass

    def GetTakeDescription(self,pTakeIndex):
        """
        Take Description.

        pTakeIndex : index of take to get. 
        """
        pass

    def GetTakeDestinationName(self,pTakeIndex):
        """
        Take Destination Name upon save or load.

        pTakeIndex : index of take to get. 
        """
        pass

    def GetTakeKeyRange(self,pTakeIndex):
        """
        Get take key range.

        pTakeIndex : index of take to get. 
        return : A time range, keys inside that time range will be kept. Keys outside that time range will be removed when importing the animation, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity 
        """
        pass

    def GetTakeName(self,pTakeIndex):
        """
        Take Original Name.

        pTakeIndex : index of take to get. 
        """
        pass

    def GetTakeSelect(self,pTakeIndex):
        """
        Return if true if the take will be saved or Loaded.

        pTakeIndex : index of take to get. 
        """
        pass

    def SaveToString(self,pString,context):
        """
        Serialize all options to a string Serialize all options to a string specifying a context.

        pString : The string containing all settings, target of serializing 
        context : The context to be used when serializing 
        """
        pass

    def SetAll(self,pElementAction,pAnimation):
        """
        Set All Options.
        Initialize all loading/saving properties to ElementAction and animation specified.

        pElementAction : Default value for all FBPropertyElementAction properties. 
        pAnimation : Default value for all Animation properties. 
        """
        pass

    def SetFromString(self,pString,context):
        """
        Set all options from string Set all parameters from a formatted string (previously serialized with SaveToString)

        pString : The string containing all settings. See SaveToFile 
        context : The context to be used when de-serializing 
        """
        pass

    def SetMultiLoadNamespaceList(self,pMultiLoadNamespaceList):
        """
        Sets the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge).
        The number of namespaces contained in this list must match the number of files merged, otherwise the merge operation will abort. The first namespace in the list will be applied on the first merged scene, the second namespace in the list will be applied on the second merged scene, and so one and so forth. This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored. 
@code
# This example shows how to merge multiple scenes, each scene in its own user specified namespace:

# Create an Load FBFbxOptions object
fbxLoadOptions = FBFbxOptions( True )

# Create a list of namespaces (2 items here, so the number of scenes to merge must also be 2)
# and set the list in the FBFbxOptions object
myNS = FBStringList( 'MyFirstNS~MySecondNS' )
fbxLoadOptions.SetMultiLoadNamespaceList( myNS )

# Create a list of scenes to merge
myScenesToMerge = FBStringList( 'C:\Temp\MyFirstScene.fbx~C:\Temp\AnotherScene.fbx' )

# Let's merge those scenes. The namespaces will be applied on the scenes' contents.
print FBApplication().FileMerge( myScenesToMerge, False, fbxLoadOptions )
@endcode

        pMultiLoadNamespaceList : The multi load namespace list to set. 
        """
        pass

    def SetObjectsToSave(self,pObjectsToSave):
        """
        Sets the list of objects that will be saved.
        This needs to be set before calling FBApplication::FileSave. The list is affecting only one save operation. Once the save is completed, the list is cleared.

        pObjectsToSave : The objects to save. 
        """
        pass

    def SetTakeDescription(self,pTakeIndex,pDescription):
        """
        Take Description.

        pTakeIndex : index of take to set. 
        pDescription : take description to set 
        """
        pass

    def SetTakeDestinationName(self,pTakeIndex,pDestinationName):
        """
        Take Destination Name upon save or load.

        pTakeIndex : index of take to set. 
        pDestinationName : take description to set 
        """
        pass

    def SetTakeKeyRange(self,pTakeIndex,pKeyTimeSpan):
        """
        Set take key range.

        pTakeIndex : index of take to set. 
        pKeyTimeSpan : Timespan indicating the time range to keep the keys. Keys that are outside the time range for this take will be removed, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity 
        """
        pass

    def SetTakeName(self,pTakeIndex,pName):
        """
        Take Original Name.

        pTakeIndex : index of take to set. 
        pName : take name to set 
        """
        pass

    def SetTakeSelect(self,pTakeIndex,pSelect):
        """
        Return if true if the take will be saved or Loaded.

        pTakeIndex : index of take to set 
        pSelect : set true if should be saved or loaded. 
        """
        pass

    ActorFaces=property(doc="<b>Read Write Property:</b> Handling of the Actor Faces elements.          ")
    ActorFacesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Actor Faces animation.          ")
    Actors=property(doc="<b>Read Write Property:</b> Handling of the Actors elements.          ")
    Audio=property(doc="<b>Read Write Property:</b> Handling of the Audio elements.          ")
    BaseCameras=property(doc="<b>Read Write Property:</b> Consider base camera settings.          ")
    Bones=property(doc="<b>Read Write Property:</b> Handling of the Bones elements.          ")
    BonesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Bones animation.          ")
    CacheSize=property(doc="<b>Read Write Property:</b> The Cached buffer size used to accelerate IO system.          ")
    CameraSwitcherSettings=property(doc="<b>Read Write Property:</b> Consider camera switcher settings.          ")
    Cameras=property(doc="<b>Read Write Property:</b> Handling of the Cameras elements.          ")
    CamerasAnimation=property(doc="<b>Read Write Property:</b> Handling of the Cameras animation.          ")
    CharacterExtensions=property(doc="<b>Read Write Property:</b> Handling of the Character Extensions.          ")
    CharacterFaces=property(doc="<b>Read Write Property:</b> Handling of the Character Faces elements.          ")
    CharacterFacesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Character Faces animation.          ")
    Characters=property(doc="<b>Read Write Property:</b> Handling of the Characters elements.          ")
    CharactersAnimation=property(doc="<b>Read Write Property:</b> Handling of the Characters animation.          ")
    ClearSelectionBeforeSave=property(doc="<b>Read Write Property:</b> Set to true if the current selected objects shouldn't saved when call FBApplication::SaveCharacterRigAndAnimation.          ")
    ConsiderMuteSolo=property(doc="<b>Read Write property:</b> Consider the mute/solo settings to identify identical layer when merging.          ")
    Constraints=property(doc="<b>Read Write Property:</b> Handling of the Constraints elements.          ")
    ConstraintsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Constraints animation.          ")
    CopyCharacterExtensions=property(doc="<b>Read Write Property:</b> pCopyMissingExtensions Set to true if the character extensions on the rig in the file should be copied to the target rig.          ")
    CurrentCameraSettings=property(doc="<b>Read Write Property:</b> Consider current camera settings.          ")
    Devices=property(doc="<b>Read Write Property:</b> Handling of the Devices elements.          ")
    DevicesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Devices animation.          ")
    EmbedMedia=property(doc="<b>Read Write Property:</b> Embed all media in the FBX file itself. When saving in ASCII mode it is not possible to embed media.          ")
    FileFormatAndVersion=property(doc="<b>Read Write Property:</b> File format and version chosen to save the scene.          ")
    FileReference=property(doc="<b>Read Write property:</b> Load/Save scene as FileReference.          ")
    FileReferenceEdit=property(doc="<b>Read Write Property:</b> Load/Save the edits made to referenced objects or not.          ")
    FileReferences=property(doc="<b>Read Write Property:</b> Handling of the FileReferences elements.          ")
    GlobalLightingSettings=property(doc="<b>Read Write Property:</b> Consider global Lighting settings.          ")
    Groups=property(doc="<b>Read Write Property:</b> Handling of the Groups elements.          ")
    IgnoreConflicts=property(doc="<b>Read Write Property:</b> Set to true to ignore conflicts between objects in character extensions and objects in the scene. Conflicting objects will be merged in the extension          ")
    KeepTransformHierarchy=property(doc="<b>Read Write Property:</b> Indicate whether we keep transform hierarchy when SaveSelectedModelsOnly is true. Default value is false to ensure consistent behavior with SaveSelected operation via file menu.          ")
    KeyingGroups=property(doc="<b>Read Write Property:</b> Handling of the Keying Groups elements.          ")
    Lights=property(doc="<b>Read Write Property:</b> Handling of the Lights elements.          ")
    LightsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Lights animation.          ")
    Materials=property(doc="<b>Read Write Property:</b> Handling of the Materials elements.          ")
    MaterialsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Materials animation.          ")
    Models=property(doc="<b>Read Write Property:</b> Handling of the Models elements.          ")
    ModelsAnimation=property(doc="<b>Read Write Property:</b> Handling of the Models animation.          ")
    NamespaceList=property(doc="<b>Read Write Property:</b> A list of namespaces separated by '~'. On Load, duplicate the loaded objects into each namespace in the list. If the SetMultiLoadNamespaceList method is also called, this property is ignored.          ")
    Notes=property(doc="<b>Read Write Property:</b> Handling of the Notes elements.          ")
    NotesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Notes animation.          ")
    OpticalData=property(doc="<b>Read Write Property:</b> Handling of the Optical Data elements.          ")
    PhysicalProperties=property(doc="<b>Read Write Property:</b> Handling of the Physical Properties elements.          ")
    PhysicalPropertiesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Physical Properties animation.          ")
    Poses=property(doc="<b>Read Write Property:</b> Handling of the Poses elements.          ")
    ProcessAnimationOnExtension=property(doc="<b>Read Write Property:</b> Set to true if animation on character extensions should also be transferred.          ")
    RemoveConstraintReference=property(doc="<b>Read Write Property:</b> Set to true if we should remove constraint reference.          ")
    RemoveEmptyLayer=property(doc="<b>Read Write property:</b> Remove empty animation layers that are in additive mode, without child or parent.          ")
    ReplaceControlSet=property(doc="<b>Read Write Property:</b> Set to true if the character extensions (and their children) should be saved when call FBApplication::SaveCharacterRigAndAnimation.          ")
    ResetDOF=property(doc="<b>Read Write Property:</b> Set to true if we should change the limits on the target rig.          ")
    ResetHierarchy=property(doc="<b>Read Write Property:</b> Set to true if we should reset the character hierarchy.          ")
    RetargetOnBaseLayer=property(doc="<b>Read Write Property:</b> If the transfer method is retarget, set this parameter to control where the retarget correction will be made (on base layer or on another layer).          ")
    SaveCharacter=property(doc="<b>Read Write Property:</b> Set to true if the character should be saved when call FBApplication::SaveCharacterRigAndAnimation.          ")
    SaveCharacterExtensions=property(doc="<b>Read Write Property:</b> Set to true if the character extensions (and their children) should be saved when call FBApplication::SaveCharacterRigAndAnimation.          ")
    SaveControlSet=property(doc="<b>Read Write Property:</b> Set to true if the rig (and its children) should be saved when call FBApplication::SaveCharacterRigAndAnimation.          ")
    SaveSelectedModelsOnly=property(doc="<b>Read Write Property:</b> Indicate that only the selected models will be saved.          ")
    Scripts=property(doc="<b>Read Write Property:</b> Handling of the Scripts elements.          ")
    SetPropertyStaticIfPossible=property(doc="<b>Read Write Property:</b> Set to false if want to keep properties' animated flag even when they are not really animated(no keyframe data) while retrieving/storing. See sample: SetPropertyStaticIfPossibleOption.py.         ")
    Sets=property(doc="<b>Read Write Property:</b> Handling of the Sets elements.          ")
    Shaders=property(doc="<b>Read Write Property:</b> Handling of the Shaders elements.          ")
    ShadersAnimation=property(doc="<b>Read Write Property:</b> Handling of the Shaders animation.          ")
    ShowFileDialog=property(doc="<b>Read Write Property:</b> Set to true if want to pop up dialog for FileName, Format, Embed, Compression, UseTakeName, OneTakePerFile.          ")
    ShowOptionsDialog=property(doc="<b>Read Write Property:</b> Set to true if want to pop up options dialog for detail settings.          ")
    Solvers=property(doc="<b>Read Write Property:</b> Handling of the Solvers elements.          ")
    SolversAnimation=property(doc="<b>Read Write Property:</b> Handling of the Solvers animation.          ")
    Story=property(doc="<b>Read Write Property:</b> Handling of the Story elements.          ")
    StoryAnimation=property(doc="<b>Read Write Property:</b> Handling of the Story animation (animatable properties on story objects).          ")
    TakeSpan=property(doc="<b>Read Write Property:</b> Indicate how the take start and end point should be set. By default it is read from the file.          ")
    Textures=property(doc="<b>Read Write Property:</b> Handling of the Textures elements.          ")
    TexturesAnimation=property(doc="<b>Read Write Property:</b> Handling of the Textures animation.          ")
    TransferMethod=property(doc="<b>Read Write Property:</b> How should the animation should be transfered on the target rig.          ")
    TransportSettings=property(doc="<b>Read Write Property:</b> Consider transport control settings.          ")
    UpdateRecentFiles=property(doc="<b>Read Write Property:</b> Set to true to update recent file list.          ")
    UseASCIIFormat=property(doc="<b>Read Write Property:</b> Indicate if the resulting FBX file will be in binary or ASCII mode.          ")
    Video=property(doc="<b>Read Write Property:</b> Handling of the Video elements.          ")
    pass

class FBFCurve (FBComponent):
    """
    FCurve class.     
    See samples: ClearKeysOnSelectedModels.py, FCurveEditor.py.     
    """
    def FBFCurve(self):
        """
        Constructor.

        """
        pass

    def CreateInterpolatorCurve(self,pCurveType):
        """
        Create and interpolator curve.

        pCurveType : Interpolator curve type to create. 
        """
        pass

    def EditBegin(self,pKeyCount):
        """
        Setup function to begin adding keys.

        pKeyCount : Key to begin adding at(default is -1). 
        """
        pass

    def EditClear(self):
        """
        Empty FCurve of all keys.

        """
        pass

    def EditEnd(self,pKeyCount):
        """
        End key adding sequence.

        pKeyCount : Key to finish adding at (default is -1). 
        """
        pass

    def Evaluate(self,pTime):
        """
        Evaluate FCurve at <b>pTime</b>.

        pTime : Time at which FCurve is to be evaluated. 
        return : Value of FCurve at <b>pTime</b>. 
        """
        pass

    def GetPostExtrapolationCount(self):
        """
        Get count for post extrapolation.

        """
        pass

    def GetPostExtrapolationMode(self):
        """
        Get modes for post extrapolation.

        """
        pass

    def GetPreExtrapolationCount(self):
        """
        Get count for pre extrapolation.

        """
        pass

    def GetPreExtrapolationMode(self):
        """
        Get modes for pre extrapolation.

        """
        pass

    def KeyAdd(self,pTime,pValue,pInterpolation,pTangentMode):
        """
        Add a key at the specified time.

        pTime : Time at which to insert the key. 
        pValue : Value of the key. 
        pInterpolation : Interpolation type of the inserted key, default value is Cubic interpolation. 
        pTangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth). 
        return : The position of the new key in the list of FCurve keys. 
        """
        pass

    def KeyDelete(self,pStartIndex,pStopIndex):
        """
        Delete keys within an index range.
        This function is much faster than multiple removes.

        pStartIndex : Index of first deleted key. 
        pStopIndex : Index of last deleted key. 
        return : True if the delete operation is successful, false otherwise (e.g. the FCurve is locked, the index range is invalid, etc.). 
        """
        pass

    def KeyDelete(self,pStart,pStop,pInclusive):
        """
        Delete keys within a time range.
        This function is much faster than multiple removes.

        pStart : Start of time range. 
        pStop : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        return : True if the delete operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.). 
        """
        pass

    def KeyGetInterpolation(self,pIndex):
        """
        Get the key interpolation type at the specified index.

        pIndex : Index of the key to query. 
        return : Type of interpolation. 
        """
        pass

    def KeyGetLeftBezierTangent(self,pIndex):
        """
        Get the key left bezier tangent value at the specified index.

        pIndex : Index of the key to query. 
        return : Left bezier tangent. 
        """
        pass

    def KeyGetLeftDerivative(self,pIndex):
        """
        Get the key left derivative value at the specified index.

        pIndex : Index of the key to query. 
        return : Left derivative value, in units/seconds. 
        """
        pass

    def KeyGetLeftTangentWeight(self,pIndex):
        """
        Get the key left tangent weight at the specified index.

        pIndex : Index of the key to query. 
        return : Left tangent weight. 
        """
        pass

    def KeyGetMarkedForManipulation(self,pIndex):
        """
        Get the key manipulation state.

        pIndex : Index of the key to query. 
        return : True if the key is being manipulated, false otherwise. 
        """
        pass

    def KeyGetRightBezierTangent(self,pIndex):
        """
        Get the key right bezier tangent value at the specified index.

        pIndex : Index of the key to query. 
        return : Right bezier tangent. 
        """
        pass

    def KeyGetRightDerivative(self,pIndex):
        """
        Get the key right derivative value at the specified index.

        pIndex : Index of the key to query. 
        return : Right derivative value, in units/seconds. 
        """
        pass

    def KeyGetRightTangentWeight(self,pIndex):
        """
        Get the key right tangent weight at the specified index.

        pIndex : Index of the key to query. 
        return : Right tangent weight. 
        """
        pass

    def KeyGetSelected(self,pIndex):
        """
        Get the key selected state.

        pIndex : Index of the key to query. 
        return : True if the key is selected, false otherwise. 
        """
        pass

    def KeyGetTCBBias(self,pIndex):
        """
        Get the key bias value at the specified index (TCB key).

        pIndex : Index of the key to query. 
        return : Bias value. 
        """
        pass

    def KeyGetTCBContinuity(self,pIndex):
        """
        Get the key continuity value at the specified index (TCB key).

        pIndex : Index of the key to query. 
        return : Continuity value. 
        """
        pass

    def KeyGetTCBTension(self,pIndex):
        """
        Get the key tension value at the specified index (TCB key).

        pIndex : Index of the key to query. 
        return : Tension value. 
        """
        pass

    def KeyGetTangentBreak(self,pIndex):
        """
        Get the key tangent's break status at the specified index.

        pIndex : Index of the key to query. 
        return : Tangent's break status. 
        """
        pass

    def KeyGetTangentClampMode(self,pIndex):
        """
        Get the key tangent's clamp method at the specified index.

        pIndex : Index of the key to query. 
        return : Tangent's clamp method. 
        """
        pass

    def KeyGetTangentConstantMode(self,pIndex):
        """
        Get the key tangent's constant mode at the specified index.

        pIndex : Index of the key to query. 
        return : Tangent's constant mode. 
        """
        pass

    def KeyGetTangentCustomIndex(self,pIndex):
        """
        Get the key tangent's custom index at the specified index.

        pIndex : Index of the key to query. 
        return : Tangent's custom index. 
        """
        pass

    def KeyGetTangentMode(self,pIndex):
        """
        Get the key tangent mode at the specified index.

        pIndex : Index of the key to query. 
        return : Tangent calculation method. 
        """
        pass

    def KeyGetTangentWeightMode(self,pIndex):
        """
        Get the tangent weight mode for a key.

        pIndex : Index of the key to query. 
        return : Current weight mode. 
        """
        pass

    def KeyGetTime(self,pIndex):
        """
        Get the key time value at the specified index.

        pIndex : Index of the key to query. 
        return : Time of key. 
        """
        pass

    def KeyGetValue(self,pIndex):
        """
        Get the key value at the specified index.

        pIndex : Index of the key to query. 
        return : Value of the key. 
        """
        pass

    def KeyInsert(self,pTime,pInterpolation,pTangentMode):
        """
        Insert a key without affecting the curve shape.

        pTime : Time at which the key is to be inserted. 
        pInterpolation : Interpolation type of the inserted key, default value is Cubic interpolation. 
        pTangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth). 
        """
        pass

    def KeyOffset(self,pOffsetTime,pStartIndex,pStopIndex):
        """
        Offset keys within an index range by a given offset time.
        When offsetting many keys at once, all non-moving keys that are situated in the target range are deleted automatically, to preserve the animation being offset.

        pOffsetTime : The offset time to apply on keys. 
        pStartIndex : Index of first key to be offset. 
        pStopIndex : Index of last key to be offset. 
        return : True if the offset operation is successful, false otherwise (e.g. the FCurve is locked, the index range is invalid, etc.). 
        """
        pass

    def KeyOffset(self,pOffsetTime,pStartTime,pStopTime,pInclusive):
        """
        Offset keys within a time range by a given offset time.
        Non-moving keys that are situated in the target range are deleted automatically, to preserve the animation being offset.

        pOffsetTime : The offset time to apply on keys. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        return : True if the offset operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.). 
        """
        pass

    def KeyReplaceBy(self,pSource,pStart,pStop,pUseExactGivenSpan,pKeyStartEndOnNoKey):
        """
        Replace keys within a range in current function curve with keys found in a source function curve.

        pSource : Source function curve. 
        pStart : Start of time range. 
        pStop : End of time range. 
        pUseExactGivenSpan : When false, the time of the first and last key in the range will be used. 
        pKeyStartEndOnNoKey : When true, inserts a key at the beginning and at the end of the range if there is no key to insert. 
        """
        pass

    def KeySetInterpolation(self,pIndex,pValue):
        """
        Set the key interpolation type at the specified index.

        pIndex : Index of the key to set. 
        pValue : Type of interpolation. 
        """
        pass

    def KeySetLeftBezierTangent(self,pIndex,pValue):
        """
        Set the key left bezier tangent value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Left bezier tangent. 
        """
        pass

    def KeySetLeftDerivative(self,pIndex,pValue):
        """
        Set the key left derivative value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Left derivative value, in units/seconds. 
        """
        pass

    def KeySetLeftTangentWeight(self,pIndex,pValue):
        """
        Set the key left tangent weight at the specified index.

        pIndex : Index of the key to set. 
        pValue : Left tangent weight. 
        """
        pass

    def KeySetMarkedForManipulation(self,pIndex,pValue):
        """
        Set the key manipulation state.

        pIndex : Index of the key to set. 
        pValue : New manipulation state. 
        return : True if the operation was successful, false otherwise. 
        """
        pass

    def KeySetRightBezierTangent(self,pIndex,pValue):
        """
        Set the key right bezier tangent value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Right bezier tangent. 
        """
        pass

    def KeySetRightDerivative(self,pIndex,pValue):
        """
        Set the key right derivative value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Right derivative value, in units/seconds. 
        """
        pass

    def KeySetRightTangentWeight(self,pIndex,pValue):
        """
        Set the key right tangent weight at the specified index.

        pIndex : Index of the key to set. 
        pValue : Right tangent weight. 
        """
        pass

    def KeySetSelected(self,pIndex,pValue):
        """
        Set the key selected state.

        pIndex : Index of the key to set. 
        pValue : New selection state. 
        return : True if the operation was successful, false otherwise. 
        """
        pass

    def KeySetTCBBias(self,pIndex,pValue):
        """
        Set the key bias value at the specified index (TCB key).

        pIndex : Index of the key to set. 
        pValue : Bias value. 
        """
        pass

    def KeySetTCBContinuity(self,pIndex,pValue):
        """
        Set the key continuity value at the specified index (TCB key).

        pIndex : Index of the key to set. 
        pValue : Continuity value. 
        """
        pass

    def KeySetTCBTension(self,pIndex,pValue):
        """
        Set the key tension value at the specified index (TCB key).

        pIndex : Index of the key to set. 
        pValue : Tension value. 
        """
        pass

    def KeySetTangentBreak(self,pIndex,pValue):
        """
        Set the key tangent's break status at the specified index.

        pIndex : Index of the key to set. 
        pValue : Tangent's break status. 
        """
        pass

    def KeySetTangentClampMode(self,pIndex,pValue):
        """
        Set the key tangent's clamp method at the specified index.

        pIndex : Index of the key to set. 
        pValue : Tangent's clamp method. 
        """
        pass

    def KeySetTangentConstantMode(self,pIndex,pValue):
        """
        Set the key tangent's constant mode at the specified index.

        pIndex : Index of the key to set. 
        pValue : Tangent's constant mode. 
        """
        pass

    def KeySetTangentCustomIndex(self,pIndex,pValue):
        """
        Set the key tangent's custom index at the specified index.

        pIndex : Index of the key to set. 
        pValue : Tangent's custom index. 
        """
        pass

    def KeySetTangentMode(self,pIndex,pValue):
        """
        Set the key tangent mode at the specified index.

        pIndex : Index of the key to set. 
        pValue : Tangent calculation method. 
        """
        pass

    def KeySetTangentWeightMode(self,pIndex,pValue):
        """
        Change the tangent weight for a key.
        Setting the value for LeftTangentWeight/RightTangentWeight will also activate the weight for that part. Please see the note provided with FBTangentWeightMode for the left weight of a key.

        pIndex : Index of the key to set. 
        pValue : Set the pValue according to the desired mode, kFBTangentWeightModeNone to disable it. 
        """
        pass

    def KeySetTime(self,pIndex,pValue):
        """
        Set the key time value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Time of key. 
        """
        pass

    def KeySetValue(self,pIndex,pValue):
        """
        Set the key value at the specified index.

        pIndex : Index of the key to set. 
        pValue : Value of the key. 
        """
        pass

    def SetPostExtrapolationCount(self,pCount):
        """
        Set count for post extrapolation.

        pCount : int
        """
        pass

    def SetPostExtrapolationMode(self,pExtrapolationMode):
        """
        Set modes for post extrapolation.

        pExtrapolationMode : FBExtrapolationMode
        """
        pass

    def SetPreExtrapolationCount(self,pCount):
        """
        Set count for pre extrapolation.

        pCount : int
        """
        pass

    def SetPreExtrapolationMode(self,pExtrapolationMode):
        """
        Set modes for pre extrapolation.

        pExtrapolationMode : FBExtrapolationMode
        """
        pass

    Keys=property(doc="<b>List:</b> Keys.          ")
    pass

class FBFCurveEditorUtility (FBComponent):
    """
    FBFCurveEditor Utility class Utility class allowing different operations on a FBFCurveEditor or on the main FCurveEditor.     
         
    """
    def Frame(self,pSelectedKeysOnly,pEditor):
        """
        Frame keys in the FCurve Editor interface.

        pSelectedKeysOnly : If true, only the selected keys will be framed, otherwise all keys will be framed. 
        pEditor : Pointer to a FBFCurveEditor for framing the keys in that custom editor, NULL to frame in the default editor. 
        return : True if successful, false otherwise. 
        """
        pass

    def GetObjects(self,pObjectList):
        """
        Get all the objects displayed in the left pane of the FCurve Editor.

        pObjectList : A list that will be filled with the objects displayed in the FCurve Editor. 
        return : True if successful, false otherwise. 
        """
        pass

    def GetProperties(self,pProperties,pSelectedOnly,pEditor):
        """
        Get the displayed properties.

        pProperties : Array that will contain the properties displayed. 
        pSelectedOnly : If true, only the selected properties will be returned. 
        pEditor : Pointer to a FBFCurveEditor for getting the properties in that custom editor, NULL to frame in the default editor. 
        return : True if successful, false otherwise. 
        """
        pass

    def GetTimeSpan(self,pEditor):
        """
        Get the displayed time range of the FCurve Editor.

        pEditor : Pointer to a FBFCurveEditor where the time span will be get, NULL to get the time span from the default editor. 
        return : FCurve Editor time span, default FBTimeSpan if not successful. 
        """
        pass

    def SetTimeSpan(self,pTimeSpan,pEditor):
        """
        Set the displayed time range of the FCurve Editor.

        pTimeSpan : The time span that will be set. 
        pEditor : Pointer to a FBFCurveEditor where the time span will be set, NULL to set the time span on the default editor. 
        return : True if successful, false otherwise. 
        """
        pass

    pass

class FBFCurveEventManager (FBComponent):
    """
    FCurve Event Manager Interface to the FBFCurveEventManager.     
     This class is used to track the changes on a FCurve of a property.      
    """
    def RegisterProperty(self,pProperty):
        """
        Register a property to the FCurve Event Manager.
        Properties that are registered will receive events with the OnFCurveEvent/OnPropertyEvent properties when their FCurves are modified.

        pProperty : The property to track. 
        return : True if the registration was successful, False otherwise. 
        """
        pass

    def UnregisterProperty(self,pProperty):
        """
        Unregister a property from the FCurve Event Manager.
        Those properties will not be tracked and no update will be sent with the OnFCurveEvent/OnPropertyEvent properties anymore.

        pProperty : The property to stop tracking. 
        return : True if the unregistration was successful, False otherwise. 
        """
        pass

    OnFCurveEvent=property(doc="<b>Event:</b> Called when a registered FCurve is modified.          ")
    OnPropertyEvent=property(doc="<b>Event:</b> Called when a registered property state is modified (detached, destroyed...).          ")
    pass

class FBFileMonitoringManager (FBComponent):
    """
    File Change Monitoring Interface to the file change monitoring.     
         
    """
    def AddFileToMonitor(self,pFilePath,pFileMonitoringType):
        """
        Add file to monitor.

        pFilePath : The file path to monitor. 
        pFileMonitoringType : The monitor type of this file. 
        """
        pass

    def CleanFileMonitoring(self,pIncludePythonEditorScripts):
        """
        Clean files and directories currently been monitored.

        pIncludePythonEditorScripts : True to also clean the monitoring of Python Editor script files loaded, false otherwise. 
        """
        pass

    def PauseFileMonitoring(self,pPause):
        """
        Pause file from monitoring, except for Python Editor script files loaded.

        pPause : True to pause the file monitoring, false to resume. 
        """
        pass

    def RemoveFileFromMonitor(self,pFilePath):
        """
        Remove file from monitoring.

        pFilePath : The file path to be removed. 
        """
        pass

    OnFileChangeAnimationClip=property(doc="<b>Event:</b> Animation clip file change event.          ")
    OnFileChangeFileReference=property(doc="<b>Event:</b> File Reference file change event.          ")
    OnFileChangeMainScene=property(doc="<b>Event:</b> Main scene file change event.          ")
    OnFileChangePythonEditorScript=property(doc="<b>Event:</b> Python Editor Script file change event.          ")
    pass

class FBFilter (FBComponent):
    """
    Filters are used to modify motion capture data.     
     Filters are objects which can be applied on a FCurve, or the animation node associated with an animated object property, to modify shape and number of keys. Filters can be created from the GUI, using the Filters tool, or programmatically with an instance of a FBFilterManager.The filter properties can be found in the object's PropertyList data member. They will use the same name, and be of the same type, as what can be seen in the GUI.Instances of FBFilter should be created with the help of the class FBFilterManager. Only internal application code should call the FBFilter's class constructor.Sample C++ code: 
@code
FBFilterManager lFilterManager;

// Create a filter instace.
FBFilter* lFilter = lFilterManager.CreateFilter( 'Key Reducing' );

if( lFilter )
{
    // Create a FCurve and populate it with keys.
    FBFCurve lCurve( 'Temp Curve' );
    for( int lIdx = 1; lIdx < 10; ++lIdx )
    {
        FBTime lTime( 0, 0, 0, lIdx * 5 );
        lCurve.KeyAdd( lTime, lIdx * 5 );
    }

    FBTrace( 'Keys before: %d\n', lCurve.Keys.GetCount() ); // Should be 9.

    // Apply the key reducing filter.
    lFilter->Apply( &lCurve );

    FBTrace( 'Keys after: %d\n', lCurve.Keys.GetCount() ); // Should be 2.
}
@endcode

Sample Python code: 
@code
from pyfbsdk import *

# Find a given model in the scene.
lModel = FBFindModelByLabelName( 'Cube' )

if lModel:
    # Create a Key Reducing filter.
    lFilter = FBFilterManager().CreateFilter( 'Key Reducing' )

    if lFilter:
        # Set the filter's precision to 2.0, and apply it to
        # the object's translation animation.
        lFilter.PropertyList.Find( 'Precision' ).Data = 2.0
        lFilter.Apply( lModel.Translation.GetAnimationNode(), True )
@endcode

     
    """
    def FBFilter(self):
        """
        Constructor.

        """
        pass

    def Apply(self,pCurve):
        """
        Apply the filter to an FCurve.
        This is one of the two apply method that is meant to be called by client code. The FCurve can be a standalone independant FCurve, or can be associated to an object's animated property.

        pCurve : FCurve to apply filter to. 
        return : <b>true</b> if successful. 
        """
        pass

    def Apply(self,pNode,pRecursive):
        """
        Apply the filter to an animation node.
        This is the other apply method and it can be used on an object's animation node.

        pNode : Node to apply filter to. 
        pRecursive : Recursively apply filter on child nodes? 
        return : <b>true</b> if successful. 
        """
        pass

    def Reset(self):
        """
        Reset properties.

        """
        pass

    Start=property(doc="<b>Read Write Property:</b> Start time of the filtering region          ")
    Stop=property(doc="<b>Read Write Property:</b> Stop time of the filtering region          ")
    pass

class FBFolder (FBComponent):
    """
    Folder class.     
     This class is an interface to manipulate folders in the scene. See sample: FBFolder.py.     
    """
    def FBFolder(self,pName,pComponent):
        """
        Constructor.

        pName : Name to assign to new folder. 
        pComponent : Object used to determine folder's category. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    Items=property(doc="<b>List:</b> List of components in the folder.          ")
    pass

class FBGenericMenu (FBComponent):
    """
    A GenericMenu class.     
     You can use this class either to create a new menu in the menu bar (or in a menuitem in the menu bar) or you can use this class to create a pop-up menu. 
@code
#to start a pop up menu use the Execute method
def mouseClick(x, y):
    item = menu.Execute(x, y)
    if item.Id == 10:
       [do this]
    else if item.Id == 100:
        [do that...]
@endcode

There are 4 ways to insert new item in a menu. Each method needs the name of the menuitem as well as it's unique id. You can also optionally sets a new menu for a specific item. 
@code
embeededMenu = FBGenericMenu()
menu.InsertLast('new new item', 67, embeddedMenu)

#A genericMenu contains a GenericMenuItem for each entry. You can iterate on the different menuitem
#using GetFirstITem/GetNextItem or if you already know the id of the item you can get it with GetItem.

item = menu.GetFirstItem()
while item:
    print item.Name
    item = menu.GetNextItem(item)
@endcode


@code
# This example shows how to list the Caption/Id of all the menu items of the Edit menu
menuManager = FBMenuManager() 
editMenu = menuManager.GetMenu( 'Edit' )
item = editMenu.GetFirstItem()
while item:
    print ''' + item.Caption + '' (id: ' + str( item.Id ) + ')'
    item = editMenu.GetNextItem( item )
@endcode

You can also delete a Menu item: this will remove the item from the menu as well as freeing its memory.To be notified when a menuitem is clicked, you can register using OnMenuActivate. This will send a FBEventMenu containing the name and the Id of the menu item that was clicked. See sample: FBMenu.py.     
    """
    def FBGenericMenu(self):
        """
        Default constructor.
        Used to create embedded menu (inside another menu item) or pop-up menu.

        """
        pass

    def DeleteItem(self,pToDelete):
        """
        Remove a menu item from the menu and delete it.

        pToDelete : The item to remove.  
        """
        pass

    def Execute(self,pX,pY,pRightAlign):
        """
        Starts the menu as a pop-up menu at a specific location on screen.
        It returns the item that was clicked by the user.

        pX : X location in pixel on screen where the menu is to be popped. 
        pY : Y location in pixel on screen where the menu is to be popped. 
        pRightAlign : All menu item will be align to the right justified (if true) or left justified (if false)  
        return : The selected item by the user. Null if the user clicks outside the menu. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetFirstItem(self):
        """
        Returns the first menu item (if existing) in this menu.
        You can then use GetNextItem to iterate on other menu items.

        return : The first menu item in this Menu. 
        """
        pass

    def GetItem(self,pItemId):
        """
        Returns the menu item corresponding to an id.

        pItemId : Id of the item we are looking for. 
        return : Will return the Item corresponding to an id (null if not found). 
        """
        pass

    def GetLastItem(self):
        """
        Returns the last menu item (if existing) in this menu.
        You can then use GetPrevItem to reverse iterate on other menu items.

        return : The last menu item in this Menu. 
        """
        pass

    def GetNextItem(self,pItem):
        """
        Returns the menu item following an other item.
        Returns null if this is the last item in menu.

        pItem : Will return the item after pItem 
        return : Will return the item after pItem. Null if pItem is the last item. 
        """
        pass

    def GetPrevItem(self,pItem):
        """
        Returns the menu item preceding an other item.
        Returns null if this is the first item in menu.

        pItem : Will return the item BEFORE pItem 
        return : Will return the item BEFORE pItem. Null if pItem is the first item. 
        """
        pass

    def InsertAfter(self,pBeforeItem,pItemName,pItemId,pMenu):
        """
        Inserts a new menu Item AFTER another item.

        pBeforeItem : The reference item. We will create a new item AFTER this one. 
        pItemName : Caption of the newly added item. 
        pItemId : Unique id of this menu item. 
        pMenu : Optional. If this Item leads to another menu (embedded) it can be specified here. 
        return : Will return the menu item created from this insertion. 
        """
        pass

    def InsertBefore(self,pAfterItem,pItemName,pItemId,pMenu):
        """
        Inserts a new menu Item BEFORE another item.

        pAfterItem : The reference item. We will create a new item BEFORE this one. 
        pItemName : Caption of the newly added item. 
        pItemId : Unique id of this menu item. 
        pMenu : Optional. If this Item leads to another menu (embedded) it can be specified here. 
        return : Will return the menu item created from this insertion. 
        """
        pass

    def InsertFirst(self,pItemName,pItemId,pMenu):
        """
        Inserts a new menu Item at the first position in the menu list.

        pItemName : Caption of the newly added item. 
        pItemId : Unique id of this menu item. 
        pMenu : Optional. If this Item leads to another menu (embedded) it can be specified here. 
        return : Will return the menu item created from this insertion. 
        """
        pass

    def InsertLast(self,pItemName,pItemId,pMenu):
        """
        Inserts a new menu Item at the last position in the menu list.

        pItemName : Caption of the newly added item. 
        pItemId : Unique id of this menu item. 
        pMenu : Optional. If this Item leads to another menu (embedded) it can be specified here. 
        return : Will return the menu item created from this insertion. 
        """
        pass

    OnMenuActivate=property(doc="<b>Event Property:</b> Register on this property to be notified when a menu item is clicked by the user.          ")
    pass

class FBGenericMenuItem (FBComponent):
    """
    FBGenericMenuItem This class stores data for a single menu item.     
     A single menu item can contains another menu (embedded menu) or not. A GenericMenuItem has an Id and a Name.You can use a GenericMenuItem to modify the attributes of a menu (it is the only way to change its name).You cannot create a FBGenericMenuItem directly. You must use the insertion method in FBMenu of FBMenuManager to obtain a handle on a FBGenericMenuItem. See sample: FBMenu.py.     
    """
    def FBGenericMenuItem(self):
        """
        """
        pass

    Caption=property(doc="<b>Read/Write Property:</b> Caption of the menu item.          ")
    Enable=property(doc="<b>Read/Write Property:</b> Enable or Disable (grey out) a menu Item.          ")
    Id=property(doc="<b>Read/Write Property:</b> Id of the menu item.          ")
    Menu=property(doc="<b>Read/Write Property:</b> If the menu item leads to another menu.          ")
    pass

class FBGeometry (FBComponent):
    """
    Geometry class.     
     This class groups all geometry related elements which are shared across the different subclasses (FBMesh, FBSurface, FBNurbs and FBPatch). Geometry Material always use kFBGeometryReference_INDEX mode. While Normal, UV could have different combination of mapping and reference modes.Geometries created with SDK can support FBGeometryMapping_ALL_SAME or kFBGeometryMapping_BY_POLYGON for material, and kFBGeometryMapping_BY_CONTROL_POINT for Normal, Tangent, Binormal, Color and UV. Only one set of UV could be supported.Geometries passed from FBXSDK pipeline could have various complex mapping/reference mode combination for material, normal and UV. And could potentially contains multiple set of UVs. See samples: ShapeCreation.py, VertexArrayManipulation.py.     
    """
    def GeometryBegin(self):
        """
        Begin geometry editing.

        return : <b>true</b> if successful. 
        """
        pass

    def GeometryEnd(self):
        """
        End geometry editing.

        return : <b>true</b> if successful. 
        """
        pass

    def GetBinormalsDirectArray(self,pOutArrayCount):
        """
        Get a pointer to the direct array of binormals.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to direct array of binormals, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetBinormalsIndexArray(self,pOutArrayCount):
        """
        Get a pointer to the index array of binormals.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of binormals, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetMaterialIndexArray(self,pOutArrayCount):
        """
        Get a pointer to the index array of Material.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of Material, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetNormalsDirectArray(self,pOutArrayCount):
        """
        Get a pointer to the direct array of normals.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to direct array of normals, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetNormalsIndexArray(self,pOutArrayCount):
        """
        Get a pointer to the index array of normals.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of normals, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetPositionsArray(self,pOutArrayCount):
        """
        Get a pointer to the position array.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of normals, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetTangentsDirectArray(self,pOutArrayCount):
        """
        Get a pointer to the direct array of tangents.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to direct array of tangents, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetTangentsIndexArray(self,pOutArrayCount):
        """
        Get a pointer to the index array of tangents.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of tangents, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetUVSetDirectArray(self,pOutArrayCount,pUVSetName):
        """
        Get a pointer to the direct array of UVset Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        pUVSetName : The name of UVset, NULL for the first UVset. 
        return : pointer to the array of UV, or NULL is the array hasn't been allocated yet. 
        """
        pass

    def GetUVSetIndexArray(self,pOutArrayCount,pUVSetName):
        """
        Get a pointer to the index array of UVset.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        pUVSetName : The name of UVset, NULL for the first UVset. 
        return : Pointer to index array of UVSet, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetUVSetMappingMode(self,pUVSetName):
        """
        Get UVSet mapping mode.

        pUVSetName : The name of UVset, NULL for the first UVset. 
        return : Mapping mode of the UVset. 
        """
        pass

    def GetUVSetReferenceMode(self,pUVSetName):
        """
        Get UVSet reference mode.

        pUVSetName : The name of UVset, NULL for the first UVset. 
        return : Reference mode of the UVset. 
        """
        pass

    def GetUVSets(self):
        """
        Get available UVSet name.

        return : StringList contain all the available UVSets' name. 
        """
        pass

    def GetVertexColorsDirectArray(self,pOutArrayCount):
        """
        Get a pointer to the direct array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to direct array of vertex colors, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def GetVertexColorsIndexArray(self,pOutArrayCount):
        """
        Get a pointer to the index array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.

        pOutArrayCount : To return the length the array. 
        return : Pointer to index array of vertex color, or NULL if the array hasn't been allocated yet. 
        """
        pass

    def ShapeAdd(self,pName):
        """
        Add new shape.

        pName : the shape name 
        return : the index of the new shape, -1 if the shape adding fail. 
        """
        pass

    def ShapeClearAll(self):
        """
        Clears all the shapes.

        """
        pass

    def ShapeGetCount(self):
        """
        Get Shape Count.

        """
        pass

    def ShapeGetDiffPoint(self,pShapeIdx,pDiffIndex,pOriIndex,pPosDiff):
        """
        Get the differentiate point.

        pShapeIdx : The index of the shape 
        pDiffIndex : The index of the diff point in this shape. 
        pOriIndex : The index of the diff point in the original geometry. 
        pPosDiff : The position differentiation. 
        """
        pass

    def ShapeGetDiffPoint(self,pShapeIdx,pDiffIndex,pOriIndex,pPosDiff,pNormalDiff):
        """
        Get the differentiate point.

        pShapeIdx : The index of the shape 
        pDiffIndex : The index of the diff point in this shape. 
        pOriIndex : The index of the diff point in the original geometry. 
        pPosDiff : The position differentiation. 
        pNormalDiff : The normal differentiation. 
        """
        pass

    def ShapeGetName(self,pShapeIdx):
        """
        Return the shape Name.

        pShapeIdx : int
        """
        pass

    def ShapeInit(self,pShapeIdx,pDiffSize,pWithNormal):
        """
        Init the shape.

        pShapeIdx : The index of the shape to be initialized 
        pDiffSize : Total number of different point (pos or normal) compared to base geometry. 
        pWithNormal : Currently normal won't be considered during shape blending. 
        """
        pass

    def ShapeSetDiffPoint(self,pShapeIdx,pDiffIndex,pOriIndex,pPosDiff):
        """
        Set the differentiate point.

        pShapeIdx : The index of the shape 
        pDiffIndex : The index of the diff point in this shape. 
        pOriIndex : The index of the diff point in the original geometry. 
        pPosDiff : The position differentiation. 
        """
        pass

    def ShapeSetDiffPoint(self,pShapeIdx,pDiffIndex,pOriIndex,pPosDiff,pNormalDiff):
        """
        Set the differentiate point.

        pShapeIdx : The index of the shape 
        pDiffIndex : The index of the diff point in this shape. 
        pOriIndex : The index of the diff point in the original geometry. 
        pPosDiff : The position differentiation. 
        pNormalDiff : The normal differentiation. 
        """
        pass

    def VertexAdd(self,pVertex):
        """
        Add a vertex.

        pVertex : Vertex values used to add vertex. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,pVertex,pNormal):
        """
        Add a vertex.

        pVertex : Vertex values used to add vertex. 
        pNormal : Normal values used to add vertex. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,pVertex,pNormal,pUV):
        """
        Add a vertex.

        pVertex : Vertex values used to add vertex. 
        pNormal : Normal values used to add vertex. 
        pUV : UV values used to add vertex. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,pVertex,pNormal,pUV,pVertexColor):
        """
        Add a vertex.

        pVertex : Vertex values used to add vertex. 
        pNormal : Normal values used to add vertex. 
        pUV : UV values used to add vertex. 
        pVertexColor : Color values used to add vertex. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,px,py,pz):
        """
        Add a vertex.

        px : X coordinate of vertex to add. 
        py : Y coordinate of vertex to add. 
        pz : Z coordinate of vertex to add. 
        return : Index where vertex was added. 
        """
        pass

    def VertexAdd(self,px,py,pz,nx,ny,nz):
        """
        Begin geometry editing.

        px : float
        py : float
        pz : float
        nx : float
        ny : float
        nz : float
        return : <b>true</b> if successful. 
        """
        pass

    def VertexAdd(self,px,py,pz,nx,ny,nz,UVu,UVv):
        """
        Begin geometry editing.

        px : float
        py : float
        pz : float
        nx : float
        ny : float
        nz : float
        UVu : float
        UVv : float
        return : <b>true</b> if successful. 
        """
        pass

    def VertexAdd(self,px,py,pz,nx,ny,nz,UVu,UVv,pRed,pGreen,pBlue,pAlpha):
        """
        Begin geometry editing.

        px : float
        py : float
        pz : float
        nx : float
        ny : float
        nz : float
        UVu : float
        UVv : float
        pRed : float
        pGreen : float
        pBlue : float
        pAlpha : float
        return : <b>true</b> if successful. 
        """
        pass

    def VertexArrayClear(self):
        """
        Clear all geometry vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).

        return : <b>true</b> if successful. 
        """
        pass

    def VertexArrayInit(self,pVertexcount,pUniqueMaterial,pFBGeometryArrayIDs):
        """
        Init geometry vertex arrays.
        Init position, normal and UV arrays (tangent, bi-normal and color on demand) with kFBGeometryMapping_BY_CONTROL_POINT / kFBGeometryReference_DIRECT mode. Will call VertexArrayClear() internally. User should then call GetXXXDirectyArray() to edit the vertex attributes directly.

        pVertexcount : number of control points (vertex) 
        pUniqueMaterial : User could specify per polygon mapping mode for mesh 
        pFBGeometryArrayIDs : Request to init other attribute arrays, bitwise combined value of FBGeometryArrayID enum items, currently support Tangent, Binormal and VertexColor. Only useful for mesh. 
        """
        pass

    def VertexClear(self):
        """
        Clear all Vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).

        return : <b>true</b> if successful. 
        """
        pass

    def VertexColorGet(self,pIndex):
        """
        Get a Vertex Color.

        pIndex : Index of Vertex to get Color for(default=-1). 
        return : Color of vertex at UVSetIndex. 
        """
        pass

    def VertexColorSet(self,pColor,pIndex):
        """
        Set a Vertex Color.

        pColor : Vertex Color to set. 
        pIndex : Index of Vertex to affect with pColor(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexColorSet(self,pRed,pGreen,pBlue,pAlpha,pIndex):
        """
        Set a UV coordinate.

        pRed : Red Color Channel to set, range [0, 1]. 
        pGreen : Green Color Channel to set, range [0, 1]. 
        pBlue : Blue Color Channel to set, range [0, 1]. 
        pAlpha : Alpha Color Channel to set, range [0, 1]. 
        pIndex : Index of Vertex to affect with Red, Green, Blue and Alpha (default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexCount(self):
        """
        Get the number of vertices in the geometry.

        return : Number of vertices in the geometry. 
        """
        pass

    def VertexGet(self,pIndex):
        """
        Get a vertex.

        pIndex : Index of vertex to get. 
        return : Vertex stored at pIndex. 
        """
        pass

    def VertexGetSelected(self,pIndex):
        """
        Get the selected state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is selected, false if not 
        """
        pass

    def VertexGetTransformable(self,pIndex):
        """
        Get the Transformable state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is Transformable, false if not 
        """
        pass

    def VertexGetVisible(self,pIndex):
        """
        Get the visible state of a vertex.

        pIndex : The index of the vertex 
        return : true if the vertex is visible, false if not 
        """
        pass

    def VertexInit(self,pSize,pResize,pInitUV,pInitVertexColor):
        """
        Resize or Reserve vertex, normal and UV array for performance.

        pSize : Number of vertices to resize or reserve. 
        pResize : <b>True</b>, for the geometry with known vertex count, we should resize the arrays to fixed size, and call VertexSet() afterwards; <b>False</b>, While for dynamic size geometry, we should only reserve the arrays with the estimated optimal size, then call VertexAdd() to dynamically increase the vertex count. 
        pInitUV : init Vertex UV array if true 
        pInitVertexColor : Init Vertex Color Array if true. 
        """
        pass

    def VertexNormalGet(self,pIndex):
        """
        Get a normal at a vertex.

        pIndex : Vertex to get normal at(default=-1). 
        return : Normal of vertex at pIndex. 
        """
        pass

    def VertexNormalSet(self,pVertex,pIndex):
        """
        Set a normal at a vertex.

        pVertex : Normal to set. 
        pIndex : Index of vertex to set Normal at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexNormalSet(self,px,py,pz,pIndex):
        """
        Set a normal at a vertex.

        px : X coordinate of normal. 
        py : Y coordinate of normal. 
        pz : Z coordinate of normal.  
        pIndex : Index of vertex to set Normal at(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSet(self,pVertex,pIndex):
        """
        Set a vertex.

        pVertex : Vertex values used to set vertex. 
        pIndex : Index of vertex to affect (default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSet(self,px,py,pz,pIndex):
        """
        Set a vertex.

        px : X coordinate to set. 
        py : Y coordinate to set. 
        pz : Z coordinate to set.  
        pIndex : Index of vertex to set(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexSetSelected(self,pIndex,pState):
        """
        Set the selected state of a vertex.

        pIndex : The index of the vertex 
        pState : The true to selected, false to deselect 
        return : true if the vertex is selected, false if not 
        """
        pass

    def VertexSetVisible(self,pIndex,pState):
        """
        Set the visible state of a vertex.

        pIndex : The index of the vertex 
        pState : true to be visible 
        return : true if the vertex is visible, false if not 
        """
        pass

    def VertexUVGet(self,pIndex):
        """
        Get a UV coordinate.

        pIndex : Index of Vertex to get UV coordinate for(default=-1). 
        return : UV coordinate of vertex at UVSetIndex. 
        """
        pass

    def VertexUVSet(self,pUV,pIndex):
        """
        Set a UV coordinate.

        pUV : UV coordinate to set. 
        pIndex : Index of Vertex to affect with UV coordinate(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def VertexUVSet(self,pU,pV,pIndex):
        """
        Set a UV coordinate.

        pU : U coordinate to set. 
        pV : V coordinate to set. 
        pIndex : Index of Vertex to affect with UV coordinate(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    BinormalMappingMode=property(doc="<b>Read Only Property:</b> Binormal mapping mode.          ")
    BinormalReferenceMode=property(doc="<b>Read Only Property:</b> Binormal reference mode.          ")
    MaterialMappingMode=property(doc="<b>Read Property:</b> Material mapping mode.          ")
    NormalMappingMode=property(doc="<b>Read Only Property:</b> Normal mapping mode.          ")
    NormalReferenceMode=property(doc="<b>Read Only Property:</b> Normal reference mode.          ")
    TangentMappingMode=property(doc="<b>Read Only Property:</b> Tangent mapping mode.          ")
    TangentReferenceMode=property(doc="<b>Read Only Property:</b> Tangent reference mode.          ")
    VertexColorMappingMode=property(doc="<b>Read Only Property:</b> Vertex Color mapping mode.          ")
    VertexColorReferenceMode=property(doc="<b>Read Only Property:</b> Vertex Color reference mode.          ")
    pass

class FBHUDManager (FBComponent):
    """
        
        
    """
    DefaultHUD=property(doc="<b>Read Write Property:</b> Specifies the HUD to be displayed on cameras that do not have HUD explicitly assigned.          ")
    pass

class FBImage (FBComponent):
    """
    Image class.     
     Utility class used to load and get manipulate image data from disk or memory. See sample: VideoMemory.py.     
    """
    def FBImage(self,pFileName):
        """
        Constructor.

        pFileName : Path to the image file. If pObject is not NULL, pFileName will be ignored. 
        """
        pass

    def Cleanup(self):
        """
        Cleanup image data, making it black.

        """
        pass

    def ConvertFormat(self,pNewFormat):
        """
        Convert the image data format to another format.

        pNewFormat : The new format to convert the image to. 
        return : Return true if the convert was successful. 
        """
        pass

    def ConvertSize(self,pWidth,pHeight):
        """
        Convert the image size.

        pWidth : New width of the image. 
        pHeight : New height of the image. 
        return : Return true if the convert was successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetBufferAddress(self):
        """
        Access image data buffer, allow modifications.

        return : Pointer to the image data, values ranging from 0 to 255. 
        """
        pass

    def Init(self,pFormat,pWidth,pHeight):
        """
        Init.

        pFormat : Image format used to initialize data buffer. 
        pWidth : Image width in pixels. 
        pHeight : Image height in pixels. 
        """
        pass

    def IsCompressedTif(self,pFileName):
        """
        Query TIF file about its compressed status.

        pFileName : Full TIF file path name of the file to query. 
        return : Return true if the TIF file image data is compressed. 
        """
        pass

    def VerticalFlip(self):
        """
        Flip the image vertically.

        """
        pass

    def WriteToTif(self,pFileName,pComments,pCompressed):
        """
        Write image data to a TIF file on disk.

        pFileName : Full TIF file path name of the file to write. 
        pComments : Comments appended to the TIF file. 
        pCompressed : If true, the image data in the file will be compressed. 
        return : Return true if the image was successfully written on disk. 
        """
        pass

    Depth=property(doc="<b>Read Write Property:</b> Color depth of the image.          ")
    Format=property(doc="<b>Read Write Property:</b> Image data format.          ")
    Height=property(doc="<b>Read Write Property:</b> Height of the image in pixels.          ")
    InterleaveType=property(doc="<b>Read Only Property:</b> Image interleave type. Only meaningful if image type is field.          ")
    InterpolationType=property(doc="<b>Read Only Property:</b> Image interpolation type.          ")
    Type=property(doc="<b>Read Only Property:</b> Image type, refering to either frame or field.          ")
    Width=property(doc="<b>Read Write Property:</b> Width of the image in pixels.          ")
    pass

class FBKeyControl (FBComponent):
    """
    Key control.     
     Interface to use the key controls tool. See sample: MirrorPoseOverTime.py.     
    """
    def FBKeyControl(self):
        """
        Constructor.

        """
        pass

    def MoveKeys(self,pTimeSpan,pPivot,pT,pR,pS,pTime,pModelList):
        """
        Move animation keys in space, with respect to a pivot object.
        Equivalent to using the 'Move Keys' button in the Key Controls panel. Only keys that are part of the current animation layer will get affected.

        pTimeSpan : The time span in which the animation keys will be modified 
        pPivot : The pivot object to use as a reference. The pivot needs to be part of pModelList (or the current keying group) otherwise the move keys operation will abort 
        pT : The global translation to apply to the pivot 
        pR : The global Euler rotation to apply to the pivot (deg) 
        pS : The global scaling factors to apply to the pivot 
        pTime : The time at which the transformation values are applied to the pivot object 
        pModelList : List of models for which the animation will be modified. Optional parameter. If not supplied, the models in the current keying group will be used 
        """
        pass

    AutoKey=property(doc="<b>Read Write Property:</b> Enable/Disable Auto Key feature (key when moving 3D objects).          ")
    NewKeyInterpolationType=property(doc="<b>Read Write Property:</b> Current key interpolation type that will be used for new keys.          ")
    pass

class FBKeyingGroup (FBComponent):
    """
    KeyingGroup class.     
     This class is an interface to manipulate which properties will be keyed when active. A derived class could control when the keying group should activate and what content it should have. For example, a derived class could activate based one that is selected in the scene.To create a custom keying group, use the appropriate FBKeyingGroupType flag. Then, if it is a local keying group, call AddObjectDependency() to add an object to the keying group. You can then add properties belonging to the new object with AddProperty().If you are creating an object type keying group, call SetObjectType() to specify what kind of object will be keyed by this keying group. Then, add a property from an object, the name of the property will be used by the keying group the find corresponding properties in selected object.If you create a global keying group, simply properties from an object with AddProperty(). The name of the property will be used by the keying group to find corresponding properties in the selected object.      
    """
    def FBKeyingGroup(self,pName,pType):
        """
        Constructor.

        pName : Group name. 
        pType : Keying group type. 
        """
        pass

    def AddObjectDependency(self,pObj):
        """
        AddObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).

        pObj : a Dependency of the keying group. 
        """
        pass

    def AddProperty(self,pProp):
        """
        Add property to be keyed when current keying group is active.

        pProp : Property to be added. 
        """
        pass

    def ClearAllItems(self):
        """
        ClearAllItems clear object dependency, properties and child keying group.

        """
        pass

    def DeselectAllAnimatableProperties(self):
        """
        FBDeselectAllAnimatableProperties, deselect all animatable properties in the scene.

        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def FindPropertyIndex(self,pProp):
        """
        FindPropertyIndex.

        pProp : must be in the list (return -1 if not). 
        return : the index of pProp in the keyinggroup property list. 
        """
        pass

    def GetCumulativeProperty(self,pIndex,pStopAtVisible):
        """
        GetCumulativeProperty Same as GetSubKeyingGroup but recursive in child keying group.

        pIndex : index in the content Object Dependency list 
        pStopAtVisible : consider all keying group and stop to the first visible keying group. 
        return : he number of ObjectDependency of the keying group. 
        """
        pass

    def GetCumulativePropertyCount(self,pStopAtVisible):
        """
        GetCumulativePropertyCount Same as GetSubKeyingGroupCount but recursive in child keying group.

        pStopAtVisible : consider all keying group and stop to the first visible keying group. 
        return : he number of ObjectDependency of the keying group. 
        """
        pass

    def GetParentKeyingGroup(self,pIndex):
        """
        GetParentKeyingGroup.

        pIndex : is the index of the parent list of the current keying group. 
        return : the parent keying group. 
        """
        pass

    def GetParentKeyingGroupCount(self):
        """
        GetParentKeyingGroupCount.

        return : the number of parent. 
        """
        pass

    def GetProperty(self,pIndex):
        """
        GetProperty from the keyinggroup list.

        pIndex : index of the desired property. 
        return : property coresponding to pIndex. 
        """
        pass

    def GetPropertyCount(self):
        """
        GetPropertyCount.

        return : the number of properties in the keying group. 
        """
        pass

    def GetSubKeyingGroup(self,pIndex):
        """
        GetSubKeyingGroup.

        pIndex : index of the desired keying group child. 
        return : the the child at the index. 
        """
        pass

    def GetSubKeyingGroupCount(self):
        """
        GetSubKeyingGroupCount.

        return : the number of child keying group. 
        """
        pass

    def GetSubObject(self,pIndex):
        """
        GetSubObject.

        pIndex : index in the content Object Dependency list 
        return : the desired object at pIndex. 
        """
        pass

    def GetSubObjectCount(self):
        """
        GetSubObjectCount.

        return : the number of ObjectDependency of the keying group. 
        """
        pass

    def IsObjectDependency(self,pObj):
        """
        IsObjectDependency determine if the pObj is a dependency.

        pObj : an object to test the Dependency. 
        return : true if it depend. 
        """
        pass

    def IsObjectDependencySelected(self):
        """
        IsObjectDependencySelected.

        return : return true as soon as a Property Owner or another Object Dependency is selected. 
        """
        pass

    def RemoveAllObjectDependency(self):
        """
        IsObjectDependencySelected empty the content list.

        """
        pass

    def RemoveAllProperties(self):
        """
        IsObjectDependencySelected empty the property list.

        """
        pass

    def RemoveAllSubKeyingGroup(self):
        """
        RemoveAllSubKeyingGroup empty the child keying group.

        """
        pass

    def RemoveObjectDependency(self,pObj):
        """
        RemoveObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).

        pObj : a Dependency of the keying group. 
        """
        pass

    def RemoveProperty(self,pProp):
        """
        RemoveProperty from the keyinggroup list.

        pProp : Property to be removed. 
        """
        pass

    def SetActive(self,pActive):
        """
        SetActive, activate the keying group, replacing the other keying group.

        pActive : bool
        """
        pass

    def SetActiveAppend(self,pActive):
        """
        SetActiveAppend, activate and append the keying group to the other keying groups.

        pActive : bool
        """
        pass

    def SetEnabled(self,pEnable):
        """
        SetEnabled, makes the keying group available in keying group list of the key control UI.

        pEnable : bool
        """
        pass

    def SetObjectType(self,pObject):
        """
        Set the object type filter for and object type keying group.

        pObject : Object that will be used to set the keying group object type. Use NULL to remove the filter. 
        """
        pass

    pass

class FBManipulator (FBComponent):
    """
    Manipulator class.     
         
    """
    def FBManipulator(self,pName):
        """
        Constructor.

        pName : Name of manipulator. 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Is manipulator active?          ")
    AlwaysActive=property(doc="<b>Read Write Property:</b> Is manipulator always active?          ")
    ConsumeEvent=property(doc="<b>Read Write Property:</b> Is manipulator consuming event? If true, this will prevent other manipulators from being called.          ")
    DefaultBehavior=property(doc="<b>Read Write Property:</b> Using default manipulator behavior?          ")
    ViewerText=property(doc="<b>Read Write Property:</b> Text displayed in view.          ")
    Visible=property(doc="<b>Read Write Property:</b> Is manipulator visible?          ")
    pass

class FBMarkerSet (FBComponent):
    """
    Marker set class.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBMarkerSet(self,pName):
        """
        Constructor.

        pName : Name of new marker set. 
        """
        pass

    def AddMarker(self,pNodeId,pModel,pIsOriented):
        """
        Add a marker to the marker set.

        pNodeId : Id of Actor skeleton node. For hand, use the "C" index (ex:kFBSkeletonLeftThumbCIndex, kFBSkeletonLeftMiddleCIndex...) 
        pModel : The model to be associated with the marker (Optional). 
        pIsOriented : Set marker to be oriented or not (Optional). 
        return : Index of the new marker. 
        """
        pass

    def BeginTransaction(self):
        """
        Specify that you are about to call a group of functions.

        """
        pass

    def EndTransaction(self):
        """
        Specify that you are done calling a group of functions.

        """
        pass

    def GetLinkToModelOk(self):
        """
        Get the marker set association correctness.

        return : True if all used markers are link with models. 
        """
        pass

    def GetMarkerCount(self,pNodeId):
        """
        Get the number of marker in the set.

        pNodeId : If specified, obtain the number of marker for the specific node. 
        return : Total number of marker. 
        """
        pass

    def GetMarkerModel(self,pNodeId,pMarkerIndex):
        """
        Get the model associated with a marker.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker. 
        return : The model associated with the marker. 
        """
        pass

    def GetMarkerName(self,pNodeId,pMarkerIndex):
        """
        Get the name of marker at index <b>pMarkerIndex</b>.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        return : Name of marker at index <b>pMarkerIndex</b>. 
        """
        pass

    def GetMarkerOriented(self,pNodeId,pMarkerIndex):
        """
        Is marker orientated ?

        pNodeId : Id of Actor body node. 
        pMarkerIndex : Index of marker to access. 
        return : <b>True</b> if marker is oriented, <b>false</b> otherwise. 
        """
        pass

    def GetMarkerROffset(self,pNodeId,pMarkerIndex,pROffset):
        """
        Get/Set a marker rotation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pROffset : Current or new value of the marker rotation. 
        """
        pass

    def GetMarkerSetVisibility(self):
        """
        Get the marker set visibility.

        return : 1 if all markers are visible, 2 if some are visible, 0 if none are visible.  
        """
        pass

    def GetMarkerTOffset(self,pNodeId,pMarkerIndex,pTOffset):
        """
        Get/Set a marker translation.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pTOffset : Current or new value of the marker translation. 
        """
        pass

    def GetMarkerUsed(self,pNodeId,pMarkerIndex):
        """
        Is marker used ?

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        return : <b>True</b> if marker is used, <b>false</b> otherwise. 
        """
        pass

    def GetReferenceModel(self):
        """
        Get the reference model associated with this marker set.

        return : The reference model associated with the marker set. 
        """
        pass

    def GetUsedMarkerCount(self,pNodeId):
        """
        Get the number of used marker in the set.

        pNodeId : If specified, obtain the number of used marker for the specific node. 
        return : Total number of used marker. 
        """
        pass

    def SetMarkerModel(self,pNodeId,pMarkerIndex,pModel):
        """
        Associate a model to a marker.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker. 
        pModel : Model to be associated to the marker. 
        """
        pass

    def SetMarkerName(self,pNodeId,pMarkerIndex,pMarkerName):
        """
        Set the name of marker at index <b>pMarkerIndex</b>.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pMarkerName : New name to give to the marker. 
        """
        pass

    def SetMarkerOriented(self,pNodeId,pMarkerIndex,pIsOriented):
        """
        Set marker to be oriented or not.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pIsOriented : Oriented or not. 
        """
        pass

    def SetMarkerROffset(self,pNodeId,pMarkerIndex,pROffset):
        """
        pNodeId : FBSkeletonNodeId
        pMarkerIndex : int
        pROffset : FBRVector
        """
        pass

    def SetMarkerSetVisibility(self,pVisibility):
        """
        Set the marker set visibility.

        pVisibility : True will make to markers visible, false will hide them.  
        """
        pass

    def SetMarkerTOffset(self,pNodeId,pMarkerIndex,pTOffset):
        """
        pNodeId : FBSkeletonNodeId
        pMarkerIndex : int
        pTOffset : FBTVector
        """
        pass

    def SetMarkerUsed(self,pNodeId,pMarkerIndex,pUsed):
        """
        Set marker to be used or not.

        pNodeId : Id of Actor skeleton node. 
        pMarkerIndex : Index of marker to access. 
        pUsed : Used or not. 
        """
        pass

    def SetMultipleMarkerModels(self,pModelList):
        """
        Associate multiple models to markers, matching them by name.

        pModelList : A list of models to be matched with marker names. 
        return : True if at least one marker was matched. 
        """
        pass

    def SetReferenceModel(self,pReferenceModel):
        """
        Associate a model to a marker.

        pReferenceModel : Model to be associated to the marker. 
        """
        pass

    pass

class FBMemo (FBEdit):
    """
    Multi-line text input.     
    See samples: Memo.py, TutorialBox.py, TutorialGrid.py.     
    """
    def FBMemo(self):
        """
        Constructor.

        """
        pass

    def GetStrings(self,pLines):
        """
        Get the content of the memo.

        pLines : Content of the memo will be copied to it. 
        """
        pass

    def SetStrings(self,pLines):
        """
        Set the content of the memo.

        pLines : Content of the memo from will be set to it. 
        """
        pass

    pass

class FBMenuManager (FBComponent):
    """
    The menu manager allows access to MotionBuilder menu bar.     
     It can be used to retrieve the item corresponding to a menu path in the menu bar. A menu path is similar to a file path but it specifies the location of menu item in a hierarchy of menu. ex: to retrieve the item corresponding to MoBu Save item: item = menuMgr.GetMenu('File/Save')Other menu items in MoBu menu bar include the following: 'File', 'Edit','Animation','Window','Settings', 'Layout','Help'The menu manager can be used to insert new menu item in the menubar. You have to specify the menu path at which to insert the menu (to insert a new root menu, use NULL or None as the menu path) 
@code
#Insert a new Root Menu before the Help menu
menuMgr.InsertBefore(None, 'Help', 'before menu')

#Insert a new Root Menu after the Help menu
menuMgr.InsertAfter(None, 'Help', 'After menu')
@endcode

As a convenience operation, you can from the menu manager enable and disable menu item (instead of retrieving their corresponding item). See sample: FBMenu.py.     
    """
    def FBMenuManager(self):
        """
        Constructor.
        There is only one MenuManager in MotionBuilder, creating multiple FBMenuManager always return the same handle to the same global menu manager.

        """
        pass

    def ExecuteMenuItem(self,pMenuPath,pMenuItemID):
        """
        Execute a particular menu item.
        The menu path specifies the menu containing the menu item to execute. The ID specifies which menu item to execute in the menu.

        pMenuPath : Path containing the menu item to execute. 
        pMenuItemID : Unique ID of the menu item to execute. 
        return : True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator. 
        """
        pass

    def ExecuteMenuItemFromFullPath(self,pMenuItemFullPath):
        """
        Execute a particular menu item.
        The menu path specifies the menu item (NOT menu) to execute. Don't forget that most menu path already in MotionBuilder have a '&' as the first letter of their name. You have to use the '/' character as a separator in the specified menu path (ex: 'Settings/&Preferences...'), and exactly what is written in the menu item (ex: 'Edit/D&eselect\tShift+D'). 
@code
# This example shows how to display the About Box, as if the user opened it via the main menu Help > About MotionBuilder:
menuManager = FBMenuManager()
aboutBoxFullPath = 'Help/&About MotionBuilder'
menuManager.ExecuteMenuItemFromFullPath( aboutBoxFullPath )
@endcode

        pMenuItemFullPath : Path of the menu item to execute. 
        return : True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator. 
        """
        pass

    def GetMenu(self,pPath):
        """
        Get the Menu (NOT menu item) corresponding to a menu path.
        Don't forget that most menu path already in MotionBuilder have a '&' character as the first letter of their name. You have to use the '/' character as a separator in the specified menu path (ex: 'Help/&Communities').

        pPath : Path of the menu to retrieve 
        return : the FBGenericMenu at this path./ 
        """
        pass

    def InsertAfter(self,pMenuPath,pBeforeMenuName,pMenuName):
        """
        Insert a new menu at a specific path AFTER another item.

        pMenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu. 
        pBeforeMenuName : Name of the menu item AFTER which we will insert the new item. 
        pMenuName : str
        return : Returns the menu item corresponding to the newly inserted menu. 
        """
        pass

    def InsertBefore(self,pMenuPath,pAfterMenuName,pMenuName):
        """
        Insert a new menu at a specific path BEFORE another item.

        pMenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu. 
        pAfterMenuName : Name of the menu item BEFORE which we will insert the new item. 
        pMenuName : str
        return : Returns the menu item corresponding to the newly inserted menu. 
        """
        pass

    def InsertFirst(self,pMenuPath,pMenuName):
        """
        Insert a new menu at the first position of a specific path.

        pMenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu. 
        pMenuName : Name (Caption) of the newly inserted menu. 
        return : Returns the menu item corresponding to the newly inserted menu. 
        """
        pass

    def InsertLast(self,pMenuPath,pMenuName):
        """
        Insert a new menu at the last position of a specific path.

        pMenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu. 
        pMenuName : Name (Caption) of the newly inserted menu. 
        return : Returns the menu item corresponding to the newly inserted menu. 
        """
        pass

    def IsItemEnable(self,pMenuPath,pItemId):
        """
        Check if a particular item is enabled or disabled.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.

        pMenuPath : Path where to find the menu to check 
        pItemId : Id of the item to check.  
        return : Is the item enable or not. 
        """
        pass

    def SetItemEnable(self,pMenuPath,pItemId,pEnable):
        """
        Enable or disable a specific menu item.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.

        pMenuPath : Path where to find the menu to enable/disable 
        pItemId : Id of the item in the menu to disable.  
        pEnable : Enable (true) or disable (false) a menu item. 
        """
        pass

    pass

class FBModelOpticalAdvanced (FBComponent):
    """
    Advanced optical model information.     
         
    """
    def FBModelOpticalAdvanced(self,pOptical):
        """
        Constructor.

        pOptical : Optical model. 
        """
        pass

    def AcceptAllSegments(self):
        """
        Accept all segments.

        """
        pass

    def AcceptSegment(self):
        """
        Accept current segment.

        """
        pass

    def AutomaticBuild(self):
        """
        Automatic build.

        """
        pass

    def CropSegmentsAnimation(self):
        """
        Crop segment animation.

        """
        pass

    def SkipSegment(self):
        """
        Skip segment.

        """
        pass

    Active=property(doc="<b>Property:</b> Optical engine for model active?          ")
    AutoPlayToNextSegment=property(doc="<b>Property:</b> Automatic play to next segment ?          ")
    ControllerMode=property(doc="<b>Property:</b> Controller mode.          ")
    GenerationMode=property(doc="<b>Property:</b> Optical genration mode.          ")
    InsertSegmentMode=property(doc="<b>Property:</b> Insert segment mode.          ")
    MaxMatchDistance=property(doc="<b>Property:</b> Max matching distance.          ")
    PlayToNextSegment=property(doc="<b>Property:</b> Play to next segment ?          ")
    Quality=property(doc="<b>Property:</b> Rigid body quality.          ")
    SegmentMode=property(doc="<b>Property:</b> Segment mode.          ")
    ShowRigidQuality=property(doc="<b>Property:</b> Show the rigid quality?          ")
    UsedTake=property(doc="<b>Property:</b> Take used by optical model.          ")
    pass

class FBModelTemplate (FBComponent):
    """
    Model template class.     
     Model templates are 'placeholders' for animation input from devices. These generic 'models' can be any type of element, and permit the abstraction of the input from the actual type of model. In order to animate a model, one should bind the model to an animation node.      
    """
    def FBModelTemplate(self):
        """
        Constructor from parent object.

        """
        pass

    def FBModelTemplate(self,pPrefix,pName,pStyle):
        """
        Constructor (no parent) from prefix, name, and style.

        pPrefix : Location of model template in application object directory structure. 
        pName : Name of model template. 
        pStyle : Style of model template. 
        """
        pass

    Bindings=property(doc="<b>List:</b> Bindings for animation interface.          ")
    Children=property(doc="<b>List:</b> Children for object hierarchy.          ")
    DefaultRotation=property(doc="<b>Read Write Property:</b> Default rotation.          ")
    DefaultScaling=property(doc="<b>Read Write Property:</b> Default scaling.          ")
    DefaultTranslation=property(doc="<b>Read Write Property:</b> Default translation.          ")
    Model=property(doc="<b>Read Write Property:</b> Model being interfaced.          ")
    Prefix=property(doc="<b>Read Write Property:</b> Prefix of model template.          ")
    pass

class FBModelVertexData (FBComponent):
    """
        
        
    """
    def DisableOGLUVSet(self):
        """
        Disable OpenGL UV set array.

        """
        pass

    def DisableOGLVertexData(self):
        """
        Disable OpenGL Vertex Array (Pos & Normal).

        """
        pass

    def DrawSubPatch(self,pSubPatchIndex,pWireFrame):
        """
        Draw the specified sub patch.
        Must be called between Enable/DisableOGLVertexData function calls.

        pSubPatchIndex : Index of the sub patch to be drawn. 
        pWireFrame : Draw wire frame if true. 
        """
        pass

    def DrawSubRegion(self,pSubRegionIndex,pWireFrame):
        """
        Draw the specified sub region.
        Must be called between Enable/DisableOGLVertexData function calls.

        pSubRegionIndex : Index of the sub region to be drawn. 
        pWireFrame : Draw wire frame if true. 
        """
        pass

    def EnableOGLUVSet(self,pTextureMapping,pUVSet):
        """
        Enable (Setup) OpenGL UV set array.

        pTextureMapping : Texture Mapping Mode. 
        pUVSet : UV Set name if pTextureMapping is kFBTextureMappingUV, otherwise ignored. 
        """
        pass

    def EnableOGLVertexData(self,pAfterDeform):
        """
        Enable (Setup) OpenGL Vertex Array (Pos & Normal).

        pAfterDeform : Unused parameter. 
        """
        pass

    def GetIndexArray(self):
        """
        Return the index array.
        For the size of the array, see GetIndexArraySize().

        return : (C++) The index array pointer. (Python) The index array as a list. 
        """
        pass

    def GetIndexArraySize(self):
        """
        Return the index array size (see GetIndexArray()).
        It will sum the index size of each sub patch (see GetSubPatchIndexSize()).

        return : The index array size. 
        """
        pass

    def GetIndexArrayVBOId(self):
        """
        Return the index array VBO Id.

        return : The index array VBO Id. 
        """
        pass

    def GetSubPatchCount(self):
        """
        Return the number of sub patches.

        return : The number of sub patches. 
        """
        pass

    def GetSubPatchIndexOffset(self,pSubPatchIndex):
        """
        Return the start offset of the indexes for the specified sub patch (see GetIndexArray()).

        pSubPatchIndex : Index of the sub patch to be queried. 
        return : The start offset of the indexes for the specified sub patch, -1 if the specific sub path index is invalid. 
        """
        pass

    def GetSubPatchIndexSize(self,pSubPatchIndex):
        """
        Return the size of the indexes for the specified sub patch (see GetIndexArray()).

        pSubPatchIndex : Index of the sub patch to be queried. 
        return : The size of the indexes for the specified sub patch, -1 if the specific sub path index is invalid. 
        """
        pass

    def GetSubPatchMaterial(self,pSubPatchIndex):
        """
        Return the mapped material for the specified sub patch.

        pSubPatchIndex : Index of the sub patch to be queried. 
        return : The mapped material for the specified sub patch, the default material if the specific sub path index is invalid. 
        """
        pass

    def GetSubPatchMaterialId(self,pSubPatchIndex):
        """
        Return the mapped material ID for the specified sub patch.

        pSubPatchIndex : Index of the sub patch to be queried. 
        return : The mapped material ID for the specified sub patch, -1 if the specific sub path index is invalid. 
        """
        pass

    def GetSubPatchPrimitiveType(self,pSubPatchIndex,pIsOptimized):
        """
        Return the primitive type for the specified sub patch.
        Most of the time, kFBGeometry_TRIANGLES will be returned.

        pSubPatchIndex : Index of the sub patch to be queried. 
        pIsOptimized : (C++ only) Out parameter, return true if the specified sub patch is optimized for fast rendering, custom shader & render should use the optimized sub patch only. 
        return : (C++) The primitive type of the queried sub patch. (Python) A tuple with 2 values: (the primitive type of the queried sub patch, the value of pIsOptimized). 
        """
        pass

    def GetSubRegionCount(self):
        """
        Return the number of sub regions (mapping with different materials).

        return : The number of sub regions. 
        """
        pass

    def GetSubRegionMaterial(self,pSubRegionIndex):
        """
        Return the specified sub region's material.

        pSubRegionIndex : Index of the sub region to be queried. 
        return : The sub region's material, the default material if the specific sub region index is invalid. 
        """
        pass

    def GetUVSetArray(self,pTextureMapping,pUVSet):
        """
        Return the UV Set array for the specified texture mapping mode.

        pTextureMapping : Texture mapping mode to be queried. 
        pUVSet : UV Set name to be queried if pTextureMapping is kFBTextureMappingUV, otherwise ignored. 
        return : (C++) The UV Set array pointer. (Python) The UV Set array as a list. 
@code
// The following C++ snippet show how to deal with the UV mapping UV Set array pointer returned.
void* lUVSetArray = lModelVertexData.GetUVSetArray();
if( lUVSetArray )
{
    int lUVArrayCount = lModelVertexData->GetUVSetUVCount();
    
    FBGeometryArrayElementType lArrayType = lModelVertexData->GetUVSetArrayFormat( kFBTextureMappingUV );
    if( lArrayType == kFBGeometryArrayElementType_Float2 )
    {
        FBUV* lUVArray = (FBUV*)lUVSetArray;
        
        for( int i = 0; i < lUVArrayCount; i++ )
        {
            // Do something useful here
            FBTrace( "%f, %f\n", lUVArray[ i ][ 0 ], lUVArray[ i ][ 1 ] );
        }
    }
}
@endcode

 
        """
        pass

    def GetUVSetArrayFormat(self,pTextureMapping,pUVSet):
        """
        Return the UV Set array format.

        pTextureMapping : Unused parameter. 
        pUVSet : Unused parameter. 
        return : The UV Set array format. 
        """
        pass

    def GetUVSetUVCount(self,pTextureMapping,pUVSet):
        """
        Return the number of UVs in the UV Set for the specified texture mapping mode.

        pTextureMapping : Texture mapping mode to be queried. 
        pUVSet : UV Set name to be queried if pTextureMapping is kFBTextureMappingUV, otherwise ignored. 
        return : The number of UVs in the UV Set for the specified texture mapping mode. 
        """
        pass

    def GetUVSetVBOId(self,pTextureMapping,pUVSet):
        """
        Return the UV Set Buffer Object (VBO) Id for the specified texture mapping mode.

        pTextureMapping : Texture mapping mode to be queried. 
        pUVSet : UV Set name to be queried if pTextureMapping is kFBTextureMappingUV, otherwise ignored. 
        return : The UV Set VBO Id. 
        """
        pass

    def GetUVSetVBOOffset(self,pTextureMapping,pUVSet):
        """
        Return the UV Set Buffer Object (VBO) offset for the specified texture mapping mode.

        pTextureMapping : Texture mapping mode to be queried. 
        pUVSet : UV Set name to be queried if pTextureMapping is kFBTextureMappingUV, otherwise ignored. 
        return : The UV Set VBO offset (C++: as a pointer, Python: as a kReference). 
        """
        pass

    def GetVertexArray(self,pArrayId,pAfterDeform):
        """
        Return the vertex array for the specified vertex array Id.

        pArrayId : Vertex array Id type to be queried. 
        pAfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array. 
        return : (C++) The vertex array pointer. (Python) The vertex array as a list. Deformed position & normal vertex arrays could be NULL if one has not requested the mapping vertex array on CPU. 
        """
        pass

    def GetVertexArrayDuplicationMap(self,pDuplicatedVertexCount):
        """
        The FBModel::TessellatedMesh could contain per-face mapping UVSet/Normal or other layer elements.
        In order to build a valid VBO buffer for accelerated rendering, those control points with multiple attribute data must be duplicated. This function returns the duplicated vertices' ID mapping from FBModel::ModelVertexData vertex array to its FBModel::TessellatedMesh vertex array. Note those duplicated vertices are always appended after the original vertex array.

        pDuplicatedVertexCount : only) pDuplicatedVertexCount Out parameter, return the count of those duplicated vertices. 
        return : (C++) A pointer to the original vertex ID mapping for those duplicated vertices. (Python) A list containing the vertex ID mapping for those duplicated vertices. 
        """
        pass

    def GetVertexArrayType(self,pArrayId,pAfterDeform):
        """
        Return the vertex array format for the specified array Id.

        pArrayId : Vertex array Id type to be queried. 
        pAfterDeform : Unused parameter. 
        return : The vertex array format for the specified array Id. 
        """
        pass

    def GetVertexArrayVBOId(self,pArrayId,pAfterDeform):
        """
        Return the Vertex Buffer Object (VBO) Id for the specified vertex array Id.

        pArrayId : Vertex array Id type to be queried. 
        pAfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array. 
        return : The vertex array VBO Id. Deformed position & normal vertex VBO Id could be 0 if model use CPU skinning. 
        """
        pass

    def GetVertexArrayVBOOffset(self,pArrayId,pAfterDeform):
        """
        Return the Vertex Buffer Object (VBO) offset for the specified vertex array Id.

        pArrayId : Vertex array Id type to be queried. Only position or normal vertex array Id types are available. 
        pAfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array. 
        return : The vertex array VBO offset (C++: as a pointer, Python: as a kReference). 
        """
        pass

    def GetVertexCount(self):
        """
        Return the number of vertices.

        return : The number of vertices. 
        """
        pass

    def IsDeformable(self):
        """
        Return true if the model is deformable.

        return : True if the model is deformable, false otherwise. 
        """
        pass

    def IsDrawable(self):
        """
        Queries if this model should be drawn, e.g., in custom render callback.
        Returns false if e.g., deformed vertex data has not been computed for this frame (thus not ready to be drawn), or if model should be hidden when Z-Depth selection tool is active.

        return : True if the model should be drawn, false otherwise. 
        """
        pass

    def PopZDepthClipOverride(self):
        """
        Re-enables Z-Depth clip plane if it had been disabled via PushZDepthClipOverride().
        Call this function after drawing each model in custom render callback, so that Z-Depth clip plane is re-enabled if it was earlier disabled via PushZDepthClipOverride().

        """
        pass

    def PushZDepthClipOverride(self):
        """
        Disables Z-Depth clip plane if this model is selected using Z-Depth HideFront selection tool.
        Call this function before drawing each model in custom render callback, so that the selected model is unaffected by the Z-Depth clip plane, and hence is visible when Z-Depth HideFront selection tool is active. Be sure to call PopZDepthClipOverride() after drawing each model.

        """
        pass

    def VertexArrayMappingRelease(self):
        """
        Release deformed vertex array mapping on CPU.
        Call this function if plug-in don't need CPU access of the deformed vertex array to be mapped on CPU memory anymore, hence allow the application flexibility to choose higher performance approach.

        """
        pass

    def VertexArrayMappingRequest(self):
        """
        Request deformed vertex array mapping on CPU.
        Model's deformation computation could be executed on GPU, and thus the deformed vertex data will reside in GPU memory only by default. Calling this function VertexArrayMappingRequest() will ensure the deformed vertex array to be always mapped to CPU memory.

        """
        pass

    pass

class FBMotionClip (FBComponent):
    """
    Motion class.     
     Properties of this class are work in progress, but you can still list them and get their names.      
    """
    def FBMotionClip(self,pFileName):
        """
        Constructor.

        pFileName : The complete file path of the media file to access. 
        """
        pass

    def FBMotionClip(self,pName,pFilename):
        """
        Constructor.

        pName : Name of the new MotionClip. 
        pFilename : Name of the file containing the associated motion. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    Filename=property(doc="<b>Read Write Property:</b> Filename and path of motion file.          ")
    RelativePath=property(doc="<b>Read Only Property:</b> Relative path to the motion file.          ")
    Start=property(doc="<b>Read Only Property:</b> Start time of clip.          ")
    Stop=property(doc="<b>Read Only Property:</b> Stop time of clip.          ")
    pass

class FBMotionFileOptions (FBComponent):
    """
    Customize motion file loading.     
         
    """
    def FBMotionFileOptions(self,pStringList):
        """
        Constructor.
        Create a FBMotionFileOptions to be used when importing a motion file. Pass file paths to get the appropriate information about those files, modify the options and then call the file import process. Not all options are usable at the same time, some of them are for specific motion type. You can see the valid configuration by looking at the motion file dialog (accessible from File/Motion File Import...).

        pStringList : The client needs to pass a list of files path to load to collect the motion file information. 
        """
        pass

    def GetTakeCount(self):
        """
        Return the take count in the file to be loaded.

        return : Take count 
        """
        pass

    def GetTakeName(self,pTakeIndex):
        """
        Get the take name.

        pTakeIndex : Index of take to get the name. 
        return : Take name 
        """
        pass

    def GetTakeSamples(self,pTakeIndex):
        """
        Return the number of samples.

        pTakeIndex : Index of take to get the samples count. 
        return : Number of samples 
        """
        pass

    def GetTakeSamplingRate(self,pTakeIndex):
        """
        Return the actual sampling rate as a double, useful when you have a custom sampling rate.

        pTakeIndex : Index of take to get the sampling rate 
        return : Sample rate 
        """
        pass

    def GetTakeSamplingRateMode(self,pTakeIndex):
        """
        Return the sampling rate mode.

        pTakeIndex : Index of take to get the sampling rate mode 
        return : Sample rate mode 
        """
        pass

    def GetTakeSelect(self,pTakeIndex):
        """
        Return true if the take will be loaded.

        pTakeIndex : Index of take. 
        return : True is the take will be loaded 
        """
        pass

    def GetTakeStart(self,pTakeIndex):
        """
        Return the Take Start time.

        pTakeIndex : Index of take to get the start time. 
        return : Start time of the take 
        """
        pass

    def GetTakeStop(self,pTakeIndex):
        """
        Return the Take Stop time.

        pTakeIndex : Index of take to get the stop time. 
        return : Stop time of the take 
        """
        pass

    def SetTakeName(self,pTakeIndex,pName):
        """
        Set the take name.

        pTakeIndex : Index of take to set. 
        pName : Take name to set 
        """
        pass

    def SetTakeSamples(self,pTakeIndex,pSamplesCount):
        """
        Set the number of samples for a particular take.

        pTakeIndex : Index of take to set. 
        pSamplesCount : Number of samples 
        """
        pass

    def SetTakeSamplingRate(self,pTakeIndex,pTimeMode,pCustomSamplingRate):
        """
        Set the sampling rate for a particular take.

        pTakeIndex : Index of take to set. 
        pTimeMode : Time mode to set. 
        pCustomSamplingRate : Custom sampling rate if pTimeMode is set to kFBTimeModeCustom, unused otherwise (default is 30.0) 
        """
        pass

    def SetTakeSelect(self,pTakeIndex,pSelect):
        """
        Indicate if the take will be loaded.

        pTakeIndex : Index of take to set. 
        pSelect : Set to true if the take should be loaded. 
        """
        pass

    def SetTakeStart(self,pTakeIndex,pStartTime):
        """
        Set the Take Start time.

        pTakeIndex : Index of take to set. 
        pStartTime : Time of the first frame of the take 
        """
        pass

    def SetTakeStop(self,pTakeIndex,pStopTime):
        """
        Set the Take Stop time.

        pTakeIndex : Index of take to set. 
        pStopTime : Time of the last frame of the take 
        """
        pass

    BaseRotationOnPreRotation=property(doc="<b>Read Write Property:</b> If set to true, the base rotation will be imported as Pre Rotation. Used for htr, asf/amc files.          ")
    BaseTranslationOnRotationOffset=property(doc="<b>Read Write Property:</b> If set to true, the base translation will be imported as Rotation Pivot offset. Used for htr, asf/amc          ")
    CreateInsteadOfMerge=property(doc="<b>Read Write Property:</b> If set to true, the motion will imported/models will be created in the scene, if set to false, the motion will be merged.          ")
    CreateOpticalSegments=property(doc="<b>Read Write Property:</b> If set to true, optical segments will be created. Used for trc, c3d files.          ")
    CreateReferenceNode=property(doc="Settings based on file type.          ")
    CreateUnmatchedModels=property(doc="<b>Read Write Property:</b> If set to true, nodes will be created to match the hierarchical structure of the imported file.          ")
    CreateUnusedOpticalSegments=property(doc="<b>Read Write Property:</b> If set to true, unused optical segments will be created. Used for trc, c3d files.          ")
    IgnoreModelType=property(doc="<b>Read Write Property:</b> If set to true, model type will not be considered when finding a matching model in the scene.          ")
    ImportDOF=property(doc="<b>Read Write Property:</b> If set to true, the DOF value will be imported from the file.          ")
    ImportScaling=property(doc="<b>Read Write Property:</b> If set to true, scaling values will be imported.          ")
    KeepActorPrefix=property(doc="<b>Read Write Property:</b> If set to true, the Actor prefix will be kept when naming each optical marker. Used with c3d files.          ")
    KeepDummyNode=property(doc="<b>Read Write Property:</b> If set to true, dummy bones from the file are not removed. Used for asf/amc files.          ")
    ModelSelection=property(doc="Common settings when merging, unused with the CreateInsteadOfMerge property is set to true.          ")
    SetLimits=property(doc="<b>Read Write Property:</b> If set to true, use motion limits. Used for asf/amc files.          ")
    SetOccludedToLastValidPosition=property(doc="<b>Read Write Property:</b> If set to true, occluded segments will be set to their last valid position. Used for trc, c3d files.          ")
    TakeStartEnd=property(doc="<b>Read Write Property:</b> Indicates how the start/end value of the take will be modified.          ")
    UpAxisUsedInFile=property(doc="<b>Read Write Property:</b> Indicated the up axis used in the motion file. Only effective when loading c3d files.          ")
    pass

class FBNamespace (FBComponent):
    """
    Objects Containing class.     
     This class is an interface to manipulate object's containing in the scene.      
    """
    def FBNamespace(self,pSingleLevelNamespace,pParentNSObj):
        """
        Constructor.
        Create a new direct children namespace object

        pSingleLevelNamespace : FBNamespace name. This name will be used as namespace itself. this name string shouldn't contain namespace string separator ":". 
        pParentNSObj : the parent namespace object. if NULl means to create top level namespace. 
        """
        pass

    def GetContent(self,pIndex):
        """
        Get the namespace content object count (Not Recursive).

        pIndex : content object index to query. return content object inside this namespace (not recursive) 
        """
        pass

    def GetContentCount(self):
        """
        Get the namespace content objects count (Not Recursive).
        return content objects count inside this namespace (not recursive)

        """
        pass

    def GetContentList(self,pContentList,pModificationFlags,pRecursive,pTypeInfo,pExactTypeMatch):
        """
        Get List of the namespace content.

        pContentList : the list of content to return. 
        pModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBAllContent means all the content. 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively. 
        pTypeInfo : the typeInfo of the type of interested object, 0 for all the objects. 
        pExactTypeMatch : if <b>True</b>, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo). 
        """
        pass

    ChildrenNamespaces=property(doc="<b>List:</b> Direct Children Namespace Objects.          ")
    ContentLocked=property(doc="<b>Read Write Property:</b> Content locking state.          ")
    pass

class FBOpticalGap (FBComponent):
    """
    Optical Gap class.     
         
    """
    def FBOpticalGap(self,pMarker):
        """
        Constructor.

        pMarker : Model marker(default=NULL). 
        """
        pass

    def FBOpticalGap(self,pGap):
        """
        Constructor (copy).

        pGap : Gap to copy data from. 
        """
        pass

    def InsertControlKey(self,pTime):
        """
        Insert a control key for the gap.

        pTime : Insert time for the control key. 
        """
        pass

    def IsValid(self):
        """
        Check if valid (if item exists).

        return : <b>true</b> if segment is valid. 
        """
        pass

    Data=property(doc="<b>Property:</b> Gap curve data.          ")
    Interpolation=property(doc="<b>Property:</b> Gap mode.          ")
    TimeSpan=property(doc="<b>Property:</b> Current timespan.          ")
    pass

class FBOpticalSegment (FBComponent):
    """
    Optical segment class.     
         
    """
    def FBOpticalSegment(self,pOptical):
        """
        Constructor.

        pOptical : Optical model(default=NULL). 
        """
        pass

    def FBOpticalSegment(self,pSegment):
        """
        Constructor.

        pSegment : Optical segment to copy information from. 
        """
        pass

    def Cut(self,pTime):
        """
        Cut the segment for the marker at a given time.

        pTime : Time to cut segment at. 
        """
        pass

    def IsValid(self):
        """
        Check if valid (if item exists).

        return : <b>true</b> if segment is valid. 
        """
        pass

    def Reset(self):
        """
        Reset the marker segment.

        """
        pass

    Data=property(doc="<b>Property:</b> Segment curve data.          ")
    Marker=property(doc="<b>Property:</b> Optical marker.          ")
    MarkerTimeSpan=property(doc="<b>Property:</b> Marker/Segment timespan.          ")
    OriginalTimeSpan=property(doc="<b>Property:</b> Original timespan for segment.          ")
    TimeSpan=property(doc="<b>Property:</b> Current segment timespan.          ")
    Used=property(doc="<b>Property:</b> Is segment used?          ")
    pass

class FBPlayerControl (FBComponent):
    """
    Player control.     
     Interface to use the transport controls (play, stop, etc.) The following Python snippet shows its basic playback operation 
@code
lPlayer = FBPlayerControl()
lPlayer.GotoStart()
lPlayer.Play()
@endcode

Keys can also be set and used with Key(), GotoNextKey(), and GotoPreviousKey(). All actions are performed by default on the current take. The is the MotionBuilder default take, unless you have multiple takes in your scene. To switch between takes, use FBTake. See samples: ShotTrackSetupTool.py, RenderLayers.py, CameraSwitcher.py, BloopSlate.py, RecordLight.py, Timeline.py, CreateProfilingEventsLog.py, MirrorPoseOverTime.py, MultiLayerKeying.py, StartDevice.py, StopDevice.py, TimeCodeKeying.py.     
    """
    def FBPlayerControl(self):
        """
        Constructor.

        """
        pass

    def AddGlobalTimeMark(self,pTime,pName):
        """
        Add a global time mark.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the global time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.

        pTime : Time where to add the time mark. 
        pName : Name of the time mark to add. 
        return : The index of the time mark added if the operation is successful, -1 otherwise. 
        """
        pass

    def DeleteAllGlobalTimeMarks(self):
        """
        Delete all global time marks.

        """
        pass

    def DeleteGlobalTimeMark(self,pIndex):
        """
        Delete a global time mark.
        Note: Internally, the global time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.

        pIndex : Index of the time mark to delete. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def EvaluationPause(self):
        """
        Pause device evaluation thread.

        """
        pass

    def EvaluationResume(self):
        """
        Resume device evaluation thread.

        """
        pass

    def GetEditCurrentTime(self):
        """
        Get Edit Current Time.

        return : The current time, in the edit time referential. 
        """
        pass

    def GetEditStart(self):
        """
        Get Edit Start.

        return : Start value for the edit time range. 
        """
        pass

    def GetEditStop(self):
        """
        Get Edit Stop.

        return : Stop value for the edit time range. 
        """
        pass

    def GetEditZoomStart(self):
        """
        Get Edit Zoom Start.

        return : Start value for the edit zoom window. 
        """
        pass

    def GetEditZoomStop(self):
        """
        Get Edit Zoom Stop.

        return : Stop value for the edit zoom window. 
        """
        pass

    def GetGlobalTimeMarkAction(self,pIndex):
        """
        Returns the action associated with a global time mark.

        pIndex : Index of the time mark. 
        return : The action associated with the time mark. 
        """
        pass

    def GetGlobalTimeMarkColor(self,pIndex):
        """
        Returns the color associated with a global time mark.

        pIndex : Index of the time mark. 
        return : The color associated with the time mark. 
        """
        pass

    def GetGlobalTimeMarkCount(self):
        """
        Returns the number of global time marks.

        return : The number of global time marks. 
        """
        pass

    def GetGlobalTimeMarkName(self,pIndex):
        """
        Returns the name associated with a global time mark.

        pIndex : Index of the time mark. 
        return : The name associated with the time mark. 
        """
        pass

    def GetGlobalTimeMarkTime(self,pIndex):
        """
        Returns the time associated with a global time mark.

        pIndex : Index of the time mark. 
        return : The time associated with the time mark. 
        """
        pass

    def GetNextGlobalTimeMarkIndex(self):
        """
        Returns the next global time mark index, based on the current local time.

        return : The next global time mark index, -1 if any next time mark is available. 
        """
        pass

    def GetPlaySpeed(self):
        """
        Get Play Speed .

        return : transport current playback speed. 
        """
        pass

    def GetPlaySpeedMode(self):
        """
        Get Play Speed Mode.

        return : transport current playback speed mode, including kFBSpeed_Custom mode. 
        """
        pass

    def GetPreviousGlobalTimeMarkIndex(self):
        """
        Returns the previous global time mark index, based on the current local time.

        return : The previous global time mark index, -1 if any previous time mark is available. 
        """
        pass

    def GetTimeReferential(self):
        """
        Get Time Referential.

        return : Current time referential. 
        """
        pass

    def GetTransportFps(self):
        """
        Get the UI frame rate use for display configure in the system.

        return : current FrameRate selected for the system. 
        """
        pass

    def GetTransportFpsValue(self,pTimeMode):
        """
        Get the UI frame rate value.

        pTimeMode : the time mode whose frame rate will be returned 
        return : Frame rate of the input time mode or system time mode when pTimeMode is not provided. 
        """
        pass

    def GetTransportMode(self):
        """
        Get Transport Mode.

        return : Current mode of the transport controls. 
        """
        pass

    def Goto(self,pTime):
        """
        Goto a time specified by pTime.

        pTime : Time to jump to. 
        return : true if successful. 
        """
        pass

    def Goto(self,p0,p1):
        """
        Goto a time specified by <b>pTime</b>.

        p0 : Time to jump to. 
        p1 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit 
        return : <b>true</b> if successful. 
        """
        pass

    def GotoEnd(self):
        """
        GotoEnd button (FastForward).

        return : true if successful. 
        """
        pass

    def GotoEnd(self,p0):
        """
        GotoEnd button (FastForward).

        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit 
        return : <b>true</b> if successful. 
        """
        pass

    def GotoNextKey(self):
        """
        Go to the next key.

        """
        pass

    def GotoPreviousKey(self):
        """
        Go to the previous key.

        """
        pass

    def GotoStart(self):
        """
        GotoStart button (Rewind).

        return : true if successful. 
        """
        pass

    def GotoStart(self,p0):
        """
        GotoStart button (Rewind).

        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit 
        return : <b>true</b> if successful. 
        """
        pass

    def IsLocked(self):
        """
        Return the current locking state of the transport.

        """
        pass

    def Key(self):
        """
        Key default data.
        Key all selected data.

        """
        pass

    def LockTransport(self,pLock):
        """
        Lock the transport control.

        pLock : boolean value that indicates the new locked state of the transport. 
        """
        pass

    def Play(self,pUseMarkers):
        """
        Play button.

        pUseMarkers : Play until next marker if true, ignore markers otherwise. 
        return : true if successful. 
        """
        pass

    def PlayReverse(self,pUseMarkers):
        """
        Play Reverse button.

        pUseMarkers : Play until next marker if true, ignore markers otherwise. 
        return : true if successful. 
        """
        pass

    def Record(self,pOverrideTake,pCopyData):
        """
        Begin recording.

        pOverrideTake : Write over current take?(default=false) 
        pCopyData : Unused. Necessary for compatibility(default=true). 
        return : true if successful. 
        """
        pass

    def SetEditStart(self,pTime):
        """
        Set Edit Start.

        pTime : The new start value for the edit time range. 
        """
        pass

    def SetEditStop(self,pTime):
        """
        Set Edit Stop.

        pTime : The new stop value for the edit time range. 
        """
        pass

    def SetEditZoomStart(self,pTime):
        """
        Set Edit Zoom Start.

        pTime : The new start value for the edit zoom window. 
        """
        pass

    def SetEditZoomStop(self,pTime):
        """
        Set Edit Zoom Stop.

        pTime : The new stop value for the edit zoom window. 
        """
        pass

    def SetGlobalTimeMarkAction(self,pIndex,pAction):
        """
        Sets a new action for an existing global time mark.

        pIndex : Index of the time mark. 
        pAction : The new action for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetGlobalTimeMarkColor(self,pIndex,pColor):
        """
        Sets a new color for an existing global time mark.

        pIndex : Index of the time mark. 
        pColor : The new color for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetGlobalTimeMarkName(self,pIndex,pName):
        """
        Sets a new name for an existing global time mark.

        pIndex : Index of the time mark. 
        pName : The new name for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetGlobalTimeMarkTime(self,pIndex,pTime):
        """
        Sets a new time for an existing global time mark.
        Note: Internally, the global time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.

        pIndex : Index of the time mark. 
        pTime : The new time for the time mark. 
        return : The new index of the modified time mark. 
        """
        pass

    def SetPlaySpeed(self,pSpeed):
        """
        Set Play Speed.

        pSpeed : set customized speed. It will automatically convert to one of pre-defined play speed mode if it is equal to the pre-defined speed. 
        """
        pass

    def SetPlaySpeedMode(self,pPlaySpeedMode):
        """
        Set Play Speed Mode.

        pPlaySpeedMode : a pre-defined play speed mode. Don't make sense to input kFBSpeed_Custom. To set the custom speed, use SetPlaySpeed() function directly. 
        """
        pass

    def SetTimeReferential(self,pTimeReferential):
        """
        Set Time Referential.

        pTimeReferential : The new time referential. Only kFBTimeReferentialAction and kFBTimeReferentialEdit are supported 
        """
        pass

    def SetTransportFps(self,pTimeMode,pCustom):
        """
        Set the system frame rate use for display.

        pTimeMode : Indicate the frame rate value to use base on the FBTimeMode values enum.(kFBTimeModeDefault will be stored in fps) 
        pCustom : Should the time mode be kFBTimeModeCustom, this is used to specify the custom framerate. 
        """
        pass

    def StepBackward(self):
        """
        Step one frame backward.

        return : true if successful. 
        """
        pass

    def StepBackward(self,p0):
        """
        Step one frame backward.

        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit 
        return : <b>true</b> if successful. 
        """
        pass

    def StepForward(self):
        """
        Step one frame ahead.

        return : true if successful. 
        """
        pass

    def StepForward(self,p0):
        """
        Step one frame ahead.

        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit 
        return : <b>true</b> if successful. 
        """
        pass

    def Stop(self):
        """
        Stop button.

        return : true if successful. 
        """
        pass

    IsPlaying=property(doc="<b>Read Only Property:</b> Is the transport control playing?          ")
    IsPlotting=property(doc="<b>Read Only Property:</b> Is there a plotting in progress?          ")
    IsRecording=property(doc="<b>Read Only Property:</b> Is there a recording in progress?          ")
    LoopActive=property(doc="<b>Read Write Property:</b> Is looping active? Deprecated, use the LoopMode property instead.          ")
    LoopMode=property(doc="<b>Read Write Property:</b> Loop mode.          ")
    LoopStart=property(doc="<b>Read Write Property:</b> Loop begin time.          ")
    LoopStop=property(doc="<b>Read Write Property:</b> Loop end time.          ")
    NextMarker=property(doc="<b>Read Only Property:</b> Next marked time.          ")
    OnChange=property(doc="<b>Event Property:</b> Fired when something in the player control has changed. (see FBEventPlayerControlChange)          ")
    PlotSamplingPeriod=property(doc="<b>Read Write Property:</b> Sampling period for the model plotting.          ")
    PreviousMarker=property(doc="<b>Read Only Property:</b> Previous marked time.          ")
    RecordingSamplingPeriod=property(doc="<b>Read Write Property:</b> Sampling period for the model recording.          ")
    SnapMode=property(doc="<b>Read Write Property:</b> Set the transport control snap mode.          ")
    TransportTimeFormat=property(doc="<b>Read Write Property:</b> Current Time Mode of the transport controls.          ")
    ZoomWindowStart=property(doc="<b>Read Write Property:</b> Starting time of the transport control zoom window.          ")
    ZoomWindowStop=property(doc="<b>Read Write Property:</b> Stopping time of the transport control zoom window.          ")
    pass

class FBPointCacheFile (FBComponent):
    """
    Base Model deformer class.     
         
    """
    def FBPointCacheFile(self,pName):
        """
        Constructor.

        pName : Name of Point Cache File Object. 
        """
        pass

    CacheFileName=property(doc="<b>Read Write Property:</b> Filename of media.          ")
    ChannelCount=property(doc="<b>Read Only Property:</b> Channel Count.          ")
    FreeRunning=property(doc="<b>Read Write Property:</b> Free Running.          ")
    Loop=property(doc="<b>Read Write Property:</b> Loop.          ")
    Offset=property(doc="<b>Read Write Property:</b> Offset.          ")
    PlaySpeed=property(doc="<b>Read Write Property:</b> Play Speed.          ")
    StartTime=property(doc="<b>Read Write Property:</b> Start Time.          ")
    StopTime=property(doc="<b>Read Write Property:</b> Stop Time.          ")
    pass

class FBPointCacheManager (FBComponent):
    """
    Point Cache Manager Interface to the point cache manager.     
    See sample: CharacterPointCache.py.     
    """
    AllowCacheResampling=property(doc="<b>Read Write Property:</b> Allow the resample models's existing point cache deformation when true.          ")
    AlwaysAskForPath=property(doc="<b>Read Write Property:</b> Always ask for the point cache file save path when true.          ")
    ApplyCacheOnNewModel=property(doc="<b>Read Write Property:</b> Duplicated the cached models, and assoicated the point cache to the new models.          ")
    ApplyGlobalTransform=property(doc="<b>Read Write Property:</b> Include no-deformable models and the global transform to Vertex Cache when true.          ")
    CacheAABBox=property(doc="<b>Read Write Property:</b> Cache AABBox (Axis Aligned Bounding Box) when true.          ")
    CacheNormal=property(doc="<b>Read Write Property:</b> Cache normal when true.          ")
    CreateFilePerFrameCache=property(doc="<b>Read Write Property:</b> Create the point cache file for each frame when true.          ")
    CreateMultiChannelCache=property(doc="<b>Read Write Property:</b> Create a single multiple channel point cache file for all models when true.          ")
    DefaultPath=property(doc="<b>Read Write Property:</b> Default point cache file save path.          ")
    Models=property(doc="<b>Read Write Property:</b> Models to be recorded          ")
    NewModelRoot=property(doc="<b>Read Write Property:</b> Valid only when ApplyCacheOnNewModel is on. Create New Models under NewModelRoot. otherwise, a NULL model will be created.          ")
    SaveEveryFrame=property(doc="<b>Read Write Property:</b> Recording Frequency.          ")
    SetTransformReference=property(doc="<b> Action Property:</b> Set the model's current transformation as the reference.          ")
    pass

class FBPopup (FBLayout):
    """
    Popup window.     
     This class lets a window (inheriting from FBLayout) be created for another interface. See sample: Popup.py.     
    """
    def FBPopup(self):
        """
        Constructor.

        """
        pass

    def Close(self,pOk):
        """
        Close popup.

        pOk : Equivalent of <b>OK</b> button clicked if <b>true</b> (default = <b>false</b>). 
        """
        pass

    def Show(self,pParent):
        """
        Show popup.

        pParent : Parent object for popup 
        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display in popup.          ")
    Modal=property(doc="<b>Read Write Property:</b> Modal?          ")
    pass

class FBPose (FBComponent):
    """
    Pose class.     
         
    """
    def FBPose(self,pName):
        """
        Constructor.

        pName : Name of pose. 
        """
        pass

    def AddNode(self,pObject,pMatrix,pIsLocalMatrix):
        """
        Add a new pose node.

        pObject : The object for which we are creating the pose information. 
        pMatrix : The transformation of the object we want to save. 
        pIsLocalMatrix : Is the matrix a local matrix? 
        """
        pass

    def CreatePoseThumbnail(self):
        """
        Create an image thumbnail for the current pose.

        """
        pass

    def Find(self,pNodeName):
        """
        Look in this pose if the given node is present.

        pNodeName : Name of the node we are looking for. 
        return : -1 if the node is not in the list or it's position. 
        """
        pass

    def GetNodeCount(self):
        """
        Returns the number of pose nodes stored.

        """
        pass

    def GetNodeMatrix(self,pIndex):
        """
        Get the pose node matrix.

        pIndex : Index of the node. 
        return : a reference to the node's Matrix. 
        """
        pass

    def GetNodeName(self,pIndex):
        """
        Get the pose node at specified index.

        pIndex : Index of the node. 
        """
        pass

    def GetNodeObject(self,pIndex):
        """
        Get the pose node object.

        pIndex : Index of the node. 
        return : a pointer to the node's Object. 
        """
        pass

    def IsNodeLocalMatrix(self,pIndex):
        """
        Get the type of the Matrix for a given node.

        pIndex : Index of the node. 
        return : true if the matrix is defined in Local coordinate space. 
        """
        pass

    def RemoveNode(self,pIndex):
        """
        Remove the pose node at specified index.

        pIndex : Index of the node to be removed. 
        """
        pass

    def SetIsNodeLocalMatrix(self,pIndex,pIsNodeLocalMatrix):
        """
        Set the type of the Matrix for a given node.

        pIndex : Index of the node. 
        pIsNodeLocalMatrix : True if the matrix of the node is a local matrix. 
        """
        pass

    def SetNodeMatrix(self,pIndex,pMatrix):
        """
        Set the pose node matrix.

        pIndex : Index of the node. 
        pMatrix : Matrix to set for this pose node. 
        """
        pass

    def SetNodeObject(self,pIndex,pObject):
        """
        Set the pose node object.

        pIndex : Index of the node. 
        pObject : Object to associate with this pose node. 
        """
        pass

    Type=property(doc="<b>Read Only Property:</b> Type of the pose (bind pose or rest pose)          ")
    pass

class FBProfiler (FBComponent):
    """
    FBProfiler.     
     Central place to query profiling results and change profiling options. See sample: CreateProfilingEventsLog.py.     
    """
    def FBProfiler(self):
        """
        Constructor.

        """
        pass

    def GetEndEventSample(self,pIndex):
        """
        Get end time event for event at given index.
        This function and FBProfileTimeEvent.IsSingleEvent are useful to identify duration of event action.

        pIndex : Sample index. 
        return : Sample object if sample at given index is start sample. 
        """
        pass

    def GetEventSample(self,pIndex):
        """
        Only possible way to query collected FBProfileTimeEvent.

        pIndex : Sample index. 
        return : Sample object. 
        """
        pass

    def GetEventSampleCount(self):
        """
        Get number of time event samples collected during last sampling.

        return : Number of FBProfileTimeEvent samples gathered during sampling. 
        """
        pass

    def GetProfilingCost(self):
        """
        Profiling collection can affect scene performace.
        This function return how costly is profiling.

        return : Cost of profiling the scene. (in mini seconds) 
        """
        pass

    def GetStatComment(self,pIndex):
        """
        Get aditional information about what action is stat refering to.

        pIndex : Index of stat. 
        return : Stat comment. 
        """
        pass

    def GetStatCount(self):
        """
        Stats are holding last execution time/duration of action.
        They are used for actions that doesn't appear frequently, like file IO.

        return : Stats count. They are created when stat occurs, so open or save action needs to be done first to get any information stored in stats. 
        """
        pass

    def GetStatDuration(self,pIndex):
        """
        Get time that was spend on execution of action.

        pIndex : Index of stat. 
        return : Stat duration (in seconds). 
        """
        pass

    def GetStatIndex(self,pName):
        """
        Search for index of given stat name.

        pName : Name of the sample that we are looking for. 
        return : Stat index if found, -1 if not in the list. 
        """
        pass

    def GetStatName(self,pIndex):
        """
        Get information about what action is stat refering to.

        pIndex : Index of stat. 
        return : Stat name. 
        """
        pass

    def GetStatStart(self,pIndex):
        """
        Get start time of action.

        pIndex : Index of stat. 
        return : Start time (in seconds). 
        """
        pass

    def GetStatStop(self,pIndex):
        """
        Get stop time of action.

        pIndex : Index of stat. 
        return : Stop time (in seconds). 
        """
        pass

    ActiveSampling=property(doc="<b>Read/Write Property:</b> Activate the sampling for time events. Call before quering for FBProfileTimeEvent.          ")
    BufferSize=property(doc="<b>Read/Write Property:</b> Buffer size for average and timing computation (maximum value 200).          ")
    EvaluationDepth=property(doc="<b>Read/Write Property:</b> Specify the depth of evaluation profiling for data collection (maximum value is 10).          ")
    FrameReference=property(doc="<b>Read/Write Property:</b> Draw task cycles in relation to main thread cycle time - frame cycle (percentage display).          ")
    ProfilingMode=property(doc="<b>Read/Write Property:</b> Profiling collection modes, including disabling all profiling.          ")
    pass

class FBPropertyAnimatableAction (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableBool (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableColor (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableColorAndAlpha (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableDouble (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableEnum (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="Return the string associated with the index. Will return None when no value is associated.         ")
    pass

class FBPropertyAnimatableInt (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableTime (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableVector2d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableVector3d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyAnimatableVector4d (FBPropertyAnimatable):
    """
        
        
    """
    Data=property(doc="        ")
    pass

class FBPropertyListCharacterExtension (FBPropertyListComponent):
    """
    Character extension property list.b>PropertyList: Character face.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListCharacterExtension(self):
        """
        """
        pass

    pass

class FBPropertyListCharacterMarkerSet (FBPropertyListComponent):
    """
    b>PropertyList: CharacterPose.     
         
    """
    def FBPropertyListCharacterMarkerSet(self):
        """
        """
        pass

    pass

class FBPropertyListCharacterPose (FBPropertyListComponent):
    """
    b>PropertyList: Concrete class for PropertyList of component      
        
    """
    def FBPropertyListCharacterPose(self):
        """
        """
        pass

    pass

class FBPropertyListConstraint (FBPropertyListComponent):
    """
    b>PropertyList: Constraint solver      
        
    """
    def FBPropertyListConstraint(self):
        """
        """
        pass

    pass

class FBPropertyListConstraintSolver (FBPropertyListComponent):
    """
    b>PropertyList: MarkerSet.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBPropertyListConstraintSolver(self):
        """
        """
        pass

    pass

class FBPropertyListControlSet (FBPropertyListComponent):
    """
    b>PropertyList: Deck      
        
    """
    def FBPropertyListControlSet(self):
        """
        """
        pass

    pass

class FBPropertyListDeformer (FBPropertyListComponent):
    """
    b>PropertyList: Device      
        
    """
    def FBPropertyListDeformer(self):
        """
        """
        pass

    pass

class FBPropertyListFileReference (FBPropertyListComponent):
    """
    b>PropertyList: Folder      
        
    """
    def FBPropertyListFileReference(self):
        """
        """
        pass

    pass

class FBPropertyListFolder (FBPropertyListComponent):
    """
    b>List: Group      
        
    """
    def FBPropertyListFolder(self):
        """
        """
        pass

    pass

class FBPropertyListHUD (FBPropertyListComponent):
    """
    b>PropertyList: Handle.     
         
    """
    def FBPropertyListHUD(self):
        """
        """
        pass

    pass

class FBPropertyListHUDElement (FBPropertyListComponent):
    """
    b>PropertyList: Handle.     
         
    """
    def FBPropertyListHUDElement(self):
        """
        """
        pass

    pass

class FBPropertyListKeyingGroup (FBPropertyListComponent):
    """
    b>PropertyList: Light      
        
    """
    def FBPropertyListKeyingGroup(self):
        """
        """
        pass

    pass

class FBPropertyListModelOptical (FBPropertyListComponent):
    """
    b>PropertyList: ModelSkeleton.     
         
    """
    def FBPropertyListModelOptical(self):
        """
        """
        pass

    pass

class FBPropertyListModelSkeleton (FBPropertyListComponent):
    """
    b>PropertyList: ModelTemplate.     
         
    """
    def FBPropertyListModelSkeleton(self):
        """
        """
        pass

    pass

class FBPropertyListMotionClip (FBPropertyListComponent):
    """
    b>List: Namespace      
        
    """
    def FBPropertyListMotionClip(self):
        """
        """
        pass

    pass

class FBPropertyListNamespace (FBPropertyListComponent):
    """
    b>List: Note      
        
    """
    def FBPropertyListNamespace(self):
        """
        """
        pass

    pass

class FBPropertyListObjectPose (FBPropertyListComponent):
    """
    b>PropertyList: Device optical marker      
        
    """
    def FBPropertyListObjectPose(self):
        """
        """
        pass

    pass

class FBPropertyListPhysicalProperties (FBPropertyListComponent):
    """
    b>List: Story Clip pivot models      
        
    """
    def FBPropertyListPhysicalProperties(self):
        """
        """
        pass

    pass

class FBPropertyListRendererCallback (FBPropertyListComponent):
    """
    b>PropertyList: Device optical marker      
        
    """
    def FBPropertyListRendererCallback(self):
        """
        """
        pass

    pass

class FBPropertyListVideoClip (FBPropertyListComponent):
    """
    b>PropertyList: VideoIn      
        
    """
    def FBPropertyListVideoClip(self):
        """
        """
        pass

    pass

class FBPropertyViewManager (FBComponent):
    """
    FBProperty View Manager.     
     Interface to create new property views. There are two ways of creating properties view:on library load using AddPropertyView, RemovePropertyView, HidePropertyView - example can be found in \OpenRealitySDK\Samples\constraints\CharacterSolver\HIK2014Solverwhile application is running using FBPropertyViewList - example can be found in \bin\config\Scripts\Samples\Properties\PropertyViewManager.py See sample: PropertyViewManager.py.     
    """
    def AddPropertyView(self,pClassName,pPropertyName,pHierarchy):
        """
        Add property view to global ('All') view set.

        pClassName : Property owner class name (pClassName if won't be found, a new entry for this class is created). 
        pPropertyName : Property name. 
        pHierarchy : Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation"). 
        return : created object. 
        """
        pass

    def CreatePropertyList(self,pObject,pViewType,pName):
        """
        Create new property view list.

        pObject : Property view set attached to. 
        pViewType : Property view set type. 
        pName : Name for new view list. 
        return : created object. 
        """
        pass

    def FindPropertyList(self,pObject,pViewType,pName):
        """
        Find property view list.

        pObject : Property view set attached to. 
        pViewType : Property view set type. 
        pName : Name of view set. 
        return : Found property view set object or NULL. 
        """
        pass

    def HidePropertyView(self,pClassName,pPropertyName,pHide):
        """
        Hide property view in global ('All') view set.

        pClassName : Property owner class name. 
        pPropertyName : Property name. 
        pHide : Show/Hide. 
        """
        pass

    def RefreshPropertyViews(self):
        """
        Force refresh of browsing property tool.

        """
        pass

    def RemovePropertyList(self,pObject,pViewType,pName):
        """
        Remove property view list (only if editable).

        pObject : Property view set attached to. 
        pViewType : Property view set type. 
        pName : Name for property view list. 
        return : True if successful. 
        """
        pass

    def RemovePropertyView(self,pClassName,pPropertyName):
        """
        Remove property view from global ('All') view set.

        pClassName : Property owner class name. 
        pPropertyName : Property name. 
        return : true if succeed (should not be call on system views). 
        """
        pass

    pass

class FBReferenceTime (FBComponent):
    """
    Reference time class.     
     Interface for the reference time used by MotionBuilder The reference time are identified using unique ID. A unique ID is given when a reference time is added to the system with Add(). Instead of using a linear array to store the reference time, a map is used to link an ID to a reference time. The available IDs can be queried using GetUniqueIDList().      
    """
    def FBReferenceTime(self):
        """
        Constructor.

        """
        pass

    def Add(self,pName):
        """
        Add a reference time to list.

        pName : Name of time to add the list. 
        return : Unique ID of the reference time, use this ID to access the reference time in the future. 
        """
        pass

    def GetReferenceTimeName(self,pID):
        """
        Get the name of a time reference.

        pID : ID of the time reference whose name will be returned. 
        return : Name of reference time with the pID. 
        """
        pass

    def GetTime(self,pID,pSystem):
        """
        Get a reference time.

        pID : ID of reference to get. 
        pSystem : System time. 
        return : Reference time at pIndex. 
        """
        pass

    def GetUniqueIDList(self,pIDArray):
        """
        Get list of currently available IDs.

        pIDArray : Array that will be filled with the requested IDs. 
        """
        pass

    def Remove(self,pID):
        """
        Remove a reference time from the list.

        pID : ID of reference time to remove. 
        """
        pass

    def SetTime(self,pID,pReferenceTime,pSystem):
        """
        Set a reference time.

        pID : ID of reference time set. 
        pReferenceTime : Time to use as reference time. 
        pSystem : System time. 
        """
        pass

    Count=property(doc="<b>Read Only Property:</b> Number of reference times. Deprecated, use GetUniqueIDList() instead.          ")
    CurrentTimeReferenceID=property(doc="<b>Read Write Property:</b> Current reference time ID          ")
    ItemIndex=property(doc="<b>Read Write Property:</b> Current reference time index. Deprecated, use CurrentTimeReferenceID instead.          ")
    pass

class FBRenderer (FBComponent):
    """
    Open Reality renderer interface.     
    See samples: render.py, CameraSwitcher.py.     
    """
    def FBRenderer(self):
        """
        Constructor.
        Client code cannot instantiate objects of this class. The FBSystem and FBScene classes provide access to the current renderer.

        """
        pass

    def ArrangeAllInSchematic(self,pMode):
        """
        Request to arrange all objects in schematic view .

        pMode : Arrange mode. 
        """
        pass

    def ArrangeObjectsInSchematicFromModel(self,pModel):
        """
        Request to arrange a node's tree in the Schematic View, given a starting node.

        pModel : The starting node from which the arrange operation is requested. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def ArrangeSelectedObjectsInSchematic(self):
        """
        Request to arrange selected objects in schematic view .

        """
        pass

    def CreateSchematicBookmark(self,pBookmarkName):
        """
        Create a new bookmark in the Schematic View.

        pBookmarkName : The new bookmark name. 
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if a bookmark with the given name already exists. 
        """
        pass

    def DeleteSchematicBookmark(self,pBookmarkName):
        """
        Delete a bookmark from the Schematic View.

        pBookmarkName : The bookmark name to delete. 
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name. 
        """
        pass

    def FrameCurrentCameraWithModels(self,pAll):
        """
        Frame the current camera either with all models or with the currently selected models.

        pAll : true to frame with all models. 
        return : <b>true</b> if successful. 
        """
        pass

    def GetCameraInPane(self,pPaneIndex):
        """
        Return the camera displayed in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned camera is the camera that would be displayed if the Schematic View was deactivated. If the Camera Switcher is on in the pane associated with the given pane index, the returned camera is the switcher's current camera.Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher().

        pPaneIndex : The pane index. 
        return : The camera used in the given pane index, NULL if the pane index is invalid. 
        """
        pass

    def GetCurrentSchematicBookmarkName(self):
        """
        Return the current bookmark name used by the Schematic View.

        return : The current bookmark name used by the Schematic View. An empty string is returned if there is no current bookmark. 
        """
        pass

    def GetDisplayableGeometry(self,pIndex):
        """
        Get the displayable geometry model.
        Those geometry models which have Show property ON are considered as 'displayable'.

        pIndex : displayable geometry model index to query. 
        return : displayable geometry model. 
        """
        pass

    def GetDisplayableGeometryInCameraFrustum(self,pModelList,pCamera):
        """
        Get a list of displayable geometry inside given camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.

        pModelList : ModelList holding the return models. 
        pCamera : use current camera if NULL. 
        return : Reference to pModelList. if pModelList is NULL return a const reference to internal static FBModelList and consecutive call to this function will invalidate the result of previous call. 
        """
        pass

    def GetDisplayableLight(self,pIndex):
        """
        Get the displayable light.
        Those light models which have Show property ON are considered as 'displayable'.

        pIndex : displayable light index to query. 
        return : displayable light. 
        """
        pass

    def GetLastPickInfoList(self,pPickInfosList):
        """
        Return the last picking info list in the current view pane.

        pPickInfosList : The list of pick infos. 
        return : number of item in the list. 
        """
        pass

    def GetPaneCount(self):
        """
        Return the number of panes displayed in the viewer's layout.

        return : The number of panes displayed. 
        """
        pass

    def GetSchematicBookmarkNames(self):
        """
        Return the bookmark names available in the Schematic View.

        return : A string list containing the bookmark names available in the Schematic View. An empty list is returned if no bookmark is available. 
        """
        pass

    def GetSchematicNodesBoundingBox(self,pConsiderCollapsedNodes,pTop,pLeft,pBottom,pRight):
        """
        Returns the bounding box (top, left, bottom, right) used by all the Schematic View nodes.

        pConsiderCollapsedNodes : True to also consider nodes which are not visible because collapsed, false otherwise. 
        pTop : Top value of the bounding box. Will be filled once the method returns. 
        pLeft : Left value of the bounding box. Will be filled once the method returns. 
        pBottom : Bottom value of the bounding box. Will be filled once the method returns. 
        pRight : Right value of the bounding box. Will be filled once the method returns. 
        return : True if the operation is successful, false otherwise (e.g. the Schematic View has any node in it, etc.). 
        """
        pass

    def GetSchematicNodesBoundingBoxFromModel(self,pModel,pConsiderCollapsedNodes,pTop,pLeft,pBottom,pRight):
        """
        Returns the bounding box (top, left, bottom, right) of a node's tree in the Schematic View, given a starting node.

        pModel : The starting node from which the bounding box tree is requested. 
        pConsiderCollapsedNodes : True to also consider nodes which are not visible because collapsed, false otherwise. 
        pTop : Top value of the bounding box. Will be filled once the method returns. 
        pLeft : Left value of the bounding box. Will be filled once the method returns. 
        pBottom : Bottom value of the bounding box. Will be filled once the method returns. 
        pRight : Right value of the bounding box. Will be filled once the method returns. 
        return : True if the operation is successful, false otherwise (e.g. the starting node is not in the Schematic View, etc.). 
        """
        pass

    def GetSchematicViewPaneIndex(self):
        """
        Return the pane index of the pane displaying the Schematic View.

        return : The pane index of the pane displaying the Schematic View, -1 if the Schematic View is currently not displayed in any pane. 
        """
        pass

    def GetSelectedPaneIndex(self):
        """
        Return the pane index associated with the selected pane in the active viewer's layout.

        return : The selected pane index. 
        """
        pass

    def GetViewingOptions(self):
        """
        Obtain the current viewing options.

        return : A structure that can be queried and updated for a call to SetViewingOptions. 
        """
        pass

    def IsCameraSwitcherInPane(self,pPaneIndex):
        """
        Return the Camera Switcher activeness in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned value is the value that would be returned if the Schematic View was deactivated.

        pPaneIndex : The pane index. 
        return : True if the Camera Switcher is active in the pane associated with the given pane index, False otherwise. 
        """
        pass

    def IsCurrentSchematicBookmarkDirty(self):
        """
        Return if the current bookmark used by the Schematic View is dirty or not.

        return : True if the current bookmark is dirty, false otherwise. False is returned if there is no current bookmark. 
        """
        pass

    def IsModelInsideCameraFrustum(self,pGeometry,pCamera):
        """
        To tell if given model is located inside camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.

        pGeometry : the geometry to be queried. 
        pCamera : use current camera if NULL. 
        return : true if Model is inside camera frustum. 
        """
        pass

    def KeyboardInput(self,pKeyIndex,pKeyState,pIsTrigger):
        """
        Keyboard input.

        pKeyIndex : Key index. (See "enum FBDeviceKeyboardKey" above for supported keys) 
        pKeyState : Key state. (True == key is down, False == key is up) 
        pIsTrigger : When setting pKeyState to True, resets key state to False right after operation. 
        """
        pass

    def MouseInput(self,pX,pY,pInputType,pButtonKey,pModifier,pWheelDeltaValue,pLayer):
        """
        Mouse input.

        pX : X position. 
        pY : Y position. 
        pInputType : Type of input. 
        pButtonKey : Button/Key pressed. 
        pModifier : Modifier pressed (CTRL/ALT/SHIFT). 
        pWheelDeltaValue : Mouse wheel delta value 
        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def MouseInputNormalized(self,pX,pY,pInputType,pButtonKey,pModifier,pWheelDeltaValue,pLayer,pPaneId):
        """
        Mouse input.

        pX : X position, normalized to the range of [0, 1] in the view port dimension. 
        pY : Y position, normalized to the range of [0, 1] in the view port dimension. 
        pInputType : Type of input. 
        pButtonKey : Button/Key pressed. 
        pModifier : Modifier pressed (CTRL/ALT/SHIFT). 
        pWheelDeltaValue : Mouse wheel delta value 
        pLayer : Rendering layer ID(default=-1). 
        pPaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer. 
        return : <b>true</b> if successful. 
        """
        pass

    def OGLModelDisplay(self,pRenderOptions,pModel):
        """
        pRenderOptions : FBRenderOptions
        pModel : FBModel
        """
        pass

    def OGLSetupSceneLights(self,pRenderOptions):
        """
        Setup the scene lights in OpenGL.

        pRenderOptions : See FBRenderOptions for more detail. 
        """
        pass

    def Pick(self,pX,pY,pPickInfosList,pNeedIntersectPosition):
        """
        Object picking selection.

        pX : X position. 
        pY : Y position. 
        pPickInfosList : The list of pick infos. 
        pNeedIntersectPosition : require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh. 
        """
        pass

    def PickNormalized(self,pX,pY,pPickInfosList,pNeedIntersectPosition,pPaneId):
        """
        Object picking selection.

        pX : X position, normalized to the range of [0, 1] in the view port dimension. 
        pY : Y position, normalized to the range of [0, 1] in the view port dimension. 
        pPickInfosList : The list of pick infos. 
        pNeedIntersectPosition : require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh. 
        pPaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer. 
        """
        pass

    def PreRender(self,pLayer):
        """
        PreRenders one frame (needed for some shaders) This functions destroys the frame buffer content and must be called every time a render is called the typical order of call must be Renderer->Prerender // at this point the frame buffer is garbage -Clear the ogl -Do your render functions Renderer->Render.

        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def RectPick(self,pX1,pY1,pX2,pY2,pPickInfosList):
        """
        Object rectangle selection.

        pX1 : Left upper corner X position. 
        pY1 : Left upper corner y position. 
        pX2 : Right bottom corner X position. 
        pY2 : Right bottom corner y position. 
        pPickInfosList : The list of pick infos. 
        """
        pass

    def RectPickNormalized(self,pX1,pY1,pX2,pY2,pPickInfosList,pPaneId):
        """
        Object rectangle selection.

        pX1 : Left upper corner X position, normalized to the range of [0, 1] in the viewport dimension. 
        pY1 : Left upper corner y position, normalized to the range of [0, 1] in the viewport dimension. 
        pX2 : Right bottom corner X position, normalized to the range of [0, 1] in the viewport dimension. 
        pY2 : Right bottom corner y position, normalized to the range of [0, 1] in the viewport dimension. 
        pPickInfosList : The list of pick infos. 
        pPaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer. 
        """
        pass

    def RenameSchematicBookmark(self,pOldBookmarkName,pNewBookmarkName):
        """
        Rename a bookmark in the Schematic View.

        pOldBookmarkName : The bookmark name to rename. 
        pNewBookmarkName : The new bookmark name. 
        return : True if the operation is successful, false otherwise. False is returned if the old/new bookmark name is empty, if the old bookmark doesn't exist or if a bookmark with the new given name already exists. 
        """
        pass

    def Render(self,pLayer):
        """
        Renders one frame.

        pLayer : Rendering layer ID(default=-1). 
        return : <b>true</b> if successful. 
        """
        pass

    def RenderBegin(self,pX,pY,pW,pH):
        """
        RenderBegin.
        must be called before rendering can happen

        pX : X position where to render. 
        pY : Y position where to render. 
        pW : Width of render area. 
        pH : Hight of render area. 
        """
        pass

    def RenderEnd(self,pView):
        """
        RenderEnd.

        pView : If you want the renderer to draw artifacts, such as TimeCode, CameraLabel or SafeArea, you must provide the FBView on which the renderer draws on. 
        """
        pass

    def SelectSchematicBookmark(self,pBookmarkName):
        """
        Select an existing bookmark in the Schematic View and use it as the current bookmark.

        pBookmarkName : The bookmark name to select. 
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name. 
        """
        pass

    def SetCameraInPane(self,pCamera,pPaneIndex):
        """
        Set the camera to display in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the camera will be displayed when the Schematic View will be deactivated from this pane.Note: If current pane uses Camera Switcher, it will be set to use Camera, rather than old behavior that still uses Camera Switcher and sets Camera to be Camera Switcher's current camera, which introduce a Zombie Camera Switcher problem. By using Camera, the problem is gone.Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher().

        pCamera : The camera to set. 
        pPaneIndex : The pane index. 
        """
        pass

    def SetCameraSwitcherInPane(self,pPaneIndex,pActive):
        """
        Set/Remove the Camera Switcher in the given pane index.
        To specify which camera the Camera Switcher should be displaying, use the SetCameraInPane method. If the Schematic View is displayed in the pane associated with the given pane index, the camera switcher will be displayed (if activated) when the Schematic View will be deactivated from this pane.

        pPaneIndex : The pane index. 
        pActive : True to activate the Camera Switcher in the given pane, False to remove it. 
        """
        pass

    def SetPaneCount(self,pPaneCount):
        """
        Set the number of panes to display in the viewer's layout.

        pPaneCount : The number of panes to display. 
        """
        pass

    def SetSchematicViewInPane(self,pPaneIndex,pActive):
        """
        Set/Remove the Schematic View in the given pane index.
        When activating the Schematic View in the pane, if the Schematic View is already activated in another pane, the Schematic View will be removed from latter before being activated into the new pane.

        pPaneIndex : The pane index. 
        pActive : True to activate the Schematic View in the given pane, False to remove it. 
        """
        pass

    def SetSelectedPaneIndex(self,pPaneIndex):
        """
        Select the pane associated with the given pane index in the active viewer's layout.

        pPaneIndex : The pane index. 
        return : True if the operation is successful, False otherwise. 
        """
        pass

    def SetViewingOptions(self,pOptions):
        """
        Set the viewing options.

        pOptions : See FBViewingOptions for more detail. 
        """
        pass

    def SetViewport(self,pX,pY,pW,pH):
        """
        Must be called before inputing if the same renderer is used on multiple views/cameras in the same application.

        pX : X position where to render. 
        pY : Y position where to render. 
        pW : Width of render area. 
        pH : Hight of render area. 
        """
        pass

    def UpdateCurrentSchematicBookmark(self):
        """
        Update the current bookmark in the Schematic View.

        return : True if the operation is successful, false otherwise. False is returned if there is no current bookmark. 
        """
        pass

    AdvancedLightingMode=property(doc="<b>Read write Property:</b> Turn on/off advanced lighting setting UI widgets.          ")
    AdvancedMaterialMode=property(doc="<b>Read write Property:</b> Turn on/off advanced material setting UI widgets.          ")
    AutoEvaluate=property(doc="<b>Read Write Property:</b> Indicate if a call to RenderBegin will also cause a re-evaluation of the scene.          ")
    Background=property(doc="<b>Read Write Property:</b> The renderer.          ")
    CurrentCamera=property(doc="        ")
    CurrentPaneCallbackIndex=property(doc="<b>Read Write Property:</b> Current Pane's Renderer Callback Index.          ")
    CurrentPaneCallbackPrefIndex=property(doc="<b>Read Write Property:</b> Current Pane's Renderer Callback Preference Index.          ")
    DisplayNormals=property(doc="<b>Read Write Property:</b> Display model normals in main viewer.          ")
    DisplaySetUpdateId=property(doc="<b>Read Only Property:</b> Current DisplaySet Update Id. Add/Delete models, Show/Hide models will affect DisplaySet.          ")
    DisplayableGeometryCount=property(doc="<b>Read Only Property:</b> Displayable geometry count.          ")
    DisplayableLightCount=property(doc="<b>Read Only Property:</b> Displayable light count.          ")
    FrustumCulling=property(doc="<b>Read Write Property:</b> Turn on/off the early frustum culling optimization.          ")
    HideManipulatorsOnManip=property(doc="<b>Read Write Property:</b> Hide manipulators UI elements while manipulating.          ")
    HideManipulatorsOnPlayback=property(doc="<b>Read Write Property:</b> Hide manipulators UI elements during playback.          ")
    IDBufferDisplay=property(doc="<b>Read write Property:</b> Render Model's unique Color ID into color Buffer (used for picking)          ")
    IDBufferPicking=property(doc="<b>Read write Property:</b> Use ID (Color) Buffer for picking, instead of OpenGl selection buffer picking.          ")
    IDBufferPickingAlpha=property(doc="<b>Read write Property:</b> Those Semi-transparent (Alpha Blend) geometry(region) contribute less than this threshold, will be considered as invisible during ID picking.          ")
    PickingEnabled=property(doc="<b>Read Write Property:</b> Is picking in the viewer enabled?          ")
    RegisteredCallbackCount=property(doc="<b>Read Only Property:</b> Registered Renderer Callback Count.          ")
    RendererCallbacks=property(doc="<b>List:</b> Renderer Callbacks attached.          ")
    RendererUpdateId=property(doc="<b>Read Only Property:</b> Current Render Update Id. DisplaySet update, material change, texture changes and shader change and other operations will trigger Renderer update.          ")
    Scene=property(doc="<b>Read Write Property:</b> Scene that the renderer will use/draw          ")
    SelectionForceSnapPointsDisplay=property(doc="<b>Read write Property:</b> Force show all feature points (pivots and etc) on selected models if true, ignore individual model's settings.          ")
    SelectionOverride=property(doc="<b>Read write Property:</b> Add transparent color override layer on selected models if true.          ")
    SelectionOverrideColor=property(doc="<b>Read write Property:</b> Selection override layer color.          ")
    SelectionOverrideTransparency=property(doc="<b>Read write Property:</b> Selection override layer transparency.          ")
    ShowStats=property(doc="<b>Read Write Property:</b> Show the stats about FPS, Evaluation rate ... like when using Shift-F in main viewer.          ")
    UseCameraSwitcher=property(doc="        ")
    pass

class FBRendererCallback (FBComponent):
    """
    Open Reality renderer callback interface.     
         
    """
    def FBRendererCallback(self,pName):
        """
        Constructor.

        pName : str
        """
        pass

    DefaultCameraBackPlateRendering=property(doc="<b>Read write Property:</b> Set true to use default camera back plate rendering; set false to disable it.          ")
    DefaultCameraFrontPlateRendering=property(doc="<b>Read write Property:</b> Set true to use default camera front plate rendering; set false to disable it.          ")
    DefaultLightGroundProjectionRendering=property(doc="<b>Read write Property:</b> Set true to use default light ground projection rendering; set false to disable it.          ")
    DefaultLightVolumeRendering=property(doc="<b>Read write Property:</b> Set true to use default light volume rendering; set false to disable it.          ")
    SupportIDBufferPicking=property(doc="<b>Read write Property:</b> Can this Renderer Callback support IDBuffer Picking.          ")
    pass

class FBRigidBody (FBComponent):
    """
    Rigid body class.     
         
    """
    def FBRigidBody(self,pOptical):
        """
        Constructor.

        pOptical : Optical model(default=NULL). 
        """
        pass

    def FBRigidBody(self,pRigidBody):
        """
        Constructor.

        pRigidBody : Rigid body to copy information from. 
        """
        pass

    def ComputeAnimation(self):
        """
        Compute the rigid body animation.

        """
        pass

    def IsValid(self):
        """
        Check if valid (if item exists).

        return : <b>true</b> if segment is valid. 
        """
        pass

    def Snap(self):
        """
        Snap the rigid body.

        """
        pass

    Done=property(doc="<b>Property:</b> Done?          ")
    Markers=property(doc="<b>Property:</b> List of markers composing the rigid body.          ")
    Mode=property(doc="<b>Property:</b> Rigid body mode.          ")
    Model=property(doc="<b>Property:</b> Rigid body model.          ")
    QualityData=property(doc="<b>Property:</b> Quality of rigid body.          ")
    SmoothWidth=property(doc="<b>Property:</b> Smoothing width.          ")
    pass

class FBScene (FBComponent):
    """
    Access to the MotionBuilder scene.     
     In MotionBuilder, the scene is the environment where your models exist. The scene contains models which you can import, select, transform, copy, tweak, and animate.The FBScene object is obtained from the scene attribute of FBSystem.The FBScene class contains many attributes that you can use to access objects, e.g cameras, characters, lights, and takes, essentially everything you see in the Navigator in the UI. A project can only contain one scene, and if you try to create an instance of a scene you will get an error, so you must access the scene by getting a handle through FBSystem. 
@code
myScene = FBSystem().Scene
@endcode

See also the C++ code sample in toolscene. See samples: InsertCurrentTake.py, DeleteUnusedMedia.py, MirrorPoseOverTime.py, SelectModelsWithNameContainingSubstring.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py, StartDevice.py.     
    """
    def FBScene(self):
        """
        Constructor.
        Client code cannot instantiate objects of this class. The FBSystem class provides access to the current scene object.

        """
        pass

    def CandidateEvaluationAndResolve(self):
        """
        Resolving the Candidate.

        return : true if successful. 
        """
        pass

    def CleanEmptyGroups(self):
        """
        Remove all empty groups present in the scene.

        return : The number of empty groups removed. 
        """
        pass

    def CleanEmptyRelationConstraints(self):
        """
        Remove all empty relation constraints present in the scene.

        return : The number of empty relation constraints removed. 
        """
        pass

    def CleanEmptySets(self):
        """
        Remove all empty sets present in the scene.

        return : The number of empty sets removed. 
        """
        pass

    def CleanInactiveConstraints(self):
        """
        Remove all inactive constraints present in the scene.

        return : The number of inactive constraints removed. 
        """
        pass

    def CleanRelationConstraintsUnusedBoxes(self):
        """
        Remove all unused boxes in relations constraints present in the scene.

        return : The number of unused boxes in relations constraints removed. 
        """
        pass

    def CleanUnusedAudioClips(self):
        """
        Remove all unused audio clips present in the scene.

        return : The number of unused audio clips removed. 
        """
        pass

    def CleanUnusedMaterials(self):
        """
        Remove all unused materials present in the scene.

        return : The number of unused material removed. 
        """
        pass

    def CleanUnusedShaders(self):
        """
        Remove all unused shaders present in the scene.

        return : The number of unused shaders removed. 
        """
        pass

    def CleanUnusedTextures(self):
        """
        Remove all unused textures present in the scene.

        return : The number of unused textures removed. 
        """
        pass

    def CleanUnusedVideoClips(self):
        """
        Remove all unused video clips present in the scene.

        return : The number of unused video clips removed. 
        """
        pass

    def Clear(self):
        """
        Clears the elements part of the scene.
        Not those that belong to all the scenes.

        """
        pass

    def Evaluate(self):
        """
        Evaluate the scene.

        return : true if successful. 
        """
        pass

    def EvaluateDeformations(self):
        """
        Evaluate the deformations of the scene.

        return : true if successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetScriptsPaths(self,pPathList):
        """
        Get paths of all the python scripts object in the scene.

        pPathList : Out parameter, to collect the path of python scripts. 
        """
        pass

    def NamespaceCleanup(self):
        """
        Remove all empty namespaces.
        During some namespace operations, empty namespace may left over, while this is not harmful but could be annoying. Save the scene and load it back those empty namespaces will disappear. And this function also allow user to remove all empty namespaces from the scene easily via SDK.

        return : <b>True</b> if operation successfully. 
        """
        pass

    def NamespaceDelete(self,pNamespace):
        """
        Delete the namespace & all its content.

        pNamespace : the namespace to work on 
        return : <b>True</b> if operation successfully, <b>False</b> is this namespace doesn't exist, or is locked (by FileReferencing or etc.,) 
        """
        pass

    def NamespaceDeleteContent(self,pNamespace,pModificationFlags,pRecursive,pTypeInfo,pExactTypeMatch):
        """
        Delete the namespace content.

        pNamespace : the namespace to work on 
        pModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace. 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively. 
        pTypeInfo : the typeInfo of the type of interested object, default for all the objects. 
        pExactTypeMatch : if <b>True</b>, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo). 
        return : <b>False</b> is the given namespace doesn't exist, or is locked (by FileRef or etc.,), <b>True</b> otherwise. 
        """
        pass

    def NamespaceEmpty(self,pNamespace):
        """
        Query if namespace is empty.

        pNamespace : the namespace to query, NULL for whole scene. 
        return : <b>True</b> if the namespace (don't include nested children namespace) is empty 
        """
        pass

    def NamespaceExist(self,pNamespace):
        """
        Query if namespace exists.

        pNamespace : the namespace to query 
        return : <b>True</b> if the namespace exist, otherwise return <b>False</b>. 
        """
        pass

    def NamespaceExport(self,pNamespace,pFilePath,pASCIIFormat):
        """
        Export scene content within namespace to file.

        pNamespace : the namespace to use, must exist 
        pFilePath : the referenced file path to export. 
        pASCIIFormat : save the file in ASCII format. 
        return : <b>True</b> if successfully. 
        """
        pass

    def NamespaceGet(self,pNamespace):
        """
        Get Namespace object.

        pNamespace : the namespace to query 
        return : Namespace with exact name matching 
        """
        pass

    def NamespaceGetChildrenList(self,pNamespaceList,pNamespace,pRecursive):
        """
        Get list of children namespaces in the given namespace.

        pNamespaceList : the list of namespace to return. 
        pNamespace : specify the parent namespace, NULL for the whole scene. 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively. 
        return : the list of children namespaces. 
        """
        pass

    def NamespaceGetContentList(self,pContentList,pNamespace,pModificationFlags,pRecursive,pTypeInfo,pExactTypeMatch):
        """
        Get List of the namespace content.

        pContentList : the list of content to return. 
        pNamespace : the namespace to work on, NULL for whole scene. 
        pModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace. 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively. 
        pTypeInfo : the typeInfo of the type of interested object, 0 for all the objects. 
        pExactTypeMatch : if <b>True</b>, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo). 
        """
        pass

    def NamespaceGetOwnerFileReference(self,pNamespace):
        """
        Get Owner FileReference object if the namespace is originated from File Reference.

        pNamespace : the namespace to work on, could be nested namespace inside the FileReference's namespace. 
        return : the FileReference object is the namespace is originated from. NULL otherwise. 
        """
        pass

    def NamespaceImport(self,pNamespace,pFilePath,pAsFileReference):
        """
        Import file into Namespace (or as file reference)

        pNamespace : the namespace to import to, must be in editable scope. 
        pFilePath : the referenced file path to import. 
        pAsFileReference : import the file as file reference. The default value is false. 
        return : <b>True</b> if successfully. 
        """
        pass

    def NamespaceImportToMultiple(self,pDstNamespaceList,pFilePath,pAsFileReference):
        """
        Import file into multiple Namespaces (or as file references)

        pDstNamespaceList : the Dst namespaces list to import, must not exist or be self contained. 
        pFilePath : the referenced file path to import. 
        pAsFileReference : import the file as file reference. The default value is false. 
        return : <b>True</b> if successfully. 
        """
        pass

    def NamespaceRename(self,pNameSpace,pNewNamespace,pRecursive,pTypeInfo,pExactTypeMatch):
        """
        Rename the namespace.

        pNameSpace : the namespace to work on, NULL for whole scene. 
        pNewNamespace : the new namespace 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively. 
        pTypeInfo : the typeInfo of the type of interested object, default for all the objects. 
        pExactTypeMatch : if <b>True</b>, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo). 
        return : <b>True</b> if operation successfully, <b>False</b> is this namespace (or pTypeInfo type of objects) doesn't exist, or locked (by FileReferencing or etc.,) 
        """
        pass

    def NamespaceSelectContent(self,pNamespace,pSelect,pModificationFlags,pRecursive,pTypeInfo,pExactTypeMatch):
        """
        Select (or de-select) the namespace content.

        pNamespace : the namespace to work on, NULL for whole scene. 
        pSelect : <b>True</b> (or <b>False</b>) indicate to select (or de-select) 
        pModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace. 
        pRecursive : <b>True</b> only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively. 
        pTypeInfo : the typeInfo of the type of interested object, default for all the objects. 
        pExactTypeMatch : if <b>True</b>, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo). 
        """
        pass

    ActorFaces=property(doc="<b>List:</b> ActorFaces in scene.          ")
    Actors=property(doc="<b>List:</b> Actors in scene.          ")
    AudioClips=property(doc="<b>List:</b> Audio clips in scene.          ")
    Cameras=property(doc="<b>List:</b> Cameras in scene.          ")
    CharacterExtensions=property(doc="<b>List:</b> Character extensions available in the scene.          ")
    CharacterFaces=property(doc="<b>List:</b> Character faces in scene.          ")
    CharacterMarkerSets=property(doc="<b>List:</b> Character marker sets in scene.          ")
    CharacterPoses=property(doc="<b>List:</b> Character poses in scene.          ")
    Characters=property(doc="<b>List:</b> Characters in scene.          ")
    Components=property(doc="<b>List:</b> Generic List of components.          ")
    ConstraintSolvers=property(doc="<b>List:</b> Constraint Solvers present in the scene.          ")
    Constraints=property(doc="<b>List:</b> Constraints in scene.          ")
    ControlSets=property(doc="<b>List:</b> Control set rigs in scene.          ")
    Deformers=property(doc="<b>List:</b> Deformers for scene.          ")
    Devices=property(doc="<b>List:</b> Devices for scene.          ")
    FileReferences=property(doc="<b>List:</b> FileReference available in the scene.          ")
    Folders=property(doc="<b>List:</b> Folders in scene.          ")
    Groups=property(doc="<b>List:</b> Groups available in the scene.          ")
    HUDs=property(doc="<b>Read Only Property:</b> Heads Up Displays in the scene.          ")
    Handles=property(doc="<b>List:</b> Handles present in the scene.          ")
    KeyingGroups=property(doc="<b>Read Write Property:</b> Keying Groups in the scene.          ")
    Lights=property(doc="<b>List:</b> Lights in scene.          ")
    MarkerSets=property(doc="<b>List:</b> Marker sets in scene.          ")
    Materials=property(doc="<b>List:</b> Materials for scene.          ")
    ModelOpticals=property(doc="<b>Read Write Property:</b> Optical Data in the scene.          ")
    ModelSkeletons=property(doc="<b>Read Write Property:</b> Bones (Skeletons) in the scene.          ")
    MotionClips=property(doc="<b>List:</b> Motion clips in scene.          ")
    Namespaces=property(doc="<b>List:</b> Namespace (include FileReference) available in the scene          ")
    Notes=property(doc="<b>List:</b> Notes in scene.          ")
    ObjectPoses=property(doc="<b>List:</b> ObjectPoses in scene.          ")
    OnChange=property(doc="<b>Event:</b> Something in the scene has happened.(FBEventSceneChange)          ")
    OnTakeChange=property(doc="<b>Event:</b> Something related to a take has happened.(FBEventTakeChange)          ")
    PhysicalProperties=property(doc="<b>List:</b> PhysicalProperties present in the scene.          ")
    Poses=property(doc="<b>List:</b> Poses in scene.          ")
    Renderer=property(doc="<b>Read Only Property:</b> Local renderer.          ")
    RootModel=property(doc="<b>Read Only Property:</b> Scene Root model for that scene          ")
    Sets=property(doc="<b>List:</b> Sets available in the scene.          ")
    Shaders=property(doc="<b>List:</b> Shaders for scene.          ")
    Takes=property(doc="<b>List:</b> Takes for scene.          ")
    Textures=property(doc="<b>List:</b> Textures for scene.          ")
    UserObjects=property(doc="<b>List:</b> User objects          ")
    VideoClips=property(doc="<b>List:</b> Video clips in scene.          ")
    pass

class FBSpreadPart (FBComponent):
    """
    Spreadsheet part.     
     Due to protected constructor, this can only be created by a child object.      
    """
    Column=property(doc="<b>Read Only Property:</b> Column number.          ")
    Enabled=property(doc="<b>Read Write Property:</b> Is SpreadPart enabled?          ")
    Justify=property(doc="<b>Read Write Property:</b> Text justification for SpreadPart          ")
    ReadOnly=property(doc="<b>Read Write Property:</b> Is SpreadPart read-only?          ")
    Row=property(doc="<b>Read Only Property:</b> Row number.          ")
    Style=property(doc="<b>Read Write Property:</b> Style of cell          ")
    pass

class FBStory (FBComponent):
    """
    Story Management class.     
     This class serve as a management control for the Story global settings and members. See samples: CreateShotClip.py, InsertCurrentTake.py, BloopSlate.py, RecordLight.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py, PrintClipNamesAndStartStopFrames.py.     
    """
    def FBStory(self):
        """
        Constructor.

        """
        pass

    def CleanEmptyTracksAndFolders(self):
        """
        Remove all empty tracks and folders present in the Story Tool.

        return : The number of empty story tracks and/or folders removed. 
        """
        pass

    ClipsTextsVisible=property(doc="<b>Read Write Property:</b> If true, clips' texts are visible.          ")
    LockedShot=property(doc="<b>Read Write Property:</b> If true, shots will be locked (no time discontinuity).          ")
    MaintainShotAndClipShotLengthsSynced=property(doc="<b>Read Write Property:</b> When working in time discontinuity, if true, shots and their corresponding shot clips will be kept in sync in regards of their lengths.          ")
    Mute=property(doc="<b>Read Write Property:</b> If true, the Story mode will be globally disabled.          ")
    NoneBlockingPostprocess=property(doc="<b>Read Write Property:</b> If true, record to disk will post process recorded data in low priority thread without affecting application performance. Clip in story will remain unloaded.          ")
    RecordToDisk=property(doc="<b>Read Write Property:</b> If true, record to story will record directly to disk.          ")
    RootEditFolder=property(doc="<b>Read Only Property:</b> Story's root edit folder          ")
    RootFolder=property(doc="<b>Read Only Property:</b> Story's root folder          ")
    SummaryClip=property(doc="<b>Read Write Property:</b> If true, summary clips for story folders will be created to help manipulating folder content.          ")
    pass

class FBStoryClip (FBComponent):
    """
    Story Clip class.     
     Clips represents media, at a specific time, for a specific duration, in a track.Clip offset is depending on Traveling node and Traveling node function. First we compute clip transformation matrix, where scaling is always 1, 1, 1. Translation is in position of Traveling node at clip first frame. Rotation is based on vector from first to last frame position of Traveling node. On top of that we apply offset and expose that as Clip Offset T & R. When you change clip offset T or R we extract clip offset based on current clip transformation matrix. Clip transformation matrix can change when Traveling node change or Traveling node function change. See samples: AudioTrackSetupTool.py, VideoClip.py, PrintClipNamesAndStartStopFrames.py.     
    """
    def FBStoryClip(self,pClipObject,pTrack,pTime):
        """
        Constructor.

        pClipObject : Object (media data) for the clip. 
        pTrack : The track in which we create the clip. 
        pTime : Time where the clip should begin. 
        """
        pass

    def FBStoryClip(self,pFilePath,pTrack,pTime):
        """
        Constructor.

        pFilePath : Media file path to create clip with. 
        pTrack : The track in which we create the clip. 
        pTime : Time where the clip should begin. 
        """
        pass

    def FBStoryClip(self,pFilePath,pTrack,pTime,pTimeOffset):
        """
        Constructor.

        pFilePath : Media file path to create clip with. 
        pTrack : The track in which we create the clip. 
        pTime : Time where the clip should begin. 
        pTimeOffset : Time offset where the clip should begin. 
        """
        pass

    def CanAssignSourcesToDestinations(self):
        """
        CanAssignSourcesToDestinations.
        Determines if the animation clip can assign its sources to some destinations or not.

        return : Returns true if the animation clip can assign its sources to some destinations, false otherwise. 
        """
        pass

    def Clone(self):
        """
        Clone the clip.

        """
        pass

    def DestinationSetObject(self,pSrcName,pObject):
        """
        Assign source to destination if the pSrcName is found in source list and pObject is in the Details list.

        pSrcName : The name of the source. 
        pObject : The destination object. 
        return : Returns true if assignment has been executed when the pSrcName is found in source list and pObject is in the Details list. 
        """
        pass

    def ExportToFile(self,pOutputFile):
        """
        ExportToFile.
        Export animation clip to disk file.

        pOutputFile : Output file path name. 
        return : Returns true if successful. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetAffectedAnimationNodes(self,pAffectedAnimationNodes,pClipObject):
        """
        GetAffectedAnimationNodes.
        Get the list of animation nodes affected by this story clip, for a specific object.

        pAffectedAnimationNodes : Array of affected animation nodes, will be filled by the function. 
        pClipObject : The object for which we search for affected animation nodes. 
        """
        pass

    def GetAffectedObjects(self,pAffectedObjects):
        """
        GetAffectedObjects.
        Get the list of objects affected by this story clip.

        pAffectedObjects : Array of affected objects, will be filled by the function. 
        """
        pass

    def GetAssignSourcesToDestinationsInfo(self,pSrcList,pAvailableDstList,pDefaultDstList,pEffectiveDstList):
        """
        GetAssignSourcesToDestinationsInfo.
        Returns the information about the current state of Sources to Destinations assignment. The pSrcList, pDefaultDstList & pEffectiveDstList parameters will all be of same size, each index being related to the same index in the other lists. The pAvailableDstList parameter can contains more item than the other lists.

        pSrcList : String list containing all the sources, will be filled by the method. 
        pAvailableDstList : String list containing all the available destinations, will be filled by the method. 
        pDefaultDstList : String list containing the default destinations (contains each string item that will be put back when pressing the 'Reset' button in the UI), will be filled by the method. 
        pEffectiveDstList : String list containing the effective destination (destinations currently active), will be filled by the method. 
        """
        pass

    def GetReadOnly(self):
        """
        GetReadOnly Retrieves the clip read-only status.

        return : Returns the clip read-only status. 
        """
        pass

    def MakeWritable(self):
        """
        MakeWritable.
        Imports FCurves from story clip scene making them accessible for the user.

        return : Returns true if successful. 
        """
        pass

    def Match(self):
        """
        Match.
        Match the animation clip with the specified pivot property.

        """
        pass

    def Match(self,pObjectName,pTimeType,pTranslationType,pRotationType):
        """
        Match.
        Match the animation clip to its previous/next animation clip, one to each other.

        pObjectName : The object name that specifies which part of the track content to use to match clips. If the object name is not valid, or empty, the match object will be disabled so that the blend does not take it into account when matching clips. 
        pTimeType : The time type specifying which point of a cross-blend the selected clip is matched. 
        pTranslationType : The translation type specifying if/how a clip's match object is translated to match another clip's animation. 
        pRotationType : The rotation type specifying if/how a clip's match object is rotated to match another clip's animation. 
        """
        pass

    def Move(self,pDelta,pForce):
        """
        Move.
        Move the clip of a delta offset.

        pDelta : Delta time to apply to the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Return the delta between the new and previous clip's position. 
        """
        pass

    def MoveTo(self,pTime,pForce):
        """
        MoveTo.
        Move the clip to the specified time.

        pTime : Time where to put the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Returns the new clip's time position. 
        """
        pass

    def Razor(self,pTime):
        """
        Razor.
        Cut (razor) the clip at the specified time.

        pTime : Time where to cut. This time is local to the track, not to the clip. 
        return : Returns the new clip generated by the razor action (right part). 
        """
        pass

    def SetAssignSourcesToDestinationsInfo(self,pEffectiveDstList):
        """
        SetAssignSourcesToDestinationsInfo.
        Sets the new effective destinations information for the Sources to Destinations assignment. The input string list size must contain the same number of items than the effective destination list returned by the GetAssignSourcesToDestinationsInfo method. Each item in the input string list must match an item in the available destination list returned by the GetAssignSourcesToDestinationsInfo method. The item at a given index of the input string list will be related to the same index of the sources list returned by the GetAssignSourcesToDestinationsInfo method.

        pEffectiveDstList : String list containing the new effective destination. 
        return : Returns true if the assign succeeded, false otherwise. 
        """
        pass

    def SetReadOnly(self,pMakeClipReadOnly,pOutputFile):
        """
        SetReadOnly Assigns the clip read-only status.

        pMakeClipReadOnly : New read-only status 
        pOutputFile : Output file path name, when setting the clip's read-only status to true. 
        return : Returns true if successful. 
        """
        pass

    def SetTime(self,pSourceIn,pSourceOut,pDestinationIn,pDestinationOut,pUseAlternateSrcInProp):
        """
        SetTime Sets any in/out values for the source/destination times.
        In and out values are optional and the current values for the story clip will be used if not supplied. The story 'Speed' property will be adjusted in order for the supplied values to be respected by the story clip.

        pSourceIn : New value for the source IN time. Passing a value will modify the "MarkIn" and/or the "Speed" properties. 
        pSourceOut : New value for the source OUT time. Passing a value will modify the "MarkOut" and/or the "Speed" properties. 
        pDestinationIn : New value for the destination IN time. Passing a value will modify the "Stop" and/or the "Speed" properties. 
        pDestinationOut : New value for the destination OUT time. Passing a value will modify the "Start" and/or the "Speed" properties. 
        pUseAlternateSrcInProp : Will work on the "ExtractStart" property instead of the "MarkIn" property when passing pSourceIn. 
        """
        pass

    def UpdateFromCurrentTake(self):
        """
        Update clip animation from current take animation for clip track's scope, works only for clip created by Insert Current Take and connected to current take.

        return : Returns true if succeed. 
        """
        pass

    AudioClip=property(doc="<b>Read Only Property:</b> The audio clip used by this StoryClip.          ")
    AutoLoop=property(doc="<b>Read Write Property:</b> If true, clip will automatically loop          ")
    ClipAnimationPath=property(doc="<b>Read Write Property:</b> Animation clip's file path          ")
    ClipAudioPath=property(doc="<b>Read Write Property:</b> Audio clip's file path          ")
    ClipPitch=property(doc="<b>Read Write Property:</b> The clip pitch value.          ")
    ClipVideoPath=property(doc="<b>Read Write Property:</b> Video clip's file path          ")
    Color=property(doc="<b>Read Write Property:</b> Color of the clip.          ")
    ConnectedToTake=property(doc="<b>Read Write Property:</b> When connected to current take, user can do updating from current take, but user can't edit clip animation by adding keys, only works for clips created by Insert Current Take.          ")
    CustomTimeWarp=property(doc="<b>Read Only Property:</b> Animation and Shot clip's custom TimeWarp FCurve.          ")
    FrameRate=property(doc="<b>Read Write Property:</b> Frame rate value. Only effective when UseSystemFrameRate is false.          ")
    Ghost=property(doc="<b>Read Write Property:</b> Show ghosts          ")
    GhostCustomTime=property(doc="<b>Read Write Property:</b> Custom time to display ghost, only applicable if ShowGhostClipMode is kFBStoryClipTimeCustom.          ")
    GhostManipulatorCustomTime=property(doc="<b>Read Write Property:</b> Custom time to display ghost manipulator, only applicable if GhostManipulatorMode is kFBStoryClipGhostCustom.          ")
    GhostManipulatorMode=property(doc="<b>Read Write Property:</b> Time mode to display ghost manipulator. See FBStoryClipGhostTimeMode.          ")
    GhostManipulatorOffset=property(doc="<b>Read Write Property:</b> Animation clip's ghost manipulator offset.          ")
    GhostModel=property(doc="<b>Read Write Property:</b> Show ghost of models          ")
    GhostPivot=property(doc="<b>Read Write Property:</b> Show ghost of match object          ")
    GhostTravelling=property(doc="<b>Read Write Property:</b> Show ghost of clip vector or traveling node          ")
    ImageSequence=property(doc="<b>Read Write Property:</b> Whether is a image sequence.          ")
    Loaded=property(doc="<b>Read Write Property:</b> If true, clip file is loaded into memory and can be evaluated (will affect track content).          ")
    LockPitchToSpeed=property(doc="<b>Read Write Property:</b> Time-stretching enabled or not.          ")
    Loop=property(doc="<b>Read Write Property:</b> If true, loop clip's animation          ")
    LoopTranslation=property(doc="<b>Read Write Property:</b> Animation clip's loop translation.          ")
    MarkIn=property(doc="<b>Read Write Property:</b> Start time inside the clip.          ")
    MarkOut=property(doc="<b>Read Write Property:</b> Stop time inside the clip.          ")
    MirrorAnimation=property(doc="<b>Read Write Property:</b> If true, clip animation will be mirrored          ")
    MirrorPlane=property(doc="<b>Read Write Property:</b> Several mirror planes to mirror animation. See FBStoryClipMirrorPlane          ")
    Offset=property(doc="<b>Read Write Property:</b> First loop time offset.          ")
    OnChange=property(doc="<b>Event:</b> Something in the clip has changed. (FBEventClip)          ")
    Pivots=property(doc="<b>List:</b> Pivots models (Generally, only one model is necessary)          ")
    PostBlend=property(doc="<b>Read Write Property:</b> Start/Stop time of the post-blend phase.          ")
    PreBlend=property(doc="<b>Read Write Property:</b> Start/Stop time of the pre-blend phase.          ")
    Rotation=property(doc="<b>Read Write Property:</b> Animation clip's rotation offset. Refer to class notes to learn more about how this is applied.          ")
    Scale=property(doc="<b>Read Write Property:</b> Animation clip's scaling (some don't support this property)          ")
    ShotActionStart=property(doc="<b>Read Write Property:</b> If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property.          ")
    ShotActionStop=property(doc="<b>Read Write Property:</b> If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property.          ")
    ShotBackplate=property(doc="<b>Read Write Property:</b> The backplate used for that specific shot.          ")
    ShotCamera=property(doc="<b>Read Write Property:</b> The camera used for that specific shot.          ")
    ShotFrontplate=property(doc="<b>Read Write Property:</b> The frontplate used for that specific shot.          ")
    ShotStartStopLocked=property(doc="<b>Read Write Property:</b> Shot clip's 'In/Out Locked' property value. True if the shot clip's In/Out properties (start/stop times of the clip local to its track) are locked, false otherwise.          ")
    ShowBackplate=property(doc="<b>Read Write Property:</b> Enable/Disable the shot backplate.          ")
    ShowEmbeddedTimecode=property(doc="<b>Read Write Property:</b> Whether to show embedded timecode of the clip, if available.          ")
    ShowFrontplate=property(doc="<b>Read Write Property:</b> Enable/Disable the shot frontplate.          ")
    ShowGhostClipMode=property(doc="<b>Read Write Property:</b> Show the ghost depending on the time. See FBStoryClipShowGhostMode          ")
    SolvingMode=property(doc="<b>Read Write Property:</b> Solve Modes for story character clips. See FBStoryClipSolveMode          ")
    Speed=property(doc="<b>Read Write Property:</b> Speed of the clip.          ")
    Start=property(doc="<b>Read Write Property:</b> Start time of the clip local to its track.          ")
    StartStopLocked=property(doc="<b>Read Write Property:</b> Clip's 'In/Out Locked' property value. True if the clip's In/Out properties (start/stop times of the clip local to its track) are locked, false otherwise.          ")
    Stop=property(doc="<b>Read Write Property:</b> Stop time of the clip local to its track.          ")
    TimeWarpEnabled=property(doc="<b>Read Write Property:</b> Animation and Shot clip's TimeWarp activeness.          ")
    TimeWarpInterpolatorType=property(doc="<b>Read Write Property:</b> Animation and Shot clip's TimeWarp interpolation type. See FBStoryClipTimeWarpInterpolatorType.          ")
    TimeWarpReverse=property(doc="<b>Read Write Property:</b> If true, reverse the Animation or Shot clip's TimeWarp FCurve.          ")
    Translation=property(doc="<b>Read Write Property:</b> Animation clip's translation offset. Refer to class notes to learn more about how this is applied.          ")
    TravellingNode=property(doc="<b>List:</b> Travelling node(s). If set, this property will overwrite the Track's Travelling node(s).          ")
    TravellingNodeFunction=property(doc="<b>Read Write Property:</b> Travelling node function. If set, this property will overwrite the Track's Travelling node function. See FBStoryClipNodeFunction.          ")
    UseSystemFrameRate=property(doc="<b>Read Write Property:</b> Whether always use system frame rate.          ")
    pass

class FBStoryFolder (FBComponent):
    """
    Story Folder class.     
     With folders, you can group tracks together and create different timelines. See sample: FBStoryFolder.py.     
    """
    def FBStoryFolder(self,pParentFolder):
        """
        Constructor.

        pParentFolder : If NULL, parent will be the global root folder, according to its type. 
        """
        pass

    def AlignSelectedClips(self,pType,pReferenceClip):
        """
        Used to align selected clips .

        pType : Type of alignment that will be done. 
        pReferenceClip : Needed when kFBStoryClipAlignmentEndPreviousAllAligned, kFBStoryClipAlignmentBeginningNextAllAligned or kFBStoryClipAlignmentCurrentTimelineWithOffset are used. 
        """
        pass

    def AlignSelectedClipsGroup(self,pType):
        """
        Used to align clips inside a group.

        pType : Type of alignment that will be done. 
        """
        pass

    def ConvertClipsToReadOnly(self,pSelected,pFilePath):
        """
        Convert all clips to read-only clips.
        Identical clips are replaced by the same read-only clip.

        pSelected : Only selected clip will be converted. 
        pFilePath : Folder path where the read-only clips will be saved. 
        """
        pass

    def ExpandSelectedClips(self,pPreserveOverlap):
        """
        Used to expand selected clips .

        pPreserveOverlap : If true, portion of clips that overlap other clips won't be modified. 
        """
        pass

    def ExpandSelectedClipsGroup(self,pPreserveOverlap):
        """
        ExpandSelectedClipsGroup Used to expand group clip dependent clips.

        pPreserveOverlap : If true, portion of clips that overlap other clips won't be modified. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Load(self,pLoad):
        """
        Allow to load/unload all story clips under this folder.

        pLoad : bool
        """
        pass

    Childs=property(doc="<b>List:</b> Children folders of this folder.          ")
    Collapsed=property(doc="<b>Read Write Property:</b> Toggle to collapse or expand the story folder.          ")
    Label=property(doc="<b>Read Write Property:</b> Label to display for this story folder.          ")
    Mute=property(doc="<b>Read Write Property:</b> If true, this story folder will be muted.          ")
    Parent=property(doc="<b>Read Only Property:</b> Object pointing to the folder's parent.          ")
    RecordClipPath=property(doc="<b>Read Write Property:</b> Path for story recording. Can be relative or full path.          ")
    Solo=property(doc="<b>Read Write Property:</b> If true, this story folder will be the only one to play.          ")
    Tracks=property(doc="<b>List:</b> Tracks of this folder.          ")
    pass

class FBStoryGroupClip (FBComponent):
    """
    Story Group Clip class.     
     Group Clip represents a group of clips that can be manipulated together.      
    """
    def FBStoryGroupClip(self,pAffectedClipObject):
        """
        Constructor.

        pAffectedClipObject : Clips that will be controlled by the group clip. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Move(self,pDelta,pForce):
        """
        Move.
        Move the clip of a delta offset.

        pDelta : Delta time to apply to the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Return the delta between the new and previous clip's position. 
        """
        pass

    def MoveTo(self,pTime,pForce):
        """
        MoveTo.
        Move the clip to the specified time.

        pTime : Time where to put the clip. 
        pForce : Force clip to find the nearest position if the move fail. 
        return : Returns the new clip's time position. 
        """
        pass

    def Razor(self,pTime):
        """
        Razor.
        Cut (razor) the clip at the specified time.

        pTime : Time where to cut. This time is local to the track, not to the clip. 
        """
        pass

    DependentClips=property(doc="<b>Read Write Property:</b> Clips that are included in the group clip.          ")
    Start=property(doc="<b>Read Write Property:</b> Start time of the clip.          ")
    StartStopLocked=property(doc="<b>Read Write Property:</b> Clip's 'In/Out Locked' property value. True if the clip's In/Out properties (start/end times of the clip local to its track) are locked, false otherwise.          ")
    Stop=property(doc="<b>Read Write Property:</b> Stop time of the clip.          ")
    pass

class FBTake (FBComponent):
    """
    A take is a container for animation in a scene.     
     A take stores data about animation for objects. The transport controls (FBPlayerControl) act on the current take.In the UI transport controls, a take's start and end determine when the Timeline indicator starts and stops.You get the current take with FBSystem::CurrentTake, as in the following Python sample: 
@code
for myTake in FBSystem().Scene.Takes:
print myTake.Name
@endcode

To create a take and have it accessible in the Transport control you could use CopyTake (called Duplicate in the UI):Python sample code:  
@code
from pyfbsdk import *    
newTake = FBSystem().CurrentTake.CopyTake('my new take name')
@endcode

C++ sample code: 
@code
FBTake* lTake = FBSystem::ThenOne().CurrentTake->CopyTake( 'my new take' );    
@endcode

Or simply create a new empty take like the following:Python sample code:  
@code
from pyfbsdk import *    
newTake = FBTake('my new take name')
FBSystem().Scene.Takes.append(newTake)
@endcode

C++ sample code: 
@code
FBSystem::TheOne()::Scene.Takes.Add( new FBTake( 'my new take' ));
@endcode

See samples: MergePreviewAnimationLayers.py, ExportAnimationLibrary.py, GoToNextTake.py, GoToPreviousTake.py, MirrorPoseOverTime.py, MultiLayerKeying.py, RenameFirstTakeOnMultipleFiles.py, SaveOneTakePerFile.py, TimeCodeKeying.py.     
    """
    def FBTake(self,pName):
        """
        Constructor.

        pName : Name of take. 
        """
        pass

    def AddTimeMark(self,pTime,pName):
        """
        Add a time mark to the take.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.

        pTime : Time where to add the time mark on the take. 
        pName : Name of the time mark to add. 
        return : The index of the time mark added if the operation is successful, -1 otherwise. 
        """
        pass

    def ClearAllProperties(self,pOnSelectedObjectsOnly,pOnLockedProperties):
        """
        Clear the animation on all the properties.

        pOnSelectedObjectsOnly : Specify if clear will be performed on all objects or only on the one that are currently selected. 
        pOnLockedProperties : Specify if clear will be performed on locked properties as well. 
        """
        pass

    def ClearAllPropertiesOnCurrentLayer(self):
        """
        Clear all the animation on the current layer.

        """
        pass

    def CopyTake(self,pNewTakeName):
        """
        Copy the take.
        Will create a copy of the current take, with the current take data. This is analogous to creating a new take, and copying the current take data into it. The Layers data and the TimeWarp date will be copied. The newly created take will be set as the current take. The newly created take is automatically added to the scene and available in the Transport control.

        pNewTakeName : The name for the new take. 
        return : Handle to the newly created take. 
        """
        pass

    def CreateNewLayer(self):
        """
        Create a new layer.

        """
        pass

    def DeleteAllTimeMarks(self):
        """
        Delete all time marks from the take.

        """
        pass

    def DeleteAnimation(self,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties):
        """
        Delete animation (FCurve keys) of this take object within a time range.

        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers. 
        pOnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties. 
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def DeleteAnimationOnObjects(self,pObjects,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties):
        """
        Delete animation (FCurve keys) of this take object on given objects within a time range.

        pObjects : Objects affected by the delete operation. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers. 
        pOnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties. 
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def DeleteAnimationOnProperties(self,pProperties,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties,pPropertyComponents):
        """
        Delete animation (FCurve keys) of this take object on given properties within a time range.

        pProperties : Properties affected by the delete operation. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers. 
        pOnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties. 
        pPropertyComponents : The component bit field considered when performing the delete operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property. 
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def DeleteTimeMark(self,pIndex):
        """
        Delete a time mark from the take.
        Note: Internally, the time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.

        pIndex : Index of the time mark to delete. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def DuplicateSelectedLayers(self):
        """
        Duplicate the selected layers.
        This is equivalent of doing a copy-paste.

        """
        pass

    def FBDelete(self):
        """
        Deletion method.
        Using this method to delete the take insure that the destruction process follows the same path as if the GUI had been used.

        """
        pass

    def GetCurrentLayer(self):
        """
        Get the current layer for the take.

        return : The current layer index. 
        """
        pass

    def GetLayer(self,pLayerIndex):
        """
        Get the layer object that have the specified ID.

        pLayerIndex : The index of the layer that will be returned. 
        return : Layer with the specified ID. 
        """
        pass

    def GetLayerByName(self,pName):
        """
        Get the layer object that have the specified name.

        pName : The name of the animation layer to get. 
        return : Layer with the specified name or NULL if no layer has been found. 
        """
        pass

    def GetLayerCount(self):
        """
        Get the layer count.

        return : The layer count. 
        """
        pass

    def GetLayerRealSelection(self):
        """
        Real selection for layer.
        Check the SetLayerRealSelection function for more information about this.

        return : True if selecting a layer will also select the FBComponent of that layer. 
        """
        pass

    def GetNextTimeMarkIndex(self):
        """
        Returns the next time mark index, based on the current local time.

        return : The next time mark index, -1 if any next time mark is available. 
        """
        pass

    def GetPreviousTimeMarkIndex(self):
        """
        Returns the previous time mark index, based on the current local time.

        return : The previous time mark index, -1 if any previous time mark is available. 
        """
        pass

    def GetTimeMarkAction(self,pIndex):
        """
        Returns the action associated with a time mark.

        pIndex : Index of the time mark. 
        return : The action associated with the time mark. 
        """
        pass

    def GetTimeMarkColor(self,pIndex):
        """
        Returns the color associated with a time mark.

        pIndex : Index of the time mark. 
        return : The color associated with the time mark. 
        """
        pass

    def GetTimeMarkCount(self):
        """
        Returns the number of time marks on the take.

        return : The number of time marks on the take. 
        """
        pass

    def GetTimeMarkName(self,pIndex):
        """
        Returns the name associated with a time mark.

        pIndex : Index of the time mark. 
        return : The name associated with the time mark. 
        """
        pass

    def GetTimeMarkTime(self,pIndex):
        """
        Returns the time associated with a time mark.

        pIndex : Index of the time mark. 
        return : The time associated with the time mark. 
        """
        pass

    def MergeLayers(self,pMergeOptions,pDeleteMergedLayers,pMergeMode,pMergeLockedProperties):
        """
        Merge the selected layers.
        This is equivalent of pressing the merge button in the Animation Layer editor.

        pMergeOptions : Indicate which objects, layers and properties (selected or all) should be merged. 
        pDeleteMergedLayers : The source layer will be deleted after the merge if no animation is left on those layers, or if those layers are not parent of another layer. 
        pMergeMode : Set the layer mode of the resulting layer, if possible (the BaseAnimation layer cannot be modified). 
        pMergeLockedProperties : The properties will be merged even if they are locked. 
        """
        pass

    def MoveCurrentLayerDown(self):
        """
        Move the current layer down, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.

        return : True if successful. 
        """
        pass

    def MoveCurrentLayerUp(self):
        """
        Move the current layer up, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.

        return : True if successful. 
        """
        pass

    def OffsetAnimation(self,pOffsetTime,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties):
        """
        Offset the animation (FCurve keys) of this take object within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.

        pOffsetTime : The offset time to apply. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers. 
        pOnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties. 
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def OffsetAnimationOnObjects(self,pObjects,pOffsetTime,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties):
        """
        Offset the animation (FCurve keys) of this take object on given objects within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.

        pObjects : Objects affected by the offset operation. 
        pOffsetTime : The offset time to apply. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers. 
        pOnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties. 
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def OffsetAnimationOnProperties(self,pProperties,pOffsetTime,pStartTime,pStopTime,pInclusive,pLayerID,pOnLockedProperties,pPropertyComponents):
        """
        Offset the animation (FCurve keys) of this take object on given properties within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.

        pProperties : Properties affected by the offset operation. 
        pOffsetTime : The offset time to apply. 
        pStartTime : Start of time range. 
        pStopTime : End of time range. 
        pInclusive : True to include within the time range the keys at pStartTime and pStopTime, false otherwise. 
        pLayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers. 
        pOnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties. 
        pPropertyComponents : The component bit field considered when performing the offset operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property. 
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.). 
        """
        pass

    def PlotAllTakesOnObjects(self,pPlotPeriod,pObjectsToPlot):
        """
        Plot the animation on given objects for all takes.
        This method will plot the animation of all takes to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.

        pPlotPeriod : Period for the plot. 
        pObjectsToPlot : Objects to plot. 
        """
        pass

    def PlotAllTakesOnProperties(self,pPlotPeriod,pPropertiesToPlot):
        """
        Plot the animation on given properties for all takes.
        Will plot the animation for all takes on the given properties in the scene.

        pPlotPeriod : Period for the plot. 
        pPropertiesToPlot : Properties to plot. 
        """
        pass

    def PlotAllTakesOnSelected(self,pPlotPeriod):
        """
        Plot the animation on selected models for all takes.
        Will plot the animation for all takes on the selected models in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotAllTakesOnSelectedProperties(self,pPlotPeriod):
        """
        Plot the animation on selected properties for all takes.
        Will plot the animation for all takes on the selected properties in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotTakeOnObjects(self,pPlotOptions,pObjectsToPlot):
        """
        Plot the animation on given objects.
        This method will plot the animation of the take to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.

        pPlotOptions : Option parameters for plotting 
        pObjectsToPlot : Objects to plot. 
        """
        pass

    def PlotTakeOnObjects(self,pPlotPeriod,pObjectsToPlot):
        """
        Plot the animation on given objects.
        This method will plot the animation of the take to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.

        pPlotPeriod : Period for the plot. 
        pObjectsToPlot : Objects to plot. 
        """
        pass

    def PlotTakeOnProperties(self,pPlotPeriod,pPropertiesToPlot):
        """
        Plot the animation on given properties.
        Will plot the animation of the take in question on the given properties in the scene.

        pPlotPeriod : Period for the plot. 
        pPropertiesToPlot : Properties to plot. 
        """
        pass

    def PlotTakeOnSelected(self,pPlotOptions):
        """
        Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.

        pPlotOptions : Option parameters for plotting 
        """
        pass

    def PlotTakeOnSelected(self,pPlotPeriod):
        """
        Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def PlotTakeOnSelectedProperties(self,pPlotOptions):
        """
        Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.

        pPlotOptions : Option parameters for plotting 
        """
        pass

    def PlotTakeOnSelectedProperties(self,pPlotPeriod):
        """
        Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.

        pPlotPeriod : Period for the plot. 
        """
        pass

    def RemoveLayer(self,pLayerIndex):
        """
        Remove a layer.

        pLayerIndex : Layer with at the specified index will be removed. 
        """
        pass

    def SetCurrentLayer(self,pLayerIndex):
        """
        Set the current layer for the take.
        Note that this will not deselect the other layers.

        pLayerIndex : The layer index to be set as the current one. 
        """
        pass

    def SetLayerRealSelection(self,pValue):
        """
        Set real selection for layer.
        This method is used to specify if using the SelectLayer method of the FBAnimationLayer object will also select the FBComponent object. In previous version of MotionBuilder, an animation layer was always selected, causing the layer to be displayed in the property editor. Also, when parsing the selected objects in the SDK, a layer would always be there. Setting this value to false will prevent this.

        pValue : True if future layer selection will also select the FBComponent object. 
        """
        pass

    def SetTimeMarkAction(self,pIndex,pAction):
        """
        Sets a new action for an existing time mark.

        pIndex : Index of the time mark. 
        pAction : The new action for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetTimeMarkColor(self,pIndex,pColor):
        """
        Sets a new color for an existing time mark.

        pIndex : Index of the time mark. 
        pColor : The new color for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetTimeMarkName(self,pIndex,pName):
        """
        Sets a new name for an existing time mark.

        pIndex : Index of the time mark. 
        pName : The new name for the time mark. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetTimeMarkTime(self,pIndex,pTime):
        """
        Sets a new time for an existing time mark.
        Note: Internally, the time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.

        pIndex : Index of the time mark. 
        pTime : The new time for the time mark. 
        return : The new index of the modified time mark. 
        """
        pass

    Comments=property(doc="<b>Read Write Property:</b> Take comments.          ")
    LocalTimeSpan=property(doc="<b>Read Write Property:</b> Local time span.          ")
    ReferenceTimeSpan=property(doc="<b>Read Write Property:</b> Reference time span.          ")
    pass

class FBTimeWarpManager (FBComponent):
    """
    Time Warp Manager Interface to the Time Warp Manager.     
    See sample: TimeWarp.py.     
    """
    def FBTimeWarpManager(self):
        """
        Constructor.

        """
        pass

    def ApplyTimeWarp(self,pTake,pEvalProp,pTimeWarp):
        """
        Apply the TimeWarp in a Take to an evaluation property, just connect the storing property for the TimeWarp to the evaluation property.

        pTake : The Take where the TimeWarp in. 
        pEvalProp : The evaluation property to be applied on. 
        pTimeWarp : The TimeWarp to apply. 
        return : True if apply successfully. 
        """
        pass

    def DestroyTimeWarpFromTake(self,pTake,pTimeWarp):
        """
        Destroy the TimeWarp in a Take, and removed from the DataSet.

        pTake : The Take where the TimeWarp in. 
        pTimeWarp : The TimeWarp to be Destroyed. 
        """
        pass

    def FindTimeWarpNickNumberGlobal(self,pTimeWarp):
        """
        Find the Nick Number of one timewarp globally.

        pTimeWarp : The TimeWarp queried. 
        return : the Nick Number of the timewarp. 
        """
        pass

    def GetTimeWarpAtIndex(self,pTake,pIndex):
        """
        Get the TimeWarp in a Take At specific Index.

        pTake : The Take queried. 
        pIndex : The index of the TimeWarp. 
        return : TimeWarp at specific Index in a Take. 
        """
        pass

    def GetTimeWarpCount(self,pTake):
        """
        Get the count of TimeWarp in a Take.

        pTake : The Take queried. 
        return : the TimeWarp count. 
        """
        pass

    def GetTimeWarpFromNickNumber(self,pTake,pNumber):
        """
        Get the timeWarp of specific Nick Number in a Take.

        pTake : The Take queried. 
        pNumber : the Nick Number of one TimeWarp. 
        return : the TimeWarp of specific Nick Number. 
        """
        pass

    def GetTimeWarpNickNumber(self,pTake,pTimeWarp):
        """
        Get the Nick Number of one TimeWarp in a Take.

        pTake : The Take queried. 
        pTimeWarp : The TimeWarp queried. 
        return : the Nick Number of one TimeWarp. 
        """
        pass

    def GetTimeWarpNickNumberAtIndex(self,pTake,pIndex):
        """
        Get the Nick Number of one TimeWarp At specific index in a Take.

        pTake : The Take queried. 
        pIndex : The index a TimeWarp at. 
        return : the Nick Number of one TimeWarp At specific index. 
        """
        pass

    def RemoveTimeWarp(self,pTake,pEvalProp):
        """
        Undo apply a timeWarp in a Take to an evaluation property, just disconnect the evaluation property from storing property.

        pTake : The Take where the TimeWarp evaluation property connected is in. 
        pEvalProp : The evaluation property connected a TimeWarp in the storing property of one take. 
        """
        pass

    def RemoveTimeWarpFromScene(self,pTimeWarp):
        """
        Remove a TimeWarp from Scene.

        pTimeWarp : The TimeWarp to be Removed. 
        """
        pass

    def SetTimeWarpNickNumber(self,pTake,pTimeWarp,pNumber):
        """
        Set the Nick Number of one TimeWarp in a Take.

        pTake : The Take specific. 
        pTimeWarp : The TimeWarp specific. 
        pNumber : The Nick Number to set. 
        return : True if set successfully. 
        """
        pass

    def TimeWarpAddToTake(self,pTake,pTimeWarp,pNickNumber):
        """
        Add one TimeWarp to a Take.

        pTake : The Take one TimeWarp added to. 
        pTimeWarp : The TimeWarp to be added. 
        pNickNumber : The Nick Number for the TimeWarp. 
        """
        pass

    def TimeWarpClearTake(self,pTake):
        """
        Clear all TimeWarp in a Take, and removed from the DataSet.

        pTake : The Take to be cleared. 
        """
        pass

    def TimeWarpCopyTake(self,pDstTake,pSrcTake):
        """
        Copy all the TimeWarp in one Take, add to another Take.

        pDstTake : Copy all TimeWarp to. 
        pSrcTake : Copy all TimeWarp from. 
        """
        pass

    def TimeWarpCreateNew(self,pName):
        """
        Create a TimeWarp with a specific name.

        pName : The name for the TimeWarp. 
        return : the TimeWarp created. 
        """
        pass

    def TimeWarpInitTake(self,pTake):
        """
        Allocate container for the TimeWarp in one Take.

        pTake : The Take allocated for. 
        """
        pass

    def TimeWarpMergeCurveNode(self,pTake,pEvalProp,pNode,pTimeWarpNode):
        """
        Merge the TimeWarp to a function curve, and Remove the connection between the storing property and the evaluation property for the TimeWarp.

        pTake : The Take that the TimeWarp is in. 
        pEvalProp : the evaluation property the TimeWarp connected. 
        pNode : The function curve to merge on. 
        pTimeWarpNode : The TimeWarp to be merged. 
        """
        pass

    def TimeWarpRename(self,pTake,pTimeWarp,pNewName):
        """
        Rename a TimeWarp.

        pTake : The Take where the timeWarp is in. 
        pTimeWarp : The TimeWarp to be renamed. 
        pNewName : The new name for the TimeWarp. 
        """
        pass

    def TimeWarpTakeChange(self):
        """
        Call registered callbacks when changes related to TimeWarp happen.

        """
        pass

    pass

class FBTool (FBLayout):
    """
    Tool class.     
    See samples: MBFileRefDemo.py, CloseTool.py, MoveResizeToolExample.py, SafeToolCreationExample.py, ToolCommunicationReceiver.py, ToolNativeWidgetHolder.py.     
    """
    def FBTool(self,pName):
        """
        Constructor.

        pName : Name of tool. 
        """
        pass

    def FBTool(self,pName,pRegisterTool):
        """
        Constructor used when creating tools not in the Tools menu of MotionBuilder.

        pName : Name of tool, must be an unique name. 
        pRegisterTool : Tells if we should register the tool on the toolmanager. You can later call Showtool to pop it. 
        """
        pass

    def GetPossibleDockPosition(self):
        """
        Get the possible docking position for the tool (concatenated).

        return : Get all the docking flags in one call. Flags can be concatenated. 
        """
        pass

    def SetPossibleDockPosition(self,pFlags):
        """
        Set the possible docking position for the tool.
        Be sure to call this function once the tool is visible, a good place to call it is when the OnShow event of the layout is called.

        pFlags : Set the docking position flag values. Note: this function overwrites all flags with those passed in parameter. 
        """
        pass

    StartSizeX=property(doc="<b>Read Property:</b> Starting Size. This is the initial size in X when the tool is opened. Default = 800         ")
    StartSizeY=property(doc="<b>Read Property:</b> Starting Size. This is the initial size in Y when the tool is opened. Default = 400         ")
    MaxSizeX=property(doc="<b>Read Property:</b> Maximum Size in X (Disabled in this version). A value of -1 means no maximum size.         ")
    MaxSizeY=property(doc="Maximum Size in Y (Disabled in this version). A value of -1 means no maximum size.         ")
    MinSizeX=property(doc="<b>Read Property:</b> Minimum Size in X. A value of -1 means no minimum value.         ")
    MinSizeY=property(doc="<b>Read Property:</b> Minimum Size in Y. A value of -1 means no minimum value.         ")
    StartPosX=property(doc="<b>Read Property:</b> Starting Position in X. This is the initial position when the tool is opened. Default = 450         ")
    StartPosY=property(doc="<b>Read Property:</b> Starting Position in Y. This is the initial position when the tool is opened. Default = 450         ")
    ToolName=property(doc="<b>Read Property:</b> Tool Name         ")
    DisplayName=property(doc="<b>Read Write Property:</b> Tool Display Name (Caption on the tool's title bar)          ")
    pass

class FBToolLayoutManager (FBComponent):
    """
    Tool Layout Manager class.     
     <b>This class allows users to interact with Layouts.</b>Sample Python code: 
@code
from pyfbsdk import *

lToolLayoutMan = FBToolLayoutManager()

# Delete all existing custom layout
for i in range( lToolLayoutMan.GetCustomLayoutCount() ):
    lToolLayoutMan.DeleteLayout( lToolLayoutMan.GetCustomLayoutCount() - 1 )

# Create a new layout
lToolLayoutMan.CreateLayout( 'MyLayout' )

# Print the names of all the factory layouts
print 'Factory layouts:'
print '----------------'
for aLayoutIdx in range(lToolLayoutMan.GetFactoryLayoutCount()):
    print lToolLayoutMan.GetLayoutName(-aLayoutIdx-1)

# Print the names of all the custom layouts
print ''
print 'Custom layouts:'
print '----------------'
for aLayoutIdx in range(lToolLayoutMan.GetCustomLayoutCount()):
    print lToolLayoutMan.GetLayoutName(aLayoutIdx)

# Set the Scripting Layout
lToolLayoutMan.SetCurrentLayout( -2 )

# Delete the custom layout
lToolLayoutMan.DeleteLayout( 'MyLayout' )
@endcode

     
    """
    def CreateLayout(self,pLayoutName):
        """
        Create a new layout from the current layout state.

        pLayoutName : The new layout name to create. 
        return : The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise. 
        """
        pass

    def DeleteLayout(self,pLayoutIdx):
        """
        Delete the layout associated with the given layout index.
        Deleting a factory layout is not permitted.

        pLayoutIdx : The layout index to delete. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def DeleteLayout(self,pLayoutName):
        """
        Delete the layout with the given layout name.
        Deleting a factory layout is not permitted.

        pLayoutName : The layout name to delete. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def GetAutoUpdateLayout(self):
        """
        Get the 'Auto-update Layout' state value.

        return : The 'Auto-update Layout' state value. 
        """
        pass

    def GetCurrentLayoutIdx(self):
        """
        Get the layout index of the current layout.

        return : The layout index of the current layout. 
        """
        pass

    def GetCurrentLayoutName(self):
        """
        Get the name of the current layout.

        return : The name of the current layout. 
        """
        pass

    def GetCustomLayoutCount(self):
        """
        Get the number of custom layouts.

        return : The number of custom layouts. 
        """
        pass

    def GetFactoryLayoutCount(self):
        """
        Get the number of factory layouts.

        return : The number of factory layouts. 
        """
        pass

    def GetLayoutName(self,pLayoutIdx):
        """
        Get the layout name associated with the given layout index.

        pLayoutIdx : The layout index to query. The factory layouts are using negative indices. 
        return : The layout name if the operation is successful, nullptr (C++) or None (Python) otherwise. 
        """
        pass

    def RenameLayout(self,pOldLayoutName,pNewLayoutName):
        """
        Rename a layout.
        Renaming a factory layout is not permitted.

        pOldLayoutName : The layout's name to rename. 
        pNewLayoutName : The new layout name. 
        return : The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise. 
        """
        pass

    def SetAutoUpdateLayout(self,pAutoUpdate):
        """
        Set the 'Auto-update Layout' state value.

        pAutoUpdate : The 'Auto-update Layout' state value. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetCurrentLayout(self,pLayoutIdx):
        """
        Set the current layout from the given layout index.

        pLayoutIdx : The layout index to set as the current layout. The factory layouts are using negative indices. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetCurrentLayout(self,pLayoutName):
        """
        Set the current layout from the given layout name.

        pLayoutName : The layout's name to set as the current layout. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def UpdateCurrentLayout(self):
        """
        Update the current layout from the current layout state.
        Updating a factory layout is not permitted.

        return : True if the operation is successful, false otherwise. 
        """
        pass

    pass

class FBTransportAudioManager (FBComponent):
    """
    Transport Tool Audio Manager class.     
     <b>This class allows users to interact with the Audio Manager of the Transport Tool.</b>      
    """
    def GetAudioClip(self):
        """
        Get the Audio Clip displayed on the Transport Tool.

        return : The Audio Clip displayed, nullptr (C++) / None (Python) if any. 
        """
        pass

    def GetAudioTrack(self):
        """
        Get the Audio Track displayed on the Transport Tool.

        return : The Audio Track displayed, nullptr (C++) / None (Python) if any. 
        """
        pass

    def GetLockPitchToSpeed(self):
        """
        Get the 'Lock Pitch to Speed' state.

        return : True if the 'Lock Pitch to Speed' state is set, false otherwise. 
        """
        pass

    def GetShowAudio(self):
        """
        Get the 'Show Audio' state.

        return : True if the 'Show Audio' state is set, false otherwise. 
        """
        pass

    def GetShowLeftChannel(self):
        """
        Get the 'Show Left Channel' state.

        return : True if the 'Show Left Channel' state is set, false otherwise. 
        """
        pass

    def GetShowRightChannel(self):
        """
        Get the 'Show Right Channel' state.

        return : True if the 'Show Right Channel' state is set, false otherwise. 
        """
        pass

    def RemoveAudio(self):
        """
        Remove the audio clip or audio track currently displayed on the Transport Tool.

        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetAudioClip(self,pAudioClip):
        """
        Set the Audio Clip to display on the Transport Tool.

        pAudioClip : The Audio Clip to display. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetAudioTrack(self,pAudioTrack):
        """
        Set the Audio Track to display on the Transport Tool.

        pAudioTrack : The Audio Track to display. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetLockPitchToSpeed(self,pLock):
        """
        Set the 'Lock Pitch to Speed' state.

        pLock : True to lock pitch to speed, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowAudio(self,pShow):
        """
        Set the 'Show Audio' state.

        pShow : True to show the Audio waveform, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowLeftChannel(self,pShow):
        """
        Set the 'Show Left Channel' state.

        pShow : True to show the left channel, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetShowRightChannel(self,pShow):
        """
        Set the 'Show Right Channel' state.

        pShow : True to show the right channel, false otherwise. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    pass

class FBTreeNode (FBComponent):
    """
    A node in the tree view.     
         
    """
    def FBTreeNode(self,pTree):
        """
        Constructor.

        pTree : Parent tree. 
        """
        pass

    Checked=property(doc="<b>Read Write Property:</b> Is FBTreeNode checked.          ")
    Reference=property(doc="<b>Read Write Property:</b> Data to be associated to this node.          ")
    pass

class FBUndoManager (FBComponent):
    """
    Access to global undo and redo functionality.     
     Users have the possibility of undoing and redoing actions performed using the GUI, and interacting with the undo and redo stacks with custom actions.All undo/redo related functions should only be called inside UI event callback. Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.This class cannot be used as a base class. See sample: IndividualUndoCalls.py.     
    """
    def FBUndoManager(self):
        """
        Constructor.

        """
        pass

    def ActiveOperation(self):
        """
        Determine if an undo operation is in action.

        return : true the Undo Manager is performing an Undo or a Redo operation. 
        """
        pass

    def Clear(self):
        """
        Clear the undo and redo stacks.

        return : A boolean value indicating success (true) or failure (false). 
        """
        pass

    def Redo(self):
        """
        Redo last undone action.

        """
        pass

    def TransactionAddModelTRS(self,pModel):
        """
        Add Transaction if transaction stack is open.
        Quick Function to add Model TRS in Undo Stack

        pModel : Model to backup TRS 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionAddObjectDestroy(self,pObject):
        """
        Add Transaction if transaction stack is open.
        Function to add object to destroy in Undo Stack. No need to call FBDelete() on the object after calling this function.

        pObject : Object to backup 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionAddProperty(self,pProperty):
        """
        Add Transaction if transaction stack is open.
        Quick Function to add property value in Undo Stack

        pProperty : Property to backup 
        return : true if add transaction successfully. 
        """
        pass

    def TransactionBegin(self,pTransactionName):
        """
        Open transaction stack for adding transactions.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.

        pTransactionName : Name of Transaction. 
        return : true if open transaction stack successfully. 
        """
        pass

    def TransactionEnd(self):
        """
        Close transaction stack.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.

        return : true if transaction close successfully. 
        """
        pass

    def TransactionIsOpen(self):
        """
        Query if transaction stack is already open.

        return : true if transaction is already open. 
        """
        pass

    def Undo(self,pNoRedo):
        """
        Undo last action.

        pNoRedo : If true, once the action is undone, it cannot be redone. 
        """
        pass

    OnRedo=property(doc="<b>Event:</b> A redo operation will be executed.          ")
    OnRedoCompleted=property(doc="<b>Event:</b> A redo operation has been executed.          ")
    OnUndo=property(doc="<b>Event:</b> An undo operation will be executed.          ")
    OnUndoCompleted=property(doc="<b>Event:</b> An undo operation has been executed.          ")
    pass

class FBVideoGrabber (FBComponent):
    """
    Video Grabber class.     
     Used to grab video frames generated with the FBRenderer. See samples: codecExamples.py, render.py, RenderLayers.py, JpegRender.py.     
    """
    def FBVideoGrabber(self):
        """
        Constructor.

        """
        pass

    def BeginGrab(self):
        """
        BeginGrab.
        Begin video grabbing session.

        return : <b>True</b> if we can begin the grab session. 
        """
        pass

    def EndGrab(self):
        """
        EndGrab.
        Close video grabbing session.

        """
        pass

    def GetLastErrorMsg(self):
        """
        GetLastErrorMsg.

        return : If an error occured, this function returns the last error message, otherwise an empty string. 
        """
        pass

    def GetOptions(self):
        """
        GetOptions give you a copy of current grabbing options.

        return : Struct that contain all grabbing options.
        """
        pass

    def GetStatistics(self):
        """
        GetStatistics.

        return : Struct that contain all grabbing statistics. 
        """
        pass

    def Grab(self):
        """
        Grab.
        Grab all specified video frames.

        """
        pass

    def RenderSnapshot(self,pWidth,pHeight,pCameraLabel,pTimeCode,pSafeArea,pAxis,pGrid,pFrontPlate,pBackPlate):
        """
        Render a snapshot of the actual display.

        pWidth : int
        pHeight : int
        pCameraLabel : bool
        pTimeCode : bool
        pSafeArea : bool
        pAxis : bool
        pGrid : bool
        pFrontPlate : bool
        pBackPlate : bool
        return : An FBimage containing data of the rendered snapshot. 
        """
        pass

    def ResetOptions(self):
        """
        SetDefaultOptions.
        This function reset all grabbing options to the default value.

        """
        pass

    def SetOptions(self,pOptions):
        """
        SetOptions.

        pOptions : Struct that contain all grabbing options. 
        """
        pass

    pass

class FBAssetFile (FBAssetItem):
    """
    Class representing a file stored in a version control database.     
         
    """
    def FBAssetFile(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def GetCheckedOutBy(self):
        """
        Returns the name of the user who currently has this file checked out.

        return : The user name if the file is checked out, or an empty string if it is not. 
        """
        pass

    def IsCheckedOut(self):
        """
        Returns a boolean value indicating if this file is checked out by any user.

        return : A boolean value indicating if this node is checked out. 
        """
        pass

    def IsCheckedOutByMe(self):
        """
        Returns a boolean value indicating if this file is checked out by the current user.

        return : A boolean value indicating if this node is checked out by the current user. 
        """
        pass

    pass

class FBAssetFolder (FBAssetItem):
    """
    Class representing a folder stored in a version control database.     
         
    """
    def FBAssetFolder(self,pName):
        """
        Constructor.

        pName : Name of Command. 
        """
        pass

    def AddFile(self,pLocalPath,pComment,pCheckOut,pSilent):
        """
        Add a specified file into the database.
        It will be added in this folder.

        pLocalPath : The full path to the file on the local disk. 
        pComment : Comment to be applied for the operation. 
        pCheckOut : Whether the file should be checked out or not. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : An FBAssetfile* object representing the newly added file. 
        """
        pass

    def AddFolder(self,pName,pComment,pSilent):
        """
        Add a folder in the database.
        It will be added in this folder.

        pName : Name of the folder to be created. 
        pComment : Comment to be applied for the operation. 
        pSilent : If pSilent is set to true, no dialog will be displayed by this method. 
        return : An FBAssetFolder* object representing the newly added folder. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def GetChild(self,pIndex):
        """
        Get the child at index <b>pIndex</b>.

        pIndex : int
        return : The child at <b>pIndex</b>, or NULL if the index was out of range. 
        """
        pass

    def GetChildCount(self):
        """
        Get the number of items in this folder.

        return : The number of items in this folder. 
        """
        pass

    def GetFile(self,pName):
        """
        Get a file present in this folder by using it's name.

        pName : str
        return : The file with the given name, or NULL if it was not found. 
        """
        pass

    def GetFolder(self,pName):
        """
        Get a folder present in this folder by using it's name.

        pName : str
        return : The folder with the given name, or NULL if it was not found. 
        """
        pass

    pass

class FBBoxPlaceHolder (FBBox):
    """
    Wrapper around a specific instance of a FBBox object.     
     This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying box. The underlying box will usually be a device. Instantiation of FBBoxPlaceHolder should be left to the the system.      
    """
    def FBBoxPlaceHolder(self):
        """
        Constructor.

        """
        pass

    Box=property(doc="<b>Read Only Property:</b> Underlying box object.          ")
    pass

class FBCharacterExtension (FBKeyingGroup):
    """
    Objects Grouping class.     
     This class is an interface to manipulate object's grouping in the scene. See sample: CreateCharacterExtensionOnSelectedObject.py.     
    """
    def FBCharacterExtension(self,pName):
        """
        Constructor.

        pName : Group name. 
        """
        pass

    def AddObjectProperties(self,pObj):
        """
        Add TR Properties from Object.

        pObj : Object to add TR properties. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def GetCharacter(self):
        """
        Return the attached Character.

        return : attached Character. 
        """
        pass

    def GetExtensionObjectWithLabelName(self,pLabelName):
        """
        Find stored object based on label name.

        pLabelName : The label name. 
        return : The extension object. 
        """
        pass

    def GetLabelNameWithExtensionObject(self,pLabelName,pObj,pReturnObjectNameIfNotFound):
        """
        Find the label name that was used to store object pose.

        pLabelName : The label name that was used to store object pose. 
        pObj : The extension object. 
        pReturnObjectNameIfNotFound : If the value is true, if the object is not found, pLabelName will be set to the object name; otherwise pLabelName will be set to empty string. By default the value is false. 
        """
        pass

    def GetMirrorExtension(self):
        """
        Return the character extension determined by MirrorLabel.

        return : character extension determined by MirrorLabel. 
        """
        pass

    def GetRetargetPropertyCount(self):
        """
        Return the total number of retarget properties.

        return : The total number of retarget properties. 
        """
        pass

    def GetRetargetReferenceProperty(self,pPropIndex):
        """
        Return the reference property of the given index.

        pPropIndex : Index to query. 
        return : Reference property of the given index. 
        """
        pass

    def GetRetargetSourceProperty(self,pPropIndex):
        """
        Return the source property of the given index (the source property is the property that drives the reference property during retargeting).

        pPropIndex : Index to query. 
        return : Source property (the property that drives the reference property during retargeting) of the given index. 
        """
        pass

    def GetSourceExtension(self):
        """
        Return the character extension that is used to drive this extension during retargeting.

        return : The character extension that is used to drive this extension during retargeting. 
        """
        pass

    def GetSourceExtensionIndex(self):
        """
        Return the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.

        return : The enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character. 
        """
        pass

    def GetStancePose(self):
        """
        Return stance pose.

        return : stance pose. 
        """
        pass

    def GoToStancePose(self):
        """
        Reset object position to the stance.

        """
        pass

    def IsElementSelected(self):
        """
        Return true if one object in object dependency list is selected.

        return : true if one object in object dependency list is selected. 
        """
        pass

    def IsPropertyIncluded(self,pProp):
        """
        Return true if the property is in character extension.

        pProp : Property to check. 
        return : true if the property is in character extension. 
        """
        pass

    def RemoveObjectAndProperties(self,pObj):
        """
        Remove TR Properties from Object.

        pObj : Object to remove TR properties. 
        """
        pass

    def RemoveRetargetSourceProperty(self,pPropIndex):
        """
        Remove the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.

        pPropIndex : Index to remove. 
        """
        pass

    def SetRetargetSourceProperty(self,pPropIndex,pSourceProp):
        """
        Set the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.

        pPropIndex : Index to set. 
        pSourceProp : Source property to set. 
        """
        pass

    def SetSourceExtension(self,pSourceExtension):
        """
        Set the character extension to drive this extension during retargeting.
        Only applicable if RetargetMode is Assign.

        pSourceExtension : The source extension to drive this extension during retargeting. 
        """
        pass

    def SetSourceExtensionIndex(self,pSrcExtIndex):
        """
        Set the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.
        Only applicable if RetargetMode is Manually Assign.

        pSrcExtIndex : Enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character. 
        """
        pass

    def UpdateStancePose(self):
        """
        Update the stance pose to the current position of the character extension element.

        """
        pass

    IncludePartInBodyPart=property(doc="<b>Read Write Property:</b> Include or not this extension when the Body Part mode is active.          ")
    IncludePartInFullBody=property(doc="<b>Read Write Property:</b> Include or not this extension when the Full Body mode is active.          ")
    Label=property(doc="<b>Read Write Property:</b> The logical name of the extension, use for mirroring.          ")
    MirrorLabel=property(doc="<b>Read Write Property:</b> Enum that indicate which extension is used as mirror, 0 is none, 1 is self, 2-n represent the (ith - 2)character extension in the attached character excluding self.          ")
    PlotAllowed=property(doc="<b>Read Write Property:</b> Controls if objects in the set are transformable.          ")
    ReferenceModel=property(doc="<b>Read Write Property:</b> Controls the referential of the extension.          ")
    RetargetMode=property(doc="<b>Read Write Property:</b> Character extension retarget mode.          ")
    StancePoseMode=property(doc="<b>Read Write Property:</b> Character extension stance pose mode.          ")
    SyncActivationAndVisibilityMode=property(doc="<b>Read Write Property:</b> The 'Sync Activation & Visibility' mode.          ")
    pass

class FBCharacterPose (FBPose):
    """
    Used to work with character poses.     
     This class exposes the object used to store the pose of objects. See sample: MirrorPoseOverTime.py.     
    """
    def FBCharacterPose(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. 
        """
        pass

    def ApplyPoseCandidate(self):
        """
        After setting the candidate on the skeleton node, calling this function will allow subsequent call to get the TRS value of a skeleton node to return the candidate value.

        """
        pass

    def ClearCharacterExtensionsPose(self):
        """
        Clear only the pose of the character extensions (omit the character).

        """
        pass

    def ClearCharacterPose(self):
        """
        Clear only the pose of the character (omit the extensions).

        """
        pass

    def ClearPose(self):
        """
        Clear all the data of the pose.

        """
        pass

    def CopyFrom(self,pFromPose):
        """
        Copy everything from a given object.

        pFromPose : Pose from which to copy. 
        """
        pass

    def CopyPose(self,pCharacter):
        """
        Copy the pose of a character and its extensions.

        pCharacter : Character to copy the pose from. 
        """
        pass

    def CopyPoseCharacter(self,pCharacter):
        """
        Copy the pose of only the character (omit the extensions).

        pCharacter : Character to copy the pose from. 
        """
        pass

    def CopyPoseCharacterExtension(self,pCharacterExtension):
        """
        Copy the pose of a single character extension.

        pCharacterExtension : Character extension to copy the pose from. 
        """
        pass

    def CopyPoseCharacterExtensions(self,pCharacter):
        """
        Copy the pose of only the character extensions (omit the character).

        pCharacter : Character to copy the pose of the extensions from. 
        """
        pass

    def CopyPoseCharacterExtensionsFrom(self,pFromPose):
        """
        Copy the pose data of only the character extensions from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseCharacterFrom(self,pFromPose):
        """
        Copy the pose data of only the character from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseDataFrom(self,pFromPose):
        """
        Copy all the pose data from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def GetCharacterExtensionNameFromPose(self,pCharacterExtensionPose):
        """
        Get the name of the character extension for the specified pose.

        pCharacterExtensionPose : Pose of a character extension to check its name. 
        return : The name of the character extension (It is the label name of the character extension). 
        """
        pass

    def GetCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Get the pose of a character extension.

        pCharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension). 
        return : The pose of the character extension, NULL if not found. 
        """
        pass

    def GetCharacterExtensionPoseAt(self,pIndex):
        """
        Get the pose of a character extension.

        pIndex : Index of the character extension pose to get. 
        return : The pose of the character extension. 
        """
        pass

    def GetCharacterExtensionPoseCount(self):
        """
        Get the number of character extension stored in the pose.

        return : Number of character extension stored in the pose. 
        """
        pass

    def GetExtraBoneParentRotationOffset(self,pR,pIndex):
        """
        Get the extra bone transformation offset.

        pR : A vector that will contains the parent rotation offset value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetExtraBoneTransform(self,pT,pR,pS,pIndex):
        """
        Get the extra bone transformation.

        pT : A vector that will contains the translation value on return. 
        pR : A vector that will contains the rotation value on return. 
        pS : A vector that will contains the scale value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetExtraBoneTransformOffset(self,pT,pR,pS,pIndex):
        """
        Get the extra bone transformation offset.

        pT : A vector that will contains the translation offset value on return. 
        pR : A vector that will contains the rotation offset value on return. 
        pS : A vector that will contains the scale offset value on return. 
        pIndex : Index of the extra bone to get. 
        """
        pass

    def GetMirrorPlaneEquation(self,pMirrorPlaneEquation,pCharacter,pCharacterPoseOptions):
        """
        Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.

        pMirrorPlaneEquation : Out: Mirror plane equation. 
        pCharacter : Character to receive the pose. 
        pCharacterPoseOptions : Options used to paste the pose. 
        """
        pass

    def GetMirrorPlaneEquation(self,pMirrorPlaneEquation,pCharacter,pCharacterPoseOptions):
        """
        Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.

        pMirrorPlaneEquation : Out: Mirror plane equation. 
        pCharacter : Character to receive the pose. 
        pCharacterPoseOptions : Options used to paste the pose. 
        """
        pass

    def GetOrCreateCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Get the pose of a character extension and create it if necessary.

        pCharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension). 
        return : The pose of the character extension. 
        """
        pass

    def IsCharacterExtensionPoseStored(self,pCharacterExtensionName):
        """
        Is the pose of the character extension stored in the pose?

        pCharacterExtensionName : Name of the character extension. 
        return : <b>true</b> if the pose of the character extension stored in the pose. 
        """
        pass

    def IsCharacterPoseStored(self):
        """
        Is the pose of the character stored in the pose?

        return : <b>true</b> if the pose of the character stored in the pose. 
        """
        pass

    def PastePose(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of a character and its extensions.

        pCharacter : Character to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacter(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of only the character (omit the extensions).

        pCharacter : Character to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacterExtension(self,pCharacterExtension,pCharacterPoseOptions):
        """
        Paste the pose of a single character extension.

        pCharacterExtension : Character extension to paste the pose to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def PastePoseCharacterExtensions(self,pCharacter,pCharacterPoseOptions):
        """
        Paste the pose of only the character extensions (omit the character).

        pCharacter : Character to paste the pose of the extensions to. 
        pCharacterPoseOptions : Options used to specify how to paste. 
        """
        pass

    def RemoveCharacterExtensionPose(self,pCharacterExtensionName):
        """
        Remove the pose of a character extension.

        pCharacterExtensionName : Name of the character extension pose to remove (It is the label name of the character extension). 
        """
        pass

    def RemoveCharacterExtensionPoseAt(self,pIndex):
        """
        Remove the pose of a character extension.

        pIndex : Index of the character extension pose to remove. 
        """
        pass

    pass

class FBConstraint (FBBox):
    """
    Base class for constraints.     
         
    """
    def FBConstraint(self,pName):
        """
        Constructor.

        pName : Name of constraint. 
        """
        pass

    def AnimationNodeInCreate(self,pUserId,pModel,pAttribute):
        """
        pUserId : kReference
        pModel : FBModel
        pAttribute : str
        """
        pass

    def AnimationNodeInCreate(self,pUserId,pProperty):
        """
        Animation Node Creations (IN).
        Used to create the In connectors on an animation node. This function will return a newly created animation node, connected to the model specified by <b>pProperty</b>.

        pUserId : User specified reference number. 
        pProperty : Property of model to animate (must be animatable) 
        return : Newly created IN animation node. 
        """
        pass

    def AnimationNodeOutCreate(self,pUserId,pModel,pAttribute):
        """
        Animation Node Creations (IN/OUT).
        Used to create the connectors (in or out) on an animation node. This function will return a newly created animation node, connected to the model specified by <b>pModel</b>.

        pUserId : User specified reference number. 
        pModel : Model to associate with animation node. 
        pAttribute : Attribute of model to animate (i.e. Translation, Lcl Translation, etc.) 
        return : Newly created IN/OUT animation node. 
        """
        pass

    def Clone(self):
        """
        Clone the constraint.

        return : Newly created (and copied) constraint. 
        """
        pass

    def DeformerBind(self,pModel):
        """
        Bind/Unbind <b>pModel</b> to deformation constraint.
        These functions are used for adding/removing a deformation binding to/from <b>pModel</b> if the constraint is a deformation constraint.

        pModel : Model to bind/unbind. 
        return : <b>true</b> if successful. 
        """
        pass

    def DeformerUnBind(self,pModel):
        """
        pModel : FBModel
        """
        pass

    def Disable(self,pModel):
        """
        Disable constraint on <b>pModel</b>.

        pModel : Model on which constraint should be disabled. 
        return : <b>true</b> if successful. 
        """
        pass

    def FreezeSRT(self,pModel,pS,pR,pT):
        """
        Freeze current model state.

        pModel : Model to freeze constraint on. 
        pS : Scaling freeze? 
        pR : Rotation freeze? 
        pT : Translation freeze? 
        """
        pass

    def FreezeSuggested(self):
        """
        Suggest 'freeze'.

        """
        pass

    def ReferenceAdd(self,pGroupIndex,pModel):
        """
        Add a reference to a specified group.

        pGroupIndex : Group to add reference to. 
        pModel : Model to place at new reference. 
        return : <b>true</b> if successful. 
        """
        pass

    def ReferenceGet(self,pGroupIndex,pItemIndex):
        """
        Get a reference.

        pGroupIndex : Index of reference group containing desired reference. 
        pItemIndex : Index of reference in group to get (default is 0). 
        return : Model at specified reference. 
        """
        pass

    def ReferenceGetCount(self,pGroupIndex):
        """
        Get number of references in a specified group.

        pGroupIndex : Index of group to query the number of references. 
        return : Number of references in specified group. 
        """
        pass

    def ReferenceGroupAdd(self,pGroupName,pMaxItemCount):
        """
        Add a group of references.

        pGroupName : Name of reference group to add. 
        pMaxItemCount : Maximum number of items in <b>pGroupName</b>. 
        return : Index of new reference group. 
        """
        pass

    def ReferenceGroupGetCount(self):
        """
        Return the number of reference groups.

        return : Number of reference groups. 
        """
        pass

    def ReferenceGroupGetMaxCount(self,pGroupIndex):
        """
        Get the maximum number of items that can exist in the reference group in question.

        pGroupIndex : Index of reference group. 
        return : Maximum number of items that can be added to the reference group. 
        """
        pass

    def ReferenceGroupGetName(self,pGroupIndex):
        """
        Get the name of the reference group.

        pGroupIndex : Index of the reference group to get the name for. 
        return : The name of the reference group <b>pGroupIndex</b>. 
        """
        pass

    def ReferenceRemove(self,pGroupIndex,pModel):
        """
        Remove a reference to <b>pModel</b> from the group at <b>pGroupIndex</b>.

        pGroupIndex : Index to remove reference from. 
        pModel : Model to remove reference from. 
        return : <b>true</b> if successful. 
        """
        pass

    def RemoveAllAnimationNodes(self):
        """
        Remove animation nodes.

        """
        pass

    def RestoreModelState(self,pModel):
        """
        Restore the saved model state onto <b>pModel</b>.

        pModel : Model to affect with previous state. 
        """
        pass

    def SaveModelState(self,pModel,pS,pR,pT):
        """
        Save current state of <b>pModel</b>.

        pModel : Model to save. 
        pS : Scaling information? 
        pR : Rotation information? 
        pT : Translation information? 
        """
        pass

    def SetupAllAnimationNodes(self):
        """
        Setup animation nodes.

        """
        pass

    def SnapSuggested(self):
        """
        Suggest 'snap'.

        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Active state.          ")
    Deformer=property(doc="<b>Read Write Property:</b> Is a deformer constraint?          ")
    Description=property(doc="<b>Read Write Property:</b> Long description of constraint.          ")
    HasLayout=property(doc="<b>Read Write Property:</b> Does the constraint have a layout?          ")
    Lock=property(doc="<b>Read Write Property:</b> Lock state.          ")
    Snap=property(doc="<b>Function Property:</b> Snap constraint.          ")
    Weight=property(doc="<b>Read Write Property:</b> Weight of constraint.          ")
    pass

class FBCycleAnalysisNode (FBBox):
    """
    Cycle Analysis class.     
         
    """
    def FBCycleAnalysisNode(self,pName):
        """
        Constructor.

        pName : Name of new cycle analysis node. 
        """
        pass

    def GetPoseFCurve(self):
        """
        """
        pass

    def GetRootHFCurve(self):
        """
        """
        pass

    def GetRootRFCurve(self):
        """
        """
        pass

    def GetRootSpeedFCurve(self):
        """
        """
        pass

    def GetRootXZFCurve(self):
        """
        """
        pass

    RealTime=property(doc="<b>Read Only Property:</b> Real time.          ")
    RootHMode=property(doc="<b>Read Only Property:</b> RootH Mode.          ")
    RootRMode=property(doc="<b>Read Only Property:</b> RootR Mode.          ")
    RootSpeedMode=property(doc="<b>Read Only Property:</b> Root Speed Mode.          ")
    RootXZMode=property(doc="<b>Read Only Property:</b> RootXZ Mode.          ")
    pass

class FBDeformerPointCache (FBDeformer):
    """
    Base Model deformer class.     
         
    """
    def FBDeformerPointCache(self,pName):
        """
        Constructor.

        pName : Name of deformer. 
        """
        pass

    Active=property(doc="<b>Read Write Property:</b> Active.          ")
    ChannelCount=property(doc="<b>Read Only Property:</b> Channel Count.          ")
    ChannelEnd=property(doc="<b>Read Only Property:</b> Channel End.          ")
    ChannelFrameRate=property(doc="<b>Read Only Property:</b> Channel FrameRate.          ")
    ChannelIndex=property(doc="<b>Read Write Property:</b> Channel Index.          ")
    ChannelName=property(doc="<b>Read Only Property:</b> Channel Name.          ")
    ChannelPointCount=property(doc="<b>Read Only Property:</b> Channel Point Count.          ")
    ChannelSampleRegular=property(doc="<b>Read Only Property:</b> Channel Sample Regular.          ")
    ChannelStart=property(doc="<b>Read Only Property:</b> Channel Start.          ")
    PointCacheFile=property(doc="<b>Read Write Property:</b> Point Cache File Object.          ")
    pass

class FBDevice (FBBox):
    """
    Base Device class.     
    Cannot be instantiated from Python. See samples: StartDevice.py, StopDevice.py.     
    """
    def FBDevice(self,pName):
        """
        Constructor.

        pName : Name of device. 
        """
        pass

    def AckOneBadSampleReceived(self):
        """
        Acknowlege that one <b>bad</b> sample was received (for statistical purposes).

        """
        pass

    def AckOneSampleReceived(self):
        """
        Acknowlege that one sample was received (for statistical purposes).

        """
        pass

    def AckOneSampleSent(self):
        """
        Acknowlege that one sample was sent (for statistical purposes).

        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def FBDestroy(self):
        """
        Open Reality destruction function.

        """
        pass

    def ModelBindingCreate(self):
        """
        Create a new model binding.

        return : <b>The</b> model root that has been created or NULL is an error occured. 
        """
        pass

    def ModelBindingRootsList(self,pList):
        """
        Get the list of all the possible root models for binding.

        pList : List to add found models to. 
        """
        pass

    def RecordingDoneAnimation(self,pAnimationNode):
        """
        When recording, finish animation.

        pAnimationNode : Animation node to write information to. 
        """
        pass

    def RecordingInitAnimation(self,pAnimationNode):
        """
        When recording, initialize animation.

        pAnimationNode : Animation node to read information from. 
        """
        pass

    CommType=property(doc="<b>Read Write Property:</b> Type of communications.          ")
    HardwareVersionInfo=property(doc="<b>Read Write Property:</b> Device information: hardware version.          ")
    Information=property(doc="<b>Read Write Property:</b> Device information: information.          ")
    ModelBindingRoot=property(doc="<b>Component:</b> Root of model currently binded model hierarchy.          ")
    ModelTemplate=property(doc="<b>Component:</b> Root of model template structure.          ")
    Online=property(doc="<b>Read Write Property:</b> Is online?          ")
    RecordingStartTime=property(doc="<b>Read Only Property:</b> The time at which the recording started.          ")
    RecordingStopTime=property(doc="<b>Read Only Property:</b> The time at which the recording stopped.          ")
    SamplingMode=property(doc="<b>Read Write Property:</b> Mode to use to record device.          ")
    SamplingPeriod=property(doc="<b>Read Write Property:</b> Set this to how many times a device is to be evaluated in one second. There is no theoretical maximum value but practically you should consider scene complexity, system resources, network speed, etc. If set to 0: the device is evaluated on the sync signal. When the sync occurs; the device is scheduled to be evaluated. If you do not set, the sampling period is based on the internal variable from the [Sync] section of the .Application.txt file (NTSC, PAL, CINEMA).          ")
    Status=property(doc="<b>Read Write Property:</b> Device information: status.          ")
    pass

class FBFileReference (FBNamespace):
    """
    Objects Containing class.     
     This class is an interface to manipulate object's containing in the scene. See sample: MBFileRefDemo.py.     
    """
    def FBFileReference(self,pSingleLevelNamespace,pParentNSObj):
        """
        Constructor.
        Create a new direct children FileReference object

        pSingleLevelNamespace : FileReference name. This name will be used as namespace itself. this name string shouldn't contain namespace string separator ":". 
        pParentNSObj : the parent namespace object. if NULl means to create top level namespace. 
        """
        pass

    def ApplyRefEditPyScriptFromFile(self,pRefEditPyScriptFilePath):
        """
        Apply specified reference edits from python script file.

        pRefEditPyScriptFilePath : Reference edits Python script file path. 
        """
        pass

    def ApplyRefEditPyScriptFromString(self,pRefEditPyScript):
        """
        Apply specified reference edits from Python script string.

        pRefEditPyScript : Reference edits Python script. 
        """
        pass

    def BakeRefEditToFile(self,pFilePath):
        """
        Save the current status of the referenced content back to disk.
        If pFilePath is ReferenceFilePath, we're saving all the modification back to the original referenced file. Otherwise, we will export the referenced file plus modification to another file.

        pFilePath : File path to export. 
        return : true if successful. 
        """
        pass

    def ClearAllRefEdit(self):
        """
        Clear all cached Ref edit.

        return : <b>True</b> if the RefEdits are cleared properly. 
        """
        pass

    def ClearRefEdit(self,pFilePath):
        """
        Clear the cached RefEdit for the given ref file path.

        pFilePath : The Ref File Path to query against, default to be current Ref File. 
        return : <b>True</b> if the RefEdit for the given Ref File Path is cached and cleared properly. 
        """
        pass

    def DuplicateFileRef(self,pDstNameSpaceList,pWithRefEdit):
        """
        Duplicate/Clone the FileRef object and its referenced content (with/without refEdit).

        pDstNameSpaceList : the list of target new namespace(s) for duplication. These new namespace(s) must be residing in editable scene segments. 
        pWithRefEdit : false by default, duplication won't include the existing ref edit. otherwise ref edit will be applied on the instantiated FileRef in someway. 
        return : true if successful, false is fail. 
        """
        pass

    def GetRefEdit(self,pFilePath):
        """
        Return the RefEdit for given RefFile Path.

        pFilePath : The Ref File Path to query against, default to be current Ref File. 
        return : RefEdit as string  
        """
        pass

    def GetRefFileList(self,pRefFileList):
        """
        Return a list of ref file path which has cached Ref Edit.

        pRefFileList : the output parameter to collect the Ref File Path. 
        """
        pass

    def RevertRefEdit(self,pPlug,pModificationFlag):
        """
        Revert the modification on the referenced object/property to original state.

        pPlug : the plug to revert, revert all if NULL. 
        pModificationFlag : the modification type to revert. 
        """
        pass

    def SwapReferenceFilePath(self,pFilePath,pApplyAvailableRefEdit,pMergeCurrentRefEdit):
        """
        Swap the Ref File Path and apply ref edit.

        pFilePath : The new Ref File path to be used 
        pApplyAvailableRefEdit : Apply the cached Ref Edit (if exist) for the Ref File to be used if <b>True</b>. 
        pMergeCurrentRefEdit : Merge the current RefEdit to if <b>True</b> if the reference items' name are matching. 
        return : <b>True</b> if swap successfully. 
        """
        pass

    IsLoaded=property(doc="<b>Read Write Property: </b> File Reference Load/Unload.          ")
    ReferenceFilePath=property(doc="<b>Read Write Property: </b> File Reference file path.          ")
    pass

class FBGlobalLight (FBBox):
    """
    Global light class.     
         
    """
    AmbientColor=property(doc="<b>Read Write Property:</b> Ambient light color.          ")
    FogBegin=property(doc="<b>Read Write Property:</b> Begin fog distance.          ")
    FogColor=property(doc="<b>Read Write Property:</b> Fog color.          ")
    FogDensity=property(doc="<b>Read Write Property:</b> Fog density.          ")
    FogEnable=property(doc="<b>Read Write Property:</b> Enable fog?          ")
    FogEnd=property(doc="<b>Read Write Property:</b> End fog distance.          ")
    FogMode=property(doc="<b>Read Write Property:</b> Fog falloff mode.          ")
    pass

class FBGroup (FBBox):
    """
    Objects Grouping class.     
     This class is an interface to manipulate object's grouping in the scene. See samples: FBGetSelectedModels.py, FBGroup.py.     
    """
    def FBGroup(self,pName):
        """
        Constructor.

        pName : Group name. 
        """
        pass

    def Clone(self):
        """
        Clone the group.
        This will duplicated the current group.

        return : Newly created group. 
        """
        pass

    def Contains(self,pComponent):
        """
        Contains.

        pComponent : Component to verify if it is in the Group 
        return : True if the object is in the Group 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Select(self,pSelect):
        """
        Select.

        pSelect : If <b>true</b>, group contents will be selected. 
        """
        pass

    Items=property(doc="<b>List:</b> Items in the group.          ")
    Pickable=property(doc="<b>Read Write Property:</b> Controls if objects in the group are pickable.          ")
    Show=property(doc="<b>Read Write Property:</b> Controls if objects in the group are displayed.          ")
    Transformable=property(doc="<b>Read Write Property:</b> Controls if objects in the group are transformable.          ")
    pass

class FBHandle (FBBox):
    """
    FBHandle class exposes the Handle object of the application.     
     This is a terminal class and should not be used as a base for a new class.      
    """
    def FBHandle(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. 
        """
        pass

    def Select(self):
        """
        Meta selection.
        With this method, the handle itself is selected as well as all the models that are manipulated by the handle.

        """
        pass

    Follow=property(doc="<b>List:</b> Object to be followed by the handle. Should have a cardinality of 1.          ")
    Image=property(doc="<b>List:</b> Image to be used in the handle display. Only the image at position 0 is used.          ")
    Manipulate=property(doc="<b>List:</b> Objects manipulated by the handle.          ")
    ManipulateRotation=property(doc="<b>List:</b> Objects manipulated by the handle. Only their rotation is affected.          ")
    ManipulateScaling=property(doc="<b>List:</b> Objects manipulated by the handle. Only their scaling is affected.          ")
    ManipulateTranslation=property(doc="<b>List:</b> Objects manipulated by the handle. Only their translation is affected.          ")
    pass

class FBHUD (FBBox):
    """
    Heads Up display.     
     Display scene related information to the screen. This information will also be present in the rendered frames when creating AVIs or QuickTime files. See samples: BloopSlate.py, HUDElements.py, HUDTextElement.py, RecordLight.py, Timeline.py, HUD.py.     
    """
    def FBHUD(self,pName):
        """
        Constructor.

        pName : Name of new HUD. 
        """
        pass

    def CreateCustomElement(self,pHUDElementClassName,pName):
        """
        Creates a custom HUD Element.

        pHUDElementClassName : The HUD Element class name (mainly, the ClassName parameter of the FBStorableCustomHUDElementImplementation macro). 
        pName : Name for the custom HUD Element to create. 
        return : The created custom HUD Element. 
        """
        pass

    def CreateElement(self,pType,pName):
        """
        Creates a stock HUD Element.

        pType : View to be called for expose. 
        pName : Name for the HUD Element to create. 
        return : The created HUD Element. 
        """
        pass

    Elements=property(doc="<b>List:</b> Elements present in the HUD.          ")
    HUDs=property(doc="<b>List:</b> HUDS attached to this HUD.          ")
    OnDisplay=property(doc="<b>Event:</b> Callback just before HUD is displayed to update custom values          ")
    Visibility=property(doc="<b>Read Write Property:</b> Indicate if the information will be displayed or not.          ")
    pass

class FBHUDElement (FBBox):
    """
    Heads Up display.     
     Display scene related information on a camera output. Rendered on video out, output renderings.      
    """
    Height=property(doc="<b>Read Write Property:</b> Specifies the height of HUD element on the screen. It's in pixel when ScaleByPercent is false and percentage when ScaleByPercent is true.          ")
    HorizontalDock=property(doc="<b>Read Write Property:</b> Specifies if the HUD element will be horizontally docked to the Left, Right, or Center.          ")
    Justification=property(doc="<b>Read Write Property:</b> Specifies if the justification of the HUD element is Left, Right, or Center.          ")
    PositionByPercent=property(doc="<b>Read Write Property:</b> When set to true, X and Y position values are in percentage, relative to the corresponding camera view dimension. Otherwise, they are absolute pixel values.          ")
    ScaleByPercent=property(doc="<b>Read Write Property:</b> When set to true, Scale is in percentage, relative to the corresponding camera view dimension. Otherwise, it is an absolute value.          ")
    ScaleUniformly=property(doc="<b>Read Write Property:</b> Specifies whether the width and height of HUD element will be scaled uniformly according to the initial aspect ratio.          ")
    Show=property(doc="<b>Read Write Property:</b> Specifies if the HUD element will be displayed or not.          ")
    VerticalDock=property(doc="<b>Read Write Property:</b> Specifies if the HUD element will be vertically docked to the Bottom, Top, or Center.          ")
    Visibility=property(doc="        ")
    Width=property(doc="<b>Read Write Property:</b> Specifies the width of HUD element on the screen. It's in pixel when ScaleByPercent is false and percentage when ScaleByPercent is true.          ")
    X=property(doc="<b>Read Write Property:</b> Specifies the horizontal position of the HUD element, relative to dock position and justification.          ")
    Y=property(doc="<b>Read Write Property:</b> Specifies the vertical position of the HUD element, relative to dock position and justification.          ")
    pass

class FBMaterial (FBBox):
    """
    Material class.     
    See samples: MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py.     
    """
    def FBMaterial(self,pName):
        """
        Constructor.

        pName : Name of material. 
        """
        pass

    def Clone(self):
        """
        Clone the material.
        This will duplicated the current material.

        return : Newly created material. 
        """
        pass

    def GetTexture(self,pType):
        """
        Retrieve associated texture.

        pType : MaterialTextureType to get connected texture from (default is Diffuse is not specified). 
        """
        pass

    def OGLInit(self):
        """
        Setup OpenGL fixed pipeline material settings.

        """
        pass

    def SetTexture(self,pTexture,pType):
        """
        Set associated texture.

        pTexture : texture to be connected. 
        pType : MaterialTextureType to set connected texture to. 
        """
        pass

    Ambient=property(doc="<b>Read Write Property:</b> Ambient color.          ")
    AmbientFactor=property(doc="<b>Read Write Property:</b> Ambient Factor value.          ")
    Bump=property(doc="<b>Read Write Property:</b> Bump.          ")
    BumpFactor=property(doc="<b>Read Write Property:</b> Bump Factor value.          ")
    Diffuse=property(doc="<b>Read Write Property:</b> Diffuse color.          ")
    DiffuseFactor=property(doc="<b>Read Write Property:</b> Diffuse Factor value.          ")
    DisplacementColor=property(doc="<b>Read Write Property:</b> Displacement color.          ")
    DisplacementFactor=property(doc="<b>Read Write Property:</b> Displacement Factor value.          ")
    Emissive=property(doc="<b>Read Write Property:</b> Emissive color.          ")
    EmissiveFactor=property(doc="<b>Read Write Property:</b> Emissive Factor value.          ")
    NormalMap=property(doc="<b>Read Write Property:</b> Normal Map.          ")
    Reflection=property(doc="<b>Read Write Property:</b> Reflection color.          ")
    ReflectionFactor=property(doc="<b>Read Write Property:</b> Reflection Factor value.          ")
    Shininess=property(doc="<b>Read Write Property:</b> Shininess value.          ")
    Specular=property(doc="<b>Read Write Property:</b> Specular color.          ")
    SpecularFactor=property(doc="<b>Read Write Property:</b> Specular Factor value.          ")
    TransparencyFactor=property(doc="<b>Read Write Property:</b> Transparency Factor value.          ")
    TransparentColor=property(doc="<b>Read Write Property:</b> Transparent color.          ")
    pass

class FBMesh (FBGeometry):
    """
    Mesh class.     
    See samples: GeometryInstancing.py, VertexArrayManipulation.py, VertexColor.py.     
    """
    def FBMesh(self,pName):
        """
        Constructor.

        pName : Name of Mesh. 
        """
        pass

    def ComputeVertexNormals(self,pCW):
        """
        Compute Mesh Vertex Normal.

        pCW : <b>True</b> for clock wise normal, otherwise for counter-clock wise 
        """
        pass

    def InverseNormal(self):
        """
        Inverse Normal.

        """
        pass

    def IsTriangleMesh(self):
        """
        Determines if the mesh is composed entirely of triangles.

        return : true if all polygons are triangles, false otherwise 
        """
        pass

    def PolygonBegin(self,pMaterialId):
        """
        Begin Polygon definition.

        pMaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode. 
        return : Number of existing polygons in Mesh 
        """
        pass

    def PolygonCount(self):
        """
        Get number of polygons in mesh.

        return : Number of polygons in mesh. 
        """
        pass

    def PolygonEnd(self):
        """
        End Polygon definition.
        Clean up and associate vertices internally.

        return : Current number of polygons. 
        """
        pass

    def PolygonListAdd(self,pPolygonSize,pIndexArraySize,pIndexArray,pMaterialId):
        """
        Add Polygon List Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.

        pPolygonSize : Size of polygon, 3 mean triangle, 4 for quadrilateral, and so on. minimum input value is 3.  
        pIndexArraySize : Size of pIndexArray, Added polygon count is floor(max(pIndexArraySize, 0) / pPolygonSize) 
        pIndexArray : Index array of triangle strip. 
        pMaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode. 
        """
        pass

    def PolygonMaterialIdGet(self,pIndex):
        """
        Get a Material ID for the given Polygon index.

        pIndex : Polygon's index to get material ID at (default=-1). 
        return : ID of material of vertex at pIndex. 
        """
        pass

    def PolygonVertexAdd(self,pVertex):
        """
        Add a vertex.

        pVertex : Index in mesh of vertex to add to polygon, must be in range of [0, ControlPointCount) 
        return : <b>true</b> if successful. 
        """
        pass

    def PolygonVertexArrayGet(self,pArraySize):
        """
        Get the array of polygon vertex (i.e.
        index to control points). This array is a concatenation of the list of polygon vertices of all the polygons. Example: a mesh made of 2 triangles [1,2,3] and [2,3,4] results in [1,2,3,2,3,4]. The first polygon starts at position 0 and the second at position 3.

        pArraySize : Polygon vertex array size. 
        return : Readonly polygon vertex array. 
        """
        pass

    def PolygonVertexCount(self,pPolygonIndex):
        """
        Get Polygon vertex count.

        pPolygonIndex : Index of polygon to get vertex count from. 
        return : Number of vertices in polygon at pPolygonIndex. 
        """
        pass

    def PolygonVertexIndex(self,pPolygonIndex,pVertexPolygonIndex):
        """
        Get global (for the mesh) index of a vertex from a polygon.

        pPolygonIndex : Index of polygon in question. 
        pVertexPolygonIndex : Polygon vertex index. 
        return : Index in mesh of vertex. 
        """
        pass

    def TriangleListAdd(self,pIndexArraySize,pIndexArray,pMaterialId):
        """
        Add Triangle List, Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.

        pIndexArraySize : Size of pIndexArray, Added triangle count is floor(max(pIndexArraySize, 0) / 3) 
        pIndexArray : Index array of triangle list. 
        pMaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode. 
        """
        pass

    def TriangleStripAdd(self,pIndexArraySize,pIndexArray,pMaterialId):
        """
        Add Triangle Strip Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.

        pIndexArraySize : Size of pIndexArray, Added triangle count is max(pIndexArraySize - 2, 0) 
        pIndexArray : Index array of triangle strip. 
        pMaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode. 
        """
        pass

    pass

class FBModel (FBBox):
    """
    Model class.     
     In the MotionBuilder UI, a model can be any object in a scene, created using geometry. Models can represent simple objects like cubes, or complex objects like characters.FBModel is a base class which is not used so much directly, but is the parent of well-used classes like FBCamera, FBLight, and FBModelMarker.It also implements a number of widely-implemented functions and attributes, such as: Clone(), FBDelete() UI attributes such as Show, Pickable, and Visibility Positional attributes such as Rotation, Scaling, and Translation The following Python snippet shows how to create, show, rotate, and delete a cube 
@code
from pyfbsdk import *
myCube = FBModelCube('cube')
myCube.Show = True
myCube.Rotation = FBVector3d(45, 45, 45)
myCube.FBDelete()
@endcode

There is a few ways to get a handle on existing models in a scene: FBFindObjectsByName return a list of objects matching a pattern (can contain *). For usage, see: FindObjectsWithWildcard.py If you know the name of the model, use FBFindModelByLabelName, as demonstrated in FBComponent.py. FBGetSelectedModels can get a handle to an object which is derived from FBModel. It searches the scene for a model, based on the model's unique name and returns a list of all the selected things in the scene. See sample: ResetLocalTranslationRotation.py.     
    """
    def FBModel(self,pName):
        """
        Constructor.

        pName : Name of model. 
        """
        pass

    def Clone(self):
        """
        Clone the model.
        This will duplicate the current model.

        return : Newly created model. 
        """
        pass

    def CollapseInSchematic(self):
        """
        Collapse the model in the schematic view.

        """
        pass

    def DofToLRM(self,pLM,pDof):
        """
        Convert object space vector to local matrix.

        pLM : Resulting local rotation matrix. 
        pDof : Vector to convert 
        """
        pass

    def ExpandInSchematic(self):
        """
        Expand the model in the schematic view.

        """
        pass

    def FBDelete(self):
        """
        Open Reality deletion function.

        """
        pass

    def FbxGetObjectSubType(self):
        """
        Returns the class sub type inherited by the class of an object, for example: 'Default', 'Mesh'.

        """
        pass

    def FbxGetObjectType(self):
        """
        Returns the class type inherited by the class of an object, for example: 'Model'.

        """
        pass

    def ForceAlwaysEvaluate(self):
        """
        Force Always Evaluate.
        In some case, MoBu kernel perform optimization by skipping certain evaluation tasks. This function stop skipping for this model.

        """
        pass

    def GetAdditionalUniqueColorID(self,pIndex):
        """
        Get Additional Unique Color Id.

        pIndex : the requested unique color id index, can't be larger than GetAdditionalColorIDCount() 
        return : Additional Unique ColorId. 
        """
        pass

    def GetAdditionalUniqueColorIDCount(self):
        """
        Get additional unique color count.

        return : Additional Unique Color Count. 
        """
        pass

    def GetBoundingBox(self,pMin,pMax):
        """
        Get the bounding box of the model.
        Note. for deformable model, this function will provide the approximated (larger than the smallest) bounding box for performance consideration.

        pMin : Output parameter. Minimum value of the bounding box. 
        pMax : Output parameter. Maximum value of the bounding box. 
        """
        pass

    def GetHierarchyWorldMatrices(self,pMatricesArray,pMatricesArrayCount,pHiercharyTraverserType,pEvaluateInfo):
        """
        Computes the global transform matrices between this model and all its children (all levels).
        The hierarchy world matrix for a model is represented as a global transform matrix applied on an arbitrary root hierarchy node (this model for instance), considered as the world reference.

        pMatricesArray : The matrix array (memory already allocated) to fill in with the hierarchy world matrix of all the model's children models 
        pMatricesArrayCount : The size of the matrix array 
        pHiercharyTraverserType : The hierarchy traverser type 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified. 
        """
        pass

    def GetLocalTransformationMatrixWithGlobalRotationDoF(self,pMatrix,pInverse,pEvaluateInfo):
        """
        Get the local transformation (or local inverse transformation) matrix with the global Rotation DoF values from the model.
        The GetMatrix method was previously wrongly returning the local transformation (and local inverse transformation) matrices with global Rotation DoF values. The GetMatrix method implementation has been updated to not include the global Rotation DoF values. This method returns the same matrix values returned by the legacy GetMatrix implementation when retrieving the local transformation (and local inverse transformation) matrices.

        pMatrix : Matrix to fill with requested information. 
        pInverse : False for the transformation matrix, true for the inverse transformation matrix. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified. 
        """
        pass

    def GetMatrix(self,pMatrix,pWhat,pGlobalInfo,pEvaluateInfo):
        """
        Get a matrix from the model.

        pMatrix : Matrix to fill with requested information. 
        pWhat : Type of information requested (default=transformation). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified. 
        """
        pass

    def GetSchematicPosition(self):
        """
        Get the position in the schematic view for the model.

        return : Current position for the model. 
        """
        pass

    def GetSelectedPointsCount(self):
        """
        Get the number of selected points in the model.

        return : Number of selected points. 
        """
        pass

    def GetVector(self,pVector,pWhat,pGlobalInfo,pEvaluateInfo):
        """
        Get a vector from the model.

        pVector : Vector to fill with requested values. 
        pWhat : Type of information requested (default=translation, inverses not supported). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def IsCollapsedInSchematic(self):
        """
        Returns if the model is collapsed or not (expanded) in the schematic view.

        return : true if the model is collapsed in the schematic view, false if it is expanded. 
        """
        pass

    def IsEvaluationReady(self,pWhat,pEvaluateInfo):
        """
        Is the model's evaluation task result ready.

        pWhat : Type of evaluation task. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def IsForceAlwaysEvaluate(self):
        """
        Return Force Always Evaluate status.

        """
        pass

    def IsVisible(self,pEvaluateInfo):
        """
        If the model is visible.
        Note. this query will consider self Visibility property, plus parent node/set Visibility. The visibility of a model is affected by 4 parameters:

        pEvaluateInfo : evaluate info, 
        return : true if visible for the given evaluate info. 
        """
        pass

    def LRMToDof(self,pDof,pLM):
        """
        Convert local matrix to object space vector.

        pDof : Resulting object space vector. 
        pLM : Local rotation matrix to convert 
        """
        pass

    def MatrixToRotation(self,pRotation,pMatrix):
        """
        Convert Rotation Matrix to Euler Vector based on model's rotation order.

        pRotation : Resulting euler vector, whose angles are stored in [X,Y,Z] order. 
        pMatrix : Matrix to convert. 
        """
        pass

    def NoFrustumCullingRelease(self):
        """
        Release no frustum culling request.

        return : Current no frustum culling request count after function call. 
        """
        pass

    def NoFrustumCullingRequire(self):
        """
        Acquire no frustum culling request.

        return : Current no frustum culling request count after function call. 
        """
        pass

    def RayCast(self,pCamera,pMouseX,pMouseY,pHitPosition,pHitNormal):
        """
        Ray cast test.

        pCamera : Camera to use for casting. 
        pMouseX : Mouse X position. 
        pMouseY : Mouse Y position. 
        pHitPosition : Ray cast position on the object. 
        pHitNormal : Normal at the ray cast position on the object. 
        return : true if it hit the meshes, hit would contains the precise position & normal. 
        """
        pass

    def RotationToMatrix(self,pMatrix,pRotation):
        """
        Convert Euler Vector to Rotation Matrix based on model's rotation order.

        pMatrix : Resulting rotation matrix. 
        pRotation : Object space rotation vector to convert, whose angles are stored in [X,Y,Z] order. 
        """
        pass

    def SetAdditionalUniqueColorIDCount(self,pCount):
        """
        Request additional Unique color IDs.

        pCount : User should note that Unique Color ID resource is limited (only 24 bits), hence should avoid to use unnecessary large number. 
        return : True if Unique ColorId resource is available. 
        """
        pass

    def SetMatrix(self,pMatrix,pWhat,pGlobalInfo,pPushUndo,pEvaluateInfo):
        """
        Set a matrix for the model.

        pMatrix : Information to use to set the model's matrix. 
        pWhat : Type of matrix to set (default=transformation). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pPushUndo : <b>true</b> if this operation is undoable, don't push undo in non UI thread. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def SetMatrixWithPrecision(self,pMatrix,pWhat,pGlobalInfo,pPushUndo,pEvaluateInfo,pPrecision):
        """
        Set a matrix for the model.

        pMatrix : Information to use to set the model's matrix. 
        pWhat : Type of matrix to set (default=transformation). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pPushUndo : <b>true</b> if this operation is undoable, don't push undo in non UI thread. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        pPrecision : Indicate the precision level, used when calculating the threshold value for gimble lock. 16 * pow(10.0, -10)) is the new default value since Mobu 2016, 16 * pow(10.0, -6)) is old default value before then. 
        """
        pass

    def SetSchematicPosition(self,pX,pY):
        """
        Set the position in the schematic view for the model.

        pX : X position to set. 
        pY : Y position to set. 
        """
        pass

    def SetSchematicPosition(self,pVector2d):
        """
        Set the position in the schematic view for the model.

        pVector2d : Position to set. 
        """
        pass

    def SetVector(self,pVector,pWhat,pGlobalInfo,pPushUndo,pEvaluateInfo):
        """
        Set a vector for the model.

        pVector : Vector to use to set values. 
        pWhat : Type of information to set (default=translation, inverses not supported). 
        pGlobalInfo : <b>true</b> if it is GlobalInfo, <b>false</b> if Local (default=true). 
        pPushUndo : <b>true</b> if this operation is undoable, don't push undo in non UI thread. 
        pEvaluateInfo : EvaluateInfo, Take Display if none specified 
        """
        pass

    def SetupPropertiesForShapes(self):
        """
        Setup Shape Properties.
        Normally this function is called automatically at the next global synchronization point after the geometry has been updated. However you must call it explicitly to access the shape properties immediately after shapes adding/removing before next global synchronization point.

        """
        pass

    def UseFrustumCulling(self):
        """
        Get the current Frustum Culling Status.

        return : <b>True</b> if model don't use frustum culling currently. 
        """
        pass

    AnimationNode=property(doc="<b>Read Only Property:</b> Animation node of the model.          ")
    BlendShapeDeformable=property(doc="<b>Read Write Property:</b> Model blend-shape deformable. Not Savable          ")
    CastsShadows=property(doc="<b>Read Write Property:</b> If true, the geometry will produce shadows.          ")
    Children=property(doc="<b>List:</b> Children for model.          ")
    ConstrainDeformable=property(doc="<b>Read Write Property:</b> Model constraint deformable. Not Savable          ")
    Deformers=property(doc="<b>List:</b> Deformers (Skeleton Deformer or Point Cache Deformer).          ")
    GeometricRotation=property(doc="<b>Read Write Property:</b> Geometric rotation.          ")
    GeometricScaling=property(doc="<b>Read Write Property:</b> Geometric scaling.          ")
    GeometricTranslation=property(doc="<b>Read Write Property:</b> Geometric translation.          ")
    Geometry=property(doc="<b>Read Write Property:</b> Geometry for the model.          ")
    GeometryUpdateId=property(doc="<b>Read Only Property:</b> model geometry (vertex data) related update id.          ")
    Icon3D=property(doc="<b>Read Write Property:</b> Is model a 3D icon?          ")
    IsConstrained=property(doc="<b>Read Only Property:</b> Is model constrained?          ")
    IsDeformable=property(doc="<b>Read Only Property:</b> Is model deformable?          ")
    LookAt=property(doc="<b>Read Write Property:</b> Look at model (interest point).          ")
    Materials=property(doc="<b>List:</b> Materials for model.          ")
    ModelVertexData=property(doc="<b>Read Only Property:</b> ModelVertexData for the model.          ")
    Parent=property(doc="<b>Read Write Property:</b> Parent model.          ")
    Pickable=property(doc="<b>Read Write Property:</b> Indicate if a model can be picked in the viewer. This has a default value of 'true'.          ")
    PointCacheDeformable=property(doc="<b>Read Write Property:</b> Model point cache deformable. Not Savable          ")
    PointCacheRecord=property(doc="<b>Read Write Property:</b> Record Point Cache for model? Not Savable          ")
    PostRotation=property(doc="<b>Read Write Property:</b> Post Rotation (considered if RotationActive is true)          ")
    PreRotation=property(doc="<b>Read Write Property:</b> Pre Rotation (considered if RotationActive is true)          ")
    PrimaryVisibility=property(doc="<b>Read Write Property:</b> Control the geometry render state. Geometry can still cast shadows even if this is turned off.          ")
    QuaternionInterpolate=property(doc="<b>Read Write Property:</b> Use quaternion interpolation.          ")
    ReceiveShadows=property(doc="<b>Read Write Property:</b> If true, the geometry will receive shadows.          ")
    Rotation=property(doc="<b>Read Write Property:</b> Lcl rotation.          ")
    RotationActive=property(doc="<b>Read Write Property:</b> Is model using Rotation Limits?          ")
    RotationMax=property(doc="<b>Read Write Property:</b> Max Rotation Limit (considered if RotationActive is true)          ")
    RotationMaxX=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On X?          ")
    RotationMaxY=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On Y?          ")
    RotationMaxZ=property(doc="<b>Read Write Property:</b> Is model using Maximum Rotation Limits On Z?          ")
    RotationMin=property(doc="<b>Read Write Property:</b> Min Rotation Limit (considered if RotationActive is true)          ")
    RotationMinX=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On X?          ")
    RotationMinY=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On Y?          ")
    RotationMinZ=property(doc="<b>Read Write Property:</b> Is model using Minimum Rotation Limits On Z?          ")
    RotationOrder=property(doc="<b>Read Write Property:</b> Rotation order.          ")
    RotationSpaceForLimitOnly=property(doc="<b>Read Write Property:</b> Apply Post Rotation Matrix only for Limits?          ")
    Scaling=property(doc="<b>Read Write Property:</b> Lcl scaling.          ")
    Scene=property(doc="<b>Read Only Property:</b> Scene containing the model.          ")
    Shaders=property(doc="<b>List:</b> Shaders for model.          ")
    ShadingMode=property(doc="<b>Read Write Property:</b> Shading mode for the model.          ")
    Show=property(doc="<b>Read Write Property:</b> Indicate if the viewer should show the object, according to its visibility value. This has a default value of 'false'.          ")
    SkeletonDeformable=property(doc="<b>Read Write Property:</b> Model skeleton deformable. Not Savable          ")
    SoftSelected=property(doc="<b>Read Write Property:</b> Is model Soft selected?          ")
    Textures=property(doc="<b>List:</b> Textures with Special UseType (Other than 'Color' which should connect to materials).          ")
    Transformable=property(doc="<b>Read Write Property:</b> Indicate if a model can be transformable in the viewer. This has a default value of 'true'.          ")
    Translation=property(doc="<b>Read Write Property:</b> Lcl translation.          ")
    UniqueColorId=property(doc="<b> Read Only Property:</b> Unique Color Id for color based viewer picking. Color channel values are in the range [0, 1] with 1.0/255 precision.          ")
    UpVector=property(doc="<b>Read Write Property:</b> UpVector model.          ")
    Visibility=property(doc="<b>Read Write Property:</b> Visibility of model. This can be overridden by the 'Show' property.          ")
    VisibilityInheritance=property(doc="<b>Read Write Property:</b> //!< When this value is set to True the Visibility of this model is also applied to all its descendants          ")
    pass

class FBNote (FBBox):
    """
    Note class.     
         
    """
    def FBNote(self,pName):
        """
        Constructor.

        pName : Name of note. 
        """
        pass

    def Attach(self,pComp):
        """
        Attach the note to a component.
        Will attach the note to the component. If <b>pComp</b> is NULL, the note will only be added to the scene.

        pComp : Component on which to attach note. 
        return : A boolean indicating if the operation was successful or not. 
        """
        pass

    def Detach(self,pComp):
        """
        Detach the note from a component.
        Will detach the note from the component. If <b>pComp</b> is NULL, the note will be removed from the scene and detached from all components.

        pComp : Component from which to detach note. 
        return : A boolean indicating if the operation was successful or not. 
        """
        pass

    StaticComment=property(doc="<b>Read Write Property:</b> Comment associated to this note.          ")
    pass

class FBObjectPose (FBPose):
    """
    FBObjectPose class.     
     This class exposes the object used to store the pose of objects.      
    """
    def FBObjectPose(self,pName):
        """
        Public constructor.
        This constructor is used to create a new object.

        pName : Object name. If pObject is not NULL, pName will be ignored. 
        """
        pass

    def AddStanceOffset(self,pObjectName,pStancePose,pPoseTransformType):
        """
        Add the StanceOffset to an object in the pose.

        pObjectName : Name of the object. 
        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef). 
        """
        pass

    def AddStanceOffsetAllObjects(self,pStancePose,pPoseTransformType):
        """
        Add the StanceOffset to all the objects in the pose.

        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef). 
        """
        pass

    def ClearPose(self):
        """
        Clear all the data of the pose.

        """
        pass

    def CopyFrom(self,pFromPose):
        """
        Copy everything from a given object.

        pFromPose : Pose from which to copy. 
        """
        pass

    def CopyObjectPose(self,pObjectName,pObject):
        """
        Copy the pose of all the properties of an object.

        pObjectName : Name of the object to store in the pose. 
        pObject : Object from which we'll read all the property values to store in the pose. 
        """
        pass

    def CopyPoseAllObjectsTransformFrom(self,pFromPose,pPoseTransformType):
        """
        Copy all the transforms from a given pose.

        pFromPose : Pose from which to copy the data. 
        pPoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef). 
        """
        pass

    def CopyPoseDataFrom(self,pFromPose):
        """
        Copy all the pose data from a given pose.

        pFromPose : Pose from which to copy the data. 
        """
        pass

    def CopyPoseTransformFrom(self,pFromPose,pObjectName,pPoseTransformType):
        """
        Copy the transforms of an object from a given pose.

        pFromPose : Pose from which to copy the data. 
        pObjectName : Name of object to copy the transform from. 
        pPoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef). 
        """
        pass

    def CopyPropertyPose(self,pObjectName,pProperty):
        """
        Copy the pose of a property of an object.

        pObjectName : Name of the object to store in the pose. 
        pProperty : Property from which we'll read the value to store in the pose. 
        """
        pass

    def CopyTransform(self,pObjectName,pObject,pObjectPoseOptions):
        """
        Copy the transform of an object.

        pObjectName : Name of the object to store in the pose. 
        pObject : Object from which we'll evaluate the transform values to store in the pose. 
        pObjectPoseOptions : PoseOptions used to specify the transform of the reference object (Default: Identity). 
        """
        pass

    def GetPropertyValue(self,pValue,pSize,pObjectName,pPropertyName):
        """
        Get the value of a property stored in the pose.

        pValue : Value to get. 
        pSize : Number of elements in pValue. 
        pObjectName : Name of the object to get the value. 
        pPropertyName : Name of the property to get the value. 
        """
        pass

    def GetStoredObjectNames(self):
        """
        Get all the object names currently stored in this pose.

        return : All the object names currently stored in this pose. 
        """
        pass

    def GetTransform(self,pT,pRM,pSM,pObjectName,pPoseTransformType):
        """
        Get the transform of an object in the pose.

        pT : Translation to get. 
        pRM : Rotation to get. 
        pSM : Scaling to get. 
        pObjectName : Name of the object to get the transform. 
        pPoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef). 
        return : True if the transform was found in the pose. 
        """
        pass

    def IsPropertyPoseable(self,pProperty):
        """
        Is the property poseable?

        pProperty : FBProperty
        return : True if the value of this property can be stored in the pose. 
        """
        pass

    def IsPropertyStored(self,pObjectName,pPropertyName):
        """
        Is the property stored in the pose?

        pObjectName : Name of the object. 
        pPropertyName : Name of the property. 
        return : True if the property is stored in the pose. 
        """
        pass

    def IsTransformStored(self,pObjectName,pPoseTransformType):
        """
        Is the transform of this object stored in the specified TransformType?

        pObjectName : Name of the object. 
        pPoseTransformType : Transform type in which to check. 
        return : True if the transform of this object is stored in the specified TransformType (Local, Global and LocalRef). 
        """
        pass

    def MirrorPose(self,pObjectName,pObjectPoseMirrorOptions):
        """
        Mirror the transform of an object in the pose.

        pObjectName : Name of the object to mirror. 
        pObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane. 
        """
        pass

    def MirrorPoseAllObjects(self,pObjectPoseMirrorOptions):
        """
        Mirror the transform of all objects in the pose.

        pObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane. 
        """
        pass

    def MultTransform(self,pObjectName,pGX,pTransformAttribute,pPoseTransformType):
        """
        Multiply the transform of an objects in the pose.

        pObjectName : Name of the object. 
        pGX : Transformation matrix to apply. 
        pTransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation. 
        pPoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef). 
        """
        pass

    def MultTransformAllObjects(self,pGX,pTransformAttribute,pPoseTransformType):
        """
        Multiply the transform of all objects in the pose.

        pGX : Transformation matrix to apply. 
        pTransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation. 
        pPoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef). 
        """
        pass

    def PasteObjectPose(self,pObjectName,pObject):
        """
        Paste the pose of all the properties of an object.

        pObjectName : Name of the object stored in the pose. 
        pObject : Object which will receive the values stored in the pose. 
        """
        pass

    def PastePropertyPose(self,pObjectName,pProperty):
        """
        Paste the pose of a property of an object.

        pObjectName : Name of the object stored in the pose. 
        pProperty : Property which will receive the value stored in the pose. 
        """
        pass

    def PasteTransform(self,pObjectName,pObject,pObjectPoseOptions,pEvaluateInfo):
        """
        Paste the transform of an object.

        pObjectName : Name of the object stored in the pose. 
        pObject : Object which will receive the transform values stored in the pose. 
        pObjectPoseOptions : PoseOptions used to specify the transform of the reference object, the TransformType and TransformAttributes to paste. 
        pEvaluateInfo : Information concerning the evaluation of the animation (time, etc.) 
        """
        pass

    def RemoveStanceOffset(self,pObjectName,pStancePose,pPoseTransformType):
        """
        Remove the StanceOffset from an object in the pose.

        pObjectName : Name of the object. 
        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef). 
        """
        pass

    def RemoveStanceOffsetAllObjects(self,pStancePose,pPoseTransformType):
        """
        Remove the StanceOffset from all the objects in the pose.

        pStancePose : Pose representing the stance of all objects. 
        pPoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef). 
        """
        pass

    def SetPropertyValue(self,pObjectName,pPropertyName,pValue,pSize):
        """
        Set the value of a property in the pose.

        pObjectName : Name of the object to set the value. 
        pPropertyName : Name of the property to set the value. 
        pValue : Value to set. 
        pSize : Number of elements in pValue. 
        """
        pass

    def SetTransform(self,pT,pRM,pSM,pObjectName,pPoseTransformType):
        """
        Set the transform of an object in the pose.

        pT : Translation to set. 
        pRM : Rotation to set. 
        pSM : Scaling to set. 
        pObjectName : Name of the object to set the transform. 
        pPoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef). 
        """
        pass

    pass

class FBPhysicalProperties (FBBox):
    """
    Base class for physical properties attach to a model.     
    See sample: RigiBody.py.     
    """
    def FBPhysicalProperties(self,pName):
        """
        pName : str
        """
        pass

    pass

class FBSet (FBBox):
    """
    Objects Set class.     
     This class is an interface to manipulate object sets in the scene. Note: an item cannot be in two FBSet objects at once. Also, an FBGroup cannot contain FBSet objects, although an FBSet object can contain an FBGRoup.      
    """
    def FBSet(self,pName):
        """
        Constructor.

        pName : Set name. 
        """
        pass

    def Contains(self,pComponent):
        """
        Contains.

        pComponent : Component to verify if it is in the Group 
        return : 0 if the component is not in the FBSet, 1 if it is in this FBSet, 2 if it is in another FBSet 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def Select(self,pSelect):
        """
        Select.

        pSelect : If <b>true</b>, set contents will be selected. 
        """
        pass

    Items=property(doc="<b>List:</b> Items in the set.          ")
    Pickable=property(doc="<b>Read Write Property:</b> Controls if objects in the set are pickable.          ")
    Transformable=property(doc="<b>Read Write Property:</b> Controls if objects in the set are transformable.          ")
    Visibility=property(doc="<b>Read Write Property:</b> Visibility of set (animatable).          ")
    pass

class FBShader (FBBox):
    """
    Shader class.     
         
    """
    def FBShader(self,pName):
        """
        Protected constructor.

        pName : Shader name. 
        """
        pass

    def Append(self,pModel):
        """
        Append shader to <b>pModel</b>.

        pModel : Model to append shader to. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def CloneShaderParameter(self,pNewShader):
        """
        Clone shader.

        pNewShader : Shader to copy data to. 
        """
        pass

    def ReplaceAll(self,pModel):
        """
        Replace all shader in <b>pModel</b>.

        pModel : Model to replace all shader to. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def ShaderNeedBeginRender(self):
        """
        Does the shader need a begin render call.

        """
        pass

    RenderingPass=property(doc="<b>Read Write Property:</b> Rendering pass object are shaded in.          ")
    ShaderDescription=property(doc="Description.          ")
    pass

class FBSpreadCell (FBSpreadPart):
    """
    Spreadsheet cell.     
         
    """
    def FBSpreadCell(self,pParent,pRow,pCol):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pRow : Row to which cell belongs. 
        pCol : Column to which cell belongs. 
        """
        pass

    pass

class FBSpreadColumn (FBSpreadPart):
    """
    Spreadsheet column.     
         
    """
    def FBSpreadColumn(self,pParent,pCol):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pCol : Column number. 
        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption of the column.          ")
    Justify=property(doc="<b>Read Write Property:</b> Text justification.          ")
    Width=property(doc="<b>Read Write Property:</b> Column width.          ")
    pass

class FBSpreadRow (FBSpreadPart):
    """
    Spreadsheet row.     
         
    """
    def FBSpreadRow(self,pParent,pRow):
        """
        Constructor.

        pParent : Parent spreadsheet. 
        pRow : User-defined reference to assign to row. 
        """
        pass

    def EditCaption(self):
        """
        Edit the row caption.
        This will initiate the UI edit of a row caption.

        return : Operation was successful (<b>true</b> or <b>false</b>). 
        """
        pass

    def Remove(self):
        """
        Remove (destroy) row.

        """
        pass

    Caption=property(doc="<b>Read Write Property:</b> Caption to display with row.          ")
    Parent=property(doc="<b>Read Write Property:</b> Parent of row (reference).          ")
    RowSelected=property(doc="<b>Read Write Property:</b> Is row selected?          ")
    pass

class FBSurface (FBGeometry):
    """
    Surface class.     
         
    """
    def FBSurface(self,pName):
        """
        Constructor.

        pName : Name of Surface. 
        """
        pass

    def ControlPointsBegin(self):
        """
        """
        pass

    def ControlPointsEnd(self):
        """
        """
        pass

    def GetControlPoint(self,pIndex,pX,pY,pZ,pW):
        """
        pIndex : int
        pX : float
        pY : float
        pZ : float
        pW : float
        """
        pass

    def GetSurfaceCapped(self,pUorV,pDirection):
        """
        pUorV : int
        pDirection : int
        """
        pass

    def SetControlPoint(self,pIndex,pX,pY,pZ,pW):
        """
        pIndex : int
        pX : float
        pY : float
        pZ : float
        pW : float
        """
        pass

    def SurfaceBegin(self):
        """
        """
        pass

    def SurfaceEditBegin(self):
        """
        """
        pass

    def SurfaceEditEnd(self):
        """
        """
        pass

    def SurfaceEnd(self):
        """
        """
        pass

    def VertexGetSelected(self,pU,pV):
        """
        Get the selected state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is selected, false if not. 
        """
        pass

    def VertexGetTransformable(self,pU,pV):
        """
        Get the Transformable state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is Transformable, false if not. 
        """
        pass

    def VertexGetVisible(self,pU,pV):
        """
        Get the visible state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        return : true if the vertex is visible, false if not. 
        """
        pass

    def VertexSetSelected(self,pU,pV,pState):
        """
        Set the selected state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        pState : Set the select state. 
        return : true if the vertex is selected, false if not. 
        """
        pass

    def VertexSetVisible(self,pU,pV,pState):
        """
        Set the visible state of a vertex.

        pU : The u index of the vertex. 
        pV : The v index of the vertex. 
        pState : Set the visible state. 
        return : true if the vertex is visible, false if not. 
        """
        pass

    SurfaceMode=property(doc="<b>Read Write Property:</b> Surface mode.          ")
    UClosed=property(doc="<b>Read Write Property:</b> U Closed.          ")
    USize=property(doc="<b>Read Write Property:</b> Size in U directions.          ")
    UStep=property(doc="<b>Read Write Property:</b> Step in U directions.          ")
    VClosed=property(doc="<b>Read Write Property:</b> V Closed          ")
    VSize=property(doc="<b>Read Write Property:</b> Size in V directions.          ")
    VStep=property(doc="<b>Read Write Property:</b> Step in V directions.          ")
    pass

class FBTexture (FBBox):
    """
    See samples: HUDElements.py, MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py, DeleteUnusedMedia.py.     
        
    """
    def FBTexture(self,pName):
        """
        Constructor.

        pName : Name of the texture media. If pName is a valid path, FBTexture will create a FBVideo object which is used in the Video property; else just a ordinary name. 
        """
        pass

    def Clone(self):
        """
        Clone the texture.
        This will duplicated the current texture.

        return : Newly created texture. 
        """
        pass

    def FBDelete(self):
        """
        """
        pass

    def OGLInit(self,pRenderOptions):
        """
        pRenderOptions : FBRenderOptions
        """
        pass

    Alpha=property(doc="<b>Read Write Property:</b> Texture alpha value.          ")
    BlendMode=property(doc="<b>Read Write Property:</b> Texture blend mode.          ")
    Height=property(doc="<b>Read Only Property:</b> Height of texture.          ")
    Mapping=property(doc="<b>Read Write Property:</b> Texture mapping.          ")
    Rotation=property(doc="<b>Read Write Property:</b> Rotation coordinates.          ")
    Scaling=property(doc="<b>Read Write Property:</b> Scaling coordinates.          ")
    SwapUV=property(doc="<b>Read Write Property:</b> Swap UV coordinates?          ")
    TextureOGLId=property(doc="<b>Read Only:</b> OpenGL texture buffer object Id.          ")
    Translation=property(doc="<b>Read Write Property:</b> Translation coordinates.          ")
    UseType=property(doc="<b>Read Write Property:</b> Texture Use Type.          ")
    Video=property(doc="<b>Read Write Property:</b> Media used for texturing.          ")
    Width=property(doc="<b>Read Only Property:</b> Width of texture.          ")
    pass

class FBUserObject (FBBox):
    """
        
        
    """
    def FBUserObject(self,pName):
        """
        Constructor.

        pName : User object name. 
        """
        pass

    pass

class FBVideo (FBBox):
    """
    Video media class.     
     Similar to the FBModel class, the FBVideo class serves as a general media class for images, video clips and video memory, as well as the possibility of custom formats and custom live cards.To have a valid FBVideo object, it must be constructed with a string pointing to a valid media file. After the creation, the method 'IsValid()' should be used to confirm the object's status. An invalid object cannot be used or interact with any other application object. The only property that can be read and modified is its 'Filename'. To make convert an invalid FBVideo object into a valid one, simply change its Filename property to point to a supported media file. See sample: DeleteUnusedMedia.py.     
    """
    def FBVideo(self,pName):
        """
        Constructor.

        pName : Name of video media. 
        """
        pass

    KeepOnGPU=property(doc="<b>Read Write Property:</b> Don't auto flush from GPU if true. session runtime flag, won't be saved.          ")
    pass

class FBActor (FBConstraint):
    """
    FBActor is used to link motion data to a character.     
     In MotionBuilder, an actor is a model used to link captured motion data to a character. Use functions in FBActor to set the body color, skeleton color, pivot color, marker size, pivot size, pivot information, etc. on an actor.<b>These classes are under development and may change dramatically between versions.</b>To obtain the list of actors present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of actors in the property Actors. 
@code
FBSystem lSystem;
FBScene* lScene = lSystem.Scene;
for( int lIdx = 0; lIdx < lScene->Actors.GetCount(); ++lIdx )
{
    FBTrace( 'Actor[%d]: '%s'\n', lIdx, (char*)lScene->Actors[lIdx] );
}
@endcode

The current actor selected in the Character tool can be obtained via the FBApplication object. 
@code
FBApplication lApplication;
FBActor* lActor = lApplication.CurrentActor;
if( lActor )
{
    FBTrace( 'Current actor is: '%s'\n', (char*)lActor->Name );
}
else
{
    FBTrace( 'No actor currently selected\n' );
}
@endcode

     
    """
    def FBActor(self,pName):
        """
        Constructor.

        pName : Name of new actor. 
        """
        pass

    def FBDelete(self):
        """
        Actual Actor destructor.
        This method is used to delete the actual actor object represented by an instance of FBActor.

        """
        pass

    def GetCurrentSkeletonState(self,pResetOrientation):
        """
        Return the Current Skeleton State.

        pResetOrientation : When set to true, all rotations in the state will be reset to characterization values. 
        return : Current Skeleton State 
        """
        pass

    def GetDefaultSkeletonState(self):
        """
        Return the Default Skeleton State.

        return : Default Skeleton State 
        """
        pass

    def GetDefinitionRotationVector(self,pSkeletonId,pRotationVector):
        """
        Get Actor Rotation Definition.
        Only effective when IKManip property is set to false.

        pSkeletonId : Skeleton Node Id 
        pRotationVector : Actor Rotation Definition for the given ID 
        """
        pass

    def GetDefinitionScaleVector(self,pSkeletonId,pScaleVector):
        """
        Get Actor Scaling Definition.

        pSkeletonId : Skeleton Node Id 
        pScaleVector : Actor Scaling Definition for the given ID 
        """
        pass

    def GetDefinitionTranslationVector(self,pSkeletonId,pTranslationVector):
        """
        Get Actor Translation Definition.
        Only effective when IKManip property is set to false.

        pSkeletonId : Skeleton Node Id 
        pTranslationVector : Actor Translation Definition for the given ID 
        """
        pass

    def SetActorTranslation(self,pTranslationVector):
        """
        Translate Actor, similar to moving the hips of the Actor in the UI.
        Only effective when IKManip property is set to false.

        pTranslationVector : Will move the entire Actor to pTranslationVector coordinate 
        """
        pass

    def SetDefinitionRotationVector(self,pSkeletonId,pRotationVector,pSymmetricUpdate):
        """
        Set Actor Rotation Definition.
        Only effective when IKManip property is set to false.

        pSkeletonId : Skeleton Node Id 
        pRotationVector : Actor Rotation value for the given ID 
        pSymmetricUpdate : Update right and left part at the same time 
        """
        pass

    def SetDefinitionScaleVector(self,pSkeletonId,pScaleVector,pSymmetricUpdate):
        """
        Set Actor Scaling Definition.

        pSkeletonId : Skeleton Node Id 
        pScaleVector : Actor Scaling value for the given ID 
        pSymmetricUpdate : Update right and left part at the same time 
        """
        pass

    def SetDefinitionTranslationVector(self,pSkeletonId,pTranslationVector,pSymmetricUpdate):
        """
        Set Actor Translation Definition.
        Only effective when IKManip property is set to false.

        pSkeletonId : Skeleton Node Id 
        pTranslationVector : Actor Translation value for the given ID 
        pSymmetricUpdate : Update right and left part at the same time 
        """
        pass

    def Snap(self,pRecalcOffset):
        """
        Snap the marker set of the actor.

        pRecalcOffset : FBRecalcMarkerSetOffset
        return : True if the operation completed successfully. 
        """
        pass

    def UpdateValues(self,pEvalInfo):
        """
        Update Internal Values to be corresponding to the Given Evaluate Information.

        pEvalInfo : Evaluate Info of the Values 
        """
        pass

    BodyColor=property(doc="<b>Read Write Property:</b> The color of the body of the actor.          ")
    ChestOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    ChestOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    ChestPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    FKFingerMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered intermediate finger phalanges.          ")
    FKFingerTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered finger tip phalanges.          ")
    FKThumbTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered thumb tip phalanges.          ")
    HeadOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    HeadOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    HeadPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    HipsOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    HipsOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    HipsPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    HumanFingerLimits=property(doc="<b>Read Write Property:</b> Enables/Disables human finger limits during actor solve.          ")
    IKManip=property(doc="<b>Read Write Property:</b> Access to the IK Manip mode. This property is shared for all actors.          ")
    LeftAnkleOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftAnkleOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftAnklePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftCollarOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftCollarOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftCollarPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftElbowOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftElbowOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftElbowPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftFootOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftFootOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftFootPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHipOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftHipOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftHipPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftIndexAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftIndexAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftIndexBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftIndexBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftIndexCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftIndexCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftKneeOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftKneeOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftKneePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftMiddleAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftMiddleAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftMiddleBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftMiddleBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftMiddleCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftMiddleCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftPinkyAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftPinkyAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftPinkyBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftPinkyBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftPinkyCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftPinkyCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftRingAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftRingAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftRingBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftRingBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftRingCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftRingCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftShoulderOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftShoulderOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftShoulderPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    LeftThumbAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftThumbAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftThumbBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftThumbBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftThumbCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftThumbCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftWristOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    LeftWristOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    LeftWristPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    ManipulateOffsets=property(doc="<b>Read Write Property:</b> Flag to compute offsets while manipulating. If it is set to false, the manipulator is re-snapping as before. If it is set to true, offsets properties (T and R) are computed and candidated instead.          ")
    MarkerSet=property(doc="<b>Read Write Property:</b> Associated marker set.          ")
    MarkerSetSize=property(doc="<b>Read Write Property:</b> The size of the markers of the actor.          ")
    NeckOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    NeckOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    NeckPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    OutputMarkerSet=property(doc="<b>Read Write Property:</b> Associated output marker set.          ")
    PivotColor=property(doc="<b>Read Write Property:</b> The color of the pivot points of the actor.          ")
    PivotPointsVisibility=property(doc="<b>Read Write Property:</b> Show or Hide the Pivot Points.          ")
    PivotSize=property(doc="<b>Read Write Property:</b> The size of the pivot points of the actor.          ")
    RightAnkleOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightAnkleOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightAnklePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightCollarOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightCollarOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightCollarPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightElbowOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightElbowOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightElbowPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightFootOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightFootOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightFootPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHipOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightHipOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightHipPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightIndexAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightIndexAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightIndexBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightIndexBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightIndexCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightIndexCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightKneeOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightKneeOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightKneePosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightMiddleAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightMiddleAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightMiddleBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightMiddleBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightMiddleCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightMiddleCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightPinkyAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightPinkyAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightPinkyBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightPinkyBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightPinkyCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightPinkyCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightRingAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightRingAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightRingBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightRingBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightRingCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightRingCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightShoulderOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightShoulderOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightShoulderPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    RightThumbAOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightThumbAOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightThumbBOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightThumbBOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightThumbCOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightThumbCOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightWristOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    RightWristOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    RightWristPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    SkeletonColor=property(doc="<b>Read Write Property:</b> The color of the skeleton of the actor.          ")
    SkeletonVisibility=property(doc="<b>Read Write Property:</b> Show or Hide the Skeleton.          ")
    SymmetryEditRotation=property(doc="<b>Read Write Property:</b> Symmetry Edit (Rotation) mode state. Only effective when IKManip property is set to false. This property is shared for all actors.          ")
    SymmetryEditScaling=property(doc="<b>Read Write Property:</b> Symmetry Edit (Scaling) mode state. Only effective when IKManip property is set to false. This property is shared for all actors.          ")
    SymmetryEditTranslation=property(doc="<b>Read Write Property:</b> Symmetry Edit (Translation) mode state. Only effective when IKManip property is set to false. This property is shared for all actors.          ")
    Visibility=property(doc="<b>Read Write Property:</b> Show or Hide the Actor Body.          ")
    WaistOffsetR=property(doc="<b>Read Write Property:</b> Local rotation offset that is applied after the actor solve          ")
    WaistOffsetT=property(doc="<b>Read Write Property:</b> Local translation offset that is applied after the actor solve          ")
    WaistPosition=property(doc="<b>Read Write Property:</b> Body part pivot of the actor.          ")
    pass

class FBCamera (FBModel):
    """
    Creates custom cameras and manages system cameras.     
     When you look at a scene in the MotionBuilder Viewer, you are using a camera view.There are two types of cameras: Producer cameras. By default one of the producer cameras is used. These are always present. They can be configured but not destroyed. Custom cameras, created by the user.The SystemCamera property indicates whether a given camera is a producer or a custom camera.When you create a camera you should make it visible with the show property (inherited from FBModel).Use FBCameraSwitcher to get and set the current camera. For usage, see the Python sample CameraSwitcher.py.To see how to create a camera with a marker as an interest, see the Python sample code in FBCamera.py. For usage in C++, see the manipcamera sample. See samples: NewCamera.py, RenderLayers.py, CameraSwitcher.py, SetAllCamerasBackgroundColor.py, SetAllCamerasBackgroundColorFromCurrentCamera.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py, FBCamera.py.     
    """
    def FBCamera(self,pName):
        """
        Constructor.

        pName : Name of camera. 
        """
        pass

    def GetCameraMatrix(self,pMatrix,pType,pEvalInfo):
        """
        Obtains the camera's matrix.

        pMatrix : Matrix to fill with requested information. 
        pType : Camera Matrix type to obtain. 
        pEvalInfo : Take Display if none specified. 
        """
        pass

    def InverseProjection(self,pX,pY,pDistanceFromCamera,pRelativeToViewport):
        """
        Returns the world coordinates based on screen coordinates and input distance from the camera.

        pX : Screen horizontal coordinate in pixel. When pRelativeToViewport is false, the range is between 0 and (WindowWidth - 1). When pRelativeToViewport is true, the range is between 0 to (CameraViewportWidth - 1). The coordinate starts at left of the region. 
        pY : Screen vertical coordinate in pixel. When pRelativeToViewport is false, the range is between 0 and (WindowHeight - 1). When pRelativeToViewport is true, the range is between 0 to (CameraViewportHeight - 1). The coordinate starts at top of the region. 
        pDistanceFromCamera : Distance from the camera to the resulting world coordinate position 
        pRelativeToViewport : true indicates (pX,pY) is relative to the window; false indicates (pX,pY) is relative to the viewport of the camera. 
        return : The world coordinates in 3D space 
        """
        pass

    AntiAliasingIntensity=property(doc="<b>Read Write Property:</b> Anti-aliasing intensity.          ")
    AntiAliasingMethod=property(doc="<b>Read Write Property:</b> Anti-aliasing method.          ")
    ApertureMode=property(doc="<b>Read Write Property:</b> Aperture mode.          ")
    BackGroundColor=property(doc="<b>Read Write Property:</b> Background color for camera.          ")
    BackGroundImageCenter=property(doc="<b>Read Write Property:</b> Center the background image          ")
    BackGroundImageCrop=property(doc="<b>Read Write Property:</b> Crop the background image          ")
    BackGroundImageFit=property(doc="<b>Read Write Property:</b> Fit the background image          ")
    BackGroundImageKeepRatio=property(doc="<b>Read Write Property:</b> Keep the background image's ratio          ")
    BackGroundImageOffsetX=property(doc="<b>Read Write Property:</b> Ignored if BackGroundImageFit is true. X offset, in term of percentage of the fit background image width, applied on the background image.          ")
    BackGroundImageOffsetY=property(doc="<b>Read Write Property:</b> Ignored if BackGroundImageFit is true. Y offset, in term of percentage of the fit background image height, applied on the background image.          ")
    BackGroundImageScaleX=property(doc="<b>Read Write Property:</b> Ignored if BackGroundImageFit is true. X scale, in term of percentage of the fit background image width, applied on the background image.          ")
    BackGroundImageScaleY=property(doc="<b>Read Write Property:</b> Ignored if BackGroundImageFit and/or BackGroundImageKeepRatio is true. Y scale, in term of percentage of the fit background image height, applied on the background image. The X scale property is considered instead of this Y scale property if BackGroundImageKeepRatio is set to true.          ")
    BackGroundMedia=property(doc="        ")
    BackGroundPlaneDistance=property(doc="<b>Read Write Property:</b> Set the distance for the background plane.          ")
    BackGroundPlaneDistanceMode=property(doc="<b>Read Write Property:</b> Select mode for the background plane's distance.          ")
    BackGroundTexture=property(doc="<b>Read Write Property:</b> Background Texture          ")
    CameraViewportHeight=property(doc="<b> Read Only Property:</b> Camera Viewport height          ")
    CameraViewportWidth=property(doc="<b> Read Only Property:</b> Camera Viewport width          ")
    CameraViewportX=property(doc="<b> Read Only Property:</b> Camera Viewport start position's X value          ")
    CameraViewportY=property(doc="<b> Read Only Property:</b> Camera Viewport start position's Y value          ")
    Display2DMagnifierFrame=property(doc="<b>Read Write Property:</b> Enable/Disable the drawing of the 2D Magnifier frame box.          ")
    DisplayTurnTableIcon=property(doc="<b>Read Write Property:</b> Enable/Disable the drawing of the Turn Table icon.          ")
    FarPlaneDistance=property(doc="<b>Read Write Property:</b> Far plane distance.          ")
    FieldOfView=property(doc="<b>Read Write Property:</b> Field of View (used when in horizontal or vertical aperture modes).          ")
    FieldOfViewX=property(doc="<b>Read Write Property:</b> Field of View X angle (used in horizontal and vertical aperture mode).          ")
    FieldOfViewY=property(doc="<b>Read Write Property:</b> Field of View Y angle (used in horizontal and vertical aperture mode).          ")
    FilmAspectRatio=property(doc="<b>Read Write Property:</b> Film aspect ratio.          ")
    FilmBackType=property(doc="<b>Read Write Property:</b> Film back standard type.          ")
    FilmSizeHeight=property(doc="<b>Read Write Property:</b> Height of the film.          ")
    FilmSizeWidth=property(doc="<b>Read Write Property:</b> Width of the film.          ")
    FocalLength=property(doc="<b>Read Write Property:</b> Focal Length.          ")
    FocusAngle=property(doc="<b>Read Write Property:</b> Focus Angle (rendering dof).          ")
    FocusDistanceSource=property(doc="<b>Read Write Property:</b> Select source for focusing.          ")
    FocusModel=property(doc="<b>Read Write Property:</b> Another model that determines the focus distance.          ")
    FocusSpecificDistance=property(doc="<b>Read Write Property:</b> Specfic distance for focusing.          ")
    ForeGroundAlpha=property(doc="<b>Read Write Property:</b> Opacity of foreground.          ")
    ForeGroundImageCenter=property(doc="<b>Read Write Property:</b> Center the foreground image          ")
    ForeGroundImageCrop=property(doc="<b>Read Write Property:</b> Crop the foreground image          ")
    ForeGroundImageFit=property(doc="<b>Read Write Property:</b> Fit the foreground image          ")
    ForeGroundImageKeepRatio=property(doc="<b>Read Write Property:</b> Keep the foreground image's ratio?          ")
    ForeGroundImageOffsetX=property(doc="<b>Read Write Property:</b> Ignored if ForeGroundImageFit is true. X offset, in term of percentage of the fit foreground image width, applied on the foreground image.          ")
    ForeGroundImageOffsetY=property(doc="<b>Read Write Property:</b> Ignored if ForeGroundImageFit is true. Y offset, in term of percentage of the fit foreground image height, applied on the foreground image.          ")
    ForeGroundImageScaleX=property(doc="<b>Read Write Property:</b> Ignored if ForeGroundImageFit is true. X scale, in term of percentage of the fit foreground image width, applied on the foreground image.          ")
    ForeGroundImageScaleY=property(doc="<b>Read Write Property:</b> Ignored if ForeGroundImageFit and/or ForeGroundImageKeepRatio is true. Y scale, in term of percentage of the fit foreground image height, applied on the foreground image. The X scale property is considered instead of this Y scale property if ForeGroundImageKeepRatio is set to true.          ")
    ForeGroundMaterialThreshold=property(doc="<b>Read Write Property:</b> Material threshold for a transparent foreground.          ")
    ForeGroundMedia=property(doc="        ")
    ForeGroundPlaneDistance=property(doc="<b>Read Write Property:</b> Set the distance for the foreground plane.          ")
    ForeGroundPlaneDistanceMode=property(doc="<b>Read Write Property:</b> Select mode for the foreground plane's distance.          ")
    ForeGroundTexture=property(doc="<b>Read Write Property:</b> ForeGround Texture          ")
    ForeGroundTransparent=property(doc="<b>Read Write Property:</b> Is the foreground transparent?          ")
    FrameColor=property(doc="<b>Read Write Property:</b> Frame color for camera.          ")
    FrameSizeMode=property(doc="<b>Read Write Property:</b> Frame size standard mode.          ")
    HUDs=property(doc="<b> List :</b> HUDs present in this camera          ")
    InteractiveMode=property(doc="<b>Read Write Property:</b> Interactive mode?          ")
    Interest=property(doc="<b>Read Write Property:</b> Direct camera's interest.          ")
    MagnifierPosX=property(doc="<b>Read Write Property:</b> 2D Magnifier X Position.          ")
    MagnifierPosY=property(doc="<b>Read Write Property:</b> 2D Magnifier Y Position.          ")
    MagnifierZoom=property(doc="<b>Read Write Property:</b> 2D Magnifier Zoom value.          ")
    MotionBlurIntensity=property(doc="<b>Read Write Property:</b> Motion Blur Intensity.          ")
    MouseLockCamera=property(doc="<b>Read Write Property:</b> Mouse lock for camera?          ")
    NearPlaneDistance=property(doc="<b>Read Write Property:</b> Near plane distance.          ")
    NumberOfSamples=property(doc="<b>Read Write Property:</b> Number of samples to oversample with.          ")
    OpticalCenterX=property(doc="<b>Read Write Property:</b> Optical Center X (mm).          ")
    OpticalCenterY=property(doc="<b>Read Write Property:</b> Optical Center Y (mm).          ")
    OrthoFactor=property(doc="Constant scale factor to be used with OrthoZoom for orthographic cameras.          ")
    OrthoZoom=property(doc="<b>Read Write Property:</b> Zoom factor of an orthographic camera.          ")
    PixelAspectRatio=property(doc="<b>Read Write Property:</b> Pixel aspect ratio.          ")
    ResolutionHeight=property(doc="<b>Read Write Property:</b> Resolution height.          ")
    ResolutionMode=property(doc="<b>Read Write Property:</b> Resolution standard mode.          ")
    ResolutionWidth=property(doc="<b>Read Write Property:</b> Resolution width.          ")
    Roll=property(doc="<b>Read Write Property:</b> Camera's roll on it's Z axis.          ")
    SafeAreaMode=property(doc="<b>Read Write Property:</b> Select mode for safe area.          ")
    SamplingType=property(doc="<b>Read Write Property:</b> Type of over sampling.          ")
    SqueezeRatio=property(doc="<b>Read Write Property:</b> Squeeze ratio.          ")
    SystemCamera=property(doc="<b>Read Only Property:</b> Indicate if this a producer (default or system) camera or a custom (user-created) camera.          ")
    TurnTable=property(doc="<b>Read Write Property:</b> Camera's rotation around its interest.          ")
    Type=property(doc="<b>Read Write Property:</b> Type of camera          ")
    Use2DMagnifier=property(doc="<b>Read Write Property:</b> Enable/Disable the 2D Magnifier.          ")
    UseAccumulationBuffer=property(doc="<b>Read Write Property:</b> Use accumulation buffer?          ")
    UseAntiAliasing=property(doc="<b>Read Write Property:</b> Use anti-aliasing?          ")
    UseDepthOfField=property(doc="<b>Read Write Property:</b> Use depth of field calculations?          ")
    UseFrameColor=property(doc="<b>Read Write Property:</b> Use frame color?          ")
    UseMotionBlur=property(doc="<b>Read Write Property:</b> Enable Motion Blur.          ")
    UseRealTimeMotionBlur=property(doc="<b>Read Write Property:</b> Enable Real-time Motion Blur.          ")
    ViewBackGroundPlaneMode=property(doc="<b>Read Write Property:</b> Background plane view mode          ")
    ViewCameraInterest=property(doc="<b>Read Write Property:</b> Show the camera interest?          ")
    ViewDisplaySafeArea=property(doc="<b>Read Write Property:</b> Display safe area?          ")
    ViewForeGroundPlaneMode=property(doc="<b>Read Write Property:</b> Foreground plane view mode          ")
    ViewNearFarPlane=property(doc="<b>Read Write Property:</b> Show near/far planes?          ")
    ViewOpticalCenter=property(doc="<b>Read Write Property:</b> View optical center?          ")
    ViewShowAxis=property(doc="<b>Read Write Property:</b> Show axis?          ")
    ViewShowGrid=property(doc="<b>Read Write Property:</b> Show grid?          ")
    ViewShowName=property(doc="<b>Read Write Property:</b> Show name?          ")
    ViewShowTimeCode=property(doc="<b>Read Write Property:</b> Show time code?          ")
    WindowHeight=property(doc="<b>Read Only Property:</b> Window height.          ")
    WindowWidth=property(doc="<b>Read Only Property:</b> Window width.          ")
    pass

class FBCameraSwitcher (FBModel):
    """
    Camera switcher.     
     This class is a wrapper around the system's camera switcher object. There can only be one switcher in a given scene. Any attempts at creating a new instance will return the existing one. See sample: CameraSwitcher.py.     
    """
    def FBCameraSwitcher(self):
        """
        Constructor.

        """
        pass

    def PlotToCamera(self,pCamera):
        """
        Plot the Camera Switcher animation onto a destination camera.
        The destination camera cannot be a system camera nor a camera currently used by the Camera Switcher.

        pCamera : Destination camera to plot on. 
        return : True if the plot operation has been processed successfully, false otherwise. 
        """
        pass

    CurrentCamera=property(doc="<b>Read Write Property:</b> Camera currently being used by the switcher. Set to NULL to turn on evaluate switch, otherwise manual switch.          ")
    CurrentCameraIndex=property(doc="<b>Read Write Property:</b> Camera index currently being used by the switcher. Set to -1 to turn on evaluate switch.          ")
    pass

class FBCharacter (FBConstraint):
    """
    A character is the link between a motion source and a character model.     
     <b>These classes are under development and may change dramatically between versions.</b> This class exposes part of the functionality associated with a Character. A character can possess a number of potential sources at the same time, such as an actor and another character, but with only one active at any given time. Before setting the InputType to the desired value, one must make sure to have previously set either the InputCharacter or the InputActor.To obtain the list of characters present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of characters in the property Characters. 
@code
FBSystem lSystem;
FBScene* lScene = lSystem.Scene;
for( int lIdx = 0; lIdx < lScene->Characters.GetCount(); ++lIdx )
{
    FBTrace( 'Character[%d]: '%s'\n', lIdx, (char*)lScene->Characters[lIdx] );
}
@endcode

The current character selected in the Character tool can be obtained via the FBApplication object. 
@code
FBApplication lApplication;
FBCharacter* lCharacter = lApplication.CurrentCharacter;
if( lCharacter )
{
    FBTrace( 'Current character is: '%s'\n', (char*)lCharacter->Name );
}
else
{
    FBTrace( 'No character currently selected\n' );
}
@endcode

See samples: CharacterMarkerSet.py, EnableGameModeOnSelectedCharacters_Z.py, MirrorPoseOverTime.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py.     
    """
    def FBCharacter(self,pName):
        """
        Constructor.

        pName : Name of new character. 
        """
        pass

    def AddCharacterExtension(self,pExt):
        """
        AddCharacterExtension.

        pExt : extension to be added to the character. 
        """
        pass

    def Clone(self):
        """
        Clone the character.

        """
        pass

    def ConnectControlRig(self,pControlSet,pUpdateLimit,pResetHierarchy):
        """
        Connect a Control-Rig to the character.

        pControlSet : The control set to connect. NULL will disconnect the Control-Rig from the character. 
        pUpdateLimit : Whether to update the models' limit for a character. E.g. the Pre rotation and post rotation. 
        pResetHierarchy : Whether to reset hierarchy for a character. 
        """
        pass

    def CopyAnimation(self):
        """
        Copy the animation from the input character to us.

        """
        pass

    def CreateAuxiliary(self,pEffectorId,pPivot,pAuxReachT,pAuxReachR):
        """
        Create auxiliary on effector.

        pEffectorId : The effector ID. 
        pPivot : Create effector or pivot (pivot offset should be set on IKPivot property, at creation default values are set). 
        pAuxReachT : Default auxiliary effector reach for translation (IK Blend T since MotionBuilder 2013). 
        pAuxReachR : Default auxiliary effector reach for rotation (IK Blend R since MotionBuilder 2013). 
        return : True if auxiliary was created (can fail if FBLastEffectorSetIndex limit reached). 
        """
        pass

    def CreateCharacterMarkerSet(self,pSetActive):
        """
        Create the Character Marker Set.

        pSetActive : True when new input should be set and active. 
        return : True when marker got created and connected to character. 
        """
        pass

    def CreateControlRig(self,pSetFKIK):
        """
        Create the Control-Rig.

        pSetFKIK : true to use FK/IK or false to use IK only. 
        return : current state of the flag after the operation (true if it did succeed). 
        """
        pass

    def CycleAnalysisCurrentCharacter(self):
        """
        Run Cycle Analysis on current character.

        """
        pass

    def DisconnectControlRig(self):
        """
        Disconnect the Control-Rig from the character.

        """
        pass

    def FBDelete(self):
        """
        Actual Character destructor.
        This method is used to delete the actual character object represented by an instance of FBCharacter.

        """
        pass

    def GetActiveBodyPart(self,pActivePart):
        """
        Get the active body part array.

        pActivePart : A pointer to an array of bool. On return, the index with a "true" value are active part. 
        """
        pass

    def GetCharacterMarkerSet(self,pForce):
        """
        Obtain Input CharacterMarkerSet.

        pForce : If True, will return the current CharacterMarkerSet even if the character is not in CharacterMarkerSet Input. 
        return : Return current Active CharacterMarkerSet, NULL if none. 
        """
        pass

    def GetCharacterize(self):
        """
        Get Characterize flag.

        return : Current state of the Characterize flag. 
        """
        pass

    def GetCharacterizeError(self):
        """
        Get error message for the previous SetCharacterizeOn operation.

        return : The string containing all errors and warnings. 
        """
        pass

    def GetCtrlRigModel(self,pBodyNodeId):
        """
        Get the model associated with each body part in the Control Rig of the character.

        pBodyNodeId : FBBodyNodeId
        return : The model in the Control Rig corresponding to the specified body part. 
        """
        pass

    def GetCurrentControlSet(self,pForce):
        """
        Obtain Input ControlSet.

        pForce : If True, will return the current ControlSet even if the character is not in ControlSet Input. 
        return : Return current Active ControlSet, NULL if none. 
        """
        pass

    def GetCycleAnalysisNode(self):
        """
        Get the Cycle Analysis Node from the current character.

        return : Cycle Analysis Node linked to the current character, or create a new node 
        """
        pass

    def GetEffectorModel(self,pEffectorId,pEffectorSetID):
        """
        Get the model associated with each effector in the Control Rig of the character.

        pEffectorId : The effector ID. 
        pEffectorSetID : Id of the ControlSet to obtain, if not specified the current one is taken. 
        return : The model in the Control Rig corresponding to the specified Effector. 
        """
        pass

    def GetExternalSolver(self):
        """
        Get a pointer to the external solver of a character, or NULL is no external solver is used on the character.

        return : The pointer of the current External Solver, NULL if it's the internal solver. 
        """
        pass

    def GetFKVisibility(self):
        """
        Get the FK visibility state.

        return : The FK visibility state. 
        """
        pass

    def GetFloorContactModel(self,pMemberIndex):
        """
        Get the model associated with the floor contact ID.

        pMemberIndex : Id of the floor contact 
        return : The model associated with the floor contact ID 
        """
        pass

    def GetGoalModel(self,pBodyNodeId):
        """
        Get the goal model associated with each body part in the Character Marker Set of the character.

        pBodyNodeId : FBBodyNodeId
        return : The model in the Character Marker Set corresponding to the specified body part. 
        """
        pass

    def GetIKVisibility(self):
        """
        Get the IK visibility state.

        return : The IK visibility state. 
        """
        pass

    def GetIndexByModel(self,pModel):
        """
        Get the index associated with Given Model.

        pModel : FBModel
        return : The model linked to the specified body part. 
        """
        pass

    def GetModel(self,pBodyNodeId):
        """
        Get the model associated with each body part of the character.

        pBodyNodeId : FBBodyNodeId
        return : The model linked to the specified body part. 
        """
        pass

    def GetParentROffset(self,pBodyNodeId,pRVector):
        """
        pBodyNodeId : FBBodyNodeId
        pRVector : FBRVector
        """
        pass

    def GetROffset(self,pBodyNodeId,pRVector):
        """
        pBodyNodeId : FBBodyNodeId
        pRVector : FBRVector
        """
        pass

    def GetSOffset(self,pBodyNodeId,pSVector):
        """
        pBodyNodeId : FBBodyNodeId
        pSVector : FBSVector
        """
        pass

    def GetSkeletonVisibility(self):
        """
        Get the skeleton visibility state.

        return : The skeleton visibility state. 
        """
        pass

    def GetSkinModelList(self,pSkinModelList):
        """
        Get the skin model associated with character bones.
        Could be deformable model connected to bone via cluster, or non deformable model parented directly under the bones.

        pSkinModelList : List to be filled up. (will not be cleared) 
        """
        pass

    def GetTOffset(self,pBodyNodeId,pTVector):
        """
        pBodyNodeId : FBBodyNodeId
        pTVector : FBTVector
        """
        pass

    def GetTransformOffset(self,pBodyNodeId,pOffsetMatrix):
        """
        pBodyNodeId : FBBodyNodeId
        pOffsetMatrix : FBMatrix
        """
        pass

    def GoToStancePose(self,pPushUndo,pIncludeCharacterExtensions):
        """
        Set the character in stance pose.

        pPushUndo : Should we push an undo transaction on the undo stack? Don't push undo in non UI thread. 
        pIncludeCharacterExtensions : Should the character extensions go to stance pose too? 
        """
        pass

    def IsParentNodeOffset(self,pNodeId):
        """
        Check if there is an offset on Parent.

        pNodeId : Node Id to Check. 
        return : True if there is an offset on Parent. 
        """
        pass

    def IsRotationPin(self,pEffectorIndex):
        """
        Return true if the object is Pinned in Rotation (Manipulation).

        pEffectorIndex : Given Index to obtain Model 
        return : True if the effector is pinned in Rotation 
        """
        pass

    def IsTranslationPin(self,pEffectorIndex):
        """
        Return true if the object is Pinned in Translation (Manipulation).

        pEffectorIndex : Given Index to obtain Model 
        return : True if the effector is pinned in Translation 
        """
        pass

    def PlotAnimation(self,pPlotWhere,pPlotOptions):
        """
        Plot the animation of the character.
        When plotting onto Control Rig while the Control Rig being the source of the Character, only the selected properties, based on the active keying group, will be plotted.

        pPlotWhere : Where to plot a character, control rig or Skeleton 
        pPlotOptions : Option parameters for plotting 
        return : True if the operation completed successfully. 
        """
        pass

    def ReadyForRetarget(self):
        """
        Test if character is ready for the Retarget operation (basically, is it in character input ?).

        return : True if the character is ready. 
        """
        pass

    def RemoveCharacterExtension(self,pExt):
        """
        Get the model associated with each body part of the character.

        pExt : extension to be removed to the character. 
        """
        pass

    def ResetProperties(self,pType):
        """
        Reset the properties of the character.

        pType : Speficy which properties will be reset. 
        """
        pass

    def Retarget(self,pOnBaseLayer):
        """
        Retarget the animation from the input character to us.

        pOnBaseLayer : if true, keys corrections will be made on base layer; else they will be made on another layer. 
        """
        pass

    def SelectModels(self,pSelect,pApplyToCharacter,pApplyToRig,pApplyToExtensions):
        """
        Select the objects that make a character.

        pSelect : True to select, false to deselect. 
        pApplyToCharacter : TSould the character contraint be selected ? 
        pApplyToRig : should The rig (and its children) be selected ? 
        pApplyToExtensions : Should the character extensions (and their children) be selected ? 
        """
        pass

    def SetCharacterizeOff(self):
        """
        Set Characterize flag off.

        """
        pass

    def SetCharacterizeOn(self,pSetAsBiped):
        """
        Set the Characterize flag on.

        pSetAsBiped : true to use biped characterization or false to use quadruped. 
        return : current state of the flag after the operation (true if it did succeed).
        """
        pass

    def SetExternalSolver(self,pIndex):
        """
        Set character external solver.

        pIndex : Index of external solver. 
        """
        pass

    def SetExternalSolver(self,pSolver):
        """
        Set character solver.

        pSolver : Character solver that will be used by the character. 
        """
        pass

    def SetFKVisibility(self,pState):
        """
        Set the FK visibility state.

        pState : The FK visibility state. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetIKVisibility(self,pState):
        """
        Set the IK visibility state.

        pState : The IK visibility state. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetRotationPin(self,pEffectorIndex,pValue):
        """
        Set the object Pinned in Rotation (Manipulation) status.

        pEffectorIndex : Given Index to obtain Model. 
        pValue : The object Pinned in Rotation status. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetSkeletonVisibility(self,pState):
        """
        Set the skeleton visibility state.

        pState : The skeleton visibility state. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    def SetTranslationPin(self,pEffectorIndex,pValue):
        """
        Set the object Pinned in Translation (Manipulation) status.

        pEffectorIndex : Given Index to obtain Model 
        pValue : The object Pinned in Translation status. 
        return : True if the operation is successful, false otherwise. 
        """
        pass

    ActiveInput=property(doc="<b>Read Write Property:</b> Is the character input active?          ")
    CharacterExtensions=property(doc="<b>List:</b> Character Extensions in the character.          ")
    ContactBehaviour=property(doc="<b>Read Write Property:</b> Contact Behavior selection.          ")
    FKFingerMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered intermediate finger phalanges.          ")
    FKFingerTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered finger tip phalanges.          ")
    FKThumbTipMultiplier=property(doc="<b>Read Write Property:</b> Used to augment the amount of FK propagation for unmarkered thumb tip phalanges.          ")
    HipsTranslationMode=property(doc="<b>Read Write Property:</b> Hips Translation Mode.          ")
    HumanFingerLimits=property(doc="<b>Read Write Property:</b> Enables/Disables human finger limits during actor solve.          ")
    InputActor=property(doc="<b>Read Write Property:</b> The index of the actor used for the input.          ")
    InputCharacter=property(doc="<b>Read Write Property:</b> The index of the character used for the input.          ")
    InputType=property(doc="<b>Read Write Property:</b> The input type for the character (ex: Actor).          ")
    InverseLeftElbow=property(doc="<b>Read Write Property:</b> Is left elbow inverted.          ")
    InverseLeftKnee=property(doc="<b>Read Write Property:</b> Is left knee inverted.          ")
    InverseRightElbow=property(doc="<b>Read Write Property:</b> Is right elbow inverted.          ")
    InverseRightKnee=property(doc="<b>Read Write Property:</b> Is right knee inverted.          ")
    KeyingMode=property(doc="<b>Read Write Property:</b> The current keying mode.          ")
    LeftElbowKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Left elbow.          ")
    LeftHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    LeftKneeKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Left knee.          ")
    LockX=property(doc="<b>Read Write Property:</b> Lock character skeleton in place on X axis.          ")
    LockY=property(doc="<b>Read Write Property:</b> Lock character skeleton in place on Y axis.          ")
    LockZ=property(doc="<b>Read Write Property:</b> Lock character skeleton in place on Z axis.          ")
    MirrorMode=property(doc="<b>Read Write Property:</b> is in mirror mode.          ")
    RightElbowKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Right elbow.          ")
    RightHandIndexIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandIndexRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddlePinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandMiddleRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandPinkyRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingIndex=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingMiddle=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingPinky=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightHandRingRing=property(doc="<b>Read Write Property:</b> Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs.          ")
    RightKneeKillPitch=property(doc="<b>Read Write Property:</b> is Pitch used for Right knee.          ")
    RollSolver=property(doc="<b>Read Write Property:</b> Roll Solver selection.          ")
    ShoulderCorrection=property(doc="<b>Read Write Property:</b> shoulder correction values.          ")
    SyncMode=property(doc="<b>Read Write Property:</b> is character in sync mode.          ")
    WriteReference=property(doc="<b>Read Write Property:</b> are we writing back on reference.          ")
    pass

class FBCharacterFace (FBConstraint):
    """
    Animates a character face using an actor as input.     
     <b>These classes are under development and may change dramatically between versions.</b>      
    """
    def FBCharacterFace(self,pName):
        """
        Constructor.

        pName : Name of new character. 
        """
        pass

    def ClusterGroupAdd(self,pList,pName):
        """
        Add a cluster group to the character face.

        pList : List of clusters to add to this group. 
        pName : Optional name to assign to this cluster group. 
        return : <b>Index</b> of the new cluster group <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ClusterGroupFindByName(self,pName):
        """
        Find a cluster group by name.

        pName : Name to search for on the face. 
        return : <b>Index</b> of the matching cluster group. <b>-1</b> if not found. 
        """
        pass

    def ClusterGroupGetCount(self):
        """
        Retrieve the total number of cluster groups.

        return : Number of cluster groups on the face. 
        """
        pass

    def ClusterGroupGetName(self,pClusterGrpId):
        """
        Retrieve the name of a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        return : Name of the specified cluster group. 
        """
        pass

    def ClusterGroupRemove(self,pClusterGrpId):
        """
        Remove a cluster group from the character face.

        pClusterGrpId : Index of the cluster group to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ClusterGroupSetName(self,pClusterGrpId,pName):
        """
        Set the name of a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pName : New name for the cluster group. 
        return : True of the operation completed successfully. 
        """
        pass

    def ClusterGroupSnapRest(self,pClusterGrpId):
        """
        Set a cluster group's rest pose to the current pose.

        pClusterGrpId : Index of the cluster group to modify. 
        return : True if the operation completed succesfully. 
        """
        pass

    def ClusterShapeAdd(self,pClusterGrpId,pName):
        """
        Add a cluster shape to a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pName : Optional name to assign to the shape. 
        return : <b>Index</b> of the new shape. <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ClusterShapeFindByName(self,pClusterGrpId,pName):
        """
        Find a cluster shape in a cluster group by name.

        pClusterGrpId : Index of the cluster group to search. 
        pName : Name to search for in the cluster group. 
        return : <b>Index</b> of the matching shape. <b>-1</b> if not found. 
        """
        pass

    def ClusterShapeGetCount(self,pClusterGrpId):
        """
        Retrieve the total number of shapes in a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        return : Number of shapes in the specified cluster group. 
        """
        pass

    def ClusterShapeGetName(self,pClusterGrpId,pClusterShapeId):
        """
        Retrieve the name of a shape in a cluster group.

        pClusterGrpId : Index of the cluster group to query. 
        pClusterShapeId : Index of the cluster shape to query. 
        return : Name of the specified shape. 
        """
        pass

    def ClusterShapeRemove(self,pClusterGrpId,pClusterShapeId):
        """
        Remove a cluster shape from a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pClusterShapeId : Index of the shape in the cluster group to remove. 
        return : True of the operation completed succesfully. 
        """
        pass

    def ClusterShapeSetName(self,pClusterGrpId,pClusterShapeId,pName):
        """
        Set the name of a shape in a cluster group.

        pClusterGrpId : Index of the cluster group to modify. 
        pClusterShapeId : Index of the cluster shape to modify. 
        pName : Name to assign to the cluster shape. 
        return : True if the operation completed successfully. 
        """
        pass

    def ClusterShapeSnap(self,pClusterGrpId,pClusterShapeId):
        """
        Record the current pose of the cluster group to a cluster shape.

        pClusterGrpId : Index of the cluster group to record. 
        pClusterShapeId : Index of the cluster shape to record the pose. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionAdd(self,pName):
        """
        Add an expression to the face.

        pName : Optional name to assign to the new expression. 
        return : <b>Index</b> of the new expression. <b>-1</b> if the operation failed to complete. 
        """
        pass

    def ExpressionFindByName(self,pName):
        """
        Find an expression on the face by name.

        pName : Name of the expression to search for. 
        return : <b>Index</b> of the matching expression. <b>-1</b> if not found. 
        """
        pass

    def ExpressionGetCount(self):
        """
        Retrieve the total number of expressions on the face.

        return : Number of expressions on the face. 
        """
        pass

    def ExpressionGetName(self,pExpressionId):
        """
        Retrieve the name of an expression.

        pExpressionId : Index of the expression to query. 
        return : Name of the specified expression. 
        """
        pass

    def ExpressionGetShapeWeight(self,pExpressionId,pGrpId,pShapeId):
        """
        Retrieve the weight of a shape to an expression.

        pExpressionId : Index of the expression. 
        pGrpId : Index of the blendshape or cluster group containing the shape of interest. 
        pShapeId : Index of the blendshape or cluster shape. 
        return : Weight of the desired shape to an expression. A weight of 0.0 represents 0%, while a weight of 1.0 represents 100%. Returns 0.0 if the weight cannot be found. 
        """
        pass

    def ExpressionRemove(self,pExpressionId):
        """
        Remove an expression from the face.

        pExpressionId : Index of the expression to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionSetName(self,pExpressionId,pName):
        """
        Set the name of an expression.

        pExpressionId : Index of the expression to modify. 
        pName : Name to assign to the expression. 
        return : True if the operation completed successfully. 
        """
        pass

    def ExpressionSetShapeWeight(self,pExpressionId,pGrpId,pShapeId,pValue):
        """
        Assign the weight of a shape to an expression.

        pExpressionId : Index of the expression to modify. 
        pGrpId : Index of the blendshape or cluster group containing the shape of interest. 
        pShapeId : Index of the blendshape or cluster shape to weight. 
        pValue : Weight of the shape to assign to this expression. A weight of 0.0 represents 0%, while a weight of 1.5 represents 150%. The weight cannot be less than 0.0; if so, the weight will be clamped to 0.0. 
        return : True if the operation completed successfully. 
        """
        pass

    def FBDelete(self):
        """
        Actual Character Face destructor.
        This method is used to delete the actual character face object represented by an instance of FBCharacterFace.

        """
        pass

    def GotoRest(self):
        """
        Set the character face back to its rest shape.

        """
        pass

    def PlotAnimation(self):
        """
        Plot the animation of the character face.

        return : True if the operation completed successfully. 
        """
        pass

    def ShapeFindByName(self,pShapeGrpId,pName):
        """
        Find a shape in a blendshape group by name.

        pShapeGrpId : Index of the blendshape group to search. 
        pName : Name to search for. 
        return : <b>Index</b> of the shape, <b>-1</b> if not found. 
        """
        pass

    def ShapeGetCount(self,pShapeGrpId):
        """
        Retrieve the total number of shapes in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        return : Number of shapes in the specified blendshape group. 
        """
        pass

    def ShapeGetName(self,pShapeGrpId,pShapeId):
        """
        Retrieve the name of the shape in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        pShapeId : Index of the shape in the blendshape group to query. 
        return : Name of the specified shape. 
        """
        pass

    def ShapeGroupAdd(self,pList,pName):
        """
        Add a blendshape model group for each input model.

        pList : List of models to create a blendshape model group. 
        pName : Unused. Instead, use the ShapeGroupGetName member function to set the name of each added blendshape model group individually. 
        return : True if the operation completed successfully, false otherwise. 
        """
        pass

    def ShapeGroupFindByName(self,pName):
        """
        Find a blendshape group by name.

        pName : Name to search for. 
        return : <b>Index</b> of the blendshape group, <b>-1</b> if not found. 
        """
        pass

    def ShapeGroupGetCount(self):
        """
        Retrieve the total number of blendshape groups on this character face.

        return : Number of blendshape groups on this character face. 
        """
        pass

    def ShapeGroupGetName(self,pShapeGrpId):
        """
        Retrieve the name of a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        return : Name of the blendshape group. 
        """
        pass

    def ShapeGroupRemove(self,pShapeGrpId):
        """
        Remove a blendshape model group.

        pShapeGrpId : Index of the blendshape group to remove. 
        return : True if the operation completed successfully. 
        """
        pass

    def ShapeGroupSetName(self,pShapeGrpId,pName):
        """
        Set the name of a blendshape group.

        pShapeGrpId : Index of the blendshape group to modify. 
        pName : Name to set on the blendshape group. 
        return : True if the operation completed successfully. 
        """
        pass

    def ShapeSetName(self,pShapeGrpId,pShapeId,pName):
        """
        Set the name of the shape in a blendshape group.

        pShapeGrpId : Index of the blendshape group to query. 
        pShapeId : Index of the shape in the blendshape group to set. 
        pName : Name to set on the shape. 
        return : True if the operation completed successfully. 
        """
        pass

    ActiveInput=property(doc="<b>Read Write Property:</b> Is the character input active?          ")
    InputActorFace=property(doc="<b>Read Write Property:</b> The index of the actor used for the input.          ")
    pass

class FBConstraintSolver (FBConstraint):
    """
    Base class for constraint solver.     
         
    """
    def FBConstraintSolver(self,pName):
        """
        pName : str
        """
        pass

    pass

class FBDeviceOptical (FBDevice):
    """
    Optical device class.     
         
    """
    def FBDeviceOptical(self,pName):
        """
        Constructor.

        pName : Unique name of optical device. 
        """
        pass

    def DeviceOperation(self,pOperation):
        """
        Operate device.
        This is an operation such as Init, Start, Done, Reset, etc.

        pOperation : Operation to have device perform. 
        return : Current state : <b true if online. 
        """
        pass

    def DeviceOpticalBeginSetup(self):
        """
        Begin device setup.

        """
        pass

    def DeviceOpticalEndSetup(self):
        """
        End device setup.

        """
        pass

    def DeviceOpticalRecordFrame(self,pTime,pDeviceNotifyInfo):
        """
        Record a frame of information from device.
        Virtual function that derived class may overide

        pTime : Time of evaluation. 
        pDeviceNotifyInfo : Notification information when thread was called. 
        """
        pass

    def FBCreate(self):
        """
        Open Reality Creation function.

        return : Outcome of creation (true/false). 
        """
        pass

    def FBDestroy(self):
        """
        Open Reality destruction function.

        """
        pass

    def RecordingDoneAnimation(self,pAnimationNode):
        """
        When recording, finish animation.

        pAnimationNode : Animation node to write information to. 
        """
        pass

    def RecordingInitAnimation(self,pAnimationNode):
        """
        When recording, initialize animation.

        pAnimationNode : Animation node to read information from. 
        """
        pass

    AutoAntialiasing=property(doc="<b>Property:</b> Is it auto-antialiasing?          ")
    DampingTime=property(doc="<b>Property:</b> Damping time for device.          ")
    ForceOpticalSamplingRate=property(doc="<b>Property:</b> Force the use of the optical sampling rate?          ")
    MarkerTimeStamp=property(doc="<b>Property:</b> TimeStamp for marker.          ")
    Markers=property(doc="<b>List:</b> Markers.          ")
    ModelOptical=property(doc="<b>Property:</b> Optical model for manipulation.          ")
    OpticalSamplingRate=property(doc="<b>Property:</b> Resampling rate for optical device.          ")
    SkipFrame=property(doc="<b>Property:</b> Skip Record Frame          ")
    SupportOcclusion=property(doc="<b>Property:</b> Does the device support occulsion?          ")
    UseMarkerTimeStamp=property(doc="<b>Property:</b> Use the individual marker timestamps?          ")
    pass

class FBHUDFlashElement (FBHUDElement):
    """
    Heads Up display.     
     Flash HUD element. Display a flash (swf) file rendered on the HUD. See sample: HUDElements.py.     
    """
    def FBHUDFlashElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD flash element. 
        """
        pass

    FilePath=property(doc="<b>Read Write Property:</b> Path to load the swf file from          ")
    pass

class FBHUDRectElement (FBHUDElement):
    """
    Heads Up display.     
     Rectangle HUD element. See sample: HUDElements.py.     
    """
    def FBHUDRectElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD rectangle element. 
        """
        pass

    Color=property(doc="<b>Read Write Property:</b> Color of the rectangluar region.          ")
    pass

class FBHUDTextElement (FBHUDElement):
    """
    Heads Up display.     
     Text element. Render text with a background rectangle to the HUD. See samples: HUDElements.py, HUDTextElement.py, HUD.py.     
    """
    def FBHUDTextElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD text element. 
        """
        pass

    def GetFontList(self):
        """
        Returns a list of supported fonts.

        """
        pass

    AdjustWidthToFitText=property(doc="<b>Read Write Property:</b> If On it it will adjust the width of a text element so that a text character's aspect ratio does not change as the content grows or shrinks.          ")
    BackgroundColor=property(doc="<b>Read Write Property:</b> Background text color.          ")
    Color=property(doc="<b>Read Write Property:</b> Text color.          ")
    Content=property(doc="<b>Read Write Property:</b> C like format to display like in printf.          ")
    Font=property(doc="<b>Read Write Property:</b> Specifies the font.          ")
    ForceTimeCodeDisplay=property(doc="<b>Read Write Property:</b> Specifies if the display of time-related reference property will be in timecode format.          ")
    pass

class FBHUDTextureElement (FBHUDElement):
    """
    Heads Up display.     
     Texture HUD element. Display a texture on a rectangle on the HUD. See sample: HUDElements.py.     
    """
    def FBHUDTextureElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD texture element. 
        """
        pass

    Texture=property(doc="<b>Read Write Property:</b> Texture to display.          ")
    pass

class FBLayeredTexture (FBTexture):
    """
    LayeredTexture class.     
     This class is used to encapsulate list of textures. User could subclass this class to support customized blending & compostion modes. See /OpenRealitySDK/Samples/miscellaneous/texture_template/ for example. See sample: LayeredTexture.py.     
    """
    def FBLayeredTexture(self,pName):
        """
        Constructor.

        pName : Name of texture media. Can be a NULL pointer. If set, this will create a FBVideo object used as the Video property. 
        """
        pass

    def Clone(self):
        """
        Clone the current texture.
        Duplicates the current texture.

        return : Newly created texture. 
        """
        pass

    def FBDelete(self):
        """
        Open Reality deletion function.

        """
        pass

    def SetLayerConfigDirty(self):
        """
        Set layer config dirty to trigger new composition.

        """
        pass

    BackgroundColor=property(doc="<b>Read/Write Property:</b> Animatable Background color which is used to clear color buffer before composition.          ")
    Layers=property(doc="<b>Read/Write Property:</b> Textures Layers.          ")
    pass

class FBLight (FBModel):
    """
    Light class.     
         
    """
    def FBLight(self,pName):
        """
        Constructor.

        pName : Name of light. 
        """
        pass

    AreaLightShape=property(doc="<b>Read Write Property:</b> Area light shape.          ")
    AttenuationType=property(doc="<b>Read Write Property:</b> Type of attenuation for the light.          ")
    BottomBarnDoor=property(doc="<b>Read Write Property:</b> Angle of bottom barn door.          ")
    CastLightOnObject=property(doc="<b>Read Write Property:</b> Cast light on object?          ")
    CastShadows=property(doc="<b>Read Write Property:</b> Cast shadows on object?          ")
    ConeAngle=property(doc="<b> DEPRECATED </b> Equivalent to OuterAngle.          ")
    DiffuseColor=property(doc="<b>Read Write Property:</b> Color: Diffuse color.          ")
    DrawFrontFacingVolumetric=property(doc="<b>Read Write Property:</b> Draw front facing volumetric light?          ")
    DrawGroundProjection=property(doc="<b>Read Write Property:</b> Draw ground projection of gobo?          ")
    DrawVolumetricLight=property(doc="<b>Read Write Property:</b> Draw volumetric light with gobo?          ")
    EnableBarnDoor=property(doc="<b>Read Write Property:</b> Whether or not enable barn door.          ")
    FogIntensity=property(doc="<b>Read Write Property:</b> Intensity of the fog (spot light).          ")
    GoboMedia=property(doc="<b>Read Write Property:</b> Media to use as a Gobo with the light.          ")
    InnerAngle=property(doc="<b>Read Write Property:</b> Inner Cone angle for light.          ")
    Intensity=property(doc="<b>Read Write Property:</b> Light intensity.          ")
    LeftBarnDoor=property(doc="<b>Read Write Property:</b> Angle of left barn door.          ")
    LightType=property(doc="<b>Read Write Property:</b> Type of light.          ")
    OuterAngle=property(doc="<b>Read Write Property:</b> Outer Cone angle for light.          ")
    RightBarnDoor=property(doc="<b>Read Write Property:</b> Angle of right barn door.          ")
    TopBarnDoor=property(doc="<b>Read Write Property:</b> Angle of top barn door.          ")
    pass

class FBModelCube (FBModel):
    """
    Cube model class.     
    See samples: FBGroup.py, FBModelCube.py.     
    """
    def FBModelCube(self,pName):
        """
        Constructor.

        pName : Name of cube. 
        """
        pass

    pass

class FBModelMarker (FBModel):
    """
    Model marker class.     
    See sample: FBCamera.py.     
    """
    def FBModelMarker(self,pName):
        """
        Constructor.

        pName : Name of model marker. If pObject is not NULL, pName will be ignored. 
        """
        pass

    Color=property(doc="<b>Read Write Property:</b> Color of model marker.          ")
    IKPivot=property(doc="<b>Read Write Property:</b> marker Pivot Offset.          ")
    Length=property(doc="<b>Read Write Property:</b> Length for capsule (not related to scaling).          ")
    Look=property(doc="<b>Read Write Property:</b> Look of model marker.          ")
    ResLevel=property(doc="<b>Read Write Property:</b> Resolution level of model marker.          ")
    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).          ")
    Type=property(doc="<b>Read Write Property:</b> Type of model marker.          ")
    pass

class FBModelNull (FBModel):
    """
    Null object class.     
         
    """
    def FBModelNull(self,pName):
        """
        Constructor.

        pName : Name of null. 
        """
        pass

    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).          ")
    pass

class FBModelOptical (FBModel):
    """
    Optical model class.     
         
    """
    def FBModelOptical(self,pName):
        """
        Constructor.

        pName : Name of optical model. 
        """
        pass

    def ClearSegments(self,pUnUsedOnly):
        """
        Clear the segments (by default only the unused).

        pUnUsedOnly : Clear only the unused segments if <b>true</b>(default=true). 
        """
        pass

    def CreateRigidBody(self,pRigidBodyName,pMarkers):
        """
        Create a new rigid body from the given optical markers.

        pRigidBodyName : The name for the new rigid body to create. If left empty, the default "Rigid Body" name will be used. 
        pMarkers : The optical markers for creating the new rigid body. 
        return : The created rigid body if successful, and invalid rigid body otherwise. You can use the FBRigidBody.IsValid() method to test if the returned rigid body object is valid or not. 
        """
        pass

    def ExportSetup(self):
        """
        Setup exportation from optical model.

        return : <b>true</b> if successful. 
        """
        pass

    def ImportSetup(self):
        """
        Setup importation for optical model.

        return : <b>true</b> if successful. 
        """
        pass

    MarkerSize=property(doc="<b>Read Write Property:</b> Size of markers.          ")
    Markers=property(doc="<b>List:</b> Markers.          ")
    RigidBodies=property(doc="<b>List:</b> Rigid bodies.          ")
    SamplingPeriod=property(doc="<b>Read Write Property:</b>Sampling period.          ")
    SamplingStart=property(doc="<b>Read Write Property:</b> Sampling start time.          ")
    SamplingStop=property(doc="<b>Read Write Property:</b>Sampling stop time.          ")
    Segments=property(doc="<b>List:</b> Segments.          ")
    pass

class FBModelPath3D (FBModel):
    """
    Path 3D model class.     
         
    """
    def FBModelPath3D(self,pName):
        """
        Constructor.
        Python sample code: 
@code
from pyfbsdk import *

path = FBModelPath3D('Test')
## After creation, a path always contain two default keys.
## At this point, path.PathKeyGetCount() will be 2.
path.Show = True
## Reposition the two default keys
path.PathKeySet(0,FBVector4d(0,0,50,0))
path.PathKeySet(1,FBVector4d(50,0,0,0))
## Add new keys at start and end of the path
path.PathKeyStartAdd(FBVector4d(0,0,100,0))
path.PathKeyEndAdd(FBVector4d(100,0,0,0))
## Insert keys inbetween existing keys
path.PathKeyInsertAfter(1,FBVector4d(0,25,50,0))
path.PathKeyInsertAfter(2,FBVector4d(50,25,0,0))
@endcode

        pName : Name of Path 3D. 
        """
        pass

    def ConvertSegmentPercentToTotalPercent(self,pPercent,pEvaluateInfo):
        """
        Converting one key type Segment (time) to Total (percent).

        pPercent : Double value (as time) 
        pEvaluateInfo : FBEvaluateInfo
        return : Double value which represents the corresponding percentage 
        """
        pass

    def ConvertToSegmentPercentFactor(self):
        """
        Get factor for multiplying the derivative of a key for segment mode.

        return : Returns the derivative multiplication factor 
        """
        pass

    def ConvertToTotalPercentFactor(self):
        """
        Get factor for multiplying the derivative of a key for total mode.

        return : Returns the time factor 
        """
        pass

    def ConvertTotalPercentToSegmentPercent(self,pPercent,pEvaluateInfo):
        """
        Converting one key type Total (percent) to Segment (time).

        pPercent : Double value (as percentage) 
        pEvaluateInfo : FBEvaluateInfo
        return : Double value which represents the corresponding time. 
        """
        pass

    def GetSelectedPathKeyCount(self):
        """
        Query the number of keys present in the selected path.

        return : Returns the number of keys in the selected path  
        """
        pass

    def InsertNewEndKey(self):
        """
        Insert a new key at the end of the path.

        return : Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0. 
        """
        pass

    def InsertNewStartKey(self):
        """
        Insert a new key at the start of the path.

        return : Returns 0 since the new key becomes the first key. If path is invalid, returns 0. 
        """
        pass

    def PathKeyClear(self):
        """
        Clear the path keys.

        """
        pass

    def PathKeyEndAdd(self,pTLocal):
        """
        Adds a new key to the end of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the left tangent of the last key.

        pTLocal : Vector value for the new added Key 
        return : Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0. 
        """
        pass

    def PathKeyGet(self,pKeyIndex):
        """
        Get path's key vector for at a particular key index.

        pKeyIndex : Key ID to set with 
        return : Return the vector containing the value of the path key. 
        """
        pass

    def PathKeyGetControlNode(self,pKeyIndex):
        """
        Get the path key's control node.
        Only works when KeyPropertyBehavior is eVector.

        pKeyIndex : Key ID to get 
        return : Path key's corresponding control node if successful, otherwise NULL. 
        """
        pass

    def PathKeyGetCount(self):
        """
        Query the number of keys present in the path.

        return : Number of keys present in the path 
        """
        pass

    def PathKeyGetLeftTangent(self,pKeyIndex):
        """
        Get the path key left tangent's vector value for designated index.

        pKeyIndex : Key ID at which left tangent value is required 
        return : Vector containing value of left tangent 
        """
        pass

    def PathKeyGetLeftTangentLength(self,pKeyIndex):
        """
        Query the length of the left tangent.

        pKeyIndex : Key ID to set with 
        return : Double value of the length of left tangent 
        """
        pass

    def PathKeyGetProperty(self,pKeyIndex):
        """
        Get the path key's corresponding property.
        Only works when KeyPropertyBehavior is eVector.

        pKeyIndex : Key ID to get 
        return : Path key's corresponding property if successful, otherwise NULL. 
        """
        pass

    def PathKeyGetRightTangent(self,pKeyIndex):
        """
        Get the path key right tangent's vector value for designated index.

        pKeyIndex : Key ID to set with 
        return : Vector containing value of left tangent 
        """
        pass

    def PathKeyGetRightTangentLength(self,pKeyIndex):
        """
        Query the value of the right tangent.

        pKeyIndex : Key ID to set with 
        return : Double value of the length of right tangent 
        """
        pass

    def PathKeyGetXYZDerivative(self,pKeyIndex):
        """
        Get vector in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.

        pKeyIndex : Key ID to set with 
        return : Vector with value for path's tangent XYZ derivatives 
        """
        pass

    def PathKeyInsertAfter(self,pKeyIndex,pTLocal):
        """
        Adds a new key immediately after the specified key ID (with time gap of 1 sec).
        The following keys are all shifted by 1 sec.

        pKeyIndex : Key ID to insert after. If key ID < 0 then the behavior is the same as PathKeyStartAdd. If key ID >= PathKeyGetCount-1 then the behavior is the same as PathKeyEndAdd. 
        pTLocal : Vector value for the new added Key 
        return : Returns the newly inserted key ID. 
        """
        pass

    def PathKeyRemove(self,pKeyIndex):
        """
        Remove key at a particular index.

        pKeyIndex : Key ID at which key is to be removed. 
        """
        pass

    def PathKeyRemoveSelected(self):
        """
        Remove the selected keys from the path.

        """
        pass

    def PathKeySet(self,pKeyIndex,pTLocal,pUpdate):
        """
        Set the local coordinate vector values for path at a particular key index.

        pKeyIndex : Key ID to set with 
        pTLocal : Vector to use to set values to Key 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetControlNode(self,pKeyIndex,pControlNode):
        """
        Set the path key's control node.
        Only works when KeyPropertyBehavior is eVector and AutoControlNode is disabled.

        pKeyIndex : Key ID to set 
        pControlNode : Model to set as path key's control node. 
        return : True if successful, otherwise false. 
        """
        pass

    def PathKeySetLeftRightTangent(self,pKeyIndex,pKeyTLocal,pLeftTangentTLocal,pRightTangentTLocal,pUpdate):
        """
        Set path's vectors for key, left tangent and right tangent at a particular key index.

        pKeyIndex : Key ID to set key for left and right tangents 
        pKeyTLocal : Vector to use to set values to Key 
        pLeftTangentTLocal : Vector to use to set values to Key Left Tangent 
        pRightTangentTLocal : Vector to use to set values to Key Right Tangent 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetLeftTangent(self,pKeyIndex,pTLocal,pUpdate):
        """
        Set path's key left tangent vector for designated index.

        pKeyIndex : Key ID at which left tangent is to be set 
        pTLocal : Vector to use to set values to Key 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetRightTangent(self,pKeyIndex,pTLocal,pUpdate):
        """
        Set 3D path's key right tangent vector for designated index.

        pKeyIndex : Key ID at which right tangent is to be set 
        pTLocal : Vector to use to set values to Key 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetXDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        Set derivative in X coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.

        pKeyIndex : Key ID to set with 
        pDerivative : Value of the derivative to apply to tangent 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetXYZDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        Set derivative in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.

        pKeyIndex : Key ID to set with 
        pDerivative : Value of the derivative to apply to tangent 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetYDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        Set derivative in Y coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.

        pKeyIndex : Key ID to set with 
        pDerivative : Value of the derivative to apply to tangent 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeySetZDerivative(self,pKeyIndex,pDerivative,pUpdate):
        """
        Set derivative in Z coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.

        pKeyIndex : Key ID to set with 
        pDerivative : Value of the derivative to apply to tangent 
        pUpdate : <b>true</b> if geometry update is required, <b>false</b> if not required (default=true) 
        """
        pass

    def PathKeyStartAdd(self,pTLocal):
        """
        Adds a new key to the start of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the right tangent of the first key.

        pTLocal : Vector value for the new added Key 
        return : Returns 0 since the new key becomes the first key. If path is invalid, returns 0. 
        """
        pass

    def Segment_GlobalPathEvaluate(self,pSegmentPercent,pEvaluateInfo):
        """
        Get the path's vector at a particular point within the curve, in global coordinates.

        pSegmentPercent : Double value (as time) at which the path vector would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def Segment_GlobalPathEvaluateDerivative(self,pSegmentPercent,pEvaluateInfo):
        """
        Get the path's derivative at a particular point within the curve, in global coordinates.

        pSegmentPercent : Double value (as time) at which the path derivative would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def Segment_IsPathKey(self,pSegmentPercent,pEvaluateInfo):
        """
        Query whether a percentage value has a key associated at that point in the path.

        pSegmentPercent : Double value (as time) at which the path would be queried for existence of key 
        pEvaluateInfo : FBEvaluateInfo
        return : A valid key index in integer if key is present, otherwise -1 
        """
        pass

    def Segment_LocalPathEvaluate(self,pSegmentPercent,pEvaluateInfo):
        """
        Get the path's vector at a particular point within the curve, in local coordinates.

        pSegmentPercent : Double value (as time) at which the path vector would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def Segment_LocalPathEvaluateDerivative(self,pSegmentPercent,pEvaluateInfo):
        """
        Get the path's derivative at a particular point within the curve, in local coordinates.

        pSegmentPercent : Double value (as time) at which the path derivative would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def ShowCurveControls(self,pShow):
        """
        Enable or disable displaying Curve Controls for the 3D model path.

        pShow : <b>true</b> if curve controls are to be displayed <b>false</b> if not required 
        """
        pass

    def ShowCurvePoints(self,pShow):
        """
        Enable or disable displaying Curve Points for the 3D model path.

        pShow : <b>true</b> if curve points are to be displayed <b>false</b> if not required 
        """
        pass

    def Total_GlobalPathEvaluate(self,pTotalPercent,pEvaluateInfo):
        """
        Get the path's vector at a particular point within the curve, in global coordinates.

        pTotalPercent : Double value (as percentage) at which the path vector would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def Total_GlobalPathEvaluateDerivative(self,pTotalPercent,pEvaluateInfo):
        """
        Get the path's derivative at a particular point within the curve, in global coordinates.

        pTotalPercent : Double value (as percentage) at which the path derivative would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Derivative value at the required point in the path 
        """
        pass

    def Total_IsPathKey(self,pTotalPercent,pEvaluateInfo):
        """
        Query whether a percentage value has a key associated at that point in the path.

        pTotalPercent : Double value (as percentage) at which the path would be queried for existence of key 
        pEvaluateInfo : FBEvaluateInfo
        return : A valid key index in integer if key is present, otherwise -1 
        """
        pass

    def Total_LocalPathEvaluate(self,pTotalPercent,pEvaluateInfo):
        """
        Get the path's vector at a particular point within the curve, in local coordinates.

        pTotalPercent : Double value (as percentage) at which the path vector would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path 
        """
        pass

    def Total_LocalPathEvaluateDerivative(self,pTotalPercent,pEvaluateInfo):
        """
        Get the path's derivative at a particular point within the curve, in local coordinates.

        pTotalPercent : Double value (as percentage) at which the path derivative would be computed 
        pEvaluateInfo : FBEvaluateInfo
        return : Derivative value at the required point in the path 
        """
        pass

    def UpdateGeometry(self):
        """
        Update path geometry explicitly.

        """
        pass

    AutoControlNode=property(doc="<b>Read Write Property:</b> Automatically create key control nodes.          ")
    Color=property(doc="<b>Read Write Property:</b> Path display color in viewport.          ")
    KeyPropertyBehavior=property(doc="<b>Read Only Property:</b> Key property behavior.          ")
    PathEndCapScale=property(doc="<b>Read Write Property:</b> Path end cap display scale.          ")
    PathEndCapStyle=property(doc="<b>Read Write Property:</b> Path end cap display style.          ")
    PathLength=property(doc="<b>Read Only Property:</b> Path Length In Centimeter.          ")
    PathLengthInString=property(doc="<b>Read Only Property:</b> Path Length Display String According To The Current Unit.          ")
    PathLengthShow=property(doc="<b>Read Write Property:</b> Path length label display or not.          ")
    PathLengthUnit=property(doc="<b>Read Write Property:</b> Path Length Unit.          ")
    TextBackground=property(doc="<b>Read Write Property:</b> Path Length label display background color.          ")
    TextScale=property(doc="<b>Read Write Property:</b> Path Length label display scale.          ")
    pass

class FBModelPlaceHolder (FBBoxPlaceHolder):
    """
    Wrapper around a specific instance of a FBModel object.     
     This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying model. Instantiation of FBModelPlaceHolder should be left to the the system.      
    """
    def FBModelPlaceHolder(self):
        """
        Constructor.

        """
        pass

    Model=property(doc="<b>Read Only Property:</b> Underlying model object.          ")
    UseGlobalTransforms=property(doc="<b>Read Write Property:</b> Indicate if the translations are expressed in local or global mode.          ")
    pass

class FBModelPlane (FBModel):
    """
    Plane model class.     
         
    """
    def FBModelPlane(self,pName):
        """
        Constructor.

        pName : Name of Plane. 
        """
        pass

    pass

class FBModelRoot (FBModel):
    """
    Root object class.     
    See sample: SelectModelsWithNameContainingSubstring.py.     
    """
    def FBModelRoot(self,pName):
        """
        Constructor.

        pName : Name of root. 
        """
        pass

    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).          ")
    pass

class FBModelSkeleton (FBModel):
    """
    Root object class.     
         
    """
    def FBModelSkeleton(self,pName):
        """
        Constructor.

        pName : Name of skeleton. 
        """
        pass

    def GetSkinModelList(self,pSkinModelList):
        """
        Return the list of skin model associated with this Skeleton(Bone), which could be the deformable skins connected via cluster, or non deformable skins which are parented directly under this bone.

        pSkinModelList : List to be appended with skin models (with no duplicated items). 
        """
        pass

    Color=property(doc="<b>Read Write Property:</b> Color of skeleton node.          ")
    Length=property(doc="<b>Read Write Property:</b> Length of skeleton node. (Note: Only effective when the look is set to: Capsule)          ")
    LinkFollowGeometryOffset=property(doc="<b>Read Write Property:</b> Whether link to parent node must follow skeleton node or not, when skeleton node has a geometry offset.          ")
    Look=property(doc="<b>Read Write Property:</b> Look of skeleton node.          ")
    PreserveLinkEndPosition=property(doc="<b>Read Write Property:</b> Whether skeleton node must preserve its links' end position to children nodes, when skeleton node has a geometry offset. (Note: Only effective when the look is set to: Bone, Box or Stick)          ")
    Resolution=property(doc="<b>Read Write Property:</b> Resolution of skeleton node. (Note: Only effective when the look is set to: Sphere, Capsule or Stick)          ")
    Size=property(doc="<b>Read Write Property:</b> Size (not related to scaling).          ")
    pass

class FBNurbs (FBSurface):
    """
    Nurbs class.     
         
    """
    def FBNurbs(self,pName):
        """
        Constructor.

        pName : Name of Nurbs. 
        """
        pass

    def ControlPointsBegin(self):
        """
        Begin NURBS control points edition.

        """
        pass

    def ControlPointsEnd(self):
        """
        End NURBS control points edition.

        """
        pass

    def GetControlKnotValue(self,pUorV,pIndex):
        """
        Get knot vector value of control point.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        pIndex : Index of control point to set knot value for. 
        """
        pass

    def GetControlMultiplicity(self,pUorV,pIndex):
        """
        Get multiplicity (number of 'instances') of control point.

        pUorV : <b>1</b> if V multiplicity, <b>0</b> if U multlipicity. 
        pIndex : Index of control point to get multiplicity for. 
        """
        pass

    def GetControlWeight(self,pIndex):
        """
        Get weight of control point.

        pIndex : Index of control point to get weight from. 
        return : Weight of control point at index pIndex. 
        """
        pass

    def GetKnotCount(self,pUorV):
        """
        Number of knot vectors.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        return : Number of knot vectors on NURBS surface 
        """
        pass

    def SetControlKnotValue(self,pUorV,pIndex,pKnotValue):
        """
        Set knot vector value of control point.

        pUorV : <b>1</b> if V knot vector, <b>0</b> if U knot vector. 
        pIndex : Index of control point to set knot value for. 
        pKnotValue : Knot value for control point at pIndex. 
        """
        pass

    def SetControlMultiplicity(self,pUorV,pIndex,pMultiplicity):
        """
        Set multiplicity (number of 'instances') of control point.

        pUorV : <b>1</b> if V multiplicity, <b>0</b> if U multlipicity. 
        pIndex : Index of control point to set multiplicity for. 
        pMultiplicity : Multiplicity value for control point at pIndex. 
        """
        pass

    def SetControlWeight(self,pIndex,pWeight):
        """
        Set weight of control point.

        pIndex : Index of control point to set weight at. 
        pWeight : Weight of control point. 
        """
        pass

    def SurfaceBegin(self):
        """
        Begin NURBS definition.

        """
        pass

    def SurfaceEditBegin(self):
        """
        Begin NURBS surface edition.

        """
        pass

    def SurfaceEditEnd(self):
        """
        End NURBS surface edition.

        """
        pass

    def SurfaceEnd(self):
        """
        End NURBS definition.

        """
        pass

    UNurbType=property(doc="<b>Read Write Property:</b> Nurbs Type for U direction.          ")
    UOrder=property(doc="<b>Read Write Property:</b> Nurbs U order.          ")
    VNurbType=property(doc="<b>Read Write Property:</b> Nurbs Type for V direction.          ")
    VOrder=property(doc="<b>Read Write Property:</b> Nurbs V order.          ")
    pass

class FBPatch (FBSurface):
    """
    Patch class.     
         
    """
    def FBPatch(self,pName):
        """
        Constructor.

        pName : Name of Patch. 
        """
        pass

    def ControlPointsBegin(self):
        """
        Begin control points edition.

        """
        pass

    def ControlPointsEnd(self):
        """
        End control points edition.

        """
        pass

    def SurfaceBegin(self):
        """
        Begin Patch definition.

        """
        pass

    def SurfaceEditBegin(self):
        """
        Begin patch surface edit.

        """
        pass

    def SurfaceEditEnd(self):
        """
        End patch surface edit.

        """
        pass

    def SurfaceEnd(self):
        """
        End Patch definition.

        """
        pass

    USurfaceType=property(doc="<b>Read Write Property:</b> Patch mode for U direction.          ")
    VSurfaceType=property(doc="<b>Read Write Property:</b> Patch mode for V direction.          ")
    pass

class FBShaderLighted (FBShader):
    """
    Lighted shader class.     
     This type of shader is the default type used by the application. It allows users to control luminosity, contrast and specularity as well as how the transparency is computed, should it be used.There are two methods to create a FBShaderLighted object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code: 
@code
// Creation of a lighted shader, and setting it to use
// the constrast and specularity.
FBShaderLighted* lShader = new FBShaderLighted( 'New Shader' );

lShader->UseContrast  = true;
lShader->UseSpecular  = true;
lShader->Specular     = 35.0;
lShader->Transparency = kFBAlphaSourceTransluscentAlpha;

// Use the shader.
FBModel* lModel = FBFindModelByLabelName( 'Cube' );
if( lModel )
{
lShader->ReplaceAll( lModel );
}

// Do some more things...

// And then delete it when no longer necessary;
lShader->FBDelete();
@endcode

The following sample code does the same task, but in Python.Sample Python code: 
@code
from pyfbsdk import *

# Creating the shader.
lShader = FBShaderLighted( 'New Python Shader' )
lShader.UseContrast  = True
lShader.UseSpecular  = True
lShader.Specular     = 35.0
lShader.Transparency = FBAlphaSource.kFBAlphaSourceTransluscentAlpha

# User the shader
lModel = FBFindModelByLabelName( 'Cube' )
if lModel <> None:
    lModel.Show = True
    lShader.ReplaceAll( lModel )
@endcode

     
    """
    def FBShaderLighted(self,pName):
        """
        Constructor.

        pName : Name of shader. 
        """
        pass

    Alpha=property(doc="<b>Read Write Property:</b> Controls the actual effect of the shader on the object. At 0.0 it does nothing, and at 1.0 it fully affects the object.          ")
    Contrast=property(doc="<b>Read Write Property:</b> Changes the contrast of the object when it reflects light.          ")
    Luminosity=property(doc="<b>Read Write Property:</b> Changes the brightness of the object when reflecting light.          ")
    Specular=property(doc="<b>Read Write Property:</b> Changes an object's level of shininess when it reflects light by affecting the specular highlight.          ")
    Transparency=property(doc="<b>Read Write Property:</b> Indicates the computation method of the transparency.          ")
    UseContrast=property(doc="<b>Read Write Property:</b> Activate the Contrast option.          ")
    UseLuminosity=property(doc="<b>Read Write Property:</b> Activate the Luminosity option.          ")
    UseSpecular=property(doc="<b>Read Write Property:</b> Activate the Specularity option.          ")
    pass

class FBShaderShadowLive (FBShader):
    """
    Shader Shadow Live class.     
     Use the Live Shadow shader to apply real-time shadows to models. You can specify shadow intensity as well as the lights and objects that cast shadows in a scene.There are two methods to create a FBShaderShadowLive object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code: 
@code
// Create a shadow shader.
FBShaderShadowLive* lShader = new FBShaderShadowLive( 'New Shader' );

// Add a cube in its list of affected objects.
FBModel* lModel = FBFindModelByLabelName( 'Cube' )
if( lModel )
{
lShaderShadowLive.Add( lCube );
}
@endcode

Sample Python code: 
@code
from pyfbsdk import *

# Create shader.
lShader = FBShaderShadowLive( 'New Python Shader' )

# Find a cube to put in our list of affected objects.
lModel = FBFindModelByLabelName( 'Cube' )
if lModel:
lShader.ShadowCasterProperty.append( lModel )
@endcode

     
    """
    def FBShaderShadowLive(self,pName):
        """
        Constructor.

        pName : Name of shader. 
        """
        pass

    Lights=property(doc="<b>List:</b> List of light object which will produce shadows.          ")
    LocalShadow=property(doc="<b>Read Write Property:</b> Creates an accurate projection of a shadow for each object.          ")
    Models=property(doc="<b>List:</b> List of object which when lighted will cast a shadow.          ")
    ShadowFrameType=property(doc="<b>Read Write Property:</b> Used to select the shadow calculation method.          ")
    ShadowIntensity=property(doc="<b>Read Write Property:</b> Controls the darkness of shadows cast by a selected object.          ")
    ShadowType=property(doc="<b>Read Write Property:</b> Indicate which shadow type is desired.          ")
    ShadowZOffset=property(doc="<b>Read Write Property:</b> Specifies the offset of the Live Shadow shader's plane from the original selected plane.          ")
    UseGobo=property(doc="<b>Read Write Property:</b> Includes the gobo in the shadow map calculation.          ")
    pass

class FBStoryTrack (FBConstraint):
    """
    Story Track class.     
     Tracks are containers for clips (medias), have a specific type which offer different functions. Note: To change the travelling node of a track, search for the 'TravellingNode' property on the track and then connect/disconnect the appropriate object. Python example: lPropTravellingNode = lAnimTrack.PropertyList.Find('TravellingNode') lCube.ConnectDst(lPropTravellingNode) See samples: CreateShotClip.py, AudioTrackSetupTool.py, BloopSlate.py, RecordLight.py, FBStoryFolder.py, VideoClip.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py, PrintClipNamesAndStartStopFrames.py.     
    """
    def FBStoryTrack(self,pTrackType,pFolder):
        """
        Constructor.

        pTrackType : Type of the track to be created. 
        pFolder : If NULL, parent will be the global root folder. 
        """
        pass

    def FBStoryTrack(self,pSource,pFolder):
        """
        Constructor.

        pSource : Source of the track to be created based on media component type. 
        pFolder : If NULL, parent will be the global root folder. 
        """
        pass

    def AddClip(self,pClip,pTime):
        """
        AddClip Add the clip to the track.

        pClip : FBComponent
        pTime : FBTime
        """
        pass

    def ChangeDetailsBegin(self):
        """
        ChangeDetailsBegin.
        You must call this function before adding/removing any object to the Details list or it won't work.

        """
        pass

    def ChangeDetailsEnd(self):
        """
        ChangeDetailsEnd.
        You must call this function after adding/removing any object to the Details list or it won't work.

        """
        pass

    def CopyTakeIntoTrack(self,pTimeSpan,pTake,pOutputOffset,pMakeUndoable):
        """
        CopyTakeIntoTrack Copy animation from the specified take for affected objects of the track.

        pTimeSpan : Time span for the clip to create. 
        pTake : Take to get the animation from. 
        pOutputOffset : Time offset for the clip if necessary. 
        pMakeUndoable : If the operation should be undoable. 
        return : Created story clip if the operation succeeded otherwize NULL. 
        """
        pass

    def CreateSubTrack(self,pTrackType,pRefMode):
        """
        Create a sub track, Only Character and Animation tracks can have sub-tracks.

        pTrackType : Type of the sub track to be created. 
        pRefMode : Composition mode of the sub track, kFBStoryTrackOverride or kFBStoryTrackAdditive. 
        return : Created sub story track if the operation succeeded otherwise NULL. 
        """
        pass

    def EnableBodyPart(self,pPart,pEnable):
        """
        EnableBodyPart.

        pPart : Which part to enable/disable. 
        pEnable : If True, this will enable the body part solving while false will disable it. Enable a specific body part for character solving. 
        """
        pass

    def FBDelete(self):
        """
        Virtual FBDelete function.

        """
        pass

    def IsBodyPartEnabled(self,pPart):
        """
        IsBodyPartEnabled.
        Is a specific body part is enabled.

        pPart : FBStoryTrackBodyPart
        """
        pass

    def Load(self,pLoad):
        """
        Allow to load/unload all story clips under this track.

        pLoad : bool
        """
        pass

    AcceptKey=property(doc="<b>Read Write Property:</b> Allow track to accept keys          ")
    AudioOutIndex=property(doc="<b>Read Write Property:</b> Audio Output's index to use.          ")
    Character=property(doc="<b>Read Write Property:</b> Character to use.          ")
    CharacterIndex=property(doc="<b>Read Write Property:</b> Character's index to use.          ")
    ClipNameConvention=property(doc="<b>Read Write Property:</b> Naming convention for each new recording clip that is created. Can use special tags: <Name> <StartTCValue> <StartFrameValue> <StartDate> <StartTime> <TakeName>          ")
    Clips=property(doc="<b>List:</b> Clips contained in this track.          ")
    Details=property(doc="<b>List:</b> All objects associated to this track for processing.          ")
    Ghost=property(doc="<b>Read Write Property:</b> Show ghosts          ")
    GhostModel=property(doc="<b>Read Write Property:</b> Show ghost of models          ")
    GhostPivot=property(doc="<b>Read Write Property:</b> Show ghost of match object          ")
    GhostShowTrackMode=property(doc="<b>Read Write Property:</b> Show the ghosts for all the clips or only the adjacent clips. See FBStoryTrackGhostShowMode          ")
    GhostTravelling=property(doc="<b>Read Write Property:</b> Show ghost of clip vector or traveling node          ")
    Label=property(doc="<b>Read Write Property:</b> Label to display for this story track.          ")
    Mute=property(doc="<b>Read Write Property:</b> If true, this track wont' play.          ")
    OffsetEnable=property(doc="<b>Read Write Property:</b> When enabled, allow clip to be offset          ")
    ParentFolder=property(doc="<b>Read Only Property:</b> Parent folder.          ")
    ParentTrack=property(doc="<b>Read Only Property:</b> Parent track, if the track is of Character or Animation type.          ")
    PassThrough=property(doc="<b>Read Write Property:</b> Enable passthrough of animation if there is no clip on track animation is taken from other tracks of take          ")
    RecordClipPath=property(doc="<b>Read Write Property:</b> Path for story recording. Can be relative or full path.          ")
    RecordTrack=property(doc="<b>Read Write Property:</b> Path for story recording. Can be relative or full path.          ")
    ReferenceMode=property(doc="<b>Read Write Property:</b> Track composition mode, kFBStoryTrackOverride or kFBStoryTrackAdditive          ")
    ShowBackplate=property(doc="<b>Read Write Property:</b> If true, the backplate will be shown.          ")
    ShowFrontplate=property(doc="<b>Read Write Property:</b> If true, the frontplate will be shown.          ")
    Solo=property(doc="<b>Read Write Property:</b> If true, this track will be the only one to play.          ")
    SubTracks=property(doc="<b>List:</b> Only Character and Animation tracks can have sub-tracks.          ")
    TrackVideo=property(doc="<b>Read Only Property:</b> This FBVideo can be used as a texture.          ")
    Type=property(doc="<b>Read Only Property:</b> Type of the track          ")
    Weight=property(doc="<b>Read Write Property:</b> Control the blend amount.          ")
    pass

class FBVideoClip (FBVideo):
    """
    See sample: VideoClip.py.     
        
    """
    def FBVideoClip(self,pName):
        """
        Constructor.

        pName : Name of video media. 
        """
        pass

    def DrawImage(self,pX,pY,pW,pH,pFrame):
        """
        Draw a frame of the image to the current view.

        pX : X position of image (default=0). 
        pY : Y position of image (default=0). 
        pW : Width of image (default=-1). 
        pH : Height of image (default=-1). 
        pFrame : Frame to draw (default=-1). 
        """
        pass

    def FBDelete(self):
        """
        """
        pass

    def GetEmbeddedTimecode(self,pFrame,pTimeCode):
        """
        Get the embedded timecode associated to a video clip frame.

        pFrame : Video clip frame to get timecode for. 
        pTimeCode : The timecode object being filled by this method. 
        return : True if an embedded timecode is retrieved from the video clip, false otherwise. (Python: If no embedded timecode is retrieved, returns an FBTimeCode object with its time set to FBTime::Infinity). 
        """
        pass

    def GetTextureID(self):
        """
        Get the texture ID.

        return : ID of the texture 
        """
        pass

    def IsValid(self):
        """
        Verifies the validity of the FBVideo object.

        return : <b>true</b> if data is valid. 
        """
        pass

    CurrentFrame=property(doc="<b>Read Write Property:</b> Current frame.          ")
    CurrentFrameTime=property(doc="<b>Read Write Property:</b> Current time in clip.          ")
    CurrentFrameTimeCode=property(doc="<b>Read Only Property:</b> Embedded timecode from current frame in clip. Use the method GetEmbeddedTimecode to get the timecode of a different frame than the current frame.          ")
    Filename=property(doc="<b>Read Write Property:</b> Filename of media.          ")
    Format=property(doc="<b>Read Only Property:</b> Video format.          ")
    FrameRate=property(doc="<b>Read Write Property:</b> Frame rate.          ")
    FrameTime=property(doc="<b>Read Only Property:</b> Inverse of FPS, time per frame          ")
    FreeRunning=property(doc="<b>Read Write Property:</b> Is free Running on?          ")
    Height=property(doc="<b>Read Only Property:</b> Height of image.          ")
    InterlaceMode=property(doc="<b>Read Write Property:</b> Interlace mode.          ")
    LastFrame=property(doc="<b>Read Only Property:</b> Last frame in clip.          ")
    LastFrameTime=property(doc="<b>Read Only Property:</b> Time of last frame          ")
    Loop=property(doc="<b>Read Write Property:</b> Loop video clip?          ")
    PlaySpeed=property(doc="<b>Read Write Property:</b> Playback speed.          ")
    PowerOfTwoHeight=property(doc="<b>Read Only Property:</b> Closest power of two value superior to height of image.          ")
    PowerOfTwoWidth=property(doc="<b>Read Only Property:</b> Closest power of two value superior to width of image.          ")
    ProxyMode=property(doc="<b>Read Write Property:</b> Proxy mode.          ")
    RelativePath=property(doc="<b>Read Only Property:</b> Relative path of media.          ")
    StartFrame=property(doc="<b>Read Write Property:</b> Frame to begin video playback from.          ")
    StopFrame=property(doc="<b>Read Write Property:</b> Frame to end video playback at.          ")
    StorageMode=property(doc="<b>Read Write Property:</b> Storage mode.          ")
    TimeOffset=property(doc="<b>Read Write Property:</b> Temporal offset for beginning of video.          ")
    Width=property(doc="<b>Read Only Property:</b> Width of image.          ")
    pass

class FBVideoIn (FBVideo):
    """
    Basic video input class, supporting webcam and DV device.     
    See sample: VideoInput.py.     
    """
    def FBVideoIn(self):
        """
        Constructor.

        """
        pass

    def LiveGetCompressor(self):
        """
        Get the current compressor index.

        return : Index of the current compressor. 
        """
        pass

    def LiveGetCompressorCount(self):
        """
        Get the compressor count.

        return : Number of available compressor. 
        """
        pass

    def LiveGetCompressorName(self,pCompressorIndex):
        """
        Get the compressor name at a particular index.

        pCompressorIndex : int
        return : Name of the compressor. If the pCompressorIndex is higher than the number of compressor, the function will return NULL. 
        """
        pass

    def LiveGetResolutionFR(self):
        """
        Get the current resolution and frame rate index.

        return : Index of the current resolution and frame rate. 
        """
        pass

    def LiveGetResolutionFRCount(self):
        """
        Get the number of resolution and frame rate available for the device.

        return : Number of available resolution and frame rate. 
        """
        pass

    def LiveGetResolutionFRName(self,pIndex):
        """
        Get the resolution and frame rate string description at the specified index.

        pIndex : Index of the resolution and frame rate. 
        return : Name of the resolution and frame rate. 
        """
        pass

    def LiveGetType(self):
        """
        Get the type of the video input device.

        return : Type of the video input device. 
        """
        pass

    def LiveSetCompressor(self,pCompressorIndex):
        """
        Set the current compressor to be used when recording.

        pCompressorIndex : Index of the compressor. 
        return : True if successful. 
        """
        pass

    def LiveSetResolutionFR(self,pIndex):
        """
        Set the current resolution and frame rate for the device.

        pIndex : Index of the resolution and frame rate. 
        """
        pass

    FilePath=property(doc="<b>Read Write Property:</b> Location of the generated movie file after a recording session.          ")
    Online=property(doc="<b>Read Write Property:</b> If true, the device is online and will display the current video feed.          ")
    RecordAudio=property(doc="<b>Read Write Property:</b> If true, the device will also record audio during a recording session.          ")
    Recording=property(doc="<b>Read Write Property:</b> If true, the device will record during a recording session.          ")
    pass

class FBVideoMemory (FBVideo):
    """
    FBVideoMemory allow external media source (which can't be supported by MoBu natively)  User could create / update OGL texture (GL_TEXTURE_2D type) externally, and pass in GL texture object id to TextureOGLId property.See 'Scripts/Samples/Video/VideoMemory.py' for usage example.     
    See sample: VideoMemory.py.     
    """
    def FBVideoMemory(self,pName):
        """
        Constructor.

        pName : Name of video media. 
        """
        pass

    def SetObjectImageSize(self,pW,pH):
        """
        Set image size to allow MoBu preview texture with proper dimension / aspect.

        pW : Width of image. 
        pH : Height of image. 
        """
        pass

    TextureOGLId=property(doc="<b>Read Write Property:</b> OpenGL texture buffer object id (GL_TEXTURE_2D type).          ")
    pass

class FBVideoOut (FBVideo):
    """
    Video media class.     
    See sample: VideoOutput.py.     
    """
    def FBVideoOut(self):
        """
        Constructor.

        """
        pass

    Online=property(doc="<b>Read Write Property:</b> If true, the device is online and will output display.          ")
    pass

class FBCameraStereo (FBCamera):
    """
        
        
    """
    def FBCameraStereo(self,pName):
        """
        Constructor.

        pName : Name of stereo camera. 
        """
        pass

    CenterCamera=property(doc="<b>Read Write Property: </b> This property hold the center camera connected to it. Must be either the master, left or right camera.          ")
    DisplayZeroParallaxPlane=property(doc="<b>Read Write Property: </b> Display the zero parallax plane.          ")
    FilmOffsetLeftCam=property(doc="<b>Read Write Property: </b> This property handles the film offset for the left camera. (inch)          ")
    FilmOffsetRightCam=property(doc="<b>Read Write Property: </b> This property handles the film offset for the right camera. (inch)          ")
    InteraxialSeparation=property(doc="<b>Read Write Property: </b> This property handles the distance between left and right cameras.          ")
    LeftCamera=property(doc="<b>Read Write Property: </b> This property hold the left camera connected to it.          ")
    PrecompFileName=property(doc="<b>Read Write Property: </b> This property handles the precomp file name.          ")
    RelativePrecompFileName=property(doc="<b>Read Write Property: </b> This property handles the relative precomp file name.          ")
    RightCamera=property(doc="<b>Read Write Property: </b> This property hold the right camera connected to it.          ")
    Stereo=property(doc="<b>Read Write Property: </b> //!< This property handles the types of Stereo camera.          ")
    ToeInAdjust=property(doc="<b>Read Write Property: </b> This property is to offset the computed toe-in effect when it's in Converged mode.          ")
    ZeroParallax=property(doc="<b>Read Write Property: </b> This property handles the distance on the camera view axis where the zero parallax plane occurs.          ")
    ZeroParallaxPlaneColor=property(doc="<b>Read Write Property: </b> Zero parallax plane color.          ")
    ZeroParallaxPlaneTransparency=property(doc="<b>Read Write Property: </b> Zero parallax plane transparency.          ")
    pass

class FBHUDBloopSlateElement (FBHUDFlashElement):
    """
    Heads Up display.     
     Bloop Slate HUD element. Display a bloop slate (swf) file rendered on the HUD.      
    """
    def FBHUDBloopSlateElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD flash element. 
        """
        pass

    BackgroundColor=property(doc="<b>Read Write Property:</b> Bloop slate background color, by default it is 100% transparent.          ")
    Enable=property(doc="<b>Read Write Property:</b> Bloop slate will appear if set to true.          ")
    ForegroundColor=property(doc="<b>Read Write Property:</b> Bloop slate foreground color.          ")
    ShowAfterDelayOnRecordPlay=property(doc="<b>Read Write Property:</b> Delay before the bloop slate is displayed after recording has started.          ")
    ShowDuration=property(doc="<b>Read Write Property:</b> Time that the bloop slate will be displayed.          ")
    pass

class FBHUDTimelineElement (FBHUDFlashElement):
    """
    Heads Up display.     
     HUD Timeline element. Displays a timeline that shows Head, Cut, Tail regions, and current time cursor. The drawing is defined in the flash file(timeline.swf). See sample: Timeline.py.     
    """
    def FBHUDTimelineElement(self,pName):
        """
        Constructor.

        pName : Name of new HUD flash element. 
        """
        pass

    CutActiveColor=property(doc="<b>Read Write Property:</b> Specifies color of the Cut region when it is active.          ")
    CutIdleColor=property(doc="<b>Read Write Property:</b> Specifies color of the Cut region when it is idle.          ")
    HeadActiveColor=property(doc="<b>Read Write Property:</b> Specifies color of the Head region when it is active.          ")
    HeadDuration=property(doc="<b>Read Write Property:</b> Specifies duration of the Head region.          ")
    HeadIdleColor=property(doc="<b>Read Write Property:</b> Specifies color of the Head region when it is idle.          ")
    TailActiveColor=property(doc="<b>Read Write Property:</b> Specifies color of the Tail region when it is active.          ")
    TailDuration=property(doc="<b>Read Write Property:</b> Specifies duration of the Tail region.          ")
    TailIdleColor=property(doc="<b>Read Write Property:</b> Specifies color of the Tail region when it is idle.          ")
    pass

class FBModelMarkerOptical (FBModelMarker):
    """
    Optical model marker class.     
         
    """
    def FBModelMarkerOptical(self,pName,pOptical):
        """
        Constructor.
        If no optical model is given, be sure to add one before accessing the Segments and Gaps properties.

        pName : Name of optical marker(default=NULL). 
        pOptical : Optical model(default=NULL). 
        """
        pass

    def ExportBegin(self):
        """
        Begin export of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.

        return : Number of frames to export. 
        """
        pass

    def ExportEnd(self):
        """
        End exportation from optical model.

        return : <b>true</b> if successful. 
        """
        pass

    def ExportKey(self,pX,pY,pZ,pOcclusion):
        """
        Export a key of optical data.

        pX : X position. 
        pY : Y position. 
        pZ : Z position(default=NULL). 
        pOcclusion : Occlusion value(default=NULL). 
        return : <b>true</b> if successful. 
        """
        pass

    def GetRigidBody(self):
        """
        Get the rigid body for the marker.

        return : Rigid body for marker (check IsValid()) 
        """
        pass

    def ImportBegin(self):
        """
        Begin import of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.

        return : The number of samples taken. 
        """
        pass

    def ImportEnd(self):
        """
        End importation and clean up data.
        Interpolates optical data to create a curve from the input key frams.

        return : <b>true</b> if successful. 
        """
        pass

    def ImportKey(self,pX,pY,pZ,pOcclusion):
        """
        Import a key of optical data.

        pX : X position. 
        pY : Y position. 
        pZ : Z position(default=0.0). 
        pOcclusion : Occlusion value(default=0.0). 
        return : <b>true</b> if successful. 
        """
        pass

    def InsertSegmentedData(self,pTData,pOData):
        """
        Insert segmented data.

        pTData : Translation data. 
        pOData : Occlusion data. 
        """
        pass

    def SetModelOptical(self,pOptical):
        """
        Set the current optical model.

        pOptical : New optical model. 
        """
        pass

    Color=property(doc="<b>Property:</b> Marker color.          ")
    Data=property(doc="<b>Property:</b> Data.          ")
    Done=property(doc="<b>Property:</b> Done?          ")
    Gaps=property(doc="<b>Property:</b> Gaps.          ")
    Optical=property(doc="<b>Property:</b> Optical model.          ")
    Segments=property(doc="<b>Property:</b> Marker segments.          ")
    pass

class FBVideoClipImage (FBVideoClip):
    """
        
        
    """
    def FBVideoClipImage(self,pName):
        """
        Constructor.

        pName : Name of image file. 
        """
        pass

    ImageSequence=property(doc="<b>Read Write Property:</b> Clip is an image sequence?          ")
    MaxMipMapResolution=property(doc="<b>Read Write Property:</b> Maximum MipMap resolution will be loaded into GPU.          ")
    UseSystemFrameRate=property(doc="<b>Read Write Property:</b> Clip is using system frame rate?          ")
    pass

