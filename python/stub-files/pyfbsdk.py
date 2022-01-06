from __future__ import annotations
from typing import List
class _Enum:
    __slots__:tuple
    names:dict
    values:dict
class ETimeFormats:...
class FBAccessMode(_Enum):
    """pyfbsdk
    Data access modes."""
    kFBAccessModeDisk:FBAccessMode
    """Access data directly to disk using a cache system."""
    kFBAccessModeMemory:FBAccessMode
    """Access data from memory, which means that it will copyed entirely into it."""
class FBAlphaSource(_Enum):
    """Shader transparency computation.
    There are different way to compute transparency, and this lists the supported options."""
    kFBAlphaSource2DTransparency:FBAlphaSource
    """2D Transparency."""
    kFBAlphaSourceAccurateAlpha:FBAlphaSource
    """Accurate Transparency."""
    kFBAlphaSourceAdditiveAlpha:FBAlphaSource
    """Additive Transparency."""
    kFBAlphaSourceMatteAlpha:FBAlphaSource
    """Matte."""
    kFBAlphaSourceNoAlpha:FBAlphaSource
    """No transparency."""
    kFBAlphaSourceTransluscentAlpha:FBAlphaSource
    """Translucent."""
    kFBAlphaSourceTransluscentZSortAlpha:FBAlphaSource
    """Translucent(Models Z Sort)."""
class FBAnimationLayerMergeOptions(_Enum):
    """Merge option for animation layers."""
    kFBAnimLayerMerge_AllLayers_AllProperties:FBAnimationLayerMergeOptions
    """Merge the animation of all properties of the selected models from all the layers to the BaseAnimation layer."""
    kFBAnimLayerMerge_AllLayers_CompleteScene:FBAnimationLayerMergeOptions
    """Merge the animation of all properties from all the layers to the BaseAnimation layer."""
    kFBAnimLayerMerge_AllLayers_SelectedProperties:FBAnimationLayerMergeOptions
    """Merge the animation of the selected properties of the selected models from all the layers to the BaseAnimation layer."""
    kFBAnimLayerMerge_SelectedLayers_AllProperties:FBAnimationLayerMergeOptions
    """Merge the animation of all properties of the selected models from the selected layers to the selected layer with the lowest index."""
    kFBAnimLayerMerge_SelectedLayers_CompleteScene:FBAnimationLayerMergeOptions
    """Merge the animation of all properties from the selected layers to the selected layer with the lowest index."""
    kFBAnimLayerMerge_SelectedLayers_SelectedProperties:FBAnimationLayerMergeOptions
    """Merge the animation of the selected properties of the selected models from the selected layers to the selected layer with the lowest index."""
class FBAnimationNodeConnectorType(_Enum):
    """Different types for the animation node connectors."""
    kFBAnimationNodeConnectorTypeConnectedIn:FBAnimationNodeConnectorType
    """The animation node input connector is connected to an animation node output connector (valid for input connector only)."""
    kFBAnimationNodeConnectorTypeConnectedOut:FBAnimationNodeConnectorType
    """The animation node output connector is connected to at least one animation node input connector (valid for output connector only)."""
    kFBAnimationNodeConnectorTypeConstantIn:FBAnimationNodeConnectorType
    """The animation node input connector has a constant value set to it (valid for input connector only)."""
    kFBAnimationNodeConnectorTypeNone:FBAnimationNodeConnectorType
    """The animation node connector is not connected and doesn't have a constant value set to it."""
class FBArrangeMode(_Enum):
    """Modes for arranging objects in schematic view."""
    kHorizontalMode:FBArrangeMode
    """Arrange all objects horizontally."""
    kVerticalMode:FBArrangeMode
    """Arrange all objects vertically."""
class FBAssetMngFileOptions(_Enum):
    """Behavior of the application when working with managed files."""
    kFileAddOnNewSave:FBAssetMngFileOptions
    """Add new file automatically on save."""
    kFileAddOnNewSave_Ask:FBAssetMngFileOptions
    """Ask for adding new file on save."""
    kFileCheckInOnClose:FBAssetMngFileOptions
    """Check in file automatically when closing it."""
    kFileCheckInOnClose_Ask:FBAssetMngFileOptions
    """Ask for check in file when closing it."""
    kFileCheckOutOnLoad:FBAssetMngFileOptions
    """Check out file automatically on load."""
    kFileCheckOutOnLoad_Ask:FBAssetMngFileOptions
    """Ask for checkout on load."""
    kFileOptionsAll:FBAssetMngFileOptions
    kFileUploadOnSave:FBAssetMngFileOptions
    """Upload file automatically on save."""
    kFileUploadOnSave_Ask:FBAssetMngFileOptions
    """Ask for upload on save."""
class FBAssetMngMenuOptions(_Enum):
    """Show or hide version control menu items.
    Let you specify which functionalities will be available from the menus."""
    kMenuAddToDatabase:FBAssetMngMenuOptions
    """File -> Add to database."""
    kMenuAll:FBAssetMngMenuOptions
    """Support everything."""
    kMenuCheckIn:FBAssetMngMenuOptions
    """Version Control -> Check In."""
    kMenuCheckOut:FBAssetMngMenuOptions
    """Version Control -> Check Out."""
    kMenuEnable:FBAssetMngMenuOptions
    """Version Control -> Disable Version Control Integration."""
    kMenuFileAll:FBAssetMngMenuOptions
    """Support all elements from the File menu."""
    kMenuGetLatest:FBAssetMngMenuOptions
    """Version Control -> Get Latest."""
    kMenuOpenFromDatabase:FBAssetMngMenuOptions
    """File -> Open from database."""
    kMenuShowExplorer:FBAssetMngMenuOptions
    """Version Control -> Show Explorer."""
    kMenuShowHistory:FBAssetMngMenuOptions
    """Version Control -> Show History."""
    kMenuShowProperties:FBAssetMngMenuOptions
    """Version Control -> Show Properties."""
    kMenuShowReferenceMng:FBAssetMngMenuOptions
    """Version Control -> Show Reference Manager."""
    kMenuShowSettings:FBAssetMngMenuOptions
    """Version Control -> Show Settings."""
    kMenuSourceControlAll:FBAssetMngMenuOptions
    """Support all elements from the Version Control menu."""
    kMenuSourceControlMin:FBAssetMngMenuOptions
    """Support only the basics functionalities."""
    kMenuUndoCheckOut:FBAssetMngMenuOptions
    """Version Control -> Undo Check Out."""
    kMenuUploadToDatabase:FBAssetMngMenuOptions
    """File -> Upload to database."""
class FBAttachType(_Enum):
    """Types of attachments between UI regions.
    See samples: Attach.py, BoxLayout.py, RadioButton.py."""
    kFBAttachBottom:FBAttachType
    """Attach to bottom [max(y1,y2)]"""
    kFBAttachCenter:FBAttachType
    """Attach to center [center(x1,y1,x2,y2)]"""
    kFBAttachHeight:FBAttachType
    """Attach to height [abs(y2-y1)]"""
    kFBAttachLeft:FBAttachType
    """Attach to left [min(x1,x2)]"""
    kFBAttachNone:FBAttachType
    """No attachment."""
    kFBAttachRight:FBAttachType
    """Attach to right [max(x1,x2)]"""
    kFBAttachTop:FBAttachType
    """Attach to top [min(y1,y2)]"""
    kFBAttachWidth:FBAttachType
    """Attach to width [abs(x2-x1)]"""
class FBAttenuationType(_Enum):
    """Light attenuation types."""
    kFBAttenuationCubic:FBAttenuationType
    """Cubic attenuation."""
    kFBAttenuationLinear:FBAttenuationType
    """Linear attenuation."""
    kFBAttenuationNone:FBAttenuationType
    """No attenuation."""
    kFBAttenuationQuadratic:FBAttenuationType
    """Quadratic attenuation."""
class FBAudioBitDepthMode(_Enum):
    """Enum FBAudioBitDepthMode."""
    kFBAudioBitDepthMode_16:FBAudioBitDepthMode
    """16 bits, Wave file render support."""
    kFBAudioBitDepthMode_24:FBAudioBitDepthMode
    """24 bits, Wave file render support."""
    kFBAudioBitDepthMode_8:FBAudioBitDepthMode
    """8 bits, Wave file render support."""
    kFBAudioBitDepthMode_FP:FBAudioBitDepthMode
    """FP type audio, Wave file render not support."""
class FBAudioChannelMode(_Enum):
    """Enum FBAudioChannelMode."""
    kFBAudioChannelModeMono:FBAudioChannelMode
    """1 channel, Wave file render support."""
    kFBAudioChannelModeStereo:FBAudioChannelMode
    """2 channels, Wave file render support."""
    kFBAudioChannelMode_4:FBAudioChannelMode
    """4 channels, Wave file render not support."""
    kFBAudioChannelMode_8:FBAudioChannelMode
    """8 channels, Wave file render not support."""
class FBAudioOutputLocation(_Enum):
    """Type of locations where the audio is rendered when rendering a scene using a video format."""
    FBAudioOutputLocationCount:FBAudioOutputLocation
    """Count."""
    FBAudioOutputLocationEmbedded:FBAudioOutputLocation
    """The audio is embedded within the video output file."""
    FBAudioOutputLocationEmbeddedAndStandalone:FBAudioOutputLocation
    """The audio is embedded within the video output file and is also rendered in a standalone output file."""
    FBAudioOutputLocationStandalone:FBAudioOutputLocation
    """The audio is rendered in a standalone output file."""
class FBAudioRateMode(_Enum):
    """Enum FBAudioRateMode."""
    kFBAudioRateMode_100000:FBAudioRateMode
    """100000 hz, Wave file render not support."""
    kFBAudioRateMode_12000:FBAudioRateMode
    """12000 hz, Wave file render support."""
    kFBAudioRateMode_12500:FBAudioRateMode
    """12500 hz, Wave file render not support."""
    kFBAudioRateMode_16000:FBAudioRateMode
    """16000 hz, Wave file render support."""
    kFBAudioRateMode_22050:FBAudioRateMode
    """22050 hz, Wave file render support."""
    kFBAudioRateMode_24000:FBAudioRateMode
    """24000 hz, Wave file render support."""
    kFBAudioRateMode_25000:FBAudioRateMode
    """25000 hz, Wave file render not support."""
    kFBAudioRateMode_32000:FBAudioRateMode
    """32000 hz, Wave file render support."""
    kFBAudioRateMode_44100:FBAudioRateMode
    """44100 hz, Wave file render support."""
    kFBAudioRateMode_48000:FBAudioRateMode
    """48000 hz, Wave file render support."""
    kFBAudioRateMode_50000:FBAudioRateMode
    """50000 hz, Wave file render not support."""
    kFBAudioRateMode_64000:FBAudioRateMode
    """64000 hz, Wave file render support."""
    kFBAudioRateMode_8000:FBAudioRateMode
    """8000 hz, Wave file render support."""
    kFBAudioRateMode_88200:FBAudioRateMode
    """88200 hz, Wave file render support."""
    kFBAudioRateMode_96000:FBAudioRateMode
    """96000 hz, Wave file render support."""
    kFBRAudioateMode_11025:FBAudioRateMode
    """11025 hz, Wave file render support."""
class FBBatchFileFormat(_Enum):
    """Different file formats for the batch."""
    kFBBatchFileFormatAMC:FBBatchFileFormat
    """File format for Acclaim AMC."""
    kFBBatchFileFormatBVH:FBBatchFileFormat
    """File format for Biovision BVH."""
    kFBBatchFileFormatC3D:FBBatchFileFormat
    """File format for Vicon C3D."""
    kFBBatchFileFormatFBX:FBBatchFileFormat
    """File format for FBX (animation only)."""
    kFBBatchFileFormatHTR:FBBatchFileFormat
    """File format for Motion Analysis HTR."""
    kFBBatchFileFormatTRC:FBBatchFileFormat
    """File format for Motion Analysis TRC."""
class FBBatchOnContainsBatchTakes(_Enum):
    """Different actions to perform when a scene already contains batch takes while in a batch process."""
    kFBBatchOnContainsBatchTakesSaveAllTakes:FBBatchOnContainsBatchTakes
    """Save all the takes."""
    kFBBatchOnContainsBatchTakesSaveBatchTakesOnly:FBBatchOnContainsBatchTakes
    """Save only the batch takes."""
class FBBatchOnTakeExist(_Enum):
    """Different actions to perform when a take already exist while in a batch process."""
    kFBBatchOnTakeExistOverwrite:FBBatchOnTakeExist
    """Overwrite the take."""
    kFBBatchOnTakeExistSkip:FBBatchOnTakeExist
    """Skip the take."""
class FBBatchProcessType(_Enum):
    """Different process type for the batch."""
    kFBBatchProcessTypeConvert:FBBatchProcessType
    """Does the load and save."""
    kFBBatchProcessTypeLoad:FBBatchProcessType
    """Load the files and plot the character with every take."""
    kFBBatchProcessTypeSave:FBBatchProcessType
    """Save the takes in different files."""
class FBBatchStatus(_Enum):
    """Different return values of the Batch process."""
    kFBBatchStatusActorInputMarkersetHasNoReferenceModel:FBBatchStatus
    kFBBatchStatusActorInputMarkersetNotCorrectlyAssociated:FBBatchStatus
    kFBBatchStatusActorInputMarkersetNotSpecified:FBBatchStatus
    kFBBatchStatusAsfSkeletonFileNotSpecified:FBBatchStatus
    kFBBatchStatusCantOpenAsfSkeletonFile:FBBatchStatus
    kFBBatchStatusCharacterHasNoReference:FBBatchStatus
    kFBBatchStatusCharacterNotCharacterized:FBBatchStatus
    kFBBatchStatusCharacterNotSpecified:FBBatchStatus
    kFBBatchStatusError:FBBatchStatus
    kFBBatchStatusInputActorNotSpecified:FBBatchStatus
    kFBBatchStatusInputCharacterHasNoReference:FBBatchStatus
    kFBBatchStatusInputCharacterNotCharacterized:FBBatchStatus
    kFBBatchStatusInputDirectoryNotValid:FBBatchStatus
    kFBBatchStatusOutputDirectoryNotValid:FBBatchStatus
    kFBBatchStatusSuccess:FBBatchStatus
class FBBodyNodeId(_Enum):
    """All body nodes.
    See sample: ExportAnimationLibrary.py."""
    kFBChestNodeId:FBBodyNodeId
    """Spine 1."""
    kFBHeadNodeId:FBBodyNodeId
    """Required."""
    kFBHipsNodeId:FBBodyNodeId
    """Required."""
    kFBHipsTranslationNodeId:FBBodyNodeId
    kFBInvalidNodeId:FBBodyNodeId
    kFBLastNodeId:FBBodyNodeId
    kFBLastNodeId_Old:FBBodyNodeId
    kFBLeftAnkleNodeId:FBBodyNodeId
    """Required."""
    kFBLeftCollarNodeId:FBBodyNodeId
    kFBLeftElbowNodeId:FBBodyNodeId
    """Required."""
    kFBLeftElbowRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftElbowRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftElbowRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftElbowRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftElbowRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftElbowRollNodeId:FBBodyNodeId
    kFBLeftExtraFingerANodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFingerBNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFingerCNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFingerDNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFingerInNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFootFingerANodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFootFingerBNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFootFingerCNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFootFingerDNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftExtraFootFingerInNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBLeftFootIndexANodeId:FBBodyNodeId
    kFBLeftFootIndexBNodeId:FBBodyNodeId
    kFBLeftFootIndexCNodeId:FBBodyNodeId
    kFBLeftFootIndexDNodeId:FBBodyNodeId
    kFBLeftFootIndexInNodeId:FBBodyNodeId
    kFBLeftFootMiddleANodeId:FBBodyNodeId
    kFBLeftFootMiddleBNodeId:FBBodyNodeId
    kFBLeftFootMiddleCNodeId:FBBodyNodeId
    kFBLeftFootMiddleDNodeId:FBBodyNodeId
    kFBLeftFootMiddleInNodeId:FBBodyNodeId
    kFBLeftFootNodeId:FBBodyNodeId
    kFBLeftFootPinkyANodeId:FBBodyNodeId
    kFBLeftFootPinkyBNodeId:FBBodyNodeId
    kFBLeftFootPinkyCNodeId:FBBodyNodeId
    kFBLeftFootPinkyDNodeId:FBBodyNodeId
    kFBLeftFootPinkyInNodeId:FBBodyNodeId
    kFBLeftFootRingANodeId:FBBodyNodeId
    kFBLeftFootRingBNodeId:FBBodyNodeId
    kFBLeftFootRingCNodeId:FBBodyNodeId
    kFBLeftFootRingDNodeId:FBBodyNodeId
    kFBLeftFootRingInNodeId:FBBodyNodeId
    kFBLeftFootThumbANodeId:FBBodyNodeId
    kFBLeftFootThumbBNodeId:FBBodyNodeId
    kFBLeftFootThumbCNodeId:FBBodyNodeId
    kFBLeftFootThumbDNodeId:FBBodyNodeId
    kFBLeftFootThumbInNodeId:FBBodyNodeId
    kFBLeftHandNodeId:FBBodyNodeId
    kFBLeftHipNodeId:FBBodyNodeId
    """Required."""
    kFBLeftHipRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftHipRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftHipRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftHipRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftHipRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftHipRollNodeId:FBBodyNodeId
    kFBLeftIndexANodeId:FBBodyNodeId
    kFBLeftIndexBNodeId:FBBodyNodeId
    kFBLeftIndexCNodeId:FBBodyNodeId
    kFBLeftIndexDNodeId:FBBodyNodeId
    kFBLeftIndexInNodeId:FBBodyNodeId
    kFBLeftKneeNodeId:FBBodyNodeId
    """Required."""
    kFBLeftKneeRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftKneeRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftKneeRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftKneeRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftKneeRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftKneeRollNodeId:FBBodyNodeId
    kFBLeftMiddleANodeId:FBBodyNodeId
    kFBLeftMiddleBNodeId:FBBodyNodeId
    kFBLeftMiddleCNodeId:FBBodyNodeId
    kFBLeftMiddleDNodeId:FBBodyNodeId
    kFBLeftMiddleInNodeId:FBBodyNodeId
    kFBLeftPinkyANodeId:FBBodyNodeId
    kFBLeftPinkyBNodeId:FBBodyNodeId
    kFBLeftPinkyCNodeId:FBBodyNodeId
    kFBLeftPinkyDNodeId:FBBodyNodeId
    kFBLeftPinkyInNodeId:FBBodyNodeId
    kFBLeftRingANodeId:FBBodyNodeId
    kFBLeftRingBNodeId:FBBodyNodeId
    kFBLeftRingCNodeId:FBBodyNodeId
    kFBLeftRingDNodeId:FBBodyNodeId
    kFBLeftRingInNodeId:FBBodyNodeId
    kFBLeftShoulderNodeId:FBBodyNodeId
    """Required."""
    kFBLeftShoulderRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftShoulderRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftShoulderRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftShoulderRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftShoulderRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBLeftShoulderRollNodeId:FBBodyNodeId
    kFBLeftThumbANodeId:FBBodyNodeId
    kFBLeftThumbBNodeId:FBBodyNodeId
    kFBLeftThumbCNodeId:FBBodyNodeId
    kFBLeftThumbDNodeId:FBBodyNodeId
    kFBLeftThumbInNodeId:FBBodyNodeId
    kFBLeftWristNodeId:FBBodyNodeId
    """Required."""
    kFBNeck1NodeId:FBBodyNodeId
    kFBNeck2NodeId:FBBodyNodeId
    kFBNeck3NodeId:FBBodyNodeId
    kFBNeck4NodeId:FBBodyNodeId
    kFBNeck5NodeId:FBBodyNodeId
    kFBNeck6NodeId:FBBodyNodeId
    kFBNeck7NodeId:FBBodyNodeId
    kFBNeck8NodeId:FBBodyNodeId
    kFBNeck9NodeId:FBBodyNodeId
    kFBNeckNodeId:FBBodyNodeId
    kFBReferenceNodeId:FBBodyNodeId
    kFBRightAnkleNodeId:FBBodyNodeId
    """Required."""
    kFBRightCollarNodeId:FBBodyNodeId
    kFBRightElbowNodeId:FBBodyNodeId
    """Required."""
    kFBRightElbowRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightElbowRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightElbowRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightElbowRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightElbowRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightElbowRollNodeId:FBBodyNodeId
    kFBRightExtraFingerANodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFingerBNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFingerCNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFingerDNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFingerInNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFootFingerANodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFootFingerBNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFootFingerCNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFootFingerDNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightExtraFootFingerInNodeId:FBBodyNodeId
    """New extra finger bone."""
    kFBRightFootIndexANodeId:FBBodyNodeId
    kFBRightFootIndexBNodeId:FBBodyNodeId
    kFBRightFootIndexCNodeId:FBBodyNodeId
    kFBRightFootIndexDNodeId:FBBodyNodeId
    kFBRightFootIndexInNodeId:FBBodyNodeId
    kFBRightFootMiddleANodeId:FBBodyNodeId
    kFBRightFootMiddleBNodeId:FBBodyNodeId
    kFBRightFootMiddleCNodeId:FBBodyNodeId
    kFBRightFootMiddleDNodeId:FBBodyNodeId
    kFBRightFootMiddleInNodeId:FBBodyNodeId
    kFBRightFootNodeId:FBBodyNodeId
    kFBRightFootPinkyANodeId:FBBodyNodeId
    kFBRightFootPinkyBNodeId:FBBodyNodeId
    kFBRightFootPinkyCNodeId:FBBodyNodeId
    kFBRightFootPinkyDNodeId:FBBodyNodeId
    kFBRightFootPinkyInNodeId:FBBodyNodeId
    kFBRightFootRingANodeId:FBBodyNodeId
    kFBRightFootRingBNodeId:FBBodyNodeId
    kFBRightFootRingCNodeId:FBBodyNodeId
    kFBRightFootRingDNodeId:FBBodyNodeId
    kFBRightFootRingInNodeId:FBBodyNodeId
    kFBRightFootThumbANodeId:FBBodyNodeId
    kFBRightFootThumbBNodeId:FBBodyNodeId
    kFBRightFootThumbCNodeId:FBBodyNodeId
    kFBRightFootThumbDNodeId:FBBodyNodeId
    kFBRightFootThumbInNodeId:FBBodyNodeId
    kFBRightHandNodeId:FBBodyNodeId
    kFBRightHipNodeId:FBBodyNodeId
    """Required."""
    kFBRightHipRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightHipRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightHipRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightHipRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightHipRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightHipRollNodeId:FBBodyNodeId
    kFBRightIndexANodeId:FBBodyNodeId
    kFBRightIndexBNodeId:FBBodyNodeId
    kFBRightIndexCNodeId:FBBodyNodeId
    kFBRightIndexDNodeId:FBBodyNodeId
    kFBRightIndexInNodeId:FBBodyNodeId
    kFBRightKneeNodeId:FBBodyNodeId
    """Required."""
    kFBRightKneeRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightKneeRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightKneeRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightKneeRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightKneeRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightKneeRollNodeId:FBBodyNodeId
    kFBRightMiddleANodeId:FBBodyNodeId
    kFBRightMiddleBNodeId:FBBodyNodeId
    kFBRightMiddleCNodeId:FBBodyNodeId
    kFBRightMiddleDNodeId:FBBodyNodeId
    kFBRightMiddleInNodeId:FBBodyNodeId
    kFBRightPinkyANodeId:FBBodyNodeId
    kFBRightPinkyBNodeId:FBBodyNodeId
    kFBRightPinkyCNodeId:FBBodyNodeId
    kFBRightPinkyDNodeId:FBBodyNodeId
    kFBRightPinkyInNodeId:FBBodyNodeId
    kFBRightRingANodeId:FBBodyNodeId
    kFBRightRingBNodeId:FBBodyNodeId
    kFBRightRingCNodeId:FBBodyNodeId
    kFBRightRingDNodeId:FBBodyNodeId
    kFBRightRingInNodeId:FBBodyNodeId
    kFBRightShoulderNodeId:FBBodyNodeId
    """Required."""
    kFBRightShoulderRollNode1Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightShoulderRollNode2Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightShoulderRollNode3Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightShoulderRollNode4Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightShoulderRollNode5Id:FBBodyNodeId
    """New leaf roll bone."""
    kFBRightShoulderRollNodeId:FBBodyNodeId
    kFBRightThumbANodeId:FBBodyNodeId
    kFBRightThumbBNodeId:FBBodyNodeId
    kFBRightThumbCNodeId:FBBodyNodeId
    kFBRightThumbDNodeId:FBBodyNodeId
    kFBRightThumbInNodeId:FBBodyNodeId
    kFBRightWristNodeId:FBBodyNodeId
    """Required."""
    kFBSpine2NodeId:FBBodyNodeId
    kFBSpine3NodeId:FBBodyNodeId
    kFBSpine4NodeId:FBBodyNodeId
    kFBSpine5NodeId:FBBodyNodeId
    kFBSpine6NodeId:FBBodyNodeId
    kFBSpine7NodeId:FBBodyNodeId
    kFBSpine8NodeId:FBBodyNodeId
    kFBSpine9NodeId:FBBodyNodeId
    kFBWaistNodeId:FBBodyNodeId
    """Required, Spine 0."""
class FBBodyPartId(_Enum):
    """Body part for character."""
    kFBCtrlSetPartChest:FBBodyPartId
    """Chest Body Part."""
    kFBCtrlSetPartHead:FBBodyPartId
    """Head Body Part."""
    kFBCtrlSetPartHips:FBBodyPartId
    """Hips Body Part."""
    kFBCtrlSetPartLeftArm:FBBodyPartId
    """Left Arm Body Part."""
    kFBCtrlSetPartLeftFoot:FBBodyPartId
    """Left Foot Body Part."""
    kFBCtrlSetPartLeftHand:FBBodyPartId
    """Left Hand Body Part."""
    kFBCtrlSetPartLeftLeg:FBBodyPartId
    """Left Leg Body Part."""
    kFBCtrlSetPartNone:FBBodyPartId
    """No part selected."""
    kFBCtrlSetPartRightArm:FBBodyPartId
    """Right Arm Body Part."""
    kFBCtrlSetPartRightFoot:FBBodyPartId
    """Right Foot Body Part."""
    kFBCtrlSetPartRightHand:FBBodyPartId
    """Right Hand Body Part."""
    kFBCtrlSetPartRightLeg:FBBodyPartId
    """Right Leg Body Part."""
    kFBLastCtrlSetPartIndex:FBBodyPartId
    """Part count."""
class FBBorderStyle(_Enum):
    """Different border types available.
    See samples: Border.py, TabPanel.py."""
    kFBEmbossBorder:FBBorderStyle
    """Embossed border."""
    kFBEmbossEdgeSmoothBorder:FBBorderStyle
    """Edged smooth border."""
    kFBEmbossSmoothBorder:FBBorderStyle
    """Smooth border."""
    kFBEmbossSmoothEdgeBorder:FBBorderStyle
    """Smoothed edges border."""
    kFBHighlightBorder:FBBorderStyle
    """Highlight border."""
    kFBNoBorder:FBBorderStyle
    """No border."""
    kFBPickingBorder:FBBorderStyle
    """Picking border."""
    kFBStandardBorder:FBBorderStyle
    """Standard border."""
    kFBStandardEdgeSmoothBorder:FBBorderStyle
    """Standard edged smooth border."""
    kFBStandardSmoothBorder:FBBorderStyle
    """Standard smooth border."""
    kFBStandardSmoothEdgeBorder:FBBorderStyle
    """Standard smoothed edges border."""
class FBButtonLook(_Enum):
    """Button look.
    See sample: Button.py."""
    kFBLookAlphaBackground:FBButtonLook
    kFBLookColorChange:FBButtonLook
    kFBLookFlat:FBButtonLook
    kFBLookNormal:FBButtonLook
    kFBLookPush:FBButtonLook
class FBButtonState(_Enum):
    """Possible button states.
    Currently, only two button states are possible."""
    kFBButtonState0:FBButtonState
    """State is 0, usually meaning not active."""
    kFBButtonState1:FBButtonState
    """State is 1, usually meaning active."""
class FBButtonStyle(_Enum):
    """Style of buttons.
    Not all button styles are completely functional. See samples: Button.py, RadioButton.py."""
    kFB2States:FBButtonStyle
    """2 state button (2 colors)."""
    kFBBitmap2States:FBButtonStyle
    """2 state button with 2 bitmaps."""
    kFBBitmapButton:FBButtonStyle
    """Button with bitmap on it."""
    kFBCheckbox:FBButtonStyle
    """Check box."""
    kFBPushButton:FBButtonStyle
    """Normal button."""
    kFBRadioButton:FBButtonStyle
    """Radio button."""
class FBCameraAntiAliasingMethod(_Enum):
    """Antialiasing methods."""
    kFBAntiAliasingSoftware:FBCameraAntiAliasingMethod
    """Antaliasing in software."""
    kFBAntialiasingMultiSamplingOnyx:FBCameraAntiAliasingMethod
    """Multisampling (only on Onyx)."""
class FBCameraApertureMode(_Enum):
    """Aperture modes."""
    kFBApertureFocalLength:FBCameraApertureMode
    """Focal Length aperture varies."""
    kFBApertureHorizontal:FBCameraApertureMode
    """Horizontal aperture varies."""
    kFBApertureVertHoriz:FBCameraApertureMode
    """Vertical and horizontal aperture varies."""
    kFBApertureVertical:FBCameraApertureMode
    """Vertical aperture varies."""
class FBCameraDistanceMode(_Enum):
    """Camera plane distance modes."""
    kFBDistModeAbsoluteFromCamera:FBCameraDistanceMode
    """Camera plane distance absolute from camera."""
    kFBDistModeRelativeToInterest:FBCameraDistanceMode
    """Camera plane distance relative to interest."""
class FBCameraFilmBackType(_Enum):
    """Filmback types."""
    kFBFilmBack16mmTheatrical:FBCameraFilmBackType
    """16mm Theatrical."""
    kFBFilmBack35mm185Projection:FBCameraFilmBackType
    """35mm 185 Projection."""
    kFBFilmBack35mmAcademy:FBCameraFilmBackType
    """35mm Academy."""
    kFBFilmBack35mmAnamorphic:FBCameraFilmBackType
    """35mm Anamorphic."""
    kFBFilmBack35mmFullAperture:FBCameraFilmBackType
    """35mm Full Aperture."""
    kFBFilmBack35mmTVProjection:FBCameraFilmBackType
    """35mm TV Projection."""
    kFBFilmBack70mmProjection:FBCameraFilmBackType
    """70mm Projection."""
    kFBFilmBackCustom:FBCameraFilmBackType
    """Custom Filmback."""
    kFBFilmBackDynavision:FBCameraFilmBackType
    """Dynavision."""
    kFBFilmBackIMAX:FBCameraFilmBackType
    """IMAX."""
    kFBFilmBackSuper16mm:FBCameraFilmBackType
    """Super16mm."""
    kFBFilmBackVistaVision:FBCameraFilmBackType
    """Vista Vision."""
class FBCameraFocusDistanceSource(_Enum):
    """Focus distance sources."""
    kFBFocusDistanceCameraInterest:FBCameraFocusDistanceSource
    """Interest as source."""
    kFBFocusDistanceModel:FBCameraFocusDistanceSource
    """Another model's position as source."""
    kFBFocusDistanceSpecificDistance:FBCameraFocusDistanceSource
    """Specific distance as source."""
class FBCameraFrameSizeMode(_Enum):
    """Frame size modes."""
    kFBFrameSizeFixedHeightResolution:FBCameraFrameSizeMode
    """Fixed height resolution."""
    kFBFrameSizeFixedRatio:FBCameraFrameSizeMode
    """Fixed ratio."""
    kFBFrameSizeFixedResolution:FBCameraFrameSizeMode
    """Fixed resolution."""
    kFBFrameSizeFixedWidthResolution:FBCameraFrameSizeMode
    """Fixed width resolution."""
    kFBFrameSizeWindow:FBCameraFrameSizeMode
    """Frame size of window."""
class FBCameraMatrixType(_Enum):
    """Camera matrix types in OpenGL convention."""
    kFBModelView:FBCameraMatrixType
    """Camera's combined Model-View matrix."""
    kFBModelViewProj:FBCameraMatrixType
    """Camera's combined Model-View-Projection matrix."""
    kFBProjInverse:FBCameraMatrixType
    """Camera's Projection Inverse matrix."""
    kFBProjection:FBCameraMatrixType
    """Camera's Projection matrix."""
class FBCameraResolutionMode(_Enum):
    """Resolution modes."""
    kFBResolution128x128:FBCameraResolutionMode
    """128x128."""
    kFBResolution320x200:FBCameraResolutionMode
    """320x200."""
    kFBResolution320x240:FBCameraResolutionMode
    """320x240."""
    kFBResolution640x480:FBCameraResolutionMode
    """640x480."""
    kFBResolutionCustom:FBCameraResolutionMode
    """Custom resolution mode or From Camera as a render setting."""
    kFBResolutionD1NTSC:FBCameraResolutionMode
    """D1 NTSC."""
    kFBResolutionD1PAL:FBCameraResolutionMode
    """D1 PAL."""
    kFBResolutionFullScreen:FBCameraResolutionMode
    """FullScreen."""
    kFBResolutionHD:FBCameraResolutionMode
    """HD 1920x1080."""
    kFBResolutionNTSC:FBCameraResolutionMode
    """NTSC."""
    kFBResolutionPAL:FBCameraResolutionMode
    """PAL."""
class FBCameraSafeAreaMode(_Enum):
    """Safe area modes."""
    kFBSafeAreaRound:FBCameraSafeAreaMode
    """Round safe area."""
    kFBSafeAreaSquare:FBCameraSafeAreaMode
    """Square safe area."""
class FBCameraSamplingType(_Enum):
    """Antialiasing sampling types."""
    kFBSamplingStochastic:FBCameraSamplingType
    """Stochastic sampling."""
    kFBSamplingUniform:FBCameraSamplingType
    """Uniform sampling."""
class FBCameraStereoType(_Enum):
    kFBCameraStereoConverged:FBCameraStereoType
    kFBCameraStereoNone:FBCameraStereoType
    kFBCameraStereoOff_Axis:FBCameraStereoType
    kFBCameraStereoParallel:FBCameraStereoType
class FBCameraType(_Enum):
    """Focus distance types."""
    kFBCameraTypeOrthogonal:FBCameraType
    """Specific distance as source."""
    kFBCameraTypePerspective:FBCameraType
    """Interest as source."""
class FBCameraViewPlaneMode(_Enum):
    """Camera plane viewing modes."""
    kFBViewPlaneAlways:FBCameraViewPlaneMode
    """Always draw camera plane."""
    kFBViewPlaneDisabled:FBCameraViewPlaneMode
    """Camera plane disabled."""
    kFBViewPlaneWhenMedia:FBCameraViewPlaneMode
    """Camera plane when media."""
class FBCellStyle(_Enum):
    """Different styles of spreadsheet cell styles."""
    kFBCellStyle2StatesButton:FBCellStyle
    """2 state button."""
    kFBCellStyle3StatesButton:FBCellStyle
    """3 state button."""
    kFBCellStyleButton:FBCellStyle
    """Button."""
    kFBCellStyleDefault:FBCellStyle
    """Default cell style."""
    kFBCellStyleDouble:FBCellStyle
    """Double."""
    kFBCellStyleInteger:FBCellStyle
    """Integer."""
    kFBCellStyleMenu:FBCellStyle
    """Menu."""
    kFBCellStyleString:FBCellStyle
    """String."""
    kFBCellStyleTime:FBCellStyle
    """Time."""
    kFBCellStyleView:FBCellStyle
    """View (user definable, you need to specify the view using FBSpread::SetCellView())."""
    kFBCellStyleVoid:FBCellStyle
    """Void (no value)."""
class FBCharacterContactBehaviour(_Enum):
    """Character Contact Behaviour."""
    kFBLastContactBehaviour:FBCharacterContactBehaviour
    kFBParamContactAlwaysSync:FBCharacterContactBehaviour
    kFBParamContactNeverSync:FBCharacterContactBehaviour
    kFBParamContactSyncOnKey:FBCharacterContactBehaviour
class FBCharacterExtensionRetargetMode(_Enum):
    """Character extension Retarget Mode"""
    kFBRetargetModeAuto:FBCharacterExtensionRetargetMode
    kFBRetargetModeManual:FBCharacterExtensionRetargetMode
    kFBRetargetModeOff:FBCharacterExtensionRetargetMode
class FBCharacterExtensionStancePoseMode(_Enum):
    """Character Extension Stance Pose mode when the stance pose is activated on a character."""
    kFBStancePose_Always:FBCharacterExtensionStancePoseMode
    kFBStancePose_Never:FBCharacterExtensionStancePoseMode
    kFBStancePose_Reference_Selected:FBCharacterExtensionStancePoseMode
    kFBStancePose_Selected:FBCharacterExtensionStancePoseMode
    kFBStancePose_Self_Or_Reference_Selected:FBCharacterExtensionStancePoseMode
class FBCharacterHipsTranslationMode(_Enum):
    """Character Hips Translation modes."""
    kFBLastHipsTranslationMode:FBCharacterHipsTranslationMode
    kFBParamHipsTranslationBodyRigid:FBCharacterHipsTranslationMode
    kFBParamHipsTranslationWorldRigid:FBCharacterHipsTranslationMode
class FBCharacterInputType(_Enum):
    """Character Input/Output types."""
    kFBCharacterInputActor:FBCharacterInputType
    kFBCharacterInputCharacter:FBCharacterInputType
    kFBCharacterInputMarkerSet:FBCharacterInputType
    kFBCharacterInputMoCap:FBCharacterInputType
    kFBCharacterInputStance:FBCharacterInputType
    kFBCharacterOutputMarkerSet:FBCharacterInputType
class FBCharacterKeyingMode(_Enum):
    """Character keying modes."""
    kFBCharacterKeyingBodyPart:FBCharacterKeyingMode
    kFBCharacterKeyingFullBody:FBCharacterKeyingMode
    kFBCharacterKeyingFullBodyNoPull:FBCharacterKeyingMode
    kFBCharacterKeyingSelection:FBCharacterKeyingMode
class FBCharacterLoadAnimationMethod(_Enum):
    """This enumeration is used to choose how to load an animation file on a character."""
    kFBCharacterLoadConnect:FBCharacterLoadAnimationMethod
    """Only connect the loaded character as an input."""
    kFBCharacterLoadCopy:FBCharacterLoadAnimationMethod
    """Copy keys from loaded character to target character."""
    kFBCharacterLoadPlot:FBCharacterLoadAnimationMethod
    """Plot animation from loaded character to target character."""
    kFBCharacterLoadPlotIfSampled:FBCharacterLoadAnimationMethod
    """If loaded animation seems sampled, plot animation from loaded character to target character; else retarget."""
    kFBCharacterLoadRetarget:FBCharacterLoadAnimationMethod
    """Retarget (copy and correct) keys from loaded character to target character."""
class FBCharacterPlotWhere(_Enum):
    """Where to plot a character."""
    kFBCharacterPlotOnControlRig:FBCharacterPlotWhere
    kFBCharacterPlotOnSkeleton:FBCharacterPlotWhere
class FBCharacterPoseFlag(_Enum):
    """Character Pose Options flags."""
    kFBCharacterPoseGravity:FBCharacterPoseFlag
    kFBCharacterPoseMatchFKTranslation:FBCharacterPoseFlag
    kFBCharacterPoseMatchPivot:FBCharacterPoseFlag
    kFBCharacterPoseMatchR:FBCharacterPoseFlag
    kFBCharacterPoseMatchTX:FBCharacterPoseFlag
    kFBCharacterPoseMatchTY:FBCharacterPoseFlag
    kFBCharacterPoseMatchTZ:FBCharacterPoseFlag
    kFBCharacterPoseMirror:FBCharacterPoseFlag
    kFBCharacterPoseNoFlag:FBCharacterPoseFlag
    kFBCharacterPoseUseKeyingGroup:FBCharacterPoseFlag
class FBCharacterPoseKeyingMode(_Enum):
    """Character Pose Keying Mode."""
    kFBCharacterPoseKeyingModeBodyPart:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeCount:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeFullBody:FBCharacterPoseKeyingMode
    kFBCharacterPoseKeyingModeInvalid:FBCharacterPoseKeyingMode
class FBCharacterResetProperties(_Enum):
    """Character Reset Properties Type."""
    kFBCharacterResetPropertiesAll:FBCharacterResetProperties
    kFBCharacterResetPropertiesDefinition:FBCharacterResetProperties
    kFBCharacterResetPropertiesSolving:FBCharacterResetProperties
class FBCharacterRollSolver(_Enum):
    """Character Roll Solver version."""
    kFBLastRollSolver:FBCharacterRollSolver
    kFBParamRollSolver70:FBCharacterRollSolver
    kFBParamRollSolver75:FBCharacterRollSolver
class FBClipEnd(_Enum):
    """Clip end actions."""
    kFBClipEndEnd:FBClipEnd
    """On clip end stop clip."""
    kFBClipEndLoop:FBClipEnd
    """On clip end loop clip."""
class FBClusterMode(_Enum):
    """Different clustering modes."""
    kFBClusterAdditive:FBClusterMode
    """Add the values together."""
    kFBClusterNormalize:FBClusterMode
    """Normalize (values between 0.0 and 1.0 )"""
    kFBClusterTotal100:FBClusterMode
    """The balanced values will add up to 100 percent."""
class FBCommPortType(_Enum):
    """Communication port type."""
    kFBInternal:FBCommPortType
    """Internal."""
    kFBPhysical:FBCommPortType
    """Physical."""
    kFBVirtual:FBCommPortType
    """Virtual."""
class FBCommType(_Enum):
    """Communications type.
    Different base types of communications. There is always the 'other' type in order to use another type of communication."""
    kFBCommTypeNetworkTCP:FBCommType
    """Network (TCP) device."""
    kFBCommTypeNetworkUDP:FBCommType
    """Network (UDP) device."""
    kFBCommTypeNone:FBCommType
    """A non-communicating device."""
    kFBCommTypeOther:FBCommType
    """Any other type of communications."""
    kFBCommTypeSerial:FBCommType
    """Serial communications."""
    kFBCommTypeSharedMemory:FBCommType
    """Accessing shared memory."""
    kFBCommTypeSimulator:FBCommType
    """Software simulator."""
class FBCommandState(_Enum):
    """FBCommandState."""
    kFBCommandStateMute:FBCommandState
    """Mute."""
    kFBCommandStateMuteBecauseSolo:FBCommandState
    """Mute because of solo."""
    kFBCommandStateSolo:FBCommandState
    """Solo."""
    kFBCommandStateStandard:FBCommandState
    """Standard."""
class FBConnectionAction(_Enum):
    """Possible actions when a notify plug event occurs."""
    kFBBeginChange:FBConnectionAction
    """Begin change on destination."""
    kFBBeginReplaceDst:FBConnectionAction
    """Begin replace destination during merge."""
    kFBBeginReplaceSrc:FBConnectionAction
    """Begin replace source during merge."""
    kFBCandidate:FBConnectionAction
    """Data candidate event, before the data is set."""
    kFBCandidateGlobal:FBConnectionAction
    """Data candidate event, global candidate."""
    kFBCandidated:FBConnectionAction
    """Data candidate event, after the data is set."""
    kFBConnect:FBConnectionAction
    kFBConnectDst:FBConnectionAction
    """Connect destination to source."""
    kFBConnectSrc:FBConnectionAction
    """Connect source to destination."""
    kFBConnected:FBConnectionAction
    kFBConnectedDst:FBConnectionAction
    """Connected destination to source."""
    kFBConnectedOwner:FBConnectionAction
    """Connected owner to destination."""
    kFBConnectedSrc:FBConnectionAction
    """Connected source to destination."""
    kFBDescription:FBConnectionAction
    """Component description event."""
    kFBDestroy:FBConnectionAction
    """Component destroy."""
    kFBDetached:FBConnectionAction
    """Component detached from scene."""
    kFBDisconnect:FBConnectionAction
    kFBDisconnectDst:FBConnectionAction
    """Disconnect destination from source."""
    kFBDisconnectOwner:FBConnectionAction
    """Disconnect owner from destination."""
    kFBDisconnectSrc:FBConnectionAction
    """Disconnect source from destination."""
    kFBDisconnected:FBConnectionAction
    kFBDisconnectedDst:FBConnectionAction
    """Disconnected destination from source."""
    kFBDisconnectedSrc:FBConnectionAction
    """Disconnected source from destination."""
    kFBEndChange:FBConnectionAction
    """End change on destination."""
    kFBEndReplaceDst:FBConnectionAction
    """End replace destination during merge."""
    kFBEndReplaceSrc:FBConnectionAction
    """End replace source during merge."""
    kFBKeyingCandidate:FBConnectionAction
    """Component keying candidate event."""
    kFBKeyingCurveChange:FBConnectionAction
    """Component curve has changed."""
    kFBKeyingCurveEndChange:FBConnectionAction
    """Component curve changes in Dopesheet completed."""
    kFBKeyingDeleteKey:FBConnectionAction
    """Component keying delete event."""
    kFBKeyingKey:FBConnectionAction
    """Component keying add event."""
    kFBPrefixRename:FBConnectionAction
    """Component prefix is going to be renamed."""
    kFBPrefixRenamed:FBConnectionAction
    """Component prefix has been renamed."""
    kFBRename:FBConnectionAction
    """Component is going to be renamed."""
    kFBRenamed:FBConnectionAction
    """Component has been renamed."""
    kFBReorderSrc:FBConnectionAction
    """Reorder of source."""
    kFBReorderedSrc:FBConnectionAction
    """Source has been reordered."""
    kFBRequestConnectDst:FBConnectionAction
    """Request connection of destination to source."""
    kFBRequestConnectSrc:FBConnectionAction
    """Request connection of source to destination."""
    kFBRequestDisconnectDst:FBConnectionAction
    """Request disconnection of destination to source."""
    kFBRequestDisconnectSrc:FBConnectionAction
    """Request disconnection of source to destination."""
    kFBRequestPrefixRename:FBConnectionAction
    """Compoent request Prefix Rename."""
    kFBRequestRename:FBConnectionAction
    """Component request rename."""
    kFBReselect:FBConnectionAction
    """Component re-selection."""
    kFBSelect:FBConnectionAction
    """Component selection."""
    kFBUnselect:FBConnectionAction
    """Component de-selection."""
class FBConnectionType(_Enum):
    """Connection types available between plugs."""
    kFBConnectionTypeNone:FBConnectionType
    """Default connection type."""
    kFBConnectionTypeSystem:FBConnectionType
    """System connection type."""
class FBConsoleChannelType(_Enum):
    """Console channel types."""
    kFBConsoleButton:FBConsoleChannelType
    """Button."""
    kFBConsoleDisplay:FBConsoleChannelType
    """Display."""
    kFBConsoleEncoder:FBConsoleChannelType
    """Generic encoder."""
    kFBConsoleJoystick:FBConsoleChannelType
    """Joystick."""
    kFBConsoleKey:FBConsoleChannelType
    """Key."""
    kFBConsoleNull:FBConsoleChannelType
    """Generic type."""
    kFBConsoleSlider:FBConsoleChannelType
    """Slider."""
    kFBConsoleTransport:FBConsoleChannelType
    """Transport."""
class FBConstantKeyReducerThresholdType(_Enum):
    """Different threshold types for the Constant Key Reducer filter."""
    kFBDefaultThreshold:FBConstantKeyReducerThresholdType
    """All other curves threshold."""
    kFBRotationThreshold:FBConstantKeyReducerThresholdType
    """Rotation threshold."""
    kFBScalingThreshold:FBConstantKeyReducerThresholdType
    """Scaling threshold."""
    kFBTranslationThreshold:FBConstantKeyReducerThresholdType
    """Translation threshold."""
class FBConstructionHistoryState(_Enum):
    """Construction history manager state."""
    kFBConstructionHistory_Listening:FBConstructionHistoryState
    """Construction history is currently listening and recording operations."""
    kFBConstructionHistory_Replaying:FBConstructionHistoryState
    """Construction history is currently replaying an operation."""
class FBControlSetType(_Enum):
    """Character ControlSet type."""
    kFBControlSetTypeFKIK:FBControlSetType
    kFBControlSetTypeIKOnly:FBControlSetType
    kFBControlSetTypeNone:FBControlSetType
class FBControllerMode(_Enum):
    """Controller modes for optical model."""
    kFBControllerLabelling:FBControllerMode
    """Labelling controller."""
    kFBControllerNone:FBControllerMode
    """No controller mode."""
    kFBControllerRigidBody:FBControllerMode
    """Rigid body controller."""
    kFBControllerSegment:FBControllerMode
    """Segment controller."""
class FBDataAsStringFlag(_Enum):
    """FBDataAsStringFlag."""
    kFBDataAsStringPersistence:FBDataAsStringFlag
    """Convert data to string type for storage."""
    kFBDataAsStringUI:FBDataAsStringFlag
    """Convert data to string type for UI display."""
class FBDeckTransportMode(_Enum):
    """FBDeckTransportMode."""
    kFBDeckTransportMain:FBDeckTransportMode
    """Transport main."""
    kFBDeckTransportMaster:FBDeckTransportMode
    """K_DEPRECATED_2021, use kFBDeckTransportMain."""
    kFBDeckTransportNone:FBDeckTransportMode
    """No transport interaction."""
    kFBDeckTransportSlave:FBDeckTransportMode
    """K_DEPRECATED_2021, use kFBDeckTransportSync."""
    kFBDeckTransportSync:FBDeckTransportMode
    """Sync to transport controls."""
class FBDeformerType(_Enum):
    """Determine the deformer type.
    kFBDeformerSkeleton Skeleton (Bone) driven skinning deformer.kFBDeformerPointCache Pre-recorded point cache deformer.kFBGeometryMapping_BY_POLYGON_VERTEX There will be one mapping coordinate for each vertex, for each polygon/strip it is part of. This means that a vertex will have as many mapping coordinates as polygons it is part of.kFBGeometryMapping_BY_POLYGON There can be only one mapping coordinate for the whole polygon/strip.kFBGeometryMapping_BY_EDGE There will be one mapping coordinate for each unique edge in the mesh. This is meant to be used with smoothing layer elements.kFBGeometryMapping_ALL_SAME There can be only one mapping coordinate for the whole surface."""
    kFBDeformerPointCache:FBDeformerType
    kFBDeformerSkeleton:FBDeformerType
    kFBDeformerUnkown:FBDeformerType
class FBDeviceKeyboardKey(_Enum):
    """Keyboard keys (for input)."""
    kFBDKey0:FBDeviceKeyboardKey
    """'0'."""
    kFBDKey1:FBDeviceKeyboardKey
    """'1'."""
    kFBDKey2:FBDeviceKeyboardKey
    """'2'."""
    kFBDKey3:FBDeviceKeyboardKey
    """'3'."""
    kFBDKey4:FBDeviceKeyboardKey
    """'4'."""
    kFBDKey5:FBDeviceKeyboardKey
    """'5'."""
    kFBDKey6:FBDeviceKeyboardKey
    """'6'."""
    kFBDKey7:FBDeviceKeyboardKey
    """'7'."""
    kFBDKey8:FBDeviceKeyboardKey
    """'8'."""
    kFBDKey9:FBDeviceKeyboardKey
    """'9'."""
    kFBDKeyArrowDown:FBDeviceKeyboardKey
    """Down."""
    kFBDKeyArrowLeft:FBDeviceKeyboardKey
    """Left."""
    kFBDKeyArrowRight:FBDeviceKeyboardKey
    """Right."""
    kFBDKeyArrowUp:FBDeviceKeyboardKey
    """Up."""
    kFBDKeyEnd:FBDeviceKeyboardKey
    """End."""
    kFBDKeyEscape:FBDeviceKeyboardKey
    """Escape."""
    kFBDKeyF1:FBDeviceKeyboardKey
    """'F1'."""
    kFBDKeyF10:FBDeviceKeyboardKey
    """'F10'."""
    kFBDKeyF11:FBDeviceKeyboardKey
    """'F11'."""
    kFBDKeyF12:FBDeviceKeyboardKey
    """'F12'."""
    kFBDKeyF2:FBDeviceKeyboardKey
    """'F2'."""
    kFBDKeyF3:FBDeviceKeyboardKey
    """'F3'."""
    kFBDKeyF4:FBDeviceKeyboardKey
    """'F4'."""
    kFBDKeyF5:FBDeviceKeyboardKey
    """'F5'"""
    kFBDKeyF6:FBDeviceKeyboardKey
    """'F6'."""
    kFBDKeyF7:FBDeviceKeyboardKey
    """'F7'."""
    kFBDKeyF8:FBDeviceKeyboardKey
    """'F8'."""
    kFBDKeyF9:FBDeviceKeyboardKey
    """'F9'."""
    kFBDKeyHome:FBDeviceKeyboardKey
    """Home."""
    kFBDKeyPageDown:FBDeviceKeyboardKey
    """Page Down."""
    kFBDKeyPageUp:FBDeviceKeyboardKey
    """Page Up."""
    kFBDKeyReturn:FBDeviceKeyboardKey
    """Return."""
    kFBDKeySpace:FBDeviceKeyboardKey
    """Space bar."""
class FBDeviceSamplingMode(_Enum):
    """Recording types.
    The different values for this will control the way the keys are added when the device is being recorded. There are four different types of recording keys for devices:Hardware Timestamping. This case is when the hardware provides timestamps with each packet.Hardware Frequency. The hardware is guaranteed to provide packets at a given frequency.Auto Frequency Packets are coming in at a fixed, unknown frequency. The recorded data will be resampled to be equidistant.Software Timestamping. The application will provide a timestamp for each packet depending on when it receives the data."""
    kFBAutoFrequency:FBDeviceSamplingMode
    """Device is running at unknown, fixed frequency."""
    kFBHardwareFrequency:FBDeviceSamplingMode
    """Device is running at known, fixed frequency."""
    kFBHardwareTimestamp:FBDeviceSamplingMode
    """Device supplies timestamp."""
    kFBSoftwareTimestamp:FBDeviceSamplingMode
    """The software will timestamp packets as they arrive."""
class FBDisplayMode(_Enum):
    """Model display options."""
    kFBDisplayModeCount:FBDisplayMode
    """End of enum, this value indicates the number of display modes available."""
    kFBDisplayModeDefault:FBDisplayMode
    """Use default display mode."""
    kFBDisplayModeFlatShade:FBDisplayMode
    """Flat shading."""
    kFBDisplayModeHardShade:FBDisplayMode
    """Hard shading."""
    kFBDisplayModeTexture:FBDisplayMode
    """Textures are displayed."""
    kFBDisplayModeWireFrame:FBDisplayMode
    """Wire-frame rendering."""
class FBDisplayWhat(_Enum):
    """Model display mask This mask determines what types of models are displayed by the renderer."""
    kFBDisplay3dIcon:FBDisplayWhat
    """3D icons are displayed (3D icons are 3D elements that do not exist in the scene)."""
    kFBDisplayAll:FBDisplayWhat
    """Everything is displayed."""
    kFBDisplayCamera:FBDisplayWhat
    """Cameras are displayed."""
    kFBDisplayCenter:FBDisplayWhat
    """Centers are displayed."""
    kFBDisplayLight:FBDisplayWhat
    """Lights are displayed."""
    kFBDisplayMarker:FBDisplayWhat
    """Markers are displayed."""
    kFBDisplayNone:FBDisplayWhat
    """Nothing is displayed."""
    kFBDisplayNull:FBDisplayWhat
    """Null models are displayed."""
    kFBDisplaySkeleton:FBDisplayWhat
    """Skeletons and bones are displayed."""
class FBDragAndDropState(_Enum):
    """State of Drag and Drop.
    See samples: PropertyDrop.py, Spread.py."""
    kFBDragAndDropBegin:FBDragAndDropState
    """Begin a drag and drop sequence."""
    kFBDragAndDropDrag:FBDragAndDropState
    """Dragging."""
    kFBDragAndDropDrop:FBDragAndDropState
    """Dropping."""
    kFBDragAndDropEnd:FBDragAndDropState
    """End of drag and drop."""
    kFBDragOnEmpty:FBDragAndDropState
    """Empty the drag and drop stack."""
    kFBDragOnEmptyDrop:FBDragAndDropState
    """Dropping empty stack."""
class FBEffectorId(_Enum):
    """All effector nodes."""
    kFBChestEndEffectorId:FBEffectorId
    kFBChestOriginEffectorId:FBEffectorId
    kFBHeadEffectorId:FBEffectorId
    kFBHipsEffectorId:FBEffectorId
    kFBInvalidEffectorId:FBEffectorId
    kFBLastEffectorId:FBEffectorId
    kFBLeftAnkleEffectorId:FBEffectorId
    kFBLeftElbowEffectorId:FBEffectorId
    kFBLeftFootEffectorId:FBEffectorId
    kFBLeftFootExtraFingerEffectorId:FBEffectorId
    kFBLeftFootIndexEffectorId:FBEffectorId
    kFBLeftFootMiddleEffectorId:FBEffectorId
    kFBLeftFootPinkyEffectorId:FBEffectorId
    kFBLeftFootRingEffectorId:FBEffectorId
    kFBLeftFootThumbEffectorId:FBEffectorId
    kFBLeftHandEffectorId:FBEffectorId
    kFBLeftHandExtraFingerEffectorId:FBEffectorId
    kFBLeftHandIndexEffectorId:FBEffectorId
    kFBLeftHandMiddleEffectorId:FBEffectorId
    kFBLeftHandPinkyEffectorId:FBEffectorId
    kFBLeftHandRingEffectorId:FBEffectorId
    kFBLeftHandThumbEffectorId:FBEffectorId
    kFBLeftHipEffectorId:FBEffectorId
    kFBLeftKneeEffectorId:FBEffectorId
    kFBLeftShoulderEffectorId:FBEffectorId
    kFBLeftWristEffectorId:FBEffectorId
    kFBRightAnkleEffectorId:FBEffectorId
    kFBRightElbowEffectorId:FBEffectorId
    kFBRightFootEffectorId:FBEffectorId
    kFBRightFootExtraFingerEffectorId:FBEffectorId
    kFBRightFootIndexEffectorId:FBEffectorId
    kFBRightFootMiddleEffectorId:FBEffectorId
    kFBRightFootPinkyEffectorId:FBEffectorId
    kFBRightFootRingEffectorId:FBEffectorId
    kFBRightFootThumbEffectorId:FBEffectorId
    kFBRightHandEffectorId:FBEffectorId
    kFBRightHandExtraFingerEffectorId:FBEffectorId
    kFBRightHandIndexEffectorId:FBEffectorId
    kFBRightHandMiddleEffectorId:FBEffectorId
    kFBRightHandPinkyEffectorId:FBEffectorId
    kFBRightHandRingEffectorId:FBEffectorId
    kFBRightHandThumbEffectorId:FBEffectorId
    kFBRightHipEffectorId:FBEffectorId
    kFBRightKneeEffectorId:FBEffectorId
    kFBRightShoulderEffectorId:FBEffectorId
    kFBRightWristEffectorId:FBEffectorId
class FBEffectorSetID(_Enum):
    """Effector ID identifier."""
    EFBffectorSetAux7:FBEffectorSetID
    FBEffectorSetAux1:FBEffectorSetID
    FBEffectorSetAux10:FBEffectorSetID
    FBEffectorSetAux11:FBEffectorSetID
    FBEffectorSetAux12:FBEffectorSetID
    FBEffectorSetAux13:FBEffectorSetID
    FBEffectorSetAux14:FBEffectorSetID
    FBEffectorSetAux2:FBEffectorSetID
    FBEffectorSetAux3:FBEffectorSetID
    FBEffectorSetAux4:FBEffectorSetID
    FBEffectorSetAux5:FBEffectorSetID
    FBEffectorSetAux6:FBEffectorSetID
    FBEffectorSetAux8:FBEffectorSetID
    FBEffectorSetAux9:FBEffectorSetID
    FBEffectorSetDefault:FBEffectorSetID
    FBLastEffectorSetIndex:FBEffectorSetID
class FBElementAction(_Enum):
    """Enumeration that describe the different actions available on a scene element depending on the current context."""
    kFBElementActionAppend:FBElementAction
    """Append the elements to the current scene elements (when loading or merging)."""
    kFBElementActionDiscard:FBElementAction
    """Do not consider the element (when loading, merging and saving)."""
    kFBElementActionMerge:FBElementAction
    """Merge the elements from the file in the current scene (when merging)."""
    kFBElementActionSave:FBElementAction
    """Save the element (when saving)."""
class FBEventAnimationNodeType(_Enum):
    """Event based on animation node.
    Types of transformation."""
    kFBEventAnimationNodeConstraintChange:FBEventAnimationNodeType
    kFBEventAnimationNodeDataChange:FBEventAnimationNodeType
    kFBEventAnimationNodeNone:FBEventAnimationNodeType
class FBEventName(_Enum):
    """These events are used internally by the Python Callback mecanism.
    These are not meant to be manipulated by a user."""
    kFBEventActivate:FBEventName
    kFBEventCellChange:FBEventName
    kFBEventChange:FBEventName
    kFBEventColumnClick:FBEventName
    kFBEventDoubleClick:FBEventName
    kFBEventDragAndDrop:FBEventName
    kFBEventEnter:FBEventName
    kFBEventExit:FBEventName
    kFBEventExpose:FBEventName
    kFBEventFileExit:FBEventName
    kFBEventFileMerge:FBEventName
    kFBEventFileNew:FBEventName
    kFBEventFileNewCompleted:FBEventName
    kFBEventFileOpen:FBEventName
    kFBEventFileOpenCompleted:FBEventName
    kFBEventFileSave:FBEventName
    kFBEventFileSaveCompleted:FBEventName
    kFBEventIdle:FBEventName
    kFBEventInput:FBEventName
    kFBEventMenu:FBEventName
    kFBEventOnClick:FBEventName
    kFBEventOnClickCheck:FBEventName
    kFBEventResize:FBEventName
    kFBEventRowClick:FBEventName
    kFBEventShow:FBEventName
    kFBEventTransaction:FBEventName
    kFBEventTreeCollapsed:FBEventName
    kFBEventTreeCollapsing:FBEventName
    kFBEventTreeExpanded:FBEventName
    kFBEventTreeExpanding:FBEventName
    kFBEventTreeSelect:FBEventName
    kFBEventUnbindSDK:FBEventName
class FBExistingClipAction(_Enum):
    """Action to perform, when preparing an Audio In object to record, when the action clip associated to the recording path is already in the scene."""
    kFBExistingClipAbortOperation:FBExistingClipAction
    """Cancel preparing the audio in to record."""
    kFBExistingClipAskUser:FBExistingClipAction
    """Ask the user for desired operation via a dialog."""
    kFBExistingClipRemove:FBExistingClipAction
    """Remove the action clip from the scene."""
class FBExistingFileAction(_Enum):
    """Action to perform, when preparing an Audio In object to record, when the action clip associated to the recording path already exists on disk and is not empty."""
    kFBExistingFileAbortOperation:FBExistingFileAction
    """Cancel preparing the audio in to record."""
    kFBExistingFileAppend:FBExistingFileAction
    """Append the new recording to existing recording. Warning: Be sure that the current file format match your recording option!"""
    kFBExistingFileAskUser:FBExistingFileAction
    """Ask the user for desired operation via a dialog."""
    kFBExistingFileOverwrite:FBExistingFileAction
    """Overwrite the existing file on disk."""
class FBExtrapolationMode(_Enum):
    """Modes for pre / post extrapolation."""
    kFCurveExtrapolationConst:FBExtrapolationMode
    kFCurveExtrapolationKeepSlope:FBExtrapolationMode
    kFCurveExtrapolationMirrorRepetition:FBExtrapolationMode
    kFCurveExtrapolationRelativeRepetition:FBExtrapolationMode
    kFCurveExtrapolationRepetition:FBExtrapolationMode
class FBFCurveEventType(_Enum):
    """This enum indicates what modification was made to a tracked FCurve."""
    kFBFCurveEventTypeDerivativedChanged:FBFCurveEventType
    """A key left/right/both derivative was changed, please note that this event can affect the key specified in the event index and the following key."""
    kFBFCurveEventTypeKeyAdded:FBFCurveEventType
    """A new key was added."""
    kFBFCurveEventTypeKeyBiasChanged:FBFCurveEventType
    """A key bias was changed (only valid on TCB key)"""
    kFBFCurveEventTypeKeyContinuityChanged:FBFCurveEventType
    """A key continuity was changed (only valid on TCB key)"""
    kFBFCurveEventTypeKeyInterpolationChanged:FBFCurveEventType
    """A key interpolation mode was changed."""
    kFBFCurveEventTypeKeyMassOperation:FBFCurveEventType
    """An operation affecting multiple keys was made."""
    kFBFCurveEventTypeKeyPostExtrapolationChanged:FBFCurveEventType
    """A curve post-extrapolation value was changed."""
    kFBFCurveEventTypeKeyPreExtrapolationChanged:FBFCurveEventType
    """A curve pre-extrapolation value was changed."""
    kFBFCurveEventTypeKeyRemoved:FBFCurveEventType
    """A key was removed."""
    kFBFCurveEventTypeKeyTangentBreakChanged:FBFCurveEventType
    """A key break mode was changed."""
    kFBFCurveEventTypeKeyTangentChanged:FBFCurveEventType
    """A key tangent was changed."""
    kFBFCurveEventTypeKeyTangentClampModeChanged:FBFCurveEventType
    """A key clamping mode was changed."""
    kFBFCurveEventTypeKeyTangentConstantChanged:FBFCurveEventType
    """A key constant mode was changed."""
    kFBFCurveEventTypeKeyTensionChanged:FBFCurveEventType
    """A key tension was changed (only valid on TCB key)"""
    kFBFCurveEventTypeKeyTimeChanged:FBFCurveEventType
    """A key time was changed."""
    kFBFCurveEventTypeKeyValueChanged:FBFCurveEventType
    """A key value was changed."""
    kFBFCurveEventTypeKeyVelocityChanged:FBFCurveEventType
    """A key velocity was changed."""
    kFBFCurveEventTypeKeyWeightChanged:FBFCurveEventType
    """A key left/right weight was changed, please note that this event can affect the key specified in the event index and the following key."""
    kFBFCurveEventTypeUnknownOperation:FBFCurveEventType
    """Invalid event."""
class FBFileFormatAndVersion(_Enum):
    kFBDefaultFormatAndVersion:FBFileFormatAndVersion
    """Default Format and Version."""
    kFBFBX2010:FBFileFormatAndVersion
    """It's FBX Version 6. Note: it's not equivalent to MotionBuilder 2010 Native FBX format."""
    kFBFBX2011:FBFileFormatAndVersion
    """FBX Version 2011."""
    kFBFBX2012:FBFileFormatAndVersion
    """FBX Version 2012."""
    kFBFBX2013:FBFileFormatAndVersion
    """FBX Version 2013."""
    kFBFBX2014_2015:FBFileFormatAndVersion
    """FBX Version 2014/2015."""
    kFBFBX2016:FBFileFormatAndVersion
    """FBX Version 2016."""
    kFBFBX2018:FBFileFormatAndVersion
    """FBX Version 2018."""
    kFBFBX2019:FBFileFormatAndVersion
    """FBX Version 2019."""
    kFBFBX2020:FBFileFormatAndVersion
    """FBX Version 2020."""
class FBFileMonitoringType(_Enum):
    """File Monitoring Type."""
    kFBFileMonitoring_ANIMATIONCLIP:FBFileMonitoringType
    """Animation clip change monitoring."""
    kFBFileMonitoring_FILEREFERENCE:FBFileMonitoringType
    """File Reference change monitoring."""
    kFBFileMonitoring_InvalidIndex:FBFileMonitoringType
    """Invalid value."""
    kFBFileMonitoring_MAINSCENE:FBFileMonitoringType
    """Main Scene change monitoring."""
    kFBFileMonitoring_PYTHONEDITORSCRIPT:FBFileMonitoringType
    """Python Editor Script change monitoring."""
class FBFilePopupStyle(_Enum):
    """Different types of file popup windows.
    See samples: FBFilePopup.py, FBFolderPopup.py."""
    kFBFilePopupOpen:FBFilePopupStyle
    """Open file popup (Shows 'Open Directory')."""
    kFBFilePopupSave:FBFilePopupStyle
    """Save file popup (Shows 'Save Directory')."""
class FBFilterType(_Enum):
    """Filter types.
    A filter can be of one or both types in order to process data on single or multiple curves of data. Ex: a gimble killer filter needs to be of type vector because the three curves are inter-dependant."""
    kFBFilterNumber:FBFilterType
    """Filter single FCurves."""
    kFBFilterVector:FBFilterType
    """Filter a vector (3 FCurves)."""
class FBFloorContactID(_Enum):
    """Floor contact for the given index."""
    FBLastCharacterMember:FBFloorContactID
    FBLeftFootMemberIndex:FBFloorContactID
    FBLeftHandMemberIndex:FBFloorContactID
    FBRightFootMemberIndex:FBFloorContactID
    FBRightHandMemberIndex:FBFloorContactID
class FBFogMode(_Enum):
    """Fog falloff modes."""
    kFBFogModeExponential:FBFogMode
    """Exponential falloff."""
    kFBFogModeLinear:FBFogMode
    """Linear falloff."""
    kFBFogModeSquareExponential:FBFogMode
    """Squared exponential falloff."""
class FBGapMode(_Enum):
    """Gap interpolation modes."""
    kFBGapBezier:FBGapMode
    """Bezier interpolation."""
    kFBGapConstant:FBGapMode
    """Constant interpolation."""
    kFBGapCurve:FBGapMode
    """Cubic/curve interpolation."""
    kFBGapLinear:FBGapMode
    """Linear interpolation."""
    kFBGapRigidBody:FBGapMode
    """Use rigid body information."""
    kFBGapSample:FBGapMode
    """Sampled data."""
class FBGenerationMode(_Enum):
    """Generation modes for optical model."""
    kFBGenerationFast:FBGenerationMode
    """Fast re-generation."""
    kFBGenerationNone:FBGenerationMode
    """No re-generation."""
class FBGeometryArrayElementType(_Enum):
    """Type of data when requesting an array."""
    kFBGeometryArrayElementType_Float:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Float2:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Float3:FBGeometryArrayElementType
    """Each element is an array of 3 float."""
    kFBGeometryArrayElementType_Float4:FBGeometryArrayElementType
    """Each element is an array of 4 float."""
    kFBGeometryArrayElementType_FloatMatrix4x4:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Integer:FBGeometryArrayElementType
    kFBGeometryArrayElementType_IntegerArrayPointer:FBGeometryArrayElementType
    kFBGeometryArrayElementType_Unknown:FBGeometryArrayElementType
class FBGeometryArrayID(_Enum):
    """ID to use when requesting a specific array of data for a model.
    See sample: VertexArrayManipulation.py."""
    kFBGeometryArrayID_Binormal:FBGeometryArrayID
    """ID to the Binormal array."""
    kFBGeometryArrayID_Color:FBGeometryArrayID
    """ID to the Vertex Color Array."""
    kFBGeometryArrayID_Normal:FBGeometryArrayID
    """ID to the Normal by Point array."""
    kFBGeometryArrayID_Point:FBGeometryArrayID
    """ID to the Point array."""
    kFBGeometryArrayID_Tangent:FBGeometryArrayID
    """ID to the Tangent array."""
class FBGeometryMappingMode(_Enum):
    """Determine how the element is mapped on a surface.
    kFBGeometryMapping_NONE The mapping is undetermined.kFBGeometryMapping_BY_CONTROL_POINT There will be one mapping coordinate for each surface control point/vertex.kFBGeometryMapping_BY_POLYGON_VERTEX There will be one mapping coordinate for each vertex, for each polygon/strip it is part of. This means that a vertex will have as many mapping coordinates as polygons it is part of.kFBGeometryMapping_BY_POLYGON There can be only one mapping coordinate for the whole polygon/strip.kFBGeometryMapping_BY_EDGE There will be one mapping coordinate for each unique edge in the mesh. This is meant to be used with smoothing layer elements.kFBGeometryMapping_ALL_SAME There can be only one mapping coordinate for the whole surface."""
    kFBGeometryMapping_ALL_SAME:FBGeometryMappingMode
    kFBGeometryMapping_BY_CONTROL_POINT:FBGeometryMappingMode
    kFBGeometryMapping_BY_EDGE:FBGeometryMappingMode
    kFBGeometryMapping_BY_POLYGON:FBGeometryMappingMode
    kFBGeometryMapping_BY_POLYGON_VERTEX:FBGeometryMappingMode
    kFBGeometryMapping_NONE:FBGeometryMappingMode
class FBGeometryPrimitiveType(_Enum):
    kFBGeometry_LINES:FBGeometryPrimitiveType
    kFBGeometry_LINE_LOOP:FBGeometryPrimitiveType
    kFBGeometry_LINE_STRIP:FBGeometryPrimitiveType
    kFBGeometry_POINTS:FBGeometryPrimitiveType
    kFBGeometry_POLYGON:FBGeometryPrimitiveType
    kFBGeometry_QUADS:FBGeometryPrimitiveType
    kFBGeometry_QUADS_STRIP:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLES:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLE_FAN:FBGeometryPrimitiveType
    kFBGeometry_TRIANGLE_STRIP:FBGeometryPrimitiveType
class FBGeometryReferenceMode(_Enum):
    """Determine how the mapping information is stored in the array of coordinate.
    kFBGeometryReference_DIRECT This indicates that the mapping information for the n'th element is found in the n'th place of DirectArray.kFBGeometryReference_INDEX, This indicates that the mapping information for the n'th element is found in the n'th place of IndexArray.kFBGeometryReference_INDEX_TO_DIRECT This indicates that the KLayerElementTemplate::mIndexArray contains, for the n'th element, an index in the KLayerElementTemplate::mDirectArray array of mapping elements. eINDEX_TO_DIRECT is usually useful to store coordinates for eBY_POLYGON_VERTEX mapping mode elements. Since the same coordinates are usually repeated a large number of times, it saves spaces to store the coordinate only one time and refer to them with an index. Materials and Textures are also referenced with this mode and the actual Material/Texture can be accessed via the KLayerElementTemplate::mDirectArray"""
    kFBGeometryReference_DIRECT:FBGeometryReferenceMode
    kFBGeometryReference_INDEX:FBGeometryReferenceMode
    kFBGeometryReference_INDEX_TO_DIRECT:FBGeometryReferenceMode
class FBGlobalEvalCallbackTiming(_Enum):
    """Global Evaluation callback timing.
    Let the user to register callback function at different stage of background evaluation."""
    kFBGlobalEvalCallbackAfterDAG:FBGlobalEvalCallbackTiming
    """Invoked after all DAG (Transformation & Deformation) evaluation tasks finished in evaluation pipeline / thread."""
    kFBGlobalEvalCallbackAfterDeform:FBGlobalEvalCallbackTiming
    """Invoked after all deformation tasks finished in evaluation pipeline / thread."""
    kFBGlobalEvalCallbackAfterPlottingFrame:FBGlobalEvalCallbackTiming
    """Invoked after plotting a frame."""
    kFBGlobalEvalCallbackAfterRender:FBGlobalEvalCallbackTiming
    """Invoked in rendering pipeline, after any rendering tasks finish (just before swapping GL back/front buffer)."""
    kFBGlobalEvalCallbackBeforeDAG:FBGlobalEvalCallbackTiming
    """Invoked before any DAG (Transformation & Deformation) evaluation tasks started in evaluation pipeline / thread."""
    kFBGlobalEvalCallbackBeforePlottingFrame:FBGlobalEvalCallbackTiming
    """Invoked before plotting a frame."""
    kFBGlobalEvalCallbackBeforeRender:FBGlobalEvalCallbackTiming
    """Invoked in rendering pipeline, before any rendering tasks start (immediately after clearing GL back buffer)."""
    kFBGlobalEvalCallbackSyn:FBGlobalEvalCallbackTiming
    """Invoked when both evaluation & rendering pipelines / threads are stopped. Useful for some complicated scene change tasks to avoid race condition."""
class FBHUDElementHAlignment(_Enum):
    kFBHUDCenter:FBHUDElementHAlignment
    """Center."""
    kFBHUDLeft:FBHUDElementHAlignment
    """Left alignment."""
    kFBHUDRight:FBHUDElementHAlignment
    """Right alignment."""
class FBHUDElementVAlignment(_Enum):
    kFBHUDBottom:FBHUDElementVAlignment
    """Bottom alignment."""
    kFBHUDTop:FBHUDElementVAlignment
    """Top alignment."""
    kFBHUDVCenter:FBHUDElementVAlignment
    """Center."""
class FBIconPosition(_Enum):
    """Different icon positions possible."""
    kFBIconLeft:FBIconPosition
    """Icon on left of text."""
    kFBIconTop:FBIconPosition
    """Icon on top of text."""
class FBImageFormat(_Enum):
    """Image formats."""
    kFBImageFormatABGR32:FBImageFormat
    kFBImageFormatARGB32:FBImageFormat
    kFBImageFormatBGR16:FBImageFormat
    kFBImageFormatBGR24:FBImageFormat
    kFBImageFormatBGRA32:FBImageFormat
    kFBImageFormatRGB24:FBImageFormat
    kFBImageFormatRGBA32:FBImageFormat
    kFBImageFormatUnknown:FBImageFormat
class FBImageInterleaveType(_Enum):
    """Image field interleave types."""
    kFBImageInterleaveTypeAverage:FBImageInterleaveType
    kFBImageInterleaveTypeEven:FBImageInterleaveType
    kFBImageInterleaveTypeFullFrame:FBImageInterleaveType
    kFBImageInterleaveTypeOdd:FBImageInterleaveType
class FBImageInterpolationType(_Enum):
    """Image interpolation types."""
    kFBImageInterpolationTypeDuplicate:FBImageInterpolationType
    kFBImageInterpolationTypeLinear:FBImageInterpolationType
    kFBImageInterpolationTypeNone:FBImageInterpolationType
class FBImageType(_Enum):
    """Image types."""
    kFBImageTypeField:FBImageType
    kFBImageTypeFrame:FBImageType
class FBInputKey(_Enum):
    """Keyboard inputs."""
    kFBKeyBackSpace:FBInputKey
    """Backspace."""
    kFBKeyDel:FBInputKey
    """Delete."""
    kFBKeyDown:FBInputKey
    """Down."""
    kFBKeyEnd:FBInputKey
    """End."""
    kFBKeyEscape:FBInputKey
    """Escape."""
    kFBKeyF1:FBInputKey
    """F1."""
    kFBKeyF10:FBInputKey
    """F10."""
    kFBKeyF11:FBInputKey
    """F11."""
    kFBKeyF12:FBInputKey
    """F12."""
    kFBKeyF2:FBInputKey
    """F2."""
    kFBKeyF3:FBInputKey
    """F3."""
    kFBKeyF4:FBInputKey
    """F4."""
    kFBKeyF5:FBInputKey
    """F5."""
    kFBKeyF6:FBInputKey
    """F6."""
    kFBKeyF7:FBInputKey
    """F7."""
    kFBKeyF8:FBInputKey
    """F8."""
    kFBKeyF9:FBInputKey
    """F9."""
    kFBKeyHome:FBInputKey
    """Home."""
    kFBKeyIns:FBInputKey
    """Insert."""
    kFBKeyLeft:FBInputKey
    """Left."""
    kFBKeyPageDown:FBInputKey
    """Page Down."""
    kFBKeyPageUp:FBInputKey
    """Page Up."""
    kFBKeyReturn:FBInputKey
    """Return."""
    kFBKeyRight:FBInputKey
    """Right."""
    kFBKeyTab:FBInputKey
    """Tab."""
    kFBKeyUp:FBInputKey
    """Up."""
class FBInputModifier(_Enum):
    """Input Modifiers (Ctrl, Alt, Shift)."""
    kFBKeyAlt:FBInputModifier
    """Alt was pressed."""
    kFBKeyCtrl:FBInputModifier
    """Control was pressed."""
    kFBKeyNone:FBInputModifier
    """No modifier."""
    kFBKeyShift:FBInputModifier
    """Shift was pressed."""
class FBInputType(_Enum):
    """Types of input events.
    See sample: KeyboardMapper.py."""
    kFBButtonDoubleClick:FBInputType
    """A mouse button was double clicked."""
    kFBButtonPress:FBInputType
    """A mouse button was pressed."""
    kFBButtonRelease:FBInputType
    """A mouse button was released."""
    kFBDragging:FBInputType
    """The mouse is dragging items."""
    kFBDropping:FBInputType
    """The mouse is dropping items."""
    kFBKeyPress:FBInputType
    """A keyboard key was pressed."""
    kFBKeyPressRaw:FBInputType
    """A keyboard key was pressed."""
    kFBKeyRelease:FBInputType
    """A keyboard key was released."""
    kFBKeyReleaseRaw:FBInputType
    """A keyboard key was released."""
    kFBMotionNotify:FBInputType
    """The mouse has been moved."""
    kFBMouseEnter:FBInputType
    """The mouse pointer is entering the window."""
    kFBMouseLeave:FBInputType
    """The mouse pointer is leaving the window."""
    kFBMouseWheelNotify:FBInputType
    """The mouse wheel has moved."""
    kFBUnknownInput:FBInputType
    """The internal event could not be translated."""
class FBInsertSegmentMode(_Enum):
    """Insert segment modes."""
    kFBInsertSegmentFromStart:FBInsertSegmentMode
    """Insert from start."""
    kFBInsertSegmentToEnd:FBInsertSegmentMode
    """Insert to end."""
    kFBInsertSegmentWhole:FBInsertSegmentMode
    """Insert whole."""
class FBInterpolation(_Enum):
    """Types of interpolation for an FCurve."""
    kFBInterpolationConstant:FBInterpolation
    """Constant interpolation."""
    kFBInterpolationCubic:FBInterpolation
    """Cubic interpolation."""
    kFBInterpolationCustom:FBInterpolation
    """Custom interpolation."""
    kFBInterpolationLinear:FBInterpolation
    """Linear interpolation."""
class FBInterpolatorCurveType(_Enum):
    """Types of interpolator for an FCurve."""
    kFBInterpolatorCurveFastIn:FBInterpolatorCurveType
    kFBInterpolatorCurveFastOut:FBInterpolatorCurveType
    kFBInterpolatorCurveLast:FBInterpolatorCurveType
    kFBInterpolatorCurveLinearIn:FBInterpolatorCurveType
    kFBInterpolatorCurveLinearOut:FBInterpolatorCurveType
    kFBInterpolatorCurveSlowIn:FBInterpolatorCurveType
    kFBInterpolatorCurveSlowOut:FBInterpolatorCurveType
    kFBInterpolatorCurveSmoothIn:FBInterpolatorCurveType
    kFBInterpolatorCurveSmoothOut:FBInterpolatorCurveType
class FBKeyingGroupType(_Enum):
    """Keying group types."""
    kFBKeyingGroupGlobal:FBKeyingGroupType
    """All selected objects with the same properties as those defined in the keying group will be keyed."""
    kFBKeyingGroupLocal:FBKeyingGroupType
    """Only properties of objects specified in the keying group will be keyed."""
    kFBKeyingGroupObjectType:FBKeyingGroupType
    """All selected objects of the specified type in the keying group with the same properties as those defined in the keying group will be keyed."""
class FBLayerMode(_Enum):
    """Layer mode."""
    kFBLayerModeAdditive:FBLayerMode
    """Layer value will be added to the other layers to computed the final value."""
    kFBLayerModeInvalidIndex:FBLayerMode
    """Invalid value."""
    kFBLayerModeOverride:FBLayerMode
    """Layer value will override the value of the other precedent layers."""
    kFBLayerModeOverridePassthrough:FBLayerMode
    """If the layer has a weight of 75%, the precedent layers will have a combined effect of 25% on the final value. Setting the weight to 100% is similar to setting the layer in override."""
class FBLayerRotationMode(_Enum):
    """Rotation mode for layer."""
    kFBLayerRotationModeEulerRotation:FBLayerRotationMode
    """The rotation will be computed component by component."""
    kFBLayerRotationModeInvalidIndex:FBLayerRotationMode
    """Invalid value."""
    kFBLayerRotationModeQuaternionRotation:FBLayerRotationMode
    """The rotation will be computed using quaternion."""
class FBLightType(_Enum):
    """Light types."""
    kFBLightTypeArea:FBLightType
    """Area light."""
    kFBLightTypeInfinite:FBLightType
    """Infinite light (plane)."""
    kFBLightTypePoint:FBLightType
    """Point light."""
    kFBLightTypeSpot:FBLightType
    """Spot light."""
class FBListStyle(_Enum):
    """List style or direction.
    See samples: List.py, ToolCommunicationReceiver.py."""
    kFBDropDownList:FBListStyle
    """Drop down list."""
    kFBVerticalList:FBListStyle
    """Vertical list."""
class FBManipulatorPickType(_Enum):
    """Types of manipulator picking."""
    FBPickObjects:FBManipulatorPickType
    """Pick objects."""
    FBPickPoints:FBManipulatorPickType
    """Pick points."""
    FBPickSurfaces:FBManipulatorPickType
    """Pick surfaces."""
class FBManipulatorTransformType(_Enum):
    """Manipulator transform stles."""
    kFBManipulatorTransformNone:FBManipulatorTransformType
    """No manipulator."""
    kFBManipulatorTransformRotation:FBManipulatorTransformType
    """Rotation manipulator."""
    kFBManipulatorTransformScaling:FBManipulatorTransformType
    """Scaling manipulator."""
    kFBManipulatorTransformTranslation:FBManipulatorTransformType
    """Translation manipulator."""
class FBMarkerLook(_Enum):
    """Look of the marker."""
    kFBMarkerLookAimRollGoal:FBMarkerLook
    """Aim & Roll goal."""
    kFBMarkerLookBone:FBMarkerLook
    """Bone."""
    kFBMarkerLookBox:FBMarkerLook
    """Box."""
    kFBMarkerLookCapsule:FBMarkerLook
    """Capsule."""
    kFBMarkerLookCircle:FBMarkerLook
    """Circle."""
    kFBMarkerLookCube:FBMarkerLook
    """Cube."""
    kFBMarkerLookHardCross:FBMarkerLook
    """Thick cross."""
    kFBMarkerLookLightCross:FBMarkerLook
    """Wireframe cross."""
    kFBMarkerLookNone:FBMarkerLook
    """None."""
    kFBMarkerLookRigidGoal:FBMarkerLook
    """Rigid goal."""
    kFBMarkerLookRotationGoal:FBMarkerLook
    """Rotation goal."""
    kFBMarkerLookSphere:FBMarkerLook
    """Sphere."""
    kFBMarkerLookSquare:FBMarkerLook
    """Square."""
    kFBMarkerLookStick:FBMarkerLook
    """Box with a sphere on one end."""
class FBMarkerResolutionLevel(_Enum):
    """Resolution of marker mesh sphere and capsule (Quality)."""
    kFBMarkerHighResolution:FBMarkerResolutionLevel
    """Highest resolution."""
    kFBMarkerLowResolution:FBMarkerResolutionLevel
    """Lowest resolution."""
    kFBMarkerMediumResolution:FBMarkerResolutionLevel
    """Medium resolution."""
class FBMarkerType(_Enum):
    """Type of the marker."""
    kFBMarkerTypeFKEffector:FBMarkerType
    """FK effector."""
    kFBMarkerTypeIKEffector:FBMarkerType
    """IK effector."""
    kFBMarkerTypeOptical:FBMarkerType
    """Optical."""
    kFBMarkerTypeStandard:FBMarkerType
    """Standard."""
class FBMaterialTextureType(_Enum):
    """Various Material texture channels' type.
    See samples: LayeredTexture.py, MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py."""
    kFBMaterialTextureAmbient:FBMaterialTextureType
    kFBMaterialTextureAmbientFactor:FBMaterialTextureType
    kFBMaterialTextureBump:FBMaterialTextureType
    kFBMaterialTextureDiffuse:FBMaterialTextureType
    kFBMaterialTextureDiffuseFactor:FBMaterialTextureType
    kFBMaterialTextureEmissive:FBMaterialTextureType
    kFBMaterialTextureEmissiveFactor:FBMaterialTextureType
    kFBMaterialTextureNormalMap:FBMaterialTextureType
    kFBMaterialTextureReflection:FBMaterialTextureType
    kFBMaterialTextureReflectionFactor:FBMaterialTextureType
    kFBMaterialTextureShiness:FBMaterialTextureType
    kFBMaterialTextureSpecular:FBMaterialTextureType
    kFBMaterialTextureSpecularFactor:FBMaterialTextureType
    kFBMaterialTextureTransparent:FBMaterialTextureType
    kFBMaterialTextureTransparentFactor:FBMaterialTextureType
class FBMenuItemType(_Enum):
    """Types of menu items available."""
    kFBMenuItemMotionExport:FBMenuItemType
    """Motion Files->Export."""
    kFBMenuItemMotionImport:FBMenuItemType
    """Motion Files->Import."""
    kFBMenuItemSceneExport:FBMenuItemType
    """Scenes->Export."""
    kFBMenuItemSceneImport:FBMenuItemType
    """Scenes->Import."""
class FBMergeLayerMode(_Enum):
    """Merge layer mode for animation layers.
    This will specify the mode of the resulting merged layer, if applicable (To BaseAnimation layer mode cannot be modified)."""
    kFBMergeLayerModeAdditive:FBMergeLayerMode
    """The resulting layer will be in additive mode, if possible."""
    kFBMergeLayerModeAutomatic:FBMergeLayerMode
    """The resulting layer will be in override mode if one of the source layer is in override, otherwise, it will be in additive mode."""
    kFBMergeLayerModeOverride:FBMergeLayerMode
    """The resulting layer will be in override mode, if possible."""
class FBMirrorPlaneType(_Enum):
    """Mirror Plane Type."""
    kFBMirrorPlaneTypeAuto:FBMirrorPlaneType
    kFBMirrorPlaneTypeCount:FBMirrorPlaneType
    kFBMirrorPlaneTypeEquation:FBMirrorPlaneType
    kFBMirrorPlaneTypeInvalid:FBMirrorPlaneType
    kFBMirrorPlaneTypeUser:FBMirrorPlaneType
    kFBMirrorPlaneTypeXY:FBMirrorPlaneType
    kFBMirrorPlaneTypeXZ:FBMirrorPlaneType
    kFBMirrorPlaneTypeZY:FBMirrorPlaneType
class FBModelCullingMode(_Enum):
    """Model Culling Mode."""
    kFBCullingOff:FBModelCullingMode
    """Culling Off."""
    kFBCullingOnCCW:FBModelCullingMode
    """Culling with Counter Clock Wise."""
    kFBCullingOnCW:FBModelCullingMode
    """Culling with Clock Wise."""
class FBModelEvaluationTaskType(_Enum):
    kFBModelEvaluationBBox:FBModelEvaluationTaskType
    """Model's bouding box computation task (approximately for deformable model)"""
    kFBModelEvaluationDeform:FBModelEvaluationTaskType
    """Model's deformation task (for deformable model)"""
    kFBModelEvaluationTransform:FBModelEvaluationTaskType
    """Model's transformation evaluation task (Global )"""
class FBModelHiercharyTraverserType(_Enum):
    """Types of hierarchy traverser search type."""
    kModelTraverserBreadthFirst:FBModelHiercharyTraverserType
    """Breadth-first search."""
    kModelTraverserDepthFirst:FBModelHiercharyTraverserType
    """Depth-first search."""
class FBModelRotationOrder(_Enum):
    """Ways to apply Rotation."""
    kFBEulerXYZ:FBModelRotationOrder
    """XYZ Euler Order."""
    kFBEulerXZY:FBModelRotationOrder
    """XZY Euler Order."""
    kFBEulerYXZ:FBModelRotationOrder
    """YXZ Euler Order."""
    kFBEulerYZX:FBModelRotationOrder
    """YZX Euler Order."""
    kFBEulerZXY:FBModelRotationOrder
    """ZXY Euler Order."""
    kFBEulerZYX:FBModelRotationOrder
    """ZYX Euler Order."""
    kFBSphericXYZ:FBModelRotationOrder
    """Spheric XYZ Order."""
class FBModelSelection(_Enum):
    """Different model selection available."""
    kFBAllModels:FBModelSelection
    """Will imports motion into the hierarchies of all models in your scene. This is the only merge option when nothing is selected."""
    kFBCreateModels:FBModelSelection
    """Will create the models in the motion file, used when there is no model to match in the scene."""
    kFBInHierarchy:FBModelSelection
    """Will find the root node and will try to merge the data on the hierarchy, only useful if one model is selected."""
    kFBNone:FBModelSelection
    """No selection mode specified."""
    kFBPrefixGroupContainingModel:FBModelSelection
    """Will finds the top node with the same prefix and imports the motion as if you selected kFBInHierarchy. If the selected node has the prefix, this merge option is the same as selecting kFBSelectedModelAndChildren. If no nodes are found with the prefix, this merge option operates the same as kFBSelectedModels. Only available when one model is selected."""
    kFBSelectedModelAndChildren:FBModelSelection
    """Will try to match the models from the file to those selected in the scene, as well as the children of the selected models."""
    kFBSelectedModels:FBModelSelection
    """Will Merges data with only the selected nodes or models."""
class FBModelShadingMode(_Enum):
    """Modes for model shading.
    See samples: FBModelCube.py, GeometryInstancing.py, VertexArrayManipulation.py, VertexColor.py."""
    kFBModelShadingAll:FBModelShadingMode
    """Lighted, shaded, textured shading."""
    kFBModelShadingDefault:FBModelShadingMode
    """Default shading."""
    kFBModelShadingFlat:FBModelShadingMode
    """Flat shading."""
    kFBModelShadingHard:FBModelShadingMode
    """Hard shading."""
    kFBModelShadingLight:FBModelShadingMode
    """Lighted shading."""
    kFBModelShadingTexture:FBModelShadingMode
    """Textured shading."""
    kFBModelShadingWire:FBModelShadingMode
    """Wireframe shading."""
class FBModelTemplateStyle(_Enum):
    """Model template styles When creating model templates, this parameter will affect the actual model created (associated with the model template)."""
    kFBModelTemplateCamera:FBModelTemplateStyle
    """Camera."""
    kFBModelTemplateCameraInterest:FBModelTemplateStyle
    """Camera interest."""
    kFBModelTemplateGeometry:FBModelTemplateStyle
    """Generic geometry."""
    kFBModelTemplateLight:FBModelTemplateStyle
    """Light."""
    kFBModelTemplateMarker:FBModelTemplateStyle
    """Marker."""
    kFBModelTemplateNone:FBModelTemplateStyle
    """No style."""
    kFBModelTemplateNull:FBModelTemplateStyle
    """Null."""
    kFBModelTemplateOptical:FBModelTemplateStyle
    """Optical model (not supported yet)."""
    kFBModelTemplateRoot:FBModelTemplateStyle
    """Root (3 axes)."""
    kFBModelTemplateSensor:FBModelTemplateStyle
    """Yellow magnetic sensor."""
    kFBModelTemplateSkeleton:FBModelTemplateStyle
    """Skeleton limb."""
class FBModelTransformationType(_Enum):
    """Types of transformation vector/matrices possible.
    See samples: FBModelCube.py, GeometryInstancing.py, VertexArrayManipulation.py."""
    kModelInverse_Rotation:FBModelTransformationType
    """Inverse rotation."""
    kModelInverse_Scaling:FBModelTransformationType
    """Inverse scaling."""
    kModelInverse_Transformation:FBModelTransformationType
    """Inverse transformation."""
    kModelInverse_Transformation_Geometry:FBModelTransformationType
    """Inverse of transformation plus geometry offset."""
    kModelInverse_Translation:FBModelTransformationType
    """Inverse translation."""
    kModelRotation:FBModelTransformationType
    """Rotation."""
    kModelScaling:FBModelTransformationType
    """Scaling."""
    kModelTransformation:FBModelTransformationType
    """Transformation."""
    kModelTransformation_Geometry:FBModelTransformationType
    """Transformation plus geometry offset"""
    kModelTranslation:FBModelTransformationType
    """Translation."""
class FBNamespaceAction(_Enum):
    """Namespace flags.
    See samples: FBGetSelectedModels.py, FBGroup.py."""
    kFBConcatNamespace:FBNamespaceAction
    """Use to add a namespace name to object."""
    kFBRemoveAllNamespace:FBNamespaceAction
    """Remove all the namespace name."""
    kFBReplaceNamespace:FBNamespaceAction
    """Use to replace a define namespace."""
class FBNewKeyInterpolationType(_Enum):
    """Key Interpolation Type to use when creating new keys."""
    kFBNewKeyInterpolation_Auto:FBNewKeyInterpolationType
    """Auto interpolation type."""
    kFBNewKeyInterpolation_Custom0:FBNewKeyInterpolationType
    """Custom 0 interpolation type."""
    kFBNewKeyInterpolation_Custom1:FBNewKeyInterpolationType
    """Custom 1 interpolation type."""
    kFBNewKeyInterpolation_Custom2:FBNewKeyInterpolationType
    """Custom 2 interpolation type."""
    kFBNewKeyInterpolation_Fixed:FBNewKeyInterpolationType
    """Fixed interpolation type."""
    kFBNewKeyInterpolation_Linear:FBNewKeyInterpolationType
    """Linear interpolation type."""
    kFBNewKeyInterpolation_None:FBNewKeyInterpolationType
    """Invalid interpolation type, could be returned by the system if it is in an uninitialized state. Don't use this mode."""
    kFBNewKeyInterpolation_Smooth:FBNewKeyInterpolationType
    """Smooth interpolation type."""
    kFBNewKeyInterpolation_SmoothClamp:FBNewKeyInterpolationType
    """Smooth Clamp interpolation type."""
    kFBNewKeyInterpolation_Spline:FBNewKeyInterpolationType
    """Spline interpolation type."""
    kFBNewKeyInterpolation_SplineClamp:FBNewKeyInterpolationType
    """Spline Clamp interpolation type."""
    kFBNewKeyInterpolation_Step:FBNewKeyInterpolationType
    """Step interpolation type."""
    kFBNewKeyInterpolation_TCB:FBNewKeyInterpolationType
    """TCB interpolation type."""
class FBNurbType(_Enum):
    """Surface types."""
    kFBNurbTypeClosed:FBNurbType
    """Closed Type Nurb."""
    kFBNurbTypeOpen:FBNurbType
    """Open Type Nurb."""
    kFBNurbTypePeriodic:FBNurbType
    """Periodic Type Nurb."""
class FBObjectFlag(_Enum):
    """Available flags for any component."""
    kFBFlagAllocated:FBObjectFlag
    """Object is allocated, so it must call 'delete this' on destroy."""
    kFBFlagBrowsable:FBObjectFlag
    """Visible in the Scene Navigator/Schematic View/Property View/Model View. If disabled, the object representation in the navigator will not be visible. In the Schematic View, system object are not shown and other objects will still be visible, but a red X will be drawn on them. It is not possible to select the object in the Schematic View. After disabling that flag of a selected object, it will still be selected to allow a script based on selection to work. It will then be possible for a user to deselect the object, but it will not be possible to select it."""
    kFBFlagClonable:FBObjectFlag
    """Can be cloned. If disabled, the 'Duplicate' option will be removed in the contextual menu."""
    kFBFlagDeletable:FBObjectFlag
    """Can be deleted."""
    kFBFlagDetachable:FBObjectFlag
    """Object can be 'detached'. Used by the apply manager contextual menu."""
    kFBFlagKeyable:FBObjectFlag
    """Object can Key his property. (System Camera can't)"""
    kFBFlagMergeable:FBObjectFlag
    """Can be merged."""
    kFBFlagNamespaceEditable:FBObjectFlag
    """Allow editing on the namespace objects. If disabled, the 'Add/Remove Namespace...' option is removed from the contextual menu."""
    kFBFlagNewable:FBObjectFlag
    """Deleted on File->New."""
    kFBFlagParentable:FBObjectFlag
    """Object (model) can be 'parented'. Used by the apply manager contextual menu."""
    kFBFlagRenamable:FBObjectFlag
    """Can be renamed."""
    kFBFlagSavable:FBObjectFlag
    """Can be saved."""
    kFBFlagSelectable:FBObjectFlag
    """Can be selected. If disabled, representation of the object, like in the navigator, can still be selected and can still affect the original object."""
    kFBFlagStorable6:FBObjectFlag
    """System/Obsolete."""
    kFBFlagStorableData6:FBObjectFlag
    """System/Obsolete."""
    kFBFlagStory:FBObjectFlag
    """Object created/used by the Story tool. Useful flag for filtering Story objects."""
    kFBFlagSystem:FBObjectFlag
    """Created from System (not from user)"""
    kFBFlagUndoable:FBObjectFlag
    """Object can undo its actions and states, in a global Undo Stack."""
    kFBFlagUndoableSeparately:FBObjectFlag
    """Object which has kFlagUndoableSeparately flag turned on will have a separate Undo Stack."""
    kFBFlagUniqueName:FBObjectFlag
    """< Used in FBX SDK native IO, force bindary format for the bindary data."""
    kFBFlagVisible:FBObjectFlag
    """Can be visible. If disabled, the object will still be available in the navigator, it is only hidden in the viewer."""
class FBObjectPoseMirrorOptionsFlag(_Enum):
    """ObjectPoseMirrorOptions flags."""
    kFBObjectPoseMirrorOptionsNoFlag:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocal:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalMirrorParent:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalRef:FBObjectPoseMirrorOptionsFlag
    kFBObjectPoseMirrorOptionsUpdateLocalRefMirrorRef:FBObjectPoseMirrorOptionsFlag
class FBObjectPoseOptionsFlag(_Enum):
    """ObjectPoseOptions flags."""
    kFBObjectPoseOptionsNoFlag:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsRotation:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsScaling:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationX:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationY:FBObjectPoseOptionsFlag
    kFBObjectPoseOptionsTranslationZ:FBObjectPoseOptionsFlag
class FBObjectStatus(_Enum):
    """Available lifetime status for any component."""
    kFBStatusClearing:FBObjectStatus
    """Object is in clearing operations (File new)."""
    kFBStatusCreating:FBObjectStatus
    """Object is in creation operations."""
    kFBStatusDestroying:FBObjectStatus
    """Object is in destruction operations."""
    kFBStatusMerging:FBObjectStatus
    """Object is in Merging operations."""
    kFBStatusRetrieving:FBObjectStatus
    """Object is in retrieving operations."""
    kFBStatusStoring:FBObjectStatus
    """Object is in storing operations."""
class FBOneClickApplication(_Enum):
    """Possible application for One-Click interop with MotionBuilder."""
    kFBOneClick3dsMax:FBOneClickApplication
    """3ds Max."""
    kFBOneClickMaya:FBOneClickApplication
    """Maya."""
    kFBOneClickNone:FBOneClickApplication
    """No application."""
    kFBOneClickSoftimage:FBOneClickApplication
    """Softimage."""
class FBOrientation(_Enum):
    """General directions for UI components. DEPRICATED use ParallelEvaluation on FBEvaluateManager insteadAvailable DAG parallel schedule algorithm
    See samples: Container.py, Slider.py."""
    kFBHorizontal:FBOrientation
    """Horizontal."""
    kFBVertical:FBOrientation
    """Vertical"""
class FBParallelScheduleType(_Enum):
    kFBParallelScheduleAdvanced:FBParallelScheduleType
    """Advanced parallel schedule, task dependency analyzation will be able to across ative constraint, and plus motion hierarchy."""
    kFBParallelScheduleSerial:FBParallelScheduleType
    """No parallel schedule, use sequential evaluation order instead."""
    kFBParallelScheduleSimple:FBParallelScheduleType
    """Simple parallel schedule, mainly analyze the task dependency based on Motion Hierarchy (scene graph), but don't across active constraint."""
class FBParity(_Enum):
    """Parity modes."""
    kFBParityEven:FBParity
    """Even parity."""
    kFBParityNone:FBParity
    """No parity."""
    kFBParityOdd:FBParity
    """Odd parity."""
class FBPickingMode(_Enum):
    """3D picking mode."""
    kFBPickingModeCount:FBPickingMode
    """End of enum, this valued indicates the number of picking modes available."""
    kFBPickingModeModelsOnly:FBPickingMode
    """Models-only mode (no nulls or skeletons are displayed)."""
    kFBPickingModeStandard:FBPickingMode
    """Standard picking mode."""
    kFBPickingModeXRay:FBPickingMode
    """X-Ray picking mode (obstructed models are displayed in overlay)."""
class FBPlayMode(_Enum):
    """Play modes."""
    kFBPlayModeLoop:FBPlayMode
    """Loop clip."""
    kFBPlayModeNoPlay:FBPlayMode
    """No play (most common)."""
    kFBPlayModePlay:FBPlayMode
    """Play clip."""
    kFBPlayModePlayToEnd:FBPlayMode
    """Play clip to end."""
    kFBPlayModePreviewToEnd:FBPlayMode
    """Preview clip until end."""
class FBPlayerControlChangeType(_Enum):
    """Types of player control change events."""
    kFBPlayerControlGoto:FBPlayerControlChangeType
    """Goto."""
    kFBPlayerControlNone:FBPlayerControlChangeType
    """None."""
    kFBPlayerControlPlay:FBPlayerControlChangeType
    """Play."""
    kFBPlayerControlPlayReverse:FBPlayerControlChangeType
    """Play reverse."""
    kFBPlayerControlRecordModeOff:FBPlayerControlChangeType
    """Record mode off."""
    kFBPlayerControlRecordModeOn:FBPlayerControlChangeType
    """Record mode on."""
    kFBPlayerControlStepBackward:FBPlayerControlChangeType
    """Step backward."""
    kFBPlayerControlStepForward:FBPlayerControlChangeType
    """Step forward."""
    kFBPlayerControlStop:FBPlayerControlChangeType
    """Stop."""
class FBPlotAllowed(_Enum):
    """FBPlotAllowed"""
    kFBPlotAllowed_Both:FBPlotAllowed
    kFBPlotAllowed_ControlRig:FBPlotAllowed
    kFBPlotAllowed_None:FBPlotAllowed
    kFBPlotAllowed_Skeleton:FBPlotAllowed
class FBPlotTangentMode(_Enum):
    """The tangent mode for plotted curve."""
    kFBPlotTangentModeAuto:FBPlotTangentMode
    kFBPlotTangentModeSmooth:FBPlotTangentMode
    kFBPlotTangentModeSmoothClamp:FBPlotTangentMode
    kFBPlotTangentModeSpline:FBPlotTangentMode
    kFBPlotTangentModeSplineClamp:FBPlotTangentMode
class FBPlugModificationFlag(_Enum):
    kFBAllConnectionModified:FBPlugModificationFlag
    kFBAllCustomPropertyModified:FBPlugModificationFlag
    kFBAllDataModified:FBPlugModificationFlag
    kFBAllKeyingModified:FBPlugModificationFlag
    kFBAllModifiedMask:FBPlugModificationFlag
    kFBAllStateModified:FBPlugModificationFlag
    kFBContentAllModifiedMask:FBPlugModificationFlag
    kFBContentConnectionModified:FBPlugModificationFlag
    """Owner object/namespace has connection modified property/objects."""
    kFBContentCustomPropertyModified:FBPlugModificationFlag
    """Owner object/Namespace has dirty property/objects."""
    kFBContentDataModified:FBPlugModificationFlag
    """Owner object/Namespace has data dirty property/objects."""
    kFBContentKeyingModified:FBPlugModificationFlag
    """Owner object/Namespace has data dirty property/objects."""
    kFBContentStateModified:FBPlugModificationFlag
    """Owner object/Namespace has state dirty property/objects."""
    kFBPlugAllContent:FBPlugModificationFlag
    """None Modified."""
    kFBSelfAllModifiedMask:FBPlugModificationFlag
    kFBSelfConnectionDstObjectModified:FBPlugModificationFlag
    """The dst object of this plug has been modified."""
    kFBSelfConnectionDstPropertyModified:FBPlugModificationFlag
    """The dst property of this plug has been modified."""
    kFBSelfConnectionModifiedMask:FBPlugModificationFlag
    kFBSelfConnectionSrcObjectModified:FBPlugModificationFlag
    """The src object of this plug has been modified."""
    kFBSelfConnectionSrcPropertyModified:FBPlugModificationFlag
    """The src property of this plug has been modified."""
    kFBSelfCustomPropertyModified:FBPlugModificationFlag
    """Object custom property change."""
    kFBSelfDataModified:FBPlugModificationFlag
    """Object/Property itself has been dirty, in case of property get dirty, its owner object will be set dirty as well."""
    kFBSelfKeyingModified:FBPlugModificationFlag
    """Object/Property itself has been dirty, in case of property get dirty, its owner object will be set dirty as well."""
    kFBSelfStateModified:FBPlugModificationFlag
    """Object/Property naming change."""
class FBPlugStatusFlag(_Enum):
    kFBOwnedByUndo:FBPlugStatusFlag
    """Plug is owned by undo framework."""
    kFBPlugStatusFlagNone:FBPlugStatusFlag
    """Plug has no status set."""
    kFBStatusMask:FBPlugStatusFlag
class FBPopupInputType(_Enum):
    """User input types for a popup.
    See samples: RePrefixAllMarkers.py, SelectModelsWithNameContainingSubstring.py, FBMessageBoxGetUserValue.py."""
    kFBPopupBool:FBPopupInputType
    """Boolean input."""
    kFBPopupChar:FBPopupInputType
    """Character input."""
    kFBPopupDouble:FBPopupInputType
    """Double input."""
    kFBPopupFloat:FBPopupInputType
    """Float input."""
    kFBPopupInt:FBPopupInputType
    """Integer input."""
    kFBPopupPassword:FBPopupInputType
    """Password input (String with '*'s)."""
    kFBPopupString:FBPopupInputType
    """String input."""
class FBPoseTransformType(_Enum):
    """Transform mode of pose."""
    kFBPoseTransformGlobal:FBPoseTransformType
    kFBPoseTransformInvalid:FBPoseTransformType
    kFBPoseTransformLocal:FBPoseTransformType
    kFBPoseTransformLocalRef:FBPoseTransformType
    kFBPoseTransformTypeCount:FBPoseTransformType
class FBPoseType(_Enum):
    """Types of pose."""
    kFBBindPose:FBPoseType
    """Bind pose."""
    kFBRestPose:FBPoseType
    """Rest pose."""
class FBProfilingMode(_Enum):
    """Available Profiling modes."""
    kFBProfilingModeAllHi:FBProfilingMode
    """Collect profiling for all known tasks . For large scenes there should be an influence on performance."""
    kFBProfilingModeAllLow:FBProfilingMode
    """Collect profiling for all known tasks that doesn't increase remarkably with scene size. For large scenes this will not influence performance."""
    kFBProfilingModeDevices:FBProfilingMode
    """Collect profiling for device Input/Output and Device Evaluation."""
    kFBProfilingModeDisabled:FBProfilingMode
    """All profiling disabled, this include Viewer profiling. For the other modes, when EvaluationDepth is 0, only base information is profiled, such as FPS and evaluation rate."""
    kFBProfilingModeEvaluation:FBProfilingMode
    """Collect profiling for all known evaluation tasks (default mode)."""
    kFBProfilingModeRendering:FBProfilingMode
    """Collect profiling for all known rendering tasks."""
    kFBProfilingModeSDK:FBProfilingMode
    """Collect profiling for SDK."""
class FBPropertyComponents(_Enum):
    """Property Components Bit Field (XYZ, RGB, RGBA, UV, XYZW, etc.)."""
    kFBPropertyComponent0:FBPropertyComponents
    """First component (e.g.: X, Red, etc.)."""
    kFBPropertyComponent1:FBPropertyComponents
    """Second component (e.g.: Y, Green, etc.)."""
    kFBPropertyComponent2:FBPropertyComponents
    """Third component (e.g.: Z, Blue, etc.)."""
    kFBPropertyComponent3:FBPropertyComponents
    """Fourth component (e.g.: W, Alpha, etc.)."""
    kFBPropertyComponentAll:FBPropertyComponents
    """All components."""
class FBPropertyFlag(_Enum):
    """Available flags for FBProperty objects.PropertyList: Actor.
    Property flags are not saved into FBX files. See sample: PropertyDrop.py. These classes are under development and may change dramatically between versions."""
    kFBDrivenSetByMain:FBPropertyFlag
    """Driven property can be modified, valid only when the main property is modified."""
    kFBDynamicHidden:FBPropertyFlag
    """This flag is used to show/hide the property in the propertiview. When turn on/ff DynamicHidden flag, this property will show/hide. The nodes hidden by this flag still exist in UI."""
    kFBLoadedUserProperty:FBPropertyFlag
    """This property is loaded from file."""
    kFBPropertyFlagAnimated:FBPropertyFlag
    kFBPropertyFlagDisableProperty:FBPropertyFlag
    kFBPropertyFlagDrivenProperty:FBPropertyFlag
    """This is property is connected and driven by other same type of main property, and it always ask value from its main property."""
    kFBPropertyFlagForceStaticProperty:FBPropertyFlag
    kFBPropertyFlagHideProperty:FBPropertyFlag
    """This flag is used to show/hide the property in the propertiview. However, when turn on/off HidePropertry flag, this property won't show/hide unless you reload the UI. The nodes hidden by this flag are removed from UI."""
    kFBPropertyFlagNotSavable:FBPropertyFlag
    """Should not be saved to or loaded from an FBX file."""
    kFBPropertyFlagNotSet:FBPropertyFlag
    kFBPropertyFlagNotUserDeletable:FBPropertyFlag
    kFBPropertyFlagReadOnly:FBPropertyFlag
    kFBSlaveSetByMaster:FBPropertyFlag
    """K_DEPRECATED_2021, use kFBDrivenSetByMain."""
    kFBValueAllocated:FBPropertyFlag
    """The value has been allocated and must be delete in destructor."""
class FBPropertyStateEventType(_Enum):
    """This enum indicates what modification was made to the animation of a tracked property.Property class: const char * (String)."""
    kFBPropertyStateEventTypeAttached:FBPropertyStateEventType
    """Property connector was added (can happen when undoing a delete operation, which set back the property active in the scene)"""
    kFBPropertyStateEventTypeDestroyed:FBPropertyStateEventType
    """Property connector was destroyed (property animation was deleted)"""
    kFBPropertyStateEventTypeDetached:FBPropertyStateEventType
    """Property connector was detached (property animation was delete from the scene, but it still keep in case an undo operation is done)"""
    kFBPropertyStateEventTypeMassOperation:FBPropertyStateEventType
    """Property was heavily modified (switching to story tool, story clip deleted...)"""
    kFBPropertyStateEventTypeUnknownOperation:FBPropertyStateEventType
    """Invalid event."""
class FBPropertyType(_Enum):
    """Property types.
    See sample: CustomProperty.py."""
    kFBPT_Action:FBPropertyType
    """action."""
    kFBPT_ColorRGB:FBPropertyType
    """colorrgb."""
    kFBPT_ColorRGBA:FBPropertyType
    """colorrgba."""
    kFBPT_Reference:FBPropertyType
    """reference."""
    kFBPT_Time:FBPropertyType
    """time."""
    kFBPT_TimeCode:FBPropertyType
    """timecode."""
    kFBPT_TimeSpan:FBPropertyType
    """timespan."""
    kFBPT_Vector2D:FBPropertyType
    """vector2d."""
    kFBPT_Vector3D:FBPropertyType
    """vector3d."""
    kFBPT_Vector4D:FBPropertyType
    """vector4d."""
    kFBPT_bool:FBPropertyType
    """bool."""
    kFBPT_charptr:FBPropertyType
    """charptr."""
    kFBPT_double:FBPropertyType
    """double."""
    kFBPT_enum:FBPropertyType
    """enum."""
    kFBPT_event:FBPropertyType
    """event."""
    kFBPT_float:FBPropertyType
    """float."""
    kFBPT_int:FBPropertyType
    """int."""
    kFBPT_kReference:FBPropertyType
    """kReference."""
    kFBPT_object:FBPropertyType
    """object."""
    kFBPT_stringlist:FBPropertyType
    """stringlist."""
    kFBPT_unknown:FBPropertyType
    """unknow."""
class FBPropertyViewType(_Enum):
    """Property view set type."""
    kFBViewByObject:FBPropertyViewType
    """Object property view."""
    kFBViewByObjectType:FBPropertyViewType
    """Class type property view."""
    kFBViewGlobal:FBPropertyViewType
    """Global property view."""
class FBRSType(_Enum):
    """RS type for serial port."""
    kFBRS232:FBRSType
    """RS-232 serial protocol."""
    kFBRS422:FBRSType
    """RS-422 serial protocol."""
class FBRecalcMarkerSetOffset(_Enum):
    """Recalculate MarkerSet offset for?"""
    kFBRecalcMarkerSetOffsetROnly:FBRecalcMarkerSetOffset
    """Recalculate MarkerSet offset for R Only."""
    kFBRecalcMarkerSetOffsetTR:FBRecalcMarkerSetOffset
    """Recalculate MarkerSet offset for TR."""
class FBRenderingPass(_Enum):
    """Rendering Pass.
    Use with FBShader::RenderingPass properties to make the shader be called at any pass. Passes will be called in the order of the enum."""
    kFBPassAddColor:FBRenderingPass
    """Models are blended additively."""
    kFBPassFlat:FBRenderingPass
    """Lighting off."""
    kFBPassInvalid:FBRenderingPass
    """No pass selected."""
    kFBPassLighted:FBRenderingPass
    """Lighting on."""
    kFBPassMatte:FBRenderingPass
    """Alpha > 0.5 will show up."""
    kFBPassPostRender:FBRenderingPass
    """After everything."""
    kFBPassPreRender:FBRenderingPass
    """Before anything."""
    kFBPassTranslucent:FBRenderingPass
    """Models are blended."""
    kFBPassTranslucentZSort:FBRenderingPass
    """Models are sorted and blended."""
    kFBPassZTranslucent:FBRenderingPass
    """Writes to depth buffer."""
    kFBPassZTranslucentAlphaTest:FBRenderingPass
    """Writes to depth buffer where Alpha > 0.5."""
class FBRigidBodyMode(_Enum):
    """Rigid body modes."""
    kFBRigidBodyBest:FBRigidBodyMode
    """Best rigid body mode."""
    kFBRigidBodyFast:FBRigidBodyMode
    """Fast rigid body mode."""
class FBRootHMode(_Enum):
    kFBRootHAbsoluteDifference:FBRootHMode
    kFBRootHRelativeDifference:FBRootHMode
class FBRootRMode(_Enum):
    kFBRootRAbsoluteDifference:FBRootRMode
    kFBRootRRelativeDifference:FBRootRMode
class FBRootSpeedMode(_Enum):
    kFBRootSpeedAbsoluteDifference:FBRootSpeedMode
    kFBRootSpeedRelativeDifference:FBRootSpeedMode
class FBRootXZMode(_Enum):
    kFBRootXZAbsoluteDifference:FBRootXZMode
    kFBRootXZRelativeDifference:FBRootXZMode
class FBRotationFilter(_Enum):
    """Rotation filters."""
    kFBRotationFilterGimbleKiller:FBRotationFilter
    kFBRotationFilterNone:FBRotationFilter
    kFBRotationFilterUnroll:FBRotationFilter
class FBRotationOrder(_Enum):
    """Specify the Euler rotation order."""
    kFBXYZ:FBRotationOrder
    """XYZ"""
    kFBXZY:FBRotationOrder
    """XZY."""
    kFBYXZ:FBRotationOrder
    """YXZ."""
    kFBYZX:FBRotationOrder
    """YZX"""
    kFBZXY:FBRotationOrder
    """ZXY"""
    kFBZYX:FBRotationOrder
    """ZYX."""
class FBSceneChangeType(_Enum):
    """Types of model selection events.
    See sample: PropertyDrop.py."""
    kFBSceneChangeActivate:FBSceneChangeType
    """Activate."""
    kFBSceneChangeAddChild:FBSceneChangeType
    """Child added."""
    kFBSceneChangeAttach:FBSceneChangeType
    """Object attached."""
    kFBSceneChangeChangeName:FBSceneChangeType
    """Object change name."""
    kFBSceneChangeChangedName:FBSceneChangeType
    """Object changed name."""
    kFBSceneChangeChangedParent:FBSceneChangeType
    """Object changed parent."""
    kFBSceneChangeClearBegin:FBSceneChangeType
    """Begin clearing file (file new)"""
    kFBSceneChangeClearEnd:FBSceneChangeType
    """End clearing file (file new)"""
    kFBSceneChangeDeactivate:FBSceneChangeType
    """Deactivate."""
    kFBSceneChangeDestroy:FBSceneChangeType
    """Object destroyed."""
    kFBSceneChangeDetach:FBSceneChangeType
    """Object detached."""
    kFBSceneChangeFocus:FBSceneChangeType
    """Object have focus."""
    kFBSceneChangeHardSelect:FBSceneChangeType
    """Hard selection."""
    kFBSceneChangeLoadBegin:FBSceneChangeType
    """Begin loading file."""
    kFBSceneChangeLoadEnd:FBSceneChangeType
    """End loading file."""
    kFBSceneChangeMergeTransactionBegin:FBSceneChangeType
    """Begin merge transaction."""
    kFBSceneChangeMergeTransactionEnd:FBSceneChangeType
    """End merge transaction."""
    kFBSceneChangeNone:FBSceneChangeType
    """Unknown event."""
    kFBSceneChangePreParent:FBSceneChangeType
    """Before object parenting."""
    kFBSceneChangePreUnparent:FBSceneChangeType
    """Before object unparenting."""
    kFBSceneChangeReSelect:FBSceneChangeType
    """Re-selection."""
    kFBSceneChangeRemoveChild:FBSceneChangeType
    """Child removed."""
    kFBSceneChangeRename:FBSceneChangeType
    """Before object rename."""
    kFBSceneChangeRenamePrefix:FBSceneChangeType
    """Before object rename prefix."""
    kFBSceneChangeRenameUnique:FBSceneChangeType
    """Before object rename unique."""
    kFBSceneChangeRenameUniquePrefix:FBSceneChangeType
    """Before object rename unique prefix."""
    kFBSceneChangeRenamed:FBSceneChangeType
    """After object rename."""
    kFBSceneChangeRenamedPrefix:FBSceneChangeType
    """After object rename prefix."""
    kFBSceneChangeRenamedUnique:FBSceneChangeType
    """After object rename unique."""
    kFBSceneChangeRenamedUniquePrefix:FBSceneChangeType
    """After object rename unique prefix."""
    kFBSceneChangeReorder:FBSceneChangeType
    """Object reorder."""
    kFBSceneChangeReordered:FBSceneChangeType
    """Object reordered."""
    kFBSceneChangeSelect:FBSceneChangeType
    """Object selection."""
    kFBSceneChangeSoftSelect:FBSceneChangeType
    """Soft selection."""
    kFBSceneChangeSoftUnselect:FBSceneChangeType
    """Soft deselection."""
    kFBSceneChangeTransactionBegin:FBSceneChangeType
    """Begin transaction."""
    kFBSceneChangeTransactionEnd:FBSceneChangeType
    """End transaction."""
    kFBSceneChangeUnselect:FBSceneChangeType
    """Object deselection."""
class FBSegmentMode(_Enum):
    """Segment modes."""
    kFBSegmentAll:FBSegmentMode
    """Use all."""
    kFBSegmentMarker:FBSegmentMode
    """Use marker."""
    kFBSegmentRigidBody:FBSegmentMode
    """Use rigid body."""
class FBShadowFrameType(_Enum):
    """Shadow calculation methods."""
    kFBShadowFrameTypeShadowCaster:FBShadowFrameType
    """Bases the shadow calculation on the shadow of the caster."""
    kFBShadowFrameTypeShadowCubeMap:FBShadowFrameType
    """Undocumented or unsupported."""
    kFBShadowFrameTypeShadowReceiver:FBShadowFrameType
    """Bases the shadow calculation on the shadow of the receiver."""
class FBShadowType(_Enum):
    """Shadow types.
    The different types of shadow mapping."""
    kFBShadowTypeLightMapProjectiveTexture:FBShadowType
    """Uses a texture projection as a shadow."""
    kFBShadowTypeShadowOpaquePlanar:FBShadowType
    """Similar to the Planar Shadow, except that it treats all objects as opaque."""
    kFBShadowTypeShadowProjectiveTexture:FBShadowType
    """Uses a texture projection to create a shadow."""
    kFBShadowTypeShadowTranslucentPlanar:FBShadowType
    """Use this shadow type to create darkened shadow areas only on planar surfaces."""
    kFBShadowTypeZLightMapProjectiveTexture:FBShadowType
    """Similar to the Projective Light Map except that it uses a boolean algorithm to create a self-shadow."""
    kFBShadowTypeZShadowProjectiveTexture:FBShadowType
    """Similar to the Projective Shadow, except that it uses a boolean algorithm to create a self-shadow."""
class FBSkeletonLook(_Enum):
    """Look of the skeleton."""
    kFBSkeletonLookBone:FBSkeletonLook
    """Bone."""
    kFBSkeletonLookBox:FBSkeletonLook
    """Box."""
    kFBSkeletonLookCapsule:FBSkeletonLook
    """Capsule."""
    kFBSkeletonLookCircle:FBSkeletonLook
    """Circle."""
    kFBSkeletonLookCube:FBSkeletonLook
    """Cube."""
    kFBSkeletonLookHardCross:FBSkeletonLook
    """Thick cross."""
    kFBSkeletonLookLightCross:FBSkeletonLook
    """Wireframe cross."""
    kFBSkeletonLookSphere:FBSkeletonLook
    """Sphere."""
    kFBSkeletonLookSquare:FBSkeletonLook
    """Square."""
    kFBSkeletonLookStick:FBSkeletonLook
    """Box with a sphere on one end."""
class FBSkeletonNodeId(_Enum):
    """All Skeleton nodes"""
    kFBSkeletonChestIndex:FBSkeletonNodeId
    kFBSkeletonHeadIndex:FBSkeletonNodeId
    kFBSkeletonHipsIndex:FBSkeletonNodeId
    kFBSkeletonInvalidIndex:FBSkeletonNodeId
    kFBSkeletonLastIndex:FBSkeletonNodeId
    kFBSkeletonLeftAnkleIndex:FBSkeletonNodeId
    kFBSkeletonLeftCollarIndex:FBSkeletonNodeId
    kFBSkeletonLeftElbowIndex:FBSkeletonNodeId
    kFBSkeletonLeftFootIndex:FBSkeletonNodeId
    kFBSkeletonLeftHipIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexAIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexBIndex:FBSkeletonNodeId
    kFBSkeletonLeftIndexCIndex:FBSkeletonNodeId
    kFBSkeletonLeftKneeIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleAIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleBIndex:FBSkeletonNodeId
    kFBSkeletonLeftMiddleCIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyAIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyBIndex:FBSkeletonNodeId
    kFBSkeletonLeftPinkyCIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingAIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingBIndex:FBSkeletonNodeId
    kFBSkeletonLeftRingCIndex:FBSkeletonNodeId
    kFBSkeletonLeftShoulderIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbAIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbBIndex:FBSkeletonNodeId
    kFBSkeletonLeftThumbCIndex:FBSkeletonNodeId
    kFBSkeletonLeftWristIndex:FBSkeletonNodeId
    kFBSkeletonNeckIndex:FBSkeletonNodeId
    kFBSkeletonReferenceIndex:FBSkeletonNodeId
    kFBSkeletonRightAnkleIndex:FBSkeletonNodeId
    kFBSkeletonRightCollarIndex:FBSkeletonNodeId
    kFBSkeletonRightElbowIndex:FBSkeletonNodeId
    kFBSkeletonRightFootIndex:FBSkeletonNodeId
    kFBSkeletonRightHipIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexAIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexBIndex:FBSkeletonNodeId
    kFBSkeletonRightIndexCIndex:FBSkeletonNodeId
    kFBSkeletonRightKneeIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleAIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleBIndex:FBSkeletonNodeId
    kFBSkeletonRightMiddleCIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyAIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyBIndex:FBSkeletonNodeId
    kFBSkeletonRightPinkyCIndex:FBSkeletonNodeId
    kFBSkeletonRightRingAIndex:FBSkeletonNodeId
    kFBSkeletonRightRingBIndex:FBSkeletonNodeId
    kFBSkeletonRightRingCIndex:FBSkeletonNodeId
    kFBSkeletonRightShoulderIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbAIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbBIndex:FBSkeletonNodeId
    kFBSkeletonRightThumbCIndex:FBSkeletonNodeId
    kFBSkeletonRightWristIndex:FBSkeletonNodeId
    kFBSkeletonWaistIndex:FBSkeletonNodeId
class FBSkeletonResolutionLevel(_Enum):
    """Resolution of skeleton sphere, capsule and stick (Quality)."""
    kFBSkeletonHighResolution:FBSkeletonResolutionLevel
    """Highest resolution."""
    kFBSkeletonLowResolution:FBSkeletonResolutionLevel
    """Lowest resolution."""
    kFBSkeletonMediumResolution:FBSkeletonResolutionLevel
    """Medium resolution."""
class FBSplitStyle(_Enum):
    """Type of split style (sub-division) for layout."""
    kFBHSplit:FBSplitStyle
    """Horizontal split."""
    kFBHVSplit:FBSplitStyle
    """Horizontal and Vertical split."""
    kFBNoSplit:FBSplitStyle
    """No split."""
    kFBVSplit:FBSplitStyle
    """Vertical split."""
class FBStereoDisplayMode(_Enum):
    kFBStereoDisplayActive:FBStereoDisplayMode
    """Display in active mode. User must enable OpenGL quad stereo buffer, and choose approriate stereo mode in video card hardware's config app."""
    kFBStereoDisplayAnaglyph:FBStereoDisplayMode
    """Display in Analygh stereo mode."""
    kFBStereoDisplayAnaglyphLuminance:FBStereoDisplayMode
    """Display in Luminance Analygh stereo mode."""
    kFBStereoDisplayCenterEye:FBStereoDisplayMode
    """Display in Center Eye Camera, No Stereo effect."""
    kFBStereoDisplayCheckerboard:FBStereoDisplayMode
    """Display in Checkboard Interlace stereo mode."""
    kFBStereoDisplayFreeviewCrossed:FBStereoDisplayMode
    """Display in crossed free view stereo mode."""
    kFBStereoDisplayFreeviewParallel:FBStereoDisplayMode
    """Display in parallel free view stereo mode."""
    kFBStereoDisplayHorizontalInterlace:FBStereoDisplayMode
    """Display in Horizontal Interlace stereo mode."""
    kFBStereoDisplayLeftEye:FBStereoDisplayMode
    """Display in Left Eye Caerma, No Stereo effect."""
    kFBStereoDisplayModeCount:FBStereoDisplayMode
    """update this count value when add new mode"""
    kFBStereoDisplayRightEye:FBStereoDisplayMode
    """Display in Right Eye Caerma, No Stereo effect."""
class FBStoryClipAlignmentType(_Enum):
    """Alignment Types when aligning clips."""
    kFBStoryClipAlignmentBeginningNext:FBStoryClipAlignmentType
    """Align selected clips to the beginning of the next clip."""
    kFBStoryClipAlignmentBeginningNextAllAligned:FBStoryClipAlignmentType
    """Align selected clips to the beginning of the next clip, all clips will be align to the selected clip position."""
    kFBStoryClipAlignmentBeginningNextWithOffset:FBStoryClipAlignmentType
    """Align selected clips to the beginning of the next clip, while keeping the relative offset."""
    kFBStoryClipAlignmentCurrentTimeline:FBStoryClipAlignmentType
    """Align all selected clips with the current time."""
    kFBStoryClipAlignmentCurrentTimelineWithOffset:FBStoryClipAlignmentType
    """Align all selected clips with the current time, while keeping the relative offset."""
    kFBStoryClipAlignmentEndPrevious:FBStoryClipAlignmentType
    """Align selected clips to the end of the previous clip."""
    kFBStoryClipAlignmentEndPreviousAllAligned:FBStoryClipAlignmentType
    """Align selected clips to the end of the previous clip, all clips will be align to the selected clip position."""
    kFBStoryClipAlignmentEndPreviousWithOffset:FBStoryClipAlignmentType
    """Align selected clips to the end of the previous clip, while keeping the relative offset."""
class FBStoryClipChangeType(_Enum):
    """Types of clip change events, matching KEventClip.eType Expose only kFBStoryClipMoveClip and kFBStoryClipRemoved for now."""
    kFBStoryClipMoveBlend:FBStoryClipChangeType
    """Clip move blend."""
    kFBStoryClipMoveClip:FBStoryClipChangeType
    """Clip moved."""
    kFBStoryClipMoveData:FBStoryClipChangeType
    """Clip data moved."""
    kFBStoryClipNotSet:FBStoryClipChangeType
    """Clip none."""
    kFBStoryClipRemoved:FBStoryClipChangeType
    """Clip removed."""
    kFBStoryClipUpdateUI:FBStoryClipChangeType
    """Clip UI update."""
class FBStoryClipCompMode(_Enum):
    """Compensation Modes for story character clips."""
    kFBStoryClipAuto:FBStoryClipCompMode
    """Automatic compensation."""
    kFBStoryClipOff:FBStoryClipCompMode
    """No compensation."""
    kFBStoryClipUser:FBStoryClipCompMode
    """User defined compensation."""
class FBStoryClipGhostTimeMode(_Enum):
    """Time mode to display ghost."""
    kFBStoryClipGhostCurrent:FBStoryClipGhostTimeMode
    """Show the ghost at current time of the clip."""
    kFBStoryClipGhostCustom:FBStoryClipGhostTimeMode
    """Show the ghost at custom time of the clip. See GhostManipulatorCustomTime property."""
    kFBStoryClipGhostStart:FBStoryClipGhostTimeMode
    """Show the ghost at start time of the clip."""
    kFBStoryClipGhostStop:FBStoryClipGhostTimeMode
    """Show the ghost at stop time of the clip."""
class FBStoryClipMatchingRotationType(_Enum):
    """Matching Rotation Types, when matching clips to each other."""
    kFBStoryClipMatchingRotationDefault:FBStoryClipMatchingRotationType
    """Uses the matching translation type stored in the Application configuration file: [Story] > MatchRotation. This value, in the configuration file, is update each time a matching is done, with the selected value."""
    kFBStoryClipMatchingRotationGravityXZ:FBStoryClipMatchingRotationType
    """Rotates a selected clip's match object around the global Y axis."""
    kFBStoryClipMatchingRotationNone:FBStoryClipMatchingRotationType
    """The clip's match object is not rotated to match another clip's animation."""
    kFBStoryClipMatchingRotationXYZ:FBStoryClipMatchingRotationType
    """Rotates a selected clip's match object to the same orientation as the previous clip's match object."""
class FBStoryClipMatchingTimeType(_Enum):
    """Matching Time Types, when matching clips to each other."""
    kFBStoryClipMatchingTimeBetweenPreviousAndSelectedClip:FBStoryClipMatchingTimeType
    """Matches the selected clip and the previous clip at the middle of the blend."""
    kFBStoryClipMatchingTimeBetweenSelectedAndNextClip:FBStoryClipMatchingTimeType
    """Matches the selected clip and the next clip at the middle of the blend."""
    kFBStoryClipMatchingTimeCurrentTime:FBStoryClipMatchingTimeType
    """Matches the start of the selected clip to the previous/next clip at the current time."""
    kFBStoryClipMatchingTimeDefault:FBStoryClipMatchingTimeType
    """Uses the matching time type stored in the Application configuration file: [Story] > MatchWhen. This value, in the configuration file, is update each time a matching is done, with the selected value."""
    kFBStoryClipMatchingTimeEndOfPreviousClip:FBStoryClipMatchingTimeType
    """Matches the end of the blend with the selected clip to the end of the previous clip."""
    kFBStoryClipMatchingTimeEndOfSelectedClip:FBStoryClipMatchingTimeType
    """Matches the end of the selected clip to the end of the blend with the previous clip."""
    kFBStoryClipMatchingTimeStartOfNextClip:FBStoryClipMatchingTimeType
    """Matches the start of the blend with the selected clip to the start of the next clip."""
    kFBStoryClipMatchingTimeStartOfSelectedClip:FBStoryClipMatchingTimeType
    """Matches the start of the selected clip to the start of the blend with the previous clip."""
class FBStoryClipMatchingTranslationType(_Enum):
    """Matching Translation, Types when matching clips to each other."""
    kFBStoryClipMatchingTranslationDefault:FBStoryClipMatchingTranslationType
    """Uses the matching translation type stored in the Application configuration file: [Story] > MatchTranslation. This value, in the configuration file, is update each time a matching is done, with the selected value."""
    kFBStoryClipMatchingTranslationGravityXZ:FBStoryClipMatchingTranslationType
    """Translates a selected clip's match object along the global X and Z axes."""
    kFBStoryClipMatchingTranslationNone:FBStoryClipMatchingTranslationType
    """The clip's match object is not translated to match another clip's animation."""
    kFBStoryClipMatchingTranslationXYZ:FBStoryClipMatchingTranslationType
    """Translates a selected clip's match object to the same location as the previous clip's match object."""
class FBStoryClipMirrorPlane(_Enum):
    """Several mirror planes to mirror animation."""
    kFBStoryClipMirrorPlaneXY:FBStoryClipMirrorPlane
    """X-Y plane."""
    kFBStoryClipMirrorPlaneXZ:FBStoryClipMirrorPlane
    """X-Z plane."""
    kFBStoryClipMirrorPlaneZY:FBStoryClipMirrorPlane
    """Z-Y plane."""
class FBStoryClipNodeFunction(_Enum):
    """Node function."""
    kFBStoryClipNodeAverage:FBStoryClipNodeFunction
    """Average."""
    kFBStoryClipNodeFloorProjection:FBStoryClipNodeFunction
    """Project on XZ plane."""
    kFBStoryClipNodeNone:FBStoryClipNodeFunction
    """None."""
class FBStoryClipShowGhostMode(_Enum):
    """Show Ghost Modes for story animation clips."""
    kFBStoryClipAlways:FBStoryClipShowGhostMode
    """Always show the ghost."""
    kFBStoryClipTimeCursor:FBStoryClipShowGhostMode
    """Show the ghost only on time cursor."""
    kFBStoryClipTimeCustom:FBStoryClipShowGhostMode
    """Show the ghost for custom time frame."""
class FBStoryClipSolveMode(_Enum):
    """Solve Modes for story character clips."""
    kFBStoryClipAnimFkIk:FBStoryClipSolveMode
    """Solve forward and inverse kinematic animation."""
    kFBStoryClipAnimSkeleton:FBStoryClipSolveMode
    """Solve skeleton animation."""
    kFBStoryClipAnimSkeletonIk:FBStoryClipSolveMode
    """Solve skeleton inverse kinematic animation."""
    kFBStoryClipRetargetSkeleton:FBStoryClipSolveMode
    """Solve retarget skeleton."""
class FBStoryClipTimeWarpInterpolatorType(_Enum):
    """Types of TimeWrap Interpolator for Story Clips."""
    kFBStoryClipTimeWarpInterpolatorCustom:FBStoryClipTimeWarpInterpolatorType
    """'Custom' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorGoingFaster:FBStoryClipTimeWarpInterpolatorType
    """'Going Faster' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorGoingFasterReversed:FBStoryClipTimeWarpInterpolatorType
    """'Reversed, Going Faster' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorLinear:FBStoryClipTimeWarpInterpolatorType
    """'Normal' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorLinearReversed:FBStoryClipTimeWarpInterpolatorType
    """'Reversed' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorSlowingDown:FBStoryClipTimeWarpInterpolatorType
    """'Slowing Down' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorSlowingDownReversed:FBStoryClipTimeWarpInterpolatorType
    """'Reversed, Slowing Down' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorSmoothedEnds:FBStoryClipTimeWarpInterpolatorType
    """'Smoothed Ends' TimeWarp Interpolation"""
    kFBStoryClipTimeWarpInterpolatorSmoothedEndsReversed:FBStoryClipTimeWarpInterpolatorType
    """'Reversed, Smoothed Ends' TimeWarp Interpolation"""
class FBStoryGroupClipAlignmentType(_Enum):
    """Alignment Types when aligning groups."""
    kFBStoryGroupClipAlignmentBeginningNextWithOffset:FBStoryGroupClipAlignmentType
    """Align the clips contained in the group clip to the beginning of the next clip, while keeping the relative offset."""
    kFBStoryGroupClipAlignmentCurrentTimeline:FBStoryGroupClipAlignmentType
    """Align the clips contained in the group clip with the current time."""
    kFBStoryGroupClipAlignmentEndPreviousWithOffset:FBStoryGroupClipAlignmentType
    """Align the clips contained in the group clip to the end of the previous clip, while keeping the relative offset."""
class FBStoryTrackBodyPart(_Enum):
    """Body Parts for story track character."""
    kFBStoryTrackBodyPartAll:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartExtensions:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartHead:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftArm:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftFoot:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftHand:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftLeg:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLeftShoulder:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartLowerBody:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartNone:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartProps:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightArm:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightFoot:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightHand:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightLeg:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartRightShoulder:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartSpine:FBStoryTrackBodyPart
    kFBStoryTrackBodyPartUpperBody:FBStoryTrackBodyPart
class FBStoryTrackGhostShowMode(_Enum):
    """Ghost Show Modes for story animation tracks."""
    kFBStoryTrackShowAllClips:FBStoryTrackGhostShowMode
    """Show the ghosts for all the clips on the track."""
    kFBStoryTrackShowCurrentTimeAdjacentClips:FBStoryTrackGhostShowMode
    """Show the ghosts only for the previous clip, current clip, and next clip relative to current time."""
class FBStoryTrackRefMode(_Enum):
    """References Modes for story animation tracks."""
    kFBStoryTrackAdditive:FBStoryTrackRefMode
    """Additive track."""
    kFBStoryTrackOverride:FBStoryTrackRefMode
    """Override track."""
class FBStoryTrackType(_Enum):
    """Types for new story tracks.
    See samples: CreateShotClip.py, AudioTrackSetupTool.py."""
    kFBStoryTrackAnimation:FBStoryTrackType
    """Animation track."""
    kFBStoryTrackAudio:FBStoryTrackType
    """Audio track."""
    kFBStoryTrackCamera:FBStoryTrackType
    """Camera animation track."""
    kFBStoryTrackCharacter:FBStoryTrackType
    """Character animation track."""
    kFBStoryTrackCommand:FBStoryTrackType
    """Command track."""
    kFBStoryTrackConstraint:FBStoryTrackType
    """Constraint track."""
    kFBStoryTrackShot:FBStoryTrackType
    """Shot track."""
    kFBStoryTrackVideo:FBStoryTrackType
    """Video track."""
class FBSurfaceMode(_Enum):
    """Surface modes."""
    kFBSurfaceModeHigh:FBSurfaceMode
    """High quality."""
    kFBSurfaceModeHighNoNormals:FBSurfaceMode
    """High quality, no normals."""
    kFBSurfaceModeLow:FBSurfaceMode
    """Low quality."""
    kFBSurfaceModeLowNoNormals:FBSurfaceMode
    """Low quality, no normals."""
    kFBSurfaceModeRaw:FBSurfaceMode
    """Raw data."""
class FBSurfaceType(_Enum):
    """Surface types."""
    kFBSurfaceTypeBezier:FBSurfaceType
    """Bezier surface."""
    kFBSurfaceTypeBezierQuadric:FBSurfaceType
    """Bezier Quadric surface."""
    kFBSurfaceTypeBspline:FBSurfaceType
    """BSpline surface."""
    kFBSurfaceTypeCardinal:FBSurfaceType
    """Cardinal surface."""
    kFBSurfaceTypeLinear:FBSurfaceType
    """Linear surface."""
class FBSyncActivationAndVisibilityMode(_Enum):
    """Sync mode for Constraints' Activeness and Models' visibility belonging to the Character Extension."""
    kFBSyncMode_None:FBSyncActivationAndVisibilityMode
    kFBSyncMode_WithContolRig:FBSyncActivationAndVisibilityMode
    kFBSyncMode_WithOthersThanControlRig:FBSyncActivationAndVisibilityMode
class FBTCPIPSocketType(_Enum):
    """Types of TCP/IP Sockets."""
    kFBTCPIP_DGRAM:FBTCPIPSocketType
    """Datagrams (UDP)."""
    kFBTCPIP_RAW:FBTCPIPSocketType
    """Raw data (TCP)."""
    kFBTCPIP_Stream:FBTCPIPSocketType
    """Streaming data (TCP)."""
class FBTakeChangeType(_Enum):
    """Types of take change events."""
    kFBTakeChangeAdded:FBTakeChangeType
    kFBTakeChangeClosed:FBTakeChangeType
    kFBTakeChangeMoved:FBTakeChangeType
    kFBTakeChangeNone:FBTakeChangeType
    kFBTakeChangeOpened:FBTakeChangeType
    kFBTakeChangeRemoved:FBTakeChangeType
    kFBTakeChangeRenamed:FBTakeChangeType
    kFBTakeChangeUpdated:FBTakeChangeType
class FBTakeSpanOnLoad(_Enum):
    """This enumeration indicate the how to set the take start and end points on after a load."""
    kFBFrameAnimation:FBTakeSpanOnLoad
    """Have the take's span match the first and last key in the take."""
    kFBImportFromFile:FBTakeSpanOnLoad
    """Set the current take's span according what is set in the loaded file."""
    kFBLeaveAsIs:FBTakeSpanOnLoad
    """Use the current take's start and end point as defined before the load."""
class FBTangentClampMode(_Enum):
    """Different clamping modes for the tangents."""
    kFBTangentClampModeClamped:FBTangentClampMode
    """The tangent will be flattened when the key is placed at the same value as an adjacent key."""
    kFBTangentClampModeNone:FBTangentClampMode
    """The tangent will act normally."""
class FBTangentConstantMode(_Enum):
    """Different constant modes for the tangents."""
    kFBTangentConstantModeNext:FBTangentConstantMode
    """The tangent will contain the value of the next keyframe."""
    kFBTangentConstantModeNormal:FBTangentConstantMode
    """The tangent will contain the value of the current keyframe until the next keyframe."""
class FBTangentCustomIndex(_Enum):
    """Custom tangent index for the tangents."""
    kFBTangentCustomIndex0:FBTangentCustomIndex
    """First custom tangent type registered in the system."""
    kFBTangentCustomIndex1:FBTangentCustomIndex
    """Second custom tangent type registered in the system."""
    kFBTangentCustomIndex2:FBTangentCustomIndex
    """Third custom tangent type registered in the system."""
class FBTangentMode(_Enum):
    """Methods of tangent calculation.
    This is only relevant when interpolation is CUBIC."""
    kFBTangentModeAuto:FBTangentMode
    """This is the equivalent to a cardinal spline with no parametrization. In the UI, it is identified as Smooth."""
    kFBTangentModeBreak:FBTangentMode
    """Like USER but left slope may differ from right."""
    kFBTangentModeClampProgressive:FBTangentMode
    """Time independent, will flatten the tangent handles when the key value goes over or under the previous and next key values. In the UI, it is identified as Auto."""
    kFBTangentModeTCB:FBTangentMode
    """TCB spline (3 parameters: TENSION, CONTINUITY, BIAS)"""
    kFBTangentModeTimeIndependent:FBTangentMode
    """Time independent, is calculated based upon the slope between the previous and next key values. In the UI, it is identified as Spline."""
    kFBTangentModeUser:FBTangentMode
    """Used to represent all splines with no lost data (HERMITE, BEZIER, CATMUL, etc.)"""
class FBTangentWeightMode(_Enum):
    """Active tangent weight, no/one/both side are active on a key.
    Please note, the left value is for the next key, as the current key contains the tangent weight information for the next key. To disable the weight on the left side of a key at index 'i', you need to disable 'kFBTangentWeightModeNextLeft' the 'i-1' key."""
    kFBTangentWeightModeBoth:FBTangentWeightMode
    """Right tangent and next key left tangent weight are active."""
    kFBTangentWeightModeNextLeft:FBTangentWeightMode
    """Next key left tangent weight active."""
    kFBTangentWeightModeNone:FBTangentWeightMode
    """Tangent weight disabled."""
    kFBTangentWeightModeRight:FBTangentWeightMode
    """Right tangent weight active."""
class FBTextJustify(_Enum):
    """Text justification styles.
    See samples: Button.py, Label.py."""
    kFBTextJustifyCenter:FBTextJustify
    """Center alignment."""
    kFBTextJustifyLeft:FBTextJustify
    """Left justify."""
    kFBTextJustifyRight:FBTextJustify
    """Right justify."""
class FBTextStyle(_Enum):
    """Text appearance styles.
    See sample: Label.py."""
    kFBTextStyleBold:FBTextStyle
    """Bold."""
    kFBTextStyleItalic:FBTextStyle
    """Italic."""
    kFBTextStyleNone:FBTextStyle
    """Normal."""
    kFBTextStyleUnderlined:FBTextStyle
    """Underlined."""
class FBTextureBlendMode(_Enum):
    """Texture blend modes.
    How the texture is blended with another. See samples: LayeredTexture.py, TextureAnimation.py."""
    kFBTextureBlendAdditive:FBTextureBlendMode
    """Layer addition."""
    kFBTextureBlendModulate:FBTextureBlendMode
    """Layer multiplication."""
    kFBTextureBlendModulate2:FBTextureBlendMode
    """Layer multiplication + brightness."""
    kFBTextureBlendTranslucent:FBTextureBlendMode
    """Layer transparency."""
class FBTextureMapping(_Enum):
    """Texture mapping modes.
    How the texture is mapped."""
    kFBTextureMappingCylindrical:FBTextureMapping
    """Cylindrical mapping."""
    kFBTextureMappingEnvironment:FBTextureMapping
    """Environment mapping."""
    kFBTextureMappingProjection:FBTextureMapping
    """Projection mapping."""
    kFBTextureMappingSpherical:FBTextureMapping
    """Spherical mapping."""
    kFBTextureMappingUV:FBTextureMapping
    """UV mapping."""
    kFBTextureMappingXY:FBTextureMapping
    """XY mapping."""
    kFBTextureMappingXZ:FBTextureMapping
    """XZ mapping."""
    kFBTextureMappingYZ:FBTextureMapping
    """YZ mapping."""
    kFBTextureNoMapping:FBTextureMapping
    """No mapping."""
class FBTextureUseType(_Enum):
    """Texture Use Type.
    How the texture is used."""
    kFBTextureUseAll:FBTextureUseType
    """All textures."""
    kFBTextureUseBumpNormalMap:FBTextureUseType
    """Bump Normal Map, work with model."""
    kFBTextureUseColor:FBTextureUseType
    """standard color type, work with material."""
    kFBTextureUseLightMap:FBTextureUseType
    """Light Map, work with model."""
    kFBTextureUseShadowMap:FBTextureUseType
    """Shadow Map, work with model."""
    kFBTextureUseSphereReflexionMap:FBTextureUseType
    """Sphere Reflexion Map, work with model."""
    kFBTextureUseSphericalReflexionMap:FBTextureUseType
    """Spherical Reflexion Map, work with model."""
class FBTimeMarkAction(_Enum):
    """Time (Global & Take) Mark assigned action."""
    kFBTimeMarkAction_Loop:FBTimeMarkAction
    """When reaching the mark, the playback loops to previous global mark (or start frame if any)."""
    kFBTimeMarkAction_None:FBTimeMarkAction
    """No action. The mark is just visual hint."""
    kFBTimeMarkAction_Stop:FBTimeMarkAction
    """When reaching the mark, the playback stops."""
class FBTimeMode(_Enum):
    """Different time modes available."""
    kFBTimeMode1000Frames:FBTimeMode
    """1000 : 1 millisecond"""
    kFBTimeMode100Frames:FBTimeMode
    """100"""
    kFBTimeMode11988Frames:FBTimeMode
    """~119.88"""
    kFBTimeMode120Frames:FBTimeMode
    """120"""
    kFBTimeMode23976Frames:FBTimeMode
    """~23.976"""
    kFBTimeMode24Frames:FBTimeMode
    """24"""
    kFBTimeMode25Frames:FBTimeMode
    """25"""
    kFBTimeMode2997Frames:FBTimeMode
    """~29.97 full"""
    kFBTimeMode2997Frames_Drop:FBTimeMode
    """~29.97 drop"""
    kFBTimeMode30Frames:FBTimeMode
    """30"""
    kFBTimeMode48Frames:FBTimeMode
    """48"""
    kFBTimeMode50Frames:FBTimeMode
    """50"""
    kFBTimeMode5994Frames:FBTimeMode
    """~59.94"""
    kFBTimeMode60Frames:FBTimeMode
    """60"""
    kFBTimeMode72Frames:FBTimeMode
    """72"""
    kFBTimeMode96Frames:FBTimeMode
    """96"""
    kFBTimeModeCustom:FBTimeMode
    """Custom framerate."""
    kFBTimeModeDefault:FBTimeMode
    """Default Time Mode."""
class FBTimeReferential(_Enum):
    """FBCommandState."""
    kFBTimeReferentialAction:FBTimeReferential
    """Action."""
    kFBTimeReferentialEdit:FBTimeReferential
    """Edit."""
    kFBTimeReferentialShot:FBTimeReferential
    """Shot."""
class FBToolPossibleDockPosition(_Enum):
    kFBToolPossibleDockPosBottom:FBToolPossibleDockPosition
    kFBToolPossibleDockPosLeft:FBToolPossibleDockPosition
    kFBToolPossibleDockPosNone:FBToolPossibleDockPosition
    kFBToolPossibleDockPosRight:FBToolPossibleDockPosition
    kFBToolPossibleDockPosTop:FBToolPossibleDockPosition
class FBTransportLoopMode(_Enum):
    """Available loop modes for the transport control."""
    kFBTransportLoopCurrentTake:FBTransportLoopMode
    """Playback looping the current take."""
    kFBTransportLoopThroughAllTakes:FBTransportLoopMode
    """Playback from the current take through all takes in order then stops."""
    kFBTransportNoLoop:FBTransportLoopMode
    """Playback not looping."""
class FBTransportMode(_Enum):
    """Transport modes."""
    kFBTransportGoto:FBTransportMode
    kFBTransportGotoPrepare:FBTransportMode
    """!< Goto."""
    kFBTransportGotoReady:FBTransportMode
    kFBTransportJog:FBTransportMode
    kFBTransportJogPrepare:FBTransportMode
    """!< Jog."""
    kFBTransportJogReady:FBTransportMode
    kFBTransportPlay:FBTransportMode
    kFBTransportPlayPrepare:FBTransportMode
    """!< Play mode"""
    kFBTransportPlayReady:FBTransportMode
    kFBTransportPlayReverse:FBTransportMode
    kFBTransportPlayReversePrepare:FBTransportMode
    """!< Play reverse."""
    kFBTransportPlayReverseReady:FBTransportMode
    kFBTransportShuttle:FBTransportMode
    kFBTransportShuttlePrepare:FBTransportMode
    """!< Shuttle mode"""
    kFBTransportShuttleReady:FBTransportMode
    kFBTransportStepBackward:FBTransportMode
    kFBTransportStepBackwardPrepare:FBTransportMode
    """!< Step backward."""
    kFBTransportStepBackwardReady:FBTransportMode
    kFBTransportStepForward:FBTransportMode
    kFBTransportStepForwardPrepare:FBTransportMode
    """!< Step forward"""
    kFBTransportStepForwardReady:FBTransportMode
    kFBTransportStop:FBTransportMode
    kFBTransportStopPost:FBTransportMode
    """!< Stop mode"""
    kFBTransportStopReady:FBTransportMode
class FBTransportPlaySpeed(_Enum):
    """Available transport control play speed."""
    kFBSpeed_10x:FBTransportPlaySpeed
    """10x"""
    kFBSpeed_1_10x:FBTransportPlaySpeed
    """0.10x"""
    kFBSpeed_1_2x:FBTransportPlaySpeed
    """0.50x"""
    kFBSpeed_1_3x:FBTransportPlaySpeed
    """0.33x"""
    kFBSpeed_1_4x:FBTransportPlaySpeed
    """0.25x"""
    kFBSpeed_1_5x:FBTransportPlaySpeed
    """0.20x"""
    kFBSpeed_1x:FBTransportPlaySpeed
    """1x"""
    kFBSpeed_2x:FBTransportPlaySpeed
    """2x"""
    kFBSpeed_3x:FBTransportPlaySpeed
    """3x"""
    kFBSpeed_4x:FBTransportPlaySpeed
    """4x"""
    kFBSpeed_5x:FBTransportPlaySpeed
    """5x"""
    kFBSpeed_ALL_FR:FBTransportPlaySpeed
    """All frames."""
    kFBSpeed_Custom:FBTransportPlaySpeed
    """Custom speed."""
class FBTransportSnapMode(_Enum):
    """Available snap methods for the transport control."""
    kFBTransportSnapModeNoSnap:FBTransportSnapMode
    """No snapping is applied."""
    kFBTransportSnapModePlayOnFrames:FBTransportSnapMode
    """When playing, plays to exact frames."""
    kFBTransportSnapModeSnapAndPlayOnFrames:FBTransportSnapMode
    """Combines both Snap and Play on frames modes."""
    kFBTransportSnapModeSnapOnFrames:FBTransportSnapMode
    """Snaps to an exact frame when modifying the current time."""
class FBTransportTimeFormat(_Enum):
    """Available transport control time display."""
    kFBTimeFormatFrame:FBTransportTimeFormat
    """Frame time display mode."""
    kFBTimeFormatTimecode:FBTransportTimeFormat
    """Timecode time display mode."""
class FBTriggerStyle(_Enum):
    """Audio clips' trigger styles."""
    kFBTriggerStyleContinue:FBTriggerStyle
    """Previously triggered clips that are still playing won't be stopped and mixing will occur."""
    kFBTriggerStyleCut:FBTriggerStyle
    """Previously triggered clips that are still playing will be stopped."""
    kFBTriggerStyleToggle:FBTriggerStyle
    """If a previously triggered clip is playing, it will only be stopped, otherwise a new starts playing. No mixing and no loop."""
class FBUpAxis(_Enum):
    """This enumeration indicates which up axis is used in the motion file (so far, only effective when loading c3d files)."""
    kFBUpAxisY:FBUpAxis
    """Use the Y-axis as the up axis."""
    kFBUpAxisZ:FBUpAxis
    """Use the Z-axis as the up axis."""
class FBUseChnMode(_Enum):
    """Use Channel modes."""
    kFBUseChannelBoth:FBUseChnMode
    """Default mode, where each channel play in its respective speaker."""
    kFBUseChannelLeftOnly:FBUseChnMode
    """Left channel will be played in both speakers."""
    kFBUseChannelRightOnly:FBUseChnMode
    """Right channel will be played in both speakers."""
class FBVideoCodecMode(_Enum):
    """Enum FBVideoRenderDepth.
    See sample: render.py."""
    FBVideoCodecAsk:FBVideoCodecMode
    """Pop codec selection dialog each render."""
    FBVideoCodecStored:FBVideoCodecMode
    """Pop dialog and stored its value"""
    FBVideoCodecUncompressed:FBVideoCodecMode
    """Assume uncompressed codec."""
class FBVideoFormat(_Enum):
    """Video color modes."""
    kFBVideoFormat_422:FBVideoFormat
    kFBVideoFormat_ABGR_32:FBVideoFormat
    kFBVideoFormat_ARGB_32:FBVideoFormat
    kFBVideoFormat_Any:FBVideoFormat
    kFBVideoFormat_BGRA_32:FBVideoFormat
    kFBVideoFormat_BGR_16:FBVideoFormat
    kFBVideoFormat_BGR_24:FBVideoFormat
    kFBVideoFormat_Other:FBVideoFormat
    kFBVideoFormat_RGBA_32:FBVideoFormat
    kFBVideoFormat_RGB_24:FBVideoFormat
class FBVideoInterlaceMode(_Enum):
    """Video interlace modes."""
    kFBVideoInterlaceFullFrameEven:FBVideoInterlaceMode
    """Full frame (even field)."""
    kFBVideoInterlaceFullFrameOdd:FBVideoInterlaceMode
    """Full frame (odd field)."""
    kFBVideoInterlaceHalfFrameEven:FBVideoInterlaceMode
    """Half frame (even field)."""
    kFBVideoInterlaceHalfFrameOdd:FBVideoInterlaceMode
    """Half frame (odd field)."""
    kFBVideoInterlaceNone:FBVideoInterlaceMode
    """No interacling."""
class FBVideoLiveType(_Enum):
    """Video Live type."""
    kFBVideoLiveBasic:FBVideoLiveType
    """Basic video input, like webcam and dv camera."""
    kFBVideoLiveDefault:FBVideoLiveType
    """Generic video input, type not specified."""
class FBVideoProxyMode(_Enum):
    """Video proxy modes."""
    kFBVideoProxyAlways:FBVideoProxyMode
    """Always video proxy."""
    kFBVideoProxyNone:FBVideoProxyMode
    """No video proxy."""
    kFBVideoProxyOnPlay:FBVideoProxyMode
    """Video proxy on play."""
class FBVideoRenderDepth(_Enum):
    """Enum FBVideoRenderDepth.
    See samples: render.py, render.py."""
    FBVideoRender24Bits:FBVideoRenderDepth
    """24 bits"""
    FBVideoRender32Bits:FBVideoRenderDepth
    """32 bits"""
    FBVideoRenderDepthCount:FBVideoRenderDepth
    """Depth Count."""
class FBVideoRenderFieldMode(_Enum):
    """Enum FBVideoRenderFieldMode."""
    FBFieldModeCount:FBVideoRenderFieldMode
    """Count."""
    FBFieldModeField0:FBVideoRenderFieldMode
    """Field 0."""
    FBFieldModeField1:FBVideoRenderFieldMode
    """Field 1."""
    FBFieldModeHalfField0:FBVideoRenderFieldMode
    """Half Field 0."""
    FBFieldModeHalfField1:FBVideoRenderFieldMode
    """Half Field 1."""
    FBFieldModeNoField:FBVideoRenderFieldMode
    """No Field."""
class FBVideoRenderViewingMode(_Enum):
    """Enum FBVideoRenderViewingMode."""
    FBViewingModeCount:FBVideoRenderViewingMode
    """Count."""
    FBViewingModeCurrent:FBVideoRenderViewingMode
    """Current."""
    FBViewingModeModelsOnly:FBVideoRenderViewingMode
    """Model Only."""
    FBViewingModeStandard:FBVideoRenderViewingMode
    """Standard."""
    FBViewingModeXRay:FBVideoRenderViewingMode
    """X-Ray."""
class FBVideoResolution(_Enum):
    """Video Resolution (1D)"""
    kFBVideo_RES_1:FBVideoResolution
    kFBVideo_RES_128:FBVideoResolution
    kFBVideo_RES_16:FBVideoResolution
    kFBVideo_RES_1K:FBVideoResolution
    kFBVideo_RES_2:FBVideoResolution
    kFBVideo_RES_256:FBVideoResolution
    kFBVideo_RES_2K:FBVideoResolution
    kFBVideo_RES_32:FBVideoResolution
    kFBVideo_RES_4:FBVideoResolution
    kFBVideo_RES_4K:FBVideoResolution
    kFBVideo_RES_512:FBVideoResolution
    kFBVideo_RES_64:FBVideoResolution
    kFBVideo_RES_8:FBVideoResolution
    kFBVideo_RES_8K:FBVideoResolution
    kFBVideo_RES_FULL:FBVideoResolution
class FBVideoStorageMode(_Enum):
    """Video storage modes."""
    kFBVideoStorageDisk:FBVideoStorageMode
    """Storage on disk."""
    kFBVideoStorageDiskAsync:FBVideoStorageMode
    """Storage on disk async access."""
    kFBVideoStorageMemory:FBVideoStorageMode
    """Storage in memory."""
class FBViewerMode(_Enum):
    """Different viewer modes for the 3D viewer."""
    kFBViewerModeFourWindow:FBViewerMode
    """View four panes."""
    kFBViewerModeOneWindow:FBViewerMode
    """View one pane."""
    kFBViewerModeSchematic:FBViewerMode
    """Schematic view."""
    kFBViewerModeThreeWindow:FBViewerMode
    """View three panes."""
    kFBViewerModeTwoWindow:FBViewerMode
    """View two panes."""
class FBVisibilityState(_Enum):
    """Visibility state."""
    kFBVisibilityAll:FBVisibilityState
    """All objects requested are visible."""
    kFBVisibilityAny:FBVisibilityState
    """Any object requested is visible."""
    kFBVisibilityInvalid:FBVisibilityState
    """Invalid visibility request."""
    kFBVisibilitySome:FBVisibilityState
    """Some objects (at least one, but not all) requested are visible."""
class kDeviceIOs(_Enum):
    kIOPlayModeRead:kDeviceIOs
    kIOPlayModeWrite:kDeviceIOs
    kIOStopModeRead:kDeviceIOs
    kIOStopModeWrite:kDeviceIOs
class kDeviceOperations(_Enum):
    kOpAutoDetect:kDeviceOperations
    kOpDone:kDeviceOperations
    kOpInit:kDeviceOperations
    kOpReset:kDeviceOperations
    kOpStart:kDeviceOperations
    kOpStop:kDeviceOperations
class FBAddRegionParam():
    """This class provide a placeholder to put values necessary to create a Region with FBLayout.AddRegion.
    Each region components: X, Y, Width and Height needs its own FBAddRegionParam. ex: x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,'') y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,'') w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,'') h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,'') mainLyt.AddRegion('main','main', x, y, w, h)"""
    mMult:property
    """Read Property: Multiplier of relative value."""
    mPos:property
    """Read Property: Offset in pixel according depending on the use of FBAddRegionParam (X, Y, W or H)."""
    mRelative:property
    """Read Property: Name of Region to attach relative to."""
    mType:property
    """Read Property: Type of Attachment."""
class FBAudioRenderOptions():
    """Audio Render Options structure.
    Contain options to control how the audio rendering will occur. See sample: AudioRendering.py."""
    BitDepthMode:FBAudioBitDepthMode
    """Property: Bit depth for one sample of audio. 8, 16 and 24 bits available for audio render, 16 bits default."""
    ChannelMode:FBAudioChannelMode
    """Property: Audio render channel number, 1 for Mono(left channel right channel render mixed to one channel), 2 for Stereo(left channel right channel render separately)."""
    OutputFileName:str
    """Property: Audio Render destination file."""
    RateMode:FBAudioRateMode
    """Property: Rate mode for number of samples per second. 44100 hz default,8000, 11025,12000,16000,22050,24000,32000,44100,48000,64000,88200,96000 available for audio render."""
    TimeSpan:FBTimeSpan
    """Property: Start and stop selection time to render."""
class FBBatchOptions():
    """Option parameters for the batch process."""
    Character:property
    """Read Write Property: The character to receive the animation."""
    FrameAnimation:bool
    """Read Write Property: Set timeline start and end time to corespond with the start and end of animation."""
    InputDirectory:str
    """Read Write Property: The directory containning the input files."""
    InputFileFormat:FBBatchFileFormat
    """Read Write Property: File format of the input files."""
    KeepCharacterConstraint:bool
    """Read Write Property: To keep the character constaint when saving."""
    KeepDummyBones:bool
    """Read Write Property: To keep dummy bones."""
    OnContainsBatchTakesAction:FBBatchOnContainsBatchTakes
    """Read Write Property: Action to perform when a scene already contains batch takes while in a batch process."""
    OnTakeExistAction:FBBatchOnTakeExist
    """Read Write Property: Action to perform when a take already exist while in a batch process."""
    OutputDirectory:str
    """Read Write Property: The directory containning the output files."""
    OutputFileFormat:FBBatchFileFormat
    """Read Write Property: File format of the output files."""
    OverwriteScaling:bool
    """Read Write Property: Set the scaling to a default setting of 1.0."""
    PlotToCharacter:bool
    """Read Write Property: To plot the animation on the character."""
    PlotToControlSet:bool
    """Read Write Property: To plot the animation on the control set."""
    ProcessType:FBBatchProcessType
    """Read Write Property: What process should be done? Load, Save or Both."""
    SkeletonFile:str
    """Read Write Property: The Skeleton file (for Acclaim AMC files)."""
    StartAnimationAtZero:bool
    """Read Write Property: Set the time of all loaded files to 0."""
    UseBatchSuffix:bool
    """Read Write Property: Add a batch suffix to the name of the files."""
    UseSingleTake:bool
    """Read Write Property: Use only one take to convert all files."""
    WriteRate:bool
    """Read Write Property: Write frame rate in Acclaim AMC files."""
    WriteTranslation:bool
    """Read Write Property: Write translation animation data included with Acclaim AMC files."""
class FBCallback():
    """This class is used for the internal callback framework and is not meant to be used by clients."""
    Callback:property
    """Read Property: Python callback that will called when the FBCallback is executed."""
    EventType:property
    """Read Property: Event type to which this callback is connected."""
    Wrapper:property
    """Read Property: Pyfbsdk Wrapper that is the owner of the callback."""
class FBCharacterPoseOptions():
    """Stores options for operations on poses.
    This class exposes the object used to store the options for operations on object poses. Before using a FBCharacterPoseOptions, you need to specify the various members of the object. Here are the default values of a FBCharacterPoseOptions object: mCharacterPoseKeyingMode = kFBCharacterPoseKeyingModeFullBody mModelToMatch = NULL mMirrorPlaneType = kFBMirrorPlaneTypeAuto mMirrorPlaneEquation = 1.0, 0.0, 0.0, 0.0 mMirrorPlaneTiltAngle = 90.0 mMirrorPlanePanAngle = 0.0 Flag = kFBCharacterPoseNoFlag You need to change at least the Flag value by using SetFlag() to set how the pose will be pasted; see the FBCharacterPoseFlag enum for the various options."""
    mCharacterPoseKeyingMode:FBCharacterPoseKeyingMode
    """CharacterPoseKeyingMode (FullBody or BodyPart)."""
    mMirrorPlaneEquation:FBVector4d
    """Mirror plane equation (used when mMirrorPlaneType = kFBMirrorPlaneTypeEquation)."""
    mMirrorPlanePanAngle:float
    """Mirror plane pan angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser)."""
    mMirrorPlaneTiltAngle:float
    """Mirror plane tilt angle in degrees (used when mMirrorPlaneType = kFBMirrorPlaneTypeUser)."""
    mMirrorPlaneType:FBMirrorPlaneType
    """Mirror plane type."""
    mModelToMatch:FBModel
    """Model to match."""
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBCharacterPoseFlag)->bool:
        """Get a flag value.
        
        Flag : Flag to get.
        return : Value of the flag."""
        ...
    def SetFlag(self,Flag:FBCharacterPoseFlag,Value:bool):
        """Set a flag value.
        
        Flag : Flag to set.
        Value : Value to set."""
        ...
class FBColor():
    """FBColor class.
    Color vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
    
    
    Slicing is not supported by this object.See samples: LayeredTexture.py, SetAllCamerasBackgroundColor.py, SetAllCamerasBackgroundColorFromCurrentCamera.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py."""
    def CopyFrom(self,arg2:FBColor)->FBColor:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBColor)->bool:...
    def NotEqual(self,arg2:FBColor)->bool:...
class FBColorAndAlpha():
    """FBColorAndAlpha class.
    Color and alpha vector.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    color = FBColorAndAlpha()
    len(color)
    print color[0]
    color[0] = 1.0
    
    
    Slicing is not supported by this object."""
    def CopyFrom(self,arg2:FBColorAndAlpha)->FBColorAndAlpha:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBColorAndAlpha)->bool:...
    def NotEqual(self,arg2:FBColorAndAlpha)->bool:...
class FBComponentList():
    """FBComponentList class.
    This class implements a special sort of list that can only contain instances of FBComponent objects. To users it behaves as a tuple, since it is not possible to add new objects in the list. Only methods or function that uses FBComponentList as argument can insert new objects. Users can query the content of the list with the bracket operator.
    
    >>> # Supported list protocol methods:
    l = FBComponentList()
    len(l)
    print l[0]"""
    def Add(self,arg2:FBComponent):...
    def Clear(self):...
    def GetCount(self)->int:...
    def append(self,arg2:FBComponent):...
    def count(self)->int:...
    def removeAll(self):...
class FBConfigFile():
    """Interface to the application config files.
    This class allows client code to generate, modify and query configuration files. Config files will be automatically created when needed. They will be located in the /bin/config folder or an explicitly specified folder depending on the constructor used. See samples: FBConfigFile.py, ActionScriptMgr.py, ActionScriptMgr.py, KeyboardMapper.py, ShotTrackSetupTool.py."""
    def ClearFile(self):
        """Remove all content from the config file."""
        ...
    def Get(self,SectionName:str,ItemName:str,DefaultValue:str=0)->str:
        """Get an item's value.
        Get an item's value by looking inside a specific section of the config file.
        
        SectionName : Name of the section.
        ItemName : Name of the item.
        DefaultValue : Default value that will be returned if the item is not found.
        return : The value assigned to the item in the specified section of the config file, or the default value if not found."""
        ...
    def GetOrSet(self,SectionName:str,ItemName:str,Value:str,Comment:str=0)->bool:
        """Get a value from the config file and set it if it was not found.
        
        SectionName : Name of the section.
        ItemName : Name of the item.
        Value : Reference the the string that will contain the value of the item. If the item is not found in the file, it will be added with the initial value in this string.
        Comment : Optional parameter that can be used to add a comment.
        return : true if the value was found or added, or false if the item was not found and could not be added to the file."""
        ...
    def Set(self,SectionName:str,ItemName:str,Value:str,Comment:str=0)->bool:
        """Set an item's value.
        Assign a value to an item in the config file. If the item does not exist, it will be created.
        
        SectionName : Name of the section.
        ItemName : Name of the item.
        Value : Value assigned to the item.
        Comment : Optional parameter that can be used to add a comment.
        return : true if the item was written to the config file, false otherwise."""
        ...
class FBConstraintInfo():
    """Constraint information class.
    This data structure is passed to the real-time evaluation callback for a constraint (AnimationNodeNotify())."""
    def GetSnapRequested(self)->bool:
        """Was a 'snap' requested?
        
        return : true if 'snap' was requeststed."""
        ...
    def GetZeroRequested(self)->bool:
        """Was a 'zero' requested?
        
        return : true if 'zero' was requeststed."""
        ...
class FBConstructionOperation():
    """FBConstructionOperation is used to represent an operation in the construction history.
    The operation can be any valid script. Currently, only python scripts are supported.An instance of this class defaults to the correct value in order to add a new construction history. If the workgroup plugin is loaded, the operation will be replicated on all machine within a session."""
    def GetCommandId(self)->int:...
    def GetExecuteAsLocalOperation(self)->bool:...
    def GetLanguage(self)->str:...
    def GetLanguageVersion(self)->int:...
    def GetOrigin(self)->str:...
    def GetScript(self)->str:...
    def SetCommandId(self,commandId:int):
        """SetCommandId Set the operation's Id so that operation transactions can be resolved properly (eg: command 1 should go before command 2).
        Set this to -1 for new operations.
        
        commandId : Command Id. Defaults to -1."""
        ...
    def SetExecuteAsLocalOperation(self,bIsLocal:bool):
        """SetExecuteAsLocalOperation Whether to execute this operation as local or remote.
        If this is set to false (remote) and an operation is sent to the construction history, it will also execute locally on this motionbuilder.
        
        bIsLocal : Defaults to true (local)."""
        ...
    def SetLanguage(self,language:str):
        """SetLanguage Set the script language for this operation.
        Currently only 'python' is supported.
        
        language : Langugage string. Default to construction history's code generator's language (Currently "python")."""
        ...
    def SetLanguageVersion(self,version:int):
        """SetLanguageVersion Set the script language interpreter's version that this operation should be interpreted with.
        
        version : Version number. Defaults to construction history's code generator's version (Currently 1)."""
        ...
    def SetOrigin(self,origin:str):
        """SetOrigin Set operation's original creator.
        For instance 'localhost' or . Should mostly be 'localhost' for new operations.
        
        origin : Operation's Origin. Defaults to "localhost"."""
        ...
    def SetScript(self,script:str):
        """SetScript Set the script content for this operation.
        
        script : Script content as a string. Defaults to empty."""
        ...
class FBDeviceNotifyInfo():
    """Device Input and Output Notification information structure.
    This structure is passed to the real-time device IO callback DeviceIONotify. It furnishes the device callback with the system time, local time, and sync counts for the current device cycle."""
    def GetLocalTime(self)->FBTime:
        """Get local time.
        
        return : Current local time."""
        ...
    def GetSyncCount(self)->int:
        """Return the wanted timer sync count (internal or external)
        
        return : sync count or -1 if no sync is present"""
        ...
    def GetSystemTime(self)->FBTime:
        """Get system time.
        
        return : Current system time."""
        ...
class FBDirMap():
    def Add(self,SourceDir:str,TargetDir:str):
        """Adds an entry in the map.
        Environment variables can be specified for the target path using the syntax. Environment variables are expanded before the paths get added to the map. An error in the formatting of the paths (environment variable tokens) will abort the expansion and both given paths will remained unchanged.
        
        SourceDir : str
        TargetDir : str"""
        ...
    def Clear(self):
        """Clears the map."""
        ...
    def GetCount(self)->int:
        """Returns the number of items in the map."""
        ...
    def GetSource(self,Index:object)->str:
        """Returns the source directory for the element at specified index.
        
        Index : int"""
        ...
    def GetTarget(self,Index:object)->str:
        """Returns the target directory for the element at specified index.
        
        Index : int"""
        ...
    def Map(self,Path:str)->str:
        """Iterates through all the mapped directories.
        If one of the mapped directory's source is found in the given path, that part of the path will be replaced by the mapped directory's target. Only the first occurrence is processed.
        
        Path : The path to process"""
        ...
class FBEvaluateInfo():
    """AnimationNodeNotify evaluation information.
    This structure is passed to the AnimationNodeNotify calls (in Constraints, Devices, and Boxes), giving the connectors information with regards to the start or stop times of the evaluation. In general, only the start time is of interest for the current evaluation cycle. The advantage of the structure is to have a common time for the evaluation of all the elements in the scene."""
    def GetEvaluationID(self)->int:
        """Return the wanted timer sync count (internal or external).
        
        return : sync count or -1 if no sync is present"""
        ...
    def GetLocalTime(self)->FBTime:
        """Return local (scene) time.
        
        return : Local time."""
        ...
    def GetSyncCount(self)->int:
        """Return the wanted timer sync count (internal or external).
        
        return : sync count or -1 if no sync is present"""
        ...
    def GetSystemTime(self)->FBTime:
        """Return system time.
        
        return : System time."""
        ...
    def IsStop(self)->bool:
        """Is local time stopped? (ie: no animation).
        
        return : true if local time is stopped."""
        ...
class FBEvent():
    """Base Event class."""
    Type:int
    """Read Only Property: Type of event."""
class FBEventActivate(FBEvent):
    """Activation event."""
    Data:property
    """Read Write Property: Generic data of event."""
class FBEventClipChange(FBEvent):
    ...
class FBEventConnectionDataNotify(FBEvent):
    """Connection notify event class."""
    Action:FBConnectionAction
    """Read Only Property: Connection's action performed."""
    Plug:FBPlug
    """Read Only Property: The plug involved in the action."""
class FBEventConnectionKeyingNotify(FBEvent):
    Action:FBConnectionAction
    Plug:property
    Property:property
    StartTime:FBTime
    StopTime:FBTime
class FBEventConnectionNotify(FBEvent):
    """Connection notify event class."""
    Action:FBConnectionAction
    """Read Only Property: Connection's action performed."""
    ConnectionType:FBConnectionType
    """Read Only Property: Connection's type."""
    DstPlug:FBPlug
    """Read Only Property: The destination plug involved in the action."""
    NewPlug:FBPlug
    """Read Only Property: New plug created by the action. (Mostly used by merge/replace)"""
    SrcIndex:int
    """Read Only Property: Index of the source in the destination component."""
    SrcPlug:FBPlug
    """Read Only Property: The source plug involved in the action."""
class FBEventConnectionStateNotify(FBEvent):
    """Connection notify event class."""
    Action:FBConnectionAction
    """Read Only Property: Connection's action performed."""
    Plug:FBPlug
    """Read Only Property: The plug involved in the action."""
class FBEventDblClick(FBEvent):
    """Input event class."""
    Selection:int
    """Read Only Property: Id of selection."""
class FBEventDragAndDrop(FBEvent):
    """Drag and drop interface.Event: Global Evaluation pipeline critical timing callback event."""
    Components:property
    """Read Property: List of components drop. (it acces the same data as FBEventDragAndDrop.Get)"""
    Data:property
    """Property: User specified reference. (for example, FBSpread:row)"""
    PosX:int
    """Property: X position of mouse."""
    PosY:int
    """Property: Y position of mouse."""
    State:FBDragAndDropState
    """Property: Drag and drop sub-event."""
    def Accept(self):
        """Accept a drag and drop sequence.
        This will cause the region in question to accept a drag and drop action when this event occurs."""
        ...
    def Add(self,Component:FBComponent,Id:int=0):
        """Add an item to the drag and drop list.
        
        Component : Item to add to the list.
        Id : User-defined reference for the item (default = 0 )."""
        ...
    def Clear(self):
        """Clear drag and drop list."""
        ...
    def Get(self,Index:int)->FBComponent:
        """Get the FBComponent specified byIndex from the Drag and Drop list.
        
        Index : Index in list where to get FBComponent.
        return : Handle to FBComponent in list atIndex."""
        ...
    def GetCount(self)->int:
        """Get the number of items in the DragAndDrop list.
        
        return : Number of items in DragAndDrop list."""
        ...
class FBEventEvalGlobalCallback(FBEvent):
    Timing:property
class FBEventExpose(FBEvent):
    """Event sent when a control needs to be displayed."""
    ...
class FBEventFileChange(FBEvent):
    """File change event class.
    This event occurs every time a monitored file changed:"""
    Path:str
    """Read Only Property: The path of changed file."""
class FBEventInput(FBEvent):
    """Input event class."""
    InputType:FBInputType
    """Read Only Property: Input type."""
    Key:int
    """Read Only Property: Input key."""
    KeyState:int
    """Read Only Property: State of key."""
    MouseButton:int
    """Read Only Property: Mouse Button."""
    X:int
    """Read Only Property: Mouse X Position."""
    Y:int
    """Read Only Property: Mouse Y Position."""
class FBEventMenu(FBEvent):
    """Menu event."""
    Id:int
    """Read Write Property: Id number for menu item."""
    Name:str
    """Read Write Property: Name of menu item."""
class FBEventOverrideFileOpen(FBEvent):
    """Event that is called before a file open/merge."""
    FilePath:str
    """Read Only Property: Path to the file that will be opened/merged."""
    WillOverride:bool
    """Read Write Property: Set to true for handling the file load, false by default. If the return value is false, MotionBuilder will proceed with the normal file open/merge process."""
class FBEventPlayerControlChange(FBEvent):
    ...
class FBEventResize(FBEvent):
    """Event sent to a control that resizes."""
    Height:int
    """Property: New Height of the window."""
    Width:int
    """Property: New Width of the window."""
class FBEventSceneChange(FBEvent):
    """Select model event class.
    This event occurs every time a model is:(un)selectedaddeddestroyedrenamed, etc.."""
    ChildComponent:FBComponent
    """Read Only Property: Child component of the event."""
    Component:FBComponent
    """Read Only Property: Modified component"""
class FBEventShow(FBEvent):
    """Show event class."""
    Shown:bool
    """Read Only Property: Was layer just shown?"""
class FBEventSpread(FBEvent):
    """Spreadsheet event."""
    Action:int
    """Read Only Property: Action associated to the spread event."""
    Column:int
    """Read Only Property: Column of event."""
    Row:int
    """Read Only Property: Row of event."""
class FBEventTakeChange(FBEvent):
    """Take change event class.
    This event occurs every time a take is:addeddestroyedrenamedselected, etc."""
    Take:FBTake
    """Read Only Property: The take modified."""
class FBEventTransaction(FBEvent):
    """Transaction event."""
    IsBeginTransaction:bool
    """Read Only Property: Tells if the transaction is at begin."""
class FBEventTree(FBEvent):
    """FBTree node event."""
    TreeNode:FBTreeNode
    """Read Write Property: Tree node."""
    Why:property
    """Read Write Property: Reason of the event."""
class FBEventTreeSelect(FBEvent):
    """FBTree selection event.Event: Video Frame offline Rendering Event."""
    TreeNode:FBTreeNode
    """Read Write Property: Selected tree node."""
class FBEventVideoFrameRendering(FBEvent):
    EState:_Enum
    FrameCount:int
    FrameNumber:int
    State:EState
    eBeginRendering:EState
    eEndRendering:EState
    eRendering:EState
class FBFCurveEvent(FBEvent):
    """This class is used when a modification is made on a FCurve.
    It contains the necessary information to identify the owner of the curve and what modification was made."""
    Curve:FBFCurve
    """Read Only Property: Curve that will receive the new key."""
    CurveIndex:int
    """Read Only Property: Index of curve."""
    CurveName:str
    """Read Only Property: Name of curve."""
    EventType:FBFCurveEventType
    """Read Only Property: Type of fcurve event."""
    KeyIndexStart:int
    """Read Only Property: Index of the first key which is involved in the event."""
    KeyIndexStop:int
    """Read Only Property: Index of the last key which is involved in the event."""
    ParentAnimationNode:property
    ParentComponent:property
    ParentProperty:property
class FBFCurveKey():
    """KeyFrame for an FCurve.
    See sample: StartKeysAtCurrentTime.py."""
    Bias:float
    """Read Write Property: Bias (TCB)."""
    Continuity:float
    """Read Write Property: Continuity (TCB)."""
    ExtrapolationMode:FBExtrapolationMode
    """Read Write Property: Extrapolation mode"""
    Interpolation:FBInterpolation
    """Read Write Property: Type of interpolation."""
    LeftBezierTangent:float
    """Read Write Property: Left bezier tangent"""
    LeftDerivative:float
    """Read Write Property: Left derivative, in units/seconds."""
    LeftTangentWeight:float
    """Read Write Property: Left tangent weight"""
    MarkedForManipulation:bool
    """Read Write Property: Is the key marked for manipulation."""
    RightBezierTangent:float
    """Read Write Property: Right bezier tangent"""
    RightDerivative:float
    """Read Write Property: Right derivative, in units/seconds."""
    RightTangentWeight:float
    """Read Write Property: Right tangent weight"""
    Selected:bool
    """Read Write Property: Is the key selected."""
    TangentBreak:bool
    """Read Write Property: Tangent's break status"""
    TangentClampMode:FBTangentClampMode
    """Read Write Property: Tangent's clamp method."""
    TangentConstantMode:FBTangentConstantMode
    """Read Write Property: Tangent's constant mode"""
    TangentCustomIndex:FBTangentCustomIndex
    """Read Write Property: Tangent's custom index"""
    TangentMode:FBTangentMode
    """Read Write Property: Tangent calculation method."""
    TangentWeightMode:FBTangentWeightMode
    """Read Write Property: Tangent's weight mode. Setting the value for LeftTangentWeight/RightTangentWeight will also activate the weight for that part. Please see the note provided with FBTangentWeightMode for the left weight of a key."""
    Tension:float
    """Read Write Property: Tension (TCB)."""
    Time:FBTime
    """Read Write Property: Time of key."""
    Value:float
    """Read Write Property: Value of Key"""
class FBFilePopup():
    """File Popup (for open/save).
    See samples: AudioTrackSetupTool.py, FBFilePopup.py."""
    Caption:str
    FileName:str
    """Read Write Property: File selected."""
    Filter:str
    """Read Write Property: Filter to use for popup window file selection."""
    FullFilename:str
    """Read Only Property: Full filename (path and file)."""
    Path:str
    """Read Write Property: Path of file selected."""
    Style:FBFilePopupStyle
    """Read Write Property: Style of file popup."""
    def Execute(self)->bool:
        """Execute file popup.
        
        return : true if OK is clicked by user."""
        ...
class FBFilterManager():
    """Filter manager.
    This class provides list of all available filter types and a factory method in order to create an instance of the desired filter type.This manager will list both built-in and plug-in filters.See the class FBFilter for more details.Filter type names are not localised, and are the same as presented in the GUI.The following sample code shows how to use C++ or Python to create an instance of the orfilter_template filter and set one of its property. For the sample code to work, the plugin must have been compiled and copied in the plugins folder prior to the application startup.Sample C++ code:
    
    >>> # Create a filter of a known type. In this case the sample filter
    # provided with the samples: orfilter_template.
    FBFilterManager lFilterManager;
    FBFilter* lFilter = lFilterManager.CreateFilter( 'OR - Filter Template' );
    # Set one of the filter property:
    FBPropertyDouble* lPropDouble = (FBPropertyDouble*)lFilter->PropertyList.Find( 'Test Double' );
    if( lPropDouble )
    {
    (*lPropDouble) = 2.0;
    }
    # Now we can apply the filter on an FCurve.
    # ...
    # And when we are done, destroy it.
    lFilter->FBDelete();
    lFilter = NULL;
    
    
    Sample Python code:
    
    >>> from pyfbsdk import *
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
    lFilter.FBDelete()"""
    FilterTypeNames:FBStringList
    """List of available filters."""
    def CreateFilter(self,FilterTypeName:str)->FBFilter:
        """Create a filter instance according to the filter type requested.
        
        FilterTypeName : String describing the type of the desired filter, as obtained from list FilterTypeNames.
        return : A pointer to a filter instance, or a NULL if the type name was invalid."""
        ...
class FBFolderPopup():
    """Folder Popup (for selecting a directory).
    See samples: RenderLayers.py, BatchExportCharacterAnimationTool.py, RenameFirstTakeOnMultipleFiles.py, FBFolderPopup.py."""
    Caption:str
    Path:str
    """Read Write Property: Path of folder selected."""
    def Execute(self)->bool:
        """Execute folder popup.
        
        return : true if OK is clicked by user."""
        ...
class FBMatrix():
    """FBMatrix class.
    Four x Four (double) Matrix.This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 16 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    mat = FBMatrix()
    len(mat)
    print mat[13]
    mat[12] = 1.0
    
    
    The implementation of this 4x4 matrix uses a simple list of 16 elements, not a list of 4 vectors of 4 elements.* Slicing is not supported by this object.See sample: Matrix.py."""
    def CopyFrom(self,arg2:FBMatrix)->FBMatrix:...
    def GetBufferAddress(self)->int:...
    def Identity(self):
        """Load identity matrix."""
        ...
    def Inverse(self)->FBMatrix:
        """Get Inversed matrix.
        
        return : the matrix Inversed."""
        ...
    def InverseProduct(self,Matrix:FBMatrix)->FBMatrix:
        """InverseProduct Matrix.
        
        Matrix : Matrix to Product.
        return : result matrix."""
        ...
    def IsEqual(self,arg2:FBMatrix)->bool:...
    def NotEqual(self,arg2:FBMatrix)->bool:...
    def Set(self,Value:float):
        """Set matrix from an array.
        
        Value : Array to intialize matrix from."""
        ...
    def Transpose(self)->FBMatrix:
        """Get Transposed matrix.
        
        return : the matrix Transposed."""
        ...
    def Validate(self)->bool:
        """Validated matrix.
        
        return : true if matrix Validated."""
        ...
class FBModelList():
    """FBModelList class.
    This class implements a special sort of list that can only contain instances of FBModel objects. Users can query the content of the list with the bracket operator.
    
    >>> # Supported list protocol methods:
    l = FBModelList()
    len(l)
    print l[0]"""
    def Add(self,Model:FBModel):
        """Append a new modle at the end of the list.
        
        Model : model to add to the list."""
        ...
    def Clear(self):
        """Empty the list from all models."""
        ...
    def GetCount(self)->int:
        """Get number of models in list."""
        ...
    def GetModel(self,Index:object)->object:
        """Get the ith model in list.
        
        Index : index of modle to get (0 based).
        return : TheIndex model"""
        ...
    def append(self,Model:FBModel):
        """Append a new modle at the end of the list.
        
        Model : model to add to the list."""
        ...
    def count(self)->int:
        """Get number of models in list."""
        ...
    def removeAll(self):
        """Empty the list from all models."""
        ...
class FBMultiLangManager():
    """Language manager.
    The class FBMultiLangManager indicates the supported languages and allows to query and change the current language.The support for localization is done using conversion tables from internal names to language specific names, so that they can be used in the GUI and other human readable contexts.At this time, changing the current language will not affect the GUI. Only calls to functions 'FBGetMultiLangText()' will be affected.The following sample code lists the names of the supported languages:Python sample code:
    
    >>> from pyfbsdk import *
    lManager = FBMultiLangManager()
    print 'Current localization language: ', lManager.GetCurrentLanguage()
    print 'Supported languages:'
    for lLanguage in lManager.Languages:
    print '  ', lLanguage
    
    
    C++ sample code:
    
    >>> FBMultiLangManager lManager;
    FBTrace( 'Current localization language: %s
    ', lManager.GetCurrentLanguage());
    FBTrace( 'Supported languages:
    ' );
    int lIdx = 0;
    while( lIdx < lManager.Languages.GetCount())
    {
    FBTrace( '  %s
    ', lManager.Languages[lIdx++] );
    }"""
    Languages:FBStringList
    """List of available languages."""
    def GetCurrentLanguage(self)->str:
        """Obtain the current language.
        Query the current language used for the GUI.
        
        return : Will return the string associated with the current language used."""
        ...
    def SetCurrentLanguage(self,Language:str)->bool:
        """Set the current language.
        Change the current language to another available language.
        
        Language : The string corresponding to the desired language, as defined in property Languages.
        return : Indicate if the change of language was successful."""
        ...
class FBNormal():
    def CopyFrom(self,arg2:FBNormal)->FBNormal:...
    def CrossProduct(self,arg2:FBNormal)->FBNormal:...
    def DotProduct(self,arg2:FBNormal)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBNormal)->bool:...
    def Length(self)->float:...
    def Normalize(self)->FBNormal:...
    def NotEqual(self,arg2:FBNormal)->bool:...
    def SquareLength(self)->float:...
class FBObjectPoseMirrorOptions():
    """FBObjectPoseMirrorOptions class.
    This class exposes the object used to store the options for the mirror of an object pose."""
    mMirrorPlaneEquation:FBVector4d
    """Equation of the mirror plane."""
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBObjectPoseMirrorOptionsFlag)->bool:
        """Get a flag value.
        
        Flag : Flag to get.
        return : Value of the flag."""
        ...
    def SetFlag(self,Flag:FBObjectPoseMirrorOptionsFlag,Value:bool):
        """Set a flag value.
        
        Flag : Flag to set.
        Value : Value to set."""
        ...
class FBObjectPoseOptions():
    """FBObjectPoseOptions class.
    This class exposes the object used to store the options for operations on object poses."""
    mPoseTransformType:FBPoseTransformType
    """Transform type (Local, Global or LocalRef)."""
    mReferenceGRM:FBMatrix
    """Global rotation matrix of reference object."""
    mReferenceGSM:FBMatrix
    """Global scaling matrix of reference object."""
    mReferenceGT:FBVector3d
    """Global translation vector of reference object."""
    def ClearFlag(self):
        """Clear all flags."""
        ...
    def GetFlag(self,Flag:FBObjectPoseOptionsFlag)->bool:
        """Get a flag value.
        
        Flag : Flag to get.
        return : Value of the flag."""
        ...
    def SetFlag(self,Flag:FBObjectPoseOptionsFlag,Value:bool):
        """Set a flag value.
        
        Flag : Flag to set.
        Value : Value to set."""
        ...
class FBPickInfosList():
    """FBPickInfosList class.
    This class implements a special sort of list that can only contains a pick info which is a tuple<FBModel, FBVector3d>. A pick info give the position (FBVector3d) and the model (FBModel) that was pick on screen.To users FBPickInfosList behave like a typle, since it is not possible to add new objects in the list. Only methods or function that uses FBPickInfosList as argument can insert new objects. Users can query the content of the list with the bracket operator.
    
    >>> # Supported list protocol methods:
    l = FBPickInfosList()
    len(l)
    # tuple unpacking of pick infos.
    model, vector = l[0]"""
    def GetCount(self)->int:...
    def GetPickedModel(self,arg2:object)->object:...
    def count(self)->int:...
class FBPlotOptions():
    """Option parameters for plotting.
    See samples: PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py."""
    ConstantKeyReducerKeepOneKey:bool
    """Read Write Property: Should the constant key reducer keep at least one key?"""
    EvaluateDeformation:bool
    """Read Write Property: Should we evaluate deformation while plotting? This is useful when there is a dependency with the deformation. Disabled by default."""
    PlotAllTakes:bool
    """Read Write Property: Should we plot all takes?"""
    PlotAuxEffectors:bool
    """Read Write Property: Should we plot aux effectors?"""
    PlotLockedProperties:bool
    """Read Write Property: Should we plot locked properties?"""
    PlotOnFrame:bool
    """Read Write Property: Should we plot on frame?"""
    PlotPeriod:FBTime
    """Read Write Property: The plot period (1/fps)."""
    PlotTangentMode:FBPlotTangentMode
    """Read Write Property: The tangent mode for plotted curve."""
    PlotTranslationOnRootOnly:bool
    """Read Write Property: Should we plot the translation on root only?"""
    PreciseTimeDiscontinuities:bool
    """Read Write Property: Should we use precise time discontinuities?"""
    RotationFilterToApply:FBRotationFilter
    """Read Write Property: The rotation filter to apply."""
    UseConstantKeyReducer:bool
    """Read Write Property: Should we use a constant key reducer with the filter?"""
class FBPlugList():
    def GetCount(self)->int:...
class FBProfileTaskCycle():
    """FBProfileTaskCycle.
    Real-time profiling information for a specific task. Profiling information can be collected for:Evaluation: models, constraints, characters, story tracksDevices: DeviceIONotify, DeviceEvaluationNotifyRendering: renderer, render passes (like: Translucent, TranslucentZSort, Selected, OtherPrimitive, SelectiveLighting, etc)SDKInternal synchronization (idle callback, buffer swap, waiting on evaluation to finish before starting new rendering)When profiling a scene within a MotionBuilder session you can discover what tasks are being performed when and for how long. You can use this information to troubleshoot lengthy or repetitive actions, and use MotionBuilder more efficiently.A task is defined as a definite piece of work within MotionBuilder such as the evaluation of a character. If the same task is run numerous times it is called a task cycle. From within a scene, the hierary and dependents of the scene make up the task cycles. A task cycle spends its time computing a specific task within a task parent cycle.A task parent cycle is a hierarchy of individual task cycles, where the parent and child relationship is known to MotionBuilder and displayed in the profiling center.For example, these are all task cycles which are all parented to each other; Eval is parent of TransformNode_Active, which is a parent of Constraint, which is a parent of Character, which is in turn a parent of TransformNode_Active.This is because the evaluation is called for one model which triggers evaluation of the character which then calls the evaluation of the rest of IK/FK models.When an evaluation starts, it calls the evaluation of the character, the time will be computed for time spent on the sample. Then possibly another character is evaluated, so again the time will be computed for the time spent on this sample. This time will be added to the previous sample since that evaluation has not finished yet. The evaluation here is parented, since they both have started but not finished, all children samples are summed. When the evaluation stops, you change the sample for the children.Note: The evaluation dependency/order will be different for each scene.As you can see profiling of task cycles is done by collecting samples. Samples are added to one inside parent sample. The number of samples collected is controlled by the profiler buffer size property.Here are the steps to add profiling into a constraint, a device, or any other class that uses real-time evaluation: 1) Declare FBProfiler_CreateTaskCycle( MyConstraint, 0.5, 0.5, 0.5 ) in MyConstraint.cxx, before the constructor and AnimationNodeNotify function. 2) Set up FBProfiling_SetupTaskCycle( MyConstraint ) in the constuctor MyConstraint::MyConstraint(). 3) At the beginning of MyConstraint::AnimationNodeNotify create the variable: FBProfilerHelper lProfiling( FBProfiling_TaskCycleIndex( MyConstraint ),EvaluateInfo ); The sample for task will start at the creation of FBProfilerHelper object and stop at the destruction of this object, when returning from AnimationNodeNotify will be done."""
    def GetAvgMinMaxUsage(self)->tuple:
        """Get the task cycle's average, minimum and maximum usage.
        Results will vary on buffer size. When profiling is disabled all values are set to 1.
        
        Avg : Average time spend for computation of task (in micro seconds).
        Min : Minimum time spend for computation of task (in micro seconds).
        Max : Maximum time spend for computation of task (in micro seconds)."""
        ...
    def GetChild(self,Index:int)->FBProfileTaskCycle:
        """Get child task based on specific index.
        Can return NULL if child index is not used.
        
        Index : Child index.
        return : Child at given index."""
        ...
    def GetChildCount(self)->int:
        """Get number of child tasks.
        Task cycles are organized in a hierarchy which is dependent on the scene. Samples can be cumulative in the parent task cycle, or independent. For example, all character evaluation samples will be cumulated in one evaluation cycle.
        
        return : Number of child tasks."""
        ...
    def GetColor(self)->FBColor:
        """Get the color of the task cycle.
        Used in profiling Center for drawing."""
        ...
    def GetIndex(self)->int:
        """Get the unique registration index for each cycle."""
        ...
    def GetName(self)->str:
        """Get the name of task cycle."""
        ...
    def IsStarted(self)->bool:
        """Test to see if sampling has started."""
        ...
class FBProfileTimeEvent():
    """FBProfileTimeEvent.
    Time event information is collected during sampling (activated with a property in FBProfiler ActiveSampling). Events that can be collected are: render, evaluation, model evaluation, model deformation, synchronization of evaluation and rendering, playback commands, etc.Sampling will stop when the buffers maximum size is reached (maximum is 10MB).Currently users are not able to register any new events from ORSDK/python"""
    def GetColor(self)->FBColor:
        """Get the color assigned to the event."""
        ...
    def GetComment(self)->str:
        """Get the comment for the event.
        Comments are not editable."""
        ...
    def GetThreadID(self)->int:
        """Get the thread ID used in the event execution."""
        ...
    def GetTime(self)->FBTime:
        """Get the time when the event occurred."""
        ...
    def GetTypeName(self)->str:
        """Get the event registered type name."""
        ...
    def IsSingleEvent(self)->bool:
        """Three types of events exits: single, start and end.
        Some actions that takes more time to execute or when other events can occur inbetween are collected with start time event at begin and end time event at finish."""
        ...
class FBPropertyListAnimationNode():
    """List of animation nodes.List: AudioClip"""
    def FindByLabel(self,NodeLabel:str)->FBAnimationNode:
        """Returns the animation node from its label.
        
        NodeLabel : Label of the searched animation node.
        return : AnimationNode found."""
        ...
class FBPropertyListDeviceInstrument():
    """List of instruments.PropertyList: Device optical marker"""
    ...
class FBPropertyListDeviceOpticalMarker():
    ...
class FBPropertyListFCurveKey():
    """List of FCurveKey.List: FileReference"""
    ...
class FBPropertyListManipulator():
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListMarkerSegment():
    """PropertyList: MarkerSet.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListModelMarkerOptical():
    """PropertyList: ModelOptical."""
    ...
class FBPropertyListModelTemplate():
    """PropertyList: ModelTemplateBinding."""
    ...
class FBPropertyListModelTemplateBinding():
    """List: MotionClip  PropertyList: MotionClip"""
    ...
class FBPropertyListOpticalGap():
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListOpticalSegment():
    """PropertyList: Physical properties"""
    ...
class FBPropertyListRigidBody():
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListRigidBodyMarkers():
    """List: Set"""
    ...
class FBPropertyManager():
    """Property Manager.
    The property manager exists in all FBComponent objects, and contains an array of all the registered properties. These properties may be SDK properties, internal properties or both."""
    def Find(self,PropertyName:str,MultilangLookup:bool=True)->FBProperty:
        """Find a property, based on its name.
        
        PropertyName : Name of property to look for.
        MultilangLookup : When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true)
        return : Handle to property found."""
        ...
    def FindPropertiesByName(self,PropertyNamePattern:str,PropList:List[FBProperty],MultilangLookup:bool=True):
        """This function will query the property list for properties fulfilling a particular name pattern.
        
        PropertyNamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene )
        PropList : List that contains the resulting properties matching the pattern
        MultilangLookup : When searching, indicate if the name lookup should also be done on the property name as shown in the GUI. (default = true)"""
        ...
class FBPropertyStateEvent(FBEvent):
    """This class is used when the state of a property tracked by the FBFCurveEventManager is changed."""
    EventType:FBPropertyStateEventType
    """Read Only Property: Event type, please see the FBPropertyStateEventType for the possible types."""
    ParentComponent:property
    Property:property
class FBPropertyViewDefinition():
    """FBProperty View.
    View definition for one property."""
    def IsFolder(self)->bool:
        """Is view a folder."""
        ...
    def IsOpen(self)->bool:
        """Is property view open at run time."""
        ...
    def IsSaved(self)->bool:
        """Is property view saved on view manager store."""
        ...
    def SetOpen(self,bState:bool,ApplyUpHierarchy:bool):
        """Set view open/closed at run time.
        
        True : bool
        ApplyUpHierarchy : bool"""
        ...
    def SetSaved(self,bState:bool,ApplyUpHierarchy:bool):
        """Set view to be saved on view manager store.
        
        True : bool
        ApplyUpHierarchy : bool"""
        ...
class FBPropertyViewList():
    """FBProperty View List.
    Hold list of description for view set."""
    def AddPropertyView(self,Property:FBProperty,Hierarchy:str)->FBPropertyViewDefinition:
        """Add property view.
        
        Property : Property to add.
        Hierarchy : Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation").
        return : created object (should not be called on non editable view list)."""
        ...
    def FindPropertyView(self,PropertyName:str)->FBPropertyViewDefinition:
        """Find property view forPropertyName in this list.
        
        PropertyName : str"""
        ...
    def IsEditable(self)->bool:
        """Is property view list editable."""
        ...
    def RemovePropertyView(self,PropertyViewDefinition:FBPropertyViewDefinition)->bool:
        """Remove property view from view list.
        
        PropertyViewDefinition : Property view definition to destroy.
        return : true whenPropertyViewDefinition got removed and free (should not be called on non editable view list)."""
        ...
class FBPythonWrapper():
    """Base class of FBPlug in Python.
    This class act as a bridge between the ORSDK C++ world and the Python world. Since each Python objects wrap a ORSDK object we need a way to notify Python if the ORSDK object is destroyed.OnUnbind is used in this way: it notifies the user when the wrapped ORSDK objects is destroyed."""
    OnUnbind:property
    """Event: Will notifier the user when the corresponding ORSDK objects is unbound from the PythonObject."""
class FBPlug(FBPythonWrapper):
    """Connections Basic Open Reality SDK Element.
    Most elements that are available in the SDK inherit from this base class since FBComponent and FBProperty inherit from FBPlug. Basically, all objects can be connected together because they are all 'plugs'. To simplify the graph, you can think of a 'source' connection as a child, and a 'destination' connection as a parent. Also, it is correct to assume that a source affect/work on its destination. For example, a shader applied on an object would be seen as the source while the object is the destination. So FBPlug is a set of functions that enables you to control those connections with flexibility and ease. See samples: FBConstraintManager.py, FBFolder.py."""
    ClassGroupName:str
    """ClassGroupName of the object."""
    TypeInfo:int
    """TypeInfo."""
    def BeginChange(self)->bool:...
    def ClassName(self)->str:...
    def ConnectDst(self,Dst:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:...
    def ConnectDstAt(self,Src_DstIndex:int,Dst:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:...
    def ConnectSrc(self,Src:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:...
    def ConnectSrcAt(self,Dst_SrcIndex:int,Src:FBPlug,ConnectionType:FBConnectionType=FBConnectionType.kFBConnectionTypeNone)->bool:...
    def DisconnectAllDst(self):...
    def DisconnectAllSrc(self):...
    def DisconnectDst(self,Dst:FBPlug)->bool:...
    def DisconnectDstAt(self,Index:int)->bool:...
    def DisconnectSrc(self,Src:FBPlug)->bool:...
    def DisconnectSrcAt(self,Index:int)->bool:...
    def EndChange(self):...
    def GetContentModified(self,Flag:FBPlugModificationFlag)->bool:...
    def GetDst(self,Index:int)->FBPlug:...
    def GetDstCount(self)->int:...
    def GetDstType(self,Index:int)->FBConnectionType:...
    def GetOwned(self,Index:int)->FBPlug:...
    def GetOwnedCount(self)->int:...
    def GetOwner(self)->FBPlug:...
    def GetPlugConnectionModifiedList(self,PlugList:FBPlugList,ConnectionModificatonFlag:FBPlugModificationFlag,AddRemove:bool)->int:...
    def GetSelfModified(self,Flag:FBPlugModificationFlag)->bool:...
    def GetSrc(self,Index:int)->FBPlug:...
    def GetSrcCount(self)->int:...
    def GetSrcType(self,Index:int)->FBConnectionType:...
    def GetStatusFlag(self,Status:FBPlugStatusFlag)->bool:...
    def Is(self,TypeId:int)->bool:...
    def IsSDKComponent(self)->bool:...
    def MoveSrcAt(self,Index:int,AtIndex:int)->bool:...
    def PrintClassDefinitions(self):...
    def ReplaceDstAt(self,Index:int,Dst:FBPlug)->bool:...
    def ReplaceSrcAt(self,Index:int,Src:FBPlug)->bool:...
    def RevertModification(self,Flag:FBPlugModificationFlag=FBPlugModificationFlag.kFBAllModifiedMask)->bool:...
    def SetContentModified(self,Flag:FBPlugModificationFlag,Bool:bool):...
    def SetSelfModified(self,Flag:FBPlugModificationFlag,Bool:bool):...
    def SetStatusFlag(self,Status:FBPlugStatusFlag,Value:bool):...
    def SwapSrc(self,IndexA:int,IndexB:int)->bool:...
class FBRenderOptions():
    def GetIDBufferPickingAlphaThreshold(self)->float:
        """Get IDBuffer Picking Alpha threshold.
        
        return : ID Buffer picking alpha threshold value."""
        ...
    def GetRenderFrameId(self)->int:
        """Get Render Frame ID.
        
        return : This return a new ID each time a new frame is drawn."""
        ...
    def GetRenderingCamera(self)->object:
        """Get the rendering camera."""
        ...
    def GetViewerOptions(self)->FBViewingOptions:...
    def IsIDBufferPicking(self)->bool:...
    def IsIDBufferRendering(self)->bool:
        """Get IDBuffer Rendering request status (for display or picking)
        
        return : true if need to render Model (or subitem)'s UniqueColorID into GL Color Buffer."""
        ...
    def IsOfflineRendering(self)->bool:
        """Check if the render request comes from offline render mode (as opposed to viewport refresh).
        
        return : true if the render comes from offline render mode."""
        ...
class FBProperty(FBPlug):
    """Generic application property.
    Property: Action Action property to trigger function.FBProperty objects cannot be instantiated by the user. Reference to a property can be obtained either via an instance of a FBComponent object, or by calling the method 'Find()' of a FBPropertyManager. The class FBComponent has a FBPropertyManager data member named 'PropertyList'.When accessing a FBProperty object via its containing object, you can get or set (assuming it is not read-only) its value directly:    lObject.Visibility = TrueWhen accessing a property reference directly, its value is obtained via it's 'Data' member.    lProp = lObject.PropertyList.Find( 'Visibility' )   if lProp: lProp.Data = TrueThe methods 'PropertyCreate()' and 'PropertyRemove' of the class FBComponent can be used to modify an object's set of properties."""
    Data:property
    """Read Write Property: The property data value. Type of this depends on the subclass of FBProperty (ex: in a FBPropertyInt, Data is of type int)."""
    Name:property
    """Read Property: The property's name."""
    def AllowsLocking(self)->bool:
        """AllowsLocking.
        
        return : true if property can be locked"""
        ...
    def AsString(self,Flag:FBDataAsStringFlag=FBDataAsStringFlag.kFBDataAsStringUI)->str:
        """Get the property value as a string.
        
        Flag : Indicates the returned string to be used for UI or storage. It defaults to kFBDataAsStringUI.
        return : The string version of the property."""
        ...
    def EnumList(self,Index:int)->str:
        """Return the string of an enum value.
        
        Index : Enum value to get string for.
        return : String value of enum specified byIndex."""
        ...
    def GetEnumStringList(self,CreateIt:bool=False)->FBStringList:
        """String list for enum properties.
        
        CreateIt : Create a new list if necessary.
        return : the pointer to the string list.."""
        ...
    def GetMax(self)->float:
        """GetMax.
        
        return : Maximum value for the property."""
        ...
    def GetMin(self)->float:
        """GetMin.
        
        return : Minimum value for the property."""
        ...
    def GetName(self)->str:
        """Get the property's name.
        
        return : The property's name."""
        ...
    def GetPropertyFlag(self,Flag:FBPropertyFlag)->bool:
        """GetPropertyFlag.
        
        Flag : Flag to test if it is True or False.
        return : If the flag is True, the function returns True and vice-versa."""
        ...
    def GetPropertyFlags(self)->FBPropertyFlag:
        """GetPropertyFlags.
        
        return : Return all flags at once."""
        ...
    def GetPropertyType(self)->FBPropertyType:
        """Get the property's type.
        
        return : The property's type."""
        ...
    def GetPropertyTypeName(self)->str:
        """Get the property's type name.
        
        return : The property's type name."""
        ...
    def GetReferencedProperty(self)->FBProperty:
        """Get the referenced property, in the case of this property is a reference property (see the IsReferenceProperty() method).
        
        return : The referenced property, or a null pointer if this property is not a reference property."""
        ...
    def GetSubMemberCount(self)->int:
        """GetSubMemberCount.
        
        return : Number of sub-members."""
        ...
    def HasSomethingLocked(self)->bool:
        """HasSomethingLocked.
        
        return : true if property or any of its members is locked"""
        ...
    def IsAnimatable(self)->bool:...
    def IsInternal(self)->bool:...
    def IsList(self)->bool:
        """Verify if property is of this type.
        
        return : true if property is of type."""
        ...
    def IsLocked(self)->bool:
        """IsLocked.
        
        return : true if property is locked"""
        ...
    def IsMaxClamp(self)->bool:
        """Indicate if maximum value clamping will be applied on user input value.
        
        return : true if property the value will be clamped to a maximum value."""
        ...
    def IsMemberLocked(self,Index:int)->bool:
        """IsMemberLocked.
        
        Index : Index of the sub-member of the property to check.
        return : true if property sub-member is locked"""
        ...
    def IsMinClamp(self)->bool:
        """Indicate if minimum value clamping will be applied on user input value.
        
        return : true if property the value will be clamped to a minimum value."""
        ...
    def IsObjectList(self)->bool:
        """Indicate if is an instance of FBPropertyListObject."""
        ...
    def IsReadOnly(self)->bool:
        """Is property read-only?
        
        return : true if property is read-only."""
        ...
    def IsReferenceProperty(self)->bool:...
    def IsTextureConnectableProperty(self)->bool:...
    def IsUserProperty(self)->bool:...
    def ModifyPropertyFlag(self,Flag:FBPropertyFlag,Value:bool):
        """ModifyPropertyFlag.
        
        Flag : The flag to switch to True or False.
        Value : The value to set about this flag."""
        ...
    def NotifyEnumStringListChanged(self):
        """Notify system that the enum list was modified."""
        ...
    def OriValueAsString(self)->str:
        """Get the property original value (before any modification) as string.
        
        return : returns the original value of the property in string with format same as AsString(kDataAsStringPersistence)"""
        ...
    def SetLocked(self,Locked:bool):
        """SetLocked.
        
        Locked : True if the property is to be locked, false if it is to be unlocked."""
        ...
    def SetMax(self,Max:float,ForceMaxClamp:bool=False):
        """SetMax.
        
        Max : Maximum value of the property.
        ForceMaxClamp : Force clamping to maximum value of the property."""
        ...
    def SetMemberLocked(self,Index:int,Locked:bool):
        """SetMemberLocked.
        
        Index : Index of the sub-member of the property to lock or unlock.
        Locked : True if the sub-member is to be locked, false if it is to be unlocked."""
        ...
    def SetMin(self,Min:float,ForceMinClamp:bool=False):
        """SetMin.
        
        Min : Minimum value of the property.
        ForceMinClamp : Force clamping to minimum value of the property."""
        ...
    def SetName(self,Name:str):
        """Set the property's name.
        
        Name : New name for the property."""
        ...
    def SetString(self,String:str)->bool:
        """Set the property value from a string.
        
        String : String to set property value from, with format same as AsString(kFBDataAsStringPersistence)
        return : True if it was possible."""
        ...
class FBComponent(FBPlug):
    """MotionBuilder SDK base class.
    FBComponent defines common object characteristics, including creation and destruction methods. It is used to encapsulate internal application objects so they can be exposed to the SDK. It is also used as the base class to encapsulate objects with FBProperty data members and provides a scheme for property management. You cannot instantiate FBProperty objects. To reference a property, use an instance of an FBComponent object. The methods FBComponent::PropertyCreate and FBComponent::PropertyRemove can be used to modify an object's properties. Basic operators are overloaded in FBComponent. The constructor and destructor are created and defined with macros in the header files. Objects inheriting from FBComponent must define FBComponent::FBCreate(), and FBComponent::FBDestroy(). All memory management issues for the component should also be addressed here. Destroy an object with FBDelete(). The code sample FBComponent.py shows how to get a handle on a scene object via its name. See sample: ReplaceNamespace.py."""
    Components:FBPropertyListComponent
    """List: List of components."""
    FullName:property
    LongName:str
    """Read Write Property: Name and namespace for object."""
    Name:str
    """Read Write Property: Unique name of object. See sample: RemoveSuffixFromNameOfSceneElements.py."""
    OwnerNamespace:property
    Parents:FBPropertyListComponent
    """List: Parents."""
    PropertyList:FBPropertyManager
    """Read Only Property: Manages all of the properties for the component."""
    Selected:bool
    """Read Write Property: Selected property."""
    def DisableObjectFlags(self,Flags:FBObjectFlag):
        """Disable a specific Object Flags.
        
        Flags : Flags to disable."""
        ...
    def EnableObjectFlags(self,Flags:FBObjectFlag):
        """Enable a specific Object Flags.
        
        Flags : Flags to enable."""
        ...
    def FBCreate(self)->bool:
        """Open Reality Creation function.
        
        return : Outcome of creation (true/false)."""
        ...
    def FBDelete(self):
        """Open Reality deletion function."""
        ...
    def FBDestroy(self):
        """Open Reality destruction function."""
        ...
    def GetObjectFlags(self)->FBObjectFlag:
        """Get all Object Flags (concatenated).
        
        return : Get all object flags in one call. Flags can be concatenated."""
        ...
    def GetObjectStatus(self,Status:FBObjectStatus)->bool:
        """Check to see if an object status is enabled.
        
        Status : Status to query."""
        ...
    def GetOwnerFileReference(self)->FBFileReference:
        """Get the owner FileReference object.
        
        p0 : p0
        return : the owner FileReference object"""
        ...
    def HardSelect(self):
        """HardSelect.
        Selects the object, and emits a hard select event for UI update notification."""
        ...
    def HasObjectFlags(self,Flags:FBObjectFlag)->bool:
        """Check whether a specific object flag is enabled.
        
        Flags : Flags to check if they are present.
        return : True if all flags inFlags are enabled."""
        ...
    def ProcessNamespaceHierarchy(self,NamespaceAction:FBNamespaceAction,NamespaceName:str,ReplaceTo:str=None,AddRight:bool=True)->bool:
        """ProcessNamespaceHierarchy.
        New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This recursive function goes through the whole hierarchy (children) to add/replace the prefix. If you need to work on a single object, use the ProcessObjectPrefix function.
        
        NamespaceAction : Which operation to do on the hierarchy (children).
        NamespaceName : The Namespace name on Add/Delete or the prefix to replace in case of replace.
        ReplaceTo : The new Namespace Name or NULL in case of add or delete.
        AddRight : Whether to add the namespace on right-most or left-most side or other namespace.
        return : return true if process successful."""
        ...
    def ProcessObjectNamespace(self,NamespaceAction:FBNamespaceAction,NamespaceName:str,ReplaceTo:str=None,AddRight:bool=True)->bool:
        """ProcessObjectNamespace.
        New Namespace name should only contains alphabet, digit and '_', Can't start with digit. This function is the same as ProcessNamespaceHierarchy except that it applies only on the current object and not to the object's children.
        
        NamespaceAction : Which operation to do on the hierarchy (children).
        NamespaceName : The Namespace name on Add/Delete or the prefix to replace in case of replace.
        ReplaceTo : The new Namespace Name or NULL in case of add or delete.
        AddRight : Whether to add the namespace on right-most or left-most side or other namespace.
        return : return true if process successful."""
        ...
    def PropertyAdd(self,Property:FBProperty)->int:
        """Add a property to the component's property manager.
        
        Property : The property to add to the property manager.
        return : Index in the property array where property was inserted."""
        ...
    def PropertyAddReferenceProperty(self,ReferenceProperty:FBProperty)->bool:
        """Add a reference property to the component's property manager.
        
        ReferenceProperty : The property to from an other object to add a reference to (property cannot be a custom ORSDK property).
        return : True if the reference property could be added."""
        ...
    def PropertyCreate(self,Name:str,Type:FBPropertyType,DataType:str,Animatable:bool,IsUser:bool=False,ReferenceSource:FBProperty=None)->FBProperty:
        """Create user or dynamic property.
        
        Name : The name of the property.
        Type : Type of the property. See enum FBPropertyType.
        DataType : DataType of the property.
        Animatable : To specify if the property can be animated.
        IsUser : To specify if the property is available as a custom property or dynamic and attached to the object.
        ReferenceSource : Specifies the property that a reference refers to."""
        ...
    def PropertyGetModifiedList(self,PropList:List[FBProperty])->FBPropertyList:
        """Get list of properties which have been modified since last loading.
        
        PropList : property list to hold the modified properties.
        ModificationFlags : type of modification to query."""
        ...
    def PropertyRemove(self,Property:FBProperty):
        """Remove a Property from the component's Property manager.
        If the property was dynamically allocated, it is deleted.
        
        Property : The property to remove from the property manager."""
        ...
    def SetObjectFlags(self,Flags:FBObjectFlag):
        """SetObjectFlags.
        
        Flags : Set flag values. Note: this function overwrites all flags with those passed in parameter."""
        ...
    def SetObjectStatus(self,Status:FBObjectStatus,Value:bool):
        """Enable/Disable a specific Object Status.
        
        Status : Status to change.
        Value : Value to change the status to."""
        ...
class FBPropertyVector4d(FBProperty):
    ...
class FBReferenceTime(FBComponent):
    """Reference time class.
    Interface for the reference time used by MotionBuilder The reference time are identified using unique ID. A unique ID is given when a reference time is added to the system with Add(). Instead of using a linear array to store the reference time, a map is used to link an ID to a reference time. The available IDs can be queried using GetUniqueIDList()."""
    Count:int
    """Read Only Property: Number of reference times. Deprecated, use GetUniqueIDList() instead."""
    CurrentTimeReferenceID:int
    """Read Write Property: Current reference time ID"""
    ItemIndex:int
    """Read Write Property: Current reference time index. Deprecated, use CurrentTimeReferenceID instead."""
    def Add(self,Name:str)->int:
        """Add a reference time to list.
        
        Name : Name of time to add the list.
        return : Unique ID of the reference time, use this ID to access the reference time in the future."""
        ...
    def GetReferenceTimeName(self,ID:int)->str:
        """Get the name of a time reference.
        
        ID : ID of the time reference whose name will be returned.
        return : Name of reference time with theID."""
        ...
    def GetTime(self,ID:int,System:FBTime)->FBTime:
        """Get a reference time.
        
        ID : ID of reference to get.
        System : System time.
        return : Reference time atIndex."""
        ...
    def GetUniqueIDList(self)->list:
        """Get list of currently available IDs.
        
        IDArray : Array that will be filled with the requested IDs."""
        ...
    def Remove(self,ID:int):
        """Remove a reference time from the list.
        
        ID : ID of reference time to remove."""
        ...
    def SetTime(self,ID:int,ReferenceTime:FBTime,System:FBTime):
        """Set a reference time.
        
        ID : ID of reference time set.
        ReferenceTime : Time to use as reference time.
        System : System time."""
        ...
class FBPropertyViewManager(FBComponent):
    """FBProperty View Manager.
    Interface to create new property views. There are two ways of creating properties view:on library load using AddPropertyView, RemovePropertyView, HidePropertyView - example can be found in \\OpenRealitySDK\\Samples\\constraints\\CharacterSolver\\HIK2014Solverwhile application is running using FBPropertyViewList - example can be found in in\\config\\Scripts\\Samples\\Properties\\PropertyViewManager.py See sample: PropertyViewManager.py."""
    def AddPropertyView(self,ClassName:str,PropertyName:str,Hierarchy:str)->FBPropertyViewDefinition:
        """Add property view to global ('All') view set.
        
        ClassName : Property owner class name (pClassName if won't be found, a new entry for this class is created).
        PropertyName : Property name.
        Hierarchy : Hierarchy under which property view should be created, each level name is separated by dot (for example "Degrees of Freedom.Translation").
        return : created object."""
        ...
    def CreatePropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->FBPropertyViewList:
        """Create new property view list.
        
        Object : Property view set attached to.
        ViewType : Property view set type.
        Name : Name for new view list.
        return : created object."""
        ...
    def FindPropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->FBPropertyViewList:
        """Find property view list.
        
        Object : Property view set attached to.
        ViewType : Property view set type.
        Name : Name of view set.
        return : Found property view set object or NULL."""
        ...
    def HidePropertyView(self,ClassName:str,PropertyName:str,Hide:bool):
        """Hide property view in global ('All') view set.
        
        ClassName : Property owner class name.
        PropertyName : Property name.
        Hide : Show/Hide."""
        ...
    def RefreshPropertyViews(self):
        """Force refresh of browsing property tool."""
        ...
    def RemovePropertyList(self,Object:FBComponent,ViewType:FBPropertyViewType,Name:str)->bool:
        """Remove property view list (only if editable).
        
        Object : Property view set attached to.
        ViewType : Property view set type.
        Name : Name for property view list.
        return : True if successful."""
        ...
    def RemovePropertyView(self,ClassName:str,PropertyName:str)->bool:
        """Remove property view from global ('All') view set.
        
        ClassName : Property owner class name.
        PropertyName : Property name.
        return : true if succeed (should not be call on system views)."""
        ...
class FBPropertyVector3d(FBProperty):
    ...
class FBPropertyVector2d(FBProperty):
    ...
class FBPropertyTimeCode(FBProperty):
    ...
class FBPropertyTime(FBProperty):
    ...
class FBPropertyStringList(FBProperty):
    """>>> # Supported list protocol methods:
    len(propertyStringList)
    component= propertyStringList[0]
    propertyStringList[0] = my_string
    if my_string in propertyStringList:
    print 'it is contained!'
    del propertyStringList[0]"""
    def append(self,Value:object):
        """Append new str at end of list.
        
        Value : to append"""
        ...
    def count(self,arg2:object)->int:
        """Returns the number of elements.
        Corresponds to python: del propertyList[2]
        
        return : number of elements in list."""
        ...
    def findFromReference(self,Reference:object)->int:
        """Find the index of an element from its attached reference.
        
        Reference : Reference of searched object.
        return : Returns the index of the element corresponding to reference."""
        ...
    def getReferenceAt(self,Index:object)->int:
        """Retrieve the reference of an object at ith position.
        
        Index : Index of the object to find reference.
        return : Returns the reference of the object."""
        ...
    def insert(self,Index:int,Value:object):
        """Insert a new element in list.
        
        Index : Index where to insert string
        Value : String to append"""
        ...
    def pop(self)->object:
        """Remove an element in list.
        
        Index : Index where to remove element.
        return : Returns the element that was removed."""
        ...
    def remove(self,Index:object):
        """Remove an element in list.
        
        Index : Index where to remove element."""
        ...
    def removeAll(self):
        """Remove all elements of list"""
        ...
    def setReferenceAt(self,Reference:object,arg3:object):
        """Sets the reference value of an object.
        
        Reference : Reference of the object."""
        ...
class FBPropertyString(FBProperty):
    """Property: StringList"""
    ...
class FBPropertyListTreeNode(FBProperty):
    """PropertyList of nodes in the tree view.PropertyList: UserObject.
    These classes are under development and may change dramatically between versions."""
    def append(self,arg2:object):...
    def count(self,arg2:object)->int:...
    def insert(self,arg2:int,arg3:object):...
    def pop(self)->object:...
    def remove(self,arg2:object):...
    def removeAll(self):...
class FBPropertyListComponent(FBProperty):
    """PropertyList: Contraint
    
    
    >>> # Supported list protocol methods:
    len(propertyListComponent)
    component= propertyListComponent[0]
    propertyListComponent[0] = my_component
    if my_component in propertyListComponent:
    print 'it is contained!'
    del propertyListComponent[0]"""
    def append(self,Comp:object):
        """Append new FBComponent at end of list.
        
        Comp : to append"""
        ...
    def count(self,arg2:object)->int:
        """Returns the number of elements.
        Corresponds to python: del propertyList[2]
        
        return : number of elements in list."""
        ...
    def insert(self,Index:int,Comp:object):
        """Insert a new element in list.
        
        Index : Index where to insert component
        Comp : Component to append"""
        ...
    def pop(self)->object:
        """Remove an element in list.
        
        Index : Index where to remove element.
        return : Returns the element that was removed."""
        ...
    def remove(self,Index:object):
        """Remove an element in list.
        
        Index : Index where to remove element."""
        ...
    def removeAll(self):
        """Remove all elements of list"""
        ...
class FBPropertyList(FBProperty):
    """Tuple-like structure for system elements.
    These list objects are used to expose system wide or instance specific list of objects. Two examples of this are FBSystem's list of Cameras and a FBModel's list of Shaders. These lists have been exposed to Python as tuple, whose content cannot be modified directly. This is due to the specific nature of each type of list and the access control required by the owner of the list. For example, creating a new FBCamera object will automatically add it to the list of FBSystem's Cameras. The user does not have to add it to the list. The same being true for the destruction of the camera which should be done by calling 'FBDelete()' on the object itself. Not by atempting to remove it from the list of cameras.
    
    >>> # Supported list operations:
    len(propertyList)
    print propertyList[0]"""
    def append(self,arg2:object):...
    def count(self,arg2:object)->int:...
    def insert(self,arg2:int,arg3:object):...
    def pop(self)->object:...
    def remove(self,arg2:object):...
    def removeAll(self):...
class FBPropertyListVideoOut(FBPropertyListComponent):
    ...
class FBPropertyListVideoIn(FBPropertyListComponent):
    """PropertyList: VideoOut"""
    ...
class FBPropertyListVideoClip(FBPropertyListComponent):
    """PropertyList: VideoIn"""
    ...
class FBPropertyListUserObject(FBPropertyListComponent):
    """PropertyList: VideoClip"""
    ...
class FBPropertyListTexture(FBPropertyListComponent):
    ...
class FBPropertyListTake(FBPropertyListComponent):
    """PropertyList: Texture"""
    ...
class FBPropertyListStoryTrack(FBPropertyListComponent):
    """List: Take"""
    ...
class FBPropertyListStorySubTrack(FBPropertyListComponent):
    """List: StoryTrack"""
    ...
class FBPropertyListStoryFolder(FBPropertyListComponent):
    """List: StorySubTrack"""
    ...
class FBPropertyListStoryDetails(FBPropertyListComponent):
    """List: StoryFolder"""
    ...
class FBPropertyListStoryClip(FBPropertyListComponent):
    """List: Story track Details"""
    ...
class FBPropertyListShader(FBPropertyListComponent):
    """List: StoryClip"""
    ...
class FBPropertyListSet(FBPropertyListComponent):
    """PropertyList: Shader"""
    ...
class FBPropertyListRendererCallback(FBPropertyListComponent):
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListPose(FBPropertyListComponent):
    """PropertyList: Texture"""
    ...
class FBPropertyListPivot(FBPropertyListComponent):
    """List: Model"""
    ...
class FBPropertyListPhysicalProperties(FBPropertyListComponent):
    """List: Story Clip pivot models"""
    ...
class FBPropertyListObjectPose(FBPropertyListComponent):
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListObject(FBPropertyListComponent):
    """List-like structure fo system elements.
    PropertyList: ObjectPose.This container supports most of the list interface, but is limited to contain only FBComponent objects. New objects can be added, or objects in the list can be removed. The cardinality of the list and the use of the contained object will vary according the container object type. This class supports slice access for query, but not for assignment."""
    def GetSingleConnect(self)->int:
        """Get if the connection support only one connection.
        
        return : true is the connection support only one connection."""
        ...
    def SetSingleConnect(self,SingleConnect:bool):
        """Set if the connection is single or multiple.
        
        SingleConnect : set to true for only one connection allowed."""
        ...
class FBPropertyListNote(FBPropertyListComponent):
    """List of scene objects.
    This list is a more generic container often used as object properties. The types of actual object that it can contain can be specialized."""
    ...
class FBPropertyListNamespace(FBPropertyListComponent):
    """List: Note"""
    ...
class FBPropertyListMotionClip(FBPropertyListComponent):
    """List: Namespace"""
    ...
class FBPropertyListModelSkeleton(FBPropertyListComponent):
    """PropertyList: ModelTemplate."""
    ...
class FBPropertyListModelOptical(FBPropertyListComponent):
    """PropertyList: ModelSkeleton."""
    ...
class FBPropertyListModel(FBPropertyListComponent):
    """PropertyList: Device optical marker"""
    ...
class FBPropertyListMaterial(FBPropertyListComponent):
    """List: Model"""
    ...
class FBPropertyListMarkerSet(FBPropertyListComponent):
    """PropertyList: Material"""
    ...
class FBPropertyListLight(FBPropertyListComponent):
    """PropertyList: Manipulator."""
    ...
class FBPropertyListKeyingGroup(FBPropertyListComponent):
    """PropertyList: Light"""
    ...
class FBPropertyListHandle(FBPropertyListComponent):
    """PropertyList: KeyingGroup."""
    ...
class FBPropertyListHUDElement(FBPropertyListComponent):
    """PropertyList: Handle."""
    ...
class FBPropertyListHUD(FBPropertyListComponent):
    """PropertyList: Handle."""
    ...
class FBPropertyListGroup(FBPropertyListComponent):
    """PropertyList: Handle."""
    ...
class FBPropertyListFolder(FBPropertyListComponent):
    """List: Group"""
    ...
class FBPropertyListFileReference(FBPropertyListComponent):
    """PropertyList: Folder"""
    ...
class FBPropertyListDevice(FBPropertyListComponent):
    ...
class FBPropertyListDeformer(FBPropertyListComponent):
    """PropertyList: Device"""
    ...
class FBPropertyListDeck(FBPropertyListComponent):
    ...
class FBPropertyListControlSet(FBPropertyListComponent):
    """PropertyList: Deck"""
    ...
class FBPropertyListConstraintSolver(FBPropertyListComponent):
    """PropertyList: MarkerSet.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListActor(FBPropertyListComponent):
    """PropertyList: Actor face.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListActorFace(FBPropertyListComponent):
    ...
class FBPropertyListAudioClip(FBPropertyListComponent):
    """List: AudioIn"""
    ...
class FBPropertyListAudioIn(FBPropertyListComponent):
    """List: AudioOut"""
    ...
class FBPropertyListAudioOut(FBPropertyListComponent):
    """List: Box informations for constraint relation."""
    ...
class FBPropertyListBox(FBPropertyListComponent):
    """PropertyList: Camera"""
    ...
class FBPropertyListCamera(FBPropertyListComponent):
    """PropertyList: Character.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListCharacter(FBPropertyListComponent):
    ...
class FBPropertyListCharacterExtension(FBPropertyListComponent):
    """Character extension property list.PropertyList: Character face.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListCharacterFace(FBPropertyListComponent):
    """PropertyList: CharacterMarkerSet.
    These classes are under development and may change dramatically between versions."""
    ...
class FBPropertyListCharacterMarkerSet(FBPropertyListComponent):
    """PropertyList: CharacterPose."""
    ...
class FBPropertyListCharacterPose(FBPropertyListComponent):
    """PropertyList: Concrete class for PropertyList of component"""
    ...
class FBPropertyListConstraint(FBPropertyListComponent):
    """PropertyList: Constraint solver"""
    ...
class FBPropertyInt(FBProperty):
    ...
class FBPropertyFloat(FBProperty):
    ...
class FBPropertyEnum(FBProperty):
    """Enumeration property.
    Certain properties have strings associated with the integer values they may possess. FBModel's ShadingMode property is one of those example. The actual underlying value of the property is numerical, but it is represented by a string value in the GUI. User can create this type of property via the GUI by creating a list property. The names added to the list can be obtained via the 'EnumList()' method."""
    ...
class FBPropertyDouble(FBProperty):
    ...
class FBPropertyComponent(FBProperty):
    ...
class FBPropertyColorAndAlpha(FBProperty):
    """FBPropertyColorAndAlpha class.
    Similar in use to FBPropertyColor
    
    >>> # Supported list protocol methods:
    c = FBPropertyColorAndAlpha()
    len(c)
    print c[0]
    c[0] = 1.0
    print c.Data
    c.Data=FBColorAndAlpha(1.0,0.5,0.5,1.0)
    
    
    Slicing is not supported by this object."""
    ...
class FBPropertyColor(FBProperty):
    """FBPropertyColor class.
    Similar in use to FBPropertyVector3d
    
    >>> # Supported list protocol methods:
    c = FBPropertyColor()
    len(c)
    print c[0]
    c[0] = 1.0
    print c.Data
    c.Data=FBColor(1.0,0.5,0.5)
    
    
    Slicing is not supported by this object."""
    ...
class FBPropertyBool(FBProperty):
    ...
class FBPropertyAnimatable(FBProperty):
    """Animatable property base class."""
    def AllowsMuting(self)->bool:
        """AllowsMuting.
        
        return : true if property can be muted"""
        ...
    def GetAnimationNode(self)->FBAnimationNode:
        """Get the animation node for the property.
        
        return : Animation node for property. None is returned if property is not animated."""
        ...
    def GetBox(self)->FBBox:
        """Get the owner box.
        
        return : Handle to the owning box (i.e. model)."""
        ...
    def GetColor(self,Index:int)->FBColor:
        """Get the color of a particular FCurve of the property.
        
        Index : Index of the FCurve to get the color.
        return : The color of the FCurve at the specified index, a default FBColor object if the index is invalid."""
        ...
    def GetDataTypeName(self)->str:
        """Get the property datatype name.
        
        return : Datatype of property as a character string."""
        ...
    def HasSomethingMuted(self)->bool:
        """HasSomethingMuted.
        
        return : true if property or any of its members is muted"""
        ...
    def IsAnimated(self)->bool:
        """Is the property animated.
        This is true if the property has an FCurve associated to it.
        
        return : true if animated, false if not animated."""
        ...
    def IsFocused(self)->bool:
        """Is the property focused (keyable).
        
        return : Current focus (keyable) state for the property."""
        ...
    def IsFocusedChild(self,Index:int)->bool:
        """Get the focus (keyable) state of child component.
        
        Index : Index of the child FCurve component.
        return : true if the component is in focus, false otherwise"""
        ...
    def IsMemberMuted(self,Index:int)->bool:
        """IsMemberMuted.
        
        Index : Index of the sub-member of the property to check.
        return : true if property sub-member is muted"""
        ...
    def IsMuted(self)->bool:
        """IsMuted.
        
        return : true if property is muted"""
        ...
    def Key(self):
        """Key the property."""
        ...
    def KeyAt(self,Time:FBTime):
        """Key the property at time (t).
        
        Time : Time at which to insert the key."""
        ...
    def KeyRemoveAt(self,Time:FBTime):
        """Remove the key at time (t).
        
        Time : Time at which to insert the key."""
        ...
    def OriIsAnimated(self)->bool:...
    def ResetColor(self,Index:int)->bool:
        """Revert the FCurves to their default color.
        
        Index : Index of the FCurve to reset the color, use -1 to reset the color for all FCurves of the property.
        return : true if the color was reverted to its default value, false otherwise"""
        ...
    def SetAnimated(self,State:bool,CheckLocked:bool=False):
        """Set the animation state of the property.
        
        State : State of animation for property, true to animate, false to remove curves.
        CheckLocked : Decides whether to check the locked status."""
        ...
    def SetColor(self,Color:FBColor,Index:int)->bool:
        """Set the color of the FCurves for the property.
        
        Color : Color to set for the FCurve(s).
        Index : Index of the FCurve to set the new color, use -1 to set the color for all FCurves.
        return : true if the color was changed, false otherwise"""
        ...
    def SetFocus(self,State:bool):
        """Set the property's focus (keyable) state.
        
        State : Focus (keyable) state to set for the property."""
        ...
    def SetFocusChild(self,Index:int,State:bool)->bool:
        """Set the focus (keyable) state of child component.
        
        Index : Index of the child FCurve component.
        State : Focus (keyable) state to set for the property component.
        return : true if the operation was successful, false otherwise"""
        ...
    def SetMemberMuted(self,Index:int,Muted:bool):
        """SetMemberMuted.
        
        Index : Index of the sub-member of the property to mute or unmute.
        Muted : True if the sub-member is to be muted, false if it is to be unmuted."""
        ...
    def SetMuted(self,Muted:bool):
        """SetMuted.
        
        Muted : True if the property is to be muted, false if it is to be unmuted."""
        ...
class FBPropertyAction(FBProperty):
    ...
class FBPropertyAnimatableVector4d(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableVector3d(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableVector2d(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableUInt64(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableTimeCode(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableTime(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableInt64(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableInt(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableEnum(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableDouble(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableColorAndAlpha(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableColor(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableBool(FBPropertyAnimatable):
    ...
class FBPropertyAnimatableAction(FBPropertyAnimatable):
    ...
class FBRenderer(FBComponent):
    """Open Reality renderer interface.
    See samples: render.py, CameraSwitcher.py."""
    AdvancedLightingMode:bool
    """Read write Property: Turn on/off advanced lighting setting UI widgets."""
    AdvancedMaterialMode:bool
    """Read write Property: Turn on/off advanced material setting UI widgets."""
    AutoEvaluate:bool
    """Read Write Property: Indicate if a call to RenderBegin will also cause a re-evaluation of the scene."""
    Background:bool
    """Read Write Property: The renderer."""
    CurrentCamera:FBCamera
    CurrentPaneCallbackIndex:int
    """Read Write Property: Current Pane's Renderer Callback Index."""
    CurrentPaneCallbackPrefIndex:int
    """Read Write Property: Current Pane's Renderer Callback Preference Index."""
    DisplayNormals:bool
    """Read Write Property: Display model normals in main viewer."""
    DisplaySetUpdateId:int
    """Read Only Property: Current DisplaySet Update Id. Add/Delete models, Show/Hide models will affect DisplaySet."""
    DisplayableGeometryCount:int
    """Read Only Property: Displayable geometry count."""
    DisplayableLightCount:int
    """Read Only Property: Displayable light count."""
    FrustumCulling:bool
    """Read Write Property: Turn on/off the early frustum culling optimization."""
    HideManipulatorsOnManip:bool
    """Read Write Property: Hide manipulators UI elements while manipulating."""
    HideManipulatorsOnPlayback:bool
    """Read Write Property: Hide manipulators UI elements during playback."""
    IDBufferDisplay:bool
    """Read write Property: Render Model's unique Color ID into color Buffer (used for picking)"""
    IDBufferPicking:bool
    """Read write Property: Use ID (Color) Buffer for picking, instead of OpenGl selection buffer picking."""
    IDBufferPickingAlpha:float
    """Read write Property: Those Semi-transparent (Alpha Blend) geometry(region) contribute less than this threshold, will be considered as invisible during ID picking."""
    PickingEnabled:bool
    """Read Write Property: Is picking in the viewer enabled?"""
    RegisteredCallbackCount:int
    """Read Only Property: Registered Renderer Callback Count."""
    RendererCallbacks:FBPropertyListRendererCallback
    """List: Renderer Callbacks attached."""
    RendererUpdateId:int
    """Read Only Property: Current Render Update Id. DisplaySet update, material change, texture changes and shader change and other operations will trigger Renderer update."""
    Scene:FBScene
    """Read Write Property: Scene that the renderer will use/draw"""
    SelectionForceSnapPointsDisplay:bool
    """Read write Property: Force show all feature points (pivots and etc) on selected models if true, ignore individual model's settings."""
    SelectionOverride:bool
    """Read write Property: Add transparent color override layer on selected models if true."""
    SelectionOverrideColor:FBColor
    """Read write Property: Selection override layer color."""
    SelectionOverrideTransparency:float
    """Read write Property: Selection override layer transparency."""
    ShowStats:bool
    """Read Write Property: Show the stats about FPS, Evaluation rate ... like when using Shift-F in main viewer."""
    UseCameraSwitcher:bool
    def ArrangeAllInSchematic(self,Mode:FBArrangeMode):
        """Request to arrange all objects in schematic view .
        
        Mode : Arrange mode."""
        ...
    def ArrangeObjectsInSchematicFromModel(self,Model:FBModel)->bool:
        """Request to arrange a node's tree in the Schematic View, given a starting node.
        
        Model : The starting node from which the arrange operation is requested.
        return : True if the operation is successful, false otherwise."""
        ...
    def ArrangeSelectedObjectsInSchematic(self):
        """Request to arrange selected objects in schematic view ."""
        ...
    def CreateSchematicBookmark(self,BookmarkName:str)->bool:
        """Create a new bookmark in the Schematic View.
        
        BookmarkName : The new bookmark name.
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if a bookmark with the given name already exists."""
        ...
    def DeleteSchematicBookmark(self,BookmarkName:str)->bool:
        """Delete a bookmark from the Schematic View.
        
        BookmarkName : The bookmark name to delete.
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name."""
        ...
    def FrameCurrentCameraWithModels(self,All:bool)->bool:
        """Frame the current camera either with all models or with the currently selected models.
        
        All : true to frame with all models.
        return : true if successful."""
        ...
    def GetCameraInPane(self,PaneIndex:int)->FBCamera:
        """Return the camera displayed in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned camera is the camera that would be displayed if the Schematic View was deactivated. If the Camera Switcher is on in the pane associated with the given pane index, the returned camera is the switcher's current camera.Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher().
        
        PaneIndex : The pane index.
        return : The camera used in the given pane index, NULL if the pane index is invalid."""
        ...
    def GetCurrentSchematicBookmarkName(self)->str:
        """Return the current bookmark name used by the Schematic View.
        
        return : The current bookmark name used by the Schematic View. An empty string is returned if there is no current bookmark."""
        ...
    def GetDisplayableGeometry(self,Index:int)->FBModel:
        """Get the displayable geometry model.
        Those geometry models which have Show property ON are considered as 'displayable'.
        
        Index : displayable geometry model index to query.
        return : displayable geometry model."""
        ...
    def GetDisplayableGeometryInCameraFrustum(self,ModelList:FBModelList=None,Camera:FBCamera=None)->FBModelList:
        """Get a list of displayable geometry inside given camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.
        
        ModelList : ModelList holding the return models.
        Camera : use current camera if NULL.
        return : Reference toModelList. ifModelList is NULL return a const reference to internal static FBModelList and consecutive call to this function will invalidate the result of previous call."""
        ...
    def GetDisplayableLight(self,Index:int)->FBLight:
        """Get the displayable light.
        Those light models which have Show property ON are considered as 'displayable'.
        
        Index : displayable light index to query.
        return : displayable light."""
        ...
    def GetLastPickInfoList(self,PickInfosList:FBPickInfosList)->int:
        """Return the last picking info list in the current view pane.
        
        PickInfosList : The list of pick infos.
        return : number of item in the list."""
        ...
    def GetPaneCount(self)->int:
        """Return the number of panes displayed in the viewer's layout.
        
        return : The number of panes displayed."""
        ...
    def GetSchematicBookmarkNames(self)->FBStringList:
        """Return the bookmark names available in the Schematic View.
        
        return : A string list containing the bookmark names available in the Schematic View. An empty list is returned if no bookmark is available."""
        ...
    def GetSchematicNodesBoundingBox(self,ConsiderCollapsedNodes:bool)->bool:
        """Returns the bounding box (top, left, bottom, right) used by all the Schematic View nodes.
        
        ConsiderCollapsedNodes : True to also consider nodes which are not visible because collapsed, false otherwise.
        Top : Top value of the bounding box. Will be filled once the method returns.
        Left : Left value of the bounding box. Will be filled once the method returns.
        Bottom : Bottom value of the bounding box. Will be filled once the method returns.
        Right : Right value of the bounding box. Will be filled once the method returns.
        return : True if the operation is successful, false otherwise (e.g. the Schematic View has any node in it, etc.)."""
        ...
    def GetSchematicNodesBoundingBoxFromModel(self,Model:FBModel,ConsiderCollapsedNodes:bool)->bool:
        """Returns the bounding box (top, left, bottom, right) of a node's tree in the Schematic View, given a starting node.
        
        Model : The starting node from which the bounding box tree is requested.
        ConsiderCollapsedNodes : True to also consider nodes which are not visible because collapsed, false otherwise.
        Top : Top value of the bounding box. Will be filled once the method returns.
        Left : Left value of the bounding box. Will be filled once the method returns.
        Bottom : Bottom value of the bounding box. Will be filled once the method returns.
        Right : Right value of the bounding box. Will be filled once the method returns.
        return : True if the operation is successful, false otherwise (e.g. the starting node is not in the Schematic View, etc.)."""
        ...
    def GetSchematicViewPaneIndex(self)->int:
        """Return the pane index of the pane displaying the Schematic View.
        
        return : The pane index of the pane displaying the Schematic View, -1 if the Schematic View is currently not displayed in any pane."""
        ...
    def GetSelectedPaneIndex(self)->int:
        """Return the pane index associated with the selected pane in the active viewer's layout.
        
        return : The selected pane index."""
        ...
    def GetViewingOptions(self)->FBViewingOptions:
        """Obtain the current viewing options.
        
        return : A structure that can be queried and updated for a call to SetViewingOptions."""
        ...
    def IsCameraSwitcherInPane(self,PaneIndex:int)->bool:
        """Return the Camera Switcher activeness in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the returned value is the value that would be returned if the Schematic View was deactivated.
        
        PaneIndex : The pane index.
        return : True if the Camera Switcher is active in the pane associated with the given pane index, False otherwise."""
        ...
    def IsCurrentSchematicBookmarkDirty(self)->bool:
        """Return if the current bookmark used by the Schematic View is dirty or not.
        
        return : True if the current bookmark is dirty, false otherwise. False is returned if there is no current bookmark."""
        ...
    def IsModelInsideCameraFrustum(self,Geometry:FBModel,Camera:FBCamera=None)->bool:
        """To tell if given model is located inside camera's frustum.
        This function will return conservative result. It's possible for some geometry outside of the frustum will be considered to be visible, but it will not skip any real visible geometry. This function should only be called in the main rendering thread.
        
        Geometry : the geometry to be queried.
        Camera : use current camera if NULL.
        return : true if Model is inside camera frustum."""
        ...
    def KeyboardInput(self,KeyIndex:FBDeviceKeyboardKey,KeyState:bool,IsTrigger:bool=False):
        """Keyboard input.
        
        KeyIndex : Key index. (See "enum FBDeviceKeyboardKey" above for supported keys)
        KeyState : Key state. (True == key is down, False == key is up)
        IsTrigger : When settingKeyState to True, resets key state to False right after operation."""
        ...
    def MouseInput(self,X:int,Y:int,InputType:FBInputType,ButtonKey:int,Modifier:FBInputModifier,WheelDeltaValue:int=0,Layer:int=-1)->bool:
        """Mouse input.
        
        X : X position.
        Y : Y position.
        InputType : Type of input.
        ButtonKey : Button/Key pressed.
        Modifier : Modifier pressed (CTRL/ALT/SHIFT).
        WheelDeltaValue : Mouse wheel delta value
        Layer : Rendering layer ID(default=-1).
        return : true if successful."""
        ...
    def MouseInputNormalized(self,X:float,Y:float,InputType:FBInputType,ButtonKey:int,Modifier:FBInputModifier,WheelDeltaValue:int,Layer:int=-1,PaneId:int=-1)->bool:
        """Mouse input.
        
        X : X position, normalized to the range of [0, 1] in the view port dimension.
        Y : Y position, normalized to the range of [0, 1] in the view port dimension.
        InputType : Type of input.
        ButtonKey : Button/Key pressed.
        Modifier : Modifier pressed (CTRL/ALT/SHIFT).
        WheelDeltaValue : Mouse wheel delta value
        Layer : Rendering layer ID(default=-1).
        PaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer.
        return : true if successful."""
        ...
    def OGLModelDisplay(self,RenderOptions:FBRenderOptions,Model:FBModel):
        """RenderOptions : FBRenderOptions
        Model : FBModel"""
        ...
    def OGLSetupSceneLights(self,RenderOptions:FBRenderOptions):
        """Setup the scene lights in OpenGL.
        
        RenderOptions : See FBRenderOptions for more detail."""
        ...
    def Pick(self,X:int,Y:int,PickInfosList:FBPickInfosList)->bool:
        """Object picking selection.
        
        X : X position.
        Y : Y position.
        PickInfosList : The list of pick infos.
        NeedIntersectPosition : require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh."""
        ...
    def PickNormalized(self,X:float,Y:float,PickInfosList:FBPickInfosList,NeedIntersectPosition:bool=False)->bool:
        """Object picking selection.
        
        X : X position, normalized to the range of [0, 1] in the view port dimension.
        Y : Y position, normalized to the range of [0, 1] in the view port dimension.
        PickInfosList : The list of pick infos.
        NeedIntersectPosition : require valid intersection position if true, this will take more time to process, and not reliable with very dense mesh.
        PaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer."""
        ...
    def PreRender(self,Layer:int=-1)->bool:
        """PreRenders one frame (needed for some shaders) This functions destroys the frame buffer content and must be called every time a render is called the typical order of call must be Renderer->Prerender // at this point the frame buffer is garbage -Clear the ogl -Do your render functions Renderer->Render.
        
        Layer : Rendering layer ID(default=-1).
        return : true if successful."""
        ...
    def RectPick(self,X1:int,Y1:int,X2:int,Y2:int,PickInfosList:FBPickInfosList)->bool:
        """Object rectangle selection.
        
        X1 : Left upper corner X position.
        Y1 : Left upper corner y position.
        X2 : Right bottom corner X position.
        Y2 : Right bottom corner y position.
        PickInfosList : The list of pick infos."""
        ...
    def RectPickNormalized(self,X1:float,Y1:float,X2:float,Y2:float,PickInfosList:FBPickInfosList,PaneId:int=-1)->bool:
        """Object rectangle selection.
        
        X1 : Left upper corner X position, normalized to the range of [0, 1] in the viewport dimension.
        Y1 : Left upper corner y position, normalized to the range of [0, 1] in the viewport dimension.
        X2 : Right bottom corner X position, normalized to the range of [0, 1] in the viewport dimension.
        Y2 : Right bottom corner y position, normalized to the range of [0, 1] in the viewport dimension.
        PickInfosList : The list of pick infos.
        PaneId : specify which pane's dimension used for normalization, default (-1) for the whole viewer."""
        ...
    def RenameSchematicBookmark(self,OldBookmarkName:str,NewBookmarkName:str)->bool:
        """Rename a bookmark in the Schematic View.
        
        OldBookmarkName : The bookmark name to rename.
        NewBookmarkName : The new bookmark name.
        return : True if the operation is successful, false otherwise. False is returned if the old/new bookmark name is empty, if the old bookmark doesn't exist or if a bookmark with the new given name already exists."""
        ...
    def Render(self,Layer:int=-1)->bool:
        """Renders one frame.
        
        Layer : Rendering layer ID(default=-1).
        return : true if successful."""
        ...
    def RenderBegin(self,X:int,Y:int,W:int,H:int)->bool:
        """RenderBegin.
        must be called before rendering can happen
        
        X : X position where to render.
        Y : Y position where to render.
        W : Width of render area.
        H : Hight of render area."""
        ...
    def RenderEnd(self)->bool:
        """RenderEnd.
        
        View : If you want the renderer to draw artifacts, such as TimeCode, CameraLabel or SafeArea, you must provide the FBView on which the renderer draws on."""
        ...
    def SelectSchematicBookmark(self,BookmarkName:str)->bool:
        """Select an existing bookmark in the Schematic View and use it as the current bookmark.
        
        BookmarkName : The bookmark name to select.
        return : True if the operation is successful, false otherwise. False is returned if the bookmark name is empty or if no bookmark exists with the given name."""
        ...
    def SetCameraInPane(self,Camera:FBCamera,PaneIndex:int):
        """Set the camera to display in the given pane index.
        If the Schematic View is displayed in the pane associated with the given pane index, the camera will be displayed when the Schematic View will be deactivated from this pane.Note: If current pane uses Camera Switcher, it will be set to use Camera, rather than old behavior that still uses Camera Switcher and sets Camera to be Camera Switcher's current camera, which introduce a Zombie Camera Switcher problem. By using Camera, the problem is gone.Note: To operate current camera in Camera Switcher, it is recommended to use FBCameraSwitcher().
        
        Camera : The camera to set.
        PaneIndex : The pane index."""
        ...
    def SetCameraSwitcherInPane(self,PaneIndex:int,Active:bool):
        """Set/Remove the Camera Switcher in the given pane index.
        To specify which camera the Camera Switcher should be displaying, use the SetCameraInPane method. If the Schematic View is displayed in the pane associated with the given pane index, the camera switcher will be displayed (if activated) when the Schematic View will be deactivated from this pane.
        
        PaneIndex : The pane index.
        Active : True to activate the Camera Switcher in the given pane, False to remove it."""
        ...
    def SetPaneCount(self,PaneCount:int):
        """Set the number of panes to display in the viewer's layout.
        
        PaneCount : The number of panes to display."""
        ...
    def SetSchematicViewInPane(self,PaneIndex:int,Active:bool):
        """Set/Remove the Schematic View in the given pane index.
        When activating the Schematic View in the pane, if the Schematic View is already activated in another pane, the Schematic View will be removed from latter before being activated into the new pane.
        
        PaneIndex : The pane index.
        Active : True to activate the Schematic View in the given pane, False to remove it."""
        ...
    def SetSelectedPaneIndex(self,PaneIndex:int)->bool:
        """Select the pane associated with the given pane index in the active viewer's layout.
        
        PaneIndex : The pane index.
        return : True if the operation is successful, False otherwise."""
        ...
    def SetViewingOptions(self,Options:FBViewingOptions)->bool:
        """Set the viewing options.
        
        Options : See FBViewingOptions for more detail."""
        ...
    def SetViewport(self,X:int,Y:int,W:int,H:int):
        """Must be called before inputing if the same renderer is used on multiple views/cameras in the same application.
        
        X : X position where to render.
        Y : Y position where to render.
        W : Width of render area.
        H : Hight of render area."""
        ...
    def UpdateCurrentSchematicBookmark(self)->bool:
        """Update the current bookmark in the Schematic View.
        
        return : True if the operation is successful, false otherwise. False is returned if there is no current bookmark."""
        ...
class FBProgress(FBComponent):
    """Progress bar.Property: Base property class.
    See samples: 3dsMaxBipedTemplate.py, MirrorPoseOverTime.py, FBProgress.py. A property is a holder for function callbacks into the internals of the application.You cannot instantiate FBProperty objects. To reference a property: Use an instance of an FBComponent object. The methods FBComponent::PropertyCreate and FBComponent::PropertyRemove can be used to modify an object's set of properties. When accessing a FBProperty object via its containing object, you can get or set (assuming it is not read-only) its value directly, for example in Python: myObject.Visibility = True. FBPropertyManager exists in all FBComponent objects, and contains an array of all the registered properties. Use FBProperty::Find to find a property by name. When accessing a property reference directly, its value is obtained via its 'Data' member.
    
    >>> myProp = myObject.PropertyList.Find( 'Visibility' )
    if myProp: myProp.Data = True
    
    
    To see how to create a custom property in Python, see CustomProperty.py. See samples: CustomProperty.py, SetAllToDoneInAllTakes.py."""
    Caption:str
    Percent:int
    """Read Write Property: Percent completed for the operation. Must be used called in between ProgressBegin()/ProgressDone()"""
    Text:str
    """Read Write Property: Text to display on progress bar. Must be used in between ProgressBegin()/ProgressDone()"""
    def ProgressBegin(self):
        """Start progress, must be called before set Text & Percent property."""
        ...
    def ProgressDone(self):
        """End progress, must be called to reset progress bar UI to normal status after finishing the task."""
        ...
    def UserRequestCancell(self)->bool:
        """Return true if User is pressing and holding 'ESC' key to request the cancellation.
        Must be called in between ProgressBegin()/ProgressDone()."""
        ...
class FBProfiler(FBComponent):
    """FBProfiler.
    Central place to query profiling results and change profiling options. See sample: CreateProfilingEventsLog.py."""
    ActiveSampling:bool
    """Read/Write Property: Activate the sampling for time events. Call before quering for FBProfileTimeEvent."""
    BufferSize:int
    """Read/Write Property: Buffer size for average and timing computation (maximum value 200)."""
    EvaluationDepth:int
    """Read/Write Property: Specify the depth of evaluation profiling for data collection (maximum value is 10)."""
    FrameReference:bool
    """Read/Write Property: Draw task cycles in relation to main thread cycle time - frame cycle (percentage display)."""
    ProfilingMode:FBProfilingMode
    """Read/Write Property: Profiling collection modes, including disabling all profiling."""
    def GetEndEventSample(self,Index:int)->FBProfileTimeEvent:
        """Get end time event for event at given index.
        This function and FBProfileTimeEvent.IsSingleEvent are useful to identify duration of event action.
        
        Index : Sample index.
        return : Sample object if sample at given index is start sample."""
        ...
    def GetEventSample(self,Index:int)->FBProfileTimeEvent:
        """Only possible way to query collected FBProfileTimeEvent.
        
        Index : Sample index.
        return : Sample object."""
        ...
    def GetEventSampleCount(self)->int:
        """Get number of time event samples collected during last sampling.
        
        return : Number of FBProfileTimeEvent samples gathered during sampling."""
        ...
    def GetProfilingCost(self)->float:
        """Profiling collection can affect scene performace.
        This function return how costly is profiling.
        
        return : Cost of profiling the scene. (in mini seconds)"""
        ...
    def GetStatComment(self,Index:int)->str:
        """Get aditional information about what action is stat refering to.
        
        Index : Index of stat.
        return : Stat comment."""
        ...
    def GetStatCount(self)->int:
        """Stats are holding last execution time/duration of action.
        They are used for actions that doesn't appear frequently, like file IO.
        
        return : Stats count. They are created when stat occurs, so open or save action needs to be done first to get any information stored in stats."""
        ...
    def GetStatDuration(self,Index:int)->float:
        """Get time that was spend on execution of action.
        
        Index : Index of stat.
        return : Stat duration (in seconds)."""
        ...
    def GetStatIndex(self,Name:str)->int:
        """Search for index of given stat name.
        
        Name : Name of the sample that we are looking for.
        return : Stat index if found, -1 if not in the list."""
        ...
    def GetStatName(self,Index:int)->str:
        """Get information about what action is stat refering to.
        
        Index : Index of stat.
        return : Stat name."""
        ...
    def GetStatStart(self,Index:int)->float:
        """Get start time of action.
        
        Index : Index of stat.
        return : Start time (in seconds)."""
        ...
    def GetStatStop(self,Index:int)->float:
        """Get stop time of action.
        
        Index : Index of stat.
        return : Stop time (in seconds)."""
        ...
class FBPose(FBComponent):
    """Pose class."""
    Type:FBPoseType
    """Read Only Property: Type of the pose (bind pose or rest pose)"""
    def AddNode(self,Object:FBModel,Matrix:FBMatrix=None,IsLocalMatrix:bool=False)->int:
        """Add a new pose node.
        
        Object : The object for which we are creating the pose information.
        Matrix : The transformation of the object we want to save.
        IsLocalMatrix : Is the matrix a local matrix?"""
        ...
    def CreatePoseThumbnail(self):
        """Create an image thumbnail for the current pose."""
        ...
    def Find(self,NodeName:str)->int:
        """Look in this pose if the given node is present.
        
        NodeName : Name of the node we are looking for.
        return : -1 if the node is not in the list or it's position."""
        ...
    def GetNodeCount(self)->int:
        """Returns the number of pose nodes stored."""
        ...
    def GetNodeMatrix(self,Index:int)->FBMatrix:
        """Get the pose node matrix.
        
        Index : Index of the node.
        return : a reference to the node's Matrix."""
        ...
    def GetNodeName(self,Index:int)->str:
        """Get the pose node at specified index.
        
        Index : Index of the node."""
        ...
    def GetNodeObject(self,Index:int)->FBModel:
        """Get the pose node object.
        
        Index : Index of the node.
        return : a pointer to the node's Object."""
        ...
    def IsNodeLocalMatrix(self,Index:int)->bool:
        """Get the type of the Matrix for a given node.
        
        Index : Index of the node.
        return : true if the matrix is defined in Local coordinate space."""
        ...
    def RemoveNode(self,Index:int):
        """Remove the pose node at specified index.
        
        Index : Index of the node to be removed."""
        ...
    def SetIsNodeLocalMatrix(self,Index:int,IsNodeLocalMatrix:bool):
        """Set the type of the Matrix for a given node.
        
        Index : Index of the node.
        IsNodeLocalMatrix : True if the matrix of the node is a local matrix."""
        ...
    def SetNodeMatrix(self,Index:int,Matrix:FBMatrix):
        """Set the pose node matrix.
        
        Index : Index of the node.
        Matrix : Matrix to set for this pose node."""
        ...
    def SetNodeObject(self,Index:int,Object:FBModel):
        """Set the pose node object.
        
        Index : Index of the node.
        Object : Object to associate with this pose node."""
        ...
class FBPointCacheManager(FBComponent):
    """Point Cache Manager Interface to the point cache manager.
    See sample: CharacterPointCache.py."""
    AllowCacheResampling:bool
    """Read Write Property: Allow the resample models's existing point cache deformation when true."""
    AlwaysAskForPath:bool
    """Read Write Property: Always ask for the point cache file save path when true."""
    ApplyCacheOnNewModel:bool
    """Read Write Property: Duplicated the cached models, and assoicated the point cache to the new models."""
    ApplyGlobalTransform:bool
    """Read Write Property: Include no-deformable models and the global transform to Vertex Cache when true."""
    CacheAABBox:bool
    """Read Write Property: Cache AABBox (Axis Aligned Bounding Box) when true."""
    CacheNormal:bool
    """Read Write Property: Cache normal when true."""
    CreateFilePerFrameCache:bool
    """Read Write Property: Create the point cache file for each frame when true."""
    CreateMultiChannelCache:bool
    """Read Write Property: Create a single multiple channel point cache file for all models when true."""
    DefaultPath:str
    """Read Write Property: Default point cache file save path."""
    Models:FBPropertyListObject
    """Read Write Property: Models to be recorded"""
    NewModelRoot:FBModel
    """Read Write Property: Valid only when ApplyCacheOnNewModel is on. Create New Models under NewModelRoot. otherwise, a NULL model will be created."""
    SaveEveryFrame:int
    """Read Write Property: Recording Frequency."""
class FBCharacterPose(FBPose):
    """Used to work with character poses.
    This class exposes the object used to store the pose of objects. See sample: MirrorPoseOverTime.py."""
    def ApplyPoseCandidate(self):
        """After setting the candidate on the skeleton node, calling this function will allow subsequent call to get the TRS value of a skeleton node to return the candidate value."""
        ...
    def ClearCharacterExtensionsPose(self):
        """Clear only the pose of the character extensions (omit the character)."""
        ...
    def ClearCharacterPose(self):
        """Clear only the pose of the character (omit the extensions)."""
        ...
    def ClearPose(self):
        """Clear all the data of the pose."""
        ...
    def CopyFrom(self,FromPose:FBCharacterPose):
        """Copy everything from a given object.
        
        FromPose : Pose from which to copy."""
        ...
    def CopyPose(self,Character:FBCharacter):
        """Copy the pose of a character and its extensions.
        
        Character : Character to copy the pose from."""
        ...
    def CopyPoseCharacter(self,Character:FBCharacter):
        """Copy the pose of only the character (omit the extensions).
        
        Character : Character to copy the pose from."""
        ...
    def CopyPoseCharacterExtension(self,CharacterExtension:FBCharacterExtension):
        """Copy the pose of a single character extension.
        
        CharacterExtension : Character extension to copy the pose from."""
        ...
    def CopyPoseCharacterExtensions(self,Character:FBCharacter):
        """Copy the pose of only the character extensions (omit the character).
        
        Character : Character to copy the pose of the extensions from."""
        ...
    def CopyPoseCharacterExtensionsFrom(self,FromPose:FBCharacterPose):
        """Copy the pose data of only the character extensions from a given pose.
        
        FromPose : Pose from which to copy the data."""
        ...
    def CopyPoseCharacterFrom(self,FromPose:FBCharacterPose):
        """Copy the pose data of only the character from a given pose.
        
        FromPose : Pose from which to copy the data."""
        ...
    def CopyPoseDataFrom(self,FromPose:FBCharacterPose):
        """Copy all the pose data from a given pose.
        
        FromPose : Pose from which to copy the data."""
        ...
    def GetCharacterExtensionNameFromPose(self,CharacterExtensionPose:FBObjectPose)->str:
        """Get the name of the character extension for the specified pose.
        
        CharacterExtensionPose : Pose of a character extension to check its name.
        return : The name of the character extension (It is the label name of the character extension)."""
        ...
    def GetCharacterExtensionPose(self,CharacterExtensionName:str)->FBObjectPose:
        """Get the pose of a character extension.
        
        CharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension).
        return : The pose of the character extension, NULL if not found."""
        ...
    def GetCharacterExtensionPoseAt(self,Index:int)->FBObjectPose:
        """Get the pose of a character extension.
        
        Index : Index of the character extension pose to get.
        return : The pose of the character extension."""
        ...
    def GetCharacterExtensionPoseCount(self)->int:
        """Get the number of character extension stored in the pose.
        
        return : Number of character extension stored in the pose."""
        ...
    def GetExtraBoneParentRotationOffset(self,R,Index:int):
        """Get the extra bone transformation offset.
        
        R : A vector that will contains the parent rotation offset value on return.
        Index : Index of the extra bone to get."""
        ...
    def GetExtraBoneTransform(self,T:FBVector3d,R:FBVector3d,S:FBVector3d,Index:int):
        """Get the extra bone transformation.
        
        T : A vector that will contains the translation value on return.
        R : A vector that will contains the rotation value on return.
        S : A vector that will contains the scale value on return.
        Index : Index of the extra bone to get."""
        ...
    def GetExtraBoneTransformOffset(self,T:FBVector3d,R:FBVector3d,S:FBVector3d,Index:int):
        """Get the extra bone transformation offset.
        
        T : A vector that will contains the translation offset value on return.
        R : A vector that will contains the rotation offset value on return.
        S : A vector that will contains the scale offset value on return.
        Index : Index of the extra bone to get."""
        ...
    def GetExtraBones(self)->list:...
    def GetMirrorPlaneEquation(self,MirrorPlaneEquation:FBVector4d,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Get the mirror plane equation that would be used to mirror according to the CharacterPoseOptions.
        
        MirrorPlaneEquation : Out: Mirror plane equation.
        Character : Character to receive the pose.
        CharacterPoseOptions : Options used to paste the pose."""
        ...
    def GetOrCreateCharacterExtensionPose(self,CharacterExtensionName:str)->FBObjectPose:
        """Get the pose of a character extension and create it if necessary.
        
        CharacterExtensionName : Name of the character extension pose to get (It is the label name of the character extension).
        return : The pose of the character extension."""
        ...
    def IsCharacterExtensionPoseStored(self,CharacterExtensionName:str)->bool:
        """Is the pose of the character extension stored in the pose?
        
        CharacterExtensionName : Name of the character extension.
        return : true if the pose of the character extension stored in the pose."""
        ...
    def IsCharacterPoseStored(self)->bool:
        """Is the pose of the character stored in the pose?
        
        return : true if the pose of the character stored in the pose."""
        ...
    def PastePose(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of a character and its extensions.
        
        Character : Character to paste the pose to.
        CharacterPoseOptions : Options used to specify how to paste."""
        ...
    def PastePoseCharacter(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of only the character (omit the extensions).
        
        Character : Character to paste the pose to.
        CharacterPoseOptions : Options used to specify how to paste."""
        ...
    def PastePoseCharacterExtension(self,CharacterExtension:FBCharacterExtension,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of a single character extension.
        
        CharacterExtension : Character extension to paste the pose to.
        CharacterPoseOptions : Options used to specify how to paste."""
        ...
    def PastePoseCharacterExtensions(self,Character:FBCharacter,CharacterPoseOptions:FBCharacterPoseOptions):
        """Paste the pose of only the character extensions (omit the character).
        
        Character : Character to paste the pose of the extensions to.
        CharacterPoseOptions : Options used to specify how to paste."""
        ...
    def RemoveCharacterExtensionPose(self,CharacterExtensionName:str):
        """Remove the pose of a character extension.
        
        CharacterExtensionName : Name of the character extension pose to remove (It is the label name of the character extension)."""
        ...
    def RemoveCharacterExtensionPoseAt(self,Index:int):
        """Remove the pose of a character extension.
        
        Index : Index of the character extension pose to remove."""
        ...
class FBObjectPose(FBPose):
    """FBObjectPose class.
    This class exposes the object used to store the pose of objects."""
    def AddStanceOffset(self,ObjectName:str,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Add the StanceOffset to an object in the pose.
        
        ObjectName : Name of the object.
        StancePose : Pose representing the stance of all objects.
        PoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef)."""
        ...
    def AddStanceOffsetAllObjects(self,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Add the StanceOffset to all the objects in the pose.
        
        StancePose : Pose representing the stance of all objects.
        PoseTransformType : Transform type in which to add the offset (Local, Global or LocalRef)."""
        ...
    def ClearPose(self):
        """Clear all the data of the pose."""
        ...
    def CopyFrom(self,FromPose:FBObjectPose):
        """Copy everything from a given object.
        
        FromPose : Pose from which to copy."""
        ...
    def CopyObjectPose(self,ObjectName:str,Object:FBComponent):
        """Copy the pose of all the properties of an object.
        
        ObjectName : Name of the object to store in the pose.
        Object : Object from which we'll read all the property values to store in the pose."""
        ...
    def CopyPoseAllObjectsTransformFrom(self,FromPose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Copy all the transforms from a given pose.
        
        FromPose : Pose from which to copy the data.
        PoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef)."""
        ...
    def CopyPoseDataFrom(self,FromPose:FBObjectPose):
        """Copy all the pose data from a given pose.
        
        FromPose : Pose from which to copy the data."""
        ...
    def CopyPoseTransformFrom(self,FromPose:FBObjectPose,ObjectName:str,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Copy the transforms of an object from a given pose.
        
        FromPose : Pose from which to copy the data.
        ObjectName : Name of object to copy the transform from.
        PoseTransformType : Transform type from which to copy the transform (Local, Global or LocalRef)."""
        ...
    def CopyPropertyPose(self,ObjectName:str,Property:FBProperty):
        """Copy the pose of a property of an object.
        
        ObjectName : Name of the object to store in the pose.
        Property : Property from which we'll read the value to store in the pose."""
        ...
    def CopyTransform(self,ObjectName:str,Object:FBComponent,ObjectPoseOptions:FBObjectPoseOptions):
        """Copy the transform of an object.
        
        ObjectName : Name of the object to store in the pose.
        Object : Object from which we'll evaluate the transform values to store in the pose.
        ObjectPoseOptions : PoseOptions used to specify the transform of the reference object (Default: Identity)."""
        ...
    def GetPropertyValue(self,Value:float,Size:int,ObjectName:str,PropertyName:str):
        """Get the value of a property stored in the pose.
        
        Value : Value to get.
        Size : Number of elements inValue.
        ObjectName : Name of the object to get the value.
        PropertyName : Name of the property to get the value."""
        ...
    def GetStoredObjectNames(self)->FBStringList:
        """Get all the object names currently stored in this pose.
        
        return : All the object names currently stored in this pose."""
        ...
    def GetTransform(self,T:FBVector3d,RM:FBMatrix,SM:FBMatrix,ObjectName:str,PoseTransformType:FBPoseTransformType)->bool:
        """Get the transform of an object in the pose.
        
        T : Translation to get.
        RM : Rotation to get.
        SM : Scaling to get.
        ObjectName : Name of the object to get the transform.
        PoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef).
        return : True if the transform was found in the pose."""
        ...
    def IsPropertyPoseable(self,Property:FBProperty)->bool:
        """Is the property poseable?
        
        Property : FBProperty
        return : True if the value of this property can be stored in the pose."""
        ...
    def IsPropertyStored(self,ObjectName:str,PropertyName:str)->bool:
        """Is the property stored in the pose?
        
        ObjectName : Name of the object.
        PropertyName : Name of the property.
        return : True if the property is stored in the pose."""
        ...
    def IsTransformStored(self,ObjectName:str,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid)->bool:
        """Is the transform of this object stored in the specified TransformType?
        
        ObjectName : Name of the object.
        PoseTransformType : Transform type in which to check.
        return : True if the transform of this object is stored in the specified TransformType (Local, Global and LocalRef)."""
        ...
    def MirrorPose(self,ObjectName:str,ObjectPoseMirrorOptions:FBObjectPoseMirrorOptions):
        """Mirror the transform of an object in the pose.
        
        ObjectName : Name of the object to mirror.
        ObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane."""
        ...
    def MirrorPoseAllObjects(self,ObjectPoseMirrorOptions:FBObjectPoseMirrorOptions):
        """Mirror the transform of all objects in the pose.
        
        ObjectPoseMirrorOptions : MirrorOptions used to specify the mirror plane."""
        ...
    def MultTransform(self,ObjectName:str,GX:FBMatrix,TransformAttribute:FBModelTransformationType,PoseTransformType:FBPoseTransformType):
        """Multiply the transform of an objects in the pose.
        
        ObjectName : Name of the object.
        GX : Transformation matrix to apply.
        TransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation.
        PoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef)."""
        ...
    def MultTransformAllObjects(self,GX:FBMatrix,TransformAttribute:FBModelTransformationType,PoseTransformType:FBPoseTransformType):
        """Multiply the transform of all objects in the pose.
        
        GX : Transformation matrix to apply.
        TransformAttribute : Transform attribute to affect. Supported: T,R,S and Transformation.
        PoseTransformType : Transform type in which to mult the transform (Local, Global or LocalRef)."""
        ...
    def PasteObjectPose(self,ObjectName:str,Object:FBComponent):
        """Paste the pose of all the properties of an object.
        
        ObjectName : Name of the object stored in the pose.
        Object : Object which will receive the values stored in the pose."""
        ...
    def PastePropertyPose(self,ObjectName:str,Property:FBProperty):
        """Paste the pose of a property of an object.
        
        ObjectName : Name of the object stored in the pose.
        Property : Property which will receive the value stored in the pose."""
        ...
    def PasteTransform(self,ObjectName:str,Object:FBComponent,ObjectPoseOptions:FBObjectPoseOptions):
        """Paste the transform of an object.
        
        ObjectName : Name of the object stored in the pose.
        Object : Object which will receive the transform values stored in the pose.
        ObjectPoseOptions : PoseOptions used to specify the transform of the reference object, the TransformType and TransformAttributes to paste.
        EvaluateInfo : Information concerning the evaluation of the animation (time, etc.)"""
        ...
    def RemoveStanceOffset(self,ObjectName:str,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Remove the StanceOffset from an object in the pose.
        
        ObjectName : Name of the object.
        StancePose : Pose representing the stance of all objects.
        PoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef)."""
        ...
    def RemoveStanceOffsetAllObjects(self,StancePose:FBObjectPose,PoseTransformType:FBPoseTransformType=FBPoseTransformType.kFBPoseTransformInvalid):
        """Remove the StanceOffset from all the objects in the pose.
        
        StancePose : Pose representing the stance of all objects.
        PoseTransformType : Transform type in which to remove the offset (Local, Global or LocalRef)."""
        ...
    def SetPropertyValue(self,ObjectName:str,PropertyName:str,Value:float,Size:int):
        """Set the value of a property in the pose.
        
        ObjectName : Name of the object to set the value.
        PropertyName : Name of the property to set the value.
        Value : Value to set.
        Size : Number of elements inValue."""
        ...
    def SetTransform(self,T:FBVector3d,RM:FBMatrix,SM:FBMatrix,ObjectName:str,PoseTransformType:FBPoseTransformType):
        """Set the transform of an object in the pose.
        
        T : Translation to set.
        RM : Rotation to set.
        SM : Scaling to set.
        ObjectName : Name of the object to set the transform.
        PoseTransformType : Transform type in which to set the transform (Local, Global or LocalRef)."""
        ...
class FBCluster(FBComponent):
    """Weighting interface for meshes.
    This class is experimental. See sample: FBClusterTransactions.py."""
    ClusterAccuracy:float
    """Read Write Property: Cluster accuracy."""
    ClusterMode:FBClusterMode
    """Read Write Property: Cluster mode."""
    def ClusterBegin(self,Index:int=-1)->int:
        """Begin cluster definition.
        
        Index : Link index.
        return : Index of last item(default=-1)."""
        ...
    def ClusterEnd(self)->int:
        """End cluster definition.
        
        return : 0, (Not implemented)."""
        ...
    def LinkClearUnused(self,Threshold:float=-1.0):
        """Remove all unused links.
        
        Threshold : Weight value under which links are considered unused (default=-1)."""
        ...
    def LinkGetAssociateModel(self,LinkNumber:int)->FBModel:
        """Get model associated with link.
        
        LinkNumber : Number value of link to get associated model from.
        return : Model associated to link numberLinkNumber."""
        ...
    def LinkGetCount(self)->int:
        """Get number of links.
        
        return : Number of links."""
        ...
    def LinkGetModel(self,LinkNumber:int)->FBModel:
        """Get model from a link.
        
        LinkNumber : Number value of link to get model from.
        return : Model at link numberLinkNumber."""
        ...
    def LinkGetName(self,LinkNumber:int)->str:
        """Get the name of a link.
        
        LinkNumber : Number value of link to get name from.
        return : Name of link numberLinkNumber."""
        ...
    def LinkGetVertexIndex(self,Index:int)->int:
        """Get current vertex at link.
        
        Index : Index of link to get vertex from.
        return : Index value of the current vertex associated to link at index numberIndex"""
        ...
    def LinkRemove(self,LinkNumber:int):
        """Remove a link.
        
        LinkNumber : Number value of link to rename."""
        ...
    def LinkSetCurrentVertex(self,LinkIndex:int,PointIndex:int):
        """Link at current vertex.
        
        LinkIndex : Index of link to add vertex to.
        PointIndex : Index of vertex to add."""
        ...
    def LinkSetModel(self,Model:FBModel):
        """Set model to a link.
        
        Model : Model to set."""
        ...
    def LinkSetName(self,Name:str,LinkNumber:int):
        """Set the name of a link.
        
        Name : Name of the link.
        LinkNumber : Number value of link to name."""
        ...
    def VertexAdd(self,VertexIndex:int,Weight:float):
        """Add a vertex to a cluster.
        
        VertexIndex : Index of vertex to add.
        Weight : Weight to give to vertex."""
        ...
    def VertexClear(self):
        """Clear all linked vertices."""
        ...
    def VertexGetCount(self)->int:
        """Get the number of vertices.
        
        return : Number of vertices in a cluster."""
        ...
    def VertexGetNumber(self,Index:int)->int:
        """Get vertex number.
        
        Index : Index of link to get vertex from.
        return : Number value of vertex at link numberIndex"""
        ...
    def VertexGetTransform(self,Position:FBVector3d,Rotation:FBVector3d,Scaling:FBVector3d):
        """Get transform of a cluster set.
        
        Position : Position transform.
        Rotation : Rotation transform.
        Scaling : Scaling transform."""
        ...
    def VertexGetWeight(self,Index:int)->float:
        """Get vertex weight.
        
        Index : Index of link to get vertex from.
        return : Weight of vertex found at link numberIndex."""
        ...
    def VertexRemove(self,VertexIndex:int):
        """Remove a vertex from a cluster.
        
        VertexIndex : Index of vertex to remove."""
        ...
    def VertexSetTransform(self,Position:FBVector3d,Rotation:FBVector3d,Scaling:FBVector3d):
        """Set transform of a cluster set.
        
        Position : Position transform.
        Rotation : Rotation transform.
        Scaling : Scaling transform."""
        ...
    def VertexSetWeight(self,Weight:float,Index:int):
        """Set vertex weight.
        
        Weight : Weight to give to vertex.
        Index : Index of link to get vertex from."""
        ...
class FBCharacterMarkerSet(FBComponent):
    """Character marker set class.
    These classes are under development and may change dramatically between versions."""
    def GetExtractionProperty(self,NodeId:FBBodyNodeId)->FBProperty:
        """Get the extraction property associated with each body part of the character.
        
        NodeId : FBBodyNodeId
        return : The property associated with givenNodeId."""
        ...
    def GetMarkersProperty(self,NodeId:FBBodyNodeId)->FBProperty:
        """Get the marker property associated with each body part of the character.
        
        NodeId : FBBodyNodeId
        return : The property associated with givenNodeId."""
        ...
    def GetSnapProperty(self,NodeId:FBBodyNodeId,What:FBModelTransformationType)->FBProperty:
        """Get the snap property associated with each body part of the character for given transformation.
        Current version snap only translation and rotation.
        
        NodeId : FBBodyNodeId
        What : FBModelTransformationType
        return : The property associated with givenNodeId andWhat."""
        ...
class FBCameraSwitcherAudioManager(FBComponent):
    """Camera Switcher Audio Manager class.
    This class allows users to interact with the Audio Manager of the Camera Switcher."""
    def GetAudioClip(self)->FBAudioClip:
        """Get the Audio Clip displayed on the Camera Switcher.
        
        return : The Audio Clip displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetAudioTrack(self)->FBStoryTrack:
        """Get the Audio Track displayed on the Camera Switcher.
        
        return : The Audio Track displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetLockPitchToSpeed(self)->bool:
        """Get the 'Lock Pitch to Speed' state.
        
        return : True if the 'Lock Pitch to Speed' state is set, false otherwise."""
        ...
    def GetShowAudio(self)->bool:
        """Get the 'Show Audio' state.
        
        return : True if the 'Show Audio' state is set, false otherwise."""
        ...
    def GetShowLeftChannel(self)->bool:
        """Get the 'Show Left Channel' state.
        
        return : True if the 'Show Left Channel' state is set, false otherwise."""
        ...
    def GetShowRightChannel(self)->bool:
        """Get the 'Show Right Channel' state.
        
        return : True if the 'Show Right Channel' state is set, false otherwise."""
        ...
    def RemoveAudio(self)->bool:
        """Remove the audio clip or audio track currently displayed on the Camera Switcher.
        
        return : True if the operation is successful, false otherwise."""
        ...
    def SetAudioClip(self,AudioClip:FBAudioClip)->bool:
        """Set the Audio Clip to display on the Camera Switcher.
        
        AudioClip : The Audio Clip to display.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetAudioTrack(self,AudioTrack:FBStoryTrack)->bool:
        """Set the Audio Track to display on the Camera Switcher.
        
        AudioTrack : The Audio Track to display.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetLockPitchToSpeed(self,Lock:bool)->bool:
        """Set the 'Lock Pitch to Speed' state.
        
        Lock : True to lock pitch to speed, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowAudio(self,Show:bool)->bool:
        """Set the 'Show Audio' state.
        
        Show : True to show the Audio waveform, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowLeftChannel(self,Show:bool)->bool:
        """Set the 'Show Left Channel' state.
        
        Show : True to show the left channel, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowRightChannel(self,Show:bool)->bool:
        """Set the 'Show Right Channel' state.
        
        Show : True to show the right channel, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
class FBBox(FBComponent):
    """A box is a fundamental building block in the application architecture.
    All animatable elements are derived in some way from the main box class, either by deriving directly or owning a box."""
    Animatable:bool
    """Read Write Property: Is the box animatable."""
    Live:bool
    """Read Write Property: Is live?"""
    RecordMode:bool
    """Read Write Property: Is recording?"""
    UniqueName:str
    """internal Unique name."""
    def AnimationNodeDestroy(self,AnimationNode:FBAnimationNode)->bool:
        """Destroy an animation node.
        
        AnimationNode : Handle to the animation node to be destroyed.
        return : true if destruction was successful."""
        ...
    def AnimationNodeInGet(self)->FBAnimationNode:
        """Get the (IN/OUT) animation node for this box.
        
        return : A handle to the animation node for this box."""
        ...
    def AnimationNodeIsUserData(self,AnimationNode:FBAnimationNode)->bool:
        """Is the animation node user data?
        
        AnimationNode : Handle to the animation to be queried.
        return : true if node is user data."""
        ...
    def AnimationNodeOutGet(self)->object:...
    def GetInConnector(self,Index:int)->FBAnimationNode:
        """Get the animation node input associated with the given index.
        
        Index : The animation node input associated with the given index.
        return : The animation node input, or NULL if theIndex value is invalid."""
        ...
    def GetInConnectorCount(self)->int:
        """Get the number of animation node inputs for this box.
        
        return : The number of animation node inputs for this box."""
        ...
    def GetOutConnector(self,Index:int)->FBAnimationNode:
        """Get the animation node output associated with the given index.
        
        Index : The animation node output associated with the given index.
        return : The animation node output, or NULL if theIndex value is invalid."""
        ...
    def GetOutConnectorCount(self)->int:
        """Get the number of animation node outputs for this box.
        
        return : The number of animation node outputs for this box."""
        ...
class FBAudioOut(FBComponent):
    """Audio Out class.
    Properties of this class are work in progress, but you can still list them and get their names."""
    ...
class FBBoxPlaceHolder(FBBox):
    """Wrapper around a specific instance of a FBBox object.
    This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying box. The underlying box will usually be a device. Instantiation of FBBoxPlaceHolder should be left to the the system."""
    Box:FBBox
    """Read Only Property: Underlying box object."""
class FBConstraint(FBBox):
    """Base class for constraints."""
    Active:bool
    """Read Write Property: Active state."""
    Deformer:bool
    """Read Write Property: Is a deformer constraint?"""
    Description:str
    """Read Write Property: Long description of constraint."""
    HasLayout:bool
    """Read Write Property: Does the constraint have a layout?"""
    Lock:bool
    """Read Write Property: Lock state."""
    Weight:float
    """Read Write Property: Weight of constraint."""
    def AnimationNodeInCreate(self,UserId:object,Property:FBProperty,arg4:str)->FBAnimationNode:
        """Animation Node Creations (IN).
        Used to create the In connectors on an animation node. This function will return a newly created animation node, connected to the model specified byProperty.
        
        UserId : User specified reference number.
        Property : Property of model to animate (must be animatable)
        return : Newly created IN animation node."""
        ...
    def AnimationNodeOutCreate(self,UserId:object,Model:FBModel,Attribute:str)->FBAnimationNode:
        """Animation Node Creations (IN/OUT).
        Used to create the connectors (in or out) on an animation node. This function will return a newly created animation node, connected to the model specified byModel.
        
        UserId : User specified reference number.
        Model : Model to associate with animation node.
        Attribute : Attribute of model to animate (i.e. Translation, Lcl Translation, etc.)
        return : Newly created IN/OUT animation node."""
        ...
    def Clone(self)->FBConstraint:
        """Clone the constraint.
        
        return : Newly created (and copied) constraint."""
        ...
    def DeformerBind(self,Model:FBModel)->bool:
        """Bind/UnbindModel to deformation constraint.
        These functions are used for adding/removing a deformation binding to/fromModel if the constraint is a deformation constraint.
        
        Model : Model to bind/unbind.
        return : true if successful."""
        ...
    def DeformerUnBind(self,Model:FBModel)->bool:
        """Model : FBModel"""
        ...
    def Disable(self,Model:FBModel)->bool:
        """Disable constraint onModel.
        
        Model : Model on which constraint should be disabled.
        return : true if successful."""
        ...
    def FreezeSRT(self,Model:FBModel,S:bool,R:bool,T:bool):
        """Freeze current model state.
        
        Model : Model to freeze constraint on.
        S : Scaling freeze?
        R : Rotation freeze?
        T : Translation freeze?"""
        ...
    def FreezeSuggested(self):
        """Suggest 'freeze'."""
        ...
    def ReferenceAdd(self,GroupIndex:int,Model:FBModel)->bool:
        """Add a reference to a specified group.
        
        GroupIndex : Group to add reference to.
        Model : Model to place at new reference.
        return : true if successful."""
        ...
    def ReferenceGet(self,GroupIndex:int,ItemIndex:int=0)->FBModel:
        """Get a reference.
        
        GroupIndex : Index of reference group containing desired reference.
        ItemIndex : Index of reference in group to get (default is 0).
        return : Model at specified reference."""
        ...
    def ReferenceGetCount(self,GroupIndex:int)->int:
        """Get number of references in a specified group.
        
        GroupIndex : Index of group to query the number of references.
        return : Number of references in specified group."""
        ...
    def ReferenceGroupAdd(self,GroupName:str,MaxItemCount:int)->int:
        """Add a group of references.
        
        GroupName : Name of reference group to add.
        MaxItemCount : Maximum number of items inGroupName.
        return : Index of new reference group."""
        ...
    def ReferenceGroupGetCount(self)->int:
        """Return the number of reference groups.
        
        return : Number of reference groups."""
        ...
    def ReferenceGroupGetMaxCount(self,GroupIndex:int)->int:
        """Get the maximum number of items that can exist in the reference group in question.
        
        GroupIndex : Index of reference group.
        return : Maximum number of items that can be added to the reference group."""
        ...
    def ReferenceGroupGetName(self,GroupIndex:int)->str:
        """Get the name of the reference group.
        
        GroupIndex : Index of the reference group to get the name for.
        return : The name of the reference groupGroupIndex."""
        ...
    def ReferenceRemove(self,GroupIndex:int,Model:FBModel)->bool:
        """Remove a reference toModel from the group atGroupIndex.
        
        GroupIndex : Index to remove reference from.
        Model : Model to remove reference from.
        return : true if successful."""
        ...
    def RemoveAllAnimationNodes(self):
        """Remove animation nodes."""
        ...
    def RestoreModelState(self,Model:FBModel):
        """Restore the saved model state ontoModel.
        
        Model : Model to affect with previous state."""
        ...
    def SaveModelState(self,Model:FBModel,S:bool,R:bool,T:bool):
        """Save current state ofModel.
        
        Model : Model to save.
        S : Scaling information?
        R : Rotation information?
        T : Translation information?"""
        ...
    def SetupAllAnimationNodes(self):
        """Setup animation nodes."""
        ...
    def SnapSuggested(self):
        """Suggest 'snap'."""
        ...
class FBModelPlaceHolder(FBBoxPlaceHolder):
    """Wrapper around a specific instance of a FBModel object.
    This class is mainly used with a constraint relation to have multiple boxes that are a representation of the same underlying model. Instantiation of FBModelPlaceHolder should be left to the the system."""
    Model:FBModel
    """Read Only Property: Underlying model object."""
    UseGlobalTransforms:bool
    """Read Write Property: Indicate if the translations are expressed in local or global mode."""
class FBCharacterSolver(FBConstraint):
    """Constraint class."""
    ExtraBones:property
    """Read Property: List of Extra Bones in character"""
    ExtraFK:property
    """Read Property: List of Extra FK in character"""
    Source:FBComponent
    """Read Write Property: Source character when doing a character retarget."""
    def GetParentRotationOffset(self,R)->FBVector3d:
        """Get the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.
        
        R : Offset Rotation between the Bone and is parent at Stance Pose.
        Index : Index of extra Bone to get."""
        ...
    def GetRegisteredSolverNames(self)->list:...
    def GetTarget(self)->object:...
    def GetTransformationOffset(self,arg2:FBModel)->list:...
    def SetParentRotationOffset(self,R,Index:int):
        """Set the Parent Rotation Offset of the Given Extra Bone Index.
        The rotation Offset if extracted at Characterisation (in Stance Pose). You don't need this value if the parent of the bone is characterized too.
        
        R : Offset Rotation between the Bone and is parent at Stance Pose.
        Index : Index of extra Bone to get."""
        ...
    def SetTransformationOffset(self,arg2:FBModel,arg3:FBVector3d,arg4:FBVector3d,arg5:FBVector3d):...
class FBCharacterFace(FBConstraint):
    """Animates a character face using an actor as input.
    These classes are under development and may change dramatically between versions."""
    ActiveInput:bool
    """Read Write Property: Is the character input active?"""
    InputActorFace:FBActorFace
    """Read Write Property: The index of the actor used for the input."""
    def ClusterGroupAdd(self,List:FBModelList,Name:str=None)->int:
        """Add a cluster group to the character face.
        
        List : List of clusters to add to this group.
        Name : Optional name to assign to this cluster group.
        return : Index of the new cluster group -1 if the operation failed to complete."""
        ...
    def ClusterGroupFindByName(self,Name:str)->int:
        """Find a cluster group by name.
        
        Name : Name to search for on the face.
        return : Index of the matching cluster group. -1 if not found."""
        ...
    def ClusterGroupGetCount(self)->int:
        """Retrieve the total number of cluster groups.
        
        return : Number of cluster groups on the face."""
        ...
    def ClusterGroupGetName(self,ClusterGrpId:int)->str:
        """Retrieve the name of a cluster group.
        
        ClusterGrpId : Index of the cluster group to query.
        return : Name of the specified cluster group."""
        ...
    def ClusterGroupRemove(self,ClusterGrpId:int)->bool:
        """Remove a cluster group from the character face.
        
        ClusterGrpId : Index of the cluster group to remove.
        return : True if the operation completed successfully."""
        ...
    def ClusterGroupSetName(self,ClusterGrpId:int,Name:str)->bool:
        """Set the name of a cluster group.
        
        ClusterGrpId : Index of the cluster group to modify.
        Name : New name for the cluster group.
        return : True of the operation completed successfully."""
        ...
    def ClusterGroupSnapRest(self,ClusterGrpId:int)->bool:
        """Set a cluster group's rest pose to the current pose.
        
        ClusterGrpId : Index of the cluster group to modify.
        return : True if the operation completed succesfully."""
        ...
    def ClusterShapeAdd(self,ClusterGrpId:int,Name:str=None)->int:
        """Add a cluster shape to a cluster group.
        
        ClusterGrpId : Index of the cluster group to modify.
        Name : Optional name to assign to the shape.
        return : Index of the new shape. -1 if the operation failed to complete."""
        ...
    def ClusterShapeFindByName(self,ClusterGrpId:int,Name:str)->int:
        """Find a cluster shape in a cluster group by name.
        
        ClusterGrpId : Index of the cluster group to search.
        Name : Name to search for in the cluster group.
        return : Index of the matching shape. -1 if not found."""
        ...
    def ClusterShapeGetCount(self,ClusterGrpId:int)->int:
        """Retrieve the total number of shapes in a cluster group.
        
        ClusterGrpId : Index of the cluster group to query.
        return : Number of shapes in the specified cluster group."""
        ...
    def ClusterShapeGetName(self,ClusterGrpId:int,ClusterShapeId:int)->str:
        """Retrieve the name of a shape in a cluster group.
        
        ClusterGrpId : Index of the cluster group to query.
        ClusterShapeId : Index of the cluster shape to query.
        return : Name of the specified shape."""
        ...
    def ClusterShapeRemove(self,ClusterGrpId:int,ClusterShapeId:int)->bool:
        """Remove a cluster shape from a cluster group.
        
        ClusterGrpId : Index of the cluster group to modify.
        ClusterShapeId : Index of the shape in the cluster group to remove.
        return : True of the operation completed succesfully."""
        ...
    def ClusterShapeSetName(self,ClusterGrpId:int,ClusterShapeId:int,Name:str)->bool:
        """Set the name of a shape in a cluster group.
        
        ClusterGrpId : Index of the cluster group to modify.
        ClusterShapeId : Index of the cluster shape to modify.
        Name : Name to assign to the cluster shape.
        return : True if the operation completed successfully."""
        ...
    def ClusterShapeSnap(self,ClusterGrpId:int,ClusterShapeId:int)->bool:
        """Record the current pose of the cluster group to a cluster shape.
        
        ClusterGrpId : Index of the cluster group to record.
        ClusterShapeId : Index of the cluster shape to record the pose.
        return : True if the operation completed successfully."""
        ...
    def ExpressionAdd(self,Name:str)->int:
        """Add an expression to the face.
        
        Name : Optional name to assign to the new expression.
        return : Index of the new expression. -1 if the operation failed to complete."""
        ...
    def ExpressionFindByName(self,Name:str)->int:
        """Find an expression on the face by name.
        
        Name : Name of the expression to search for.
        return : Index of the matching expression. -1 if not found."""
        ...
    def ExpressionGetCount(self)->int:
        """Retrieve the total number of expressions on the face.
        
        return : Number of expressions on the face."""
        ...
    def ExpressionGetName(self,ExpressionId:int)->str:
        """Retrieve the name of an expression.
        
        ExpressionId : Index of the expression to query.
        return : Name of the specified expression."""
        ...
    def ExpressionGetShapeWeight(self,ExpressionId:int,GrpId:int,ShapeId:int)->float:
        """Retrieve the weight of a shape to an expression.
        
        ExpressionId : Index of the expression.
        GrpId : Index of the blendshape or cluster group containing the shape of interest.
        ShapeId : Index of the blendshape or cluster shape.
        return : Weight of the desired shape to an expression. A weight of 0.0 represents 0%, while a weight of 1.0 represents 100%. Returns 0.0 if the weight cannot be found."""
        ...
    def ExpressionRemove(self,ExpressionId:int)->bool:
        """Remove an expression from the face.
        
        ExpressionId : Index of the expression to remove.
        return : True if the operation completed successfully."""
        ...
    def ExpressionSetName(self,ExpressionId:int,Name:str)->bool:
        """Set the name of an expression.
        
        ExpressionId : Index of the expression to modify.
        Name : Name to assign to the expression.
        return : True if the operation completed successfully."""
        ...
    def ExpressionSetShapeWeight(self,ExpressionId:int,GrpId:int,ShapeId:int,Value:float=0.0)->bool:
        """Assign the weight of a shape to an expression.
        
        ExpressionId : Index of the expression to modify.
        GrpId : Index of the blendshape or cluster group containing the shape of interest.
        ShapeId : Index of the blendshape or cluster shape to weight.
        Value : Weight of the shape to assign to this expression. A weight of 0.0 represents 0%, while a weight of 1.5 represents 150%. The weight cannot be less than 0.0; if so, the weight will be clamped to 0.0.
        return : True if the operation completed successfully."""
        ...
    def GotoRest(self):
        """Set the character face back to its rest shape."""
        ...
    def PlotAnimation(self)->bool:
        """Plot the animation of the character face.
        
        return : True if the operation completed successfully."""
        ...
    def ShapeFindByName(self,ShapeGrpId:int,Name:str)->int:
        """Find a shape in a blendshape group by name.
        
        ShapeGrpId : Index of the blendshape group to search.
        Name : Name to search for.
        return : Index of the shape, -1 if not found."""
        ...
    def ShapeGetCount(self,ShapeGrpId:int)->int:
        """Retrieve the total number of shapes in a blendshape group.
        
        ShapeGrpId : Index of the blendshape group to query.
        return : Number of shapes in the specified blendshape group."""
        ...
    def ShapeGetName(self,ShapeGrpId:int,ShapeId:int)->str:
        """Retrieve the name of the shape in a blendshape group.
        
        ShapeGrpId : Index of the blendshape group to query.
        ShapeId : Index of the shape in the blendshape group to query.
        return : Name of the specified shape."""
        ...
    def ShapeGroupAdd(self,List:FBModelList,Name:str=None)->bool:
        """Add a blendshape model group for each input model.
        
        List : List of models to create a blendshape model group.
        Name : Unused. Instead, use the ShapeGroupGetName member function to set the name of each added blendshape model group individually.
        return : True if the operation completed successfully, false otherwise."""
        ...
    def ShapeGroupFindByName(self,Name:str)->int:
        """Find a blendshape group by name.
        
        Name : Name to search for.
        return : Index of the blendshape group, -1 if not found."""
        ...
    def ShapeGroupGetCount(self)->int:
        """Retrieve the total number of blendshape groups on this character face.
        
        return : Number of blendshape groups on this character face."""
        ...
    def ShapeGroupGetName(self,ShapeGrpId:int)->str:
        """Retrieve the name of a blendshape group.
        
        ShapeGrpId : Index of the blendshape group to query.
        return : Name of the blendshape group."""
        ...
    def ShapeGroupRemove(self,ShapeGrpId:int)->bool:
        """Remove a blendshape model group.
        
        ShapeGrpId : Index of the blendshape group to remove.
        return : True if the operation completed successfully."""
        ...
    def ShapeGroupSetName(self,ShapeGrpId:int,Name:str)->bool:
        """Set the name of a blendshape group.
        
        ShapeGrpId : Index of the blendshape group to modify.
        Name : Name to set on the blendshape group.
        return : True if the operation completed successfully."""
        ...
    def ShapeSetName(self,ShapeGrpId:int,ShapeId:int,Name:str)->bool:
        """Set the name of the shape in a blendshape group.
        
        ShapeGrpId : Index of the blendshape group to query.
        ShapeId : Index of the shape in the blendshape group to set.
        Name : Name to set on the shape.
        return : True if the operation completed successfully."""
        ...
class FBCharacter(FBConstraint):
    """A character is the link between a motion source and a character model.
    These classes are under development and may change dramatically between versions. This class exposes part of the functionality associated with a Character. A character can possess a number of potential sources at the same time, such as an actor and another character, but with only one active at any given time. Before setting the InputType to the desired value, one must make sure to have previously set either the InputCharacter or the InputActor.To obtain the list of characters present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of characters in the property Characters.
    
    >>> FBSystem lSystem;
    FBScene* lScene = lSystem.Scene;
    for( int lIdx = 0; lIdx < lScene->Characters.GetCount(); ++lIdx )
    {
    FBTrace( 'Character[%d]: '%s'
    ', lIdx, (char*)lScene->Characters[lIdx] );
    }
    
    
    The current character selected in the Character tool can be obtained via the FBApplication object.
    
    >>> FBApplication lApplication;
    FBCharacter* lCharacter = lApplication.CurrentCharacter;
    if( lCharacter )
    {
    FBTrace( 'Current character is: '%s'
    ', (char*)lCharacter->Name );
    }
    else
    {
    FBTrace( 'No character currently selected
    ' );
    }
    
    
    See samples: CharacterMarkerSet.py, EnableGameModeOnSelectedCharacters_Z.py, MirrorPoseOverTime.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py."""
    ActiveInput:bool
    """Read Write Property: Is the character input active?"""
    CharacterExtensions:FBPropertyListCharacterExtension
    """List: Character Extensions in the character."""
    ContactBehaviour:FBCharacterContactBehaviour
    """Read Write Property: Contact Behavior selection."""
    FKFingerMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered intermediate finger phalanges."""
    FKFingerTipMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered finger tip phalanges."""
    FKThumbTipMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered thumb tip phalanges."""
    HipsTranslationMode:FBCharacterHipsTranslationMode
    """Read Write Property: Hips Translation Mode."""
    HumanFingerLimits:bool
    """Read Write Property: Enables/Disables human finger limits during actor solve."""
    InputActor:FBActor
    """Read Write Property: The index of the actor used for the input."""
    InputCharacter:FBCharacter
    """Read Write Property: The index of the character used for the input."""
    InputType:FBCharacterInputType
    """Read Write Property: The input type for the character (ex: Actor)."""
    InverseLeftElbow:bool
    """Read Write Property: Is left elbow inverted."""
    InverseLeftKnee:bool
    """Read Write Property: Is left knee inverted."""
    InverseRightElbow:bool
    """Read Write Property: Is right elbow inverted."""
    InverseRightKnee:bool
    """Read Write Property: Is right knee inverted."""
    KeyingMode:FBCharacterKeyingMode
    """Read Write Property: The current keying mode."""
    LeftElbowKillPitch:bool
    """Read Write Property: is Pitch used for Left elbow."""
    LeftHandIndexIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddlePinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftKneeKillPitch:bool
    """Read Write Property: is Pitch used for Left knee."""
    LockX:bool
    """Read Write Property: Lock character skeleton in place on X axis."""
    LockY:bool
    """Read Write Property: Lock character skeleton in place on Y axis."""
    LockZ:bool
    """Read Write Property: Lock character skeleton in place on Z axis."""
    MirrorMode:bool
    """Read Write Property: is in mirror mode."""
    RightElbowKillPitch:bool
    """Read Write Property: is Pitch used for Right elbow."""
    RightHandIndexIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddlePinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightKneeKillPitch:bool
    """Read Write Property: is Pitch used for Right knee."""
    RollSolver:FBCharacterRollSolver
    """Read Write Property: Roll Solver selection."""
    ShoulderCorrection:float
    """Read Write Property: shoulder correction values."""
    SyncMode:bool
    """Read Write Property: is character in sync mode."""
    WriteReference:bool
    """Read Write Property: are we writing back on reference."""
    def AddCharacterExtension(self,Ext:FBCharacterExtension):
        """AddCharacterExtension.
        
        Ext : extension to be added to the character."""
        ...
    def ConnectControlRig(self,ControlSet:FBControlSet,UpdateLimit:bool,ResetHierarchy:bool):
        """Connect a Control-Rig to the character.
        
        ControlSet : The control set to connect. NULL will disconnect the Control-Rig from the character.
        UpdateLimit : Whether to update the models' limit for a character. E.g. the Pre rotation and post rotation.
        ResetHierarchy : Whether to reset hierarchy for a character."""
        ...
    def CopyAnimation(self):
        """Copy the animation from the input character to us."""
        ...
    def CreateAuxiliary(self,EffectorId:FBEffectorId,Pivot:bool,AuxReachT:float=100,AuxReachR:float=100)->bool:
        """Create auxiliary on effector.
        
        EffectorId : The effector ID.
        Pivot : Create effector or pivot (pivot offset should be set on IKPivot property, at creation default values are set).
        AuxReachT : Default auxiliary effector reach for translation (IK Blend T since MotionBuilder 2013).
        AuxReachR : Default auxiliary effector reach for rotation (IK Blend R since MotionBuilder 2013).
        return : True if auxiliary was created (can fail if FBLastEffectorSetIndex limit reached)."""
        ...
    def CreateCharacterMarkerSet(self,SetActive:bool)->bool:
        """Create the Character Marker Set.
        
        SetActive : True when new input should be set and active.
        return : True when marker got created and connected to character."""
        ...
    def CreateControlRig(self,SetFKIK:bool)->bool:
        """Create the Control-Rig.
        
        SetFKIK : true to use FK/IK or false to use IK only.
        return : current state of the flag after the operation (true if it did succeed)."""
        ...
    def CycleAnalysisCurrentCharacter(self):
        """Run Cycle Analysis on current character."""
        ...
    def DisconnectControlRig(self):
        """Disconnect the Control-Rig from the character."""
        ...
    def GetActiveBodyPart(self)->list:
        """Get the active body part array.
        
        ActivePart : A pointer to an array of bool. On return, the index with a "true" value are active part."""
        ...
    def GetCharacterMarkerSet(self,Force:bool=False)->FBCharacterMarkerSet:
        """Obtain Input CharacterMarkerSet.
        
        Force : If True, will return the current CharacterMarkerSet even if the character is not in CharacterMarkerSet Input.
        return : Return current Active CharacterMarkerSet, NULL if none."""
        ...
    def GetCharacterize(self)->bool:
        """Get Characterize flag.
        
        return : Current state of the Characterize flag."""
        ...
    def GetCharacterizeError(self)->str:
        """Get error message for the previous SetCharacterizeOn operation.
        
        return : The string containing all errors and warnings."""
        ...
    def GetCtrlRigModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the model associated with each body part in the Control Rig of the character.
        
        BodyNodeId : FBBodyNodeId
        return : The model in the Control Rig corresponding to the specified body part."""
        ...
    def GetCurrentControlSet(self)->FBControlSet:
        """Obtain Input ControlSet.
        
        Force : If True, will return the current ControlSet even if the character is not in ControlSet Input.
        return : Return current Active ControlSet, NULL if none."""
        ...
    def GetCycleAnalysisNode(self)->FBCycleAnalysisNode:
        """Get the Cycle Analysis Node from the current character.
        
        return : Cycle Analysis Node linked to the current character, or create a new node"""
        ...
    def GetEffectorModel(self,EffectorId:FBEffectorId,EffectorSetID:FBEffectorSetID=None)->FBModel:
        """Get the model associated with each effector in the Control Rig of the character.
        
        EffectorId : The effector ID.
        EffectorSetID : Id of the ControlSet to obtain, if not specified the current one is taken.
        return : The model in the Control Rig corresponding to the specified Effector."""
        ...
    def GetExternalSolver(self)->FBCharacterSolver:
        """Get a pointer to the external solver of a character, or NULL is no external solver is used on the character.
        
        return : The pointer of the current External Solver, NULL if it's the internal solver."""
        ...
    def GetFKVisibility(self)->FBVisibilityState:
        """Get the FK visibility state.
        
        return : The FK visibility state."""
        ...
    def GetFloorContactModel(self,MemberIndex:FBFloorContactID)->FBModel:
        """Get the model associated with the floor contact ID.
        
        MemberIndex : Id of the floor contact
        return : The model associated with the floor contact ID"""
        ...
    def GetGoalModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the goal model associated with each body part in the Character Marker Set of the character.
        
        BodyNodeId : FBBodyNodeId
        return : The model in the Character Marker Set corresponding to the specified body part."""
        ...
    def GetIKVisibility(self)->FBVisibilityState:
        """Get the IK visibility state.
        
        return : The IK visibility state."""
        ...
    def GetIndexByModel(self,Model:FBModel)->FBBodyNodeId:
        """Get the index associated with Given Model.
        
        Model : FBModel
        return : The model linked to the specified body part."""
        ...
    def GetModel(self,BodyNodeId:FBBodyNodeId)->FBModel:
        """Get the model associated with each body part of the character.
        
        BodyNodeId : FBBodyNodeId
        return : The model linked to the specified body part."""
        ...
    def GetParentROffset(self,BodyNodeId:FBBodyNodeId,RVector:FBVector3d):
        """BodyNodeId : FBBodyNodeId
        RVector : FBRVector"""
        ...
    def GetROffset(self,BodyNodeId:FBBodyNodeId,RVector:FBVector3d):
        """BodyNodeId : FBBodyNodeId
        RVector : FBRVector"""
        ...
    def GetSOffset(self,BodyNodeId:FBBodyNodeId,SVector:FBVector3d):
        """BodyNodeId : FBBodyNodeId
        SVector : FBSVector"""
        ...
    def GetSkeletonVisibility(self)->FBVisibilityState:
        """Get the skeleton visibility state.
        
        return : The skeleton visibility state."""
        ...
    def GetSkinModelList(self,SkinModelList:FBModelList):
        """Get the skin model associated with character bones.
        Could be deformable model connected to bone via cluster, or non deformable model parented directly under the bones.
        
        SkinModelList : List to be filled up. (will not be cleared)"""
        ...
    def GetTOffset(self,BodyNodeId:FBBodyNodeId,TVector:FBVector4d):
        """BodyNodeId : FBBodyNodeId
        TVector : FBTVector"""
        ...
    def GetTransformOffset(self,BodyNodeId:FBBodyNodeId,OffsetMatrix:FBMatrix):
        """BodyNodeId : FBBodyNodeId
        OffsetMatrix : FBMatrix"""
        ...
    def GoToStancePose(self,PushUndo:bool=False,IncludeCharacterExtensions:bool=True):
        """Set the character in stance pose.
        
        PushUndo : Should we push an undo transaction on the undo stack? Don't push undo in non UI thread.
        IncludeCharacterExtensions : Should the character extensions go to stance pose too?"""
        ...
    def IsParentNodeOffset(self,NodeId:FBBodyNodeId)->bool:
        """Check if there is an offset on Parent.
        
        NodeId : Node Id to Check.
        return : True if there is an offset on Parent."""
        ...
    def IsRotationPin(self,EffectorIndex:FBEffectorId)->bool:
        """Return true if the object is Pinned in Rotation (Manipulation).
        
        EffectorIndex : Given Index to obtain Model
        return : True if the effector is pinned in Rotation"""
        ...
    def IsTranslationPin(self,EffectorIndex:FBEffectorId)->bool:
        """Return true if the object is Pinned in Translation (Manipulation).
        
        EffectorIndex : Given Index to obtain Model
        return : True if the effector is pinned in Translation"""
        ...
    def PlotAnimation(self,PlotWhere:FBCharacterPlotWhere,PlotOptions:FBPlotOptions)->bool:
        """Plot the animation of the character.
        When plotting onto Control Rig while the Control Rig being the source of the Character, only the selected properties, based on the active keying group, will be plotted.
        
        PlotWhere : Where to plot a character, control rig or Skeleton
        PlotOptions : Option parameters for plotting
        return : True if the operation completed successfully."""
        ...
    def ReadyForRetarget(self)->bool:
        """Test if character is ready for the Retarget operation (basically, is it in character input ?).
        
        return : True if the character is ready."""
        ...
    def RemoveCharacterExtension(self,Ext:FBCharacterExtension):
        """Get the model associated with each body part of the character.
        
        Ext : extension to be removed to the character."""
        ...
    def ResetProperties(self,Type:FBCharacterResetProperties):
        """Reset the properties of the character.
        
        Type : Speficy which properties will be reset."""
        ...
    def Retarget(self,OnBaseLayer:bool):
        """Retarget the animation from the input character to us.
        
        OnBaseLayer : if true, keys corrections will be made on base layer; else they will be made on another layer."""
        ...
    def SelectModels(self,Select:bool,ApplyToCharacter:bool,ApplyToRig:bool,ApplyToExtensions:bool):
        """Select the objects that make a character.
        
        Select : True to select, false to deselect.
        ApplyToCharacter : TSould the character contraint be selected ?
        ApplyToRig : should The rig (and its children) be selected ?
        ApplyToExtensions : Should the character extensions (and their children) be selected ?"""
        ...
    def SetCharacterizeOff(self):
        """Set Characterize flag off."""
        ...
    def SetCharacterizeOn(self,SetAsBiped:bool)->bool:
        """Set the Characterize flag on.
        
        SetAsBiped : true to use biped characterization or false to use quadruped.
        return : current state of the flag after the operation (true if it did succeed)."""
        ...
    def SetExternalSolver(self,Index:int):
        """Set character solver.
        
        Solver : Character solver that will be used by the character."""
        ...
    def SetExternalSolverWithIndex(self,arg2:object):...
    def SetFKVisibility(self,State:bool)->bool:
        """Set the FK visibility state.
        
        State : The FK visibility state.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetIKVisibility(self,State:bool)->bool:
        """Set the IK visibility state.
        
        State : The IK visibility state.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetRotationPin(self,EffectorIndex:FBEffectorId,Value:bool)->bool:
        """Set the object Pinned in Rotation (Manipulation) status.
        
        EffectorIndex : Given Index to obtain Model.
        Value : The object Pinned in Rotation status.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetSkeletonVisibility(self,State:bool)->bool:
        """Set the skeleton visibility state.
        
        State : The skeleton visibility state.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetTranslationPin(self,EffectorIndex:FBEffectorId,Value:bool)->bool:
        """Set the object Pinned in Translation (Manipulation) status.
        
        EffectorIndex : Given Index to obtain Model
        Value : The object Pinned in Translation status.
        return : True if the operation is successful, false otherwise."""
        ...
class FBActor(FBConstraint):
    """FBActor is used to link motion data to a character.
    In MotionBuilder, an actor is a model used to link captured motion data to a character. Use functions in FBActor to set the body color, skeleton color, pivot color, marker size, pivot size, pivot information, etc. on an actor.These classes are under development and may change dramatically between versions.To obtain the list of actors present in a scene, you need to create an instance of class FBSystem, to obtain the current scene. The FBScene object holds the list of actors in the property Actors.
    
    >>> FBSystem lSystem;
    FBScene* lScene = lSystem.Scene;
    for( int lIdx = 0; lIdx < lScene->Actors.GetCount(); ++lIdx )
    {
    FBTrace( 'Actor[%d]: '%s'
    ', lIdx, (char*)lScene->Actors[lIdx] );
    }
    
    
    The current actor selected in the Character tool can be obtained via the FBApplication object.
    
    >>> FBApplication lApplication;
    FBActor* lActor = lApplication.CurrentActor;
    if( lActor )
    {
    FBTrace( 'Current actor is: '%s'
    ', (char*)lActor->Name );
    }
    else
    {
    FBTrace( 'No actor currently selected
    ' );
    }"""
    BodyColor:FBColor
    """Read Write Property: The color of the body of the actor."""
    ChestOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    ChestOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    ChestPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    FKFingerMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered intermediate finger phalanges."""
    FKFingerTipMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered finger tip phalanges."""
    FKThumbTipMultiplier:float
    """Read Write Property: Used to augment the amount of FK propagation for unmarkered thumb tip phalanges."""
    HeadOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    HeadOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    HeadPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    HipsOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    HipsOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    HipsPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    HumanFingerLimits:bool
    """Read Write Property: Enables/Disables human finger limits during actor solve."""
    IKManip:bool
    """Read Write Property: Access to the IK Manip mode. This property is shared for all actors."""
    LeftAnkleOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftAnkleOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftAnklePosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftCollarOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftCollarOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftCollarPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftElbowOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftElbowOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftElbowPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftFootOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftFootOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftFootPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftHandIndexIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandIndexRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddlePinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandMiddleRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandPinkyRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHandRingRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    LeftHipOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftHipOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftHipPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftIndexAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftIndexAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftIndexBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftIndexBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftIndexCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftIndexCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftKneeOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftKneeOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftKneePosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftMiddleAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftMiddleAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftMiddleBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftMiddleBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftMiddleCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftMiddleCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftPinkyAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftPinkyAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftPinkyBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftPinkyBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftPinkyCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftPinkyCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftRingAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftRingAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftRingBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftRingBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftRingCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftRingCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftShoulderOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftShoulderOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftShoulderPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    LeftThumbAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftThumbAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftThumbBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftThumbBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftThumbCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftThumbCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftWristOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    LeftWristOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    LeftWristPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    ManipulateOffsets:bool
    """Read Write Property: Flag to compute offsets while manipulating. If it is set to false, the manipulator is re-snapping as before. If it is set to true, offsets properties (T and R) are computed and candidated instead."""
    MarkerSet:FBMarkerSet
    """Read Write Property: Associated marker set."""
    MarkerSetSize:float
    """Read Write Property: The size of the markers of the actor."""
    NeckOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    NeckOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    NeckPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    OutputMarkerSet:FBMarkerSet
    """Read Write Property: Associated output marker set."""
    PivotColor:FBColor
    """Read Write Property: The color of the pivot points of the actor."""
    PivotPointsVisibility:bool
    """Read Write Property: Show or Hide the Pivot Points."""
    PivotSize:float
    """Read Write Property: The size of the pivot points of the actor."""
    RightAnkleOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightAnkleOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightAnklePosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightCollarOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightCollarOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightCollarPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightElbowOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightElbowOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightElbowPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightFootOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightFootOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightFootPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightHandIndexIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandIndexRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddlePinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandMiddleRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandPinkyRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingIndex:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingMiddle:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingPinky:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHandRingRing:float
    """Read Write Property: Used to set blending coefficients. Each of the 4 fingers can be a blend of the 4 finger. This is not available for thumbs."""
    RightHipOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightHipOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightHipPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightIndexAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightIndexAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightIndexBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightIndexBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightIndexCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightIndexCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightKneeOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightKneeOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightKneePosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightMiddleAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightMiddleAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightMiddleBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightMiddleBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightMiddleCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightMiddleCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightPinkyAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightPinkyAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightPinkyBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightPinkyBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightPinkyCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightPinkyCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightRingAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightRingAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightRingBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightRingBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightRingCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightRingCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightShoulderOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightShoulderOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightShoulderPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    RightThumbAOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightThumbAOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightThumbBOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightThumbBOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightThumbCOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightThumbCOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightWristOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    RightWristOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    RightWristPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    SkeletonColor:FBColor
    """Read Write Property: The color of the skeleton of the actor."""
    SkeletonVisibility:bool
    """Read Write Property: Show or Hide the Skeleton."""
    SymmetryEditRotation:bool
    """Read Write Property: Symmetry Edit (Rotation) mode state. Only effective when IKManip property is set to false. This property is shared for all actors."""
    SymmetryEditScaling:bool
    """Read Write Property: Symmetry Edit (Scaling) mode state. Only effective when IKManip property is set to false. This property is shared for all actors."""
    SymmetryEditTranslation:bool
    """Read Write Property: Symmetry Edit (Translation) mode state. Only effective when IKManip property is set to false. This property is shared for all actors."""
    Visibility:bool
    """Read Write Property: Show or Hide the Actor Body."""
    WaistOffsetR:FBVector3d
    """Read Write Property: Local rotation offset that is applied after the actor solve"""
    WaistOffsetT:FBVector3d
    """Read Write Property: Local translation offset that is applied after the actor solve"""
    WaistPosition:FBVector3d
    """Read Write Property: Body part pivot of the actor."""
    def GetCurrentSkeletonState(self)->FBSkeletonState:
        """Return the Current Skeleton State.
        
        ResetOrientation : When set to true, all rotations in the state will be reset to characterization values.
        return : Current Skeleton State"""
        ...
    def GetDefaultSkeletonState(self)->FBSkeletonState:
        """Return the Default Skeleton State.
        
        return : Default Skeleton State"""
        ...
    def GetDefinitionRotationVector(self,SkeletonId:FBSkeletonNodeId,RotationVector:FBVector3d):
        """Get Actor Rotation Definition.
        Only effective when IKManip property is set to false.
        
        SkeletonId : Skeleton Node Id
        RotationVector : Actor Rotation Definition for the given ID"""
        ...
    def GetDefinitionScaleVector(self,SkeletonId:FBSkeletonNodeId,ScaleVector:FBVector3d):
        """Get Actor Scaling Definition.
        
        SkeletonId : Skeleton Node Id
        ScaleVector : Actor Scaling Definition for the given ID"""
        ...
    def GetDefinitionTranslationVector(self,SkeletonId:FBSkeletonNodeId,TranslationVector:FBVector3d):
        """Get Actor Translation Definition.
        Only effective when IKManip property is set to false.
        
        SkeletonId : Skeleton Node Id
        TranslationVector : Actor Translation Definition for the given ID"""
        ...
    def SetActorTranslation(self,TranslationVector:FBVector3d):
        """Translate Actor, similar to moving the hips of the Actor in the UI.
        Only effective when IKManip property is set to false.
        
        TranslationVector : Will move the entire Actor toTranslationVector coordinate"""
        ...
    def SetDefinitionRotationVector(self,SkeletonId:FBSkeletonNodeId,RotationVector:FBVector3d,SymmetricUpdate:bool=True):
        """Set Actor Rotation Definition.
        Only effective when IKManip property is set to false.
        
        SkeletonId : Skeleton Node Id
        RotationVector : Actor Rotation value for the given ID
        SymmetricUpdate : Update right and left part at the same time"""
        ...
    def SetDefinitionScaleVector(self,SkeletonId:FBSkeletonNodeId,ScaleVector:FBVector3d,SymmetricUpdate:bool=True):
        """Set Actor Scaling Definition.
        
        SkeletonId : Skeleton Node Id
        ScaleVector : Actor Scaling value for the given ID
        SymmetricUpdate : Update right and left part at the same time"""
        ...
    def SetDefinitionTranslationVector(self,SkeletonId:FBSkeletonNodeId,TranslationVector:FBVector3d,SymmetricUpdate:bool=True):
        """Set Actor Translation Definition.
        Only effective when IKManip property is set to false.
        
        SkeletonId : Skeleton Node Id
        TranslationVector : Actor Translation value for the given ID
        SymmetricUpdate : Update right and left part at the same time"""
        ...
    def UpdateValues(self,EvalInfo:FBEvaluateInfo):
        """Update Internal Values to be corresponding to the Given Evaluate Information.
        
        EvalInfo : Evaluate Info of the Values"""
        ...
class FBConstraintRelation(FBConstraint):
    """ConstraintRelation class.
    This class exposes the relation constraint and allows addition of new boxes and removal of existing ones. See sample: TraversingRelationConstraint.py."""
    Boxes:FBPropertyListBox
    """List: Boxes used in this constraint."""
    def ConstrainObject(self,ConstrainedObject:FBBox)->FBBox:
        """Create a receiver box.
        Use an existing FBBox object to create a receiver in the relation.
        
        ConstrainedObject : Destination box to insert in the constraint.
        return : A place holder box for the object."""
        ...
    def CreateFunctionBox(self,Group:str,Name:str)->FBBox:
        """Create a function box.
        Ask the constraint to create new function box.
        
        Group : Name of the group under which the function is located in the Constraint Relation GUI (case-sensitive!).
        Name : Name of the function, as seen in the GUI (case-sensitive!).
        return : The newly created function box, or NULL if the name/group combination was invalid."""
        ...
    def GetBoxPosition(self,Box:FBBox)->bool:
        """Get a box position in the GUI.
        Get the position of a box within the constraint layout view.
        
        return : A tuple containing: the result of operation (bool), X value (int), and Y value(int)"""
        ...
    def SetAsSource(self,Source:FBBox)->FBBox:
        """Create a sender box.
        Use an existing FBBox object to create a sender in the relation.
        
        Source : Source box to insert in the constraint.
        return : A place holder box for the object."""
        ...
    def SetBoxPosition(self,Box:FBBox,X:int,Y:int)->bool:
        """Set a box position in the GUI.
        Set the position of a box within the constraint layout view.
        
        Box : Box which needs to be moved.
        X : New X position.
        Y : New Y position.
        return : A boolean value indicating success (True) or failure (False)."""
        ...
class FBCycleAnalysisNode(FBBox):
    """Cycle Analysis class."""
    RealTime:bool
    """Read Only Property: Real time."""
    RootHMode:FBRootHMode
    """Read Only Property: RootH Mode."""
    RootRMode:FBRootRMode
    """Read Only Property: RootR Mode."""
    RootSpeedMode:FBRootSpeedMode
    """Read Only Property: Root Speed Mode."""
    RootXZMode:FBRootXZMode
    """Read Only Property: RootXZ Mode."""
    def GetPoseFCurve(self)->object:...
    def GetRootHFCurve(self)->object:...
    def GetRootRFCurve(self)->object:...
    def GetRootSpeedFCurve(self)->object:...
    def GetRootXZFCurve(self)->object:...
class FBConstraintSolver(FBConstraint):
    """Base class for constraint solver."""
    ...
class FBDevice(FBBox):
    """Base Device class.
    Cannot be instantiated from Python. See samples: StartDevice.py, StopDevice.py."""
    CommType:int
    """Read Write Property: Type of communications."""
    HardwareVersionInfo:str
    """Read Write Property: Device information: hardware version."""
    Information:str
    """Read Write Property: Device information: information."""
    ModelBindingRoot:FBModel
    """Component: Root of model currently binded model hierarchy."""
    ModelTemplate:FBModelTemplate
    """Component: Root of model template structure."""
    Online:bool
    """Read Write Property: Is online?"""
    RecordingStartTime:FBTime
    """Read Only Property: The time at which the recording started."""
    RecordingStopTime:FBTime
    """Read Only Property: The time at which the recording stopped."""
    SamplingMode:FBDeviceSamplingMode
    """Read Write Property: Mode to use to record device."""
    SamplingPeriod:FBTime
    """Read Write Property: Set this to how many times a device is to be evaluated in one second. There is no theoretical maximum value but practically you should consider scene complexity, system resources, network speed, etc. If set to 0: the device is evaluated on the sync signal. When the sync occurs; the device is scheduled to be evaluated. If you do not set, the sampling period is based on the internal variable from the [Sync] section of the .Application.txt file (NTSC, PAL, CINEMA)."""
    Status:str
    """Read Write Property: Device information: status."""
    def AckOneBadSampleReceived(self):
        """Acknowlege that one bad sample was received (for statistical purposes)."""
        ...
    def AckOneSampleReceived(self):
        """Acknowlege that one sample was received (for statistical purposes)."""
        ...
    def AckOneSampleSent(self):
        """Acknowlege that one sample was sent (for statistical purposes)."""
        ...
    def ModelBindingCreate(self)->FBModel:
        """Create a new model binding.
        
        return : The model root that has been created or NULL is an error occured."""
        ...
    def ModelBindingRootsList(self,List:FBModelList):
        """Get the list of all the possible root models for binding.
        
        List : List to add found models to."""
        ...
    def RecordingDoneAnimation(self,AnimationNode:FBAnimationNode):
        """When recording, finish animation.
        
        AnimationNode : Animation node to write information to."""
        ...
    def RecordingInitAnimation(self,AnimationNode:FBAnimationNode):
        """When recording, initialize animation.
        
        AnimationNode : Animation node to read information from."""
        ...
class FBGlobalLight(FBBox):
    """Global light class."""
    AmbientColor:FBColor
    """Read Write Property: Ambient light color."""
    FogBegin:float
    """Read Write Property: Begin fog distance."""
    FogColor:FBColor
    """Read Write Property: Fog color."""
    FogDensity:float
    """Read Write Property: Fog density."""
    FogEnable:bool
    """Read Write Property: Enable fog?"""
    FogEnd:float
    """Read Write Property: End fog distance."""
    FogMode:FBFogMode
    """Read Write Property: Fog falloff mode."""
class FBDeviceOptical(FBDevice):
    """Optical device class."""
    AutoAntialiasing:bool
    """Property: Is it auto-antialiasing?"""
    DampingTime:float
    """Property: Damping time for device."""
    ForceOpticalSamplingRate:bool
    """Property: Force the use of the optical sampling rate?"""
    MarkerTimeStamp:FBTime
    """Property: TimeStamp for marker."""
    Markers:FBPropertyListDeviceOpticalMarker
    """List: Markers."""
    ModelOptical:FBModel
    """Property: Optical model for manipulation."""
    OpticalSamplingRate:float
    """Property: Resampling rate for optical device."""
    SkipFrame:bool
    """Property: Skip Record Frame"""
    SupportOcclusion:bool
    """Property: Does the device support occulsion?"""
    UseMarkerTimeStamp:bool
    """Property: Use the individual marker timestamps?"""
    def DeviceOperation(self,Operation:kDeviceOperations)->bool:
        """Operate device.
        This is an operation such as Init, Start, Done, Reset, etc.
        
        Operation : Operation to have device perform.
        return : Current state : <b true if online."""
        ...
    def DeviceOpticalBeginSetup(self):
        """Begin device setup."""
        ...
    def DeviceOpticalEndSetup(self):
        """End device setup."""
        ...
    def DeviceOpticalRecordFrame(self,Time:FBTime,DeviceNotifyInfo:FBDeviceNotifyInfo):
        """Record a frame of information from device.
        Virtual function that derived class may overide
        
        Time : Time of evaluation.
        DeviceNotifyInfo : Notification information when thread was called."""
        ...
class FBGroup(FBBox):
    """Objects Grouping class.
    This class is an interface to manipulate object's grouping in the scene. See samples: FBGetSelectedModels.py, FBGroup.py."""
    Items:FBPropertyListComponent
    """List: Items in the group."""
    Pickable:bool
    """Read Write Property: Controls if objects in the group are pickable."""
    Show:bool
    """Read Write Property: Controls if objects in the group are displayed."""
    Transformable:bool
    """Read Write Property: Controls if objects in the group are transformable."""
    def Clone(self)->FBGroup:
        """Clone the group.
        This will duplicated the current group.
        
        return : Newly created group."""
        ...
    def Contains(self,Component:FBComponent)->bool:
        """Contains.
        
        Component : Component to verify if it is in the Group
        return : True if the object is in the Group"""
        ...
    def Select(self,Select:bool):
        """Select.
        
        Select : If true, group contents will be selected."""
        ...
class FBHUD(FBBox):
    """Heads Up display.
    Display scene related information to the screen. This information will also be present in the rendered frames when creating AVIs or QuickTime files. See samples: BloopSlate.py, HUDElements.py, HUDTextElement.py, RecordLight.py, Timeline.py, HUD.py."""
    EStockElement:property
    Elements:FBPropertyListHUDElement
    """List: Elements present in the HUD."""
    HUDs:FBPropertyListHUD
    """List: HUDS attached to this HUD."""
    OnDisplay:FBEvent
    """Event: Callback just before HUD is displayed to update custom values"""
    Visibility:bool
    """Read Write Property: Indicate if the information will be displayed or not."""
    eBloopSlate:property
    eFlashElement:property
    eRecordLight:property
    eRectElement:property
    eTextElement:property
    eTextureElement:property
    eTimeline:property
    def CreateCustomElement(self,HUDElementClassName:str,Name:str)->FBHUDElement:
        """Creates a custom HUD Element.
        
        HUDElementClassName : The HUD Element class name (mainly, the ClassName parameter of the FBStorableCustomHUDElementImplementation macro).
        Name : Name for the custom HUD Element to create.
        return : The created custom HUD Element."""
        ...
    def CreateElement(self,Type:EStockElement,Name:str)->FBHUDElement:
        """Creates a stock HUD Element.
        
        Type : View to be called for expose.
        Name : Name for the HUD Element to create.
        return : The created HUD Element."""
        ...
class FBHUDElement(FBBox):
    """Heads Up display.
    Display scene related information on a camera output. Rendered on video out, output renderings."""
    Height:float
    """Read Write Property: Specifies the height of HUD element on the screen. It's in pixel when ScaleByPercent is false and percentage when ScaleByPercent is true."""
    HorizontalDock:FBHUDElementHAlignment
    """Read Write Property: Specifies if the HUD element will be horizontally docked to the Left, Right, or Center."""
    Justification:FBHUDElementHAlignment
    """Read Write Property: Specifies if the justification of the HUD element is Left, Right, or Center."""
    PositionByPercent:bool
    """Read Write Property: When set to true, X and Y position values are in percentage, relative to the corresponding camera view dimension. Otherwise, they are absolute pixel values."""
    ScaleByPercent:bool
    """Read Write Property: When set to true, Scale is in percentage, relative to the corresponding camera view dimension. Otherwise, it is an absolute value."""
    ScaleUniformly:bool
    """Read Write Property: Specifies whether the width and height of HUD element will be scaled uniformly according to the initial aspect ratio."""
    Show:bool
    """Read Write Property: Specifies if the HUD element will be displayed or not."""
    VerticalDock:FBHUDElementVAlignment
    """Read Write Property: Specifies if the HUD element will be vertically docked to the Bottom, Top, or Center."""
    Visibility:bool
    Width:float
    """Read Write Property: Specifies the width of HUD element on the screen. It's in pixel when ScaleByPercent is false and percentage when ScaleByPercent is true."""
    X:float
    """Read Write Property: Specifies the horizontal position of the HUD element, relative to dock position and justification."""
    Y:float
    """Read Write Property: Specifies the vertical position of the HUD element, relative to dock position and justification."""
class FBHandle(FBBox):
    """FBHandle class exposes the Handle object of the application.
    This is a terminal class and should not be used as a base for a new class."""
    Follow:FBPropertyListObject
    """List: Object to be followed by the handle. Should have a cardinality of 1."""
    Image:FBPropertyListObject
    """List: Image to be used in the handle display. Only the image at position 0 is used."""
    Manipulate:FBPropertyListObject
    """List: Objects manipulated by the handle."""
    ManipulateRotation:FBPropertyListObject
    """List: Objects manipulated by the handle. Only their rotation is affected."""
    ManipulateScaling:FBPropertyListObject
    """List: Objects manipulated by the handle. Only their scaling is affected."""
    ManipulateTranslation:FBPropertyListObject
    """List: Objects manipulated by the handle. Only their translation is affected."""
    def Select(self):
        """Meta selection.
        With this method, the handle itself is selected as well as all the models that are manipulated by the handle."""
        ...
class FBHUDFlashElement(FBHUDElement):
    """Heads Up display.
    Flash HUD element. Display a flash (swf) file rendered on the HUD. See sample: HUDElements.py."""
    FilePath:str
    """Read Write Property: Path to load the swf file from"""
class FBHUDRectElement(FBHUDElement):
    """Heads Up display.
    Rectangle HUD element. See sample: HUDElements.py."""
    Color:FBColorAndAlpha
    """Read Write Property: Color of the rectangluar region."""
class FBHUDBloopSlateElement(FBHUDFlashElement):
    """Heads Up display.
    Bloop Slate HUD element. Display a bloop slate (swf) file rendered on the HUD."""
    BackgroundColor:FBColorAndAlpha
    """Read Write Property: Bloop slate background color, by default it is 100% transparent."""
    Enable:bool
    """Read Write Property: Bloop slate will appear if set to true."""
    ForegroundColor:FBColorAndAlpha
    """Read Write Property: Bloop slate foreground color."""
    ShowAfterDelayOnRecordPlay:FBTime
    """Read Write Property: Delay before the bloop slate is displayed after recording has started."""
    ShowDuration:FBTime
    """Read Write Property: Time that the bloop slate will be displayed."""
class FBHUDTimelineElement(FBHUDFlashElement):
    """Heads Up display.
    HUD Timeline element. Displays a timeline that shows Head, Cut, Tail regions, and current time cursor. The drawing is defined in the flash file(timeline.swf). See sample: Timeline.py."""
    CutActiveColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Cut region when it is active."""
    CutIdleColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Cut region when it is idle."""
    HeadActiveColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Head region when it is active."""
    HeadDuration:FBTime
    """Read Write Property: Specifies duration of the Head region."""
    HeadIdleColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Head region when it is idle."""
    TailActiveColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Tail region when it is active."""
    TailDuration:FBTime
    """Read Write Property: Specifies duration of the Tail region."""
    TailIdleColor:FBColorAndAlpha
    """Read Write Property: Specifies color of the Tail region when it is idle."""
class FBHUDTextElement(FBHUDElement):
    """Heads Up display.
    Text element. Render text with a background rectangle to the HUD. See samples: HUDElements.py, HUDTextElement.py, HUD.py."""
    AdjustWidthToFitText:bool
    """Read Write Property: If On it it will adjust the width of a text element so that a text character's aspect ratio does not change as the content grows or shrinks."""
    BackgroundColor:FBColorAndAlpha
    """Read Write Property: Background text color."""
    Color:FBColorAndAlpha
    """Read Write Property: Text color."""
    Content:str
    """Read Write Property: C like format to display like in printf."""
    Font:str
    """Read Write Property: Specifies the font."""
    ForceTimeCodeDisplay:bool
    """Read Write Property: Specifies if the display of time-related reference property will be in timecode format."""
    def GetFontList(self)->FBStringList:
        """Returns a list of supported fonts."""
        ...
class FBHUDTextureElement(FBHUDElement):
    """Heads Up display.
    Texture HUD element. Display a texture on a rectangle on the HUD. See sample: HUDElements.py."""
    Texture:FBPropertyListTexture
    """Read Write Property: Texture to display."""
class FBMaterial(FBBox):
    """Material class.
    See samples: MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py."""
    Ambient:FBColor
    """Read Write Property: Ambient color."""
    AmbientFactor:float
    """Read Write Property: Ambient Factor value."""
    Bump:FBColor
    """Read Write Property: Bump."""
    BumpFactor:float
    """Read Write Property: Bump Factor value."""
    Diffuse:FBColor
    """Read Write Property: Diffuse color."""
    DiffuseFactor:float
    """Read Write Property: Diffuse Factor value."""
    DisplacementColor:FBColor
    """Read Write Property: Displacement color."""
    DisplacementFactor:float
    """Read Write Property: Displacement Factor value."""
    Emissive:FBColor
    """Read Write Property: Emissive color."""
    EmissiveFactor:float
    """Read Write Property: Emissive Factor value."""
    NormalMap:FBColor
    """Read Write Property: Normal Map."""
    Reflection:FBColor
    """Read Write Property: Reflection color."""
    ReflectionFactor:float
    """Read Write Property: Reflection Factor value."""
    Shininess:float
    """Read Write Property: Shininess value."""
    Specular:FBColor
    """Read Write Property: Specular color."""
    SpecularFactor:float
    """Read Write Property: Specular Factor value."""
    TransparencyFactor:float
    """Read Write Property: Transparency Factor value."""
    TransparentColor:FBColor
    """Read Write Property: Transparent color."""
    def Clone(self)->FBMaterial:
        """Clone the material.
        This will duplicated the current material.
        
        return : Newly created material."""
        ...
    def GetTexture(self,Type:FBMaterialTextureType=FBMaterialTextureType.kFBMaterialTextureDiffuse)->FBTexture:
        """Retrieve associated texture.
        
        Type : MaterialTextureType to get connected texture from (default is Diffuse is not specified)."""
        ...
    def OGLInit(self):
        """Setup OpenGL fixed pipeline material settings."""
        ...
    def SetTexture(self,Texture:FBTexture,Type:FBMaterialTextureType=FBMaterialTextureType.kFBMaterialTextureDiffuse):
        """Set associated texture.
        
        Texture : texture to be connected.
        Type : MaterialTextureType to set connected texture to."""
        ...
class FBModel(FBBox):
    """Model class.
    In the MotionBuilder UI, a model can be any object in a scene, created using geometry. Models can represent simple objects like cubes, or complex objects like characters.FBModel is a base class which is not used so much directly, but is the parent of well-used classes like FBCamera, FBLight, and FBModelMarker.It also implements a number of widely-implemented functions and attributes, such as: Clone(), FBDelete() UI attributes such as Show, Pickable, and Visibility Positional attributes such as Rotation, Scaling, and Translation The following Python snippet shows how to create, show, rotate, and delete a cube
    
    >>> from pyfbsdk import *
    myCube = FBModelCube('cube')
    myCube.Show = True
    myCube.Rotation = FBVector3d(45, 45, 45)
    myCube.FBDelete()
    
    
    There is a few ways to get a handle on existing models in a scene: FBFindObjectsByName return a list of objects matching a pattern (can contain *). For usage, see: FindObjectsWithWildcard.py If you know the name of the model, use FBFindModelByLabelName, as demonstrated in FBComponent.py. FBGetSelectedModels can get a handle to an object which is derived from FBModel. It searches the scene for a model, based on the model's unique name and returns a list of all the selected things in the scene. See sample: ResetLocalTranslationRotation.py."""
    AnimationNode:FBAnimationNode
    """Read Only Property: Animation node of the model."""
    BlendShapeDeformable:bool
    """Read Write Property: Model blend-shape deformable. Not Savable"""
    CastsShadows:bool
    """Read Write Property: If true, the geometry will produce shadows."""
    Children:FBPropertyListModel
    """List: Children for model."""
    ConstrainDeformable:bool
    """Read Write Property: Model constraint deformable. Not Savable"""
    CullingMode:property
    Deformers:FBPropertyListDeformer
    """List: Deformers (Skeleton Deformer or Point Cache Deformer)."""
    GeometricRotation:FBVector3d
    """Read Write Property: Geometric rotation."""
    GeometricScaling:FBVector3d
    """Read Write Property: Geometric scaling."""
    GeometricTranslation:FBVector3d
    """Read Write Property: Geometric translation."""
    Geometry:FBGeometry
    """Read Write Property: Geometry for the model."""
    GeometryUpdateId:int
    """Read Only Property: model geometry (vertex data) related update id."""
    Icon3D:bool
    """Read Write Property: Is model a 3D icon?"""
    IsConstrained:bool
    """Read Only Property: Is model constrained?"""
    IsDeformable:bool
    """Read Only Property: Is model deformable?"""
    IsVisible:bool
    """If the model is visible.
    Note. this query will consider self Visibility property, plus parent node/set Visibility. The visibility of a model is affected by 4 parameters:
    
    EvaluateInfo : evaluate info,
    return : true if visible for the given evaluate info."""
    LookAt:FBModel
    """Read Write Property: Look at model (interest point)."""
    Materials:FBPropertyListMaterial
    """List: Materials for model."""
    ModelVertexData:FBModelVertexData
    """Read Only Property: ModelVertexData for the model."""
    Parent:FBModel
    """Read Write Property: Parent model."""
    Pickable:bool
    """Read Write Property: Indicate if a model can be picked in the viewer. This has a default value of 'true'."""
    PointCacheDeformable:bool
    """Read Write Property: Model point cache deformable. Not Savable"""
    PointCacheRecord:bool
    """Read Write Property: Record Point Cache for model? Not Savable"""
    PostRotation:FBVector3d
    """Read Write Property: Post Rotation (considered if RotationActive is true)"""
    PreRotation:FBVector3d
    """Read Write Property: Pre Rotation (considered if RotationActive is true)"""
    PrimaryVisibility:bool
    """Read Write Property: Control the geometry render state. Geometry can still cast shadows even if this is turned off."""
    QuaternionInterpolate:bool
    """Read Write Property: Use quaternion interpolation."""
    ReceiveShadows:bool
    """Read Write Property: If true, the geometry will receive shadows."""
    Rotation:FBVector3d
    """Read Write Property: Lcl rotation."""
    RotationActive:bool
    """Read Write Property: Is model using Rotation Limits?"""
    RotationMax:FBVector3d
    """Read Write Property: Max Rotation Limit (considered if RotationActive is true)"""
    RotationMaxX:bool
    """Read Write Property: Is model using Maximum Rotation Limits On X?"""
    RotationMaxY:bool
    """Read Write Property: Is model using Maximum Rotation Limits On Y?"""
    RotationMaxZ:bool
    """Read Write Property: Is model using Maximum Rotation Limits On Z?"""
    RotationMin:FBVector3d
    """Read Write Property: Min Rotation Limit (considered if RotationActive is true)"""
    RotationMinX:bool
    """Read Write Property: Is model using Minimum Rotation Limits On X?"""
    RotationMinY:bool
    """Read Write Property: Is model using Minimum Rotation Limits On Y?"""
    RotationMinZ:bool
    """Read Write Property: Is model using Minimum Rotation Limits On Z?"""
    RotationOrder:FBModelRotationOrder
    """Read Write Property: Rotation order."""
    RotationSpaceForLimitOnly:bool
    """Read Write Property: Apply Post Rotation Matrix only for Limits?"""
    Scaling:FBVector3d
    """Read Write Property: Lcl scaling."""
    Scene:FBScene
    """Read Only Property: Scene containing the model."""
    Shaders:FBPropertyListShader
    """List: Shaders for model."""
    ShadingMode:FBModelShadingMode
    """Read Write Property: Shading mode for the model."""
    Show:bool
    """Read Write Property: Indicate if the viewer should show the object, according to its visibility value. This has a default value of 'false'."""
    SkeletonDeformable:bool
    """Read Write Property: Model skeleton deformable. Not Savable"""
    SoftSelected:bool
    """Read Write Property: Is model Soft selected?"""
    Textures:FBPropertyListTexture
    """List: Textures with Special UseType (Other than 'Color' which should connect to materials)."""
    Transformable:bool
    """Read Write Property: Indicate if a model can be transformable in the viewer. This has a default value of 'true'."""
    Translation:FBVector3d
    """Read Write Property: Lcl translation."""
    UniqueColorId:FBColor
    """Read Only Property: Unique Color Id for color based viewer picking. Color channel values are in the range [0, 1] with 1.0/255 precision."""
    UpVector:FBModel
    """Read Write Property: UpVector model."""
    Visibility:bool
    """Read Write Property: Visibility of model. This can be overridden by the 'Show' property."""
    VisibilityInheritance:bool
    """Read Write Property: //!< When this value is set to True the Visibility of this model is also applied to all its descendants"""
    def Clone(self)->FBModel:
        """Clone the model.
        This will duplicate the current model.
        
        return : Newly created model."""
        ...
    def CollapseInSchematic(self):
        """Collapse the model in the schematic view."""
        ...
    def DofToLRM(self,LM:FBMatrix,Dof):
        """Convert object space vector to local matrix.
        
        LM : Resulting local rotation matrix.
        Dof : Vector to convert"""
        ...
    def ExpandInSchematic(self):
        """Expand the model in the schematic view."""
        ...
    def FbxGetObjectSubType(self)->str:
        """Returns the class sub type inherited by the class of an object, for example: 'Default', 'Mesh'."""
        ...
    def FbxGetObjectType(self)->str:
        """Returns the class type inherited by the class of an object, for example: 'Model'."""
        ...
    def ForceAlwaysEvaluate(self):
        """Force Always Evaluate.
        In some case, MoBu kernel perform optimization by skipping certain evaluation tasks. This function stop skipping for this model."""
        ...
    def GetAdditionalUniqueColorID(self,Index:int)->FBColor:
        """Get Additional Unique Color Id.
        
        Index : the requested unique color id index, can't be larger than GetAdditionalColorIDCount()
        return : Additional Unique ColorId."""
        ...
    def GetAdditionalUniqueColorIDCount(self)->int:
        """Get additional unique color count.
        
        return : Additional Unique Color Count."""
        ...
    def GetBoundingBox(self,Min:FBVector3d,Max:FBVector3d):
        """Get the bounding box of the model.
        Note. for deformable model, this function will provide the approximated (larger than the smallest) bounding box for performance consideration.
        
        Min : Output parameter. Minimum value of the bounding box.
        Max : Output parameter. Maximum value of the bounding box."""
        ...
    def GetHierarchyWorldMatrices(self,MatricesArray:FBMatrix,MatricesArrayCount:int,HiercharyTraverserType:FBModelHiercharyTraverserType)->int:
        """Computes the global transform matrices between this model and all its children (all levels).
        The hierarchy world matrix for a model is represented as a global transform matrix applied on an arbitrary root hierarchy node (this model for instance), considered as the world reference.
        
        MatricesArray : The matrix array (memory already allocated) to fill in with the hierarchy world matrix of all the model's children models
        MatricesArrayCount : The size of the matrix array
        HiercharyTraverserType : The hierarchy traverser type
        EvaluateInfo : EvaluateInfo, Take Display if none specified."""
        ...
    def GetLocalTransformationMatrixWithGlobalRotationDoF(self,Matrix:FBMatrix,Inverse:bool=False,EvaluateInfo:FBEvaluateInfo=None):
        """Get the local transformation (or local inverse transformation) matrix with the global Rotation DoF values from the model.
        The GetMatrix method was previously wrongly returning the local transformation (and local inverse transformation) matrices with global Rotation DoF values. The GetMatrix method implementation has been updated to not include the global Rotation DoF values. This method returns the same matrix values returned by the legacy GetMatrix implementation when retrieving the local transformation (and local inverse transformation) matrices.
        
        Matrix : Matrix to fill with requested information.
        Inverse : False for the transformation matrix, true for the inverse transformation matrix.
        EvaluateInfo : EvaluateInfo, Take Display if none specified."""
        ...
    def GetMatrix(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,GlobalInfo:bool=True,EvaluateInfo:FBEvaluateInfo=None):
        """Get a matrix from the model.
        
        Matrix : Matrix to fill with requested information.
        What : Type of information requested (default=transformation).
        GlobalInfo : true if it is GlobalInfo, false if Local (default=true).
        EvaluateInfo : EvaluateInfo, Take Display if none specified."""
        ...
    def GetSchematicPosition(self)->FBVector2d:
        """Get the position in the schematic view for the model.
        
        return : Current position for the model."""
        ...
    def GetSelectedPointsCount(self)->int:
        """Get the number of selected points in the model.
        
        return : Number of selected points."""
        ...
    def GetVector(self,Vector:FBVector3d,What:FBModelTransformationType=FBModelTransformationType.kModelTranslation,GlobalInfo:bool=True,EvaluateInfo:FBEvaluateInfo=None):
        """Get a vector from the model.
        
        Vector : Vector to fill with requested values.
        What : Type of information requested (default=translation, inverses not supported).
        GlobalInfo : true if it is GlobalInfo, false if Local (default=true).
        EvaluateInfo : EvaluateInfo, Take Display if none specified"""
        ...
    def IsCollapsedInSchematic(self)->bool:
        """Returns if the model is collapsed or not (expanded) in the schematic view.
        
        return : true if the model is collapsed in the schematic view, false if it is expanded."""
        ...
    def IsEvaluationReady(self,What:FBModelEvaluationTaskType,EvaluateInfo:FBEvaluateInfo=None)->bool:
        """Is the model's evaluation task result ready.
        
        What : Type of evaluation task.
        EvaluateInfo : EvaluateInfo, Take Display if none specified"""
        ...
    def IsForceAlwaysEvaluate(self)->bool:
        """Return Force Always Evaluate status."""
        ...
    def LRMToDof(self,Dof,LM:FBMatrix):
        """Convert local matrix to object space vector.
        
        Dof : Resulting object space vector.
        LM : Local rotation matrix to convert"""
        ...
    def MatrixToRotation(self,Rotation,Matrix:FBMatrix):
        """Convert Rotation Matrix to Euler Vector based on model's rotation order.
        
        Rotation : Resulting euler vector, whose angles are stored in [X,Y,Z] order.
        Matrix : Matrix to convert."""
        ...
    def NoFrustumCullingRelease(self)->int:
        """Release no frustum culling request.
        
        return : Current no frustum culling request count after function call."""
        ...
    def NoFrustumCullingRequire(self)->int:
        """Acquire no frustum culling request.
        
        return : Current no frustum culling request count after function call."""
        ...
    def RayCast(self,Camera:FBCamera,MouseX:int,MouseY:int,HitPosition:FBVector3d,HitNormal:FBVector3d)->bool:
        """Ray cast test.
        
        Camera : Camera to use for casting.
        MouseX : Mouse X position.
        MouseY : Mouse Y position.
        HitPosition : Ray cast position on the object.
        HitNormal : Normal at the ray cast position on the object.
        return : true if it hit the meshes, hit would contains the precise position & normal."""
        ...
    def RotationToMatrix(self,Matrix:FBMatrix,Rotation):
        """Convert Euler Vector to Rotation Matrix based on model's rotation order.
        
        Matrix : Resulting rotation matrix.
        Rotation : Object space rotation vector to convert, whose angles are stored in [X,Y,Z] order."""
        ...
    def SetAdditionalUniqueColorIDCount(self,Count:int)->bool:
        """Request additional Unique color IDs.
        
        Count : User should note that Unique Color ID resource is limited (only 24 bits), hence should avoid to use unnecessary large number.
        return : True if Unique ColorId resource is available."""
        ...
    def SetMatrix(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,GlobalInfo:bool=True,PushUndo:bool=False):
        """Set a matrix for the model.
        
        Matrix : Information to use to set the model's matrix.
        What : Type of matrix to set (default=transformation).
        GlobalInfo : true if it is GlobalInfo, false if Local (default=true).
        PushUndo : true if this operation is undoable, don't push undo in non UI thread.
        EvaluateInfo : EvaluateInfo, Take Display if none specified"""
        ...
    def SetMatrixWithPrecision(self,Matrix:FBMatrix,What:FBModelTransformationType=FBModelTransformationType.kModelTransformation,GlobalInfo:bool=True,PushUndo:bool=False,EvaluateInfo:FBEvaluateInfo=None):
        """Set a matrix for the model.
        
        Matrix : Information to use to set the model's matrix.
        What : Type of matrix to set (default=transformation).
        GlobalInfo : true if it is GlobalInfo, false if Local (default=true).
        PushUndo : true if this operation is undoable, don't push undo in non UI thread.
        EvaluateInfo : EvaluateInfo, Take Display if none specified
        Precision : Indicate the precision level, used when calculating the threshold value for gimble lock. 16 * pow(10.0, -10)) is the new default value since Mobu 2016, 16 * pow(10.0, -6)) is old default value before then."""
        ...
    def SetSchematicPosition(self,X:int,Y:int):
        """Set the position in the schematic view for the model.
        
        Vector2d : Position to set."""
        ...
    def SetVector(self,Vector:FBVector3d,What:FBModelTransformationType=FBModelTransformationType.kModelTranslation,GlobalInfo:bool=True,PushUndo:bool=False):
        """Set a vector for the model.
        
        Vector : Vector to use to set values.
        What : Type of information to set (default=translation, inverses not supported).
        GlobalInfo : true if it is GlobalInfo, false if Local (default=true).
        PushUndo : true if this operation is undoable, don't push undo in non UI thread.
        EvaluateInfo : EvaluateInfo, Take Display if none specified"""
        ...
    def SetupPropertiesForShapes(self):
        """Setup Shape Properties.
        Normally this function is called automatically at the next global synchronization point after the geometry has been updated. However you must call it explicitly to access the shape properties immediately after shapes adding/removing before next global synchronization point."""
        ...
    def UseFrustumCulling(self)->bool:
        """Get the current Frustum Culling Status.
        
        return : True if model don't use frustum culling currently."""
        ...
class FBNote(FBBox):
    """Note class."""
    StaticComment:str
    """Read Write Property: Comment associated to this note."""
    def Attach(self,Comp:FBComponent=None)->bool:
        """Attach the note to a component.
        Will attach the note to the component. IfComp is NULL, the note will only be added to the scene.
        
        Comp : Component on which to attach note.
        return : A boolean indicating if the operation was successful or not."""
        ...
    def Detach(self,Comp:FBComponent=None)->bool:
        """Detach the note from a component.
        Will detach the note from the component. IfComp is NULL, the note will be removed from the scene and detached from all components.
        
        Comp : Component from which to detach note.
        return : A boolean indicating if the operation was successful or not."""
        ...
class FBModelCube(FBModel):
    """Cube model class.
    See samples: FBGroup.py, FBModelCube.py."""
    ...
class FBLight(FBModel):
    """Light class."""
    AreaLightShape:property
    """Read Write Property: Area light shape."""
    AttenuationType:FBAttenuationType
    """Read Write Property: Type of attenuation for the light."""
    BottomBarnDoor:float
    """Read Write Property: Angle of bottom barn door."""
    CastLightOnObject:bool
    """Read Write Property: Cast light on object?"""
    CastShadows:bool
    """Read Write Property: Cast shadows on object?"""
    ConeAngle:float
    """DEPRECATED  Equivalent to OuterAngle."""
    DiffuseColor:FBColor
    """Read Write Property: Color: Diffuse color."""
    DrawFrontFacingVolumetric:bool
    """Read Write Property: Draw front facing volumetric light?"""
    DrawGroundProjection:bool
    """Read Write Property: Draw ground projection of gobo?"""
    DrawVolumetricLight:bool
    """Read Write Property: Draw volumetric light with gobo?"""
    EAreaLightShapes:_Enum
    EnableBarnDoor:bool
    """Read Write Property: Whether or not enable barn door."""
    FogIntensity:float
    """Read Write Property: Intensity of the fog (spot light)."""
    GoboMedia:FBVideo
    """Read Write Property: Media to use as a Gobo with the light."""
    InnerAngle:float
    """Read Write Property: Inner Cone angle for light."""
    Intensity:float
    """Read Write Property: Light intensity."""
    LeftBarnDoor:float
    """Read Write Property: Angle of left barn door."""
    LightType:FBLightType
    """Read Write Property: Type of light."""
    OuterAngle:float
    """Read Write Property: Outer Cone angle for light."""
    RightBarnDoor:float
    """Read Write Property: Angle of right barn door."""
    TopBarnDoor:float
    """Read Write Property: Angle of top barn door."""
    eRectangle:EAreaLightShapes
    eSphere:EAreaLightShapes
class FBCameraSwitcher(FBModel):
    """Camera switcher.
    This class is a wrapper around the system's camera switcher object. There can only be one switcher in a given scene. Any attempts at creating a new instance will return the existing one. See sample: CameraSwitcher.py."""
    CurrentCamera:FBCamera
    """Read Write Property: Camera currently being used by the switcher. Set to NULL to turn on evaluate switch, otherwise manual switch."""
    CurrentCameraIndex:int
    """Read Write Property: Camera index currently being used by the switcher. Set to -1 to turn on evaluate switch."""
    def PlotToCamera(self,Camera:FBCamera)->bool:
        """Plot the Camera Switcher animation onto a destination camera.
        The destination camera cannot be a system camera nor a camera currently used by the Camera Switcher.
        
        Camera : Destination camera to plot on.
        return : True if the plot operation has been processed successfully, false otherwise."""
        ...
    def UseEvaluateSwitch(self):...
class FBCamera(FBModel):
    """Creates custom cameras and manages system cameras.
    When you look at a scene in the MotionBuilder Viewer, you are using a camera view.There are two types of cameras: Producer cameras. By default one of the producer cameras is used. These are always present. They can be configured but not destroyed. Custom cameras, created by the user.The SystemCamera property indicates whether a given camera is a producer or a custom camera.When you create a camera you should make it visible with the show property (inherited from FBModel).Use FBCameraSwitcher to get and set the current camera. For usage, see the Python sample CameraSwitcher.py.To see how to create a camera with a marker as an interest, see the Python sample code in FBCamera.py. For usage in C++, see the manipcamera sample. See samples: NewCamera.py, RenderLayers.py, CameraSwitcher.py, SetAllCamerasBackgroundColor.py, SetAllCamerasBackgroundColorFromCurrentCamera.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py, FBCamera.py."""
    AnimatableFarPlane:property
    AnimatableNearPlane:property
    AntiAliasingIntensity:float
    """Read Write Property: Anti-aliasing intensity."""
    AntiAliasingMethod:FBCameraAntiAliasingMethod
    """Read Write Property: Anti-aliasing method."""
    ApertureMode:FBCameraApertureMode
    """Read Write Property: Aperture mode."""
    BackGroundColor:FBColor
    """Read Write Property: Background color for camera."""
    BackGroundImageCenter:bool
    """Read Write Property: Center the background image"""
    BackGroundImageCrop:bool
    """Read Write Property: Crop the background image"""
    BackGroundImageFit:bool
    """Read Write Property: Fit the background image"""
    BackGroundImageKeepRatio:bool
    """Read Write Property: Keep the background image's ratio"""
    BackGroundImageOffsetX:float
    """Read Write Property: Ignored if BackGroundImageFit is true. X offset, in term of percentage of the fit background image width, applied on the background image."""
    BackGroundImageOffsetY:float
    """Read Write Property: Ignored if BackGroundImageFit is true. Y offset, in term of percentage of the fit background image height, applied on the background image."""
    BackGroundImageScaleX:float
    """Read Write Property: Ignored if BackGroundImageFit is true. X scale, in term of percentage of the fit background image width, applied on the background image."""
    BackGroundImageScaleY:float
    """Read Write Property: Ignored if BackGroundImageFit and/or BackGroundImageKeepRatio is true. Y scale, in term of percentage of the fit background image height, applied on the background image. The X scale property is considered instead of this Y scale property if BackGroundImageKeepRatio is set to true."""
    BackGroundMedia:FBVideo
    BackGroundPlaneDistance:float
    """Read Write Property: Set the distance for the background plane."""
    BackGroundPlaneDistanceMode:FBCameraDistanceMode
    """Read Write Property: Select mode for the background plane's distance."""
    BackGroundTexture:FBTexture
    """Read Write Property: Background Texture"""
    CameraViewportHeight:int
    """Read Only Property: Camera Viewport height"""
    CameraViewportWidth:int
    """Read Only Property: Camera Viewport width"""
    CameraViewportX:int
    """Read Only Property: Camera Viewport start position's X value"""
    CameraViewportY:int
    """Read Only Property: Camera Viewport start position's Y value"""
    Display2DMagnifierFrame:bool
    """Read Write Property: Enable/Disable the drawing of the 2D Magnifier frame box."""
    DisplayTurnTableIcon:bool
    """Read Write Property: Enable/Disable the drawing of the Turn Table icon."""
    FarPlaneDistance:float
    """Read Write Property: Far plane distance."""
    FieldOfView:float
    """Read Write Property: Field of View (used when in horizontal or vertical aperture modes)."""
    FieldOfViewX:float
    """Read Write Property: Field of View X angle (used in horizontal and vertical aperture mode)."""
    FieldOfViewY:float
    """Read Write Property: Field of View Y angle (used in horizontal and vertical aperture mode)."""
    FilmAspectRatio:float
    """Read Write Property: Film aspect ratio."""
    FilmBackType:FBCameraFilmBackType
    """Read Write Property: Film back standard type."""
    FilmSizeHeight:float
    """Read Write Property: Height of the film."""
    FilmSizeWidth:float
    """Read Write Property: Width of the film."""
    FocalLength:float
    """Read Write Property: Focal Length."""
    FocusAngle:float
    """Read Write Property: Focus Angle (rendering dof)."""
    FocusDistanceSource:FBCameraFocusDistanceSource
    """Read Write Property: Select source for focusing."""
    FocusModel:FBModel
    """Read Write Property: Another model that determines the focus distance."""
    FocusSpecificDistance:float
    """Read Write Property: Specfic distance for focusing."""
    ForeGroundAlpha:float
    """Read Write Property: Opacity of foreground."""
    ForeGroundImageCenter:bool
    """Read Write Property: Center the foreground image"""
    ForeGroundImageCrop:bool
    """Read Write Property: Crop the foreground image"""
    ForeGroundImageFit:bool
    """Read Write Property: Fit the foreground image"""
    ForeGroundImageKeepRatio:bool
    """Read Write Property: Keep the foreground image's ratio?"""
    ForeGroundImageOffsetX:float
    """Read Write Property: Ignored if ForeGroundImageFit is true. X offset, in term of percentage of the fit foreground image width, applied on the foreground image."""
    ForeGroundImageOffsetY:float
    """Read Write Property: Ignored if ForeGroundImageFit is true. Y offset, in term of percentage of the fit foreground image height, applied on the foreground image."""
    ForeGroundImageScaleX:float
    """Read Write Property: Ignored if ForeGroundImageFit is true. X scale, in term of percentage of the fit foreground image width, applied on the foreground image."""
    ForeGroundImageScaleY:float
    """Read Write Property: Ignored if ForeGroundImageFit and/or ForeGroundImageKeepRatio is true. Y scale, in term of percentage of the fit foreground image height, applied on the foreground image. The X scale property is considered instead of this Y scale property if ForeGroundImageKeepRatio is set to true."""
    ForeGroundMaterialThreshold:float
    """Read Write Property: Material threshold for a transparent foreground."""
    ForeGroundMedia:FBVideo
    ForeGroundPlaneDistance:float
    """Read Write Property: Set the distance for the foreground plane."""
    ForeGroundPlaneDistanceMode:FBCameraDistanceMode
    """Read Write Property: Select mode for the foreground plane's distance."""
    ForeGroundTexture:FBTexture
    """Read Write Property: ForeGround Texture"""
    ForeGroundTransparent:bool
    """Read Write Property: Is the foreground transparent?"""
    FrameColor:FBColor
    """Read Write Property: Frame color for camera."""
    FrameSizeMode:FBCameraFrameSizeMode
    """Read Write Property: Frame size standard mode."""
    HUDs:FBPropertyListHUD
    """List : HUDs present in this camera"""
    InteractiveMode:bool
    """Read Write Property: Interactive mode?"""
    Interest:FBModel
    """Read Write Property: Direct camera's interest."""
    MagnifierPosX:float
    """Read Write Property: 2D Magnifier X Position."""
    MagnifierPosY:float
    """Read Write Property: 2D Magnifier Y Position."""
    MagnifierZoom:float
    """Read Write Property: 2D Magnifier Zoom value."""
    MotionBlurIntensity:float
    """Read Write Property: Motion Blur Intensity."""
    MouseLockCamera:bool
    """Read Write Property: Mouse lock for camera?"""
    NearPlaneDistance:float
    """Read Write Property: Near plane distance."""
    NumberOfSamples:int
    """Read Write Property: Number of samples to oversample with."""
    OpticalCenterX:float
    """Read Write Property: Optical Center X (mm)."""
    OpticalCenterY:float
    """Read Write Property: Optical Center Y (mm)."""
    OrthoFactor:float
    """Constant scale factor to be used with OrthoZoom for orthographic cameras."""
    OrthoZoom:float
    """Read Write Property: Zoom factor of an orthographic camera."""
    PixelAspectRatio:float
    """Read Write Property: Pixel aspect ratio."""
    ResolutionHeight:float
    """Read Write Property: Resolution height."""
    ResolutionMode:FBCameraResolutionMode
    """Read Write Property: Resolution standard mode."""
    ResolutionWidth:float
    """Read Write Property: Resolution width."""
    Roll:float
    """Read Write Property: Camera's roll on it's Z axis."""
    SafeAreaMode:FBCameraSafeAreaMode
    """Read Write Property: Select mode for safe area."""
    SamplingType:FBCameraSamplingType
    """Read Write Property: Type of over sampling."""
    SqueezeRatio:float
    """Read Write Property: Squeeze ratio."""
    SystemCamera:bool
    """Read Only Property: Indicate if this a producer (default or system) camera or a custom (user-created) camera."""
    TurnTable:float
    """Read Write Property: Camera's rotation around its interest."""
    Type:FBCameraType
    """Read Write Property: Type of camera"""
    Use2DMagnifier:bool
    """Read Write Property: Enable/Disable the 2D Magnifier."""
    UseAccumulationBuffer:bool
    """Read Write Property: Use accumulation buffer?"""
    UseAntiAliasing:bool
    """Read Write Property: Use anti-aliasing?"""
    UseDepthOfField:bool
    """Read Write Property: Use depth of field calculations?"""
    UseFrameColor:bool
    """Read Write Property: Use frame color?"""
    UseMotionBlur:bool
    """Read Write Property: Enable Motion Blur."""
    UseRealTimeMotionBlur:bool
    """Read Write Property: Enable Real-time Motion Blur."""
    ViewBackGroundPlaneMode:FBCameraViewPlaneMode
    """Read Write Property: Background plane view mode"""
    ViewCameraInterest:bool
    """Read Write Property: Show the camera interest?"""
    ViewDisplaySafeArea:bool
    """Read Write Property: Display safe area?"""
    ViewForeGroundPlaneMode:FBCameraViewPlaneMode
    """Read Write Property: Foreground plane view mode"""
    ViewNearFarPlane:bool
    """Read Write Property: Show near/far planes?"""
    ViewOpticalCenter:bool
    """Read Write Property: View optical center?"""
    ViewShowAxis:bool
    """Read Write Property: Show axis?"""
    ViewShowGrid:bool
    """Read Write Property: Show grid?"""
    ViewShowName:bool
    """Read Write Property: Show name?"""
    ViewShowTimeCode:bool
    """Read Write Property: Show time code?"""
    WindowHeight:float
    """Read Only Property: Window height."""
    WindowWidth:float
    """Read Only Property: Window width."""
    def GetCameraMatrix(self,Matrix:FBMatrix,Type:FBCameraMatrixType,EvalInfo:FBEvaluateInfo=None):
        """Obtains the camera's matrix.
        
        Matrix : Matrix to fill with requested information.
        Type : Camera Matrix type to obtain.
        EvalInfo : Take Display if none specified."""
        ...
    def InverseProjection(self,X:int,Y:int,DistanceFromCamera:float)->FBVector4d:
        """Returns the world coordinates based on screen coordinates and input distance from the camera.
        
        X : Screen horizontal coordinate in pixel. WhenRelativeToViewport is false, the range is between 0 and (WindowWidth - 1). WhenRelativeToViewport is true, the range is between 0 to (CameraViewportWidth - 1). The coordinate starts at left of the region.
        Y : Screen vertical coordinate in pixel. WhenRelativeToViewport is false, the range is between 0 and (WindowHeight - 1). WhenRelativeToViewport is true, the range is between 0 to (CameraViewportHeight - 1). The coordinate starts at top of the region.
        DistanceFromCamera : Distance from the camera to the resulting world coordinate position
        RelativeToViewport : true indicates (pX,pY) is relative to the window; false indicates (pX,pY) is relative to the viewport of the camera.
        return : The world coordinates in 3D space"""
        ...
class FBModelMarker(FBModel):
    """Model marker class.
    See sample: FBCamera.py."""
    Color:FBColor
    """Read Write Property: Color of model marker."""
    IKPivot:FBVector3d
    """Read Write Property: marker Pivot Offset."""
    Length:float
    """Read Write Property: Length for capsule (not related to scaling)."""
    Look:FBMarkerLook
    """Read Write Property: Look of model marker."""
    ResLevel:FBMarkerResolutionLevel
    """Read Write Property: Resolution level of model marker."""
    Size:float
    """Read Write Property: Size (not related to scaling)."""
    Type:FBMarkerType
    """Read Write Property: Type of model marker."""
class FBCameraStereo(FBCamera):
    CenterCamera:FBCameraStereo
    """Read Write Property:  This property hold the center camera connected to it. Must be either the master, left or right camera."""
    DisplayZeroParallaxPlane:bool
    """Read Write Property:  Display the zero parallax plane."""
    FilmOffsetLeftCam:float
    """Read Write Property:  This property handles the film offset for the left camera. (inch)"""
    FilmOffsetRightCam:float
    """Read Write Property:  This property handles the film offset for the right camera. (inch)"""
    InteraxialSeparation:float
    """Read Write Property:  This property handles the distance between left and right cameras."""
    LeftCamera:FBCamera
    """Read Write Property:  This property hold the left camera connected to it."""
    PrecompFileName:str
    """Read Write Property:  This property handles the precomp file name."""
    RelativePrecompFileName:str
    """Read Write Property:  This property handles the relative precomp file name."""
    RightCamera:FBCamera
    """Read Write Property:  This property hold the right camera connected to it."""
    Stereo:FBCameraStereoType
    """Read Write Property:  //!< This property handles the types of Stereo camera."""
    ToeInAdjust:float
    """Read Write Property:  This property is to offset the computed toe-in effect when it's in Converged mode."""
    ZeroParallax:float
    """Read Write Property:  This property handles the distance on the camera view axis where the zero parallax plane occurs."""
    ZeroParallaxPlaneColor:FBColor
    """Read Write Property:  Zero parallax plane color."""
    ZeroParallaxPlaneTransparency:float
    """Read Write Property:  Zero parallax plane transparency."""
class FBModelNull(FBModel):
    """Null object class."""
    Size:float
    """Read Write Property: Size (not related to scaling)."""
class FBModelMarkerOptical(FBModelMarker):
    """Optical model marker class."""
    Data:FBAnimationNode
    """Property: Data."""
    Done:bool
    """Property: Done?"""
    Gaps:FBPropertyListOpticalGap
    """Property: Gaps."""
    Optical:FBModelOptical
    """Property: Optical model."""
    Segments:FBPropertyListMarkerSegment
    """Property: Marker segments."""
    def ExportBegin(self)->int:
        """Begin export of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.
        
        return : Number of frames to export."""
        ...
    def ExportEnd(self)->bool:
        """End exportation from optical model.
        
        return : true if successful."""
        ...
    def ExportKey(self,X:float,Y:float,Z:float=None,Occlusion:float=None)->bool:
        """Export a key of optical data.
        
        X : X position.
        Y : Y position.
        Z : Z position(default=NULL).
        Occlusion : Occlusion value(default=NULL).
        return : true if successful."""
        ...
    def GetRigidBody(self)->FBRigidBody:
        """Get the rigid body for the marker.
        
        return : Rigid body for marker (check IsValid())"""
        ...
    def ImportBegin(self)->int:
        """Begin import of optical data.
        Sample communication with optical device and return the number of samples that were taken during the sampling period for statistical purposes.
        
        return : The number of samples taken."""
        ...
    def ImportEnd(self)->bool:
        """End importation and clean up data.
        Interpolates optical data to create a curve from the input key frams.
        
        return : true if successful."""
        ...
    def ImportKey(self,X:float,Y:float,Z:float=0.0,Occlusion:float=0.0)->bool:
        """Import a key of optical data.
        
        X : X position.
        Y : Y position.
        Z : Z position(default=0.0).
        Occlusion : Occlusion value(default=0.0).
        return : true if successful."""
        ...
    def InsertSegmentedData(self,TData:FBAnimationNode,OData:FBAnimationNode):
        """Insert segmented data.
        
        TData : Translation data.
        OData : Occlusion data."""
        ...
    def SetModelOptical(self,Optical:FBModelOptical):
        """Set the current optical model.
        
        Optical : New optical model."""
        ...
class FBModelOptical(FBModel):
    """Optical model class."""
    MarkerSize:float
    """Read Write Property: Size of markers."""
    Markers:FBPropertyListModelMarkerOptical
    """List: Markers."""
    RigidBodies:FBPropertyListRigidBody
    """List: Rigid bodies."""
    SamplingPeriod:FBTime
    """Read Write Property:Sampling period."""
    SamplingStart:FBTime
    """Read Write Property: Sampling start time."""
    SamplingStop:FBTime
    """Read Write Property:Sampling stop time."""
    Segments:FBPropertyListOpticalSegment
    """List: Segments."""
    def ClearSegments(self,UnUsedOnly:bool=True):
        """Clear the segments (by default only the unused).
        
        UnUsedOnly : Clear only the unused segments if true(default=true)."""
        ...
    def CreateRigidBody(self,RigidBodyName:str,Markers:List[FBModelMarkerOptical])->FBRigidBody:
        """Create a new rigid body from the given optical markers.
        
        RigidBodyName : The name for the new rigid body to create. If left empty, the default "Rigid Body" name will be used.
        Markers : The optical markers for creating the new rigid body.
        return : The created rigid body if successful, and invalid rigid body otherwise. You can use the FBRigidBody.IsValid() method to test if the returned rigid body object is valid or not."""
        ...
    def ExportSetup(self)->bool:
        """Setup exportation from optical model.
        
        return : true if successful."""
        ...
    def ImportSetup(self)->bool:
        """Setup importation for optical model.
        
        return : true if successful."""
        ...
class FBModelPath3D(FBModel):
    """Path 3D model class."""
    AutoControlNode:bool
    """Read Write Property: Automatically create key control nodes."""
    Color:FBColor
    """Read Write Property: Path display color in viewport."""
    EKeyPropertyBehavior:_Enum
    ELengthUnitType:_Enum
    EPathEndCapStyle:_Enum
    KeyPropertyBehavior:KeyPropertyBehavior
    """Read Only Property: Key property behavior."""
    PathEndCapScale:float
    """Read Write Property: Path end cap display scale."""
    PathEndCapStyle:PathEndCapStyle
    """Read Write Property: Path end cap display style."""
    PathLength:float
    """Read Only Property: Path Length In Centimeter."""
    PathLengthInString:str
    """Read Only Property: Path Length Display String According To The Current Unit."""
    PathLengthShow:bool
    """Read Write Property: Path length label display or not."""
    PathLengthUnit:property
    """Read Write Property: Path Length Unit."""
    TextBackground:FBColorAndAlpha
    """Read Write Property: Path Length label display background color."""
    TextScale:float
    """Read Write Property: Path Length label display scale."""
    eArchitectural:ELengthUnitType
    eArrow:EPathEndCapStyle
    eCM:ELengthUnitType
    eKM:ELengthUnitType
    eLegacyVector4:EKeyPropertyBehavior
    eM:ELengthUnitType
    eMI:ELengthUnitType
    eNone:EPathEndCapStyle
    eVector:EKeyPropertyBehavior
    def ConvertSegmentPercentToTotalPercent(self,Percent:float,EvaluateInfo:FBEvaluateInfo=None)->float:
        """Converting one key type Segment (time) to Total (percent).
        
        Percent : Double value (as time)
        EvaluateInfo : FBEvaluateInfo
        return : Double value which represents the corresponding percentage"""
        ...
    def ConvertToSegmentPercentFactor(self)->float:
        """Get factor for multiplying the derivative of a key for segment mode.
        
        return : Returns the derivative multiplication factor"""
        ...
    def ConvertToTotalPercentFactor(self)->float:
        """Get factor for multiplying the derivative of a key for total mode.
        
        return : Returns the time factor"""
        ...
    def ConvertTotalPercentToSegmentPercent(self,Percent:float,EvaluateInfo:FBEvaluateInfo=None)->float:
        """Converting one key type Total (percent) to Segment (time).
        
        Percent : Double value (as percentage)
        EvaluateInfo : FBEvaluateInfo
        return : Double value which represents the corresponding time."""
        ...
    def GetSelectedPathKeyCount(self)->int:
        """Query the number of keys present in the selected path.
        
        return : Returns the number of keys in the selected path"""
        ...
    def InsertNewEndKey(self)->int:
        """Insert a new key at the end of the path.
        
        return : Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0."""
        ...
    def InsertNewStartKey(self)->int:
        """Insert a new key at the start of the path.
        
        return : Returns 0 since the new key becomes the first key. If path is invalid, returns 0."""
        ...
    def PathKeyClear(self):
        """Clear the path keys."""
        ...
    def PathKeyEndAdd(self,TLocal:FBVector4d)->int:
        """Adds a new key to the end of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the left tangent of the last key.
        
        TLocal : Vector value for the new added Key
        return : Returns (N) where (N+1) is the new total number of keys, and since the new key becomes the Nth key (index starts from 0). If path is invalid, returns 0."""
        ...
    def PathKeyGet(self,KeyIndex:int)->FBVector4d:
        """Get path's key vector for at a particular key index.
        
        KeyIndex : Key ID to set with
        return : Return the vector containing the value of the path key."""
        ...
    def PathKeyGetControlNode(self,KeyIndex:int)->FBModel:
        """Get the path key's control node.
        Only works when KeyPropertyBehavior is eVector.
        
        KeyIndex : Key ID to get
        return : Path key's corresponding control node if successful, otherwise NULL."""
        ...
    def PathKeyGetCount(self)->int:
        """Query the number of keys present in the path.
        
        return : Number of keys present in the path"""
        ...
    def PathKeyGetLeftTangent(self,KeyIndex:int)->FBVector4d:
        """Get the path key left tangent's vector value for designated index.
        
        KeyIndex : Key ID at which left tangent value is required
        return : Vector containing value of left tangent"""
        ...
    def PathKeyGetLeftTangentLength(self,KeyIndex:int)->float:
        """Query the length of the left tangent.
        
        KeyIndex : Key ID to set with
        return : Double value of the length of left tangent"""
        ...
    def PathKeyGetProperty(self,KeyIndex:int)->FBProperty:
        """Get the path key's corresponding property.
        Only works when KeyPropertyBehavior is eVector.
        
        KeyIndex : Key ID to get
        return : Path key's corresponding property if successful, otherwise NULL."""
        ...
    def PathKeyGetRightTangent(self,KeyIndex:int)->FBVector4d:
        """Get the path key right tangent's vector value for designated index.
        
        KeyIndex : Key ID to set with
        return : Vector containing value of left tangent"""
        ...
    def PathKeyGetRightTangentLength(self,KeyIndex:int)->float:
        """Query the value of the right tangent.
        
        KeyIndex : Key ID to set with
        return : Double value of the length of right tangent"""
        ...
    def PathKeyGetXYZDerivative(self,KeyIndex:int)->FBVector4d:
        """Get vector in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        
        KeyIndex : Key ID to set with
        return : Vector with value for path's tangent XYZ derivatives"""
        ...
    def PathKeyInsertAfter(self,KeyIndex:int,TLocal:FBVector4d)->int:
        """Adds a new key immediately after the specified key ID (with time gap of 1 sec).
        The following keys are all shifted by 1 sec.
        
        KeyIndex : Key ID to insert after. If key ID < 0 then the behavior is the same as PathKeyStartAdd. If key ID >= PathKeyGetCount-1 then the behavior is the same as PathKeyEndAdd.
        TLocal : Vector value for the new added Key
        return : Returns the newly inserted key ID."""
        ...
    def PathKeyRemove(self,KeyIndex:int):
        """Remove key at a particular index.
        
        KeyIndex : Key ID at which key is to be removed."""
        ...
    def PathKeyRemoveSelected(self):
        """Remove the selected keys from the path."""
        ...
    def PathKeySet(self,KeyIndex:int,TLocal:FBVector4d,Update:bool=True):
        """Set the local coordinate vector values for path at a particular key index.
        
        KeyIndex : Key ID to set with
        TLocal : Vector to use to set values to Key
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetControlNode(self,KeyIndex:int,ControlNode:FBModel)->bool:
        """Set the path key's control node.
        Only works when KeyPropertyBehavior is eVector and AutoControlNode is disabled.
        
        KeyIndex : Key ID to set
        ControlNode : Model to set as path key's control node.
        return : True if successful, otherwise false."""
        ...
    def PathKeySetLeftRightTangent(self,KeyIndex:int,KeyTLocal:FBVector4d,LeftTangentTLocal:FBVector4d,RightTangentTLocal:FBVector4d,Update:bool=True):
        """Set path's vectors for key, left tangent and right tangent at a particular key index.
        
        KeyIndex : Key ID to set key for left and right tangents
        KeyTLocal : Vector to use to set values to Key
        LeftTangentTLocal : Vector to use to set values to Key Left Tangent
        RightTangentTLocal : Vector to use to set values to Key Right Tangent
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetLeftTangent(self,KeyIndex:int,TLocal:FBVector4d,Update:bool=True):
        """Set path's key left tangent vector for designated index.
        
        KeyIndex : Key ID at which left tangent is to be set
        TLocal : Vector to use to set values to Key
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetRightTangent(self,KeyIndex:int,TLocal:FBVector4d,Update:bool=True):
        """Set 3D path's key right tangent vector for designated index.
        
        KeyIndex : Key ID at which right tangent is to be set
        TLocal : Vector to use to set values to Key
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetXDerivative(self,KeyIndex:int,Derivative:float,Update:bool):
        """Set derivative in X coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        
        KeyIndex : Key ID to set with
        Derivative : Value of the derivative to apply to tangent
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetXYZDerivative(self,KeyIndex:int,Derivative:FBVector4d,Update:bool):
        """Set derivative in XYZ coordinates for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        
        KeyIndex : Key ID to set with
        Derivative : Value of the derivative to apply to tangent
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetYDerivative(self,KeyIndex:int,Derivative:float,Update:bool):
        """Set derivative in Y coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        
        KeyIndex : Key ID to set with
        Derivative : Value of the derivative to apply to tangent
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeySetZDerivative(self,KeyIndex:int,Derivative:float,Update:bool):
        """Set derivative in Z coordinate for a path tangent.
        This works only if key interpolation type is CUBIC and tangent mode is User, Break or Auto.
        
        KeyIndex : Key ID to set with
        Derivative : Value of the derivative to apply to tangent
        Update : true if geometry update is required, false if not required (default=true)"""
        ...
    def PathKeyStartAdd(self,TLocal:FBVector4d)->int:
        """Adds a new key to the start of the path (with time gap of 1 sec).
        The derivative value for the new key is copied from the right tangent of the first key.
        
        TLocal : Vector value for the new added Key
        return : Returns 0 since the new key becomes the first key. If path is invalid, returns 0."""
        ...
    def Segment_GlobalPathEvaluate(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in global coordinates.
        
        SegmentPercent : Double value (as time) at which the path vector would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def Segment_GlobalPathEvaluateDerivative(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in global coordinates.
        
        SegmentPercent : Double value (as time) at which the path derivative would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def Segment_IsPathKey(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->int:
        """Query whether a percentage value has a key associated at that point in the path.
        
        SegmentPercent : Double value (as time) at which the path would be queried for existence of key
        EvaluateInfo : FBEvaluateInfo
        return : A valid key index in integer if key is present, otherwise -1"""
        ...
    def Segment_LocalPathEvaluate(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in local coordinates.
        
        SegmentPercent : Double value (as time) at which the path vector would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def Segment_LocalPathEvaluateDerivative(self,SegmentPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in local coordinates.
        
        SegmentPercent : Double value (as time) at which the path derivative would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def ShowCurveControls(self,Show:bool):
        """Enable or disable displaying Curve Controls for the 3D model path.
        
        Show : true if curve controls are to be displayed false if not required"""
        ...
    def ShowCurvePoints(self,Show:bool):
        """Enable or disable displaying Curve Points for the 3D model path.
        
        Show : true if curve points are to be displayed false if not required"""
        ...
    def Total_GlobalPathEvaluate(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in global coordinates.
        
        TotalPercent : Double value (as percentage) at which the path vector would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def Total_GlobalPathEvaluateDerivative(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in global coordinates.
        
        TotalPercent : Double value (as percentage) at which the path derivative would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Derivative value at the required point in the path"""
        ...
    def Total_IsPathKey(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->int:
        """Query whether a percentage value has a key associated at that point in the path.
        
        TotalPercent : Double value (as percentage) at which the path would be queried for existence of key
        EvaluateInfo : FBEvaluateInfo
        return : A valid key index in integer if key is present, otherwise -1"""
        ...
    def Total_LocalPathEvaluate(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's vector at a particular point within the curve, in local coordinates.
        
        TotalPercent : Double value (as percentage) at which the path vector would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Vector value at the required point in the path"""
        ...
    def Total_LocalPathEvaluateDerivative(self,TotalPercent:float,EvaluateInfo:FBEvaluateInfo=None)->FBVector4d:
        """Get the path's derivative at a particular point within the curve, in local coordinates.
        
        TotalPercent : Double value (as percentage) at which the path derivative would be computed
        EvaluateInfo : FBEvaluateInfo
        return : Derivative value at the required point in the path"""
        ...
    def UpdateGeometry(self):
        """Update path geometry explicitly."""
        ...
class FBModelPlane(FBModel):
    """Plane model class."""
    ...
class FBModelRoot(FBModel):
    """Root object class.
    See sample: SelectModelsWithNameContainingSubstring.py."""
    Size:float
    """Read Write Property: Size (not related to scaling)."""
class FBModelSkeleton(FBModel):
    """Root object class."""
    Color:FBColor
    """Read Write Property: Color of skeleton node."""
    Length:float
    """Read Write Property: Length of skeleton node. (Note: Only effective when the look is set to: Capsule)"""
    LinkFollowGeometryOffset:bool
    """Read Write Property: Whether link to parent node must follow skeleton node or not, when skeleton node has a geometry offset."""
    Look:FBSkeletonLook
    """Read Write Property: Look of skeleton node."""
    PreserveLinkEndPosition:bool
    """Read Write Property: Whether skeleton node must preserve its links' end position to children nodes, when skeleton node has a geometry offset. (Note: Only effective when the look is set to: Bone, Box or Stick)"""
    Resolution:FBSkeletonResolutionLevel
    """Read Write Property: Resolution of skeleton node. (Note: Only effective when the look is set to: Sphere, Capsule or Stick)"""
    Size:float
    """Read Write Property: Size (not related to scaling)."""
    def GetSkinModelList(self,SkinModelList:FBModelList):
        """Return the list of skin model associated with this Skeleton(Bone), which could be the deformable skins connected via cluster, or non deformable skins which are parented directly under this bone.
        
        SkinModelList : List to be appended with skin models (with no duplicated items)."""
        ...
class FBPhysicalProperties(FBBox):
    """Base class for physical properties attach to a model.
    See sample: RigiBody.py."""
    ...
class FBAudioIn(FBComponent):
    """Audio In class.
    Used to control Audio In objects (like a Microphone Audio Device).
    
    >>> # This example shows how to prepare an FBAudioIn object for recording
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
    if lSupportedFormats & FBAudioFmt_ConvertBitDepthMode( FBAudioBitDepthMode.kFBAudioBitDepthMode_8 ) != 0 and        lSupportedFormats & FBAudioFmt_ConvertRateMode( FBAudioRateMode.kFBAudioRateMode_22050 ) != 0 and        lSupportedFormats & FBAudioFmt_ConvertChannelMode( FBAudioChannelMode.kFBAudioChannelModeStereo ) != 0:
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
    print 'Something failed while preparing to record! Tip: Do you have a C:	emp folder?'
    else:
    print 'This format (8-bit, 22060 hz, stereo) is not supported!'
    else:
    print 'No available Audio In object available'"""
    def GetDelay(self)->FBTime:
        """Returns the delay currently set.
        (Windows only).
        
        return : The delay currently set."""
        ...
    def GetDestination(self)->FBAudioOut:
        """Returns the Audio Out object currently used as the destination.
        (Windows only).
        
        return : The Audio Out object currently used as the destination. Returns a NULL pointer (None in Python) if any Audio Out object is currently set."""
        ...
    def GetRecordingFormat(self)->int:
        """Returns the recording format (i.e.
        Bit Depth, Rate and Channel(s)) currently set.
        
        return : The audio format currently set for recording."""
        ...
    def GetSupportedFormats(self)->int:
        """Returns all the Audio In supported formats (i.e.
        Bit Depths, Rates and Channels).
        
        return : The Audio In supported formats."""
        ...
    def IsOnline(self)->bool:
        """Is the Audio In online?
        
        return : True if the Audio In is online, false if it is offline."""
        ...
    def IsReadyToRecord(self)->bool:
        """Is the Audio In ready to record (has it been prepared properly)?
        
        return : True if the audio is ready to record, false otherwise."""
        ...
    def PrepareToRecord(self,RecordingPath:str,ExistingClipAction:FBExistingClipAction=FBExistingClipAction.kFBExistingClipAskUser,ExistingFileAction:FBExistingFileAction=FBExistingFileAction.kFBExistingFileAskUser)->bool:
        """Prepares the Audio In for recording (similar as checking the 'Record' checkbox in the UI).
        If the Audio In is not already online, it will turn it online automatically. If the Audio In is already ready to record, it will turn it off first automatically.
        
        RecordingPath : The file path for the desired output wav file. The file must have the .wav extension.
        ExistingClipAction : The action to perform when the action clip associated to the recording path is already in the scene.
        ExistingFileAction : The action to perform when the file associated to the recording path already exists on disk and it not empty.
        return : True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified file is not a WAV file or is invalid, the operation is abort by the user, etc.)."""
        ...
    def SetDelay(self,Delay:FBTime)->bool:
        """Sets the delay to use.
        The Audio In must be offline when this method is called. (Windows only).
        
        Delay : The delay to use. To mimic the UI, the FBTime should refer to a frame number.
        return : True if operation is successful, false otherwise."""
        ...
    def SetDestination(self,AudioOut:FBAudioOut)->bool:
        """Sets the Audio Out object to be used as the destination.
        The Audio In must be offline when this method is called. (Windows only).
        
        AudioOut : The Audio Out object to be used as the destination. Use a NULL pointer (None in Python) to unset the destination.
        return : True if operation is successful, false otherwise."""
        ...
    def SetOnline(self,Online:bool)->bool:
        """Turns Audio In online or offline.
        
        Online : True to turn the Audio In online, false to turn it offline.
        return : True if operation is successful, false otherwise."""
        ...
    def SetRecordingFormat(self,AudioFormat)->bool:
        """Sets the recording format (i.e.
        Bit Depth, Rate and Channel(s)) to use. The Audio In must be offline when this method is called.
        
        AudioFormat : The audio format to use for recording. It must specify a unique Bit Depth, Rate and Channels.
        return : True if operation is successful, false otherwise. It could fail for different reasons (e.g. the specified audio format is not supported, more than one Bit Depth is specified, etc.)."""
        ...
    def TurnOffRecording(self)->bool:
        """Turns off the Audio In recording (similar as un-checking the 'Record' checkbox in the UI).
        
        return : True if operation is successful, false otherwise."""
        ...
class FBAudioClip(FBComponent):
    """Used to play audio clips and access their properties.
    This class permits you to access audio clip's properties to read or change them. See sample: AudioTrackSetupTool.py."""
    AccessMode:FBAccessMode
    """Read Write Property: Specify the media data access mode between disk or memory."""
    Bits:int
    """Read Only Property: the bits of media."""
    Channels:int
    """Read Only Property: the number of channels in use."""
    ClipSpeed:float
    """Read Write Property: The speed of the media when being played."""
    ConstrainDstToTake:bool
    """Read Write Property: Indicates whether to constrain the EndPoint to the end of the take."""
    CurrentTake:FBTake
    """Read Write Property: The take this media belongs to."""
    Destination:FBAudioOut
    """Read Write Property: The audio output destination where the clip will be played."""
    DstDuration:FBTime
    """Read Write Property: When not used in the Story, this specify when the clips stops playing."""
    DstEnd:FBTime
    """Read Write Property: Total duration of this audio clip."""
    DstIn:FBTime
    """Read Write Property: When not used in the Story, this specify when the clips begin to play."""
    Duration:FBTime
    """[Deprecated]Read Write Property: Refer to DstDuration."""
    EndPoint:FBTime
    """[Deprecated]Read Write Property: Refer to DstEnd."""
    Filename:str
    """[Deprecated]Read Only Property: Refer to Path"""
    Format:int
    """Read Only Property: Data format of media, including rate, bits and channels count. You can typecast it to a FBAudioFmt."""
    InPoint:FBTime
    """[Deprecated]Read Write Property: Refer to DstIn."""
    LockClipSpeed:bool
    """Read Write Property: Indicates whether to lock the current playing speed."""
    LockPitchToSpeed:bool
    """Read Write Property: Time stretch enabled factor."""
    Path:str
    """Read Only Property: Full Path of the media."""
    Pitch:float
    """Read Write Property: The audio clip pitch value. To write to this property, you must first set LockPitchToSpeed property to false."""
    Rate:int
    """Read Only Property: the rate of media."""
    RelativePath:str
    """Read Only Property: Relative path of media."""
    Scrubbing:bool
    """Read Write Property: Control which clip (one at a time) can shuttle when playing a various speeds."""
    SrcDuration:FBTime
    """Read Only Property: The duration time of media."""
    SrcEnd:FBTime
    """Read Only Property: The end time of media."""
    SrcIn:FBTime
    """Read Only Property: The begin time of media."""
    TakeSetsInPoint:bool
    """[Deprecated]Read Write Property: Indicates whether to lock the InPoint to the start of the take."""
    UseChannel:FBUseChnMode
    """Read Write Property: Enables you to control which track are used with stereo clips."""
    UseChannelMode:FBUseChnMode
    """[Deprecated]Read Write Property: Enables you to control which track are used with stereo clips."""
    def IsMediaReady(self)->bool:
        """Check if the audio clip constructed properly.
        
        return : true if the audio clip was constructed properly."""
        ...
    def Play(self,Style:FBTriggerStyle=FBTriggerStyle.kFBTriggerStyleContinue,Destination:FBAudioOut=None)->bool:
        """Play audio clip now.
        
        Style : How the audio clip should be triggered.
        Destination : Where the audio clip should be played. If NULL, it will play on the default destination.
        return : Return true if the buffer for the audio clip was successfully allocated so that you can hear the sound."""
        ...
    def Stop(self,Destination:FBAudioOut=None):
        """Stop any playing triggered audio clip on a specified destination.
        
        Destination : Where the audio clip is playing. If NULL, the default destination will be used."""
        ...
class FBAssetMng(FBComponent):
    """Used to access asset manager functionity to get files locally or from a server."""
    Description:str
    """Read Write Property: Description of the manager."""
    LastError:str
    """Last error string."""
    MenuFlags:int
    """Read Write Property: Flags specifing which menu items are added by the manager."""
    def BrowseForFile(self)->FBAssetFile:
        """Let the user browse the asset database to select a file.
        
        return : A file object representing the file that was selected, or NULL if none."""
        ...
    def BrowseForFolder(self)->FBAssetFolder:
        """Let the user browse the asset database to select a folder.
        
        return : A FBAssetFolder* object representing the folder that was selected, or NULL if none."""
        ...
    def CheckAvailability(self)->bool:
        """Check if this manager can be used on the computer."""
        ...
    def CreateServerPath(self,ServerPath:str)->FBAssetFolder:
        """Create a folder path on the server side by adding each missing folders.
        
        ServerPath : The path to create on the server side.
        return : A FBAssetFolder* object representing the deepest folder of the path."""
        ...
    def FileIsManaged(self,Filename:str)->bool:
        """Is the specified local file managed (ie.
        also present in the database).
        
        Filename : Path to the file on the local disk.
        return : A boolean indicating if the file is managed or not."""
        ...
    def GetAssetFile(self,ServerFilename:str)->FBAssetFile:
        """Get a file object using it's server path.
        
        ServerFilename : Path to the file on the server.
        return : An FBAssetFile* object, or NULL if the file was not found."""
        ...
    def GetAssetFileFromLocalPath(self,LocalFilename:str)->FBAssetFile:
        """Get a file object using it's local path.
        
        LocalFilename : Path to the file on the local disk.
        return : An FBAssetFile* object, or NULL if the file was not found or no mapping could be done."""
        ...
    def GetAssetFolder(self,ServerPath:str)->FBAssetFolder:
        """Get a folder object using it's server path.
        
        ServerPath : Path the the folder on the server.
        return : An FBAssetFolder* object, or NULL if the folder was not found."""
        ...
    def GetAssetFolderFromLocalPath(self,LocalPath:str)->FBAssetFolder:
        """Get a folder object using it's local path.
        
        LocalPath : Path to the folder on the local disk.
        return : An FBAssetFolder* object, or NULL if the folder was not found or no mapping could be done."""
        ...
    def GetFileOptions(self)->int:
        """Get the file options (i.e.
        what to do when loading, saving or closing managed files).
        
        return : The options."""
        ...
    def Initialize(self)->bool:
        """Initialize the connection to the server.
        
        return : True if the connection was established, false otherwise."""
        ...
    def MapLocalPathToServerPath(self,LocalPath:str)->str:
        """Convert the local path to a server path by using managed paths mapping.
        
        LocalPath : Local path to be mapped.
        return : A string with the resulting server path, will be empty if the mapping fail."""
        ...
    def ShowSettings(self):
        """Display a dialog that let the user changes settings."""
        ...
    def WithinManagedPath(self,LocalPath:str)->bool:
        """Is the specified local path below a managed path.
        
        LocalPath : Local path to be checked.
        return : A boolean indicating if the path is within a managed path or not."""
        ...
class FBAssetItem(FBComponent):
    """Base class for all managed assets."""
    LastError:str
    """Last error string."""
    def CheckIn(self,Comment:str="",KeepCheckedOut:bool=False,Silent:bool=False)->bool:
        """Checks in this item and all its children (if this is a folder item).
        
        Comment : Comment to be applied for the check in.
        KeepCheckedOut : Flag that indicates whether the item will be kept checked out.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : A boolean indicating if the operation was successful."""
        ...
    def CheckOut(self,Comment:str="",DontGetLocal:bool=False,Silent:bool=False)->bool:
        """Checks out this item and it's childs (if this is a folder item) and makes them writeable on the local disk.
        
        Comment : Comment to be applied for the check out.
        DontGetLocal : Indicate if local copy should retrieved or not.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : A boolean indicating if the operation was successful."""
        ...
    def GetLatest(self,ReplaceCheckedOut:bool=False,Silent:bool=False)->bool:
        """Obtain the latest version of the item from the server.
        
        ReplaceCheckedOut : Whether to replace the checked out file or not.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : A boolean indicating if the operation was successful."""
        ...
    def GetLocalPath(self)->str:
        """Get the path to this item on the local hard disk.
        
        return : The path as an FBString."""
        ...
    def GetName(self)->str:
        """Get the name of this item (file name or folder name).
        
        return : The name of the item, as an FBString."""
        ...
    def GetParent(self)->FBAssetFolder:
        """Get the parent folder of this item.
        
        return : An FBAssetFolder* if the parent was found, or NULL if this is the root item."""
        ...
    def GetServerPath(self)->str:
        """Get the path to this item on the database.
        
        return : The server path as an FBString."""
        ...
    def ShowHistory(self):
        """Display a dialog with this item history."""
        ...
    def ShowProperties(self):
        """Display a dialog showing the properties of this item."""
        ...
    def UndoCheckOut(self,ReplaceLocalFile:bool=True,Silent:bool=False)->bool:
        """Cancel the last check out operation.
        
        ReplaceLocalFile : Flag indicating if the local item(s) should be replaced by the server version.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : A boolean indicating if the operation was successful."""
        ...
class FBApplication(FBComponent):
    """FBApplication is used mainly to manage files.
    It provides functionality like that in the MotionBuilder file menu, for example, open file, save file.Note that event registration is instanced-based. When an FBApplication object is destroyed, all the event callbacks are unregistered. If you want to have a tool to be notified of events, it needs to have a FBApplication data member. See samples: FBFbxOptions.py, FBSystemEvents.py, ImportWithNamespace.py, BatchExportCharacterAnimationTool.py, ExportAnimationLibrary.py, SaveOneTakePerFile.py."""
    CurrentActor:FBActor
    """Read Write Property: Indicate the current actor, as used by the character tool. Can be NULL. If not null, CurrentCharacter must be null, as the character tool works on only one item at a time."""
    CurrentCharacter:FBCharacter
    """Read Write Property: Indicate the current character, as used by the character tool. Can be NULL. If not null, CurrentActor must be null, as the character tool works on only one item at a time. See sample: CurrentCharacterGoToStancePose.py."""
    FBXFileName:str
    """Read Write Property: Current scene filename."""
    OnFileExit:FBEvent
    """Event: A File Exit as been requested, nothing has been destroyed yet."""
    OnFileMerge:FBEvent
    """Event: A File Merge has been requested, nothing has been loaded yet."""
    OnFileNew:FBEvent
    """Event: A File New has been requested, nothing has been destroyed yet."""
    OnFileNewCompleted:FBEvent
    """Event: A File New has been completed."""
    OnFileOpen:FBEvent
    """Event: A File Open has been requested, nothing has been loaded yet."""
    OnFileOpenCompleted:FBEvent
    """Event: A File Open has been completed."""
    OnFileSave:FBEvent
    """Event: A File Save has been requested, nothing has been saved yet."""
    OnFileSaveCompleted:FBEvent
    """Event: A File Save has been completed."""
    OnOverrideFileOpen:FBEventOverrideFileOpen
    """Event: Called when a file is about to be opened/merged. The user can override the process with his own file import system."""
    def AudioRender(self,AudioRenderOptions:FBAudioRenderOptions=None)->bool:
        """Render audio of current scene to media file, currently WAV file only.
        
        AudioRenderOptions : The options used when rendering audio of the scene. Default value: 2 channels, 16 bits, 44100 hz, the begin and end time span for current time referential, Default file name is "Output.wav" in the last audio output path, ro the default document path if the last path doesn't exist.
        return : True if the file was rendered successfully"""
        ...
    def ExecuteScript(self,Filename:str)->bool:
        """Execute a python script file.
        
        Filename : The script file to execute.
        return : True if the script file was found and executed."""
        ...
    def FileAppend(self,Filename:str,ShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Append one or multiple files to the current scene.
        Same as File->Merge in the menus with all options set to append. In earlier versions of MotionBuilder, a namespace could be specified with a parameter in this function, or FBFbxOptions::CustomImportNamespace, Now this is now done with FBFbxOptions::NamespaceList.
        
        Filename : File(s) to merge. For multiple files, use a list of files separated by '~'.
        ShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false).
        Options : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property andShowUIMsg are true. It is possible to append multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored.
        return : true if successful."""
        ...
    def FileBatch(self,BatchOptions:FBBatchOptions,PlotOptions:FBPlotOptions=None)->FBBatchStatus:
        """Start a batch.
        Command File->Batch... in the menus.
        
        BatchOptions : The options for the batch process (same as in the batch UI).
        PlotOptions : The options for plotting (same as in the plot UI)(default=NULL).
        return : The status of the operation."""
        ...
    def FileExit(self,Save:bool=False,ExitCode:int=0):
        """Quit application.
        Command File->Exit in the menus.
        
        Save : true if file is saved on exit(default=false).
        ExitCode : Exit code of the application(default=0)."""
        ...
    def FileExport(self,Filename:str)->bool:
        """Export a motion file.
        Command File->Motion File Export... in the menus.
        
        Filename : The file to create. To create two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2").
        return : True if the export succeeded."""
        ...
    def FileExportBatch(self,Name:str,Take:FBTake,BatchOptions:FBBatchOptions,ExportModels:FBModelList)->bool:
        """Export a motion file using batch options.
        Export used for saving files in batch process.
        
        Name : The name of the file without extension. Extension and path will be taken from batch options.
        Take : Animation take to the export.
        BatchOptions : The options for the export.
        ExportModels : Models to the export.
        return : True if the export succeeded."""
        ...
    def FileImport(self,Filename:str,MatchModels:bool=False,CreateUnmatchedModels:bool=True)->bool:
        """Import a motion file.
        Command File->Motion File Import... in the menus.
        
        Filename : The file to import. To import two files at the same time (ex: .amc & .asf), separate the two files path with a comma ("Path1,Path2").
        MatchModels : If there is already a model in the scene with the same name, the model will not be created and we replace the animation of the given model.
        CreateUnmatchedModels : Whether unmatched models will be created. This flag matters only whenMatchModels is true. whenMatchModels is false, all the models are created.
        return : True if the import succeeded."""
        ...
    def FileImportBatch(self,Name:str,BatchOptions:FBBatchOptions,Reference:FBModel)->bool:
        """Import a motion file using batch options.
        Import used for loading files in batch process.
        
        Name : The name of the file without extension. Extension and path will be taken from batch options.
        BatchOptions : The options for the import.
        Reference : Reference model for the import.
        return : True if the import succeeded."""
        ...
    def FileImportWithOptions(self,Options:FBMotionFileOptions)->bool:
        """Import a motion file with the ability to specify options.
        Command File->Motion File Import... in the menus.
        
        Options : A FBMotionFileOptions object that contains the path to the files, as well as the options to load those motion files.
        return : True if the import succeeded."""
        ...
    def FileMerge(self,Pathlist:FBStringList,ShowUIMsg:bool=False,Options:FBFbxOptions=None)->bool:
        """Merge multiple files with the current scene.
        Command File->Merge in the menus.
        
        Pathlist : Files to merge.
        ShowUIMsg : Set false if don't want to popup any UI dialog or messages (default=false).
        Options : Provide finer control on file open options (default=NULL). if not null, Option dialog will only show if both option's ShowOptionsDialog property andShowUIMsg are true. It is possible to merge multiple scenes, each one within its own user specified namespace, by calling the FBFbxOptions::SetMultiLoadNamespaceList method first. When doing so though, the FBFbxOption.NamespaceList property is then ignored.
        return : true if successful."""
        ...
    def FileNew(self,AskUser:bool=False,ClearSceneName:bool=True)->bool:
        """Command File->New in the menus.
        
        AskUser : Set to true to cause a save dialog to popup. Default is false.
        ClearSceneName : Set to true to clear the scene name, set to false to retain it. Default is true.
        return : true if successful."""
        ...
    def FileOpen(self,Buffer,BufferLength:int,arg4:FBFbxOptions)->bool:
        """Open a file from memory.
        
        p0 : the memory buffer for the file. Raw memory address is expected in pyfbsdk.
        BufferLength : the memory buffer size.
        return : true if file opened successfully."""
        ...
    def FileRender(self,RenderOptions:FBVideoGrabOptions=None)->bool:
        """Render current scene to media file.
        Command File->Render in the menus.
        
        RenderOptions : The options used when rendering the scene. If you don't specify them, current one are used.
        return : True if the file was rendered successfully otherwise False and FBVideoGrabber.GetLastErrorMsg() contains the description of the error."""
        ...
    def FileSave(self,Filename:str=None,Options:FBFbxOptions=None)->bool:
        """Save the file under another name.
        Command File->SaveAs in the menus.
        
        Filename : Save file asFilename. A value of NULL will use the current file name.
        Options : Provide finer control on file save options (default=NULL)
        return : true if successful."""
        ...
    def FlushEventQueue(self):
        """Flush event queue.
        Processes all pending events for the calling thread until there are no more events to process. You can call this function occasionally when your code is busy performing a long operation (e.g. copying a file)."""
        ...
    def GetMaxFrameCount(self,Buffer,BufferLength:int,FrameCount:int)->bool:
        """Get max frame count from a scene file in memory.
        
        p0 : the memory buffer for the file. Raw memory address is expected in pyfbsdk.
        BufferLength : the memory buffer size.
        FrameCount : out parameter to hold max frame count. this parameter is not needed in pyfbsdk.
        TimeScale : Time scale.
        return : true if file opened successfully. In pyfbsdk, a tuple (bool, kLong) will return instead, the first one is ORSDK function return value, the second is for max frame count."""
        ...
    def GetSceneAuthor(self)->str:
        """Return the scene author from the scene properties."""
        ...
    def GetSceneComment(self)->str:
        """Return the scene comment from the scene properties."""
        ...
    def GetSceneKeywords(self)->str:
        """Return the scene keywords from the scene properties."""
        ...
    def GetSceneRevisionNumber(self)->str:
        """Return the scene revision number from the scene properties."""
        ...
    def GetSceneSubject(self)->str:
        """Return the scene subject from the scene properties."""
        ...
    def GetSceneTitle(self)->str:
        """Return the scene title from the scene properties."""
        ...
    def IsSceneModified(self)->bool:
        """Is the scene modified since last save / new scene creation?
        
        return : True if the scene is modified since last save / new scene creation, false otherwise."""
        ...
    def IsValidBatchFile(self,Filename:str)->bool:
        """Verify motion file readability.
        
        Filename : The file to test.
        return : True if file was opened successfully (file is closed at the end)."""
        ...
    def LoadAnimationOnCharacter(self,FileName:str,Character:FBCharacter,FbxOptions:FBFbxOptions,PlotOptions:FBPlotOptions)->bool:
        """Load a rig and its animation from a file.
        
        FileName : File name.
        Character : Target character.
        FbxOptions : The options for the character rig and animation load
        PlotOptions : If the animation should be plotted on the target rig, these plot options will be used. Set to NULL if animation will not be plotted.
        return : true if successful."""
        ...
    def Maximize(self)->bool:
        """Maximize window (minimized).
        
        return : Operation was successful (true or false)."""
        ...
    def Minimize(self,Blocking:bool=True)->bool:
        """Minimize window.
        
        Blocking : Is the minimization blocking operation (default = true).
        return : Operation was successful (true or false)."""
        ...
    def OneClickAddToCurrentScene(self)->bool:
        """Send the scene and add it to the current scene in the specified application.
        
        return : True if transfer successful."""
        ...
    def OneClickIsConnectedTo(self)->FBOneClickApplication:
        """Return the other application that MotionBuilder is connected to.
        
        return : The application that MotionBuilder is connected to."""
        ...
    def OneClickSelectPreviouslySentObject(self):
        """Select, in MotionBuilder, the object that were sent."""
        ...
    def OneClickSendAsNewScene(self,Application:FBOneClickApplication)->bool:
        """Send the current scene as a new scene in the specified application.
        
        Application : The application that will receive the scene.
        return : True if transfer successful."""
        ...
    def OneClickUpdateCurrentScene(self)->bool:
        """Send the scene to update the current scene in the specified application.
        
        return : True if transfer successful."""
        ...
    def SaveCharacterRigAndAnimation(self,FileName:str,Character:FBCharacter,FbxOptions:FBFbxOptions)->bool:
        """Save the rig and its animation in a file.
        
        FileName : File name.
        Character : Character to save.
        FbxOptions : The options for the character rig and animation export"""
        ...
    def SetSceneAuthor(self,Author:str):
        """Set the scene author.
        
        Author : The author to set in the scene properties."""
        ...
    def SetSceneComment(self,Comment:str):
        """Set the scene comment.
        
        Comment : The comment to set in the scene properties."""
        ...
    def SetSceneKeywords(self,Keywords:str):
        """Set the scene keywords.
        
        Keywords : The keywords to set in the scene properties."""
        ...
    def SetSceneRevisionNumber(self,RevNumber:str):
        """Set the scene revision number.
        
        RevNumber : The revision number to set in the scene properties."""
        ...
    def SetSceneSubject(self,Subject:str):
        """Set the scene subject.
        
        Subject : The subject to set in the scene properties."""
        ...
    def SetSceneTitle(self,Title:str):
        """Set the scene title.
        
        Title : The title to set in the scene properties."""
        ...
    def UpdateAllWidgets(self):
        """Request to refresh display of all UI widgets."""
        ...
class FBAssetFile(FBAssetItem):
    """Class representing a file stored in a version control database."""
    def GetCheckedOutBy(self)->str:
        """Returns the name of the user who currently has this file checked out.
        
        return : The user name if the file is checked out, or an empty string if it is not."""
        ...
    def IsCheckedOut(self)->bool:
        """Returns a boolean value indicating if this file is checked out by any user.
        
        return : A boolean value indicating if this node is checked out."""
        ...
    def IsCheckedOutByMe(self)->bool:
        """Returns a boolean value indicating if this file is checked out by the current user.
        
        return : A boolean value indicating if this node is checked out by the current user."""
        ...
class FBAssetFolder(FBAssetItem):
    """Class representing a folder stored in a version control database."""
    def AddFile(self,LocalPath:str,Comment:str="",CheckOut:bool=False,Silent:bool=False)->FBAssetFile:
        """Add a specified file into the database.
        It will be added in this folder.
        
        LocalPath : The full path to the file on the local disk.
        Comment : Comment to be applied for the operation.
        CheckOut : Whether the file should be checked out or not.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : An FBAssetfile* object representing the newly added file."""
        ...
    def AddFolder(self,Name:str,Comment:str="",Silent:bool=False)->FBAssetFolder:
        """Add a folder in the database.
        It will be added in this folder.
        
        Name : Name of the folder to be created.
        Comment : Comment to be applied for the operation.
        Silent : IfSilent is set to true, no dialog will be displayed by this method.
        return : An FBAssetFolder* object representing the newly added folder."""
        ...
    def GetChild(self,Index:int)->FBAssetItem:
        """Get the child at indexIndex.
        
        Index : int
        return : The child atIndex, or NULL if the index was out of range."""
        ...
    def GetChildCount(self)->int:
        """Get the number of items in this folder.
        
        return : The number of items in this folder."""
        ...
    def GetFile(self,Name:str)->FBAssetFile:
        """Get a file present in this folder by using it's name.
        
        Name : str
        return : The file with the given name, or NULL if it was not found."""
        ...
    def GetFolder(self,Name:str)->FBAssetFolder:
        """Get a folder present in this folder by using it's name.
        
        Name : str
        return : The folder with the given name, or NULL if it was not found."""
        ...
class FBAnimationNode(FBComponent):
    """See samples: CopyAnimation.py, ClearKeysOnSelectedModels.py, TraversingRelationConstraint.py, FCurveEditor.py."""
    ConnectorType:property
    """Read Only Property: Animation node connector type."""
    DefaultInterpolation:property
    """Read Write Property: Default type of interpolation."""
    FCurve:property
    """Read Write Property: FCurve for animation. See sample: StartKeysAtCurrentTime.py."""
    KeyCount:property
    """Read Only Property: Number of keys."""
    Label:property
    """Read Write Property: Label (UI Name)."""
    Live:property
    """Read Write Property: Is animation live?"""
    Nodes:property
    """List: List of animation nodes."""
    RecordMode:property
    """Read Write Property: Is the node in recording mode (device connectors)?"""
    UserName:property
    """Read Only Property: Name of animation node."""
    def ConvertGlobalToNodeTime(self,KeyTime:FBTime)->FBTime:
        """Convert global time to node time.
        (NOTE: Only used in the context of a story clip)
        
        KeyTime : Time of the key to convert."""
        ...
    def ConvertNodeToGlobalTime(self,KeyTime:FBTime)->FBTime:
        """Convert node time to global time.
        (NOTE: Only used in the context of a story clip)
        
        KeyTime : Time of the key to convert."""
        ...
    def GetAnimationToPlay(self)->object:
        """Get animation node to play from.
        
        return : Animation node to be played."""
        ...
    def GetAnimationToRecord(self)->object:
        """Get animation node to record to.
        
        return : Animation node to record to."""
        ...
    def GetDataDoubleArrayCount(self)->int:
        """If the DataPtr is of numeric value type ...
        get the size of the array ex: Light Intensity:1, Translation 3
        
        return : Size of DataPtr array."""
        ...
    def GetSizeOfData(self)->int:
        """Get sizeof void Data Ptr."""
        ...
    def IsKey(self)->bool:
        """Verifies if there is a key at the current.
        
        return : true if there is a key at the current time."""
        ...
    def KeyAdd(self,Data:FBTime,Interpolation:object,TangentMode:FBInterpolation,arg5:FBTangentMode):
        """Add a key to the animation node at current time.
        
        Data : Value of data to add.
        Interpolation : Interpolation type of the inserted key, default value is Cubic interpolation.
        TangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth)."""
        ...
    def KeyCandidate(self,Time:FBTime):
        """Keys the current candidate values if no time is specified, at current time.
        
        Time : Time at which to insert the key."""
        ...
    def KeyRemove(self):
        """Remove key at current time."""
        ...
    def KeyRemoveAt(self,Time:FBTime):
        """Remove key at the specified time.
        
        Time : Time for the key"""
        ...
    def ReadData(self,Data:FBEvaluateInfo,arg3:object)->list:
        """Read the last data evaluated for this animation node ...
        this call doesn't generate a pull on the connection attached to this AnimationNode. No validation is done on the pointer size. You must provide a buffer that is at least GetSizerOfData() size.
        
        Data : Data to read from animation node.
        return : true if successful."""
        ...
    def ReadLastEvalData(self)->list:...
    def SetBufferType(self,Global:object):
        """Set buffer type for ANIMATIONNODE_TYPE_LOCAL_TRANSLATION, ANIMATIONNODE_TYPE_LOCAL_ROTATION and ANIMATIONNODE_TYPE_LOCAL_SCALE.
        
        Global : Is buffer local or global."""
        ...
    def SetCandidate(self,Data:list,CheckLocked:object)->bool:
        """Set the current candidate values for current time.
        
        Data : float
        CheckLocked : Decides whether to check the locked status.
        return : true if successful."""
        ...
    def WriteData(self,Data:list,EvaluateInfo:FBEvaluateInfo)->int:
        """Write data to animation node.
        
        Data : Data to write to animation node.
        EvaluateInfo : Node evaluation information (access to system and local time).
        return : true if successful."""
        ...
class FBAnimationLayer(FBComponent):
    """Used to access animation layer properties and modify them.
    Changing the various properties of the layers will modify how the animation will be interpreted. For example, muting a layer will mute all the animation contained on the layer. You can access the animation layer object from the take, usign the FBTake::GetLayer() and FBTake::GetLayerByName(). See the FBTake class for more details. See samples: AnimationLayers.py, MergeAnimationLayers.py."""
    LayerMode:FBLayerMode
    """Read Write Property: Layer mode. By default, the layer is in kFBLayerModeAdditive mode. Cannot be applied to the BaseAnimation Layer."""
    LayerRotationMode:FBLayerRotationMode
    """Read Only Property: Layer rotation mode. Cannot be applied to the BaseAnimation Layer."""
    Lock:bool
    """Read Write Property: If true, the layer is locked. You cannot modify keyframes on a locked layer."""
    Mute:bool
    """Read Write Property: If true, the layer is muted. A muted layer is not included in the result animation. Cannot be applied to the BaseAnimation Layer."""
    Solo:bool
    """Read Write Property: If true, the layer is soloed. When you solo a layer, you mute other layers that are at the same level in the hierarchy, as well as the children of those layers. Cannot be applied to the BaseAnimation Layer."""
    Weight:float
    """Read Write Property: The weight value of a layer determines how much it is present in the result animation. Takes a value from 0 (the layer is not present) to 100. The weighting of a parent layer is factored into the weighting of its child layers, if any. BaseAnimation Layer always has a Weight of 100."""
    def AddChildLayer(self,AnimationLayer:FBAnimationLayer):
        """Add a child to the layer.
        Layer ID of the new child layer might change after parenting depending where the child layer was originally located.
        
        AnimationLayer : Layer to set as a child."""
        ...
    def GetChildCount(self)->int:
        """Get the child layer count of this layer.
        The count will only includes direct child of the layer.
        
        return : Child layer count, or -1 if unsuccessful"""
        ...
    def GetChildLayer(self,Index:int)->FBAnimationLayer:
        """Get the nth child layer of this layer.
        
        Index : Index of the child layer to get.
        return : Child animation layer located atIndex"""
        ...
    def GetCompleteChildHierarchy(self,ChildArray:List[FBAnimationLayer])->list:
        """Get the all the children hierarchy of the layer, including children not directly connected to this layer.
        
        ChildArray : Array of child layers, will be filled by the function."""
        ...
    def GetLayerIndex(self)->int:
        """Get the layer index.
        
        return : The layer index in the current layer hierarchy. This value will change if the hierarchy is modified. Return -1 if unsuccessful."""
        ...
    def GetParentLayer(self)->FBAnimationLayer:
        """Get the parent layer.
        
        return : A pointer to the parent layer or NULL if the layer doesn't have a parent."""
        ...
    def IsSelected(self)->bool:
        """Verify if the layer is selected.
        
        return : True if the layer is selected, false otherwise."""
        ...
    def SelectLayer(self,Value:bool,ExclusiveSelect:bool):
        """Select the layer.
        This is the equivalent of selecting the layer in the UI in the Animation Layer Editor tool
        
        Value : True if the layer will be selected, false otherwise.
        ExclusiveSelect : IfValue is true, passing true will deselect all the other layers, creating an exclusive selection, it will also set the layer as the current layer."""
        ...
    def SetParentLayer(self,ParentLayer:FBAnimationLayer):
        """Set the parent layer.
        
        ParentLayer : A pointer to the parent layer or NULL if you want to unparent the layer."""
        ...
class FBActorFace(FBComponent):
    """Used to plot actor face animation.
    These classes are under development and may change dramatically between versions."""
    def PlotAnimation(self)->bool:
        """Plot the animation of the actor face.
        
        return : True if the operation completed successfully."""
        ...
class FBActionManager(FBComponent):
    """Action Manager class.
    This class is introduced to enable users to access to the actions related functions. between versions."""
    CurrentInteractionMode:str
class FBConstraintManager(FBComponent):
    """Constraint manager.
    See sample: FBConstraintManager.py."""
    def TypeCreateConstraint(self,TypeIndex:int)->FBConstraint:
        """Create a constraint by name.
        Given the constraint type name in the registry, this function create an instance of this constraint. The newly created constraint will be automatically added to the scene.
        
        Name : the name of the constraint to be created.
        return : The newly created constraint, or NULL ifName doesn't match any registered constraints."""
        ...
    def TypeGetCount(self)->int:
        """Get the number of registered constraint types.
        
        return : Number of registered constraint types."""
        ...
    def TypeGetName(self,TypeIndex:int)->str:
        """Get the name of a registered type of constraint.
        This will search in the registry for a constraint at the indexTypeIndex.
        
        TypeIndex : Index of a constraint type.
        return : Name of constraint type."""
        ...
class FBConstructionHistory(FBComponent):
    """Access to global construction history functionality."""
    OnChange:FBEvent
    """Event: History changed."""
    def GetDeltaOperations(self,Operations,sinceCommandId:int=-1):
        """GetDeltaOperations Get the list of delta operations in the construction history.
        
        Operations : Array of operations, will be filled by the function.
        sinceCommandId : int"""
        ...
    def GetScriptOutput(self,script:str,errors:str):
        """GetScriptOutput Returns the output from the scripting engine.
        
        script : the script text
        errors : the error outputted from the scripting engine"""
        ...
    def GetState(self)->FBConstructionHistoryState:
        """GetState returns the current state of the construction history manager.
        
        return : returns a FBConstructionHistoryState indicating the state"""
        ...
    def NetDelete(self,component:FBComponent,key:int):
        """NetDelete Network delete with support for Network Undo.
        
        component : FBComponent
        key : A key that uniquely identifies the operation"""
        ...
    def NetUndo(self,key:int):
        """NetUndo Perform network undo operation.
        
        key : The operation to undo"""
        ...
    def RunOperation(self,operation:FBConstructionOperation,out_errors:str)->int:
        """RunOperation Runs an operation.
        
        operation : The operation to run
        out_errors : A string containing the text of errors generated by running the operations (if any)"""
        ...
class FBControlSet(FBComponent):
    """Control set class.
    These classes are under development and may change dramatically between versions."""
    ControlSetType:FBControlSetType
    """Read Property: the control Set Type (FKIK or IK)."""
    UseAxis:bool
    """Read Write Property: is using axis."""
    def GetFKIndex(self,Model:FBModel)->int:
        """Return The Index of the Given Model.
        
        Model : Given Model to obtain Index
        return : The Index of the Given Model."""
        ...
    def GetFKModel(self,Index:int)->FBModel:
        """Return the object associated to the given Index.
        
        Index : Given Index to obtain Model
        return : return the model at the specified Index."""
        ...
    def GetFKName(self,Index:int)->str:
        """return the name of FK Effector at the given index
        
        Index : Given Index
        return : return the name of IK Effector Slot"""
        ...
    def GetIKEffectorIndex(self,Model:FBModel)->int:
        """Return the Index of the Given Model.
        
        Model : Given Model to Obtain Index
        return : The Index of the Given Model."""
        ...
    def GetIKEffectorModel(self,EffectorIndex:FBEffectorId,PivotIndex:int=0)->FBModel:
        """Return the object associated to the given Index.
        
        EffectorIndex : Given Index to obtain Model
        PivotIndex : Index of effector pivot
        return : return the model at the specified Index."""
        ...
    def GetIKEffectorName(self,EffectorIndex:FBEffectorId)->str:
        """return the name of IK Effector
        
        EffectorIndex : Given Index to obtain Name
        return : the name of IK Effector"""
        ...
    def GetIKEffectorPivotCount(self,EffectorIndex:FBEffectorId)->int:
        """return the number of IK Effector Slot
        
        EffectorIndex : FBEffectorId
        return : return the number of IK Effector Slot"""
        ...
    def GetReferenceModel(self)->FBModel:
        """Get the reference model associated with this Control Set.
        
        return : The reference model associated with the Control Set."""
        ...
    def GetReferenceName(self)->str:
        """Get the reference name associated with this Control Set.
        
        return : The reference name associated with the Control Set."""
        ...
class FBCycleCreator(FBComponent):
    """See sample: CycleCreator.py."""
    def CreateCycle(self,StartTime:FBTime,EndTime:FBTime,Char:FBCharacter,MoveStartToZero:object,AddZeroKey:object,NewTakeName:str,ReferencedIK:FBModel,PasteTx:object,PasteTy:object,PasteTz:object,PasteR:object,PasteG:object)->bool:
        """Create animation cycle for current character ifChar is NULL, else for the character assigned byChar; during the time scope betweenStartTime andEndTime.
        
        StartTime : Start time of the cycle
        EndTime : End time of the cycle
        Char : Target character, if it is NULL, try to use current character
        MoveStartToZero : Whether move start time to zero time
        AddZeroKey : Whether add zero key
        NewTakeName : The name used to create the new take.
        ReferencedIK : The IK that used as referenced object in pose pasting.
        PasteTx : Whether consider Translation X on referenced IK when doing pose pasting
        PasteTy : Whether consider Translation Y on referenced IK when doing pose pasting
        PasteTz : Whether consider Translation Z on referenced IK when doing pose pasting
        PasteR : Whether consider Rotation on referenced IK when doing pose pasting
        PasteG : Whether respect Gravity when doing pose pasting (Translation = Global XZ / Rotation = Global Y). Note: if G is true then Ty will be forced changed to false.
        return : true if successful."""
        ...
class FBDeck(FBComponent):
    """Interface to a tape deck."""
    CassetteInside:bool
    """Read Only Property: Is the cassette inside?"""
    EE:bool
    """Read Write Property: Is EE on?"""
    IconFilename:str
    """Read Write Property: Filename of icon for deck."""
    Latency:FBTime
    """Read Write Property: Latency of response for the deck;"""
    Offset:FBTime
    """Read Write Property: Current offset for the TC."""
    Online:bool
    """Read Write Property: Is deck online?"""
    PlayingBackward:bool
    """Read Only Property: Playing backwards?"""
    PlayingForward:bool
    """Read Only Property: Playing forward?"""
    PostRoll:FBTime
    """Read Write Property: Post-Roll."""
    PreRoll:FBTime
    """Read Write Property: Pre-Roll."""
    StandBy:bool
    """Read Write Property: In standby mode?"""
    TransportControl:FBDeckTransportMode
    """Read Write Property: Mode w/r to TC (None, Sync, Main );"""
    UniqueName:str
    """internal Unique name."""
    def CueAt(self,Time:FBTime):
        """Cue deck at a given time.
        
        Time : Time to cue deck at."""
        ...
    def DeckAutoCommandsNotify(self):
        """Deck auto commands notification."""
        ...
    def DeckStatusUpdateNotify(self):
        """Interface to IObject.
        Deck status update notification."""
        ...
    def Eject(self):
        """Eject tape."""
        ...
    def Forward(self):
        """Fast forward."""
        ...
    def GetTime(self)->FBTime:
        """Get the deck's time.
        
        return : Time of deck."""
        ...
    def Play(self,Speed:float=1.0):
        """Play forwards.
        
        Speed : Playback speed (default is 1.0)."""
        ...
    def ReversePlay(self,Speed:float=1.0):
        """Play backwards.
        
        Speed : Playback speed(default is 1.0)."""
        ...
    def Rewind(self):
        """Rewind."""
        ...
    def StepBack(self):
        """Step backwards."""
        ...
    def StepForward(self):
        """Step forwards."""
        ...
    def Stop(self):
        """Stop."""
        ...
    def ThreadSync(self):...
class FBDeformer(FBComponent):
    """Base Model deformer class."""
    DeformerType:FBDeformerType
    """Read Only Property: Deformer Type."""
class FBDeviceInstrument(FBComponent):
    """Instrument abstraction layer."""
    Active:bool
    """Read Write Property: Is instrument active?"""
    Device:FBDevice
    """Read Write Property: Handle to owner device."""
    ModelTemplate:FBModelTemplate
    """Read Write Property: Model template to build instruments' structure."""
    def InstrumentRecordFrame(self,RecordTime:FBTime,NotifyInfo:FBDeviceNotifyInfo):
        """Record the data to the function curves for the instrument.
        
        RecordTime : Time to record data at.
        NotifyInfo : Device notification information structure."""
        ...
    def InstrumentWriteData(self,EvaluateInfo:FBEvaluateInfo)->bool:
        """Write data to instrument's connectors.
        In the evaluation engine callback, this will take the data in the instrument's temporary data holders and write it to the connectors.
        
        EvaluateInfo : Evaluation information structure.
        return : true if successful."""
        ...
class FBDeformerPointCache(FBDeformer):
    """Base Model deformer class."""
    Active:bool
    """Read Write Property: Active."""
    ChannelCount:int
    """Read Only Property: Channel Count."""
    ChannelEnd:FBTime
    """Read Only Property: Channel End."""
    ChannelFrameRate:float
    """Read Only Property: Channel FrameRate."""
    ChannelIndex:int
    """Read Write Property: Channel Index."""
    ChannelName:str
    """Read Only Property: Channel Name."""
    ChannelPointCount:int
    """Read Only Property: Channel Point Count."""
    ChannelSampleRegular:bool
    """Read Only Property: Channel Sample Regular."""
    ChannelStart:FBTime
    """Read Only Property: Channel Start."""
    PointCacheFile:FBPointCacheFile
    """Read Write Property: Point Cache File Object."""
class FBDeviceOpticalMarker(FBComponent):
    """Device optical marker.
    A device optical marker represents the input locations for interfacing optical hardware. This type of marker corresponds uniquely to the input (from the hardware) and will be represented on-screen by a FBModelMarkerOptical."""
    IsUsed:bool
    """Property: Is marker used?"""
    Model:FBModel
    """Property: Model marker access."""
    Occlusion:float
    """Property: Occulsion data for marker."""
    Translation:property
    def SetData(self,X:float,Y:float,Z:float=0.0,Occlusion:float=0.0):
        """Set data for optical marker.
        
        X : X position for marker.
        Y : Y position for marker.
        Z : Z position for marker(default=0.0).
        Occlusion : Occulsion information for marker(default=0.0)."""
        ...
class FBEvaluateManager(FBComponent):
    DeviceCount:int
    """Read only Property: Number of devices to evaluate."""
    DualQuaternionSkinning:bool
    """Read/Write Property: Using state of the Dual Quaternion for skinning (CPU Skinning or GPU Skinning)."""
    FrameSkipOptimization:bool
    """Read/Write Property: if true, apply frame skip optimization during playback. off-line rendering don't use frame skip optimization."""
    NodeCount:int
    """Read only Property: Number of nodes to evaluate."""
    OnRenderingPipelineEvent:FBEvent
    """For callback events at rendering pipeline."""
    OnSynchronizationEvent:FBEvent
    """For callback events at synchronization point."""
    ParallelDeformation:bool
    """Read/Write Property: true if deformation is evaluated in parallel."""
    ParallelEvaluation:bool
    """Read/Write Property: true if parallel DAG schedule algorithm is being used. false when serial algorithm is being used."""
    ParallelPipeline:bool
    """Read/Write Property: true if transformation is evaluated in parallel."""
    ParallelScheduleType:FBParallelScheduleType
    """DEPRICATED Read/Write Property: choose between serial and parallel DAG schedule algorithm. kFBParallelScheduleSimple and kFBParallelScheduleAdvanced will set ParallelEvalution to true. kFBParallelScheduleSerial will set ParallelEvalution to false"""
    UseGPUDeformation:bool
    """Read/Write Property: true if GPU deformation is used."""
    def InvalidateDAG(self):
        """Invalidate the DAG and trigger parallel scheduling at the next frame."""
        ...
    def IsInteractiveMode(self)->bool:
        """Check if the application main loop is in interactive or offline render mode.
        
        return : true if is application is is interactive mode."""
        ...
class FBFCurveEditorUtility(FBComponent):
    """FBFCurveEditor Utility class Utility class allowing different operations on a FBFCurveEditor or on the main FCurveEditor."""
    def Frame(self,SelectedKeysOnly:bool,Editor:FBFCurveEditor=None)->bool:
        """Frame keys in the FCurve Editor interface.
        
        SelectedKeysOnly : If true, only the selected keys will be framed, otherwise all keys will be framed.
        Editor : Pointer to a FBFCurveEditor for framing the keys in that custom editor, NULL to frame in the default editor.
        return : True if successful, false otherwise."""
        ...
    def GetObjects(self,ObjectList:List[FBComponent])->bool:
        """Get all the objects displayed in the left pane of the FCurve Editor.
        
        ObjectList : A list that will be filled with the objects displayed in the FCurve Editor.
        return : True if successful, false otherwise."""
        ...
    def GetProperties(self,Properties:List[FBProperty],SelectedOnly:bool,Editor:FBFCurveEditor=None)->bool:
        """Get the displayed properties.
        
        Properties : Array that will contain the properties displayed.
        SelectedOnly : If true, only the selected properties will be returned.
        Editor : Pointer to a FBFCurveEditor for getting the properties in that custom editor, NULL to frame in the default editor.
        return : True if successful, false otherwise."""
        ...
    def GetTimeSpan(self,Editor:FBFCurveEditor=None)->FBTimeSpan:
        """Get the displayed time range of the FCurve Editor.
        
        Editor : Pointer to a FBFCurveEditor where the time span will be get, NULL to get the time span from the default editor.
        return : FCurve Editor time span, default FBTimeSpan if not successful."""
        ...
    def SetTimeSpan(self,TimeSpan:FBTimeSpan,Editor:FBFCurveEditor=None)->bool:
        """Set the displayed time range of the FCurve Editor.
        
        TimeSpan : The time span that will be set.
        Editor : Pointer to a FBFCurveEditor where the time span will be set, NULL to set the time span on the default editor.
        return : True if successful, false otherwise."""
        ...
class FBFCurveEventManager(FBComponent):
    """FCurve Event Manager Interface to the FBFCurveEventManager.
    This class is used to track the changes on a FCurve of a property."""
    OnFCurveEvent:property
    """Event: Called when a registered FCurve is modified."""
    OnPropertyEvent:property
    """Event: Called when a registered property state is modified (detached, destroyed...)."""
    def RegisterProperty(self,Property:FBPropertyAnimatable)->bool:
        """Register a property to the FCurve Event Manager.
        Properties that are registered will receive events with the OnFCurveEvent/OnPropertyEvent properties when their FCurves are modified.
        
        Property : The property to track.
        return : True if the registration was successful, False otherwise."""
        ...
    def UnregisterProperty(self,Property:FBPropertyAnimatable)->bool:
        """Unregister a property from the FCurve Event Manager.
        Those properties will not be tracked and no update will be sent with the OnFCurveEvent/OnPropertyEvent properties anymore.
        
        Property : The property to stop tracking.
        return : True if the unregistration was successful, False otherwise."""
        ...
class FBFbxOptions(FBComponent):
    """Customize file loading and saving.
    See samples: FBFbxOptions.py, ImportWithNamespace.py, BatchExportCharacterAnimationTool.py."""
    ActorFaces:FBElementAction
    """Read Write Property: Handling of the Actor Faces elements."""
    ActorFacesAnimation:bool
    """Read Write Property: Handling of the Actor Faces animation."""
    Actors:FBElementAction
    """Read Write Property: Handling of the Actors elements."""
    Audio:FBElementAction
    """Read Write Property: Handling of the Audio elements."""
    BaseCameras:bool
    """Read Write Property: Consider base camera settings."""
    Bones:FBElementAction
    """Read Write Property: Handling of the Bones elements."""
    BonesAnimation:bool
    """Read Write Property: Handling of the Bones animation."""
    CacheSize:int
    """Read Write Property: The Cached buffer size used to accelerate IO system."""
    CameraSwitcherSettings:bool
    """Read Write Property: Consider camera switcher settings."""
    Cameras:FBElementAction
    """Read Write Property: Handling of the Cameras elements."""
    CamerasAnimation:bool
    """Read Write Property: Handling of the Cameras animation."""
    CharacterExtensions:FBElementAction
    """Read Write Property: Handling of the Character Extensions."""
    CharacterFaces:FBElementAction
    """Read Write Property: Handling of the Character Faces elements."""
    CharacterFacesAnimation:bool
    """Read Write Property: Handling of the Character Faces animation."""
    Characters:FBElementAction
    """Read Write Property: Handling of the Characters elements."""
    CharactersAnimation:bool
    """Read Write Property: Handling of the Characters animation."""
    ClearSelectionBeforeSave:bool
    """Read Write Property: Set to true if the current selected objects shouldn't saved when call FBApplication::SaveCharacterRigAndAnimation."""
    ConsiderMuteSolo:bool
    """Read Write property: Consider the mute/solo settings to identify identical layer when merging."""
    Constraints:FBElementAction
    """Read Write Property: Handling of the Constraints elements."""
    ConstraintsAnimation:bool
    """Read Write Property: Handling of the Constraints animation."""
    CopyCharacterExtensions:bool
    """Read Write Property:CopyMissingExtensions Set to true if the character extensions on the rig in the file should be copied to the target rig."""
    CurrentCameraSettings:bool
    """Read Write Property: Consider current camera settings."""
    Devices:FBElementAction
    """Read Write Property: Handling of the Devices elements."""
    DevicesAnimation:bool
    """Read Write Property: Handling of the Devices animation."""
    EmbedMedia:bool
    """Read Write Property: Embed all media in the FBX file itself. When saving in ASCII mode it is not possible to embed media."""
    FileFormatAndVersion:FBFileFormatAndVersion
    """Read Write Property: File format and version chosen to save the scene."""
    FileReference:bool
    """Read Write property: Load/Save scene as FileReference."""
    FileReferenceEdit:bool
    """Read Write Property: Load/Save the edits made to referenced objects or not."""
    FileReferences:FBElementAction
    """Read Write Property: Handling of the FileReferences elements."""
    GlobalLightingSettings:bool
    """Read Write Property: Consider global Lighting settings."""
    Groups:FBElementAction
    """Read Write Property: Handling of the Groups elements."""
    IgnoreConflicts:bool
    """Read Write Property: Set to true to ignore conflicts between objects in character extensions and objects in the scene. Conflicting objects will be merged in the extension"""
    KeepTransformHierarchy:bool
    """Read Write Property: Indicate whether we keep transform hierarchy when SaveSelectedModelsOnly is true. Default value is false to ensure consistent behavior with SaveSelected operation via file menu."""
    KeyingGroups:FBElementAction
    """Read Write Property: Handling of the Keying Groups elements."""
    Lights:FBElementAction
    """Read Write Property: Handling of the Lights elements."""
    LightsAnimation:bool
    """Read Write Property: Handling of the Lights animation."""
    Materials:FBElementAction
    """Read Write Property: Handling of the Materials elements."""
    MaterialsAnimation:bool
    """Read Write Property: Handling of the Materials animation."""
    Models:FBElementAction
    """Read Write Property: Handling of the Models elements."""
    ModelsAnimation:bool
    """Read Write Property: Handling of the Models animation."""
    NamespaceList:str
    """Read Write Property: A list of namespaces separated by '~'. On Load, duplicate the loaded objects into each namespace in the list. If the SetMultiLoadNamespaceList method is also called, this property is ignored."""
    Notes:FBElementAction
    """Read Write Property: Handling of the Notes elements."""
    NotesAnimation:bool
    """Read Write Property: Handling of the Notes animation."""
    OpticalData:FBElementAction
    """Read Write Property: Handling of the Optical Data elements."""
    PhysicalProperties:FBElementAction
    """Read Write Property: Handling of the Physical Properties elements."""
    PhysicalPropertiesAnimation:bool
    """Read Write Property: Handling of the Physical Properties animation."""
    Poses:FBElementAction
    """Read Write Property: Handling of the Poses elements."""
    ProcessAnimationOnExtension:bool
    """Read Write Property: Set to true if animation on character extensions should also be transferred."""
    RemoveConstraintReference:bool
    """Read Write Property: Set to true if we should remove constraint reference."""
    RemoveEmptyLayer:bool
    """Read Write property: Remove empty animation layers that are in additive mode, without child or parent."""
    ReplaceControlSet:bool
    """Read Write Property: Set to true if the character extensions (and their children) should be saved when call FBApplication::SaveCharacterRigAndAnimation."""
    ResetDOF:bool
    """Read Write Property: Set to true if we should change the limits on the target rig."""
    ResetHierarchy:bool
    """Read Write Property: Set to true if we should reset the character hierarchy."""
    RetargetOnBaseLayer:bool
    """Read Write Property: If the transfer method is retarget, set this parameter to control where the retarget correction will be made (on base layer or on another layer)."""
    SaveCharacter:bool
    """Read Write Property: Set to true if the character should be saved when call FBApplication::SaveCharacterRigAndAnimation."""
    SaveCharacterExtensions:bool
    """Read Write Property: Set to true if the character extensions (and their children) should be saved when call FBApplication::SaveCharacterRigAndAnimation."""
    SaveControlSet:bool
    """Read Write Property: Set to true if the rig (and its children) should be saved when call FBApplication::SaveCharacterRigAndAnimation."""
    SaveSelectedModelsOnly:bool
    """Read Write Property: Indicate that only the selected models will be saved."""
    Scripts:FBElementAction
    """Read Write Property: Handling of the Scripts elements."""
    SetPropertyStaticIfPossible:bool
    """Read Write Property: Set to false if want to keep properties' animated flag even when they are not really animated(no keyframe data) while retrieving/storing. See sample: SetPropertyStaticIfPossibleOption.py."""
    Sets:FBElementAction
    """Read Write Property: Handling of the Sets elements."""
    Shaders:FBElementAction
    """Read Write Property: Handling of the Shaders elements."""
    ShadersAnimation:bool
    """Read Write Property: Handling of the Shaders animation."""
    ShowFileDialog:bool
    """Read Write Property: Set to true if want to pop up dialog for FileName, Format, Embed, Compression, UseTakeName, OneTakePerFile."""
    ShowOptionsDialog:bool
    """Read Write Property: Set to true if want to pop up options dialog for detail settings."""
    Solvers:FBElementAction
    """Read Write Property: Handling of the Solvers elements."""
    SolversAnimation:bool
    """Read Write Property: Handling of the Solvers animation."""
    Story:FBElementAction
    """Read Write Property: Handling of the Story elements."""
    StoryAnimation:bool
    """Read Write Property: Handling of the Story animation (animatable properties on story objects)."""
    TakeSpan:FBTakeSpanOnLoad
    """Read Write Property: Indicate how the take start and end point should be set. By default it is read from the file."""
    Textures:FBElementAction
    """Read Write Property: Handling of the Textures elements."""
    TexturesAnimation:bool
    """Read Write Property: Handling of the Textures animation."""
    TransferMethod:FBCharacterLoadAnimationMethod
    """Read Write Property: How should the animation should be transfered on the target rig."""
    TransportSettings:bool
    """Read Write Property: Consider transport control settings."""
    UpdateRecentFiles:bool
    """Read Write Property: Set to true to update recent file list."""
    UseASCIIFormat:bool
    """Read Write Property: Indicate if the resulting FBX file will be in binary or ASCII mode."""
    Video:FBElementAction
    """Read Write Property: Handling of the Video elements."""
    def GetMultiLoadNamespaceList(self)->FBStringList:
        """Returns the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge).
        This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored.
        
        return : The multi load namespace list currently set."""
        ...
    def GetTakeCount(self)->int:
        """Return the count of takes in the scene to saved or the file to loaded."""
        ...
    def GetTakeDescription(self,TakeIndex:int)->str:
        """Take Description.
        
        TakeIndex : index of take to get."""
        ...
    def GetTakeDestinationName(self,TakeIndex:int)->str:
        """Take Destination Name upon save or load.
        
        TakeIndex : index of take to get."""
        ...
    def GetTakeKeyRange(self,TakeIndex:int)->FBTimeSpan:
        """Get take key range.
        
        TakeIndex : index of take to get.
        return : A time range, keys inside that time range will be kept. Keys outside that time range will be removed when importing the animation, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity"""
        ...
    def GetTakeName(self,TakeIndex:int)->str:
        """Take Original Name.
        
        TakeIndex : index of take to get."""
        ...
    def GetTakeSelect(self,TakeIndex:int)->bool:
        """Return if true if the take will be saved or Loaded.
        
        TakeIndex : index of take to get."""
        ...
    def SaveToString(self)->str:
        """Serialize all options to a string Serialize all options to a string specifying a context.
        
        String : The string containing all settings, target of serializing
        context : The context to be used when serializing"""
        ...
    def SetAll(self,ElementAction:FBElementAction,Animation:bool):
        """Set All Options.
        Initialize all loading/saving properties to ElementAction and animation specified.
        
        ElementAction : Default value for all FBPropertyElementAction properties.
        Animation : Default value for all Animation properties."""
        ...
    def SetFromString(self,String:str):
        """Set all options from string Set all parameters from a formatted string (previously serialized with SaveToString)
        
        String : The string containing all settings. See SaveToFile
        context : The context to be used when de-serializing"""
        ...
    def SetMultiLoadNamespaceList(self,MultiLoadNamespaceList:FBStringList):
        """Sets the list of namespaces that will be used when merging multiple scenes (see FBApplication::FileMerge).
        The number of namespaces contained in this list must match the number of files merged, otherwise the merge operation will abort. The first namespace in the list will be applied on the first merged scene, the second namespace in the list will be applied on the second merged scene, and so one and so forth. This list is affecting only the merge operation. When merging multiple scenes, if this list of namespaces is set, the FBFbxOptions::NamespaceList property value is ignored.
        
        >>> # This example shows how to merge multiple scenes, each scene in its own user specified namespace:
        # Create an Load FBFbxOptions object
        fbxLoadOptions = FBFbxOptions( True )
        # Create a list of namespaces (2 items here, so the number of scenes to merge must also be 2)
        # and set the list in the FBFbxOptions object
        myNS = FBStringList( 'MyFirstNS~MySecondNS' )
        fbxLoadOptions.SetMultiLoadNamespaceList( myNS )
        # Create a list of scenes to merge
        myScenesToMerge = FBStringList( 'C:\\Temp\\MyFirstScene.fbx~C:\\Temp\\AnotherScene.fbx' )
        # Let's merge those scenes. The namespaces will be applied on the scenes' contents.
        print FBApplication().FileMerge( myScenesToMerge, False, fbxLoadOptions )
        
        
        MultiLoadNamespaceList : The multi load namespace list to set."""
        ...
    def SetObjectsToSave(self,ObjectsToSave:List[FBComponent]):
        """Sets the list of objects that will be saved.
        This needs to be set before calling FBApplication::FileSave. The list is affecting only one save operation. Once the save is completed, the list is cleared.
        
        ObjectsToSave : The objects to save."""
        ...
    def SetTakeDescription(self,TakeIndex:int,Description:str):
        """Take Description.
        
        TakeIndex : index of take to set.
        Description : take description to set"""
        ...
    def SetTakeDestinationName(self,TakeIndex:int,DestinationName:str):
        """Take Destination Name upon save or load.
        
        TakeIndex : index of take to set.
        DestinationName : take description to set"""
        ...
    def SetTakeKeyRange(self,TakeIndex:int,KeyTimeSpan:FBTimeSpan):
        """Set take key range.
        
        TakeIndex : index of take to set.
        KeyTimeSpan : Timespan indicating the time range to keep the keys. Keys that are outside the time range for this take will be removed, by default the time range is FBTime::MinusInfinity -> FBTime::Infinity"""
        ...
    def SetTakeName(self,TakeIndex:int,Name:str):
        """Take Original Name.
        
        TakeIndex : index of take to set.
        Name : take name to set"""
        ...
    def SetTakeSelect(self,TakeIndex:int,Select:bool):
        """Return if true if the take will be saved or Loaded.
        
        TakeIndex : index of take to set
        Select : set true if should be saved or loaded."""
        ...
class FBFileMonitoringManager(FBComponent):
    """File Change Monitoring Interface to the file change monitoring."""
    OnFileChangeAnimationClip:FBEvent
    """Event: Animation clip file change event."""
    OnFileChangeFileReference:FBEvent
    """Event: File Reference file change event."""
    OnFileChangeMainScene:FBEvent
    """Event: Main scene file change event."""
    OnFileChangePythonEditorScript:FBEvent
    """Event: Python Editor Script file change event."""
    def AddFileToMonitor(self,FilePath:str,FileMonitoringType:FBFileMonitoringType):
        """Add file to monitor.
        
        FilePath : The file path to monitor.
        FileMonitoringType : The monitor type of this file."""
        ...
    def CleanFileMonitoring(self,IncludePythonEditorScripts:bool=True):
        """Clean files and directories currently been monitored.
        
        IncludePythonEditorScripts : True to also clean the monitoring of Python Editor script files loaded, false otherwise."""
        ...
    def PauseFileMonitoring(self,Pause:bool=True):
        """Pause file from monitoring, except for Python Editor script files loaded.
        
        Pause : True to pause the file monitoring, false to resume."""
        ...
    def RemoveFileFromMonitor(self,FilePath:str):
        """Remove file from monitoring.
        
        FilePath : The file path to be removed."""
        ...
class FBFilter(FBComponent):
    """Filters are used to modify motion capture data.
    Filters are objects which can be applied on a FCurve, or the animation node associated with an animated object property, to modify shape and number of keys. Filters can be created from the GUI, using the Filters tool, or programmatically with an instance of a FBFilterManager.The filter properties can be found in the object's PropertyList data member. They will use the same name, and be of the same type, as what can be seen in the GUI.Instances of FBFilter should be created with the help of the class FBFilterManager. Only internal application code should call the FBFilter's class constructor.Sample C++ code:
    
    >>> FBFilterManager lFilterManager;
    # Create a filter instace.
    FBFilter* lFilter = lFilterManager.CreateFilter( 'Key Reducing' );
    if( lFilter )
    {
    # Create a FCurve and populate it with keys.
    FBFCurve lCurve( 'Temp Curve' );
    for( int lIdx = 1; lIdx < 10; ++lIdx )
    {
    FBTime lTime( 0, 0, 0, lIdx * 5 );
    lCurve.KeyAdd( lTime, lIdx * 5 );
    }
    FBTrace( 'Keys before: %d
    ', lCurve.Keys.GetCount() ); // Should be 9.
    # Apply the key reducing filter.
    lFilter->Apply( &lCurve );
    FBTrace( 'Keys after: %d
    ', lCurve.Keys.GetCount() ); // Should be 2.
    }
    
    
    Sample Python code:
    
    >>> from pyfbsdk import *
    # Find a given model in the scene.
    lModel = FBFindModelByLabelName( 'Cube' )
    if lModel:
    # Create a Key Reducing filter.
    lFilter = FBFilterManager().CreateFilter( 'Key Reducing' )
    if lFilter:
    # Set the filter's precision to 2.0, and apply it to
    # the object's translation animation.
    lFilter.PropertyList.Find( 'Precision' ).Data = 2.0
    lFilter.Apply( lModel.Translation.GetAnimationNode(), True )"""
    Start:FBTime
    """Read Write Property: Start time of the filtering region"""
    Stop:FBTime
    """Read Write Property: Stop time of the filtering region"""
    def Apply(self,Curve:FBFCurve,Recursive:object)->bool:
        """Apply the filter to an animation node.
        This is the other apply method and it can be used on an object's animation node.
        
        Node : Node to apply filter to.
        Recursive : Recursively apply filter on child nodes?
        return : true if successful."""
        ...
    def Reset(self):
        """Reset properties."""
        ...
class FBFolder(FBComponent):
    """Folder class.
    This class is an interface to manipulate folders in the scene. See sample: FBFolder.py."""
    Items:FBPropertyListComponent
    """List: List of components in the folder."""
class FBGenericMenu(FBComponent):
    """A GenericMenu class.
    You can use this class either to create a new menu in the menu bar (or in a menuitem in the menu bar) or you can use this class to create a pop-up menu.
    
    >>> #to start a pop up menu use the Execute method
    def mouseClick(x, y):
    item = menu.Execute(x, y)
    if item.Id == 10:
    [do this]
    else if item.Id == 100:
    [do that...]
    
    
    There are 4 ways to insert new item in a menu. Each method needs the name of the menuitem as well as it's unique id. You can also optionally sets a new menu for a specific item.
    
    >>> embeededMenu = FBGenericMenu()
    menu.InsertLast('new new item', 67, embeddedMenu)
    #A genericMenu contains a GenericMenuItem for each entry. You can iterate on the different menuitem
    #using GetFirstITem/GetNextItem or if you already know the id of the item you can get it with GetItem.
    item = menu.GetFirstItem()
    while item:
    print item.Name
    item = menu.GetNextItem(item)
    
    
    
    
    >>> # This example shows how to list the Caption/Id of all the menu items of the Edit menu
    menuManager = FBMenuManager()
    editMenu = menuManager.GetMenu( 'Edit' )
    item = editMenu.GetFirstItem()
    while item:
    print ''' + item.Caption + '' (id: ' + str( item.Id ) + ')'
    item = editMenu.GetNextItem( item )
    
    
    You can also delete a Menu item: this will remove the item from the menu as well as freeing its memory.To be notified when a menuitem is clicked, you can register using OnMenuActivate. This will send a FBEventMenu containing the name and the Id of the menu item that was clicked. See sample: FBMenu.py."""
    OnMenuActivate:FBEvent
    """Event Property: Register on this property to be notified when a menu item is clicked by the user."""
    def DeleteItem(self,ToDelete:FBGenericMenuItem):
        """Remove a menu item from the menu and delete it.
        
        ToDelete : The item to remove."""
        ...
    def Execute(self,X:int,Y:int,RightAlign:bool=True)->FBGenericMenuItem:
        """Starts the menu as a pop-up menu at a specific location on screen.
        It returns the item that was clicked by the user.
        
        X : X location in pixel on screen where the menu is to be popped.
        Y : Y location in pixel on screen where the menu is to be popped.
        RightAlign : All menu item will be align to the right justified (if true) or left justified (if false)
        return : The selected item by the user. Null if the user clicks outside the menu."""
        ...
    def GetFirstItem(self)->FBGenericMenuItem:
        """Returns the first menu item (if existing) in this menu.
        You can then use GetNextItem to iterate on other menu items.
        
        return : The first menu item in this Menu."""
        ...
    def GetItem(self,ItemId:int)->FBGenericMenuItem:
        """Returns the menu item corresponding to an id.
        
        ItemId : Id of the item we are looking for.
        return : Will return the Item corresponding to an id (null if not found)."""
        ...
    def GetLastItem(self)->FBGenericMenuItem:
        """Returns the last menu item (if existing) in this menu.
        You can then use GetPrevItem to reverse iterate on other menu items.
        
        return : The last menu item in this Menu."""
        ...
    def GetNextItem(self,Item:FBGenericMenuItem)->FBGenericMenuItem:
        """Returns the menu item following an other item.
        Returns null if this is the last item in menu.
        
        Item : Will return the item afterItem
        return : Will return the item afterItem. Null ifItem is the last item."""
        ...
    def GetPrevItem(self,Item:FBGenericMenuItem)->FBGenericMenuItem:
        """Returns the menu item preceding an other item.
        Returns null if this is the first item in menu.
        
        Item : Will return the item BEFOREItem
        return : Will return the item BEFOREItem. Null ifItem is the first item."""
        ...
    def InsertAfter(self,BeforeItem:FBGenericMenuItem,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item AFTER another item.
        
        BeforeItem : The reference item. We will create a new item AFTER this one.
        ItemName : Caption of the newly added item.
        ItemId : Unique id of this menu item.
        Menu : Optional. If this Item leads to another menu (embedded) it can be specified here.
        return : Will return the menu item created from this insertion."""
        ...
    def InsertBefore(self,AfterItem:FBGenericMenuItem,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item BEFORE another item.
        
        AfterItem : The reference item. We will create a new item BEFORE this one.
        ItemName : Caption of the newly added item.
        ItemId : Unique id of this menu item.
        Menu : Optional. If this Item leads to another menu (embedded) it can be specified here.
        return : Will return the menu item created from this insertion."""
        ...
    def InsertFirst(self,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item at the first position in the menu list.
        
        ItemName : Caption of the newly added item.
        ItemId : Unique id of this menu item.
        Menu : Optional. If this Item leads to another menu (embedded) it can be specified here.
        return : Will return the menu item created from this insertion."""
        ...
    def InsertLast(self,ItemName:str,ItemId:int,Menu:FBGenericMenu=None)->FBGenericMenuItem:
        """Inserts a new menu Item at the last position in the menu list.
        
        ItemName : Caption of the newly added item.
        ItemId : Unique id of this menu item.
        Menu : Optional. If this Item leads to another menu (embedded) it can be specified here.
        return : Will return the menu item created from this insertion."""
        ...
class FBGenericMenuItem(FBComponent):
    """FBGenericMenuItem This class stores data for a single menu item.
    A single menu item can contains another menu (embedded menu) or not. A GenericMenuItem has an Id and a Name.You can use a GenericMenuItem to modify the attributes of a menu (it is the only way to change its name).You cannot create a FBGenericMenuItem directly. You must use the insertion method in FBMenu of FBMenuManager to obtain a handle on a FBGenericMenuItem. See sample: FBMenu.py."""
    Caption:str
    """Read/Write Property: Caption of the menu item."""
    Enable:bool
    """Read/Write Property: Enable or Disable (grey out) a menu Item."""
    Id:int
    """Read/Write Property: Id of the menu item."""
    Menu:FBGenericMenu
    """Read/Write Property: If the menu item leads to another menu."""
class FBGeometry(FBComponent):
    """Geometry class.
    This class groups all geometry related elements which are shared across the different subclasses (FBMesh, FBSurface, FBNurbs and FBPatch). Geometry Material always use kFBGeometryReference_INDEX mode. While Normal, UV could have different combination of mapping and reference modes.Geometries created with SDK can support FBGeometryMapping_ALL_SAME or kFBGeometryMapping_BY_POLYGON for material, and kFBGeometryMapping_BY_CONTROL_POINT for Normal, Tangent, Binormal, Color and UV. Only one set of UV could be supported.Geometries passed from FBXSDK pipeline could have various complex mapping/reference mode combination for material, normal and UV. And could potentially contains multiple set of UVs. See samples: ShapeCreation.py, VertexArrayManipulation.py."""
    BinormalMappingMode:FBGeometryMappingMode
    """Read Only Property: Binormal mapping mode."""
    BinormalReferenceMode:FBGeometryReferenceMode
    """Read Only Property: Binormal reference mode."""
    MaterialMappingMode:FBGeometryMappingMode
    """Read Property: Material mapping mode."""
    NormalMappingMode:FBGeometryMappingMode
    """Read Only Property: Normal mapping mode."""
    NormalReferenceMode:FBGeometryReferenceMode
    """Read Only Property: Normal reference mode."""
    TangentMappingMode:FBGeometryMappingMode
    """Read Only Property: Tangent mapping mode."""
    TangentReferenceMode:FBGeometryReferenceMode
    """Read Only Property: Tangent reference mode."""
    VertexColorMappingMode:FBGeometryMappingMode
    """Read Only Property: Vertex Color mapping mode."""
    VertexColorReferenceMode:FBGeometryReferenceMode
    """Read Only Property: Vertex Color reference mode."""
    def GeometryBegin(self)->bool:
        """Begin geometry editing.
        
        return : true if successful."""
        ...
    def GeometryEnd(self)->bool:
        """End geometry editing.
        
        return : true if successful."""
        ...
    def GetBinormalsDirectArray(self)->FBNormal:
        """Get a pointer to the direct array of binormals.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to direct array of binormals, or NULL if the array hasn't been allocated yet."""
        ...
    def GetBinormalsIndexArray(self)->int:
        """Get a pointer to the index array of binormals.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of binormals, or NULL if the array hasn't been allocated yet."""
        ...
    def GetMaterialIndexArray(self)->int:
        """Get a pointer to the index array of Material.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of Material, or NULL if the array hasn't been allocated yet."""
        ...
    def GetNormalsDirectArray(self)->FBNormal:
        """Get a pointer to the direct array of normals.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to direct array of normals, or NULL if the array hasn't been allocated yet."""
        ...
    def GetNormalsIndexArray(self)->int:
        """Get a pointer to the index array of normals.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of normals, or NULL if the array hasn't been allocated yet."""
        ...
    def GetPositionsArray(self)->FBVertex:
        """Get a pointer to the position array.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of normals, or NULL if the array hasn't been allocated yet."""
        ...
    def GetTangentsDirectArray(self)->FBNormal:
        """Get a pointer to the direct array of tangents.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to direct array of tangents, or NULL if the array hasn't been allocated yet."""
        ...
    def GetTangentsIndexArray(self)->int:
        """Get a pointer to the index array of tangents.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of tangents, or NULL if the array hasn't been allocated yet."""
        ...
    def GetUVSetDirectArray(self,OutArrayCount:int)->FBUV:
        """Get a pointer to the direct array of UVset Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        UVSetName : The name of UVset, NULL for the first UVset.
        return : pointer to the array of UV, or NULL is the array hasn't been allocated yet."""
        ...
    def GetUVSetIndexArray(self,OutArrayCount:int)->int:
        """Get a pointer to the index array of UVset.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        UVSetName : The name of UVset, NULL for the first UVset.
        return : Pointer to index array of UVSet, or NULL if the array hasn't been allocated yet."""
        ...
    def GetUVSetMappingMode(self,UVSetName:str=None)->FBGeometryMappingMode:
        """Get UVSet mapping mode.
        
        UVSetName : The name of UVset, NULL for the first UVset.
        return : Mapping mode of the UVset."""
        ...
    def GetUVSetReferenceMode(self,UVSetName:str=None)->FBGeometryReferenceMode:
        """Get UVSet reference mode.
        
        UVSetName : The name of UVset, NULL for the first UVset.
        return : Reference mode of the UVset."""
        ...
    def GetUVSets(self)->FBStringList:
        """Get available UVSet name.
        
        return : StringList contain all the available UVSets' name."""
        ...
    def GetVertexColorsDirectArray(self)->list:
        """Get a pointer to the direct array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to direct array of vertex colors, or NULL if the array hasn't been allocated yet."""
        ...
    def GetVertexColorsIndexArray(self)->int:
        """Get a pointer to the index array of vertex color.
        Modify array value will be only effective when geometry editing is enabled.
        
        OutArrayCount : To return the length the array.
        return : Pointer to index array of vertex color, or NULL if the array hasn't been allocated yet."""
        ...
    def SetBinormalsDirectArray(self,arg2:list)->bool:...
    def SetBinormalsIndexArray(self,arg2:list)->bool:...
    def SetMaterialIndexArray(self,arg2:list)->bool:...
    def SetNormalsDirectArray(self,arg2:list)->bool:...
    def SetNormalsIndexArray(self,arg2:list)->bool:...
    def SetPositionsArray(self,arg2:list)->bool:...
    def SetTangentsDirectArray(self,arg2:list)->bool:...
    def SetTangentsIndexArray(self,arg2:list)->bool:...
    def SetUVSetDirectArray(self,arg2:list,arg3:str)->bool:...
    def SetUVSetIndexArray(self,arg2:list,arg3:str)->bool:...
    def SetVertexColorsDirectArray(self,arg2:list)->bool:...
    def SetVertexColorsIndexArray(self,arg2:list)->bool:...
    def ShapeAdd(self,Name:str)->int:
        """Add new shape.
        
        Name : the shape name
        return : the index of the new shape, -1 if the shape adding fail."""
        ...
    def ShapeClearAll(self):
        """Clears all the shapes."""
        ...
    def ShapeGetCount(self)->int:
        """Get Shape Count."""
        ...
    def ShapeGetDiffPoint(self,ShapeIdx:int,DiffIndex:int,OriIndex:int,PosDiff:FBVertex,NormalDiff:FBNormal)->bool:
        """Get the differentiate point.
        
        ShapeIdx : The index of the shape
        DiffIndex : The index of the diff point in this shape.
        OriIndex : The index of the diff point in the original geometry.
        PosDiff : The position differentiation.
        NormalDiff : The normal differentiation."""
        ...
    def ShapeGetDiffPointAsList(self,arg2:object,arg3:object,arg4:list,arg5:FBVertex,arg6:FBNormal)->bool:...
    def ShapeGetName(self,ShapeIdx:int)->str:
        """Return the shape Name.
        
        ShapeIdx : int"""
        ...
    def ShapeInit(self,ShapeIdx:int,DiffSize:int,WithNormal:bool=False):
        """Init the shape.
        
        ShapeIdx : The index of the shape to be initialized
        DiffSize : Total number of different point (pos or normal) compared to base geometry.
        WithNormal : Currently normal won't be considered during shape blending."""
        ...
    def ShapeSetDiffPoint(self,ShapeIdx:int,DiffIndex:int,OriIndex:int,PosDiff:FBVertex,NormalDiff:FBNormal)->bool:
        """Set the differentiate point.
        
        ShapeIdx : The index of the shape
        DiffIndex : The index of the diff point in this shape.
        OriIndex : The index of the diff point in the original geometry.
        PosDiff : The position differentiation.
        NormalDiff : The normal differentiation."""
        ...
    def VertexAdd(self,Vertex:FBVertex)->int:
        """Begin geometry editing.
        
        px : float
        py : float
        pz : float
        nx : float
        ny : float
        nz : float
        UVu : float
        UVv : float
        Red : float
        Green : float
        Blue : float
        Alpha : float
        return : true if successful."""
        ...
    def VertexArrayClear(self)->bool:
        """Clear all geometry vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).
        
        return : true if successful."""
        ...
    def VertexArrayInit(self,Vertexcount:int,UniqueMaterial:bool,FBGeometryArrayIDs:int=0)->bool:
        """Init geometry vertex arrays.
        Init position, normal and UV arrays (tangent, bi-normal and color on demand) with kFBGeometryMapping_BY_CONTROL_POINT / kFBGeometryReference_DIRECT mode. Will call VertexArrayClear() internally. User should then call GetXXXDirectyArray() to edit the vertex attributes directly.
        
        Vertexcount : number of control points (vertex)
        UniqueMaterial : User could specify per polygon mapping mode for mesh
        FBGeometryArrayIDs : Request to init other attribute arrays, bitwise combined value of FBGeometryArrayID enum items, currently support Tangent, Binormal and VertexColor. Only useful for mesh."""
        ...
    def VertexClear(self)->bool:
        """Clear all Vertex arrays.
        Call this function to clear Position, Normal, UV, Color and etc vertex arrays, and it won't affect geometry's topology (polygon, Surface and etc.,).
        
        return : true if successful."""
        ...
    def VertexColorGet(self,Index:int=-1)->FBColorAndAlpha:
        """Get a Vertex Color.
        
        Index : Index of Vertex to get Color for(default=-1).
        return : Color of vertex at UVSetIndex."""
        ...
    def VertexColorSet(self,Red:float,Green:float)->bool:
        """Set a UV coordinate.
        
        Red : Red Color Channel to set, range [0, 1].
        Green : Green Color Channel to set, range [0, 1].
        Blue : Blue Color Channel to set, range [0, 1].
        Alpha : Alpha Color Channel to set, range [0, 1].
        Index : Index of Vertex to affect with Red, Green, Blue and Alpha (default=-1).
        return : true if successful."""
        ...
    def VertexCount(self)->int:
        """Get the number of vertices in the geometry.
        
        return : Number of vertices in the geometry."""
        ...
    def VertexGet(self,Index:int)->FBVertex:
        """Get a vertex.
        
        Index : Index of vertex to get.
        return : Vertex stored atIndex."""
        ...
    def VertexGetSelected(self,Index:int)->bool:
        """Get the selected state of a vertex.
        
        Index : The index of the vertex
        return : true if the vertex is selected, false if not"""
        ...
    def VertexGetTransformable(self,Index:int)->bool:
        """Get the Transformable state of a vertex.
        
        Index : The index of the vertex
        return : true if the vertex is Transformable, false if not"""
        ...
    def VertexGetVisible(self,Index:int)->bool:
        """Get the visible state of a vertex.
        
        Index : The index of the vertex
        return : true if the vertex is visible, false if not"""
        ...
    def VertexInit(self,Size:int,Resize:bool,InitUV:bool=True,InitVertexColor:bool=False):
        """Resize or Reserve vertex, normal and UV array for performance.
        
        Size : Number of vertices to resize or reserve.
        Resize : True, for the geometry with known vertex count, we should resize the arrays to fixed size, and call VertexSet() afterwards; False, While for dynamic size geometry, we should only reserve the arrays with the estimated optimal size, then call VertexAdd() to dynamically increase the vertex count.
        InitUV : init Vertex UV array if true
        InitVertexColor : Init Vertex Color Array if true."""
        ...
    def VertexNormalGet(self,Index:int=-1)->FBNormal:
        """Get a normal at a vertex.
        
        Index : Vertex to get normal at(default=-1).
        return : Normal of vertex atIndex."""
        ...
    def VertexNormalSet(self,Vertex:FBNormal,Index:int=-1)->bool:
        """Set a normal at a vertex.
        
        px : X coordinate of normal.
        py : Y coordinate of normal.
        pz : Z coordinate of normal.
        Index : Index of vertex to set Normal at(default=-1).
        return : true if successful."""
        ...
    def VertexSet(self,Vertex:FBVertex,Index:int=-1)->bool:
        """Set a vertex.
        
        px : X coordinate to set.
        py : Y coordinate to set.
        pz : Z coordinate to set.
        Index : Index of vertex to set(default=-1).
        return : true if successful."""
        ...
    def VertexSetSelected(self,Index:int,State:bool)->bool:
        """Set the selected state of a vertex.
        
        Index : The index of the vertex
        State : The true to selected, false to deselect
        return : true if the vertex is selected, false if not"""
        ...
    def VertexSetVisible(self,Index:int,State:bool)->bool:
        """Set the visible state of a vertex.
        
        Index : The index of the vertex
        State : true to be visible
        return : true if the vertex is visible, false if not"""
        ...
    def VertexUVGet(self,Index:int=-1)->FBUV:
        """Get a UV coordinate.
        
        Index : Index of Vertex to get UV coordinate for(default=-1).
        return : UV coordinate of vertex at UVSetIndex."""
        ...
    def VertexUVSet(self,U:float,V:float)->bool:
        """Set a UV coordinate.
        
        U : U coordinate to set.
        V : V coordinate to set.
        Index : Index of Vertex to affect with UV coordinate(default=-1).
        return : true if successful."""
        ...
class FBHUDManager(FBComponent):
    DefaultHUD:property
    """Read Write Property: Specifies the HUD to be displayed on cameras that do not have HUD explicitly assigned."""
class FBMesh(FBGeometry):
    """Mesh class.
    See samples: GeometryInstancing.py, VertexArrayManipulation.py, VertexColor.py."""
    def ComputeVertexNormals(self,CW:bool=False):
        """Compute Mesh Vertex Normal.
        
        CW : True for clock wise normal, otherwise for counter-clock wise"""
        ...
    def InverseNormal(self):
        """Inverse Normal."""
        ...
    def IsTriangleMesh(self)->bool:
        """Determines if the mesh is composed entirely of triangles.
        
        return : true if all polygons are triangles, false otherwise"""
        ...
    def PolygonBegin(self,MaterialId:int=0)->int:
        """Begin Polygon definition.
        
        MaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode.
        return : Number of existing polygons in Mesh"""
        ...
    def PolygonCount(self)->int:
        """Get number of polygons in mesh.
        
        return : Number of polygons in mesh."""
        ...
    def PolygonEnd(self)->int:
        """End Polygon definition.
        Clean up and associate vertices internally.
        
        return : Current number of polygons."""
        ...
    def PolygonListAdd(self,PolygonSize:int,IndexArraySize:int,IndexArray:int,MaterialId:int=0)->bool:
        """Add Polygon List Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        
        PolygonSize : Size of polygon, 3 mean triangle, 4 for quadrilateral, and so on. minimum input value is 3.
        IndexArraySize : Size ofIndexArray, Added polygon count is floor(max(pIndexArraySize, 0) /PolygonSize)
        IndexArray : Index array of triangle strip.
        MaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode."""
        ...
    def PolygonMaterialIdGet(self,Index:int=-1)->int:
        """Get a Material ID for the given Polygon index.
        
        Index : Polygon's index to get material ID at (default=-1).
        return : ID of material of vertex atIndex."""
        ...
    def PolygonVertexAdd(self,Vertex:int)->bool:
        """Add a vertex.
        
        Vertex : Index in mesh of vertex to add to polygon, must be in range of [0, ControlPointCount)
        return : true if successful."""
        ...
    def PolygonVertexArrayGet(self)->int:
        """Get the array of polygon vertex (i.e.
        index to control points). This array is a concatenation of the list of polygon vertices of all the polygons. Example: a mesh made of 2 triangles [1,2,3] and [2,3,4] results in [1,2,3,2,3,4]. The first polygon starts at position 0 and the second at position 3.
        
        ArraySize : Polygon vertex array size.
        return : Readonly polygon vertex array."""
        ...
    def PolygonVertexCount(self,PolygonIndex:int)->int:
        """Get Polygon vertex count.
        
        PolygonIndex : Index of polygon to get vertex count from.
        return : Number of vertices in polygon atPolygonIndex."""
        ...
    def PolygonVertexIndex(self,PolygonIndex:int,VertexPolygonIndex:int)->int:
        """Get global (for the mesh) index of a vertex from a polygon.
        
        PolygonIndex : Index of polygon in question.
        VertexPolygonIndex : Polygon vertex index.
        return : Index in mesh of vertex."""
        ...
    def TriangleListAdd(self,IndexArraySize:int,IndexArray:int,MaterialId:int=0)->bool:
        """Add Triangle List, Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        
        IndexArraySize : Size ofIndexArray, Added triangle count is floor(max(pIndexArraySize, 0) / 3)
        IndexArray : Index array of triangle list.
        MaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode."""
        ...
    def TriangleStripAdd(self,IndexArraySize:int,IndexArray:int,MaterialId:int=0)->bool:
        """Add Triangle Strip Must be called in-between FBGeometry::GeometryBegin() / GeometryEnd() It's user's responsibility to make sure to input valid index values, otherwise afterwards behavior will be undefined.
        
        IndexArraySize : Size ofIndexArray, Added triangle count is max(pIndexArraySize - 2, 0)
        IndexArray : Index array of triangle strip.
        MaterialId : Index of material for this polygon. Only effective when MaterialMappingMode is kFBGeometryMapping_BY_POLYGON mode."""
        ...
class FBImage(FBComponent):
    """Image class.
    Utility class used to load and get manipulate image data from disk or memory. See sample: VideoMemory.py."""
    Depth:int
    """Read Write Property: Color depth of the image."""
    Format:FBImageFormat
    """Read Write Property: Image data format."""
    Height:int
    """Read Write Property: Height of the image in pixels."""
    InterleaveType:FBImageInterleaveType
    """Read Only Property: Image interleave type. Only meaningful if image type is field."""
    InterpolationType:FBImageInterpolationType
    """Read Only Property: Image interpolation type."""
    Type:FBImageType
    """Read Only Property: Image type, refering to either frame or field."""
    Width:int
    """Read Write Property: Width of the image in pixels."""
    def Cleanup(self):
        """Cleanup image data, making it black."""
        ...
    def ConvertFormat(self,NewFormat:FBImageFormat)->bool:
        """Convert the image data format to another format.
        
        NewFormat : The new format to convert the image to.
        return : Return true if the convert was successful."""
        ...
    def ConvertSize(self,Width:int,Height:int)->bool:
        """Convert the image size.
        
        Width : New width of the image.
        Height : New height of the image.
        return : Return true if the convert was successful."""
        ...
    def GetBufferAddress(self)->str:
        """Access image data buffer, allow modifications.
        
        return : Pointer to the image data, values ranging from 0 to 255."""
        ...
    def Init(self,Format:FBImageFormat,Width:int,Height:int)->bool:
        """Init.
        
        Format : Image format used to initialize data buffer.
        Width : Image width in pixels.
        Height : Image height in pixels."""
        ...
    def IsCompressedTif(self,FileName:str)->bool:
        """Query TIF file about its compressed status.
        
        FileName : Full TIF file path name of the file to query.
        return : Return true if the TIF file image data is compressed."""
        ...
    def VerticalFlip(self):
        """Flip the image vertically."""
        ...
    def WriteToTif(self,FileName:str,Comments:str,Compressed:bool)->bool:
        """Write image data to a TIF file on disk.
        
        FileName : Full TIF file path name of the file to write.
        Comments : Comments appended to the TIF file.
        Compressed : If true, the image data in the file will be compressed.
        return : Return true if the image was successfully written on disk."""
        ...
class FBKeyControl(FBComponent):
    """Key control.
    Interface to use the key controls tool. See sample: MirrorPoseOverTime.py."""
    AutoKey:bool
    """Read Write Property: Enable/Disable Auto Key feature (key when moving 3D objects)."""
    NewKeyInterpolationType:FBNewKeyInterpolationType
    """Read Write Property: Current key interpolation type that will be used for new keys."""
    def MoveKeys(self,TimeSpan:FBTimeSpan,Pivot:FBModel,T:FBVector3d,R:FBVector3d,S:FBVector3d,Time:FBTime,ModelList:FBModelList=None):
        """Move animation keys in space, with respect to a pivot object.
        Equivalent to using the 'Move Keys' button in the Key Controls panel. Only keys that are part of the current animation layer will get affected.
        
        TimeSpan : The time span in which the animation keys will be modified
        Pivot : The pivot object to use as a reference. The pivot needs to be part ofModelList (or the current keying group) otherwise the move keys operation will abort
        T : The global translation to apply to the pivot
        R : The global Euler rotation to apply to the pivot (deg)
        S : The global scaling factors to apply to the pivot
        Time : The time at which the transformation values are applied to the pivot object
        ModelList : List of models for which the animation will be modified. Optional parameter. If not supplied, the models in the current keying group will be used"""
        ...
class FBKeyingGroup(FBComponent):
    """KeyingGroup class.
    This class is an interface to manipulate which properties will be keyed when active. A derived class could control when the keying group should activate and what content it should have. For example, a derived class could activate based one that is selected in the scene.To create a custom keying group, use the appropriate FBKeyingGroupType flag. Then, if it is a local keying group, call AddObjectDependency() to add an object to the keying group. You can then add properties belonging to the new object with AddProperty().If you are creating an object type keying group, call SetObjectType() to specify what kind of object will be keyed by this keying group. Then, add a property from an object, the name of the property will be used by the keying group the find corresponding properties in selected object.If you create a global keying group, simply properties from an object with AddProperty(). The name of the property will be used by the keying group to find corresponding properties in the selected object."""
    def AddObjectDependency(self,Obj:FBComponent):
        """AddObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).
        
        Obj : a Dependency of the keying group."""
        ...
    def AddProperty(self,Prop:FBProperty):
        """Add property to be keyed when current keying group is active.
        
        Prop : Property to be added."""
        ...
    def ClearAllItems(self):
        """ClearAllItems clear object dependency, properties and child keying group."""
        ...
    def DeselectAllAnimatableProperties(self):
        """FBDeselectAllAnimatableProperties, deselect all animatable properties in the scene."""
        ...
    def FindPropertyIndex(self,Prop:FBProperty)->int:
        """FindPropertyIndex.
        
        Prop : must be in the list (return -1 if not).
        return : the index ofProp in the keyinggroup property list."""
        ...
    def GetCumulativeProperty(self,Index:int,StopAtVisible:bool=False)->FBProperty:
        """GetCumulativeProperty Same as GetSubKeyingGroup but recursive in child keying group.
        
        Index : index in the content Object Dependency list
        StopAtVisible : consider all keying group and stop to the first visible keying group.
        return : he number of ObjectDependency of the keying group."""
        ...
    def GetCumulativePropertyCount(self,StopAtVisible:bool=False)->int:
        """GetCumulativePropertyCount Same as GetSubKeyingGroupCount but recursive in child keying group.
        
        StopAtVisible : consider all keying group and stop to the first visible keying group.
        return : he number of ObjectDependency of the keying group."""
        ...
    def GetParentKeyingGroup(self,Index:int)->FBKeyingGroup:
        """GetParentKeyingGroup.
        
        Index : is the index of the parent list of the current keying group.
        return : the parent keying group."""
        ...
    def GetParentKeyingGroupCount(self)->int:
        """GetParentKeyingGroupCount.
        
        return : the number of parent."""
        ...
    def GetProperty(self,Index:int)->FBProperty:
        """GetProperty from the keyinggroup list.
        
        Index : index of the desired property.
        return : property coresponding toIndex."""
        ...
    def GetPropertyCount(self)->int:
        """GetPropertyCount.
        
        return : the number of properties in the keying group."""
        ...
    def GetSubKeyingGroup(self,Index:int)->FBKeyingGroup:
        """GetSubKeyingGroup.
        
        Index : index of the desired keying group child.
        return : the the child at the index."""
        ...
    def GetSubKeyingGroupCount(self)->int:
        """GetSubKeyingGroupCount.
        
        return : the number of child keying group."""
        ...
    def GetSubObject(self,Index:int)->FBComponent:
        """GetSubObject.
        
        Index : index in the content Object Dependency list
        return : the desired object atIndex."""
        ...
    def GetSubObjectCount(self)->int:
        """GetSubObjectCount.
        
        return : the number of ObjectDependency of the keying group."""
        ...
    def IsObjectDependency(self,Obj:FBComponent)->bool:
        """IsObjectDependency determine if theObj is a dependency.
        
        Obj : an object to test the Dependency.
        return : true if it depend."""
        ...
    def IsObjectDependencySelected(self)->bool:
        """IsObjectDependencySelected.
        
        return : return true as soon as a Property Owner or another Object Dependency is selected."""
        ...
    def RemoveAllObjectDependency(self):
        """IsObjectDependencySelected empty the content list."""
        ...
    def RemoveAllProperties(self):
        """IsObjectDependencySelected empty the property list."""
        ...
    def RemoveAllSubKeyingGroup(self):
        """RemoveAllSubKeyingGroup empty the child keying group."""
        ...
    def RemoveObjectDependency(self,Obj:FBComponent):
        """RemoveObjectDependency An object dependency is the content of a keying group and will activate keying group when selected (activation only works if the keying group is a character extension).
        
        Obj : a Dependency of the keying group."""
        ...
    def RemoveProperty(self,Prop:FBProperty):
        """RemoveProperty from the keyinggroup list.
        
        Prop : Property to be removed."""
        ...
    def SetActive(self,Active:bool):
        """SetActive, activate the keying group, replacing the other keying group.
        
        Active : bool"""
        ...
    def SetActiveAppend(self,Active:bool):
        """SetActiveAppend, activate and append the keying group to the other keying groups.
        
        Active : bool"""
        ...
    def SetEnabled(self,Enable:bool):
        """SetEnabled, makes the keying group available in keying group list of the key control UI.
        
        Enable : bool"""
        ...
    def SetObjectType(self,Object:FBComponent):
        """Set the object type filter for and object type keying group.
        
        Object : Object that will be used to set the keying group object type. Use NULL to remove the filter."""
        ...
class FBLogger(FBComponent):
    def DisableClear(self):...
    def DumpObject(self,arg2:FBPlug,arg3:object)->object:...
    def Enable(self,TypeInfo:int,Enable:bool)->bool:...
    def GetLog(self)->object:...
class FBCharacterExtension(FBKeyingGroup):
    """Objects Grouping class.
    This class is an interface to manipulate object's grouping in the scene. See sample: CreateCharacterExtensionOnSelectedObject.py."""
    IncludePartInBodyPart:bool
    """Read Write Property: Include or not this extension when the Body Part mode is active."""
    IncludePartInFullBody:bool
    """Read Write Property: Include or not this extension when the Full Body mode is active."""
    Label:str
    """Read Write Property: The logical name of the extension, use for mirroring."""
    MirrorLabel:int
    """Read Write Property: Enum that indicate which extension is used as mirror, 0 is none, 1 is self, 2-n represent the (ith - 2)character extension in the attached character excluding self."""
    PlotAllowed:FBPlotAllowed
    """Read Write Property: Controls if objects in the set are transformable."""
    ReferenceModel:FBModel
    """Read Write Property: Controls the referential of the extension."""
    RetargetMode:FBCharacterExtensionRetargetMode
    """Read Write Property: Character extension retarget mode."""
    StancePoseMode:FBCharacterExtensionStancePoseMode
    """Read Write Property: Character extension stance pose mode."""
    SyncActivationAndVisibilityMode:FBSyncActivationAndVisibilityMode
    """Read Write Property: The 'Sync Activation & Visibility' mode."""
    def AddObjectProperties(self,Obj:FBComponent):
        """Add TR Properties from Object.
        
        Obj : Object to add TR properties."""
        ...
    def GetCharacter(self)->FBCharacter:
        """Return the attached Character.
        
        return : attached Character."""
        ...
    def GetExtensionObjectWithLabelName(self,LabelName:str)->FBComponent:
        """Find stored object based on label name.
        
        LabelName : The label name.
        return : The extension object."""
        ...
    def GetLabelNameWithExtensionObject(self,LabelName:str,Obj:FBComponent)->str:
        """Find the label name that was used to store object pose.
        
        LabelName : The label name that was used to store object pose.
        Obj : The extension object.
        ReturnObjectNameIfNotFound : If the value is true, if the object is not found,LabelName will be set to the object name; otherwiseLabelName will be set to empty string. By default the value is false."""
        ...
    def GetMirrorExtension(self)->FBCharacterExtension:
        """Return the character extension determined by MirrorLabel.
        
        return : character extension determined by MirrorLabel."""
        ...
    def GetRetargetPropertyCount(self)->int:
        """Return the total number of retarget properties.
        
        return : The total number of retarget properties."""
        ...
    def GetRetargetReferenceProperty(self,PropIndex:int)->FBProperty:
        """Return the reference property of the given index.
        
        PropIndex : Index to query.
        return : Reference property of the given index."""
        ...
    def GetRetargetSourceProperty(self,PropIndex:int)->FBProperty:
        """Return the source property of the given index (the source property is the property that drives the reference property during retargeting).
        
        PropIndex : Index to query.
        return : Source property (the property that drives the reference property during retargeting) of the given index."""
        ...
    def GetSourceExtension(self)->FBCharacterExtension:
        """Return the character extension that is used to drive this extension during retargeting.
        
        return : The character extension that is used to drive this extension during retargeting."""
        ...
    def GetSourceExtensionIndex(self)->int:
        """Return the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.
        
        return : The enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character."""
        ...
    def GetStancePose(self)->FBObjectPose:
        """Return stance pose.
        
        return : stance pose."""
        ...
    def GoToStancePose(self):
        """Reset object position to the stance."""
        ...
    def IsElementSelected(self)->bool:
        """Return true if one object in object dependency list is selected.
        
        return : true if one object in object dependency list is selected."""
        ...
    def IsPropertyIncluded(self,Prop:FBProperty)->bool:
        """Return true if the property is in character extension.
        
        Prop : Property to check.
        return : true if the property is in character extension."""
        ...
    def RemoveObjectAndProperties(self,Obj:FBComponent):
        """Remove TR Properties from Object.
        
        Obj : Object to remove TR properties."""
        ...
    def RemoveRetargetSourceProperty(self,PropIndex:int):
        """Remove the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.
        
        PropIndex : Index to remove."""
        ...
    def SetRetargetSourceProperty(self,PropIndex:int,SourceProp:FBProperty):
        """Set the source property for retargeting.
        Only applicable if RetargetMode is Manually Assign.
        
        PropIndex : Index to set.
        SourceProp : Source property to set."""
        ...
    def SetSourceExtension(self,SourceExtension:FBCharacterExtension):
        """Set the character extension to drive this extension during retargeting.
        Only applicable if RetargetMode is Assign.
        
        SourceExtension : The source extension to drive this extension during retargeting."""
        ...
    def SetSourceExtensionIndex(self,SrcExtIndex:int):
        """Set the enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character.
        Only applicable if RetargetMode is Manually Assign.
        
        SrcExtIndex : Enum that indicate which extension is used as a source during retargeting, 0 is none, 1-n represent the (ith - 1)character extension in the source character."""
        ...
    def UpdateStancePose(self):
        """Update the stance pose to the current position of the character extension element."""
        ...
class FBManipulator(FBComponent):
    """Manipulator class."""
    Active:bool
    """Read Write Property: Is manipulator active?"""
    AlwaysActive:bool
    """Read Write Property: Is manipulator always active?"""
    ConsumeEvent:bool
    """Read Write Property: Is manipulator consuming event? If true, this will prevent other manipulators from being called."""
    DefaultBehavior:bool
    """Read Write Property: Using default manipulator behavior?"""
    ViewerText:str
    """Read Write Property: Text displayed in view."""
    Visible:bool
    """Read Write Property: Is manipulator visible?"""
class FBMarkerSet(FBComponent):
    """Marker set class.
    These classes are under development and may change dramatically between versions."""
    def AddMarker(self,NodeId:FBSkeletonNodeId,Model:FBModel=None,IsOriented:bool=False)->int:
        """Add a marker to the marker set.
        
        NodeId : Id of Actor skeleton node. For hand, use the "C" index (ex:kFBSkeletonLeftThumbCIndex, kFBSkeletonLeftMiddleCIndex...)
        Model : The model to be associated with the marker (Optional).
        IsOriented : Set marker to be oriented or not (Optional).
        return : Index of the new marker."""
        ...
    def BeginTransaction(self):
        """Specify that you are about to call a group of functions."""
        ...
    def EndTransaction(self):
        """Specify that you are done calling a group of functions."""
        ...
    def GetLinkToModelOk(self)->bool:
        """Get the marker set association correctness.
        
        return : True if all used markers are link with models."""
        ...
    def GetMarkerCount(self,NodeId:FBSkeletonNodeId=FBSkeletonNodeId.kFBSkeletonInvalidIndex)->int:
        """Get the number of marker in the set.
        
        NodeId : If specified, obtain the number of marker for the specific node.
        return : Total number of marker."""
        ...
    def GetMarkerModel(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->FBModel:
        """Get the model associated with a marker.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker.
        return : The model associated with the marker."""
        ...
    def GetMarkerName(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->str:
        """Get the name of marker at indexMarkerIndex.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        return : Name of marker at indexMarkerIndex."""
        ...
    def GetMarkerOriented(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->bool:
        """Is marker orientated ?
        
        NodeId : Id of Actor body node.
        MarkerIndex : Index of marker to access.
        return : True if marker is oriented, false otherwise."""
        ...
    def GetMarkerROffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,ROffset):
        """Get/Set a marker rotation.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        ROffset : Current or new value of the marker rotation."""
        ...
    def GetMarkerSetVisibility(self)->int:
        """Get the marker set visibility.
        
        return : 1 if all markers are visible, 2 if some are visible, 0 if none are visible."""
        ...
    def GetMarkerTOffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,TOffset:FBVector3d):
        """Get/Set a marker translation.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        TOffset : Current or new value of the marker translation."""
        ...
    def GetMarkerUsed(self,NodeId:FBSkeletonNodeId,MarkerIndex:int)->bool:
        """Is marker used ?
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        return : True if marker is used, false otherwise."""
        ...
    def GetReferenceModel(self)->FBModel:
        """Get the reference model associated with this marker set.
        
        return : The reference model associated with the marker set."""
        ...
    def GetUsedMarkerCount(self,NodeId:FBSkeletonNodeId=FBSkeletonNodeId.kFBSkeletonInvalidIndex)->int:
        """Get the number of used marker in the set.
        
        NodeId : If specified, obtain the number of used marker for the specific node.
        return : Total number of used marker."""
        ...
    def SetMarkerModel(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,Model:FBModel):
        """Associate a model to a marker.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker.
        Model : Model to be associated to the marker."""
        ...
    def SetMarkerName(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,MarkerName:str):
        """Set the name of marker at indexMarkerIndex.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        MarkerName : New name to give to the marker."""
        ...
    def SetMarkerOriented(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,IsOriented:bool):
        """Set marker to be oriented or not.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        IsOriented : Oriented or not."""
        ...
    def SetMarkerROffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:object,ROffset:FBVector3d):
        """NodeId : FBSkeletonNodeId
        MarkerIndex : int
        ROffset : FBRVector"""
        ...
    def SetMarkerSetVisibility(self,Visibility:bool):
        """Set the marker set visibility.
        
        Visibility : True will make to markers visible, false will hide them."""
        ...
    def SetMarkerTOffset(self,NodeId:FBSkeletonNodeId,MarkerIndex:object,TOffset:FBVector3d):
        """NodeId : FBSkeletonNodeId
        MarkerIndex : int
        TOffset : FBTVector"""
        ...
    def SetMarkerUsed(self,NodeId:FBSkeletonNodeId,MarkerIndex:int,Used:bool):
        """Set marker to be used or not.
        
        NodeId : Id of Actor skeleton node.
        MarkerIndex : Index of marker to access.
        Used : Used or not."""
        ...
    def SetMultipleMarkerModels(self,ModelList:FBModelList)->bool:
        """Associate multiple models to markers, matching them by name.
        
        ModelList : A list of models to be matched with marker names.
        return : True if at least one marker was matched."""
        ...
    def SetReferenceModel(self,ReferenceModel:FBModel):
        """Associate a model to a marker.
        
        ReferenceModel : Model to be associated to the marker."""
        ...
class FBMenuManager(FBComponent):
    """The menu manager allows access to MotionBuilder menu bar.
    It can be used to retrieve the item corresponding to a menu path in the menu bar. A menu path is similar to a file path but it specifies the location of menu item in a hierarchy of menu. ex: to retrieve the item corresponding to MoBu Save item: item = menuMgr.GetMenu('File/Save')Other menu items in MoBu menu bar include the following: 'File', 'Edit','Animation','Window','Settings', 'Layout','Help'The menu manager can be used to insert new menu item in the menubar. You have to specify the menu path at which to insert the menu (to insert a new root menu, use NULL or None as the menu path)
    
    >>> #Insert a new Root Menu before the Help menu
    menuMgr.InsertBefore(None, 'Help', 'before menu')
    #Insert a new Root Menu after the Help menu
    menuMgr.InsertAfter(None, 'Help', 'After menu')
    
    
    As a convenience operation, you can from the menu manager enable and disable menu item (instead of retrieving their corresponding item). See sample: FBMenu.py."""
    def ExecuteMenuItem(self,MenuPath:str,MenuItemID:int)->bool:
        """Execute a particular menu item.
        The menu path specifies the menu containing the menu item to execute. The ID specifies which menu item to execute in the menu.
        
        MenuPath : Path containing the menu item to execute.
        MenuItemID : Unique ID of the menu item to execute.
        return : True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator."""
        ...
    def ExecuteMenuItemFromFullPath(self,MenuItemFullPath:str)->bool:
        """Execute a particular menu item.
        The menu path specifies the menu item (NOT menu) to execute. Don't forget that most menu path already in MotionBuilder have a '&' as the first letter of their name. You have to use the '/' character as a separator in the specified menu path (ex: 'Settings/&Preferences...'), and exactly what is written in the menu item (ex: 'Edit/D&eselect	Shift+D').
        
        >>> # This example shows how to display the About Box, as if the user opened it via the main menu Help > About MotionBuilder:
        menuManager = FBMenuManager()
        aboutBoxFullPath = 'Help/&About MotionBuilder'
        menuManager.ExecuteMenuItemFromFullPath( aboutBoxFullPath )
        
        
        MenuItemFullPath : Path of the menu item to execute.
        return : True if the menu item has been executed, false otherwise. It could returns false if the menu item cannot be found or if the menu item is found but is disabled or is a separator."""
        ...
    def GetMenu(self,Path:str)->FBGenericMenu:
        """Get the Menu (NOT menu item) corresponding to a menu path.
        Don't forget that most menu path already in MotionBuilder have a '&' character as the first letter of their name. You have to use the '/' character as a separator in the specified menu path (ex: 'Help/&Communities').
        
        Path : Path of the menu to retrieve
        return : the FBGenericMenu at this path./"""
        ...
    def InsertAfter(self,MenuPath:str,BeforeMenuName:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at a specific path AFTER another item.
        
        MenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu.
        BeforeMenuName : Name of the menu item AFTER which we will insert the new item.
        MenuName : str
        return : Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertBefore(self,MenuPath:str,AfterMenuName:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at a specific path BEFORE another item.
        
        MenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu.
        AfterMenuName : Name of the menu item BEFORE which we will insert the new item.
        MenuName : str
        return : Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertFirst(self,MenuPath:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at the first position of a specific path.
        
        MenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu.
        MenuName : Name (Caption) of the newly inserted menu.
        return : Returns the menu item corresponding to the newly inserted menu."""
        ...
    def InsertLast(self,MenuPath:str,MenuName:str)->FBGenericMenuItem:
        """Insert a new menu at the last position of a specific path.
        
        MenuPath : Path where to insert the menu. If this is NULL (None) it will insert a new root menu.
        MenuName : Name (Caption) of the newly inserted menu.
        return : Returns the menu item corresponding to the newly inserted menu."""
        ...
    def IsItemEnable(self,MenuPath:str,ItemId:int)->bool:
        """Check if a particular item is enabled or disabled.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.
        
        MenuPath : Path where to find the menu to check
        ItemId : Id of the item to check.
        return : Is the item enable or not."""
        ...
    def SetItemEnable(self,MenuPath:str,ItemId:int,Enable:bool):
        """Enable or disable a specific menu item.
        The menu path specifies the menu where we find the item to be enabled/disabled. The Id specifies which item in the menu.
        
        MenuPath : Path where to find the menu to enable/disable
        ItemId : Id of the item in the menu to disable.
        Enable : Enable (true) or disable (false) a menu item."""
        ...
class FBModelOpticalAdvanced(FBComponent):
    """Advanced optical model information."""
    Active:bool
    """Property: Optical engine for model active?"""
    AutoPlayToNextSegment:bool
    """Property: Automatic play to next segment ?"""
    ControllerMode:FBControllerMode
    """Property: Controller mode."""
    GenerationMode:FBGenerationMode
    """Property: Optical genration mode."""
    InsertSegmentMode:FBInsertSegmentMode
    """Property: Insert segment mode."""
    MaxMatchDistance:float
    """Property: Max matching distance."""
    PlayToNextSegment:bool
    """Property: Play to next segment ?"""
    Quality:FBAnimationNode
    """Property: Rigid body quality."""
    SegmentMode:FBSegmentMode
    """Property: Segment mode."""
    ShowRigidQuality:bool
    """Property: Show the rigid quality?"""
    UsedTake:FBTake
    """Property: Take used by optical model."""
    def AcceptAllSegments(self):
        """Accept all segments."""
        ...
    def AcceptSegment(self):
        """Accept current segment."""
        ...
    def AutomaticBuild(self):
        """Automatic build."""
        ...
    def CropSegmentsAnimation(self):
        """Crop segment animation."""
        ...
    def SkipSegment(self):
        """Skip segment."""
        ...
class FBModelTemplate(FBComponent):
    """Model template class.
    Model templates are 'placeholders' for animation input from devices. These generic 'models' can be any type of element, and permit the abstraction of the input from the actual type of model. In order to animate a model, one should bind the model to an animation node."""
    Bindings:FBPropertyListModelTemplateBinding
    """List: Bindings for animation interface."""
    Children:FBPropertyListModelTemplate
    """List: Children for object hierarchy."""
    DefaultRotation:FBVector3d
    """Read Write Property: Default rotation."""
    DefaultScaling:FBVector3d
    """Read Write Property: Default scaling."""
    DefaultTranslation:FBVector3d
    """Read Write Property: Default translation."""
    Model:FBModel
    """Read Write Property: Model being interfaced."""
    Prefix:str
    """Read Write Property: Prefix of model template."""
class FBModelVertexData(FBComponent):
    def DisableOGLUVSet(self):
        """Disable OpenGL UV set array."""
        ...
    def DisableOGLVertexData(self):
        """Disable OpenGL Vertex Array (Pos & Normal)."""
        ...
    def DrawSubPatch(self,SubPatchIndex:object,WireFrame:object):
        """Draw the specified sub patch.
        Must be called between Enable/DisableOGLVertexData function calls.
        
        SubPatchIndex : Index of the sub patch to be drawn.
        WireFrame : Draw wire frame if true."""
        ...
    def DrawSubRegion(self,SubRegionIndex:object,WireFrame:object):
        """Draw the specified sub region.
        Must be called between Enable/DisableOGLVertexData function calls.
        
        SubRegionIndex : Index of the sub region to be drawn.
        WireFrame : Draw wire frame if true."""
        ...
    def EnableOGLUVSet(self,TextureMapping:FBTextureMapping,UVSet:str):
        """Enable (Setup) OpenGL UV set array.
        
        TextureMapping : Texture Mapping Mode.
        UVSet : UV Set name ifTextureMapping is kFBTextureMappingUV, otherwise ignored."""
        ...
    def EnableOGLVertexData(self,AfterDeform:object):
        """Enable (Setup) OpenGL Vertex Array (Pos & Normal).
        
        AfterDeform : Unused parameter."""
        ...
    def GetIndexArray(self)->list:
        """Return the index array.
        For the size of the array, see GetIndexArraySize().
        
        return : (C++) The index array pointer. (Python) The index array as a list."""
        ...
    def GetIndexArraySize(self)->int:
        """Return the index array size (see GetIndexArray()).
        It will sum the index size of each sub patch (see GetSubPatchIndexSize()).
        
        return : The index array size."""
        ...
    def GetIndexArrayVBOId(self)->int:
        """Return the index array VBO Id.
        
        return : The index array VBO Id."""
        ...
    def GetSubPatchCount(self)->int:
        """Return the number of sub patches.
        
        return : The number of sub patches."""
        ...
    def GetSubPatchIndexOffset(self,SubPatchIndex:object)->int:
        """Return the start offset of the indexes for the specified sub patch (see GetIndexArray()).
        
        SubPatchIndex : Index of the sub patch to be queried.
        return : The start offset of the indexes for the specified sub patch, -1 if the specific sub path index is invalid."""
        ...
    def GetSubPatchIndexSize(self,SubPatchIndex:object)->int:
        """Return the size of the indexes for the specified sub patch (see GetIndexArray()).
        
        SubPatchIndex : Index of the sub patch to be queried.
        return : The size of the indexes for the specified sub patch, -1 if the specific sub path index is invalid."""
        ...
    def GetSubPatchMaterial(self,SubPatchIndex:object)->object:
        """Return the mapped material for the specified sub patch.
        
        SubPatchIndex : Index of the sub patch to be queried.
        return : The mapped material for the specified sub patch, the default material if the specific sub path index is invalid."""
        ...
    def GetSubPatchMaterialId(self,SubPatchIndex:object)->int:
        """Return the mapped material ID for the specified sub patch.
        
        SubPatchIndex : Index of the sub patch to be queried.
        return : The mapped material ID for the specified sub patch, -1 if the specific sub path index is invalid."""
        ...
    def GetSubPatchPrimitiveType(self,SubPatchIndex:object)->tuple:
        """Return the primitive type for the specified sub patch.
        Most of the time, kFBGeometry_TRIANGLES will be returned.
        
        SubPatchIndex : Index of the sub patch to be queried.
        IsOptimized : (C++ only) Out parameter, return true if the specified sub patch is optimized for fast rendering, custom shader & render should use the optimized sub patch only.
        return : (C++) The primitive type of the queried sub patch. (Python) A tuple with 2 values: (the primitive type of the queried sub patch, the value ofIsOptimized)."""
        ...
    def GetSubRegionCount(self)->int:
        """Return the number of sub regions (mapping with different materials).
        
        return : The number of sub regions."""
        ...
    def GetSubRegionMaterial(self,SubRegionIndex:object)->object:
        """Return the specified sub region's material.
        
        SubRegionIndex : Index of the sub region to be queried.
        return : The sub region's material, the default material if the specific sub region index is invalid."""
        ...
    def GetUVSetArray(self,TextureMapping:FBTextureMapping,UVSet:str)->list:
        """Return the UV Set array for the specified texture mapping mode.
        
        TextureMapping : Texture mapping mode to be queried.
        UVSet : UV Set name to be queried ifTextureMapping is kFBTextureMappingUV, otherwise ignored.
        return : (C++) The UV Set array pointer. (Python) The UV Set array as a list.
        
        >>> # The following C++ snippet show how to deal with the UV mapping UV Set array pointer returned.
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
        # Do something useful here
        FBTrace( "%f, %f
        ", lUVArray[ i ][ 0 ], lUVArray[ i ][ 1 ] );
        }
        }
        }"""
        ...
    def GetUVSetArrayFormat(self,TextureMapping:FBTextureMapping,UVSet:str)->FBGeometryArrayElementType:
        """Return the UV Set array format.
        
        TextureMapping : Unused parameter.
        UVSet : Unused parameter.
        return : The UV Set array format."""
        ...
    def GetUVSetUVCount(self,TextureMapping:FBTextureMapping,UVSet:str)->int:
        """Return the number of UVs in the UV Set for the specified texture mapping mode.
        
        TextureMapping : Texture mapping mode to be queried.
        UVSet : UV Set name to be queried ifTextureMapping is kFBTextureMappingUV, otherwise ignored.
        return : The number of UVs in the UV Set for the specified texture mapping mode."""
        ...
    def GetUVSetVBOId(self,TextureMapping:FBTextureMapping,UVSet:str)->int:
        """Return the UV Set Buffer Object (VBO) Id for the specified texture mapping mode.
        
        TextureMapping : Texture mapping mode to be queried.
        UVSet : UV Set name to be queried ifTextureMapping is kFBTextureMappingUV, otherwise ignored.
        return : The UV Set VBO Id."""
        ...
    def GetUVSetVBOOffset(self,TextureMapping:FBTextureMapping,UVSet:str)->int:
        """Return the UV Set Buffer Object (VBO) offset for the specified texture mapping mode.
        
        TextureMapping : Texture mapping mode to be queried.
        UVSet : UV Set name to be queried ifTextureMapping is kFBTextureMappingUV, otherwise ignored.
        return : The UV Set VBO offset (C++: as a pointer, Python: as a kReference)."""
        ...
    def GetVertexArray(self,ArrayId:FBGeometryArrayID,AfterDeform:object)->list:
        """Return the vertex array for the specified vertex array Id.
        
        ArrayId : Vertex array Id type to be queried.
        AfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array.
        return : (C++) The vertex array pointer. (Python) The vertex array as a list. Deformed position & normal vertex arrays could be NULL if one has not requested the mapping vertex array on CPU."""
        ...
    def GetVertexArrayDuplicationMap(self)->list:
        """The FBModel::TessellatedMesh could contain per-face mapping UVSet/Normal or other layer elements.
        In order to build a valid VBO buffer for accelerated rendering, those control points with multiple attribute data must be duplicated. This function returns the duplicated vertices' ID mapping from FBModel::ModelVertexData vertex array to its FBModel::TessellatedMesh vertex array. Note those duplicated vertices are always appended after the original vertex array.
        
        DuplicatedVertexCount : only)DuplicatedVertexCount Out parameter, return the count of those duplicated vertices.
        return : (C++) A pointer to the original vertex ID mapping for those duplicated vertices. (Python) A list containing the vertex ID mapping for those duplicated vertices."""
        ...
    def GetVertexArrayType(self,ArrayId:FBGeometryArrayID,AfterDeform:object)->FBGeometryArrayElementType:
        """Return the vertex array format for the specified array Id.
        
        ArrayId : Vertex array Id type to be queried.
        AfterDeform : Unused parameter.
        return : The vertex array format for the specified array Id."""
        ...
    def GetVertexArrayVBOId(self,ArrayId:FBGeometryArrayID,AfterDeform:object)->int:
        """Return the Vertex Buffer Object (VBO) Id for the specified vertex array Id.
        
        ArrayId : Vertex array Id type to be queried.
        AfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array.
        return : The vertex array VBO Id. Deformed position & normal vertex VBO Id could be 0 if model use CPU skinning."""
        ...
    def GetVertexArrayVBOOffset(self,ArrayId:FBGeometryArrayID,AfterDeform:object)->int:
        """Return the Vertex Buffer Object (VBO) offset for the specified vertex array Id.
        
        ArrayId : Vertex array Id type to be queried. Only position or normal vertex array Id types are available.
        AfterDeform : True to query the deformed position or normal vertex array (model must be deformable and deformation must occur in CPU), false to query the original vertex array.
        return : The vertex array VBO offset (C++: as a pointer, Python: as a kReference)."""
        ...
    def GetVertexCount(self)->int:
        """Return the number of vertices.
        
        return : The number of vertices."""
        ...
    def IsDeformable(self)->bool:
        """Return true if the model is deformable.
        
        return : True if the model is deformable, false otherwise."""
        ...
    def IsDrawable(self)->bool:
        """Queries if this model should be drawn, e.g., in custom render callback.
        Returns false if e.g., deformed vertex data has not been computed for this frame (thus not ready to be drawn), or if model should be hidden when Z-Depth selection tool is active.
        
        return : True if the model should be drawn, false otherwise."""
        ...
    def PopZDepthClipOverride(self):
        """Re-enables Z-Depth clip plane if it had been disabled via PushZDepthClipOverride().
        Call this function after drawing each model in custom render callback, so that Z-Depth clip plane is re-enabled if it was earlier disabled via PushZDepthClipOverride()."""
        ...
    def PushZDepthClipOverride(self):
        """Disables Z-Depth clip plane if this model is selected using Z-Depth HideFront selection tool.
        Call this function before drawing each model in custom render callback, so that the selected model is unaffected by the Z-Depth clip plane, and hence is visible when Z-Depth HideFront selection tool is active. Be sure to call PopZDepthClipOverride() after drawing each model."""
        ...
    def VertexArrayMappingRelease(self):
        """Release deformed vertex array mapping on CPU.
        Call this function if plug-in don't need CPU access of the deformed vertex array to be mapped on CPU memory anymore, hence allow the application flexibility to choose higher performance approach."""
        ...
    def VertexArrayMappingRequest(self):
        """Request deformed vertex array mapping on CPU.
        Model's deformation computation could be executed on GPU, and thus the deformed vertex data will reside in GPU memory only by default. Calling this function VertexArrayMappingRequest() will ensure the deformed vertex array to be always mapped to CPU memory."""
        ...
class FBMotionClip(FBComponent):
    """Motion class.
    Properties of this class are work in progress, but you can still list them and get their names."""
    Filename:str
    """Read Write Property: Filename and path of motion file."""
    RelativePath:str
    """Read Only Property: Relative path to the motion file."""
    Start:FBTime
    """Read Only Property: Start time of clip."""
    Stop:FBTime
    """Read Only Property: Stop time of clip."""
class FBMotionFileOptions(FBComponent):
    """Customize motion file loading."""
    BaseRotationOnPreRotation:bool
    """Read Write Property: If set to true, the base rotation will be imported as Pre Rotation. Used for htr, asf/amc files."""
    BaseTranslationOnRotationOffset:bool
    """Read Write Property: If set to true, the base translation will be imported as Rotation Pivot offset. Used for htr, asf/amc"""
    CreateInsteadOfMerge:bool
    """Read Write Property: If set to true, the motion will imported/models will be created in the scene, if set to false, the motion will be merged."""
    CreateOpticalSegments:bool
    """Read Write Property: If set to true, optical segments will be created. Used for trc, c3d files."""
    CreateReferenceNode:bool
    """Settings based on file type."""
    CreateUnmatchedModels:bool
    """Read Write Property: If set to true, nodes will be created to match the hierarchical structure of the imported file."""
    CreateUnusedOpticalSegments:bool
    """Read Write Property: If set to true, unused optical segments will be created. Used for trc, c3d files."""
    IgnoreModelType:bool
    """Read Write Property: If set to true, model type will not be considered when finding a matching model in the scene."""
    ImportDOF:bool
    """Read Write Property: If set to true, the DOF value will be imported from the file."""
    ImportScaling:bool
    """Read Write Property: If set to true, scaling values will be imported."""
    KeepActorPrefix:bool
    """Read Write Property: If set to true, the Actor prefix will be kept when naming each optical marker. Used with c3d files."""
    KeepDummyNode:bool
    """Read Write Property: If set to true, dummy bones from the file are not removed. Used for asf/amc files."""
    ModelSelection:FBModelSelection
    """Common settings when merging, unused with the CreateInsteadOfMerge property is set to true."""
    SetLimits:bool
    """Read Write Property: If set to true, use motion limits. Used for asf/amc files."""
    SetOccludedToLastValidPosition:bool
    """Read Write Property: If set to true, occluded segments will be set to their last valid position. Used for trc, c3d files."""
    TakeStartEnd:FBTakeSpanOnLoad
    """Read Write Property: Indicates how the start/end value of the take will be modified."""
    UpAxisUsedInFile:FBUpAxis
    """Read Write Property: Indicated the up axis used in the motion file. Only effective when loading c3d files."""
    def GetTakeCount(self)->int:
        """Return the take count in the file to be loaded.
        
        return : Take count"""
        ...
    def GetTakeName(self,TakeIndex:int)->str:
        """Get the take name.
        
        TakeIndex : Index of take to get the name.
        return : Take name"""
        ...
    def GetTakeSamples(self,TakeIndex:int)->int:
        """Return the number of samples.
        
        TakeIndex : Index of take to get the samples count.
        return : Number of samples"""
        ...
    def GetTakeSamplingRate(self,TakeIndex:int)->float:
        """Return the actual sampling rate as a double, useful when you have a custom sampling rate.
        
        TakeIndex : Index of take to get the sampling rate
        return : Sample rate"""
        ...
    def GetTakeSamplingRateMode(self,TakeIndex:int)->FBTimeMode:
        """Return the sampling rate mode.
        
        TakeIndex : Index of take to get the sampling rate mode
        return : Sample rate mode"""
        ...
    def GetTakeSelect(self,TakeIndex:int)->bool:
        """Return true if the take will be loaded.
        
        TakeIndex : Index of take.
        return : True is the take will be loaded"""
        ...
    def GetTakeStart(self,TakeIndex:int)->FBTime:
        """Return the Take Start time.
        
        TakeIndex : Index of take to get the start time.
        return : Start time of the take"""
        ...
    def GetTakeStop(self,TakeIndex:int)->FBTime:
        """Return the Take Stop time.
        
        TakeIndex : Index of take to get the stop time.
        return : Stop time of the take"""
        ...
    def SetTakeName(self,TakeIndex:int,Name:str):
        """Set the take name.
        
        TakeIndex : Index of take to set.
        Name : Take name to set"""
        ...
    def SetTakeSamples(self,TakeIndex:int,SamplesCount:int):
        """Set the number of samples for a particular take.
        
        TakeIndex : Index of take to set.
        SamplesCount : Number of samples"""
        ...
    def SetTakeSamplingRate(self,TakeIndex:int,TimeMode:FBTimeMode,CustomSamplingRate:float=30.0):
        """Set the sampling rate for a particular take.
        
        TakeIndex : Index of take to set.
        TimeMode : Time mode to set.
        CustomSamplingRate : Custom sampling rate ifTimeMode is set to kFBTimeModeCustom, unused otherwise (default is 30.0)"""
        ...
    def SetTakeSelect(self,TakeIndex:int,Select:bool):
        """Indicate if the take will be loaded.
        
        TakeIndex : Index of take to set.
        Select : Set to true if the take should be loaded."""
        ...
    def SetTakeStart(self,TakeIndex:int,StartTime:FBTime):
        """Set the Take Start time.
        
        TakeIndex : Index of take to set.
        StartTime : Time of the first frame of the take"""
        ...
    def SetTakeStop(self,TakeIndex:int,StopTime:FBTime):
        """Set the Take Stop time.
        
        TakeIndex : Index of take to set.
        StopTime : Time of the last frame of the take"""
        ...
class FBNamespace(FBComponent):
    """Objects Containing class.
    This class is an interface to manipulate object's containing in the scene."""
    ChildrenNamespaces:FBPropertyListNamespace
    """List: Direct Children Namespace Objects."""
    ContentCount:property
    ContentLocked:bool
    """Read Write Property: Content locking state."""
    def GetContent(self,Index:int)->FBComponent:
        """Get the namespace content object count (Not Recursive).
        
        Index : content object index to query. return content object inside this namespace (not recursive)"""
        ...
    def GetContentCount(self)->int:
        """Get the namespace content objects count (Not Recursive).
        return content objects count inside this namespace (not recursive)"""
        ...
    def GetContentList(self,ContentList:FBComponentList,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,Recursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,ExactTypeMatch:bool=False):
        """Get List of the namespace content.
        
        ContentList : the list of content to return.
        ModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBAllContent means all the content.
        Recursive : True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        TypeInfo : the typeInfo of the type of interested object, 0 for all the objects.
        ExactTypeMatch : if True, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo)."""
        ...
class FBOpticalGap(FBComponent):
    """Optical Gap class."""
    Data:FBAnimationNode
    """Property: Gap curve data."""
    Interpolation:FBGapMode
    """Property: Gap mode."""
    TimeSpan:FBTimeSpan
    """Property: Current timespan."""
    def InsertControlKey(self,Time:FBTime):
        """Insert a control key for the gap.
        
        Time : Insert time for the control key."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        
        return : true if segment is valid."""
        ...
class FBFileReference(FBNamespace):
    """Objects Containing class.
    This class is an interface to manipulate object's containing in the scene. See sample: MBFileRefDemo.py."""
    IsLoaded:bool
    """Read Write Property:  File Reference Load/Unload."""
    ReferenceFilePath:str
    """Read Write Property:  File Reference file path."""
    def ApplyRefEditPyScriptFromFile(self,RefEditPyScriptFilePath:str):
        """Apply specified reference edits from python script file.
        
        RefEditPyScriptFilePath : Reference edits Python script file path."""
        ...
    def ApplyRefEditPyScriptFromString(self,RefEditPyScript:str):
        """Apply specified reference edits from Python script string.
        
        RefEditPyScript : Reference edits Python script."""
        ...
    def BakeRefEditToFile(self,FilePath:str=None)->bool:
        """Save the current status of the referenced content back to disk.
        IfFilePath is ReferenceFilePath, we're saving all the modification back to the original referenced file. Otherwise, we will export the referenced file plus modification to another file.
        
        FilePath : File path to export.
        return : true if successful."""
        ...
    def ClearAllRefEdit(self)->bool:
        """Clear all cached Ref edit.
        
        return : True if the RefEdits are cleared properly."""
        ...
    def ClearRefEdit(self,FilePath:str)->bool:
        """Clear the cached RefEdit for the given ref file path.
        
        FilePath : The Ref File Path to query against, default to be current Ref File.
        return : True if the RefEdit for the given Ref File Path is cached and cleared properly."""
        ...
    def DuplicateFileRef(self,DstNameSpaceList:FBStringList,WithRefEdit:bool=False)->bool:
        """Duplicate/Clone the FileRef object and its referenced content (with/without refEdit).
        
        DstNameSpaceList : the list of target new namespace(s) for duplication. These new namespace(s) must be residing in editable scene segments.
        WithRefEdit : false by default, duplication won't include the existing ref edit. otherwise ref edit will be applied on the instantiated FileRef in someway.
        return : true if successful, false is fail."""
        ...
    def GetRefEdit(self,FilePath:str=None)->str:
        """Return the RefEdit for given RefFile Path.
        
        FilePath : The Ref File Path to query against, default to be current Ref File.
        return : RefEdit as string"""
        ...
    def GetRefFileList(self,RefFileList:FBStringList):
        """Return a list of ref file path which has cached Ref Edit.
        
        RefFileList : the output parameter to collect the Ref File Path."""
        ...
    def RevertRefEdit(self,Plug:FBPlug=None,ModificationFlag:FBPlugModificationFlag=FBPlugModificationFlag.kFBAllModifiedMask):
        """Revert the modification on the referenced object/property to original state.
        
        Plug : the plug to revert, revert all if NULL.
        ModificationFlag : the modification type to revert."""
        ...
    def SwapReferenceFilePath(self,FilePath:str,ApplyAvailableRefEdit:bool=True,MergeCurrentRefEdit:bool=True)->bool:
        """Swap the Ref File Path and apply ref edit.
        
        FilePath : The new Ref File path to be used
        ApplyAvailableRefEdit : Apply the cached Ref Edit (if exist) for the Ref File to be used if True.
        MergeCurrentRefEdit : Merge the current RefEdit to if True if the reference items' name are matching.
        return : True if swap successfully."""
        ...
class FBOpticalSegment(FBComponent):
    """Optical segment class."""
    Data:FBAnimationNode
    """Property: Segment curve data."""
    Marker:FBModelMarkerOptical
    """Property: Optical marker."""
    MarkerTimeSpan:FBTimeSpan
    """Property: Marker/Segment timespan."""
    OriginalTimeSpan:FBTimeSpan
    """Property: Original timespan for segment."""
    TimeSpan:FBTimeSpan
    """Property: Current segment timespan."""
    Used:bool
    """Property: Is segment used?"""
    def Cut(self,Time:FBTime):
        """Cut the segment for the marker at a given time.
        
        Time : Time to cut segment at."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        
        return : true if segment is valid."""
        ...
    def Reset(self):
        """Reset the marker segment."""
        ...
class FBPlayerControl(FBComponent):
    """Player control.
    Interface to use the transport controls (play, stop, etc.) The following Python snippet shows its basic playback operation
    
    >>> lPlayer = FBPlayerControl()
    lPlayer.GotoStart()
    lPlayer.Play()
    
    
    Keys can also be set and used with Key(), GotoNextKey(), and GotoPreviousKey(). All actions are performed by default on the current take. The is the MotionBuilder default take, unless you have multiple takes in your scene. To switch between takes, use FBTake. See samples: ShotTrackSetupTool.py, RenderLayers.py, CameraSwitcher.py, BloopSlate.py, RecordLight.py, Timeline.py, CreateProfilingEventsLog.py, MirrorPoseOverTime.py, MultiLayerKeying.py, StartDevice.py, StopDevice.py, TimeCodeKeying.py."""
    IsPlaying:bool
    """Read Only Property: Is the transport control playing?"""
    IsPlotting:bool
    """Read Only Property: Is there a plotting in progress?"""
    IsRecording:bool
    """Read Only Property: Is there a recording in progress?"""
    LoopActive:bool
    """Read Write Property: Is looping active? Deprecated, use the LoopMode property instead."""
    LoopMode:FBTransportLoopMode
    """Read Write Property: Loop mode."""
    LoopStart:FBTime
    """Read Write Property: Loop begin time."""
    LoopStop:FBTime
    """Read Write Property: Loop end time."""
    NextMarker:FBTime
    """Read Only Property: Next marked time."""
    OnChange:FBEvent
    """Event Property: Fired when something in the player control has changed. (see FBEventPlayerControlChange)"""
    PlotSamplingPeriod:FBTime
    """Read Write Property: Sampling period for the model plotting."""
    PreviousMarker:FBTime
    """Read Only Property: Previous marked time."""
    RecordingSamplingPeriod:FBTime
    """Read Write Property: Sampling period for the model recording."""
    SnapMode:FBTransportSnapMode
    """Read Write Property: Set the transport control snap mode."""
    TransportTimeFormat:FBTransportTimeFormat
    """Read Write Property: Current Time Mode of the transport controls."""
    ZoomWindowStart:FBTime
    """Read Write Property: Starting time of the transport control zoom window."""
    ZoomWindowStop:FBTime
    """Read Write Property: Stopping time of the transport control zoom window."""
    def AddGlobalTimeMark(self,Time:FBTime)->int:
        """Add a global time mark.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the global time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.
        
        Time : Time where to add the time mark.
        Name : Name of the time mark to add.
        return : The index of the time mark added if the operation is successful, -1 otherwise."""
        ...
    def DeleteAllGlobalTimeMarks(self):
        """Delete all global time marks."""
        ...
    def DeleteGlobalTimeMark(self,Index:int)->bool:
        """Delete a global time mark.
        Note: Internally, the global time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.
        
        Index : Index of the time mark to delete.
        return : True if the operation is successful, false otherwise."""
        ...
    def EvaluationPause(self):
        """Pause device evaluation thread."""
        ...
    def EvaluationResume(self):
        """Resume device evaluation thread."""
        ...
    def GetEditCurrentTime(self)->FBTime:
        """Get Edit Current Time.
        
        return : The current time, in the edit time referential."""
        ...
    def GetEditStart(self)->FBTime:
        """Get Edit Start.
        
        return : Start value for the edit time range."""
        ...
    def GetEditStop(self)->FBTime:
        """Get Edit Stop.
        
        return : Stop value for the edit time range."""
        ...
    def GetEditZoomStart(self)->FBTime:
        """Get Edit Zoom Start.
        
        return : Start value for the edit zoom window."""
        ...
    def GetEditZoomStop(self)->FBTime:
        """Get Edit Zoom Stop.
        
        return : Stop value for the edit zoom window."""
        ...
    def GetGlobalTimeMarkAction(self,Index:int)->FBTimeMarkAction:
        """Returns the action associated with a global time mark.
        
        Index : Index of the time mark.
        return : The action associated with the time mark."""
        ...
    def GetGlobalTimeMarkColor(self,Index:int)->FBColor:
        """Returns the color associated with a global time mark.
        
        Index : Index of the time mark.
        return : The color associated with the time mark."""
        ...
    def GetGlobalTimeMarkCount(self)->int:
        """Returns the number of global time marks.
        
        return : The number of global time marks."""
        ...
    def GetGlobalTimeMarkName(self,Index:int)->str:
        """Returns the name associated with a global time mark.
        
        Index : Index of the time mark.
        return : The name associated with the time mark."""
        ...
    def GetGlobalTimeMarkTime(self,Index:int)->FBTime:
        """Returns the time associated with a global time mark.
        
        Index : Index of the time mark.
        return : The time associated with the time mark."""
        ...
    def GetNextGlobalTimeMarkIndex(self)->int:
        """Returns the next global time mark index, based on the current local time.
        
        return : The next global time mark index, -1 if any next time mark is available."""
        ...
    def GetPlaySpeed(self)->float:
        """Get Play Speed .
        
        return : transport current playback speed."""
        ...
    def GetPlaySpeedMode(self)->FBTransportPlaySpeed:
        """Get Play Speed Mode.
        
        return : transport current playback speed mode, including kFBSpeed_Custom mode."""
        ...
    def GetPreviousGlobalTimeMarkIndex(self)->int:
        """Returns the previous global time mark index, based on the current local time.
        
        return : The previous global time mark index, -1 if any previous time mark is available."""
        ...
    def GetTimeReferential(self)->FBTimeReferential:
        """Get Time Referential.
        
        return : Current time referential."""
        ...
    def GetTransportFps(self)->FBTimeMode:
        """Get the UI frame rate use for display configure in the system.
        
        return : current FrameRate selected for the system."""
        ...
    def GetTransportFpsValue(self,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault)->float:
        """Get the UI frame rate value.
        
        TimeMode : the time mode whose frame rate will be returned
        return : Frame rate of the input time mode or system time mode whenTimeMode is not provided."""
        ...
    def GetTransportMode(self)->FBTransportMode:
        """Get Transport Mode.
        
        return : Current mode of the transport controls."""
        ...
    def Goto(self,p0:FBTime,p1:FBTimeReferential)->bool:
        """Goto a time specified byTime.
        
        p0 : Time to jump to.
        p1 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit
        return : true if successful."""
        ...
    def GotoEnd(self,p0:FBTimeReferential)->bool:
        """GotoEnd button (FastForward).
        
        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit
        return : true if successful."""
        ...
    def GotoNextKey(self):
        """Go to the next key."""
        ...
    def GotoPreviousKey(self):
        """Go to the previous key."""
        ...
    def GotoStart(self,p0:FBTimeReferential)->bool:
        """GotoStart button (Rewind).
        
        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit
        return : true if successful."""
        ...
    def IsLocked(self)->bool:
        """Return the current locking state of the transport."""
        ...
    def Key(self):
        """Key default data.
        Key all selected data."""
        ...
    def LockTransport(self,Lock:bool):
        """Lock the transport control.
        
        Lock : boolean value that indicates the new locked state of the transport."""
        ...
    def Play(self,UseMarkers:bool=False)->bool:
        """Play button.
        
        UseMarkers : Play until next marker if true, ignore markers otherwise.
        return : true if successful."""
        ...
    def PlayReverse(self,UseMarkers:bool=False)->bool:
        """Play Reverse button.
        
        UseMarkers : Play until next marker if true, ignore markers otherwise.
        return : true if successful."""
        ...
    def Record(self,OverrideTake:bool=False,CopyData:bool=True)->bool:
        """Begin recording.
        
        OverrideTake : Write over current take?(default=false)
        CopyData : Unused. Necessary for compatibility(default=true).
        return : true if successful."""
        ...
    def SetEditStart(self,Time:FBTime):
        """Set Edit Start.
        
        Time : The new start value for the edit time range."""
        ...
    def SetEditStop(self,Time:FBTime):
        """Set Edit Stop.
        
        Time : The new stop value for the edit time range."""
        ...
    def SetEditZoomStart(self,Time:FBTime):
        """Set Edit Zoom Start.
        
        Time : The new start value for the edit zoom window."""
        ...
    def SetEditZoomStop(self,Time:FBTime):
        """Set Edit Zoom Stop.
        
        Time : The new stop value for the edit zoom window."""
        ...
    def SetGlobalTimeMarkAction(self,Index:int,Action:FBTimeMarkAction)->bool:
        """Sets a new action for an existing global time mark.
        
        Index : Index of the time mark.
        Action : The new action for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkColor(self,Index:int,Color:FBColor)->bool:
        """Sets a new color for an existing global time mark.
        
        Index : Index of the time mark.
        Color : The new color for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkName(self,Index:int,Name:str)->bool:
        """Sets a new name for an existing global time mark.
        
        Index : Index of the time mark.
        Name : The new name for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetGlobalTimeMarkTime(self,Index:int,Time:FBTime)->int:
        """Sets a new time for an existing global time mark.
        Note: Internally, the global time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.
        
        Index : Index of the time mark.
        Time : The new time for the time mark.
        return : The new index of the modified time mark."""
        ...
    def SetPlaySpeed(self,Speed:float):
        """Set Play Speed.
        
        Speed : set customized speed. It will automatically convert to one of pre-defined play speed mode if it is equal to the pre-defined speed."""
        ...
    def SetPlaySpeedMode(self,PlaySpeedMode:FBTransportPlaySpeed):
        """Set Play Speed Mode.
        
        PlaySpeedMode : a pre-defined play speed mode. Don't make sense to input kFBSpeed_Custom. To set the custom speed, use SetPlaySpeed() function directly."""
        ...
    def SetTimeReferential(self,TimeReferential:FBTimeReferential):
        """Set Time Referential.
        
        TimeReferential : The new time referential. Only kFBTimeReferentialAction and kFBTimeReferentialEdit are supported"""
        ...
    def SetTransportFps(self,TimeMode:FBTimeMode,Custom:float=0.0):
        """Set the system frame rate use for display.
        
        TimeMode : Indicate the frame rate value to use base on the FBTimeMode values enum.(kFBTimeModeDefault will be stored in fps)
        Custom : Should the time mode be kFBTimeModeCustom, this is used to specify the custom framerate."""
        ...
    def StepBackward(self,p0:FBTimeReferential)->bool:
        """Step one frame backward.
        
        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit
        return : true if successful."""
        ...
    def StepForward(self,p0:FBTimeReferential)->bool:
        """Step one frame ahead.
        
        p0 : Time referential to use. kFBTimeReferentialAction or kFBTimeReferentialEdit
        return : true if successful."""
        ...
    def Stop(self)->bool:
        """Stop button.
        
        return : true if successful."""
        ...
class FBPointCacheFile(FBComponent):
    """Base Model deformer class."""
    CacheFileName:str
    """Read Write Property: Filename of media."""
    ChannelCount:int
    """Read Only Property: Channel Count."""
    FreeRunning:bool
    """Read Write Property: Free Running."""
    Loop:bool
    """Read Write Property: Loop."""
    Offset:FBTime
    """Read Write Property: Offset."""
    PlaySpeed:float
    """Read Write Property: Play Speed."""
    StartTime:FBTime
    """Read Write Property: Start Time."""
    StopTime:FBTime
    """Read Write Property: Stop Time."""
class FBRendererCallback(FBComponent):
    """Open Reality renderer callback interface."""
    DefaultCameraBackPlateRendering:bool
    """Read write Property: Set true to use default camera back plate rendering; set false to disable it."""
    DefaultCameraFrontPlateRendering:bool
    """Read write Property: Set true to use default camera front plate rendering; set false to disable it."""
    DefaultLightGroundProjectionRendering:bool
    """Read write Property: Set true to use default light ground projection rendering; set false to disable it."""
    DefaultLightVolumeRendering:bool
    """Read write Property: Set true to use default light volume rendering; set false to disable it."""
    SupportIDBufferPicking:bool
    """Read write Property: Can this Renderer Callback support IDBuffer Picking."""
class FBRigidBody(FBComponent):
    """Rigid body class."""
    Done:bool
    """Property: Done?"""
    Markers:FBPropertyListRigidBodyMarkers
    """Property: List of markers composing the rigid body."""
    Mode:FBRigidBodyMode
    """Property: Rigid body mode."""
    Model:FBModel
    """Property: Rigid body model."""
    QualityData:FBAnimationNode
    """Property: Quality of rigid body."""
    SmoothWidth:int
    """Property: Smoothing width."""
    def ComputeAnimation(self):
        """Compute the rigid body animation."""
        ...
    def IsValid(self)->bool:
        """Check if valid (if item exists).
        
        return : true if segment is valid."""
        ...
    def Snap(self):
        """Snap the rigid body."""
        ...
class FBSVector():
    """Three dimensional scaling vector.
    See sample: Vectors.py."""
    def CopyFrom(self,arg2:FBSVector)->FBSVector:...
    def DotProduct(self,arg2:FBSVector)->float:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBSVector)->bool:...
    def Length(self)->float:...
    def Normalize(self)->FBSVector:...
    def NotEqual(self,arg2:FBSVector)->bool:...
    def SquareLength(self)->float:...
class FBScene(FBComponent):
    """Access to the MotionBuilder scene.
    In MotionBuilder, the scene is the environment where your models exist. The scene contains models which you can import, select, transform, copy, tweak, and animate.The FBScene object is obtained from the scene attribute of FBSystem.The FBScene class contains many attributes that you can use to access objects, e.g cameras, characters, lights, and takes, essentially everything you see in the Navigator in the UI. A project can only contain one scene, and if you try to create an instance of a scene you will get an error, so you must access the scene by getting a handle through FBSystem.
    
    >>> myScene = FBSystem().Scene
    
    
    See also the C++ code sample in toolscene. See samples: InsertCurrentTake.py, DeleteUnusedMedia.py, MirrorPoseOverTime.py, SelectModelsWithNameContainingSubstring.py, SetAllCamerasBackgroundColorFromFirstSelectedCamera.py, StartDevice.py."""
    ActorFaces:FBPropertyListActorFace
    """List: ActorFaces in scene."""
    Actors:FBPropertyListActor
    """List: Actors in scene."""
    AudioClips:FBPropertyListAudioClip
    """List: Audio clips in scene."""
    Cameras:FBPropertyListCamera
    """List: Cameras in scene."""
    CharacterExtensions:FBPropertyListCharacterExtension
    """List: Character extensions available in the scene."""
    CharacterFaces:FBPropertyListCharacterFace
    """List: Character faces in scene."""
    CharacterMarkerSets:FBPropertyListCharacterMarkerSet
    """List: Character marker sets in scene."""
    CharacterPoses:FBPropertyListCharacterPose
    """List: Character poses in scene."""
    Characters:FBPropertyListCharacter
    """List: Characters in scene."""
    ConstraintSolvers:FBPropertyListConstraintSolver
    """List: Constraint Solvers present in the scene."""
    Constraints:FBPropertyListConstraint
    """List: Constraints in scene."""
    ControlSets:FBPropertyListControlSet
    """List: Control set rigs in scene."""
    Deformers:FBPropertyListDeformer
    """List: Deformers for scene."""
    Devices:FBPropertyListDevice
    """List: Devices for scene."""
    FileReferences:FBPropertyListFileReference
    """List: FileReference available in the scene."""
    Folders:FBPropertyListFolder
    """List: Folders in scene."""
    Groups:FBPropertyListGroup
    """List: Groups available in the scene."""
    HUDs:FBPropertyListHUD
    """Read Only Property: Heads Up Displays in the scene."""
    Handles:FBPropertyListHandle
    """List: Handles present in the scene."""
    KeyingGroups:FBPropertyListKeyingGroup
    """Read Write Property: Keying Groups in the scene."""
    Lights:FBPropertyListLight
    """List: Lights in scene."""
    MarkerSets:FBPropertyListMarkerSet
    """List: Marker sets in scene."""
    Materials:FBPropertyListMaterial
    """List: Materials for scene."""
    ModelOpticals:FBPropertyListModelOptical
    """Read Write Property: Optical Data in the scene."""
    ModelSkeletons:FBPropertyListModelSkeleton
    """Read Write Property: Bones (Skeletons) in the scene."""
    MotionClips:FBPropertyListMotionClip
    """List: Motion clips in scene."""
    Namespaces:FBPropertyListNamespace
    """List: Namespace (include FileReference) available in the scene"""
    Notes:FBPropertyListNote
    """List: Notes in scene."""
    ObjectPoses:FBPropertyListObjectPose
    """List: ObjectPoses in scene."""
    OnChange:FBEvent
    """Event: Something in the scene has happened.(FBEventSceneChange)"""
    OnTakeChange:FBEvent
    """Event: Something related to a take has happened.(FBEventTakeChange)"""
    PhysicalProperties:FBPropertyListPhysicalProperties
    """List: PhysicalProperties present in the scene."""
    Poses:FBPropertyListPose
    """List: Poses in scene."""
    Renderer:FBRenderer
    """Read Only Property: Local renderer."""
    RootModel:FBModel
    """Read Only Property: Scene Root model for that scene"""
    Sets:FBPropertyListSet
    """List: Sets available in the scene."""
    Shaders:FBPropertyListShader
    """List: Shaders for scene."""
    Takes:FBPropertyListTake
    """List: Takes for scene."""
    Textures:FBPropertyListTexture
    """List: Textures for scene."""
    UserObjects:FBPropertyListUserObject
    """List: User objects"""
    VideoClips:FBPropertyListVideoClip
    """List: Video clips in scene."""
    def CandidateEvaluationAndResolve(self)->bool:
        """Resolving the Candidate.
        
        return : true if successful."""
        ...
    def CleanEmptyGroups(self)->int:
        """Remove all empty groups present in the scene.
        
        return : The number of empty groups removed."""
        ...
    def CleanEmptyRelationConstraints(self)->int:
        """Remove all empty relation constraints present in the scene.
        
        return : The number of empty relation constraints removed."""
        ...
    def CleanEmptySets(self)->int:
        """Remove all empty sets present in the scene.
        
        return : The number of empty sets removed."""
        ...
    def CleanInactiveConstraints(self)->int:
        """Remove all inactive constraints present in the scene.
        
        return : The number of inactive constraints removed."""
        ...
    def CleanRelationConstraintsUnusedBoxes(self)->int:
        """Remove all unused boxes in relations constraints present in the scene.
        
        return : The number of unused boxes in relations constraints removed."""
        ...
    def CleanUnusedAudioClips(self)->int:
        """Remove all unused audio clips present in the scene.
        
        return : The number of unused audio clips removed."""
        ...
    def CleanUnusedMaterials(self)->int:
        """Remove all unused materials present in the scene.
        
        return : The number of unused material removed."""
        ...
    def CleanUnusedShaders(self)->int:
        """Remove all unused shaders present in the scene.
        
        return : The number of unused shaders removed."""
        ...
    def CleanUnusedTextures(self)->int:
        """Remove all unused textures present in the scene.
        
        return : The number of unused textures removed."""
        ...
    def CleanUnusedVideoClips(self)->int:
        """Remove all unused video clips present in the scene.
        
        return : The number of unused video clips removed."""
        ...
    def Clear(self):
        """Clears the elements part of the scene.
        Not those that belong to all the scenes."""
        ...
    def Evaluate(self)->bool:
        """Evaluate the scene.
        
        return : true if successful."""
        ...
    def EvaluateDeformations(self)->bool:
        """Evaluate the deformations of the scene.
        
        return : true if successful."""
        ...
    def GetScriptsPaths(self)->FBStringList:
        """Get paths of all the python scripts object in the scene.
        
        PathList : Out parameter, to collect the path of python scripts."""
        ...
    def NamespaceCleanup(self)->bool:
        """Remove all empty namespaces.
        During some namespace operations, empty namespace may left over, while this is not harmful but could be annoying. Save the scene and load it back those empty namespaces will disappear. And this function also allow user to remove all empty namespaces from the scene easily via SDK.
        
        return : True if operation successfully."""
        ...
    def NamespaceDelete(self,Namespace:str)->bool:
        """Delete the namespace & all its content.
        
        Namespace : the namespace to work on
        return : True if operation successfully, False is this namespace doesn't exist, or is locked (by FileReferencing or etc.,)"""
        ...
    def NamespaceDeleteContent(self,Namespace:str,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,Recursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,ExactTypeMatch:bool=False)->bool:
        """Delete the namespace content.
        
        Namespace : the namespace to work on
        ModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        Recursive : True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        TypeInfo : the typeInfo of the type of interested object, default for all the objects.
        ExactTypeMatch : if True, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo).
        return : False is the given namespace doesn't exist, or is locked (by FileRef or etc.,), True otherwise."""
        ...
    def NamespaceEmpty(self,Namespace:str)->bool:
        """Query if namespace is empty.
        
        Namespace : the namespace to query, NULL for whole scene.
        return : True if the namespace (don't include nested children namespace) is empty"""
        ...
    def NamespaceExist(self,Namespace:str)->bool:
        """Query if namespace exists.
        
        Namespace : the namespace to query
        return : True if the namespace exist, otherwise return False."""
        ...
    def NamespaceExport(self,Namespace:str,FilePath:str,ASCIIFormat:bool=False)->bool:
        """Export scene content within namespace to file.
        
        Namespace : the namespace to use, must exist
        FilePath : the referenced file path to export.
        ASCIIFormat : save the file in ASCII format.
        return : True if successfully."""
        ...
    def NamespaceGet(self,Namespace:str)->FBNamespace:
        """Get Namespace object.
        
        Namespace : the namespace to query
        return : Namespace with exact name matching"""
        ...
    def NamespaceGetChildrenList(self,NamespaceList:FBStringList,Namespace:str=None,Recursive:bool=True)->int:
        """Get list of children namespaces in the given namespace.
        
        NamespaceList : the list of namespace to return.
        Namespace : specify the parent namespace, NULL for the whole scene.
        Recursive : True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        return : the list of children namespaces."""
        ...
    def NamespaceGetContentList(self,ContentList:FBComponentList,Namespace:str,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,Recursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,ExactTypeMatch:bool=False):
        """Get List of the namespace content.
        
        ContentList : the list of content to return.
        Namespace : the namespace to work on, NULL for whole scene.
        ModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        Recursive : True only work on the direct children level namespace, otherwise will work on the whole children namespace hierarchy recursively.
        TypeInfo : the typeInfo of the type of interested object, 0 for all the objects.
        ExactTypeMatch : if True, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo)."""
        ...
    def NamespaceGetOwnerFileReference(self,Namespace:str)->FBFileReference:
        """Get Owner FileReference object if the namespace is originated from File Reference.
        
        Namespace : the namespace to work on, could be nested namespace inside the FileReference's namespace.
        return : the FileReference object is the namespace is originated from. NULL otherwise."""
        ...
    def NamespaceImport(self,Namespace:str,FilePath:str,AsFileReference:bool=False)->bool:
        """Import file into Namespace (or as file reference)
        
        Namespace : the namespace to import to, must be in editable scope.
        FilePath : the referenced file path to import.
        AsFileReference : import the file as file reference. The default value is false.
        return : True if successfully."""
        ...
    def NamespaceImportToMultiple(self,DstNamespaceList:FBStringList,FilePath:str,AsFileReference:bool=False)->bool:
        """Import file into multiple Namespaces (or as file references)
        
        DstNamespaceList : the Dst namespaces list to import, must not exist or be self contained.
        FilePath : the referenced file path to import.
        AsFileReference : import the file as file reference. The default value is false.
        return : True if successfully."""
        ...
    def NamespaceRename(self,NameSpace:str,NewNamespace:str,Recursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,ExactTypeMatch:bool=False)->bool:
        """Rename the namespace.
        
        NameSpace : the namespace to work on, NULL for whole scene.
        NewNamespace : the new namespace
        Recursive : True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        TypeInfo : the typeInfo of the type of interested object, default for all the objects.
        ExactTypeMatch : if True, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo).
        return : True if operation successfully, False is this namespace (orTypeInfo type of objects) doesn't exist, or locked (by FileReferencing or etc.,)"""
        ...
    def NamespaceSelectContent(self,Namespace:str,Select:bool,ModificationFlags:FBPlugModificationFlag=FBPlugModificationFlag.kFBPlugAllContent,Recursive:bool=True,TypeInfo:int=FBPlug.TypeInfo,ExactTypeMatch:bool=False):
        """Select (or de-select) the namespace content.
        
        Namespace : the namespace to work on, NULL for whole scene.
        Select : True (or False) indicate to select (or de-select)
        ModificationFlags : bitwise combination of kFBConnectionSrcObjectModified, kFBConnectionDstObjectModified, kFBConnectionSrcPropertyModified, kFBConnectionDstPropertyModified flags. kFBPlugAllContent means all the content. Modification flags beside kFBPlugAllContent will only work on FileReference Namespace.
        Recursive : True only work on the direct children level namespace, otherwise will work on the children namespace hierarchy recursively.
        TypeInfo : the typeInfo of the type of interested object, default for all the objects.
        ExactTypeMatch : if True, the derived typeInfo won't be considered (For example, FBCamera won't be considered when passing FBModel::TypeInfo)."""
        ...
class FBSet(FBBox):
    """Objects Set class.
    This class is an interface to manipulate object sets in the scene. Note: an item cannot be in two FBSet objects at once. Also, an FBGroup cannot contain FBSet objects, although an FBSet object can contain an FBGRoup."""
    Items:FBPropertyListComponent
    """List: Items in the set."""
    Pickable:bool
    """Read Write Property: Controls if objects in the set are pickable."""
    Transformable:bool
    """Read Write Property: Controls if objects in the set are transformable."""
    Visibility:bool
    """Read Write Property: Visibility of set (animatable)."""
    def Contains(self,Component:FBComponent)->int:
        """Contains.
        
        Component : Component to verify if it is in the Group
        return : 0 if the component is not in the FBSet, 1 if it is in this FBSet, 2 if it is in another FBSet"""
        ...
    def Select(self,Select:bool):
        """Select.
        
        Select : If true, set contents will be selected."""
        ...
class FBShader(FBBox):
    """Shader class."""
    RenderingPass:FBRenderingPass
    """Read Write Property: Rendering pass object are shaded in."""
    ShaderDescription:str
    """Description."""
    def Append(self,Model:FBModel)->bool:
        """Append shader toModel.
        
        Model : Model to append shader to.
        return : True if the operation is successful, false otherwise."""
        ...
    def CloneShaderParameter(self,NewShader:FBShader):
        """Clone shader.
        
        NewShader : Shader to copy data to."""
        ...
    def ReplaceAll(self,Model:FBModel)->bool:
        """Replace all shader inModel.
        
        Model : Model to replace all shader to.
        return : True if the operation is successful, false otherwise."""
        ...
    def ShaderNeedBeginRender(self)->bool:
        """Does the shader need a begin render call."""
        ...
class FBShaderLighted(FBShader):
    """Lighted shader class.
    This type of shader is the default type used by the application. It allows users to control luminosity, contrast and specularity as well as how the transparency is computed, should it be used.There are two methods to create a FBShaderLighted object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code:
    
    >>> # Creation of a lighted shader, and setting it to use
    # the constrast and specularity.
    FBShaderLighted* lShader = new FBShaderLighted( 'New Shader' );
    lShader->UseContrast  = true;
    lShader->UseSpecular  = true;
    lShader->Specular     = 35.0;
    lShader->Transparency = kFBAlphaSourceTransluscentAlpha;
    # Use the shader.
    FBModel* lModel = FBFindModelByLabelName( 'Cube' );
    if( lModel )
    {
    lShader->ReplaceAll( lModel );
    }
    # Do some more things...
    # And then delete it when no longer necessary;
    lShader->FBDelete();
    
    
    The following sample code does the same task, but in Python.Sample Python code:
    
    >>> from pyfbsdk import *
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
    lShader.ReplaceAll( lModel )"""
    Alpha:float
    """Read Write Property: Controls the actual effect of the shader on the object. At 0.0 it does nothing, and at 1.0 it fully affects the object."""
    Contrast:float
    """Read Write Property: Changes the contrast of the object when it reflects light."""
    Luminosity:float
    """Read Write Property: Changes the brightness of the object when reflecting light."""
    Specular:float
    """Read Write Property: Changes an object's level of shininess when it reflects light by affecting the specular highlight."""
    Transparency:FBAlphaSource
    """Read Write Property: Indicates the computation method of the transparency."""
    UseContrast:bool
    """Read Write Property: Activate the Contrast option."""
    UseLuminosity:bool
    """Read Write Property: Activate the Luminosity option."""
    UseSpecular:bool
    """Read Write Property: Activate the Specularity option."""
class FBShaderManager():
    """Shader manager.
    This class provides access to the list of available shaders, both system shaders and user shaders. The list comes in two versions:ShaderTypeNames : which gives the internal names of the shaders,ShaderTypeNamesLocalized : uses the GUI names of the shaders.Both of these lists will have the same number of elements. The strings at position i in the lists refer to the same shader type. In cases where there is no localized version of the shader name, the internal name will be used in ShaderTypeNamesLocalized, thus ensuring consistency between the two lists.It also provides a generic shader creation method that uses the shader type name, internal or localized, to create the new shader instance.The destruction of shaders is achieved by calling the FBDelete method of a shader instance.The list of all the instantiated shaders can be obtained from instances of classes FBSystem or FBScene. Both classes have a Shaders property which lists the existing shader instances.Strings are used instead of enum, define or typedef values to refer to shader types as this proves to be more flexible.The system has a default shader of type 'Lighted'. Do not attempt to destroy it.The use of localized names in shader creation is non portable as it is dependent of the current language used by the application. The name may also change from one version to another. Using the internal name is the only way to ensure portable shader creation.Sample C++ code:
    
    >>> # This could be a constant value in the code, coming from a custom
    # registry or simply coming from one of the list ShaderTypeNames
    # or ShaderTypeNamesLocalized.
    const char* lDesiredShaderTypeName = 'MyShader';
    # Shader creation.
    FBShader* lShader = NULL;
    FBShaderManager lShaderManager;
    if( lShaderManager.ShaderTypeNames.Find( lDesiredShaderTypeName ) != -1 ||
    lShaderManager.ShaderTypeNamesLocalized.Find( lDesiredShaderTypeName ) != -1 )
    {
    lShader = lShaderManager.CreateShader( lDesiredShaderTypeName );
    # Change its name, as the default name will be the type name.
    if( lShader )
    {
    lShader->Name = 'My new shader';
    }
    else
    {
    # Warn about creation failure on a correctly registered
    # shader type.
    }
    }
    else
    {
    # Warn about an unknown shader type.
    }
    #
    # Do some work with the shader...
    #
    if( lShader )
    {
    lShader->FBDelete();
    }
    
    
    In the previous code sample, the lookup in the manager list is not necessary, as the call to CreateShader would have failed nonetheless and returned a NULL pointer.Sample Python code:
    
    >>> from pyfbsdk import *
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
    
    
    See sample: VertexArrayManipulation.py."""
    ShaderTypeNames:FBStringList
    """List of available shaders."""
    ShaderTypeNamesLocalized:FBStringList
    """List of available shaders."""
    def CreateShader(self,ShaderTypeName:str)->FBShader:
        """Creates a shader according to the shader type provided.
        This method provides a generic way of creating shaders using the type name, internal or localized. The name of the new shader will be the same as the type name used, subject to changes according to the system's unique name policy.
        
        ShaderTypeName : Name of the type of shader desired.
        return : A pointer to the newly created shader object, or a NULL pointer if the type name was not recognised."""
        ...
class FBShaderModelInfo():
    Model:property
    """Read Write Property: Shader mModel"""
    Model_Version:property
    """Read Write Property: Shader version informations"""
    Shader_Version:property
class FBShaderShadowLive(FBShader):
    """Shader Shadow Live class.
    Use the Live Shadow shader to apply real-time shadows to models. You can specify shadow intensity as well as the lights and objects that cast shadows in a scene.There are two methods to create a FBShaderShadowLive object: using the FBShaderManager, or simply by instantiating a class object explicitely.Please consult the application documentation for more infos on shader properties and their effects.This class should not serve as a base class for another class.Sample C++ code:
    
    >>> # Create a shadow shader.
    FBShaderShadowLive* lShader = new FBShaderShadowLive( 'New Shader' );
    # Add a cube in its list of affected objects.
    FBModel* lModel = FBFindModelByLabelName( 'Cube' )
    if( lModel )
    {
    lShaderShadowLive.Add( lCube );
    }
    
    
    Sample Python code:
    
    >>> from pyfbsdk import *
    # Create shader.
    lShader = FBShaderShadowLive( 'New Python Shader' )
    # Find a cube to put in our list of affected objects.
    lModel = FBFindModelByLabelName( 'Cube' )
    if lModel:
    lShader.ShadowCasterProperty.append( lModel )"""
    Lights:FBPropertyListObject
    """List: List of light object which will produce shadows."""
    LocalShadow:bool
    """Read Write Property: Creates an accurate projection of a shadow for each object."""
    Models:FBPropertyListObject
    """List: List of object which when lighted will cast a shadow."""
    ShadowFrameType:FBShadowFrameType
    """Read Write Property: Used to select the shadow calculation method."""
    ShadowIntensity:float
    """Read Write Property: Controls the darkness of shadows cast by a selected object."""
    ShadowType:FBShadowType
    """Read Write Property: Indicate which shadow type is desired."""
    ShadowZOffset:float
    """Read Write Property: Specifies the offset of the Live Shadow shader's plane from the original selected plane."""
    UseGobo:bool
    """Read Write Property: Includes the gobo in the shadow map calculation."""
class FBSkeletonState():
    def GetNodeMatrix(self,SkeletonId:FBSkeletonNodeId,SkeletonGlobalMatrix:FBMatrix):
        """Returned global matrix associated to the given Index.
        
        SkeletonId : Index of the skeleton Node
        SkeletonGlobalMatrix : returned global matrix of the index Given"""
        ...
class FBSpreadPart(FBComponent):
    """Spreadsheet part.
    Due to protected constructor, this can only be created by a child object."""
    Column:int
    """Read Only Property: Column number."""
    Enabled:bool
    """Read Write Property: Is SpreadPart enabled?"""
    Justify:FBTextJustify
    """Read Write Property: Text justification for SpreadPart"""
    ReadOnly:bool
    """Read Write Property: Is SpreadPart read-only?"""
    Row:int
    """Read Only Property: Row number."""
    Style:FBCellStyle
    """Read Write Property: Style of cell"""
class FBSpreadRow(FBSpreadPart):
    """Spreadsheet row."""
    Caption:str
    """Read Write Property: Caption to display with row."""
    Parent:property
    """Read Write Property: Parent of row (reference)."""
    RowSelected:bool
    """Read Write Property: Is row selected?"""
    def EditCaption(self)->bool:
        """Edit the row caption.
        This will initiate the UI edit of a row caption.
        
        return : Operation was successful (true or false)."""
        ...
    def Remove(self):
        """Remove (destroy) row."""
        ...
class FBSpreadColumn(FBSpreadPart):
    """Spreadsheet column."""
    Caption:str
    """Read Write Property: Caption of the column."""
    Width:int
    """Read Write Property: Column width."""
class FBSpreadCell(FBSpreadPart):
    """Spreadsheet cell."""
    ...
class FBStory(FBComponent):
    """Story Management class.
    This class serve as a management control for the Story global settings and members. See samples: CreateShotClip.py, InsertCurrentTake.py, BloopSlate.py, RecordLight.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py, PrintClipNamesAndStartStopFrames.py."""
    ClipsTextsVisible:bool
    """Read Write Property: If true, clips' texts are visible."""
    LockedShot:bool
    """Read Write Property: If true, shots will be locked (no time discontinuity)."""
    MaintainShotAndClipShotLengthsSynced:bool
    """Read Write Property: When working in time discontinuity, if true, shots and their corresponding shot clips will be kept in sync in regards of their lengths."""
    Mute:bool
    """Read Write Property: If true, the Story mode will be globally disabled."""
    NoneBlockingPostprocess:bool
    """Read Write Property: If true, record to disk will post process recorded data in low priority thread without affecting application performance. Clip in story will remain unloaded."""
    RecordToDisk:bool
    """Read Write Property: If true, record to story will record directly to disk."""
    RootEditFolder:FBStoryFolder
    """Read Only Property: Story's root edit folder"""
    RootFolder:FBStoryFolder
    """Read Only Property: Story's root folder"""
    SummaryClip:bool
    """Read Write Property: If true, summary clips for story folders will be created to help manipulating folder content."""
    def CleanEmptyTracksAndFolders(self)->int:
        """Remove all empty tracks and folders present in the Story Tool.
        
        return : The number of empty story tracks and/or folders removed."""
        ...
class FBStoryClip(FBComponent):
    """Story Clip class.
    Clips represents media, at a specific time, for a specific duration, in a track.Clip offset is depending on Traveling node and Traveling node function. First we compute clip transformation matrix, where scaling is always 1, 1, 1. Translation is in position of Traveling node at clip first frame. Rotation is based on vector from first to last frame position of Traveling node. On top of that we apply offset and expose that as Clip Offset T & R. When you change clip offset T or R we extract clip offset based on current clip transformation matrix. Clip transformation matrix can change when Traveling node change or Traveling node function change. See samples: AudioTrackSetupTool.py, VideoClip.py, PrintClipNamesAndStartStopFrames.py."""
    AudioClip:FBAudioClip
    """Read Only Property: The audio clip used by this StoryClip."""
    AutoLoop:bool
    """Read Write Property: If true, clip will automatically loop"""
    ClipAnimationPath:str
    """Read Write Property: Animation clip's file path"""
    ClipAudioPath:str
    """Read Write Property: Audio clip's file path"""
    ClipPitch:float
    """Read Write Property: The clip pitch value."""
    ClipVideoPath:str
    """Read Write Property: Video clip's file path"""
    Color:FBColor
    """Read Write Property: Color of the clip."""
    ConnectedToTake:bool
    """Read Write Property: When connected to current take, user can do updating from current take, but user can't edit clip animation by adding keys, only works for clips created by Insert Current Take."""
    CustomTimeWarp:FBAnimationNode
    """Read Only Property: Animation and Shot clip's custom TimeWarp FCurve."""
    FrameRate:float
    """Read Write Property: Frame rate value. Only effective when UseSystemFrameRate is false."""
    Ghost:bool
    """Read Write Property: Show ghosts"""
    GhostCustomTime:FBTime
    """Read Write Property: Custom time to display ghost, only applicable if ShowGhostClipMode is kFBStoryClipTimeCustom."""
    GhostManipulatorCustomTime:FBTime
    """Read Write Property: Custom time to display ghost manipulator, only applicable if GhostManipulatorMode is kFBStoryClipGhostCustom."""
    GhostManipulatorMode:FBStoryClipGhostTimeMode
    """Read Write Property: Time mode to display ghost manipulator. See FBStoryClipGhostTimeMode."""
    GhostManipulatorOffset:FBVector3d
    """Read Write Property: Animation clip's ghost manipulator offset."""
    GhostModel:bool
    """Read Write Property: Show ghost of models"""
    GhostPivot:bool
    """Read Write Property: Show ghost of match object"""
    GhostTravelling:bool
    """Read Write Property: Show ghost of clip vector or traveling node"""
    ImageSequence:bool
    """Read Write Property: Whether is a image sequence."""
    Loaded:bool
    """Read Write Property: If true, clip file is loaded into memory and can be evaluated (will affect track content)."""
    LockPitchToSpeed:bool
    """Read Write Property: Time-stretching enabled or not."""
    Loop:bool
    """Read Write Property: If true, loop clip's animation"""
    LoopTranslation:FBVector3d
    """Read Write Property: Animation clip's loop translation."""
    MarkIn:FBTime
    """Read Write Property: Start time inside the clip."""
    MarkOut:FBTime
    """Read Write Property: Stop time inside the clip."""
    MirrorAnimation:bool
    """Read Write Property: If true, clip animation will be mirrored"""
    MirrorPlane:FBStoryClipMirrorPlane
    """Read Write Property: Several mirror planes to mirror animation. See FBStoryClipMirrorPlane"""
    Offset:FBTime
    """Read Write Property: First loop time offset."""
    OnChange:FBEvent
    """Event: Something in the clip has changed. (FBEventClip)"""
    Pivots:FBPropertyListPivot
    """List: Pivots models (Generally, only one model is necessary)"""
    PostBlend:FBTimeSpan
    """Read Write Property: Start/Stop time of the post-blend phase."""
    PreBlend:FBTimeSpan
    """Read Write Property: Start/Stop time of the pre-blend phase."""
    Rotation:FBVector3d
    """Read Write Property: Animation clip's rotation offset. Refer to class notes to learn more about how this is applied."""
    Scale:float
    """Read Write Property: Animation clip's scaling (some don't support this property)"""
    ShotActionStart:FBTime
    """Read Write Property: If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property."""
    ShotActionStop:FBTime
    """Read Write Property: If not in locked shot mode (time discontinuity enabled), this time can be different from the Clip->Start property."""
    ShotBackplate:FBVideo
    """Read Write Property: The backplate used for that specific shot."""
    ShotCamera:FBCamera
    """Read Write Property: The camera used for that specific shot."""
    ShotFrontplate:FBVideo
    """Read Write Property: The frontplate used for that specific shot."""
    ShotStartStopLocked:bool
    """Read Write Property: Shot clip's 'In/Out Locked' property value. True if the shot clip's In/Out properties (start/stop times of the clip local to its track) are locked, false otherwise."""
    ShowBackplate:bool
    """Read Write Property: Enable/Disable the shot backplate."""
    ShowEmbeddedTimecode:bool
    """Read Write Property: Whether to show embedded timecode of the clip, if available."""
    ShowFrontplate:bool
    """Read Write Property: Enable/Disable the shot frontplate."""
    ShowGhostClipMode:FBStoryClipShowGhostMode
    """Read Write Property: Show the ghost depending on the time. See FBStoryClipShowGhostMode"""
    SolvingMode:FBStoryClipSolveMode
    """Read Write Property: Solve Modes for story character clips. See FBStoryClipSolveMode"""
    Speed:float
    """Read Write Property: Speed of the clip."""
    Start:FBTime
    """Read Write Property: Start time of the clip local to its track."""
    StartStopLocked:bool
    """Read Write Property: Clip's 'In/Out Locked' property value. True if the clip's In/Out properties (start/stop times of the clip local to its track) are locked, false otherwise."""
    Stop:FBTime
    """Read Write Property: Stop time of the clip local to its track."""
    TimeWarpEnabled:bool
    """Read Write Property: Animation and Shot clip's TimeWarp activeness."""
    TimeWarpInterpolatorType:FBStoryClipTimeWarpInterpolatorType
    """Read Write Property: Animation and Shot clip's TimeWarp interpolation type. See FBStoryClipTimeWarpInterpolatorType."""
    TimeWarpReverse:bool
    """Read Write Property: If true, reverse the Animation or Shot clip's TimeWarp FCurve."""
    Translation:FBVector3d
    """Read Write Property: Animation clip's translation offset. Refer to class notes to learn more about how this is applied."""
    TravellingNode:FBPropertyListObject
    """List: Travelling node(s). If set, this property will overwrite the Track's Travelling node(s)."""
    TravellingNodeFunction:FBStoryClipNodeFunction
    """Read Write Property: Travelling node function. If set, this property will overwrite the Track's Travelling node function. See FBStoryClipNodeFunction."""
    UseSystemFrameRate:bool
    """Read Write Property: Whether always use system frame rate."""
    def CanAssignSourcesToDestinations(self)->bool:
        """CanAssignSourcesToDestinations.
        Determines if the animation clip can assign its sources to some destinations or not.
        
        return : Returns true if the animation clip can assign its sources to some destinations, false otherwise."""
        ...
    def Clone(self)->FBStoryClip:
        """Clone the clip."""
        ...
    def DestinationSetObject(self,SrcName:str,Object:FBComponent)->bool:
        """Assign source to destination if theSrcName is found in source list andObject is in the Details list.
        
        SrcName : The name of the source.
        Object : The destination object.
        return : Returns true if assignment has been executed when theSrcName is found in source list andObject is in the Details list."""
        ...
    def ExportToFile(self,OutputFile:str)->bool:
        """ExportToFile.
        Export animation clip to disk file.
        
        OutputFile : Output file path name.
        return : Returns true if successful."""
        ...
    def GetAffectedAnimationNodes(self,AffectedAnimationNodes:List[FBAnimationNode])->list:
        """GetAffectedAnimationNodes.
        Get the list of animation nodes affected by this story clip, for a specific object.
        
        AffectedAnimationNodes : Array of affected animation nodes, will be filled by the function.
        ClipObject : The object for which we search for affected animation nodes."""
        ...
    def GetAffectedObjects(self)->list:
        """GetAffectedObjects.
        Get the list of objects affected by this story clip.
        
        AffectedObjects : Array of affected objects, will be filled by the function."""
        ...
    def GetAssignSourcesToDestinationsInfo(self)->tuple:
        """GetAssignSourcesToDestinationsInfo.
        Returns the information about the current state of Sources to Destinations assignment. TheSrcList,DefaultDstList &EffectiveDstList parameters will all be of same size, each index being related to the same index in the other lists. TheAvailableDstList parameter can contains more item than the other lists.
        
        SrcList : String list containing all the sources, will be filled by the method.
        AvailableDstList : String list containing all the available destinations, will be filled by the method.
        DefaultDstList : String list containing the default destinations (contains each string item that will be put back when pressing the 'Reset' button in the UI), will be filled by the method.
        EffectiveDstList : String list containing the effective destination (destinations currently active), will be filled by the method."""
        ...
    def GetReadOnly(self)->bool:
        """GetReadOnly Retrieves the clip read-only status.
        
        return : Returns the clip read-only status."""
        ...
    def MakeWritable(self)->bool:
        """MakeWritable.
        Imports FCurves from story clip scene making them accessible for the user.
        
        return : Returns true if successful."""
        ...
    def Match(self):
        """Match.
        Match the animation clip to its previous/next animation clip, one to each other.
        
        ObjectName : The object name that specifies which part of the track content to use to match clips. If the object name is not valid, or empty, the match object will be disabled so that the blend does not take it into account when matching clips.
        TimeType : The time type specifying which point of a cross-blend the selected clip is matched.
        TranslationType : The translation type specifying if/how a clip's match object is translated to match another clip's animation.
        RotationType : The rotation type specifying if/how a clip's match object is rotated to match another clip's animation."""
        ...
    def Move(self,Delta:FBTime,Force:bool=True)->FBTime:
        """Move.
        Move the clip of a delta offset.
        
        Delta : Delta time to apply to the clip.
        Force : Force clip to find the nearest position if the move fail.
        return : Return the delta between the new and previous clip's position."""
        ...
    def MoveTo(self,Time:FBTime,Force:bool=True)->FBTime:
        """MoveTo.
        Move the clip to the specified time.
        
        Time : Time where to put the clip.
        Force : Force clip to find the nearest position if the move fail.
        return : Returns the new clip's time position."""
        ...
    def Razor(self,Time:FBTime)->FBStoryClip:
        """Razor.
        Cut (razor) the clip at the specified time.
        
        Time : Time where to cut. This time is local to the track, not to the clip.
        return : Returns the new clip generated by the razor action (right part)."""
        ...
    def SetAssignSourcesToDestinationsInfo(self,EffectiveDstList:FBStringList)->bool:
        """SetAssignSourcesToDestinationsInfo.
        Sets the new effective destinations information for the Sources to Destinations assignment. The input string list size must contain the same number of items than the effective destination list returned by the GetAssignSourcesToDestinationsInfo method. Each item in the input string list must match an item in the available destination list returned by the GetAssignSourcesToDestinationsInfo method. The item at a given index of the input string list will be related to the same index of the sources list returned by the GetAssignSourcesToDestinationsInfo method.
        
        EffectiveDstList : String list containing the new effective destination.
        return : Returns true if the assign succeeded, false otherwise."""
        ...
    def SetReadOnly(self,MakeClipReadOnly:bool,OutputFile:str="")->bool:
        """SetReadOnly Assigns the clip read-only status.
        
        MakeClipReadOnly : New read-only status
        OutputFile : Output file path name, when setting the clip's read-only status to true.
        return : Returns true if successful."""
        ...
    def SetTime(self,SourceIn:FBTime=None,SourceOut:FBTime=None,DestinationIn:FBTime=None,DestinationOut:FBTime=None,UseAlternateSrcInProp:bool=False):
        """SetTime Sets any in/out values for the source/destination times.
        In and out values are optional and the current values for the story clip will be used if not supplied. The story 'Speed' property will be adjusted in order for the supplied values to be respected by the story clip.
        
        SourceIn : New value for the source IN time. Passing a value will modify the "MarkIn" and/or the "Speed" properties.
        SourceOut : New value for the source OUT time. Passing a value will modify the "MarkOut" and/or the "Speed" properties.
        DestinationIn : New value for the destination IN time. Passing a value will modify the "Stop" and/or the "Speed" properties.
        DestinationOut : New value for the destination OUT time. Passing a value will modify the "Start" and/or the "Speed" properties.
        UseAlternateSrcInProp : Will work on the "ExtractStart" property instead of the "MarkIn" property when passingSourceIn."""
        ...
    def UpdateFromCurrentTake(self)->bool:
        """Update clip animation from current take animation for clip track's scope, works only for clip created by Insert Current Take and connected to current take.
        
        return : Returns true if succeed."""
        ...
class FBStoryFolder(FBComponent):
    """Story Folder class.
    With folders, you can group tracks together and create different timelines. See sample: FBStoryFolder.py."""
    Childs:FBPropertyListStoryFolder
    """List: Children folders of this folder."""
    Collapsed:bool
    """Read Write Property: Toggle to collapse or expand the story folder."""
    Label:str
    """Read Write Property: Label to display for this story folder."""
    Mute:bool
    """Read Write Property: If true, this story folder will be muted."""
    Parent:FBStoryFolder
    """Read Only Property: Object pointing to the folder's parent."""
    RecordClipPath:str
    """Read Write Property: Path for story recording. Can be relative or full path."""
    Solo:bool
    """Read Write Property: If true, this story folder will be the only one to play."""
    Tracks:FBPropertyListStoryTrack
    """List: Tracks of this folder."""
    def AlignSelectedClips(self,Type:FBStoryClipAlignmentType,ReferenceClip:FBComponent):
        """Used to align selected clips .
        
        Type : Type of alignment that will be done.
        ReferenceClip : Needed when kFBStoryClipAlignmentEndPreviousAllAligned, kFBStoryClipAlignmentBeginningNextAllAligned or kFBStoryClipAlignmentCurrentTimelineWithOffset are used."""
        ...
    def AlignSelectedClipsGroup(self,Type:FBStoryGroupClipAlignmentType):
        """Used to align clips inside a group.
        
        Type : Type of alignment that will be done."""
        ...
    def ConvertClipsToReadOnly(self,Selected:bool,FilePath:str):
        """Convert all clips to read-only clips.
        Identical clips are replaced by the same read-only clip.
        
        Selected : Only selected clip will be converted.
        FilePath : Folder path where the read-only clips will be saved."""
        ...
    def ExpandSelectedClips(self,PreserveOverlap:bool):
        """Used to expand selected clips .
        
        PreserveOverlap : If true, portion of clips that overlap other clips won't be modified."""
        ...
    def ExpandSelectedClipsGroup(self,PreserveOverlap:bool):
        """ExpandSelectedClipsGroup Used to expand group clip dependent clips.
        
        PreserveOverlap : If true, portion of clips that overlap other clips won't be modified."""
        ...
    def Load(self,Load:bool):
        """Allow to load/unload all story clips under this folder.
        
        Load : bool"""
        ...
class FBStoryGroupClip(FBComponent):
    """Story Group Clip class.
    Group Clip represents a group of clips that can be manipulated together."""
    DependentClips:FBPropertyListObject
    """Read Write Property: Clips that are included in the group clip."""
    Start:FBTime
    """Read Write Property: Start time of the clip."""
    StartStopLocked:bool
    """Read Write Property: Clip's 'In/Out Locked' property value. True if the clip's In/Out properties (start/end times of the clip local to its track) are locked, false otherwise."""
    Stop:FBTime
    """Read Write Property: Stop time of the clip."""
    def Move(self,Delta:FBTime,Force:bool=True)->FBTime:
        """Move.
        Move the clip of a delta offset.
        
        Delta : Delta time to apply to the clip.
        Force : Force clip to find the nearest position if the move fail.
        return : Return the delta between the new and previous clip's position."""
        ...
    def MoveTo(self,Time:FBTime,Force:bool=True)->FBTime:
        """MoveTo.
        Move the clip to the specified time.
        
        Time : Time where to put the clip.
        Force : Force clip to find the nearest position if the move fail.
        return : Returns the new clip's time position."""
        ...
    def Razor(self,Time:FBTime):
        """Razor.
        Cut (razor) the clip at the specified time.
        
        Time : Time where to cut. This time is local to the track, not to the clip."""
        ...
class FBStoryTrack(FBConstraint):
    """Story Track class.
    Tracks are containers for clips (medias), have a specific type which offer different functions. Note: To change the travelling node of a track, search for the 'TravellingNode' property on the track and then connect/disconnect the appropriate object. Python example: lPropTravellingNode = lAnimTrack.PropertyList.Find('TravellingNode') lCube.ConnectDst(lPropTravellingNode) See samples: CreateShotClip.py, AudioTrackSetupTool.py, BloopSlate.py, RecordLight.py, FBStoryFolder.py, VideoClip.py, PlotNonSelectedCharStoryTracks.py, PlotSelectedCharStoryTracks.py, PrintClipNamesAndStartStopFrames.py."""
    AcceptKey:bool
    """Read Write Property: Allow track to accept keys"""
    AudioOutIndex:int
    """Read Write Property: Audio Output's index to use."""
    Character:FBCharacter
    """Read Write Property: Character to use."""
    CharacterIndex:int
    """Read Write Property: Character's index to use."""
    ClipNameConvention:str
    """Read Write Property: Naming convention for each new recording clip that is created. Can use special tags: <Name> <StartTCValue> <StartFrameValue> <StartDate> <StartTime> <TakeName>"""
    Clips:FBPropertyListStoryClip
    """List: Clips contained in this track."""
    Details:FBPropertyListStoryDetails
    """List: All objects associated to this track for processing."""
    Ghost:bool
    """Read Write Property: Show ghosts"""
    GhostModel:bool
    """Read Write Property: Show ghost of models"""
    GhostPivot:bool
    """Read Write Property: Show ghost of match object"""
    GhostShowTrackMode:FBStoryTrackGhostShowMode
    """Read Write Property: Show the ghosts for all the clips or only the adjacent clips. See FBStoryTrackGhostShowMode"""
    GhostTravelling:bool
    """Read Write Property: Show ghost of clip vector or traveling node"""
    Label:str
    """Read Write Property: Label to display for this story track."""
    Mute:bool
    """Read Write Property: If true, this track wont' play."""
    OffsetEnable:bool
    """Read Write Property: When enabled, allow clip to be offset"""
    ParentFolder:FBStoryFolder
    """Read Only Property: Parent folder."""
    ParentTrack:FBStoryTrack
    """Read Only Property: Parent track, if the track is of Character or Animation type."""
    PassThrough:bool
    """Read Write Property: Enable passthrough of animation if there is no clip on track animation is taken from other tracks of take"""
    RecordClipPath:str
    """Read Write Property: Path for story recording. Can be relative or full path."""
    RecordTrack:bool
    """Read Write Property: Path for story recording. Can be relative or full path."""
    ReferenceMode:FBStoryTrackRefMode
    """Read Write Property: Track composition mode, kFBStoryTrackOverride or kFBStoryTrackAdditive"""
    ShowBackplate:bool
    """Read Write Property: If true, the backplate will be shown."""
    ShowFrontplate:bool
    """Read Write Property: If true, the frontplate will be shown."""
    Solo:bool
    """Read Write Property: If true, this track will be the only one to play."""
    SubTracks:FBPropertyListStorySubTrack
    """List: Only Character and Animation tracks can have sub-tracks."""
    TrackVideo:FBVideo
    """Read Only Property: This FBVideo can be used as a texture."""
    Type:FBStoryTrackType
    """Read Only Property: Type of the track"""
    def AddClip(self,Clip:FBComponent,Time:FBTime):
        """AddClip Add the clip to the track.
        
        Clip : FBComponent
        Time : FBTime"""
        ...
    def ChangeDetailsBegin(self):
        """ChangeDetailsBegin.
        You must call this function before adding/removing any object to the Details list or it won't work."""
        ...
    def ChangeDetailsEnd(self):
        """ChangeDetailsEnd.
        You must call this function after adding/removing any object to the Details list or it won't work."""
        ...
    def CopyTakeIntoTrack(self,TimeSpan:FBTimeSpan,Take:FBTake,OutputOffset:FBTime=0,MakeUndoable:bool=False)->FBStoryClip:
        """CopyTakeIntoTrack Copy animation from the specified take for affected objects of the track.
        
        TimeSpan : Time span for the clip to create.
        Take : Take to get the animation from.
        OutputOffset : Time offset for the clip if necessary.
        MakeUndoable : If the operation should be undoable.
        return : Created story clip if the operation succeeded otherwize NULL."""
        ...
    def CreateSubTrack(self,TrackType:FBStoryTrackType,RefMode:FBStoryTrackRefMode)->FBStoryTrack:
        """Create a sub track, Only Character and Animation tracks can have sub-tracks.
        
        TrackType : Type of the sub track to be created.
        RefMode : Composition mode of the sub track, kFBStoryTrackOverride or kFBStoryTrackAdditive.
        return : Created sub story track if the operation succeeded otherwise NULL."""
        ...
    def EnableBodyPart(self,Part:FBStoryTrackBodyPart,Enable:bool):
        """EnableBodyPart.
        
        Part : Which part to enable/disable.
        Enable : If True, this will enable the body part solving while false will disable it. Enable a specific body part for character solving."""
        ...
    def IsBodyPartEnabled(self,Part:FBStoryTrackBodyPart)->bool:
        """IsBodyPartEnabled.
        Is a specific body part is enabled.
        
        Part : FBStoryTrackBodyPart"""
        ...
    def Load(self,Load:bool):
        """Allow to load/unload all story clips under this track.
        
        Load : bool"""
        ...
class FBStringList():
    """String list.
    See sample: Memo.py."""
    def Add(self,S:str,Ref:object=0)->int:
        """Add a string to the list.
        
        S : String to add to list.
        Ref : Reference to store with string (default = 0)
        return : Index where item was stored."""
        ...
    def AsString(self,Separator:str='~')->str:
        """Get as string.
        
        Separator : the string list separator.
        return : String list."""
        ...
    def Clear(self):
        """Clear the list (remove all the items)."""
        ...
    def Find(self,Ref:object)->int:
        """Find the index with the stringString (or start withString)
        
        String : String to search for.
        CaseSensitive : true if considering case.
        StartWith : true if to find the index of the string which start withString.
        return : Index where S is stored."""
        ...
    def GetAt(self,Index:int)->str:
        """Get the string atIndex.
        
        Index : Index to get string at.
        return : String atIndex."""
        ...
    def GetReferenceAt(self,Index:int)->int:
        """Get the reference store with the string atIndex.
        
        Index : Index to get reference at.
        return : Reference stored with value atIndex."""
        ...
    def IndexOf(self,S:str)->int:
        """Get the index of a string.
        
        S : String to look for.
        return : Index where string S was found."""
        ...
    def InsertAt(self,Index:int,S:str,Ref:object=0):
        """Insert an entry atIndex.
        
        Index : Index where item is to be inserted.
        S : String to insert.
        Ref : Reference to store with string(default=0)."""
        ...
    def Remove(self,S:str)->int:
        """Remove a string from the list.
        
        S : String to remove from the list.
        return : Index where item was found."""
        ...
    def RemoveAt(self,Index:int):
        """Remove an entry atIndex.
        
        Index : Index where item is to be removed from."""
        ...
    def SetAt(self,Index:int,String:str)->bool:
        """Set the string atIndex.
        
        Index : Index where string is to be set.
        String : String to set value atIndex with."""
        ...
    def SetReferenceAt(self,Index:int,Ref:object):
        """Set the reference stored with the string atIndex.
        
        Index : Index to store reference at.
        Ref : Reference to store atIndex."""
        ...
    def SetString(self,String:str,Separator:str='~')->bool:
        """Set string for list.
        
        String : String to set for list.
        Separator : the string list separator."""
        ...
    def Sort(self):
        """Sort the string list (ascending)"""
        ...
class FBSurface(FBGeometry):
    """Surface class."""
    SurfaceMode:FBSurfaceMode
    """Read Write Property: Surface mode."""
    UClosed:bool
    """Read Write Property: U Closed."""
    USize:int
    """Read Write Property: Size in U directions."""
    UStep:int
    """Read Write Property: Step in U directions."""
    VClosed:bool
    """Read Write Property: V Closed"""
    VSize:int
    """Read Write Property: Size in V directions."""
    VStep:int
    """Read Write Property: Step in V directions."""
    def ControlPointsBegin(self):...
    def ControlPointsEnd(self):...
    def GetControlPoint(self,Index:object,X:object,Y:object,Z:object,W:object):
        """Index : int
        X : float
        Y : float
        Z : float
        W : float"""
        ...
    def GetSurfaceCapped(self,UorV:object,Direction:object)->bool:
        """UorV : int
        Direction : int"""
        ...
    def SetControlPoint(self,Index:object,X:object,Y:object,Z:object,W:object):
        """Index : int
        X : float
        Y : float
        Z : float
        W : float"""
        ...
    def SurfaceBegin(self):...
    def SurfaceEditBegin(self):...
    def SurfaceEditEnd(self):...
    def SurfaceEnd(self):...
class FBSystem(FBComponent):
    """Provides access to the underlying system, and the MotionBuilder scene.
    Use this class to access system properties such as the computer name, the system time, and the MotionBuilder application version.It is also used to get access to the scene (FBScene) and the current take (FBTake), as in the following Python snippet:
    
    >>> myScene = FBSystem().Scene
    for take in myScene.Takes:
    print take.Name
    
    
    The Python sample FBSystemEvents.py shows how to register a callback to FBSystem. See samples: FBSystemEvents.py, CameraSwitcher.py, BatchExportCharacterAnimationTool.py, ExportAnimationLibrary.py."""
    ApplicationPath:str
    """Read Only Property: Location where the application is installed."""
    AreMessageBoxesSuspended:bool
    """Read Only Property: While true, the system is suspending the messages boxes that would normally be displayed."""
    AssetManager:FBAssetMng
    """Read Only Property: Current asset manager."""
    AudioInputs:FBPropertyListAudioIn
    """List: Available audio inputs."""
    AudioOutputs:FBPropertyListAudioOut
    """List: Available audio outputs."""
    BuildId:str
    """Read Only Property: Unique build Id string."""
    BuildVersion:str
    """Read Only Property: Unique build version string. The format of the build version information is: Major.Minor.Revision.BuildNumber. All sub-parts of the build version string are containing only numeric characters."""
    Cameras:FBPropertyListCamera
    ComputerName:str
    """Read Only Property: Computer name. See sample: ShowMachineNameAndCameraNamePlusResolution.py."""
    ConfigPath:str
    ConstructionHistory:FBConstructionHistory
    """Read Only Property: Construction History."""
    CurrentTake:FBTake
    """Read Write Property: Current take. See samples: GoToNextTake.py,"""
    DesktopSize:FBVector2d
    """Read Only Property: The width and height of the desktop."""
    Devices:FBPropertyListDevice
    EPluginItemInfo:_Enum
    FrameRate:float
    """Read Only Property: The frame rate of the viewer."""
    FullScreenViewer:bool
    """Read Write Property: Indicates that the viewer is in full screen mode."""
    Lights:FBPropertyListLight
    LocalTime:FBTime
    """Read Only Property: Local time in take."""
    Manipulators:FBPropertyListManipulator
    """List: of manipulators."""
    Materials:FBPropertyListMaterial
    OnConnectionDataNotify:FBEventConnectionDataNotify
    """Event: A data event occurred between objects in the system."""
    OnConnectionKeyingNotify:FBEventConnectionKeyingNotify
    """Event: A keying event occurred when objects are being keyed."""
    OnConnectionNotify:FBEventConnectionNotify
    """Event: A connection event occurred between objects in the system. See sample: FBSystemEvents.py."""
    OnConnectionStateNotify:FBEventConnectionStateNotify
    """Event: A state change event occurred between objects in the system."""
    OnUIIdle:property
    """Event: User-interface idle event. Useful callback for less frequent GUI refresh and etc. lightweight tasks (occur once per several frames)."""
    OnVideoFrameRendering:FBEventVideoFrameRendering
    """Event: A video frame rendering event occurred when the scene is being off-line rendered into video files."""
    PathImages:str
    """Read Only Property: Path to images."""
    PathMeshs:str
    """Read Only Property: Path to meshes"""
    ProcessMemory:float
    """Read Only Property: The size (MB) of process's working set memory."""
    ProcessMemoryPeak:float
    """Read Only Property: The size (MB) of process's peak memory."""
    PythonVersion:int
    """Read Only Property: The Python interpreter version being used. The value is either 27 or 37."""
    Renderer:FBRenderer
    """Read Only Property: Default renderer."""
    RootModel:FBModel
    """Read Only Property: Root model."""
    Scene:FBScene
    """Read Only Property: Scene."""
    SceneRootModel:FBModel
    """Read Only Property: Scene root model."""
    Shaders:FBPropertyListShader
    SuspendMessageBoxes:bool
    """Read Write Property: While true, all the message boxes, that would normally be displayed, are suspended."""
    SystemTime:FBTime
    """Read Only Property: System time."""
    Takes:FBPropertyListTake
    Textures:FBPropertyListTexture
    UserConfigPath:str
    Version:float
    """Read Only Property: Application version."""
    VideoInputs:FBPropertyListVideoIn
    """List: Available video inputs."""
    VideoOutputs:FBPropertyListVideoOut
    """List: Available video outputs."""
    ePluginItemDescription:EPluginItemInfo
    ePluginItemFileName:EPluginItemInfo
    ePluginItemIconName:EPluginItemInfo
    def CurrentDirectory(self)->str:
        """Get current work directory.
        
        return : current work directory."""
        ...
    def GetCommandLineArgs(self)->FBStringList:
        """Returns the command line arguments for SDK.
        This function returns portion of the command line arguments within a pair of delimiters (sdk-begin & sdk-end). Example:Note that '-console', '-G500,500', '-suspendMessages' and 'C:/temp/sample.fbx' are for MotionBuilder itself hence are consumed accordingly. Only those arguments between sdk-begin and sdk-end are accessible with this function. In this example, they will be '--department mocap --usage on-stage'This SDK command line argument is useful for plugin deployment and management in large production facility, where different department or different workflow may require a different set of plugins or functionality/behavior dynamically.Python users also have access to this through official built-in module sys.argv which could be parsed easily via argparse module.
        
        return : the command line arguments"""
        ...
    def GetLoadedPluginItemGroups(self,PluginItemName:str)->FBStringList:
        """Returns a string list containing the groups list in which the specified plug-in item's name belongs to.
        
        PluginItemName : str
        return : the groups list in which the specified plug-in item's name belongs to."""
        ...
    def GetLoadedPluginItemInfo(self,PluginItemName:str)->FBStringList:
        """Returns a string list containing the information of the specified plug-in item's name.
        A specific plug-in item information can be retrieved from the returned string list with a EPluginItemInfo enum value.
        
        PluginItemName : str
        return : the information of the specified plug-in item's name."""
        ...
    def GetLoadedPluginItemsName(self)->FBStringList:
        """Returns a string list containing the names of all the loaded plug-in.
        
        return : the names of all the loaded plug-in."""
        ...
    def GetPluginPath(self)->FBStringList:
        """Returns the plugin path.
        By default, MotionBuilder searches C++ plug-ins and load them at start-up. Users could provide additional plugin paths by setting environment variable 'MOTIONBUILDER_PLUGIN_PATH' before running MotionBuilder.
        
        return : the plugin path"""
        ...
    def GetPythonStartupPath(self)->FBStringList:
        """Returns the python startup path.
        User could put python script in the startup folders, and MotionBuilder will search scripts from those folders and run them at startup. By default, there are two startup folders: /config/PythonStartup and /bin/config/PythonStartup. Users could append additional paths by setting environment variable 'MOTIONBUILDER_PYTHON_STARTUP' before launching application.
        
        return : the python startup path"""
        ...
    def MakeFullPath(self,RelativeFilePath:str)->str:
        """Return the full path.
        
        RelativeFilePath : The relative file path
        return : Full file path based on combining the current directory"""
        ...
class FBPatch(FBSurface):
    """Patch class."""
    USurfaceType:FBSurfaceType
    """Read Write Property: Patch mode for U direction."""
    VSurfaceType:FBSurfaceType
    """Read Write Property: Patch mode for V direction."""
class FBNurbs(FBSurface):
    """Nurbs class."""
    UNurbType:FBNurbType
    """Read Write Property: Nurbs Type for U direction."""
    UOrder:int
    """Read Write Property: Nurbs U order."""
    VNurbType:FBNurbType
    """Read Write Property: Nurbs Type for V direction."""
    VOrder:int
    """Read Write Property: Nurbs V order."""
    def GetControlKnotValue(self,UorV:int,Index:int)->float:
        """Get knot vector value of control point.
        
        UorV : 1 if V knot vector, 0 if U knot vector.
        Index : Index of control point to set knot value for."""
        ...
    def GetControlMultiplicity(self,UorV:int,Index:int)->int:
        """Get multiplicity (number of 'instances') of control point.
        
        UorV : 1 if V multiplicity, 0 if U multlipicity.
        Index : Index of control point to get multiplicity for."""
        ...
    def GetControlWeight(self,Index:int)->float:
        """Get weight of control point.
        
        Index : Index of control point to get weight from.
        return : Weight of control point at indexIndex."""
        ...
    def GetKnotCount(self,UorV:int)->int:
        """Number of knot vectors.
        
        UorV : 1 if V knot vector, 0 if U knot vector.
        return : Number of knot vectors on NURBS surface"""
        ...
    def SetControlKnotValue(self,UorV:int,Index:int,KnotValue:float):
        """Set knot vector value of control point.
        
        UorV : 1 if V knot vector, 0 if U knot vector.
        Index : Index of control point to set knot value for.
        KnotValue : Knot value for control point atIndex."""
        ...
    def SetControlMultiplicity(self,UorV:int,Index:int,Multiplicity:int):
        """Set multiplicity (number of 'instances') of control point.
        
        UorV : 1 if V multiplicity, 0 if U multlipicity.
        Index : Index of control point to set multiplicity for.
        Multiplicity : Multiplicity value for control point atIndex."""
        ...
    def SetControlWeight(self,Index:int,Weight:float):
        """Set weight of control point.
        
        Index : Index of control point to set weight at.
        Weight : Weight of control point."""
        ...
class FBTexture(FBBox):
    """See samples: HUDElements.py, MaterialAndTexture.py, TextureAnimation.py, VideoInput.py, VideoMemory.py, DeleteUnusedMedia.py."""
    Alpha:property
    """Read Write Property: Texture alpha value."""
    BlendMode:property
    """Read Write Property: Texture blend mode."""
    Height:property
    """Read Only Property: Height of texture."""
    Mapping:property
    """Read Write Property: Texture mapping."""
    Rotation:property
    """Read Write Property: Rotation coordinates."""
    Scaling:property
    """Read Write Property: Scaling coordinates."""
    SwapUV:property
    """Read Write Property: Swap UV coordinates?"""
    TextureOGLId:property
    """Read Only: OpenGL texture buffer object Id."""
    Translation:property
    """Read Write Property: Translation coordinates."""
    UseType:property
    """Read Write Property: Texture Use Type."""
    Video:property
    """Read Write Property: Media used for texturing."""
    Width:property
    """Read Only Property: Width of texture."""
    def Clone(self)->object:
        """Clone the texture.
        This will duplicated the current texture.
        
        return : Newly created texture."""
        ...
    def OGLInit(self):
        """RenderOptions : FBRenderOptions"""
        ...
class FBLayeredTexture(FBTexture):
    """LayeredTexture class.
    This class is used to encapsulate list of textures. User could subclass this class to support customized blending & compostion modes. See /OpenRealitySDK/Samples/miscellaneous/texture_template/ for example. See sample: LayeredTexture.py."""
    BackgroundColor:FBColorAndAlpha
    """Read/Write Property: Animatable Background color which is used to clear color buffer before composition."""
    Layers:FBPropertyListTexture
    """Read/Write Property: Textures Layers."""
    def SetLayerConfigDirty(self):
        """Set layer config dirty to trigger new composition."""
        ...
class FBTime():
    """Time data structure.
    See samples: FBTime.py, CameraSwitcher.py, ExportAnimationLibrary.py, StartKeysAtCurrentTime.py."""
    ETimeFormats:_Enum
    Infinity:FBTime
    """Time constant: Infinity, the largest time value."""
    MinusInfinity:FBTime
    """Time constant: Minus Infinity, the lowest negative time value."""
    OneHour:FBTime
    """Time constant: One Hour."""
    OneMinute:FBTime
    """Time constant: One Minute."""
    OneSecond:FBTime
    """Time constant: One Second."""
    Zero:FBTime
    """Time constant: Zero."""
    eDefaultFormat:ETimeFormats
    eFrame:ETimeFormats
    eSMPTE:ETimeFormats
    def Get(self)->float:
        """Get time value (long)
        
        return : Time value as long."""
        ...
    def GetFrame(self,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault)->float:
        """Get the frame count.
        With this function, it is possible to obtain the cumulative and local frame counts.
        
        TimeMode : Time mode to get the constant (default is kFBTimeModeDefault).
        return : Frames per second constant for the specified time mode."""
        ...
    def GetMilliSeconds(self)->float:
        """Get milliseconds for time.
        
        return : MilliSeconds value."""
        ...
    def GetSecondDouble(self)->float:
        """Get seconds as double.
        
        return : Seconds in double form."""
        ...
    def GetTimeString(self,Mode:FBTimeMode=FBTimeMode.kFBTimeModeDefault,Format:ETimeFormats=eDefaultFormat)->str:
        """Get time as a string.
        
        Mode : Time mode (default=kFBTimeModeDefault) to use (call FBSystem().GetTransportFps() to the the current UI displayed mode).
        Format : Format to use for the returned string(default=FBTime::eDefaultFormat).
        return : String value of time."""
        ...
    def Set(self,Time:float):
        """Set time value from a long.
        
        Time : Time value to set."""
        ...
    def SetFrame(self,Frames:float,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault):
        """Set time in frame format.
        
        Frames : The number of frames.
        TimeMode : The time mode identifier which will dictate the extraction algorithm."""
        ...
    def SetMilliSeconds(self,MilliSeconds:float):
        """Set milliseconds time.
        
        MilliSeconds : MilliSeconds value."""
        ...
    def SetSecondDouble(self,Time:float):
        """Set seconds from double.
        
        Time : Time to set seconds from."""
        ...
    def SetTime(self,Hour:int,Minute:int=0,Second:int=0,Frame:int=0,Field:int=0,TimeMode:FBTimeMode=FBTimeMode.kFBTimeModeDefault):
        """Set time (from separate values)
        
        Hour : Hour value.
        Minute : Minute value(default=0).
        Second : Second value(default=0).
        Frame : Frame value(default=0).
        Field : Field value(default=0).
        TimeMode : Time mode to get time as(default=kFBTimeModeDefault)."""
        ...
    def SetTimeString(self,Time:str):
        """Set time from string.
        
        Time : String to set time from."""
        ...
class FBTimeCode():
    """TimeCode data structure.
    See sample: TimeCodeKeying.py."""
    FILM_23976:float
    """-23.976f"""
    FILM_24:float
    """-24.0f"""
    FRAMES_11988:float
    """-119.88f"""
    FRAMES_30:float
    """-30.0f"""
    FRAMES_5994:float
    """-59.94f"""
    Frame:float
    FrameRate:float
    MPAL_30:float
    """-29.971f Currently not supported : '1' is added just to differentiate from NTSC_FULL(-29.97f)"""
    NTSC_DROP:float
    """Rates."""
    NTSC_FULL:float
    """-29.97f"""
    PAL_25:float
    """-25.0f"""
    TimeCodeString:property
    def GetRawFrame(self)->float:
        """Get the raw value for the frame.
        
        return : raw value for the frame."""
        ...
    def GetRawRate(self)->float:
        """Get the raw value for the rate.
        
        return : raw value for the rate."""
        ...
    def GetRawSecond(self)->float:
        """Get the raw value for the second.
        
        return : raw value for the second."""
        ...
    def GetTime(self)->FBTime:
        """Return a Time corresponding to the timecode."""
        ...
    def GetTimeCodeString(self,Format=FBTime.eDefaultFormat)->str:
        """Get time as a string.
        
        Format : Format to use for the returned string(default=FBTime::eDefaultFormat).
        return : String value of time."""
        ...
    def SetTime(self,Time:FBTime):
        """Set TimeCode according to the given time.
        
        Time : Time value to set."""
        ...
    def SetTimeCode(self,Hour:int,Minute:int=0,Second:int=0,Frame:float=0):
        """Set timecode.
        
        Hour : Hour value.
        Minute : Minute value.
        Second : Second value.
        Frame : Frame value."""
        ...
    def SetTimeCodeString(self,Time:str,Format=FBTime.eDefaultFormat):
        """Set time from string.
        
        Time : String to set time from.
        Format : Format to use for the string(default=FBTime::eDefaultFormat)."""
        ...
class FBTake(FBComponent):
    """A take is a container for animation in a scene.
    A take stores data about animation for objects. The transport controls (FBPlayerControl) act on the current take.In the UI transport controls, a take's start and end determine when the Timeline indicator starts and stops.You get the current take with FBSystem::CurrentTake, as in the following Python sample:
    
    >>> for myTake in FBSystem().Scene.Takes:
    print myTake.Name
    
    
    To create a take and have it accessible in the Transport control you could use CopyTake (called Duplicate in the UI):Python sample code:
    
    >>> from pyfbsdk import *
    newTake = FBSystem().CurrentTake.CopyTake('my new take name')
    
    
    C++ sample code:
    
    >>> FBTake* lTake = FBSystem::ThenOne().CurrentTake->CopyTake( 'my new take' );
    
    
    Or simply create a new empty take like the following:Python sample code:
    
    >>> from pyfbsdk import *
    newTake = FBTake('my new take name')
    FBSystem().Scene.Takes.append(newTake)
    
    
    C++ sample code:
    
    >>> FBSystem::TheOne()::Scene.Takes.Add( new FBTake( 'my new take' ));
    
    
    See samples: MergePreviewAnimationLayers.py, ExportAnimationLibrary.py, GoToNextTake.py, GoToPreviousTake.py, MirrorPoseOverTime.py, MultiLayerKeying.py, RenameFirstTakeOnMultipleFiles.py, SaveOneTakePerFile.py, TimeCodeKeying.py."""
    Comments:str
    """Read Write Property: Take comments."""
    LocalTimeSpan:FBTimeSpan
    """Read Write Property: Local time span."""
    ReferenceTimeSpan:FBTimeSpan
    """Read Write Property: Reference time span."""
    def AddTimeMark(self,Time:FBTime)->int:
        """Add a time mark to the take.
        It doesn't allow creating a time mark at the same time of another time mark. Note: Internally, the time marks are stored in time order. Adding a time mark before other existing time marks will modify the index of these other time marks.
        
        Time : Time where to add the time mark on the take.
        Name : Name of the time mark to add.
        return : The index of the time mark added if the operation is successful, -1 otherwise."""
        ...
    def ClearAllProperties(self,OnSelectedObjectsOnly:bool,OnLockedProperties:bool=False):
        """Clear the animation on all the properties.
        
        OnSelectedObjectsOnly : Specify if clear will be performed on all objects or only on the one that are currently selected.
        OnLockedProperties : Specify if clear will be performed on locked properties as well."""
        ...
    def ClearAllPropertiesOnCurrentLayer(self):
        """Clear all the animation on the current layer."""
        ...
    def CopyTake(self,NewTakeName:str)->FBTake:
        """Copy the take.
        Will create a copy of the current take, with the current take data. This is analogous to creating a new take, and copying the current take data into it. The Layers data and the TimeWarp date will be copied. The newly created take will be set as the current take. The newly created take is automatically added to the scene and available in the Transport control.
        
        NewTakeName : The name for the new take.
        return : Handle to the newly created take."""
        ...
    def CreateNewLayer(self):
        """Create a new layer."""
        ...
    def DeleteAllTimeMarks(self):
        """Delete all time marks from the take."""
        ...
    def DeleteAnimation(self,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False)->bool:
        """Delete animation (FCurve keys) of this take object within a time range.
        
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        OnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties.
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteAnimationOnObjects(self,Objects:List[FBBox],StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False)->bool:
        """Delete animation (FCurve keys) of this take object on given objects within a time range.
        
        Objects : Objects affected by the delete operation.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        OnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties.
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteAnimationOnProperties(self,Properties:List[FBProperty],StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False,PropertyComponents:FBPropertyComponents=FBPropertyComponents.kFBPropertyComponentAll)->bool:
        """Delete animation (FCurve keys) of this take object on given properties within a time range.
        
        Properties : Properties affected by the delete operation.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the delete operation, -1 to delete the animation of all animations layers.
        OnLockedProperties : True to delete animation on locked properties, false to skip deleting animation on locked properties.
        PropertyComponents : The component bit field considered when performing the delete operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property.
        return : True if the delete operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def DeleteTimeMark(self,Index:int)->bool:
        """Delete a time mark from the take.
        Note: Internally, the time marks are stored in time order. Deleting a time mark will modify the index of time marks laying after the deleted time mark.
        
        Index : Index of the time mark to delete.
        return : True if the operation is successful, false otherwise."""
        ...
    def DuplicateSelectedLayers(self):
        """Duplicate the selected layers.
        This is equivalent of doing a copy-paste."""
        ...
    def GetCurrentLayer(self)->int:
        """Get the current layer for the take.
        
        return : The current layer index."""
        ...
    def GetLayer(self,LayerIndex:int)->FBAnimationLayer:
        """Get the layer object that have the specified ID.
        
        LayerIndex : The index of the layer that will be returned.
        return : Layer with the specified ID."""
        ...
    def GetLayerByName(self,Name:str)->FBAnimationLayer:
        """Get the layer object that have the specified name.
        
        Name : The name of the animation layer to get.
        return : Layer with the specified name or NULL if no layer has been found."""
        ...
    def GetLayerCount(self)->int:
        """Get the layer count.
        
        return : The layer count."""
        ...
    def GetLayerRealSelection(self)->bool:
        """Real selection for layer.
        Check the SetLayerRealSelection function for more information about this.
        
        return : True if selecting a layer will also select the FBComponent of that layer."""
        ...
    def GetNextTimeMarkIndex(self)->int:
        """Returns the next time mark index, based on the current local time.
        
        return : The next time mark index, -1 if any next time mark is available."""
        ...
    def GetPreviousTimeMarkIndex(self)->int:
        """Returns the previous time mark index, based on the current local time.
        
        return : The previous time mark index, -1 if any previous time mark is available."""
        ...
    def GetTimeMarkAction(self,Index:int)->FBTimeMarkAction:
        """Returns the action associated with a time mark.
        
        Index : Index of the time mark.
        return : The action associated with the time mark."""
        ...
    def GetTimeMarkColor(self,Index:int)->FBColor:
        """Returns the color associated with a time mark.
        
        Index : Index of the time mark.
        return : The color associated with the time mark."""
        ...
    def GetTimeMarkCount(self)->int:
        """Returns the number of time marks on the take.
        
        return : The number of time marks on the take."""
        ...
    def GetTimeMarkName(self,Index:int)->str:
        """Returns the name associated with a time mark.
        
        Index : Index of the time mark.
        return : The name associated with the time mark."""
        ...
    def GetTimeMarkTime(self,Index:int)->FBTime:
        """Returns the time associated with a time mark.
        
        Index : Index of the time mark.
        return : The time associated with the time mark."""
        ...
    def MergeLayers(self,MergeOptions:FBAnimationLayerMergeOptions,DeleteMergedLayers:bool,MergeMode:FBMergeLayerMode,MergeLockedProperties:bool=False):
        """Merge the selected layers.
        This is equivalent of pressing the merge button in the Animation Layer editor.
        
        MergeOptions : Indicate which objects, layers and properties (selected or all) should be merged.
        DeleteMergedLayers : The source layer will be deleted after the merge if no animation is left on those layers, or if those layers are not parent of another layer.
        MergeMode : Set the layer mode of the resulting layer, if possible (the BaseAnimation layer cannot be modified).
        MergeLockedProperties : The properties will be merged even if they are locked."""
        ...
    def MoveCurrentLayerDown(self)->bool:
        """Move the current layer down, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.
        
        return : True if successful."""
        ...
    def MoveCurrentLayerUp(self)->bool:
        """Move the current layer up, similar to using the button to move the layer in the Animation Layer tool.
        Use the SetCurrentLayer to specify the current layer.
        
        return : True if successful."""
        ...
    def OffsetAnimation(self,OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False)->bool:
        """Offset the animation (FCurve keys) of this take object within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        
        OffsetTime : The offset time to apply.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        OnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def OffsetAnimationOnObjects(self,Objects:List[FBBox],OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False)->bool:
        """Offset the animation (FCurve keys) of this take object on given objects within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        
        Objects : Objects affected by the offset operation.
        OffsetTime : The offset time to apply.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        OnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def OffsetAnimationOnProperties(self,Properties:List[FBProperty],OffsetTime:FBTime,StartTime:FBTime=FBTime.MinusInfinity,StopTime:FBTime=FBTime.Infinity,Inclusive:bool=True,LayerID:int=-1,OnLockedProperties:bool=False,PropertyComponents:FBPropertyComponents=FBPropertyComponents.kFBPropertyComponentAll)->bool:
        """Offset the animation (FCurve keys) of this take object on given properties within a time range by a given offset time.
        Non-moving FCurve keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        
        Properties : Properties affected by the offset operation.
        OffsetTime : The offset time to apply.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        LayerID : The animation layer ID being affected by the offset operation, -1 to offset the animation of all animations layers.
        OnLockedProperties : True to offset animation on locked properties, false to skip offsetting animation on locked properties.
        PropertyComponents : The component bit field considered when performing the offset operation, for properties having such components. By default, all components are considered. If a property don't have any component, this parameter is not affecting that property.
        return : True if the offset operation is successful (at least one FCurve has been modified), false otherwise (e.g. no keys found within the time range, invalid layer ID, etc.)."""
        ...
    def PlotAllTakesOnObjects(self,PlotPeriod:FBTime,ObjectsToPlot:List[FBBox]):
        """Plot the animation on given objects for all takes.
        This method will plot the animation of all takes to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.
        
        PlotPeriod : Period for the plot.
        ObjectsToPlot : Objects to plot."""
        ...
    def PlotAllTakesOnProperties(self,PlotPeriod:FBTime,PropertiesToPlot:List[FBProperty]):
        """Plot the animation on given properties for all takes.
        Will plot the animation for all takes on the given properties in the scene.
        
        PlotPeriod : Period for the plot.
        PropertiesToPlot : Properties to plot."""
        ...
    def PlotAllTakesOnSelected(self,PlotPeriod:FBTime):
        """Plot the animation on selected models for all takes.
        Will plot the animation for all takes on the selected models in the scene.
        
        PlotPeriod : Period for the plot."""
        ...
    def PlotAllTakesOnSelectedProperties(self,PlotPeriod:FBTime):
        """Plot the animation on selected properties for all takes.
        Will plot the animation for all takes on the selected properties in the scene.
        
        PlotPeriod : Period for the plot."""
        ...
    def PlotTakeOnObjects(self,PlotPeriod:FBTime,ObjectsToPlot:List[FBBox]):
        """Plot the animation on given objects.
        This method will plot the animation of the take to the specified objects. Although the method supports boxes, the most common use case it to specify FBModels that have been cast to boxes.
        
        PlotPeriod : Period for the plot.
        ObjectsToPlot : Objects to plot."""
        ...
    def PlotTakeOnProperties(self,PlotPeriod:FBTime,PropertiesToPlot:List[FBProperty]):
        """Plot the animation on given properties.
        Will plot the animation of the take in question on the given properties in the scene.
        
        PlotPeriod : Period for the plot.
        PropertiesToPlot : Properties to plot."""
        ...
    def PlotTakeOnSelected(self,PlotPeriod:FBTime):
        """Plot the animation on selected models.
        Will plot the animation of the take in question on the selected models in the scene.
        
        PlotPeriod : Period for the plot."""
        ...
    def PlotTakeOnSelectedProperties(self,PlotPeriod:FBTime):
        """Plot the animation on selected properties.
        Will plot the animation of the take in question on the selected properties in the scene.
        
        PlotPeriod : Period for the plot."""
        ...
    def RemoveLayer(self,LayerIndex:int):
        """Remove a layer.
        
        LayerIndex : Layer with at the specified index will be removed."""
        ...
    def SetCurrentLayer(self,LayerIndex:int):
        """Set the current layer for the take.
        Note that this will not deselect the other layers.
        
        LayerIndex : The layer index to be set as the current one."""
        ...
    def SetLayerRealSelection(self,Value:bool):
        """Set real selection for layer.
        This method is used to specify if using the SelectLayer method of the FBAnimationLayer object will also select the FBComponent object. In previous version of MotionBuilder, an animation layer was always selected, causing the layer to be displayed in the property editor. Also, when parsing the selected objects in the SDK, a layer would always be there. Setting this value to false will prevent this.
        
        Value : True if future layer selection will also select the FBComponent object."""
        ...
    def SetTimeMarkAction(self,Index:int,Action:FBTimeMarkAction)->bool:
        """Sets a new action for an existing time mark.
        
        Index : Index of the time mark.
        Action : The new action for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkColor(self,Index:int,Color:FBColor)->bool:
        """Sets a new color for an existing time mark.
        
        Index : Index of the time mark.
        Color : The new color for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkName(self,Index:int,Name:str)->bool:
        """Sets a new name for an existing time mark.
        
        Index : Index of the time mark.
        Name : The new name for the time mark.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetTimeMarkTime(self,Index:int,Time:FBTime)->int:
        """Sets a new time for an existing time mark.
        Note: Internally, the time marks are stored in time order. Modifying the time of a time mark may modify the index of all time marks.
        
        Index : Index of the time mark.
        Time : The new time for the time mark.
        return : The new index of the modified time mark."""
        ...
class FBFCurve(FBComponent):
    """FCurve class.
    See samples: ClearKeysOnSelectedModels.py, FCurveEditor.py."""
    Keys:FBPropertyListFCurveKey
    """List: Keys."""
    def CreateInterpolatorCurve(self,CurveType:FBInterpolatorCurveType)->FBFCurve:
        """Create and interpolator curve.
        
        CurveType : Interpolator curve type to create."""
        ...
    def EditBegin(self,KeyCount:int=-1):
        """Setup function to begin adding keys.
        
        KeyCount : Key to begin adding at(default is -1)."""
        ...
    def EditClear(self):
        """Empty FCurve of all keys."""
        ...
    def EditEnd(self,KeyCount:int=-1):
        """End key adding sequence.
        
        KeyCount : Key to finish adding at (default is -1)."""
        ...
    def Evaluate(self,Time:FBTime)->float:
        """Evaluate FCurve atTime.
        
        Time : Time at which FCurve is to be evaluated.
        return : Value of FCurve atTime."""
        ...
    def GetPostExtrapolationCount(self)->int:
        """Get count for post extrapolation."""
        ...
    def GetPostExtrapolationMode(self)->FBExtrapolationMode:
        """Get modes for post extrapolation."""
        ...
    def GetPreExtrapolationCount(self)->int:
        """Get count for pre extrapolation."""
        ...
    def GetPreExtrapolationMode(self)->FBExtrapolationMode:
        """Get modes for pre extrapolation."""
        ...
    def KeyAdd(self,Time:FBTime,Value:float)->int:
        """Add a key at the specified time.
        
        Time : Time at which to insert the key.
        Value : Value of the key.
        Interpolation : Interpolation type of the inserted key, default value is Cubic interpolation.
        TangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth).
        return : The position of the new key in the list of FCurve keys."""
        ...
    def KeyDelete(self,StartIndex:int,StopIndex:int)->bool:
        """Delete keys within a time range.
        This function is much faster than multiple removes.
        
        Start : Start of time range.
        Stop : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        return : True if the delete operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.)."""
        ...
    def KeyDeleteByIndexRange(self,arg2:object,arg3:object)->bool:...
    def KeyDeleteByTimeRange(self,arg2:FBTime,arg3:FBTime,arg4:object)->bool:...
    def KeyGetInterpolation(self,Index:int)->FBInterpolation:
        """Get the key interpolation type at the specified index.
        
        Index : Index of the key to query.
        return : Type of interpolation."""
        ...
    def KeyGetLeftBezierTangent(self,Index:int)->float:
        """Get the key left bezier tangent value at the specified index.
        
        Index : Index of the key to query.
        return : Left bezier tangent."""
        ...
    def KeyGetLeftDerivative(self,Index:int)->float:
        """Get the key left derivative value at the specified index.
        
        Index : Index of the key to query.
        return : Left derivative value, in units/seconds."""
        ...
    def KeyGetLeftTangentWeight(self,Index:int)->float:
        """Get the key left tangent weight at the specified index.
        
        Index : Index of the key to query.
        return : Left tangent weight."""
        ...
    def KeyGetMarkedForManipulation(self,Index:int)->bool:
        """Get the key manipulation state.
        
        Index : Index of the key to query.
        return : True if the key is being manipulated, false otherwise."""
        ...
    def KeyGetRightBezierTangent(self,Index:int)->float:
        """Get the key right bezier tangent value at the specified index.
        
        Index : Index of the key to query.
        return : Right bezier tangent."""
        ...
    def KeyGetRightDerivative(self,Index:int)->float:
        """Get the key right derivative value at the specified index.
        
        Index : Index of the key to query.
        return : Right derivative value, in units/seconds."""
        ...
    def KeyGetRightTangentWeight(self,Index:int)->float:
        """Get the key right tangent weight at the specified index.
        
        Index : Index of the key to query.
        return : Right tangent weight."""
        ...
    def KeyGetSelected(self,Index:int)->bool:
        """Get the key selected state.
        
        Index : Index of the key to query.
        return : True if the key is selected, false otherwise."""
        ...
    def KeyGetTCBBias(self,Index:int)->float:
        """Get the key bias value at the specified index (TCB key).
        
        Index : Index of the key to query.
        return : Bias value."""
        ...
    def KeyGetTCBContinuity(self,Index:int)->float:
        """Get the key continuity value at the specified index (TCB key).
        
        Index : Index of the key to query.
        return : Continuity value."""
        ...
    def KeyGetTCBTension(self,Index:int)->float:
        """Get the key tension value at the specified index (TCB key).
        
        Index : Index of the key to query.
        return : Tension value."""
        ...
    def KeyGetTangentBreak(self,Index:int)->bool:
        """Get the key tangent's break status at the specified index.
        
        Index : Index of the key to query.
        return : Tangent's break status."""
        ...
    def KeyGetTangentClampMode(self,Index:int)->FBTangentClampMode:
        """Get the key tangent's clamp method at the specified index.
        
        Index : Index of the key to query.
        return : Tangent's clamp method."""
        ...
    def KeyGetTangentConstantMode(self,Index:int)->FBTangentConstantMode:
        """Get the key tangent's constant mode at the specified index.
        
        Index : Index of the key to query.
        return : Tangent's constant mode."""
        ...
    def KeyGetTangentCustomIndex(self,Index:int)->FBTangentCustomIndex:
        """Get the key tangent's custom index at the specified index.
        
        Index : Index of the key to query.
        return : Tangent's custom index."""
        ...
    def KeyGetTangentMode(self,Index:int)->FBTangentMode:
        """Get the key tangent mode at the specified index.
        
        Index : Index of the key to query.
        return : Tangent calculation method."""
        ...
    def KeyGetTangentWeightMode(self,Index:int)->FBTangentWeightMode:
        """Get the tangent weight mode for a key.
        
        Index : Index of the key to query.
        return : Current weight mode."""
        ...
    def KeyGetTime(self,Index:int)->FBTime:
        """Get the key time value at the specified index.
        
        Index : Index of the key to query.
        return : Time of key."""
        ...
    def KeyGetValue(self,Index:int)->float:
        """Get the key value at the specified index.
        
        Index : Index of the key to query.
        return : Value of the key."""
        ...
    def KeyInsert(self,Time:FBTime,Interpolation:FBInterpolation=FBInterpolation.kFBInterpolationCubic,TangentMode:FBTangentMode=FBTangentMode.kFBTangentModeAuto):
        """Insert a key without affecting the curve shape.
        
        Time : Time at which the key is to be inserted.
        Interpolation : Interpolation type of the inserted key, default value is Cubic interpolation.
        TangentMode : Tangent calculation method of the inserted key, default value is Auto (Smooth)."""
        ...
    def KeyOffset(self,OffsetTime:FBTime,StartIndex:int,StopIndex:int)->bool:
        """Offset keys within a time range by a given offset time.
        Non-moving keys that are situated in the target range are deleted automatically, to preserve the animation being offset.
        
        OffsetTime : The offset time to apply on keys.
        StartTime : Start of time range.
        StopTime : End of time range.
        Inclusive : True to include within the time range the keys atStartTime andStopTime, false otherwise.
        return : True if the offset operation is successful, false otherwise (e.g. the FCurve is locked, no keys found within the time range, etc.)."""
        ...
    def KeyReplaceBy(self,Source:FBFCurve,Start:FBTime=FBTime.MinusInfinity,Stop:FBTime=FBTime.Infinity,UseExactGivenSpan:bool=False,KeyStartEndOnNoKey:bool=True):
        """Replace keys within a range in current function curve with keys found in a source function curve.
        
        Source : Source function curve.
        Start : Start of time range.
        Stop : End of time range.
        UseExactGivenSpan : When false, the time of the first and last key in the range will be used.
        KeyStartEndOnNoKey : When true, inserts a key at the beginning and at the end of the range if there is no key to insert."""
        ...
    def KeySetInterpolation(self,Index:int,Value:FBInterpolation):
        """Set the key interpolation type at the specified index.
        
        Index : Index of the key to set.
        Value : Type of interpolation."""
        ...
    def KeySetLeftBezierTangent(self,Index:int,Value:float):
        """Set the key left bezier tangent value at the specified index.
        
        Index : Index of the key to set.
        Value : Left bezier tangent."""
        ...
    def KeySetLeftDerivative(self,Index:int,Value:float):
        """Set the key left derivative value at the specified index.
        
        Index : Index of the key to set.
        Value : Left derivative value, in units/seconds."""
        ...
    def KeySetLeftTangentWeight(self,Index:int,Value:float):
        """Set the key left tangent weight at the specified index.
        
        Index : Index of the key to set.
        Value : Left tangent weight."""
        ...
    def KeySetMarkedForManipulation(self,Index:int,Value:bool)->bool:
        """Set the key manipulation state.
        
        Index : Index of the key to set.
        Value : New manipulation state.
        return : True if the operation was successful, false otherwise."""
        ...
    def KeySetRightBezierTangent(self,Index:int,Value:float):
        """Set the key right bezier tangent value at the specified index.
        
        Index : Index of the key to set.
        Value : Right bezier tangent."""
        ...
    def KeySetRightDerivative(self,Index:int,Value:float):
        """Set the key right derivative value at the specified index.
        
        Index : Index of the key to set.
        Value : Right derivative value, in units/seconds."""
        ...
    def KeySetRightTangentWeight(self,Index:int,Value:float):
        """Set the key right tangent weight at the specified index.
        
        Index : Index of the key to set.
        Value : Right tangent weight."""
        ...
    def KeySetSelected(self,Index:int,Value:bool)->bool:
        """Set the key selected state.
        
        Index : Index of the key to set.
        Value : New selection state.
        return : True if the operation was successful, false otherwise."""
        ...
    def KeySetTCBBias(self,Index:int,Value:float):
        """Set the key bias value at the specified index (TCB key).
        
        Index : Index of the key to set.
        Value : Bias value."""
        ...
    def KeySetTCBContinuity(self,Index:int,Value:float):
        """Set the key continuity value at the specified index (TCB key).
        
        Index : Index of the key to set.
        Value : Continuity value."""
        ...
    def KeySetTCBTension(self,Index:int,Value:float):
        """Set the key tension value at the specified index (TCB key).
        
        Index : Index of the key to set.
        Value : Tension value."""
        ...
    def KeySetTangentBreak(self,Index:int,Value:bool):
        """Set the key tangent's break status at the specified index.
        
        Index : Index of the key to set.
        Value : Tangent's break status."""
        ...
    def KeySetTangentClampMode(self,Index:int,Value:FBTangentClampMode):
        """Set the key tangent's clamp method at the specified index.
        
        Index : Index of the key to set.
        Value : Tangent's clamp method."""
        ...
    def KeySetTangentConstantMode(self,Index:int,Value:FBTangentConstantMode):
        """Set the key tangent's constant mode at the specified index.
        
        Index : Index of the key to set.
        Value : Tangent's constant mode."""
        ...
    def KeySetTangentCustomIndex(self,Index:int,Value:FBTangentCustomIndex):
        """Set the key tangent's custom index at the specified index.
        
        Index : Index of the key to set.
        Value : Tangent's custom index."""
        ...
    def KeySetTangentMode(self,Index:int,Value:FBTangentMode):
        """Set the key tangent mode at the specified index.
        
        Index : Index of the key to set.
        Value : Tangent calculation method."""
        ...
    def KeySetTangentWeightMode(self,Index:int,Value:FBTangentWeightMode):
        """Change the tangent weight for a key.
        Setting the value for LeftTangentWeight/RightTangentWeight will also activate the weight for that part. Please see the note provided with FBTangentWeightMode for the left weight of a key.
        
        Index : Index of the key to set.
        Value : Set theValue according to the desired mode, kFBTangentWeightModeNone to disable it."""
        ...
    def KeySetTime(self,Index:int,Value:FBTime):
        """Set the key time value at the specified index.
        
        Index : Index of the key to set.
        Value : Time of key."""
        ...
    def KeySetValue(self,Index:int,Value:float):
        """Set the key value at the specified index.
        
        Index : Index of the key to set.
        Value : Value of the key."""
        ...
    def SetPostExtrapolationCount(self,Count:int):
        """Set count for post extrapolation.
        
        Count : int"""
        ...
    def SetPostExtrapolationMode(self,ExtrapolationMode:FBExtrapolationMode):
        """Set modes for post extrapolation.
        
        ExtrapolationMode : FBExtrapolationMode"""
        ...
    def SetPreExtrapolationCount(self,Count:int):
        """Set count for pre extrapolation.
        
        Count : int"""
        ...
    def SetPreExtrapolationMode(self,ExtrapolationMode:FBExtrapolationMode):
        """Set modes for pre extrapolation.
        
        ExtrapolationMode : FBExtrapolationMode"""
        ...
class FBTimeSpan():
    """TimeSpan class."""
    def GetDirection(self)->int:
        """Get the direction of the timespan.
        Returns 1 if positive, -1 otherwise.
        
        return : Direction of timespan."""
        ...
    def GetDuration(self)->FBTime:
        """Get the unsigned duration value of a timespan.
        
        return : Unsigned duration of the timespan."""
        ...
    def GetSignedDuration(self)->FBTime:
        """Get the signed duration value of a timespan.
        
        return : Signed duration of the timespan."""
        ...
    def GetStart(self)->FBTime:...
    def GetStop(self)->FBTime:...
    def Set(self,Start:FBTime,Stop:FBTime):
        """Set the TimeSpan.
        
        Start : Start time.
        Stop : Stop time."""
        ...
class FBTimeWarpManager(FBComponent):
    """Time Warp Manager Interface to the Time Warp Manager.
    See sample: TimeWarp.py."""
    def ApplyTimeWarp(self,Take:FBTake,EvalProp:FBProperty,TimeWarp:FBAnimationNode)->bool:
        """Apply the TimeWarp in a Take to an evaluation property, just connect the storing property for the TimeWarp to the evaluation property.
        
        Take : The Take where the TimeWarp in.
        EvalProp : The evaluation property to be applied on.
        TimeWarp : The TimeWarp to apply.
        return : True if apply successfully."""
        ...
    def DestroyTimeWarpFromTake(self,Take:FBTake,TimeWarp:FBAnimationNode):
        """Destroy the TimeWarp in a Take, and removed from the DataSet.
        
        Take : The Take where the TimeWarp in.
        TimeWarp : The TimeWarp to be Destroyed."""
        ...
    def FindTimeWarpNickNumberGlobal(self,TimeWarp:FBAnimationNode)->int:
        """Find the Nick Number of one timewarp globally.
        
        TimeWarp : The TimeWarp queried.
        return : the Nick Number of the timewarp."""
        ...
    def GetTimeWarpAtIndex(self,Take:FBTake,Index:int)->FBAnimationNode:
        """Get the TimeWarp in a Take At specific Index.
        
        Take : The Take queried.
        Index : The index of the TimeWarp.
        return : TimeWarp at specific Index in a Take."""
        ...
    def GetTimeWarpCount(self,Take:FBTake)->int:
        """Get the count of TimeWarp in a Take.
        
        Take : The Take queried.
        return : the TimeWarp count."""
        ...
    def GetTimeWarpFromNickNumber(self,Take:FBTake,Number:int)->FBAnimationNode:
        """Get the timeWarp of specific Nick Number in a Take.
        
        Take : The Take queried.
        Number : the Nick Number of one TimeWarp.
        return : the TimeWarp of specific Nick Number."""
        ...
    def GetTimeWarpNickNumber(self,Take:FBTake,TimeWarp:FBAnimationNode)->int:
        """Get the Nick Number of one TimeWarp in a Take.
        
        Take : The Take queried.
        TimeWarp : The TimeWarp queried.
        return : the Nick Number of one TimeWarp."""
        ...
    def GetTimeWarpNickNumberAtIndex(self,Take:FBTake,Index:int)->int:
        """Get the Nick Number of one TimeWarp At specific index in a Take.
        
        Take : The Take queried.
        Index : The index a TimeWarp at.
        return : the Nick Number of one TimeWarp At specific index."""
        ...
    def RemoveTimeWarp(self,Take:FBTake,EvalProp:FBProperty):
        """Undo apply a timeWarp in a Take to an evaluation property, just disconnect the evaluation property from storing property.
        
        Take : The Take where the TimeWarp evaluation property connected is in.
        EvalProp : The evaluation property connected a TimeWarp in the storing property of one take."""
        ...
    def RemoveTimeWarpFromScene(self,TimeWarp:FBAnimationNode):
        """Remove a TimeWarp from Scene.
        
        TimeWarp : The TimeWarp to be Removed."""
        ...
    def SetTimeWarpNickNumber(self,Take:FBTake,TimeWarp:FBAnimationNode,Number:int)->bool:
        """Set the Nick Number of one TimeWarp in a Take.
        
        Take : The Take specific.
        TimeWarp : The TimeWarp specific.
        Number : The Nick Number to set.
        return : True if set successfully."""
        ...
    def TimeWarpAddToTake(self,Take:FBTake,TimeWarp:FBAnimationNode,NickNumber:int=0):
        """Add one TimeWarp to a Take.
        
        Take : The Take one TimeWarp added to.
        TimeWarp : The TimeWarp to be added.
        NickNumber : The Nick Number for the TimeWarp."""
        ...
    def TimeWarpClearTake(self,Take:FBTake):
        """Clear all TimeWarp in a Take, and removed from the DataSet.
        
        Take : The Take to be cleared."""
        ...
    def TimeWarpCopyTake(self,DstTake:FBTake,SrcTake:FBTake):
        """Copy all the TimeWarp in one Take, add to another Take.
        
        DstTake : Copy all TimeWarp to.
        SrcTake : Copy all TimeWarp from."""
        ...
    def TimeWarpCreateNew(self,Name:str)->FBAnimationNode:
        """Create a TimeWarp with a specific name.
        
        Name : The name for the TimeWarp.
        return : the TimeWarp created."""
        ...
    def TimeWarpInitTake(self,Take:FBTake):
        """Allocate container for the TimeWarp in one Take.
        
        Take : The Take allocated for."""
        ...
    def TimeWarpMergeCurveNode(self,Take:FBTake,EvalProp:FBProperty,Node:FBAnimationNode,TimeWarpNode:FBAnimationNode):
        """Merge the TimeWarp to a function curve, and Remove the connection between the storing property and the evaluation property for the TimeWarp.
        
        Take : The Take that the TimeWarp is in.
        EvalProp : the evaluation property the TimeWarp connected.
        Node : The function curve to merge on.
        TimeWarpNode : The TimeWarp to be merged."""
        ...
    def TimeWarpRename(self,Take:FBTake,TimeWarp:FBAnimationNode,NewName:str):
        """Rename a TimeWarp.
        
        Take : The Take where the timeWarp is in.
        TimeWarp : The TimeWarp to be renamed.
        NewName : The new name for the TimeWarp."""
        ...
    def TimeWarpTakeChange(self):
        """Call registered callbacks when changes related to TimeWarp happen."""
        ...
class FBToolLayoutManager(FBComponent):
    """Tool Layout Manager class.
    This class allows users to interact with Layouts.Sample Python code:
    
    >>> from pyfbsdk import *
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
    lToolLayoutMan.DeleteLayout( 'MyLayout' )"""
    def CreateLayout(self,LayoutName:str)->str:
        """Create a new layout from the current layout state.
        
        LayoutName : The new layout name to create.
        return : The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    def DeleteLayout(self,LayoutIdx:int)->bool:
        """Delete the layout with the given layout name.
        Deleting a factory layout is not permitted.
        
        LayoutName : The layout name to delete.
        return : True if the operation is successful, false otherwise."""
        ...
    def GetAutoUpdateLayout(self)->bool:
        """Get the 'Auto-update Layout' state value.
        
        return : The 'Auto-update Layout' state value."""
        ...
    def GetCurrentLayoutIdx(self)->int:
        """Get the layout index of the current layout.
        
        return : The layout index of the current layout."""
        ...
    def GetCurrentLayoutName(self)->str:
        """Get the name of the current layout.
        
        return : The name of the current layout."""
        ...
    def GetCustomLayoutCount(self)->int:
        """Get the number of custom layouts.
        
        return : The number of custom layouts."""
        ...
    def GetFactoryLayoutCount(self)->int:
        """Get the number of factory layouts.
        
        return : The number of factory layouts."""
        ...
    def GetLayoutName(self,LayoutIdx:int)->str:
        """Get the layout name associated with the given layout index.
        
        LayoutIdx : The layout index to query. The factory layouts are using negative indices.
        return : The layout name if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    def RenameLayout(self,OldLayoutName:str,NewLayoutName:str)->str:
        """Rename a layout.
        Renaming a factory layout is not permitted.
        
        OldLayoutName : The layout's name to rename.
        NewLayoutName : The new layout name.
        return : The new layout's name (could be different that the one supplied) if the operation is successful, nullptr (C++) or None (Python) otherwise."""
        ...
    def SetAutoUpdateLayout(self,AutoUpdate:bool)->bool:
        """Set the 'Auto-update Layout' state value.
        
        AutoUpdate : The 'Auto-update Layout' state value.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetCurrentLayout(self,LayoutIdx:int)->bool:
        """Set the current layout from the given layout name.
        
        LayoutName : The layout's name to set as the current layout.
        return : True if the operation is successful, false otherwise."""
        ...
    def UpdateCurrentLayout(self)->bool:
        """Update the current layout from the current layout state.
        Updating a factory layout is not permitted.
        
        return : True if the operation is successful, false otherwise."""
        ...
class FBTransportAudioManager(FBComponent):
    """Transport Tool Audio Manager class.
    This class allows users to interact with the Audio Manager of the Transport Tool."""
    def GetAudioClip(self)->FBAudioClip:
        """Get the Audio Clip displayed on the Transport Tool.
        
        return : The Audio Clip displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetAudioTrack(self)->FBStoryTrack:
        """Get the Audio Track displayed on the Transport Tool.
        
        return : The Audio Track displayed, nullptr (C++) / None (Python) if any."""
        ...
    def GetLockPitchToSpeed(self)->bool:
        """Get the 'Lock Pitch to Speed' state.
        
        return : True if the 'Lock Pitch to Speed' state is set, false otherwise."""
        ...
    def GetShowAudio(self)->bool:
        """Get the 'Show Audio' state.
        
        return : True if the 'Show Audio' state is set, false otherwise."""
        ...
    def GetShowLeftChannel(self)->bool:
        """Get the 'Show Left Channel' state.
        
        return : True if the 'Show Left Channel' state is set, false otherwise."""
        ...
    def GetShowRightChannel(self)->bool:
        """Get the 'Show Right Channel' state.
        
        return : True if the 'Show Right Channel' state is set, false otherwise."""
        ...
    def RemoveAudio(self)->bool:
        """Remove the audio clip or audio track currently displayed on the Transport Tool.
        
        return : True if the operation is successful, false otherwise."""
        ...
    def SetAudioClip(self,AudioClip:FBAudioClip)->bool:
        """Set the Audio Clip to display on the Transport Tool.
        
        AudioClip : The Audio Clip to display.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetAudioTrack(self,AudioTrack:FBStoryTrack)->bool:
        """Set the Audio Track to display on the Transport Tool.
        
        AudioTrack : The Audio Track to display.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetLockPitchToSpeed(self,Lock:bool)->bool:
        """Set the 'Lock Pitch to Speed' state.
        
        Lock : True to lock pitch to speed, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowAudio(self,Show:bool)->bool:
        """Set the 'Show Audio' state.
        
        Show : True to show the Audio waveform, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowLeftChannel(self,Show:bool)->bool:
        """Set the 'Show Left Channel' state.
        
        Show : True to show the left channel, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
    def SetShowRightChannel(self,Show:bool)->bool:
        """Set the 'Show Right Channel' state.
        
        Show : True to show the right channel, false otherwise.
        return : True if the operation is successful, false otherwise."""
        ...
class FBTreeNode(FBComponent):
    """A node in the tree view."""
    Checked:bool
    """Read Write Property: Is FBTreeNode checked."""
    Reference:property
    """Read Write Property: Data to be associated to this node."""
class FBUV():
    def CopyFrom(self,arg2:FBUV)->FBUV:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBUV)->bool:...
    def NotEqual(self,arg2:FBUV)->bool:...
class FBUndoManager(FBComponent):
    """Access to global undo and redo functionality.
    Users have the possibility of undoing and redoing actions performed using the GUI, and interacting with the undo and redo stacks with custom actions.All undo/redo related functions should only be called inside UI event callback. Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.This class cannot be used as a base class. See sample: IndividualUndoCalls.py."""
    OnRedo:FBEvent
    """Event: A redo operation will be executed."""
    OnRedoCompleted:FBEvent
    """Event: A redo operation has been executed."""
    OnUndo:FBEvent
    """Event: An undo operation will be executed."""
    OnUndoCompleted:FBEvent
    """Event: An undo operation has been executed."""
    def ActiveOperation(self)->bool:
        """Determine if an undo operation is in action.
        
        return : true the Undo Manager is performing an Undo or a Redo operation."""
        ...
    def Clear(self)->bool:
        """Clear the undo and redo stacks.
        
        return : A boolean value indicating success (true) or failure (false)."""
        ...
    def Redo(self):
        """Redo last undone action."""
        ...
    def TransactionAddModelTRS(self,Model:FBModel)->bool:
        """Add Transaction if transaction stack is open.
        Quick Function to add Model TRS in Undo Stack
        
        Model : Model to backup TRS
        return : true if add transaction successfully."""
        ...
    def TransactionAddObjectDestroy(self,Object)->bool:
        """Add Transaction if transaction stack is open.
        Function to add object to destroy in Undo Stack. No need to call FBDelete() on the object after calling this function.
        
        Object : Object to backup
        return : true if add transaction successfully."""
        ...
    def TransactionAddProperty(self,Property:FBProperty)->bool:
        """Add Transaction if transaction stack is open.
        Quick Function to add property value in Undo Stack
        
        Property : Property to backup
        return : true if add transaction successfully."""
        ...
    def TransactionBegin(self,TransactionName:str)->bool:
        """Open transaction stack for adding transactions.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.
        
        TransactionName : Name of Transaction.
        return : true if open transaction stack successfully."""
        ...
    def TransactionEnd(self)->bool:
        """Close transaction stack.
        Users should call TransactionBegin()/TransactionEnd() in pairs, Transaction stack must be closed before UI event callback return.
        
        return : true if transaction close successfully."""
        ...
    def TransactionIsOpen(self)->bool:
        """Query if transaction stack is already open.
        
        return : true if transaction is already open."""
        ...
    def Undo(self,NoRedo:bool=False):
        """Undo last action.
        
        NoRedo : If true, once the action is undone, it cannot be redone."""
        ...
class FBUserObject(FBBox):
    ...
class FBVector2d():
    """Vector2d class.
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 2 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
    
    
    Slicing is not supported by this object."""
    def CopyFrom(self,arg2:FBVector2d)->FBVector2d:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector2d)->bool:...
    def NotEqual(self,arg2:FBVector2d)->bool:...
class FBVector3d():
    """Vector3d class.
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 3 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
    
    
    Slicing is not supported by this object."""
    def CopyFrom(self,arg2:FBVector3d)->FBVector3d:...
    def CrossProduct(self,arg2:FBVector3d)->FBVector3d:...
    def Distance(self,arg2:FBVector3d)->float:...
    def DotProduct(self,arg2:FBVector3d)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector3d)->bool:...
    def Length(self)->float:...
    def Normalize(self)->FBVector3d:...
    def NotEqual(self,arg2:FBVector3d)->bool:...
    def SquareLength(self)->float:...
class FBVector4d():
    """Vector4d class.
    This class creates a list like object, which can be modified using the list protocol method. But unlike lists, its length is fixed: it always contain 4 floating point values. Thus it does not support the any list methods that would affect its length. The values within can be changed, usually via the bracket operator.
    
    >>> # Supported list protocol methods:
    color = FBColor()
    len(color)
    print color[0]
    color[0] = 1.0
    
    
    Slicing is not supported by this object."""
    def CopyFrom(self,arg2:FBVector4d)->FBVector4d:...
    def CrossProduct(self,arg2:FBVector4d)->FBVector4d:...
    def Distance(self,arg2:FBVector4d)->float:...
    def DotProduct(self,arg2:FBVector4d)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVector4d)->bool:...
    def Length(self)->float:...
    def Normalize(self)->FBVector4d:...
    def NotEqual(self,arg2:FBVector4d)->bool:...
    def SquareLength(self)->float:...
class FBVertex():
    """Vertex class.
    Similar in use to FBVector4d
    
    >>> # Supported list protocol methods:
    v = FBVertex()
    len(v)
    print v[0]
    v[0] = 1.0
    
    
    Slicing is not supported by this object."""
    def CopyFrom(self,arg2:FBVertex)->FBVertex:...
    def CrossProduct(self,arg2:FBVertex)->FBVertex:...
    def Distance(self,arg2:FBVertex)->float:...
    def DotProduct(self,arg2:FBVertex)->float:...
    def GetBufferAddress(self)->int:...
    def GetList(self)->list:...
    def IsEqual(self,arg2:FBVertex)->bool:...
    def Length(self)->float:...
    def Normalize(self)->FBVertex:...
    def NotEqual(self,arg2:FBVertex)->bool:...
    def SquareLength(self)->float:...
class FBVideo(FBBox):
    """Video media class.
    Similar to the FBModel class, the FBVideo class serves as a general media class for images, video clips and video memory, as well as the possibility of custom formats and custom live cards.To have a valid FBVideo object, it must be constructed with a string pointing to a valid media file. After the creation, the method 'IsValid()' should be used to confirm the object's status. An invalid object cannot be used or interact with any other application object. The only property that can be read and modified is its 'Filename'. To make convert an invalid FBVideo object into a valid one, simply change its Filename property to point to a supported media file. See sample: DeleteUnusedMedia.py."""
    KeepOnGPU:bool
    """Read Write Property: Don't auto flush from GPU if true. session runtime flag, won't be saved."""
class FBVideoClip(FBVideo):
    """See sample: VideoClip.py."""
    CurrentFrame:property
    """Read Write Property: Current frame."""
    CurrentFrameTime:property
    """Read Write Property: Current time in clip."""
    CurrentFrameTimeCode:property
    """Read Only Property: Embedded timecode from current frame in clip. Use the method GetEmbeddedTimecode to get the timecode of a different frame than the current frame."""
    Filename:property
    """Read Write Property: Filename of media."""
    Format:property
    """Read Only Property: Video format."""
    FrameRate:property
    """Read Write Property: Frame rate."""
    FrameTime:property
    """Read Only Property: Inverse of FPS, time per frame"""
    FreeRunning:property
    """Read Write Property: Is free Running on?"""
    Height:property
    """Read Only Property: Height of image."""
    InterlaceMode:property
    """Read Write Property: Interlace mode."""
    LastFrame:property
    """Read Only Property: Last frame in clip."""
    LastFrameTime:property
    """Read Only Property: Time of last frame"""
    Loop:property
    """Read Write Property: Loop video clip?"""
    PlaySpeed:property
    """Read Write Property: Playback speed."""
    PowerOfTwoHeight:property
    """Read Only Property: Closest power of two value superior to height of image."""
    PowerOfTwoWidth:property
    """Read Only Property: Closest power of two value superior to width of image."""
    ProxyMode:property
    """Read Write Property: Proxy mode."""
    RelativePath:property
    """Read Only Property: Relative path of media."""
    StartFrame:property
    """Read Write Property: Frame to begin video playback from."""
    StopFrame:property
    """Read Write Property: Frame to end video playback at."""
    StorageMode:property
    """Read Write Property: Storage mode."""
    TimeOffset:property
    """Read Write Property: Temporal offset for beginning of video."""
    Width:property
    """Read Only Property: Width of image."""
    def DrawImage(self,X:object,Y:object,W:object,H:object,Frame:object):
        """Draw a frame of the image to the current view.
        
        X : X position of image (default=0).
        Y : Y position of image (default=0).
        W : Width of image (default=-1).
        H : Height of image (default=-1).
        Frame : Frame to draw (default=-1)."""
        ...
    def GetEmbeddedTimecode(self,Frame:object)->FBTimeCode:
        """Get the embedded timecode associated to a video clip frame.
        
        Frame : Video clip frame to get timecode for.
        TimeCode : The timecode object being filled by this method.
        return : True if an embedded timecode is retrieved from the video clip, false otherwise. (Python: If no embedded timecode is retrieved, returns an FBTimeCode object with its time set to FBTime::Infinity)."""
        ...
    def GetTextureID(self)->int:
        """Get the texture ID.
        
        return : ID of the texture"""
        ...
    def IsValid(self)->bool:
        """Verifies the validity of the FBVideo object.
        
        return : true if data is valid."""
        ...
class FBVideoClipImage(FBVideoClip):
    ImageSequence:property
    """Read Write Property: Clip is an image sequence?"""
    MaxMipMapResolution:property
    """Read Write Property: Maximum MipMap resolution will be loaded into GPU."""
    UseSystemFrameRate:property
    """Read Write Property: Clip is using system frame rate?"""
class FBVideoCodecManager():
    """Video Codec manager class.
    Use to set or get codec used and codec params See samples: codecExamples.py, render.py."""
    VideoCodecMode:FBVideoCodecMode
    """Read Write Property: This decide how the system behaves when ask to render a file (codec dialog, uncompress, use default codec)"""
    def GetCodecIdList(self,FileFormatInfo:str)->list:
        """GetCodecIdList.
        Get all codec id available for a given file format.
        
        FileFormatInfo : file format description string (AVI, MOV...)
        CodecList : Codec list id"""
        ...
    def GetDefaultCodec(self,FileFormatInfo:str)->str:
        """GetDefaultCodec.
        Get the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault
        
        FileFormatInfo : file format description string (AVI, MOV...)"""
        ...
    def RegisterExternalVideoFormat(self,FormatSuffix:str)->bool:
        """Register external video format suffix.
        Only alphabetic and number is allowed in provided suffix, and can not be empty suffix or the system exist suffixes. This will allow this suffix to be appeared in the filters of file dialog when importing video, also allow to create a texture/video object with a path containing this suffix via SDK. However it will the custom SDK plug-in developer's responsibility to load the file into memory.
        
        FormatSuffix : Suffix/File extension of external video file format
        return : true if register successful"""
        ...
    def SetDefaultCodec(self,FileFormatInfo:str,CodecId:str):
        """SetDefaultCodec.
        Set the default codec id for a given file format. This is the codec that will be used if codec mode is FBVideoCodecUseDefault
        
        FileFormatInfo : file format description string (AVI, MOV...)
        CodecId : the codec id to set as default"""
        ...
class FBVideoGrabOptions():
    """Video Grabbing Options.
    Contain options to control how the grabbing process will occur."""
    AntiAliasing:bool
    """Read Write Property: If true, video frames will be anti-aliased."""
    AudioCustomStandaloneFileName:property
    """Destination for the custom audio standalone file, if mAudioUseCustomStandaloneFileName is set to true."""
    AudioOutputLocation:FBAudioOutputLocation
    """Audio output location when rendering using a video format (for still image formats & SWF (Flash) format, the audio is always rendered in a standalone file)."""
    AudioRenderFormat:int
    """Read Write Property: Audio render format."""
    AudioUseCustomStandaloneFileName:bool
    """If true and if the audio is rendered in a standalone output file, the audio file is generated at the file location specified by mAudioCustomStandaloneFileName, otherwise the audio file is generated in the same directory as the rendered images/video files based on their names."""
    BitsPerPixel:FBVideoRenderDepth
    """Read Write Property: Video grab color depth."""
    CameraResolution:FBCameraResolutionMode
    """Read Write Property: Camera Resolution."""
    FieldMode:FBVideoRenderFieldMode
    """Read Write Property: Video grab field mode."""
    OutputFileName:property
    """Read Write Property: Grabbing destination file."""
    RenderAudio:bool
    """Read Write Property: If true and there's audio in the scene, render the audio as well."""
    RendererCallbackIndex:int
    RendererCallbackPrefIndex:int
    ShowCameraLabel:bool
    """Read Write Property: If true, display camera label information."""
    ShowSafeArea:bool
    """Read Write Property: If true, display safe area."""
    ShowTimeCode:bool
    """Read Write Property: If true, display time code information."""
    StereoDisplayMode:FBStereoDisplayMode
    StillImageCompression:int
    """Property: Compression ratio for image(jpg) 0-100 where 0=Greatest compression, 100=Least Compression."""
    TimeSpan:FBTimeSpan
    """Read Write Property: Start and stop selection time to grab."""
    TimeSteps:FBTime
    """Read Write Property: Time step length between each grab."""
    ViewingMode:FBVideoRenderViewingMode
    """Read Write Property: Video grab viewing mode."""
class FBVideoGrabber(FBComponent):
    """Video Grabber class.
    Used to grab video frames generated with the FBRenderer. See samples: codecExamples.py, render.py, RenderLayers.py, JpegRender.py."""
    def BeginGrab(self)->bool:
        """BeginGrab.
        Begin video grabbing session.
        
        return : True if we can begin the grab session."""
        ...
    def EndGrab(self):
        """EndGrab.
        Close video grabbing session."""
        ...
    def GetLastErrorMsg(self)->str:
        """GetLastErrorMsg.
        
        return : If an error occured, this function returns the last error message, otherwise an empty string."""
        ...
    def GetOptions(self)->FBVideoGrabOptions:
        """GetOptions give you a copy of current grabbing options.
        
        return : Struct that contain all grabbing options."""
        ...
    def GetStatistics(self)->object:
        """GetStatistics.
        
        return : Struct that contain all grabbing statistics."""
        ...
    def Grab(self):
        """Grab.
        Grab all specified video frames."""
        ...
    def RenderSnapshot(self,Width:int=-1,Height:int=-1,CameraLabel:bool=False,TimeCode:bool=False,SafeArea:bool=False,Axis:bool=False,Grid:bool=False,FrontPlate:bool=False,BackPlate:bool=False)->FBImage:
        """Render a snapshot of the actual display.
        
        Width : int
        Height : int
        CameraLabel : bool
        TimeCode : bool
        SafeArea : bool
        Axis : bool
        Grid : bool
        FrontPlate : bool
        BackPlate : bool
        return : An FBimage containing data of the rendered snapshot."""
        ...
    def ResetOptions(self):
        """SetDefaultOptions.
        This function reset all grabbing options to the default value."""
        ...
    def SetOptions(self,Options:FBVideoGrabOptions):
        """SetOptions.
        
        Options : Struct that contain all grabbing options."""
        ...
class FBVideoIn(FBVideo):
    """Basic video input class, supporting webcam and DV device.
    See sample: VideoInput.py."""
    FilePath:str
    """Read Write Property: Location of the generated movie file after a recording session."""
    Online:bool
    """Read Write Property: If true, the device is online and will display the current video feed."""
    RecordAudio:bool
    """Read Write Property: If true, the device will also record audio during a recording session."""
    Recording:bool
    """Read Write Property: If true, the device will record during a recording session."""
    def LiveGetCompressor(self)->int:
        """Get the current compressor index.
        
        return : Index of the current compressor."""
        ...
    def LiveGetCompressorCount(self)->int:
        """Get the compressor count.
        
        return : Number of available compressor."""
        ...
    def LiveGetCompressorName(self,CompressorIndex:int)->str:
        """Get the compressor name at a particular index.
        
        CompressorIndex : int
        return : Name of the compressor. If theCompressorIndex is higher than the number of compressor, the function will return NULL."""
        ...
    def LiveGetResolutionFR(self)->int:
        """Get the current resolution and frame rate index.
        
        return : Index of the current resolution and frame rate."""
        ...
    def LiveGetResolutionFRCount(self)->int:
        """Get the number of resolution and frame rate available for the device.
        
        return : Number of available resolution and frame rate."""
        ...
    def LiveGetResolutionFRName(self,Index:int)->str:
        """Get the resolution and frame rate string description at the specified index.
        
        Index : Index of the resolution and frame rate.
        return : Name of the resolution and frame rate."""
        ...
    def LiveGetType(self)->FBVideoLiveType:
        """Get the type of the video input device.
        
        return : Type of the video input device."""
        ...
    def LiveSetCompressor(self,CompressorIndex:int)->bool:
        """Set the current compressor to be used when recording.
        
        CompressorIndex : Index of the compressor.
        return : True if successful."""
        ...
    def LiveSetResolutionFR(self,Index:int):
        """Set the current resolution and frame rate for the device.
        
        Index : Index of the resolution and frame rate."""
        ...
class FBVideoMemory(FBVideo):
    """FBVideoMemory allow external media source (which can't be supported by MoBu natively)  User could create / update OGL texture (GL_TEXTURE_2D type) externally, and pass in GL texture object id to TextureOGLId property.See 'Scripts/Samples/Video/VideoMemory.py' for usage example.
    See sample: VideoMemory.py."""
    TextureOGLId:int
    """Read Write Property: OpenGL texture buffer object id (GL_TEXTURE_2D type)."""
    def SetObjectImageSize(self,W:int,H:int):
        """Set image size to allow MoBu preview texture with proper dimension / aspect.
        
        W : Width of image.
        H : Height of image."""
        ...
class FBVideoOut(FBVideo):
    """Video media class.
    See sample: VideoOutput.py."""
    Online:bool
    """Read Write Property: If true, the device is online and will output display."""
class FBViewingOptions():
    """Viewing options for rendering.
    The FBRenderer allows to get and set those options."""
    DisplayMode:property
    """Read Write Property: Current Shading mode"""
    DisplayWhat:int
    """Read Write Property: current display mask."""
    PaneIndex:int
    """Current Viewer Pane being rendered.
    
    return : Index of the pane being rendered."""
    PickingMode:FBPickingMode
    """Read Write Property: Reference to the current picking mode."""
    ShowCameraLabel:bool
    """Read Write Property: Show Camera Label when rendering."""
    ShowSafeArea:bool
    """Read Write Property: Show Safe Area when rendering."""
    ShowTimeCode:bool
    """Read Write Property: Show Time Code when rendering."""
    StereoDisplayMode:FBStereoDisplayMode
    """Get a reference to the stereo display mode.
    
    return : Reference to the current stereo display mode."""
    def InPicking(self)->bool:...
    def IsInColorBufferPicking(self)->bool:
        """Is the rendering routine during picking status with GL color buffer method."""
        ...
    def IsInSelectionBufferPicking(self)->bool:
        """Is the rendering routine during picking status with GL selection buffer method."""
        ...
    def RenderCallbackPrefIndex(self)->int:
        """Current Render callback Settings Index."""
        ...
class FBVisualComponent(FBComponent):
    """Visual Component base class.
    All of the user interface elements available in the SDK derive from this class."""
    BorderCaption:property
    """Read Write Property: Caption to display in border."""
    BorderCornerRadius:property
    """Read Write Property: Corner radius (rounded)."""
    BorderInSet:property
    """Read Write Property: Is border inset?"""
    BorderMaxAngle:property
    """Read Write Property: Max angle for rounding."""
    BorderShowCaption:property
    """Read Write Property: Show caption?"""
    BorderSpacing:property
    """Read Write Property: Spacing of border."""
    BorderStyle:property
    """Read Write Property: Style of border."""
    BorderWidth:property
    """Read Write Property: Width of border."""
    Caption:str
    """Property: Widget caption."""
    Enabled:bool
    """Read Write Property: Is visual enabled?"""
    Height:int
    """Read Write Property: Height."""
    Hint:str
    """Read Write Property: Hint to show."""
    Left:int
    """Read Write Property: Left coordinate."""
    ReadOnly:bool
    """Read Write Property: Is visual component read only?"""
    RegionAttachToHeight:property
    """Read Write Property: Height Attachment source."""
    RegionAttachToWidth:property
    """Read Write Property: Width Attachment source."""
    RegionAttachToX:property
    """Read Write Property X Attachment source."""
    RegionAttachToY:property
    """Read Write Property: Y Attachment source."""
    RegionAttachTypeHeight:property
    """Read Write Property: Height Attachment type."""
    RegionAttachTypeWidth:property
    """Read Write Property: Width Attachment type."""
    RegionAttachTypeX:property
    """Read Write Property: X Attachment type."""
    RegionAttachTypeY:property
    """Read Write Property: Y Attachment type."""
    RegionName:property
    """Read Write Property: Region name."""
    RegionOffsetHeight:property
    """Read Write Property: Region height offset."""
    RegionOffsetWidth:property
    """Read Write Property: Region width offset."""
    RegionOffsetX:property
    """Read Write Property: Region X offset."""
    RegionOffsetY:property
    """Read Write Property: Region Y offset."""
    RegionPosMaxX:property
    """Read Write Property: Region X position Max"""
    RegionPosMaxY:property
    """Read Write Property: Region Y position Max"""
    RegionPosMinX:property
    """Read Write Property: Region X position Min"""
    RegionPosMinY:property
    """Read Write Property: Region Y position Min"""
    RegionRatioHeight:property
    """Read Write Property: Ratio for Height attachment."""
    RegionRatioWidth:property
    """Read Write Property: Ratio for Width attachment."""
    RegionRatioX:property
    """Read Write Property: Ratio for X attachment."""
    RegionRatioY:property
    """Read Write Property: Ratio for Y attachment."""
    Top:int
    """Read Write Property: Top coordinate."""
    Visible:bool
    """Read Write Property: Is visual component visible?"""
    Width:int
    """Read Write Property: Width."""
    def AddChild(self,Child:FBVisualComponent,Id:int=0)->bool:
        """Add a child component.
        
        Child : Visual component to add as a child.
        Id : User reference number to associate withChild(default=0).
        return : Operation was successful (true or false)."""
        ...
    def GetChild(self,Id:int=0)->FBVisualComponent:
        """Get a child component.
        
        Id : User reference number to look for child with(default=0).
        return : Handle to child (NULL if not found)."""
        ...
    def GetQWidgetAddress(self)->int:
        """Get internal QWidget.
        
        return : Handle to internal QWidget object."""
        ...
    def IsView(self)->bool:
        """Is component a view?
        
        return : true if component is a view."""
        ...
    def Refresh(self,Now:bool=False):
        """Refresh component.
        
        Now : Refresh immediately if true (default = false)."""
        ...
    def ViewExpose(self):
        """Exposed view callback function."""
        ...
    def ViewInput(self,MouseX:int,MouseY:int,Action:FBInputType,ButtonKey:int,Modifier:int):
        """Input callback function.
        
        MouseX : Mouse X position.
        MouseY : Mouse Y position.
        Action : Mouse action.
        ButtonKey : Keyboard input.
        Modifier : Keyboard input modifier."""
        ...
class FBVisualContainer(FBVisualComponent):
    """Used to create a container for a tool UI.
    See samples: Container.py, PropertyDrop.py, TutorialBox.py."""
    IconPosition:FBIconPosition
    """Read Write Property: Where the icon is positioned for the items."""
    ItemHeight:int
    """Read Write Property: Item height."""
    ItemIndex:int
    """Read Write Property: Current item selected."""
    ItemWidth:int
    """Read Write Property: Item width."""
    ItemWrap:bool
    """Read Write Property: Are items wrapped when enough space is available?"""
    Items:FBStringList
    """List: Names of items in container."""
    OnChange:FBEvent
    """Event: Container contents changed."""
    OnDblClick:FBEvent
    """Event: Double click."""
    OnDragAndDrop:FBEvent
    """Event: Drag and Drop event."""
    Orientation:FBOrientation
    """Read Write Property: Orientation of container."""
    def GetSelection(self)->int:
        """Get the selected item.
        
        return : Index of current selection."""
        ...
    def ItemIconSet(self,Ref:object,Image:FBImage,UseACopyOfTheImage:bool=True)->bool:
        """Set an item's icon.
        
        Ref : Reference to item in container.
        Filename : Name of file where image is located.
        return : Operation was successful (true or false)."""
        ...
    def ItemNameEdit(self,Ref:object)->bool:
        """Edit a container item.
        
        Ref : Reference of container to edit.
        return : Operation was successful (true or false)."""
        ...
class FBView(FBVisualComponent):
    """Generic view."""
    DoubleBuffer:bool
    """Read Only Property: Indicates if the view is double buffered."""
    GraphicOGL:bool
    """Read Only Property: Indicates if the view is OpenGL."""
    def DrawString(self,Text:str,X:float,Y:float,Enable:int=-1):
        """Draw a string in the view.
        
        Text : Text to draw.
        X : X position of string.
        Y : Y position of string.
        Enable : Is string enabled? (default =-1)"""
        ...
    def SetViewport(self,X:int,Y:int,W:int,H:int)->bool:
        """Set view's viewport.
        
        X : Viewport X value.
        Y : Viewport Y value.
        W : Viewport W (width) value.
        H : Viewport H (height) value.
        return : Operation was successful (true or false)."""
        ...
class FBTree(FBVisualComponent):
    """Tree list view.
    See sample: Tree.py."""
    AllowCollapse:bool
    """Read Write Property: When OnCollapsing occurs, set this to true to allow collapse."""
    AllowExpansion:bool
    """Read Write Property: When OnExpanding occurs, set this to true to allow expansion."""
    AutoExpandOnDblClick:bool
    """Read Write Property: Allow automatic expand on double click, default is false."""
    AutoExpandOnDragOver:bool
    """Read Write Property: Allow automatic expand on drag over, default is false."""
    AutoScroll:bool
    """Read Write Property: If AutoScroll property is True then the tree window will be automatically scrolled when the user drags item(s) over the boundaries of the tree."""
    AutoScrollOnExpand:bool
    """Read Write Property: Allow automatic scroll on expand, default is true."""
    CheckBoxes:bool
    """Read Write Property: Draw check boxe for each node."""
    DeselectOnCollapse:bool
    """Read Write Property: Tells whether node are deselected if parent node is collapsed."""
    EditNodeOn2Select:bool
    """Read Write Property: Set to true, to allow automatic node editing on second select."""
    HighlightOnRightClick:bool
    """Read Write Property: Hightlight node on right click."""
    Indent:int
    """Read Write Property: Use Indent to determine how far child nodes are indented from their parent nodes when the parent is expanded."""
    ItemHeight:int
    """Read Write Property: Height of an item."""
    MultiDrag:bool
    """Read Write Property: Tells whether multiple drag/drop is allowed or not."""
    MultiSelect:bool
    """Read Write Property: Tells whether multiple selection is allowed or not."""
    NoSelectOnDrag:bool
    """Read Write Property: Tells whether node are selected if drag is start and node is not already selected."""
    NoSelectOnRightClick:bool
    """Read Write Property: Tells whether node are selected if right click on node."""
    OnChange:FBEvent
    """Event: Change of the selection."""
    OnClick:FBEvent
    """Event: Click on a node of the tree. Use OnSelect."""
    OnClickCheck:FBEvent
    """Event: Click on a node checkbox of the tree."""
    OnCollapsed:FBEvent
    """Event: Click on the '-' sign before a non-leaf node."""
    OnCollapsing:FBEvent
    """Event: Fired before the node collapse. To refuse collapsing, set AllowCollapse to false."""
    OnDblClick:FBEvent
    """Event: Double-Click on a node of the tree. Use FBEventTreeSelect to cast event."""
    OnDragAndDrop:FBEvent
    """Event: Drag and drop of an element."""
    OnExpanded:FBEvent
    """Event: Click on the '+' sign before a non-leaf node"""
    OnExpanding:FBEvent
    """Event: Is fired before the node expand. To refuse expanding set AllowExpansion to false."""
    OnSelect:FBEvent
    """Event: A node was selected. Use FBEventTreeSelect to cast event."""
    SelectedCount:int
    """Read Only Property: Count of selected items."""
    SelectedNodes:FBPropertyListTreeNode
    """Read Only Property: List of selected nodes."""
    SelectionActive:bool
    """Read Write Property: Tells whether selection is allowed or not."""
    ShowLines:bool
    """Read Write Property: On node selection, will draw entire line selected"""
    TreeHeight:int
    """Read Only Property: Height of the tree."""
    TreeWidth:int
    """Read Only Property: Width of the tree."""
    VisibleItemCount:int
    """Read Only Property: Count of visible items."""
    def Clear(self):
        """Clear the tree (remove all nodes)."""
        ...
    def GetRoot(self)->FBTreeNode:
        """Get the root node.
        
        return : the root node of the tree."""
        ...
    def InsertLast(self,Node:FBTreeNode,Name:str)->FBTreeNode:
        """Insert node at the end.
        
        Node : Node under which the new node will appear.
        Name : Text to display for this node.
        return : the newly created node."""
        ...
class FBThermometer(FBVisualComponent):
    """Thermometer.
    See sample: Thermometer.py."""
    Max:float
    """Read Write Property: Maximum value."""
    Min:float
    """Read Write Property: Minimum value."""
    Value:float
    """Read Write Property: Current value."""
    def Clear(self):
        """Reset bounds and value."""
        ...
class FBTabPanel(FBVisualComponent):
    """Tab panel.
    See sample: TabPanel.py."""
    ItemIndex:int
    """Read Write Property: Current tab panel."""
    Items:FBStringList
    """List: Names for tab panels."""
    Layout:FBLayout
    """Read Write Property: Layout for current tab panel."""
    OnChange:FBEvent
    """Event: Tab panel change."""
    TabStyle:int
    """Read Write Property: Style of the tab panel, 0 creates normal tabs, 1 creates buttons to activate tabs."""
class FBSpread(FBVisualComponent):
    """Base spreadsheet class.
    See samples: ActionScriptMgr.py, KeyboardMapper.py, Spread.py."""
    Column:int
    """Read Write Property: Current column."""
    MultiSelect:bool
    """Read Write Property: Can there be multiple selections?"""
    OnCellChange:FBEvent
    """Event: Cell value changed."""
    OnColumnClick:FBEvent
    """Event: Column clicked."""
    OnDragAndDrop:FBEvent
    """Event: Drag and drop event."""
    OnRowClick:FBEvent
    """Event: Row clicked."""
    Row:property
    """Read Write Property: Current row."""
    def Clear(self):
        """Clear spreadsheet This function will empty spreadsheet of all its rows, columns and cells."""
        ...
    def ColumnAdd(self,String:str,Ref:object=0):
        """Add a column.
        
        String : Text to display with column.
        Ref : User-define column reference number(default=0)."""
        ...
    def GetCellValue(self,Row:object,Column:object)->object:
        """Get a cell's value.
        
        Row : Row of cell.
        Column : Column of cell."""
        ...
    def GetCellView(self,Ref:object,Column:int)->object:
        """Get a cell's internal toolkit view.
        
        Ref : Row of cell.
        Column : Column of cell.
        View : Handle of view."""
        ...
    def GetColumn(self,Column:int)->FBSpreadColumn:
        """Get a column from a column number.
        
        Column : Column number.
        return : A copy of column."""
        ...
    def GetCurrentCell(self)->FBSpreadCell:
        """Get the current cell.
        
        return : A copy of the the current cell."""
        ...
    def GetRow(self,Ref:object)->FBSpreadRow:
        """Get a row from a row reference.
        
        Ref : Reference to a row.
        return : A copy of the row."""
        ...
    def GetSpreadCell(self,Ref:object,Column:object)->object:
        """Get a cell from row and column numbers.
        
        Ref : Row reference.
        Column : Column number.
        return : A copy of the cell."""
        ...
    def RowAdd(self,String:str,Ref:object=0):
        """Add a row.
        
        String : Text to display with row.
        Ref : User-defined reference for row(default=0)."""
        ...
    def RowSort(self,Ascending:bool=True):
        """Sort rows.
        
        Ascending : If true, sort ascending."""
        ...
    def SetCellValue(self,Row:object,Column:object,Value:object):
        """Set a cell's value.
        This will also set the FBSpreadCell.Style to the type ofValue (kFBCellStyleInteger ifValue is an int, kFBCellStyleDouble ifValue is a float, kFBCellStyleString ifValue is a str).
        
        Row : Row of cell.
        Column : Column of cell.
        Value : Value of the cell (can be str, int or float)"""
        ...
    def SetCellView(self,Ref:object,Column:int,View):
        """Set a cell's internal toolkit view.
        
        Ref : Row of cell.
        Column : Column of cell.
        View : View to use to set cell's view."""
        ...
class FBSlider(FBVisualComponent):
    """Slider.
    See samples: BlendShape_Editor.py, Slider.py."""
    Max:float
    """Read Write Property: Maximum value."""
    Min:float
    """Read Write Property: Minimum value."""
    OnChange:FBEvent
    """Event: Slider value changed."""
    OnTransaction:FBEvent
    """Event: Transaction begin/end (continuous value changes). This event property doesn't exist in pyfbsdk."""
    Orientation:FBOrientation
    """Read Write Property: Slider orientation."""
    Value:float
    """Read Write Property: Current value."""
class FBScrollBox(FBVisualComponent):
    """Scroll Box.
    This class provides a layout that will be automatically managed with a scrollbar according to the specified width and height. This provides a way to add dynamic UI control. See sample: Scrollbox.py."""
    Content:FBLayout
    """Read Property: an empty layout in which you can add scrollable content."""
    def SetContentSize(self,arg2:object,arg3:object):...
class FBPropertyConnectionEditor(FBVisualComponent):
    """Property Connection Editor."""
    Property:property
    """Read Write Property: Property to edit connections. Set to NULL to disable."""
    def PopupList(self):
        """Launch a list of connected objects."""
        ...
    def PopupTree(self):
        """Launch a tree of object connections."""
        ...
class FBPlotPopup(FBVisualComponent):
    """Plot Popup (for setting options only).
    See sample: FBPlotPopup.py."""
    EnableEvaluateDeformation:bool
    """Read Write Property: Enable Evaluate Deformation option for popup."""
    EnablePlotAuxEffectors:bool
    """Read Write Property: Enable Plot Aux Effectors option for popup."""
    EnablePlotCharacterExtension:bool
    """Read Write Property: Enable Plot Character Extension option for popup."""
    EnablePlotLockedProperties:bool
    """Read Write Property: Enable Plot Locked Properties option for popup."""
    EnablePlotTranslationOnRootOnly:bool
    """Read Write Property: Enable Plot Translation On Root Only option for popup."""
    EnableSmartPlotControls:bool
    """Read Write Property: Enable Smart Plot option for popup."""
    def GetPlotOptions(self)->FBPlotOptions:
        """Get plot options.
        
        return : plot options."""
        ...
    def Popup(self,WindowName:str)->bool:
        """Execute plot popup.
        
        WindowName : str
        return : true if OK is clicked by user."""
        ...
    def SetPlotOptions(self,PlotOptions:FBPlotOptions):
        """Set plot options.
        
        PlotOptions : Set the plot options that will be used when displaying the plot popup. First use the GetPlotOptions(), change the options and use the SetPlotOptions() to set them before calling the Popup() function."""
        ...
class FBList(FBVisualComponent):
    """List of items.
    See samples: List.py, ToolCommunicationReceiver.py."""
    ExtendedSelect:bool
    """Read Write Property: Extended selection state?"""
    ItemIndex:int
    """Read Write Property: Current item index."""
    Items:FBStringList
    """List: Names of items in list."""
    MultiSelect:bool
    """Read Write Property: Can multiple items be selected?"""
    OnChange:FBEvent
    """Event: List changed."""
    OnDragAndDrop:FBEvent
    """Event: Drag and drop event."""
    Style:FBListStyle
    """Read Write Property: Style or direction of list."""
    def IsSelected(self,Index:int)->bool:
        """Returns whether or not the itemIndex is currently selected.
        
        Index : Index to see if select or not.
        return : true if item atIndex is selected."""
        ...
class FBLayoutRegion(FBVisualComponent):
    """Layout region."""
    ...
class FBLayout(FBVisualComponent):
    """Used to build the user interface.
    Layouts manage areas of the screen called regions. Regions contain UI components such as buttons, viewers, and edit boxes. Regions are added to layouts. When a UI component is bound to a region, the region defines how big it is and how it behaves when the layout is resized.Types of Layouts Device Constraint Manipulator Shader A region is first defined using the FBLayout::AddRegion() function. Once a region is defined and the corresponding UI component is created, and the component is bound to its region with FBLayout::SetControl(). You can use the FBSystem::OnUIIdle() in your layout to update real-time UI components such as guages and status indicators. In Python, FBBoxLayout and FBGridLayout take care of most of the region handling. They are used to create basic control layouts for simple tools. If you have a lot of content you can use FBScrollBox to manage it. For an example, see the Python sample Scrollbox.py.* Also see the Python sample Layout.py, and the C++ sample ortooluidemo. See samples: KeyboardMapper.py, ShotTrackSetupTool.py, Attach.py, Border.py, Layout.py."""
    OnIdle:FBEvent
    """Event: Idle."""
    OnInput:FBEvent
    """Event: Input."""
    OnPaint:FBEvent
    """Event: Paint layout."""
    OnResize:FBEvent
    """Event: Resize layout."""
    OnShow:FBEvent
    """Event: Show layout."""
    def AddRegion(self,Name:str,Title:str,X:int,XType:FBAttachType,XRelative:str,MultX:float)->bool:
        """Add a region to the layout.
        
        Name : Name of region.
        Title : Title to display.
        X : X: Position.
        XType : X: Type of attachment.
        XRelative : X: Item to attach to.
        MultX : X: Multiplier of relative value.
        Y : Y: Position.
        YType : Y: Type of attachment.
        YRelative : Y: Item to attach to.
        MultY : Y: Multiplier of relative value.
        W : W: Width of region.
        WType : W: Type of attachment.
        WRelative : W: Item to attach to.
        MultW : W: Multiplier of relative value.
        H : H: Height of region.
        HType : H: Type of attachment.
        HRelative : H: Item to attach to.
        MultH : H: Multiplier of relative value.
        return : Operation was successful (true or false)."""
        ...
    def ClearControl(self,Name:str):
        """Remove a control from a region in a visual component.
        
        Name : Name of region to remove control."""
        ...
    def GetControl(self,Name:str)->FBVisualComponent:
        """Get control of a region in a visual component.
        
        Name : Name of region to find.
        return : The component if it is found."""
        ...
    def GetRegion(self,Name:str)->bool:
        """Verify if a region withName exists.
        
        Name : Name of region to check.
        return : Operation was successful (true or false)."""
        ...
    def GetRegionPositions(self,Name:str,Computed:bool,X:int,Y:int,W:int=None,H:int=None)->bool:
        """Get regionName information (position and size)
        
        Name : Name of region.
        Computed : Is the information retrieved relative or absolute?
        X : Position in X of the region.
        Y : Position in Y of the region.
        W : Width of the region.
        H : Height of the region.
        return : Operation was successful (true or false)."""
        ...
    def GetSplitStyle(self,Name:str)->FBSplitStyle:
        """Get a region's splitstyle.
        
        Name : Name of Region to get splitstyle from.
        return : Split style of specified region."""
        ...
    def MoveRegion(self,Name:str,X:int,Y:int)->bool:
        """Move a region.
        
        Name : Name of region to move.
        X : New X position.
        Y : New Y position.
        return : Operation was successful (true or false)."""
        ...
    def RemoveRegion(self,Name:str)->bool:
        """Remove a region.
        
        Name : Name of region to remove.
        return : Operation was successful (true or false)."""
        ...
    def RenameRegion(self,OldName:str,NewName:str)->bool:
        """Rename a region.
        
        OldName : Region's old name.
        NewName : Region's new name.
        return : Operation was successful (true or false)."""
        ...
    def Restructure(self,NoMove:bool):
        """Force a recomputation of all region placements in the layout.
        
        NoMove : bool"""
        ...
    def SetAutoRestructure(self,AutoRestructure:bool):
        """Suspend all automatic layout recomputation.
        
        AutoRestructure : If true, Suspend all automatic layout recomputation, else restore it."""
        ...
    def SetBorder(self,Name:str,Type:FBBorderStyle,ShowTitle:bool,InSet:bool,Width:int,Spacing:int,MaxAngle:float,CornerRadius:int)->bool:
        """Set border properties for a region.
        
        Name : Name of Region to change border properties.
        Type : Border style to use.
        ShowTitle : Show region title?
        InSet : Is region inset?
        Width : Border width.
        Spacing : Border spacing.
        MaxAngle : Max angle for rounding.
        CornerRadius : Corner radius for rounding.
        return : Operation was successful (true or false)."""
        ...
    def SetControl(self,Name:str,Component:FBVisualComponent)->bool:
        """Name : str
        Component : FBVisualComponent"""
        ...
    def SetRegionTitle(self,Name:str,Title:str)->bool:
        """Set a region's title.
        
        Name : Name of region to change title.
        Title : New title for region.
        return : Operation was successful (true or false)."""
        ...
    def SetSplitStyle(self,Name:str,RegionType:FBSplitStyle)->bool:
        """Set a region's splitstyle.
        
        Name : Name of Region to set splitstyle.
        RegionType : Split style give to region.
        return : Operation was successful (true or false)."""
        ...
    def SetView(self,Name:str,Component:FBVisualComponent)->bool:
        """Name : str
        Component : FBVisualComponent"""
        ...
    def SizeRegion(self,Name:str,W:int,H:int)->bool:
        """Change a region's size.
        
        Name : Name of region to resize.
        W : New region width.
        H : New region height.
        return : Operation was successful (true or false)."""
        ...
class FBLabel(FBVisualComponent):
    """Text label.
    See sample: Label.py."""
    Justify:FBTextJustify
    """Read Write Property: Text justification for label."""
    Style:FBTextStyle
    """Read Write Property: Text style appearance."""
    WordWrap:bool
    """Read Write Property: Enable wordwrap on text drawing."""
class FBTool(FBLayout):
    """Tool class.
    See samples: MBFileRefDemo.py, CloseTool.py, MoveResizeToolExample.py, SafeToolCreationExample.py, ToolCommunicationReceiver.py, ToolNativeWidgetHolder.py."""
    DisplayName:str
    """Read Write Property: Tool Display Name (Caption on the tool's title bar)"""
    MaxSizeX:property
    """Read Property: Maximum Size in X (Disabled in this version). A value of -1 means no maximum size."""
    MaxSizeY:property
    """Maximum Size in Y (Disabled in this version). A value of -1 means no maximum size."""
    MinSizeX:property
    """Read Property: Minimum Size in X. A value of -1 means no minimum value."""
    MinSizeY:property
    """Read Property: Minimum Size in Y. A value of -1 means no minimum value."""
    StartPosX:property
    """Read Property: Starting Position in X. This is the initial position when the tool is opened. Default = 450"""
    StartPosY:property
    """Read Property: Starting Position in Y. This is the initial position when the tool is opened. Default = 450"""
    StartSizeX:property
    """Read Property: Starting Size. This is the initial size in X when the tool is opened. Default = 800"""
    StartSizeY:property
    """Read Property: Starting Size. This is the initial size in Y when the tool is opened. Default = 400"""
    ToolName:property
    """Read Property: Tool Name"""
    def GetPossibleDockPosition(self)->FBToolPossibleDockPosition:
        """Get the possible docking position for the tool (concatenated).
        
        return : Get all the docking flags in one call. Flags can be concatenated."""
        ...
    def SetPossibleDockPosition(self,Flags:FBToolPossibleDockPosition):
        """Set the possible docking position for the tool.
        Be sure to call this function once the tool is visible, a good place to call it is when the OnShow event of the layout is called.
        
        Flags : Set the docking position flag values. Note: this function overwrites all flags with those passed in parameter."""
        ...
class FBPopup(FBLayout):
    """Popup window.
    This class lets a window (inheriting from FBLayout) be created for another interface. See sample: Popup.py."""
    Modal:bool
    """Read Write Property: Modal?"""
    def Close(self,Ok:bool=False):
        """Close popup.
        
        Ok : Equivalent of OK button clicked if true (default = false)."""
        ...
    def Show(self,Parent:FBVisualComponent=None)->bool:
        """Show popup.
        
        Parent : Parent object for popup
        return : Operation was successful (true or false)."""
        ...
class FBImageContainer(FBVisualComponent):
    """Image.
    See sample: ImageContainer.py."""
    Filename:str
    """Read Write Property: Filename for image."""
    OnDragAndDrop:FBEvent
    """Event: Drag and drop."""
class FBFCurveEditor(FBVisualComponent):
    """FCurve editor.
    See sample: FCurveEditor.py."""
    def AddAnimationNode(self,Node:FBAnimationNode):
        """Add an animation node to the editor.
        
        Node : Animation node to show in the editor."""
        ...
    def AddProperty(self,Property:FBPropertyAnimatable):
        """Add an animatable property to the editor.
        
        Property : Property to show in the editor."""
        ...
    def Clear(self):
        """Clear the editor."""
        ...
    def RemoveAnimationNode(self,Node:FBAnimationNode):
        """Remove an animation node from the editor.
        
        Node : Animation node to hide from editor."""
        ...
class FBEditVector(FBVisualComponent):
    """Vector edit widget."""
    OnChange:FBEvent
    """Event: Vector value changed."""
    Value:FBVector3d
    """Read Write Property: Current value of vector."""
class FBEditTimeCode(FBVisualComponent):
    OnChange:FBEvent
    """Event: Timecode changed."""
    Value:FBTime
    """Read Write Property: Current timecode value."""
class FBEditPropertyModern(FBVisualComponent):
    """Property editor widget.
    This is a more modern version of the widget FBEditProperty which is used in the property editor tool of the application.See class FBEditProperty for more details. See sample: PropertyDrop.py."""
    LargeInc:float
    """Read Write Property: Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)"""
    Precision:float
    """Read Write Property: Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals."""
    Property:property
    """Read Write Property: Property to edit. Set to NULL to disable."""
    SliderMax:float
    """Read Write Property: Should the property be editable using a slider, set the maximum value atainable with the slider."""
    SliderMin:float
    """Read Write Property: Should the property be editable using a slider, set the minimum value atainable with the slider."""
    SmallInc:float
    """Read Write Property: Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)"""
    def SetBackgroundColorIndex(self,Index):
        """Set the background color index.
        Use the system-defined color palette to set the backgound color. By default the color used is kFBColorIndexStdListBg1
        
        Index : FBColorIndex"""
        ...
class FBEditProperty(FBVisualComponent):
    """Property editor widget.
    This widget allows users to edit the values of a property without having to manually customize the GUI depending on the type of the property being edited.SDK objects can have three types of properties:An internal property which maps to an actual property that can be seen in the property editor tool of the application. This type of property is usually obtained from the PropertyList data member.SDK-only property which does not maps onto an existing property of the encapsulated object. The existence of these types of property is often to make the object interface simpler. All the FBPropertyList-types will fall into this category, except for FBPropertyListObjects.SDK property which maps onto an existing object property, but does so indirectly using function calls instead of direct property access. This is usually for historical reason. In this case the property will usually be present twice in the PropertyList: once as an SDK-Only property and another time as an internal property.Another limitation of this widget is that it can only display non hidden internal properties. To get around this issue, the property flag can be changed to unhide it. Doing so will also cause the property to be visible via the property tool.
    
    >>> # In a tool header file...
    FBEditProperty mEditProperty;
    # In a tool source file...
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
    
    
    See sample: PropertyDrop.py."""
    LargeInc:float
    """Read Write Property: Indicate the large increment applied when click-draging on the property value (usually left-click-dragging)"""
    Precision:float
    """Read Write Property: Used to specify the width and precision of the value shown. A value of 7.2 indicates to show at minimum 7 numbers, with 2 decimals."""
    Property:property
    """Read Write Property: Property to edit. Set to NULL to disable."""
    SliderMax:float
    """Read Write Property: Should the property be editable using a slider, set the maximum value atainable with the slider."""
    SliderMin:float
    """Read Write Property: Should the property be editable using a slider, set the minimum value atainable with the slider."""
    SmallInc:float
    """Read Write Property: Indicate the small increment applied when click-draging on the property value (usually right-click-dragging)"""
class FBEditNumber(FBVisualComponent):
    """Number edit box."""
    LargeStep:float
    """Read Write Property: Large step value."""
    Max:float
    """Read Write Property: Maximum value."""
    Min:float
    """Read Write Property: Minimum value."""
    OnChange:FBEvent
    """Event: Number changed."""
    Precision:float
    """Read Write Property: Precision of value."""
    SmallStep:float
    """Read Write Property: Small step value."""
    Value:float
    """Read Write Property: Current value."""
class FBEditColor(FBVisualComponent):
    """Color edit widget."""
    ColorMode:int
    """Read Write Property: 3 for RGB, 4 for RGBA (Default = 3)"""
    OnChange:FBEvent
    """Event: Color changed."""
    Value:FBColor
    """Read Write Property: Current value of color."""
class FBEdit(FBVisualComponent):
    """Text edit box."""
    OnChange:FBEvent
    """Event: Text changed."""
    PasswordMode:bool
    """Read Write Property: Set password mode for this edit box."""
    Text:str
    """Read Write Property: Text displayed."""
class FBButton(FBVisualComponent):
    """Used to create and manage buttons in a user interface.
    This class includes functionality to create buttons in a user interface and add a callback. In MotionBuilder, buttons are created within regions, which are in turn created in layouts with FBLayout. For usage, see the Python sample Button.py. See also: FBButtonStyle, FBTextJustify, FBButtonLook. See samples: Button.py, Popup.py, RadioButton.py."""
    Justify:FBTextJustify
    """Read Write Property: Current state of button."""
    Look:FBButtonLook
    """Read Write Property: Current state of button."""
    OnClick:FBEvent
    """Event: Button clicked."""
    State:int
    """Read Write Property: Current state of button."""
    Style:FBButtonStyle
    """Read Write Property: Button style."""
    def GetStateColor(self,State:FBButtonState)->FBColor:
        """Queries the color associated with a button state.
        This method is only useful for buttons of style kFB2States.
        
        State : The state to be queried.
        return : The color vector."""
        ...
    def SetImageFileNames(self,UpImage:str,DownImage:str=0,ThirdImage:str=0,FromResources:bool=False):
        """Sets the image used to generate a kFBBitmap2States.
        
        UpImage : The image used when button is unpushed
        DownImage : The image used when button is pushed
        ThirdImage : str
        FromResources : Add resource path to image path."""
        ...
    def SetStateColor(self,State:FBButtonState,Color:FBColor):
        """Returns whether or not the itemIndex is currently selected.
        
        State : The state to be set.
        Color : The desired color vector."""
        ...
class FBMemo(FBEdit):
    """Multi-line text input.
    See samples: Memo.py, TutorialBox.py, TutorialGrid.py."""
    def GetStrings(self,Lines:FBStringList):
        """Get the content of the memo.
        
        Lines : Content of the memo will be copied to it."""
        ...
    def SetStrings(self,Lines:FBStringList):
        """Set the content of the memo.
        
        Lines : Content of the memo from will be set to it."""
        ...
class FBBrowsingProperty(FBVisualComponent):
    """Property browsing.
    See sample: BrowsingProperty.py."""
    def AddObject(self,Object:FBPlug):
        """Add an object whose properties will be displayed.
        
        Object : Object whose properties will be displayed in the property brwoser."""
        ...
    def ObjectGet(self,Index:int)->FBPlug:
        """Return the object at the specified index.
        
        Index : Index of the object to get.
        return : Object at the index specified currently displayed in the property browser."""
        ...
    def ObjectGetCount(self)->int:
        """Get the number of object displayed in the property browser.
        
        return : Object currently displayed in the property browser."""
        ...
    def RemoveObject(self,Object:FBPlug):
        """Remove an object from the property browser.
        
        Object : Object to remove."""
        ...
class FBArrowButton(FBVisualComponent):
    """Creates a button which opens a layout to display content.
    When pushed a layout to display content (another control or a layout) is opened. A small arrow to the left of the button title, shows whether the content is shown (points down) or not (points to the title). See samples: ArrowButton.py, FBCamera.py."""
    def SetContent(self,Title:str,Content:FBVisualComponent,ContentWidth:int,ContentHeight:int):
        """Sets the content to be hidden/shown by button.
        The FBArrowButton must already have been added to a layout before calling this method.
        
        Title : Title of the content managed by the FBArrowButton
        Content : Content that the FBArrowButton displays or hides
        ContentWidth : Width of the content
        ContentHeight : Height of the content"""
        ...
class FBWebView(FBVisualComponent):
    """Web viewer.
    See sample: WebView.py."""
    def Load(self,URL:str):
        """Load the specified Url.
        
        URL : url to load in the WebView."""
        ...
class FBWidgetHolder(FBVisualComponent):
    """Native Widget Holder (can be used to embed native Qt Widget inside MoBu UI elements) A Widget holder provides a bridge to instantiate a Native Qt widget into MB framework.
    This will be used to allow user to create UI with QT designer and hook their created UI into MB. To allow a FBWidgetHolder to work properly, you need to specify a Creator function. This function will be called when needed to instantiate the native Widget.Or override WidgetCreate(QWidget*Parent) function in the subclass./bin/config/Scripts/UI/ToolNativeWidgetHolder.py for python usage example. See samples: MBFileRefDemo.py, ToolNativeWidgetHolder.py."""
    ...
def CloseTool(arg1:FBTool)->bool:...
def CloseToolByName(arg1:str)->bool:...
def FBActionManager_TypeInfo()->int:...
def FBActorFace_TypeInfo()->int:...
def FBActor_TypeInfo()->int:...
def FBAdd(Result:FBVector4d,V1:FBVector4d,V2:FBVector4d):
    """Add two vectors together (pResult =V1 +V2)
    
    Result : Resulting vector.
    V1 : 1st vector.
    V2 : 2nd vector."""
    ...
def FBAnimationLayer_TypeInfo()->int:...
def FBAnimationNode_TypeInfo()->int:...
def FBApplication_TypeInfo()->int:...
def FBArrowButton_TypeInfo()->int:...
def FBAssetFile_TypeInfo()->int:...
def FBAssetFolder_TypeInfo()->int:...
def FBAssetItem_TypeInfo()->int:...
def FBAssetMng_TypeInfo()->int:...
def FBAudioClip_TypeInfo()->int:...
def FBAudioFmt_AppendFormat(Format:object,SrcFormat:object,arg3:object,arg4:object)->int:
    """Append the rendering audio format with another audio format.
    
    Format : Audio format to use.
    SrcFormat : Audio format to be appended.
    return : An audio format object with the specified format."""
    ...
def FBAudioFmt_ConvertBitDepthMode(BitDepthMode:FBAudioBitDepthMode)->int:
    """Converts an FBAudioBitDepthMode enum value to its FBAudioFmt object equivalent.
    
    BitDepthMode : The bit depth mode enum value.
    return : The FBAudioFmt object equivalent to the input bit depth mode enum value."""
    ...
def FBAudioFmt_ConvertChannelMode(ChannelMode:FBAudioChannelMode)->int:
    """Converts an FBAudioChannelMode enum value to its FBAudioFmt object equivalent.
    
    ChannelMode : The channel mode enum value.
    return : The FBAudioFmt object equivalent to the input channel mode enum value."""
    ...
def FBAudioFmt_ConvertRateMode(RateMode:FBAudioRateMode)->int:
    """Converts an FBAudioRateMode enum value to its FBAudioFmt object equivalent.
    
    RateMode : The rate mode enum value.
    return : The FBAudioFmt object equivalent to the input rate mode enum value."""
    ...
def FBAudioFmt_GetBitsValue(Format:object)->int:
    """Get the bit depth value of the Audio format object.
    
    Format : Audio format to use.
    return : Bit depth value as an integer value."""
    ...
def FBAudioFmt_GetBytesValue(Format:object)->int:
    """Get the bytes value of the Audio format object.
    
    Format : Audio format to use.
    return : Bytes value as an integer value."""
    ...
def FBAudioFmt_GetChannelValue(Format:object)->int:
    """Get the channel value of the Audio format object.
    
    Format : Audio format to use.
    return : Channel value as an integer value."""
    ...
def FBAudioFmt_GetDefaultFormat()->int:
    """Get default audio format.
    
    return : An audio format object."""
    ...
def FBAudioFmt_GetRateValue(Format:object)->int:
    """Get the rate value of the Audio format object.
    
    Format : Audio format to use.
    return : Audio rate value as an integer value."""
    ...
def FBAudioFmt_RemoveFormat(Format:object,SrcFormat:object,arg3:object,arg4:object)->int:
    """Remove audio format from another audio format object.
    
    Format : Audio format to use.
    SrcFormat : Audio format to remove.
    return : An audio format object without the specified format settings passed in parameter."""
    ...
def FBAudioFmt_TestFormat(SrcFormat:object,Channels:object,Bits:object,Rate:object)->bool:
    """Test if the given audio format object contains the channel, bit depth, and rate.
    
    SrcFormat : Audio format to test.
    Channels : Number of channels to test.
    Bits : Bit depth to test.
    Rate : Audio rate to test.
    return : True if the given audio format object contains the channel, bit depth, and rate."""
    ...
def FBAudioIn_TypeInfo()->int:...
def FBAudioOut_TypeInfo()->int:...
def FBBeginChangeAllModels():
    """Call begin change to all models (need to be closed).
    Useful for selection of many models that can trigger many related callbacks)"""
    ...
def FBBoxPlaceHolder_TypeInfo()->int:...
def FBBox_TypeInfo()->int:...
def FBBrowsingProperty_TypeInfo()->int:...
def FBButton_TypeInfo()->int:...
def FBCameraStereo_TypeInfo()->int:...
def FBCameraSwitcherAudioManager_TypeInfo()->int:...
def FBCameraSwitcher_TypeInfo()->int:...
def FBCamera_TypeInfo()->int:...
def FBCharacterExtension_TypeInfo()->int:...
def FBCharacterFace_TypeInfo()->int:...
def FBCharacterMarkerSet_TypeInfo()->int:...
def FBCharacterPose_TypeInfo()->int:...
def FBCharacterSolver_TypeInfo()->int:...
def FBCharacter_TypeInfo()->int:...
def FBClamp(V:object,L:object,H:object)->float:
    """Clamp value.
    
    V : Value to clamp.
    L : Low limit.
    H : High limit.
    return : Clamped value."""
    ...
def FBCluster_TypeInfo()->int:...
def FBComponent_TypeInfo()->int:...
def FBConnect(Src:FBPlug,Dst:FBPlug,ConnectionType:FBConnectionType)->bool:
    """Request the connection two FBPlug objects.
    
    Src : Source plug.
    Dst : Destination plug.
    ConnectionType : Type of connection, taken from FBConnectionType.
    return : A boolean indicating success (True) or failure (False)."""
    ...
def FBConstraintManager_TypeInfo()->int:...
def FBConstraintRelation_TypeInfo()->int:...
def FBConstraintSolver_TypeInfo()->int:...
def FBConstraint_TypeInfo()->int:...
def FBConstructionHistory_TypeInfo()->int:...
def FBControlSet_TypeInfo()->int:...
def FBCreateObject(GroupName:str,EntryName:str,Name:str,p3:object)->object:
    """FBCreateObject.
    
    GroupName : Set the name of the Group.
    EntryName : Set the name of the Entry.
    Name : Set the name of the Object to create.
    p3 : Data to pass to object creator function.
    nth : Set the occurrence of the object to remove."""
    ...
def FBCycleAnalysisNode_TypeInfo()->int:...
def FBCycleCreator_TypeInfo()->int:...
def FBDeck_TypeInfo()->int:...
def FBDeformerPointCache_TypeInfo()->int:...
def FBDeformer_TypeInfo()->int:...
def FBDeleteCharacterPinningPreset(PresetName:str)->bool:
    """Deletes a pinning preset from the Character Controls Tool.
    
    PresetName : The preset name to delete (not the file path nor the filename of the preset).
    return : True if the operation is successful, false otherwise."""
    ...
def FBDeleteObjectsByName(NamePattern:str,NameSpace:str,GroupName:str)->int:
    """FBDeleteObjectsByName.
    This function will query the system for objects fulfilling a particular name pattern and delete them. specify a namespace preferred, delete all objects with the group name without specified a namespace specified may lead to inconsistent in scene. Wrap multiple calls to FBDeleteObjectsByName() inside pair of FBPreventUIUpdateBegin() / FBPreventUIUpdateEnd() could improve application's performance.
    
    NamePattern : if not NULL, indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene ). if is NULL or Empty string, * will be used for match all.
    NameSpace : if not NULL, the objects must be inside the given namespace.
    GroupName : if not NULL, indicate the object group name (type).
    return : the count of objects found and deleted."""
    ...
def FBDeviceInstrument_TypeInfo()->int:...
def FBDeviceOpticalMarker_TypeInfo()->int:...
def FBDeviceOptical_TypeInfo()->int:...
def FBDevice_TypeInfo()->int:...
def FBDisconnect(Src:FBPlug,Dst:FBPlug)->bool:
    """Connect two FBPlug objects.
    
    Src : Source plug.
    Dst : Destination plug.
    return : A boolean indicating success (True) or failure (False)."""
    ...
def FBDot(V1:FBVector4d,V2:FBVector4d)->float:
    """Calculate the dot product of two vectors.
    
    V1 : 1st vector.
    V2 : 2nd vector.
    return : Dot product."""
    ...
def FBEditColor_TypeInfo()->int:...
def FBEditNumber_TypeInfo()->int:...
def FBEditPropertyModern_TypeInfo()->int:...
def FBEditProperty_TypeInfo()->int:...
def FBEditTimeCode_TypeInfo()->int:...
def FBEditVector_TypeInfo()->int:...
def FBEdit_TypeInfo()->int:...
def FBEndChangeAllModels():
    """Call end change to all models (should be first open)."""
    ...
def FBEvaluateManager_TypeInfo()->int:...
def FBFCurveEditorUtility_TypeInfo()->int:...
def FBFCurveEditor_TypeInfo()->int:...
def FBFCurveEventManager_TypeInfo()->int:...
def FBFCurve_TypeInfo()->int:...
def FBFbxOptions_TypeInfo()->int:...
def FBFileMonitoringManager_TypeInfo()->int:...
def FBFileReference_TypeInfo()->int:...
def FBFilter_TypeInfo()->int:...
def FBFindModelByLabelName(ModelLabelName:str)->object:
    """Find a model in the scene by its label name.
    Searches the scene for a model, based on the model's label name. Label name is 'NameSpaceName:ObjectName'. also known as 'PrefixName::ObjectName' Full name is 'GroupName::NameSpaceName:ObjectName'.
    
    ModelLabelName : LabelName of model to search for. Specify it with schema like "NameSpaceName:ObjectName",or "ObjectName" if no NameSpaceName.
    return : A handle onto the model with Label name matching, returns NULL if no model was found by the search."""
    ...
def FBFindModelByUniqueColorId(Color:FBColor)->tuple:
    """Find a model in the scene by its unique color id.
    A model could have a single unique ColorID, but SDK plugin user could request additional ColorID per model to support multi sub items picking. see FBModel::SetAdditionalUniqueColorIDCount().
    
    Color : Color channel values are in range of [0,1] with precision 1.0/255
    SubItemIndex : Pass out SubImtem index value if not null. In pyfbsdk no such parameter.
    return : A handle onto the model with unique color id matching, returns NULL if no model was found by the search. In pyfbsdk return tuple [model, subItemIndex]"""
    ...
def FBFindObjectByFullName(ObjectFullName:str)->object:
    """FBFindObjectByFullName.
    This function will query the system for an object with its FullName matching. Full name is 'GroupName::NameSpaceName:ObjectName'. Label name is 'NameSpaceName:ObjectName'. also known as 'PrefixName::ObjectName'
    
    ObjectFullName : Full Name of object to search for. Specify it with schema like "GroupName::NameSpaceName:ObjectName",or "GroupName::ObjectName" if no NameSpaceName.
    return : A handle onto the object with Full name matchingObjectFullName, returns NULL if no object was found by the search."""
    ...
def FBFindObjectsByName(NamePattern:str,List:FBComponentList,IncludeNamespace:object,ModelsOnly:object):
    """FBFindObjectsByName.
    This function will query the system for objects fulfilling a particular name pattern
    
    NamePattern : Indicate the name pattern to search. This pattern can contain any amount of *. (ex: *tr*mod*scene )
    List : List that contains the objects
    IncludeNamespace : Does the search use the complete name (with namespace)
    ModelsOnly : Is the search on models or all types of objects"""
    ...
def FBFolder_TypeInfo()->int:...
def FBGenericMenuItem_TypeInfo()->int:...
def FBGenericMenu_TypeInfo()->int:...
def FBGeometry_TypeInfo()->int:...
def FBGetActorMarkerSetVisibility()->bool:
    """Queries visibility of the marker set of the current actor.
    
    return : True if the marker set of the current actor are visible, or false if it is hidden."""
    ...
def FBGetCharacterExternalSolverCount()->int:
    """Get character external solver count.
    
    return : Number of external character solver available."""
    ...
def FBGetCharacterExternalSolverIndex(Name:str)->int:
    """Get character external solver index.
    
    Name : Name of external solver.
    return : Index of external solver specified at the provided name."""
    ...
def FBGetCharacterExternalSolverName(Index:object)->str:
    """Get character external solver name.
    
    Index : Index of external solver.
    return : Name of the external solver specified at the provided index."""
    ...
def FBGetCharacterFingerTipsVisibility()->bool:
    """Queries visibility of the finger-tips of the current character.
    
    return : True if finger-tips of the current character are visible, or false if they are hidden."""
    ...
def FBGetCharacterFloorContactsVisibility()->bool:
    """Queries visibility of the floor contacts of the current character.
    
    return : True if floor contacts of the current character are visible, or false if they are hidden."""
    ...
def FBGetCharactersKeyingMode()->FBCharacterKeyingMode:
    """return Character Manipulation/Keying Mode
    
    return : Keying Mode"""
    ...
def FBGetConstantKeyReducerThresholdValue(ThresholdType:FBConstantKeyReducerThresholdType)->float:
    """Return a specific threshold value used by the Constant Key Reducer filter.
    
    ThresholdType : The threshold type to retrieve its value.
    return : The threshold value."""
    ...
def FBGetContinuousRotation(ROut:FBVector3d,R0:FBVector3d,R1:FBVector3d):
    """Get a continuous rotation in Euler space.
    This routine will help to avoid gimble locks due to interpolation.
    
    ROut : Successful continuous rotation (gimble-lock free).
    R0 : Suggested next rotation.
    R1 : Previous rotation."""
    ...
def FBGetDisplayInfo()->FBEvaluateInfo:
    """Get the displays evaluation information structure.
    This function can be used in order to call real-time functions based on the current display evalution state.
    
    return : The display evalution structure."""
    ...
def FBGetEffectorBodyPart(EffectorId:FBEffectorId)->FBBodyPartId:
    """return BodyPart ID from Effector.
    
    EffectorId : Effector ID.
    return : ID of the BodyPart the effector is in."""
    ...
def FBGetEvaluationTaskCycle()->FBProfileTaskCycle:
    """Get evaluation task cycle."""
    ...
def FBGetGlobalMatrix(Matrix:FBMatrix,MatrixParent:FBMatrix,LocalMatrix:FBMatrix):
    """Get global matrix from parent and child matrices.
    From an input referential, this function will calculate the global matrix corresponding to the input local matrix (which is with respect to the parent matrix).
    
    Matrix : Calculated local matrix.
    MatrixParent : Parent matrix.
    LocalMatrix : Local matrix."""
    ...
def FBGetLastSelectedModel()->object:
    """Get the last selected model, which is the one having the manipulator in the viewer.
    
    return : The last selected model or nullptr (C++) or None (Python) if no model is selected."""
    ...
def FBGetLocalMatrix(Matrix:FBMatrix,MatrixParent:FBMatrix,MatrixChild:FBMatrix):
    """Get local matrix from parent and child matrices.
    Will calculate the local matrix from two global matrices. The resulting matrix will be a local matrix containing the local transformations to go from the parent referentialto the child referential.
    
    Matrix : Calculated local matrix.
    MatrixParent : Parent matrix (new base referential).
    MatrixChild : Child matrix."""
    ...
def FBGetMainThreadTaskCycle()->FBProfileTaskCycle:
    """Get root task cycle."""
    ...
def FBGetMainWindow()->int:
    """Return the MotionBuilder main window.
    The following Python snippet shows how to get the MotionBuilder main window.
    
    >>> from PySide2 import QtWidgets
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
    
    
    return : The MotionBuilder main window."""
    ...
def FBGetMultiLangText(Context:FBPlug,Key:str,FlagReturnKey:object)->str:
    """Name lookup in a user defined context context.
    This version of the function is a little less useful as the context string, if not empty, will usually refer to internal class names of objects which is not easily available to the outside world.As a general rule, an SDK object whose class is 'FBObject' will be wrapping an internal object of class 'KObject'. For example an 'FBCamera' is a wrapper around a 'KCamera' object. Similarily an 'FBConstraint' wll wrap a 'KConstraint'. This pattern is not universal and may differ at times, so it will not always be applicable. There are also cases where an 'FB' objects has no corresponding 'K' object, such as in the case of an 'FBSystem' object.On lookup there are potentially two searches made: a first one, using the context if one was provided. Should the first search fail, a second search will be done without using the context.Again the lookup result is dependant on the current language selected, as indicated by the class FBMultiLangManager.The following sample code shows 2 cases that do not use context, and 2 cases that are using a context which are internal class names.Python sample code:
    
    >>> from pyfbsdk import *
    print FBGetMultiLangText( '', 'CharacterExtension' )            # Will return 'Character Extension'.
    print FBGetMultiLangText( '', 'TranslationMax' )                # Will return 'Max Freedom'.
    print FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ) # Will return 'Parent/Child'.
    print FBGetMultiLangText( 'KCamera', 'FieldOfView' )            # Will return 'Field Of View'.
    
    
    C++ sample code:
    
    >>> # Will return 'Character Extension'.
    FBTrace( '%s
    ', FBGetMultiLangText( '', 'CharacterExtension' ));
    # Will return 'Max Freedom'.
    FBTrace( '%s
    ', FBGetMultiLangText( '', 'TranslationMax' ));
    # Will return 'Parent/Child'.
    FBTrace( '%s
    ', FBGetMultiLangText( 'KConstraintUIName', 'Parent-Child' ));
    # Will return 'Field Of View'.
    FBTrace( '%s
    ', FBGetMultiLangText( 'KCamera', 'FieldOfView' ));
    
    
    Context : String which dictates the context of the lookup.
    Key : String to look up.
    FlagReturnKey : Should the lookup fail, will return the key instead of an empty string.
    return : The corresponding string if the lookup was succesfull. If not will return an empty string ifFlagReturnKey was false. Otherwise will return the key string."""
    ...
def FBGetRenderingTaskCycle()->FBProfileTaskCycle:
    """Get rendering task cycle."""
    ...
def FBGetSelectedModels(List:FBModelList,Parent:FBModel,Selected:object,SortBySelectOrder:object):
    """Find all models that are selected (ifSelected is true) Searches recursively from a root model for models that are selected, and adds them to a list of models.
    
    List : List to add found models to.
    Parent : Root model to look from (default=NULL(root)).
    Selected : true to find selected models, false to find unselected models(default=true).
    SortBySelectOrder : true to sort the result by selection order, first selected model in the first part of the list; false to sort the result by scene graph order"""
    ...
def FBGlobalLight_TypeInfo()->int:...
def FBGroup_TypeInfo()->int:...
def FBHUDBloopSlateElement_TypeInfo()->int:...
def FBHUDElement_TypeInfo()->int:...
def FBHUDFlashElement_TypeInfo()->int:...
def FBHUDManager_TypeInfo()->int:...
def FBHUDRectElement_TypeInfo()->int:...
def FBHUDTextElement_TypeInfo()->int:...
def FBHUDTextureElement_TypeInfo()->int:...
def FBHUDTimelineElement_TypeInfo()->int:...
def FBHUD_TypeInfo()->int:...
def FBHandle_TypeInfo()->int:...
def FBImageContainer_TypeInfo()->int:...
def FBImage_TypeInfo()->int:...
def FBInterpolateRotation(QOut:FBVector3d,Q0:FBVector3d,Q1:FBVector3d,U:object):
    """Interpolate a rotation in Quaternion.
    
    QOut : Resulting, interpolated rotation.
    Q0 : 1st rotation.
    Q1 : 2nd rotation.
    U : Interpolation ratio."""
    ...
def FBKeyControl_TypeInfo()->int:...
def FBKeyingGroup_TypeInfo()->int:...
def FBLabel_TypeInfo()->int:...
def FBLayeredTexture_TypeInfo()->int:...
def FBLayoutRegion_TypeInfo()->int:...
def FBLayout_TypeInfo()->int:...
def FBLength(V:FBVector4d)->float:
    """Get the length of a vertex (from origin)
    
    V : Vertex for which length is to be measured.
    return : Length of vertex (from origin)."""
    ...
def FBLight_TypeInfo()->int:...
def FBList_TypeInfo()->int:...
def FBLoadCharacterPinningPreset(PresetName:str)->bool:
    """Loads a pinning preset in the Character Controls Tool.
    
    PresetName : The preset name to load (not the file path nor the filename of the preset).
    return : True if the operation is successful, false otherwise."""
    ...
def FBLoadFbxPrimitivesModel(ModelName:str)->object:
    """Load a model.
    
    ModelName : Name of primitive model to load.
    return : A handle onto the model that was loaded, returns NULL if no model was found."""
    ...
def FBLogger_TypeInfo()->int:...
def FBManipulator_TypeInfo()->int:...
def FBMarkerSet_TypeInfo()->int:...
def FBMaterial_TypeInfo()->int:...
def FBMatrixInverse(Matrix:FBMatrix,Src:FBMatrix):
    """Invert a matrix.
    
    Matrix : Calculated inverse matrix.
    Src : Source matrix to invert."""
    ...
def FBMatrixMult(Matrix:FBMatrix,A:FBMatrix,B:FBMatrix):
    """Multiply two matrices.
    
    Matrix : Calculated resulting matrix.
    A : 1st matrix.
    B : 2nd matrix."""
    ...
def FBMatrixOrthogonalize(Matrix:FBMatrix):
    """Make sure that rotation vectors are orthogonal and normalized (fast way for removing scaling from matrix)
    
    Matrix : Rotation Matrix to Orthogonalize."""
    ...
def FBMatrixToQuaternion(Quaternion:FBVector4d,Matrix:FBMatrix):
    """Get a quaternion from a matrix (potential ).
    
    Quaternion : Calculated quaternion.
    Matrix : Input matrix."""
    ...
def FBMatrixToRotation(Vector:FBVector3d,Matrix:FBMatrix,RotationOrder:FBRotationOrder):
    """Obtain rotation vector from a matrix.
    
    Vector : Extracted rotation vector, ordered the same way as the rotation order specified byRotationOrder.
    Matrix : Input matrix.
    RotationOrder : Rotation order."""
    ...
def FBMatrixToRotationWithPrecision(Vector:FBVector3d,Matrix:FBMatrix,RotationOrder:FBRotationOrder,Precision:object):
    """Obtain rotation vector from a matrix.
    
    Vector : Extracted rotation vector.
    Matrix : Input matrix.
    RotationOrder : Rotation Order.
    Precision : Indicate the precision level (pow(10.0, -pPrecision)) used when calculating the threshold value for gimble lock."""
    ...
def FBMatrixToScaling(Vector:FBSVector,Matrix:FBMatrix):
    """Obtain scaling vector from a matrix.
    
    Vector : Extracted scaling vector.
    Matrix : Input matrix."""
    ...
def FBMatrixToTQS(TVector:FBVector4d,Quaternion:FBVector4d,SVector:FBSVector,Matrix:FBMatrix):
    """Obtain translation vector, rotation quaternion, and scaling vector from a matrix.
    
    TVector : Extracted translation vector.
    Quaternion : Extracted rotation quaternion.
    SVector : Extracted scaling vector.
    Matrix : Input matrix."""
    ...
def FBMatrixToTRS(TVector:FBVector4d,RVector:FBVector3d,SVector:FBSVector,Matrix:FBMatrix):
    """Obtain translation, rotation, and scaling vectors from a matrix.
    
    TVector : Extracted translation vector.
    RVector : Extracted rotation vector.
    SVector : Extracted scaling vector.
    Matrix : Input matrix."""
    ...
def FBMatrixToTranslation(Vector:FBVector4d,Matrix:FBMatrix):
    """Obtain translation vector from a matrix.
    
    Vector : Extracted translation vector.
    Matrix : Input matrix."""
    ...
def FBMatrixTranspose(Matrix:FBMatrix,Src:FBMatrix):
    """Transpose a matrix.
    
    Matrix : Calculated transpose matrix.
    Src : Source matrix to transpose."""
    ...
def FBMemo_TypeInfo()->int:...
def FBMenuManager_TypeInfo()->int:...
def FBMergeTransactionBegin():
    """Call to begin the transaction for merging multiple files.
    Useful to consecutively merge multiple files into scene."""
    ...
def FBMergeTransactionEnd():
    """Call to end the merge transaction."""
    ...
def FBMergeTransactionFileRefEditBegin():
    """Call to begin the transaction for merging multiple files and applying File Reference edit at the same time.
    Useful to consecutively merge multiple files into scene with FileRef edit operation in between."""
    ...
def FBMergeTransactionFileRefEditEnd():
    """Call to end merge transaction with File Reference edit."""
    ...
def FBMergeTransactionFileRefEditIsOn()->bool:
    """Call to tell if system is during File Reference Edit Merge transaction."""
    ...
def FBMergeTransactionIsOn()->bool:
    """Call to tell if system is during Merge transaction."""
    ...
def FBMesh_TypeInfo()->int:...
def FBMessageBox(BoxTitle:str,Message:str,Button1Str:str,Button2Str:str,Button3Str:str,DefaultButton:object,ScrolledMessage:object)->int:
    """Dialog popup box.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button.
    
    BoxTitle : Title of message box.
    Message : Message to place in box.
    Button1Str : String for first button (Cannot be NULL).
    Button2Str : String for second button (NULL will not create a button).
    Button3Str : String for third button (NULL will not create a button).
    DefaultButton : Indicates the default (pre-selected) button (default is 0).
    ScrolledMessage : Scroll message (default is 0).
    return : The number of the button selected."""
    ...
def FBMessageBoxGetUserValue(BoxTitle:str,Message:str,Value:object,ValueType:FBPopupInputType,Button1Str:str,Button2Str:str,Button3Str:str,DefaultButton:object,arg9:object)->tuple:
    """Dialog popup box to get user input.
    Opens a message box, with up to three buttons, asking the user to enter data. The type of data to be entered is specified by theValue andValueType parameters.
    
    BoxTitle : Title of message box.
    Message : Message to place in box.
    Value : Value entered by user (must correspond withValueType).
    ValueType : Type of pointer specified inValue.
    Button1Str : String for first button (Cannot be None).
    Button2Str : String for second button (None will not create a button).
    Button3Str : String for third button (None will not create a button).
    DefaultButton : Indicates the default (pre-selected) button(default=0).
    return : A tuple containing the index of the button selected and the value entered by the user, if any."""
    ...
def FBMessageBoxWithCheck(BoxTitle:str,Message:str,Button1Str:str,Button2Str:str,Button3Str:str,CheckBoxStr:str,CheckBoxValue:object,DefaultButton:object,ScrolledMessage:object)->tuple:
    """Dialog popup box with 'don't show again' option.
    Opens a message box containing a message and up to three buttons. Waits for the user to click a button. This dialog also gives the user the option of never showing the dialog again.
    
    BoxTitle : Title of message box.
    Message : Message to place in box.
    Button1Str : String for first button (Cannot be None).
    Button2Str : String for second button (None will not create a button).
    Button3Str : String for third button (None will not create a button).
    CheckBoxStr : Check box string (Cannot be None).
    CheckBoxValue : Check box value.
    DefaultButton : Indicates the default (pre-selected) button (default is 0).
    ScrolledMessage : Scroll message (default is False).
    return : A tuple containing the index of the button selected and the boolean value of the check box."""
    ...
def FBModelCube_TypeInfo()->int:...
def FBModelMarkerOptical_TypeInfo()->int:...
def FBModelMarker_TypeInfo()->int:...
def FBModelNull_TypeInfo()->int:...
def FBModelOpticalAdvanced_TypeInfo()->int:...
def FBModelOptical_TypeInfo()->int:...
def FBModelPath3D_TypeInfo()->int:...
def FBModelPlaceHolder_TypeInfo()->int:...
def FBModelPlane_TypeInfo()->int:...
def FBModelRoot_TypeInfo()->int:...
def FBModelSkeleton_TypeInfo()->int:...
def FBModelTemplate_TypeInfo()->int:...
def FBModelTransactionBegin():
    """FBModelTransactionBegin.
    This set of functions speeds up the process of batch operations on models."""
    ...
def FBModelTransactionEnd():
    """FBModelTransactionEnd.
    This set of functions speeds up the process of batch operations on models."""
    ...
def FBModelVertexData_TypeInfo()->int:...
def FBModel_TypeInfo()->int:...
def FBMotionClip_TypeInfo()->int:...
def FBMotionFileOptions_TypeInfo()->int:...
def FBMult(Result:FBVector4d,M:FBVector4d,V:object):
    """Calculate the cross product of a Matrix and Scale Vector.
    
    Result : Resulting Matrix.
    M : Matrix.
    V : vector."""
    ...
def FBNamespace_TypeInfo()->int:...
def FBNote_TypeInfo()->int:...
def FBNurbs_TypeInfo()->int:...
def FBObjectGetGlobalUniqueId()->int:
    """Get the global static object unique ID counter.
    Each new created object will be assigned this global unique ID. Object.UniqueID = GlobalUniqueID++"""
    ...
def FBObjectGetLivingCount()->int:
    """Get current total living object count."""
    ...
def FBObjectLifeLogEnable(Enable:object):
    """Enable object creation / deletion logging.
    Default logging if off This logging may hurt performance slightly. use it only for debug purpose.
    
    Enable : true to enable logging."""
    ...
def FBObjectPose_TypeInfo()->int:...
def FBObjectPrintLivings(StartUniqueId:int):
    """Print those living objects created when logging is enabled.
    
    StartUniqueId : Any living object has been logged and with its uniqueId no less thanStartUniqueId will be printed out."""
    ...
def FBObject_GetEntryCount(GroupIndex:object)->int:
    """GroupIndex : int"""
    ...
def FBObject_GetEntryDLLName(GroupIndex:object,Index:object,nth:object)->str:
    """GroupIndex : int
    Index : int
    nth : int"""
    ...
def FBObject_GetEntryDescription(GroupIndex:object,Index:object,nth:object)->str:
    """GroupIndex : int
    Index : int
    nth : int"""
    ...
def FBObject_GetEntryName(GroupIndex:object,Index:object)->str:
    """GroupIndex : int
    Index : int"""
    ...
def FBObject_GetGroupCount()->int:
    """A set of functions to query the registration table."""
    ...
def FBObject_GetGroupName(GroupIndex:object)->str:
    """GroupIndex : int"""
    ...
def FBObject_GetIconName(GroupIndex:object,Index:object,nth:object)->str:
    """GroupIndex : int
    Index : int
    nth : int"""
    ...
def FBObject_GetMultiplicity(GroupIndex:object,Index:object,nth:object)->bool:
    """GroupIndex : int
    Index : int
    nth : int"""
    ...
def FBOpticalGap_TypeInfo()->int:...
def FBOpticalSegment_TypeInfo()->int:...
def FBPatch_TypeInfo()->int:...
def FBPhysicalProperties_TypeInfo()->int:...
def FBPlayerControl_TypeInfo()->int:...
def FBPlotPopup_TypeInfo()->int:...
def FBPlug_TypeInfo()->int:...
def FBPointCacheFile_TypeInfo()->int:...
def FBPointCacheManager_TypeInfo()->int:...
def FBPopNormalTool(ToolName:str,SetFocus:object)->bool:
    """This function is used to bring up a specific tool in the GUI.
    
    ToolName : The name of the tool as shown in the Open Reality menu.
    SetFocus : Indicate if the tool will have the focus.
    return : If the tool was brought up successfully."""
    ...
def FBPopup_TypeInfo()->int:...
def FBPose_TypeInfo()->int:...
def FBPreventUIUpdateBegin():
    """Call to prevent UI updates when creating/deleting/renaming objects.
    Useful to speed up script operations. Previously, FBMergeTransactionBegin()/ FBMergeTransactionEnd() could be used to do this kind of optimization, even if no merge operations were done. However, using FBMergeTransactionBegin()/ FBMergeTransactionEnd() with non-merge operation could lead to issues, like objects with invalid namespaces. FBPreventUIUpdateBegin()/FBPreventUIUpdateEnd() fix this issue, while giving the same speed increase."""
    ...
def FBPreventUIUpdateEnd():
    """Call to end blocking the UI updates."""
    ...
def FBPreventUIUpdateIsOn():
    """Call to tell if UI updates are blocked."""
    ...
def FBProfiler_TypeInfo()->int:...
def FBProgress_TypeInfo()->int:...
def FBPropertyConnectionEditor_TypeInfo()->int:...
def FBPropertyViewManager_TypeInfo()->int:...
def FBProperty_TypeInfo()->int:...
def FBQAdd(Result:FBVector4d,Q1:FBVector4d,Q2:FBVector4d):
    """Add two quaternions together (pResult =Q1 +Q2)
    
    Result : Resulting quaternion.
    Q1 : 1st quaternion.
    Q2 : 2nd quaternion."""
    ...
def FBQDot(Q1:FBVector4d,Q2:FBVector4d)->float:
    """Calculate the dot product of two quaternions.
    
    Q1 : 1st quaternion.
    Q2 : 2nd quaternion.
    return : Dot product."""
    ...
def FBQLength(Q:FBVector4d)->float:
    """Get the length of a quaternion.
    
    Q : Quaternion to calculate length for.
    return : Length of quaternionQ."""
    ...
def FBQMult(Result:FBVector4d,Q1:FBVector4d,Q2:object):
    """Calculate the cross product of two quaternions.
    
    Result : Resulting quaternion.
    Q1 : 1st quaternion.
    Q2 : 2nd quaternion."""
    ...
def FBQSub(Result:FBVector4d,Q1:FBVector4d,Q2:FBVector4d):
    """SubtractQ2 fromQ1 (pResult =Q1 -Q2)
    
    Result : Resulting quaternion.
    Q1 : 1st quaternion.
    Q2 : 2nd quaternion."""
    ...
def FBQuaternionToMatrix(Matrix:FBMatrix,Quaternion:FBVector4d):
    """Get a rotation matrix from a quaternion vector.
    
    Matrix : Calculated rotation matrix.
    Quaternion : Input quaternion."""
    ...
def FBQuaternionToRotation(Vector:FBVector3d,Quaternion:FBVector4d,RotationOrder:FBRotationOrder):
    """Get a rotation vector from a quaternion vector.
    
    Vector : Calculated rotation vector, ordered the same way as the rotation order specified byRotationOrder.
    Quaternion : Input quaternion.
    RotationOrder : Rotation order."""
    ...
def FBQuaternionToRotationWithPrecision(Vector:FBVector3d,Quaternion:FBVector4d,RotationOrder:FBRotationOrder,Precision:object):
    """Get a rotation vector from a quaternion vector.
    
    Vector : Calculated rotation vector.
    Quaternion : Input quaternion.
    RotationOrder : Rotation order of the rotation vector.
    Precision : Indicate the precision level (pow(10.0, -pPrecision)) used when calculating the threshold value for gimble lock."""
    ...
def FBReferenceTime_TypeInfo()->int:...
def FBRendererCallback_TypeInfo()->int:...
def FBRenderer_TypeInfo()->int:...
def FBRigidBody_TypeInfo()->int:...
def FBRotationToMatrix(Matrix:FBMatrix,Vector:FBVector3d,RotationOrder:FBRotationOrder):
    """Convert a rotation vector to a matrix.
    
    Matrix : Calculated resulting matrix.
    Vector : Rotation vector, ordered the same way as the rotation order specified byRotationOrder.
    RotationOrder : Rotation order."""
    ...
def FBRotationToQuaternion(Quaternion:FBVector4d,Vector:FBVector3d,RotationOrder:FBRotationOrder):
    """Get a quaternion from a rotation vector.
    
    Quaternion : Calculated quaternion.
    Vector : Input rotation vector, ordered the same way as the rotation order specified byRotationOrder.
    RotationOrder : Rotation order."""
    ...
def FBSaveCharacterPinningPreset(PresetName:str,AllowOverwriting:object)->bool:
    """Saves a pinning preset from the current pinning values in the Character Controls Tool.
    
    PresetName : The preset name to save (not the file path nor the filename of the preset).
    AllowOverwriting : True to allow overwriting an existing preset having the same name as the one provided, false otherwise.
    return : True if the operation is successful, false otherwise."""
    ...
def FBScalingToMatrix(Matrix:FBMatrix,Vector:FBSVector):
    """Convert a scaling vector to a matrix.
    
    Matrix : Calculated resulting matrix.
    Vector : Scaling vector."""
    ...
def FBScene_TypeInfo()->int:...
def FBSchedulingDependencyOutput(Enable:object):
    """Debug function for MT dependency debug.
    When enabled log file will be created and updated each time MultiThreaded scheduling is happening (scene rebuild)
    
    Enable : ON/OFF switch. This is not stored in config (should be changed only for debug purpose, because slow down rebuild process )"""
    ...
def FBScrollBox_TypeInfo()->int:...
def FBSetActorMarkerSetVisibility(Show:object)->bool:
    """Sets visibility of the marker set of the current actor.
    
    Show : Specifies if the market of the current actor should be visible.
    return : True if the operation is successful, false otherwise."""
    ...
def FBSetCharacterFingerTipsVisibility(Show:object):
    """Sets visibility of the finger-tips of the current character.
    
    Show : Specifies if finger-tips of the current character should be visible."""
    ...
def FBSetCharacterFloorContactsVisibility(Show:object):
    """Sets visibility of the floor contacts of the current character.
    
    Show : Specifies if floor contacts of the current character should be visible."""
    ...
def FBSetConstantKeyReducerThresholdValue(ThresholdType:FBConstantKeyReducerThresholdType,Value:object):
    """Set a specific threshold value used by the Constant Key Reducer filter.
    
    ThresholdType : The threshold type to set its value.
    Value : The new threshold value to set."""
    ...
def FBSetLastSelectedModel(Model:FBModel):
    """Set the given model as the last one selected, so the manipulator in the viewer will then be on that particular model.
    If the model is not selected, it will also be selected.
    
    Model : Model that will be flagged as the last selected model."""
    ...
def FBSet_TypeInfo()->int:...
def FBShaderLighted_TypeInfo()->int:...
def FBShaderShadowLive_TypeInfo()->int:...
def FBShader_TypeInfo()->int:...
def FBSleep(MilliSeconds:int):
    """Sleep function Puts system to sleep for specified time.
    
    MilliSeconds : Time to sleep for."""
    ...
def FBSlider_TypeInfo()->int:...
def FBSpreadCell_TypeInfo()->int:...
def FBSpreadColumn_TypeInfo()->int:...
def FBSpreadPart_TypeInfo()->int:...
def FBSpreadRow_TypeInfo()->int:...
def FBSpread_TypeInfo()->int:...
def FBStoryClip_TypeInfo()->int:...
def FBStoryFolder_TypeInfo()->int:...
def FBStoryGroupClip_TypeInfo()->int:...
def FBStoryTrack_TypeInfo()->int:...
def FBStory_TypeInfo()->int:...
def FBSub(Result:FBVector4d,V1:FBVector4d,V2:FBVector4d):
    """SubtractV2 fromV1 (pResult =V1 -V2)
    
    Result : Resulting vector.
    V1 : 1st vector.
    V2 : 2nd vector."""
    ...
def FBSurface_TypeInfo()->int:...
def FBSystem_TypeInfo()->int:...
def FBTQSToMatrix(Matrix:FBMatrix,TVector:FBVector4d,Quaternion:FBVector4d,SVector:FBSVector):
    """Convert translation vector, rotation quaternion, and scaling vector to a matrix.
    
    Matrix : Calculated resulting matrix.
    TVector : Translation vector.
    Quaternion : Rotation quaternion.
    SVector : Scaling vector."""
    ...
def FBTRSToMatrix(Matrix:FBMatrix,TVector:FBVector4d,RVector:FBVector3d,SVector:FBSVector):
    """Convert translation, rotation, and scaling vectors to a matrix.
    
    Matrix : Calculated resulting matrix.
    TVector : Translation vector.
    RVector : Rotation vector.
    SVector : Scaling vector."""
    ...
def FBTabPanel_TypeInfo()->int:...
def FBTake_TypeInfo()->int:...
def FBTexture_TypeInfo()->int:...
def FBThermometer_TypeInfo()->int:...
def FBTimeWarpManager_TypeInfo()->int:...
def FBToolLayoutManager_TypeInfo()->int:...
def FBTool_TypeInfo()->int:...
def FBTrace(FormatString:str):
    """This function prints useful debugging strings in the console with kFBNORMAL_TRACE output detailed level.
    
    FormatString : A printf-style format string, to use the following arguments in the list.
    p1 : ..."""
    ...
def FBTraceGetLevel()->int:
    """Get Global Trace Detailed Level which affects all the output targets.
    
    return : Current global trace detailed level."""
    ...
def FBTraceSetLevel(NewLevel:int):
    """Set Global Trace Detailed Level which affects all the output targets.
    
    NewLevel : Any trace message with detailed level higher than this new level will be ignored, valid value range [kFBNO_TRACE, kFBALL_TRACE]"""
    ...
def FBTraceWithLevel(Level:int,FormatString:str):
    """This function prints useful debugging strings in the console.
    
    Level : to control trace output detailed level, valid value range [kFBCRITICAL_TRACE, kFBALL_TRACE]
    FormatString : A printf-style format string, to use the following arguments in the list.
    p2 : ..."""
    ...
def FBTranslationToMatrix(Matrix:FBMatrix,Vector:FBVector4d):
    """Convert a translation vector to a matrix.
    
    Matrix : Calculated resulting matrix.
    Vector : Translation vector."""
    ...
def FBTransportAudioManager_TypeInfo()->int:...
def FBTreeNode_TypeInfo()->int:...
def FBTree_TypeInfo()->int:...
def FBUndoManager_TypeInfo()->int:...
def FBUserObject_TypeInfo()->int:...
def FBVectorMatrixMult(OutVector:FBVector4d,Matrix:FBMatrix,Vector:FBVector4d):
    """Multiply a vector by a matrix.
    
    OutVector : Resulting vector.
    Matrix : Matrix to affect the vector with.
    Vector : Source vector."""
    ...
def FBVertexMatrixMult(OutVertex:FBVertex,Matrix:FBMatrix,Vertex:FBVertex):
    """Multiply a vertex by a matrix.
    
    OutVertex : Resulting vertex.
    Matrix : Matrix to affect the vertex with.
    Vertex : Source vertex."""
    ...
def FBVideoClipImage_TypeInfo()->int:...
def FBVideoClip_TypeInfo()->int:...
def FBVideoGrabber_TypeInfo()->int:...
def FBVideoIn_TypeInfo()->int:...
def FBVideoMemory_TypeInfo()->int:...
def FBVideoOut_TypeInfo()->int:...
def FBVideo_TypeInfo()->int:...
def FBView_TypeInfo()->int:...
def FBVisualComponent_TypeInfo()->int:...
def FBVisualContainer_TypeInfo()->int:...
def FBWebView_TypeInfo()->int:...
def FBWidgetHolder_TypeInfo()->int:...
def GetToolPosition(arg1:FBTool)->tuple:...
def GetToolPositionByName(arg1:str)->tuple:...
def GetToolSize(arg1:FBTool)->tuple:...
def GetToolSizeByName(arg1:str)->tuple:...
def SetToolPosition(arg1:FBTool,arg2:object,arg3:object):...
def SetToolPositionByName(arg1:str,arg2:object,arg3:object):...
def SetToolSize(arg1:FBTool,arg2:object,arg3:object):...
def SetToolSizeByName(arg1:str,arg2:object,arg3:object):...
def ShowTool(arg1:FBTool,arg2:object)->object:...
def ShowToolByName(arg1:str,arg2:object)->object:...
