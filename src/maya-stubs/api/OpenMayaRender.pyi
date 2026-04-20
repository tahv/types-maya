from typing import Annotated, Literal, Sequence

from _typeshed import Incomplete
from maya.api.OpenMaya import (
    MColor,
    MColorArray,
    MDagPath,
    MDoubleArray,
    MFloatPoint,
    MMatrix,
    MObject,
    MPoint,
    MPointArray,
    MSelectionList,
    MUintArray,
    MVector,
    MVectorArray,
)
from typing_extensions import Self, TypeAlias, overload

__all__ = [
    "MAttributeParameterMapping",
    "MAttributeParameterMappingList",
    "MBlendState",
    "MBlendStateDesc",
    "MCameraOverride",
    "MClearOperation",
    "MColorManagementUtilities",
    "MComponentDataIndexing",
    "MComponentDataIndexingList",
    "MDepthNormalizationDescription",
    "MDepthStencilState",
    "MDepthStencilStateDesc",
    "MDrawContext",
    "MDrawRegistry",
    "MFragmentManager",
    "MFrameContext",
    "MGeometry",
    "MGeometryExtractor",
    "MGeometryIndexMapping",
    "MGeometryRequirements",
    "MGeometryUtilities",
    "MHUDRender",
    "MIndexBuffer",
    "MIndexBufferDescriptor",
    "MIndexBufferDescriptorList",
    "MInitContext",
    "MInitFeedback",
    "MIntersection",
    "MLightParameterInformation",
    "MPassContext",
    "MPresentTarget",
    "MPxComponentConverter",
    "MPxDrawOverride",
    "MPxGeometryOverride",
    "MPxImagePlaneOverride",
    "MPxIndexBufferMutator",
    "MPxPrimitiveGenerator",
    "MPxShaderOverride",
    "MPxShadingNodeOverride",
    "MPxSubSceneOverride",
    "MPxSurfaceShadingNodeOverride",
    "MPxVertexBufferGenerator",
    "MPxVertexBufferMutator",
    "MQuadRender",
    "MRasterizerState",
    "MRasterizerStateDesc",
    "MRenderItem",
    "MRenderItemList",
    "MRenderOperation",
    "MRenderOverride",
    "MRenderParameters",
    "MRenderProfile",
    "MRenderTarget",
    "MRenderTargetAssignment",
    "MRenderTargetDescription",
    "MRenderTargetManager",
    "MRenderUtilities",
    "MRenderer",
    "MSamplerState",
    "MSamplerStateDesc",
    "MSceneRender",
    "MSelectionContext",
    "MSelectionInfo",
    "MShaderCompileMacro",
    "MShaderInstance",
    "MShaderManager",
    "MStateManager",
    "MStencilOpDesc",
    "MSubSceneContainer",
    "MSubSceneContainerIterator",
    "MSwatchRenderBase",
    "MTargetBlendDesc",
    "MTexture",
    "MTextureAssignment",
    "MTextureDescription",
    "MTextureManager",
    "MTextureUpdateRegion",
    "MUIDrawManager",
    "MUniformParameter",
    "MUniformParameterList",
    "MUserRenderOperation",
    "MVaryingParameter",
    "MVaryingParameterList",
    "MVertexBuffer",
    "MVertexBufferArray",
    "MVertexBufferDescriptor",
    "MVertexBufferDescriptorList",
]

MAttributeParameterMapping: Incomplete
MAttributeParameterMappingList: Incomplete
MBlendStateDesc: Incomplete
MCameraOverride: Incomplete
MColorManagementUtilities: Incomplete
MComponentDataIndexing: Incomplete
MComponentDataIndexingList: Incomplete
MDepthNormalizationDescription: Incomplete
MDepthStencilState: Incomplete
MDepthStencilStateDesc: Incomplete
MDrawContext: Incomplete
MDrawRegistry: Incomplete
MFragmentManager: Incomplete
MGeometry: Incomplete
MGeometryExtractor: Incomplete
MGeometryIndexMapping: Incomplete
MGeometryRequirements: Incomplete
MGeometryUtilities: Incomplete
MHUDRender: Incomplete
MIndexBuffer: Incomplete
MIndexBufferDescriptor: Incomplete
MIndexBufferDescriptorList: Incomplete
MInitContext: Incomplete
MInitFeedback: Incomplete
MIntersection: Incomplete
MLightParameterInformation: Incomplete
MPassContext: Incomplete
MPxComponentConverter: Incomplete
MPxDrawOverride: Incomplete
MPxGeometryOverride: Incomplete
MPxImagePlaneOverride: Incomplete
MPxIndexBufferMutator: Incomplete
MPxPrimitiveGenerator: Incomplete
MPxShaderOverride: Incomplete
MPxShadingNodeOverride: Incomplete
MPxSubSceneOverride: Incomplete
MPxSurfaceShadingNodeOverride: Incomplete
MPxVertexBufferGenerator: Incomplete
MPxVertexBufferMutator: Incomplete
MQuadRender: Incomplete
MRasterizerState: Incomplete
MRasterizerStateDesc: Incomplete
MRenderItem: Incomplete
MRenderItemList: Incomplete
MRenderParameters: Incomplete
MRenderProfile: Incomplete
MRenderTarget: Incomplete
MRenderTargetAssignment: Incomplete
MRenderTargetDescription: Incomplete
MRenderTargetManager: Incomplete
MRenderUtilities: Incomplete
MSamplerStateDesc: Incomplete
MSelectionContext: Incomplete
MSelectionInfo: Incomplete
MShaderCompileMacro: Incomplete
MShaderInstance: Incomplete
MShaderManager: Incomplete
MStateManager: Incomplete
MStencilOpDesc: Incomplete
MSubSceneContainer: Incomplete
MSubSceneContainerIterator: Incomplete
MSwatchRenderBase: Incomplete
MTargetBlendDesc: Incomplete
MTexture: Incomplete
MTextureAssignment: Incomplete
MTextureDescription: Incomplete
MTextureManager: Incomplete
MTextureUpdateRegion: Incomplete
MUniformParameter: Incomplete
MUniformParameterList: Incomplete
MUserRenderOperation: Incomplete
MVaryingParameter: Incomplete
MVaryingParameterList: Incomplete
MVertexBuffer: Incomplete
MVertexBufferArray: Incomplete
MVertexBufferDescriptor: Incomplete
MVertexBufferDescriptorList: Incomplete

class MBlendState:
    kMaxTargets: Literal[8]
    BlendOperation: TypeAlias = Literal[1, 2, 3, 4, 5]
    kAdd: Literal[1]
    kSubtract: Literal[2]
    kReverseSubtract: Literal[3]
    kMin: Literal[4]
    kMax: Literal[5]
    ChannelMask: TypeAlias = Literal[1, 2, 4, 7, 8, 15]
    kNoChannels: Literal[0]
    kRedChannel: Literal[1]
    kGreenChannel: Literal[2]
    kBlueChannel: Literal[4]
    kRGBChannels: Literal[7]
    kAlphaChannel: Literal[8]
    kRGBAChannels: Literal[15]
    BlendOption: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    kZero: Literal[1]
    kOne: Literal[2]
    kSourceColor: Literal[3]
    kInvSourceColor: Literal[4]
    kSourceAlpha: Literal[5]
    kInvSourceAlpha: Literal[6]
    kDestinationAlpha: Literal[7]
    kInvDestinationAlpha: Literal[8]
    kDestinationColor: Literal[9]
    kInvDestinationColor: Literal[10]
    kSourceAlphaSat: Literal[11]
    kBothSourceAlpha: Literal[12]
    kBothInvSourceAlpha: Literal[13]
    kBlendFactor: Literal[14]
    kInvBlendFactor: Literal[15]
    def desc(self) -> MBlendStateDesc: ...
    def resourceHandle(self) -> int: ...

class MClearOperation(MRenderOperation):
    ClearMask: TypeAlias = Literal[0, 1, 2, 3, 4, -1]
    kClearNone: Literal[0]
    kClearColor: Literal[1]
    kClearDepth: Literal[2]
    kClearStencil: Literal[4]
    kClearAll: Literal[-1]
    def __init__(self, name: str, /) -> None: ...
    def clearColor(self) -> Annotated[list[float], "[r, g, b, a]"]: ...
    def clearColor2(self) -> Annotated[list[float], "[r, g, b, a]"]: ...
    def clearDepth(self) -> float: ...
    def clearGradient(self) -> bool: ...
    def clearStencil(self) -> int: ...
    def mask(self) -> int: ...
    def overridesColors(self) -> bool: ...
    def setClearColor(
        self, value: Annotated[Sequence[float], "[r, g, b, a]"], /
    ) -> Self: ...
    def setClearColor2(
        self, value: Annotated[Sequence[float], "[r, g, b, a]"], /
    ) -> Self: ...
    def setClearDepth(self, value: float, /) -> Self: ...
    def setClearGradient(self, value: bool, /) -> Self: ...
    def setClearStencil(self, value: int, /) -> Self: ...
    def setMask(self, value: int, /) -> Self: ...
    def setOverridesColors(self, value: bool, /) -> Self: ...

class MFrameContext:
    MatrixType: TypeAlias = Literal[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23,
    ]  # fmt: skip
    kWorldMtx: Literal[0]
    kWorldTransposeMtx: Literal[1]
    kWorldInverseMtx: Literal[2]
    kWorldTranspInverseMtx: Literal[3]
    kViewMtx: Literal[4]
    kViewTransposeMtx: Literal[5]
    kViewInverseMtx: Literal[6]
    kViewTranspInverseMtx: Literal[7]
    kProjectionMtx: Literal[8]
    kProjectionTranposeMtx: Literal[9]
    kProjectionInverseMtx: Literal[10]
    kProjectionTranspInverseMtx: Literal[11]
    kViewProjMtx: Literal[12]
    kViewProjTranposeMtx: Literal[13]
    kViewProjInverseMtx: Literal[14]
    kViewProjTranspInverseMtx: Literal[15]
    kWorldViewMtx: Literal[16]
    kWorldViewTransposeMtx: Literal[17]
    kWorldViewInverseMtx: Literal[18]
    kWorldViewTranspInverseMtx: Literal[19]
    kWorldViewProjMtx: Literal[20]
    kWorldViewProjTransposeMtx: Literal[21]
    kWorldViewProjInverseMtx: Literal[22]
    kWorldViewProjTranspInverseMtx: Literal[23]
    TupleType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
    kViewPosition: Literal[0]
    kViewDirection: Literal[1]
    kViewUp: Literal[2]
    kViewRight: Literal[3]
    kViewportPixelSize: Literal[4]
    kViewNearClipValue: Literal[5]
    kViewFarClipValue: Literal[6]
    kViewUnnormlizedNearClipValue: Literal[7]
    kViewUnnormalizedFarClipValue: Literal[8]
    DisplayStyle: TypeAlias = Literal[0,]
    kGouraudShaded: Literal[1]
    kWireFrame: Literal[2]
    kBoundingBox: Literal[4]
    kTextured: Literal[8]
    kDefaultMaterial: Literal[16]
    kXrayJoint: Literal[32]
    kXray: Literal[64]
    kTwoSidedLighting: Literal[128]
    kFlatShaded: Literal[256]
    kShadeActiveOnly: Literal[512]
    kXrayActiveComponents: Literal[1024]
    kBackfaceCulling: Literal[2048]
    kSmoothWireframe: Literal[4096]
    kSelectionHighlighting: Literal[8192]
    LightingMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
    kNoLighting: Literal[0]
    kAmbientLight: Literal[1]
    kLightDefault: Literal[2]
    kSelectedLights: Literal[3]
    kSceneLights: Literal[4]
    kCustomLights: Literal[5]
    PostEffectType: TypeAlias = Literal[0, 1, 2, 3, 4]
    kAmbientOcclusion: Literal[0]
    kMotionBlur: Literal[1]
    kGammaCorrection: Literal[2]
    kViewColorTransformEnabled: Literal[2]
    kDepthOfField: Literal[3]
    kAntiAliasing: Literal[4]
    FogMode: TypeAlias = Literal[0, 1, 2]
    kFogLinear: Literal[0]
    kFogExp: Literal[1]
    kFogExp2: Literal[2]
    TransparencyAlgorithm: TypeAlias = Literal[0, 1, 2, 3]
    kUnsorted: Literal[0]
    kObjectSorting: Literal[1]
    kWeightedAverage: Literal[2]
    kDepthPeeling: Literal[3]
    WireOnShadedMode: TypeAlias = Literal[0, 1, 2]
    kWireframeOnShadedFull: Literal[0]
    kWireFrameOnShadedReduced: Literal[1]
    kWireFrameOnShadedNone: Literal[2]
    RenderingDestination: TypeAlias = Literal[0, 1, 2]
    k3dViewport: Literal[0]
    k2dViewport: Literal[1]
    kImage: Literal[2]
    Exclusion: TypeAlias = Literal[
        1, 2, 4,
        8, 16, 32,
        64, 128, 256,
        512, 1024, 2048,
        4096, 8192, 16384,
        32768, 65536, 131072,
        262144, 524288, 1048576,
        2097152, 4194304, 8388608,
        16777216, 33554432, 67108864,
        134217728, 268435455, 536870912,
        1073741824, 2147483648, 4294967296,
        8589934592, 17179869184, 34359738368,
        68719476736, 18446744073709551615,
    ]  # fmt: off
    kExcludeNone: Literal[0]
    kExcludeNurbsCurves: Literal[1]
    kExcludeNurbsSurfaces: Literal[2]
    kExcludeMeshes: Literal[4]
    kExcludePlanes: Literal[8]
    kExcludeLights: Literal[16]
    kExcludeCameras: Literal[32]
    kExcludeJoints: Literal[64]
    kExcludeIkHandles: Literal[128]
    kExcludeDeformers: Literal[256]
    kExcludeDynamics: Literal[512]
    kExcludeParticleInstancers: Literal[1024]
    kExcludeLocators: Literal[2048]
    kExcludeDimensions: Literal[4096]
    kExcludeSelectHandles: Literal[8192]
    kExcludePivots: Literal[16384]
    kExcludeTextures: Literal[32768]
    kExcludeGrid: Literal[65536]
    kExcludeCVs: Literal[131072]
    kExcludeStrokes: Literal[524288]
    kExcludeSubdivSurfaces: Literal[1048576]
    kExcludeFluids: Literal[2097152]
    kExcludeFollicles: Literal[4194304]
    kExcludeHairSystems: Literal[8388608]
    kExcludeImagePlane: Literal[16777216]
    kExcludeNCloths: Literal[33554432]
    kExcludeNRigids: Literal[67108864]
    kExcludeDynamicConstraints: Literal[134217728]
    kExcludeManipulators: Literal[268435456]
    kExcludeNParticles: Literal[536870912]
    kExcludeMotionTrails: Literal[1073741824]
    kExcludeHoldOuts: Literal[2147483648]
    kExcludePluginShapes: Literal[4294967296]
    kExcludeHUD: Literal[8589934592]
    kExcludeClipGhosts: Literal[17179869184]
    kExcludeGreasePencils: Literal[34359738368]
    kExcludeControllers: Literal[68719476736]
    kExcludeAll: Literal[18446744073709551615]
    def __init__(self) -> None: ...
    def classificationExclusions(self) -> list[str]: ...
    def getBackgroundParameters(
        self,
    ) -> Annotated[
        tuple[bool, bool, bool, bool, MColor, MColor, float, int],
        "[displayGradient, clearColorFlag, clearDepthFlag, clearStencilFlag, clearColor1, clearColor2, clearDepthValue, clearStencilValue]",
    ]: ...
    def getCurrentCameraPath(self) -> MDagPath: ...
    def getCurrentColorRenderTarget(self) -> MRenderTarget: ...
    def getCurrentDepthRenderTarget(self) -> MRenderTarget: ...
    def getDOFParameters(
        self,
    ) -> Annotated[tuple[bool, float, float], "[enabled, focalDistance, alpha]"]: ...
    def getDisplayStyle(self) -> DisplayStyle: ...
    def getEnvironmentParameters(
        self,
    ) -> Annotated[tuple[bool, str], "[enabled, filePath]"]: ...
    def getGlobalLineWidth(self) -> float: ...
    def getHwFogParameters(
        self,
    ) -> Annotated[
        tuple[bool, FogMode, float, float, float, MColor],
        "[enabled, mode, start, end, density, color]",
    ]: ...
    def getLightLimit(self) -> int: ...
    def getLightingMode(self) -> LightingMode: ...
    def getMatrix(self, mtype: MatrixType, /) -> MMatrix: ...
    def getPostEffectEnabled(self, postEffectType: PostEffectType, /) -> bool: ...
    def getRenderOverrideInformation(self) -> Annotated[tuple[str], "[name]"]: ...
    def getTransparencyAlgorithm(self) -> TransparencyAlgorithm: ...
    def getTuple(self, ttype: TupleType, /) -> MDoubleArray: ...
    def getViewportDimensions(
        self,
    ) -> Annotated[tuple[int, int, int, int], "[originX, originY, width, height]"]: ...
    def objectTypeExclusions(self) -> Exclusion: ...
    def renderingDestination(
        self,
    ) -> Annotated[
        tuple[RenderingDestination, str], "[RenderingDestination, destinationName]"
    ]: ...
    @staticmethod
    def inUserInteraction() -> bool: ...
    @staticmethod
    def semanticToMatrixType(value: str) -> MatrixType: ...
    @staticmethod
    def semanticToTupleType(value: str) -> TupleType: ...
    @staticmethod
    def shadeTemplates() -> bool: ...
    @staticmethod
    def userChangingViewContext() -> bool: ...
    @staticmethod
    def wireOnShadedMode() -> WireOnShadedMode: ...

class MPresentTarget(MRenderOperation):
    MTargetBackBuffer: TypeAlias = Literal[0, 1, 2]
    kCenterBuffer: Literal[0]
    kLeftBuffer: Literal[1]
    kRightBuffer: Literal[2]
    def __init__(self, name: str, /) -> None: ...
    def presentDepth(self) -> bool: ...
    def setPresentDepth(self, val: bool, /) -> Self: ...
    def setTargetBackBuffer(self, backBuffer: MTargetBackBuffer) -> Self: ...
    def targetBackBuffer(self) -> MTargetBackBuffer: ...

class MRenderer:
    @staticmethod
    def GPUDeviceHandle() -> int: ...
    @staticmethod
    def GPUmaximumPrimitiveCount() -> int: ...
    @staticmethod
    def GPUmaximumVertexBufferSize() -> int: ...
    @staticmethod
    def activeRenderOverride() -> str: ...
    @staticmethod
    def copyTargetToScreen(renderTarget: MRenderTarget, /) -> bool: ...
    @staticmethod
    def deregisterOverride(roverride: MRenderOverride, /) -> None: ...
    @staticmethod
    def disableChangeManagementUntilNextRefresh() -> None: ...
    @staticmethod
    def drawAPI() -> DrawAPI: ...
    @staticmethod
    def drawAPIIsOpenGL() -> bool: ...
    @staticmethod
    def drawAPIVersion() -> int: ...
    @staticmethod
    def findRenderOverride(name: str, /) -> MRenderOverride | None: ...
    @staticmethod
    def getFragmentManager() -> MFragmentManager | None: ...
    @staticmethod
    def getOutputTargetOverrideSize() -> Annotated[
        tuple[int, int], "[width, height]"
    ]: ...
    @staticmethod
    def getRenderTargetManager() -> MRenderTargetManager | None: ...
    @staticmethod
    def getShaderManager() -> MShaderManager | None: ...
    @staticmethod
    def getTextureManager() -> MTextureManager | None: ...
    @staticmethod
    def needEvaluateAllLights() -> None: ...
    @staticmethod
    def outputTargetSize() -> Annotated[tuple[int, int], "[width, height]"]: ...
    @staticmethod
    def registerOverride(roveridde: MRenderOverride, /) -> None: ...
    @staticmethod
    def render(sourceName: str, targetList: list[MRenderTarget], /) -> bool: ...
    @staticmethod
    def renderOverrideCount() -> int: ...
    @staticmethod
    def renderOverrideName() -> str: ...
    @staticmethod
    def setGeometryDrawDirty(
        object: MObject, /, topologyChanged: bool = True
    ) -> None: ...
    @staticmethod
    def setLightRequiresShadows(object: MObject, flag: bool, /) -> bool: ...
    @staticmethod
    def setLightsAndShadowsDirty() -> None: ...
    @staticmethod
    def setOutputTargetOverrideSize(width: int, height: int, /) -> None: ...
    @staticmethod
    def setRenderOverrideName(name: str, /) -> bool: ...
    @staticmethod
    def unsetOutputTargetOverrideSize() -> None: ...
    DrawAPI: TypeAlias = Literal[0, 1, 2, 4, 7]
    kNone: Literal[0]
    kOpenGL: Literal[1]
    kDirectX11: Literal[2]
    kOpenGLCoreProfile: Literal[4]
    kAllDevices: Literal[7]
    MRasterFormat: TypeAlias = Literal[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
    ]  # fmt: skip
    kD24S8: Literal[0]
    kD24X8: Literal[1]
    kD32_FLOAT: Literal[2]
    kR24G8: Literal[3]
    kR24X8: Literal[4]
    kDXT1_UNORM: Literal[5]
    kDXT1_UNORM_SRGB: Literal[6]
    kDXT2_UNORM: Literal[7]
    kDXT2_UNORM_SRGB: Literal[8]
    kDXT2_UNORM_PREALPHA: Literal[9]
    kDXT3_UNORM: Literal[10]
    kDXT3_UNORM_SRGB: Literal[11]
    kDXT3_UNORM_PREALPHA: Literal[12]
    kDXT4_UNORM: Literal[13]
    kDXT4_SNORM: Literal[14]
    kDXT5_UNORM: Literal[15]
    kDXT5_SNORM: Literal[16]
    kBC6H_UF16: Literal[17]
    kBC6H_SF16: Literal[18]
    kBC7_UNORM: Literal[19]
    kBC7_UNORM_SRGB: Literal[20]
    kR9G9B9E5_FLOAT: Literal[21]
    kR1_UNORM: Literal[22]
    kA8: Literal[23]
    kR8_UNORM: Literal[24]
    kR8_SNORM: Literal[25]
    kR8_UINT: Literal[26]
    kR8_SINT: Literal[27]
    kL8: Literal[28]
    kR16_FLOAT: Literal[29]
    kR16_UNORM: Literal[30]
    kR16_SNORM: Literal[31]
    kR16_UINT: Literal[32]
    kR16_SINT: Literal[33]
    kL16: Literal[34]
    kR8G8_UNORM: Literal[35]
    kR8G8_SNORM: Literal[36]
    kR8G8_UINT: Literal[37]
    kR8G8_SINT: Literal[38]
    kB5G5R5A1: Literal[39]
    kB5G6R5: Literal[40]
    kR32_FLOAT: Literal[41]
    kR32_UINT: Literal[42]
    kR32_SINT: Literal[43]
    kR16G16_FLOAT: Literal[44]
    kR16G16_UNORM: Literal[45]
    kR16G16_SNORM: Literal[46]
    kR16G16_UINT: Literal[47]
    kR16G16_SINT: Literal[48]
    kR8G8B8A8_UNORM: Literal[49]
    kR8G8B8A8_SNORM: Literal[50]
    kR8G8B8A8_UINT: Literal[51]
    kR8G8B8A8_SINT: Literal[52]
    kR10G10B10A2_UNORM: Literal[53]
    kR10G10B10A2_UINT: Literal[54]
    kB8G8R8A8: Literal[55]
    kB8G8R8X8: Literal[56]
    kR8G8B8X8: Literal[57]
    kA8B8G8R8: Literal[58]
    kR32G32_FLOAT: Literal[59]
    kR32G32_UINT: Literal[60]
    kR32G32_SINT: Literal[61]
    kR16G16B16A16_FLOAT: Literal[62]
    kR16G16B16A16_UNORM: Literal[63]
    kR16G16B16A16_SNORM: Literal[64]
    kR16G16B16A16_UINT: Literal[65]
    kR16G16B16A16_SINT: Literal[66]
    kR32G32B32_FLOAT: Literal[67]
    kR32G32B32_UINT: Literal[68]
    kR32G32B32_SINT: Literal[69]
    kR32G32B32A32_FLOAT: Literal[70]
    kR32G32B32A32_UINT: Literal[71]
    kR32G32B32A32_SINT: Literal[72]
    kNumberOfRasterFormats: Literal[73]

class MRenderOperation:
    MRenderOperationType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]
    kClear: Literal[0]
    kSceneRender: Literal[1]
    kQuadRender: Literal[2]
    kUserDefined: Literal[3]
    kDataServer: Literal[4]
    kHUDRender: Literal[5]
    kPresentTarget: Literal[6]
    def __init__(self, name: str, /) -> None: ...
    def enableSRGBWrite(self) -> bool: ...
    def name(self) -> str: ...
    def operationType(self) -> MRenderOperationType: ...
    def targetOverrideList(self) -> list[MRenderTarget]: ...
    def viewportRectangleOverride(self) -> MFloatPoint: ...

class MRenderOverride:
    def __init__(self, name: str, /) -> None: ...
    def cleanup(self) -> Self: ...
    def getFrameContext(self) -> MFrameContext: ...
    def name(self) -> str: ...
    def nextRenderOperation(self) -> bool: ...
    def renderOperation(self) -> MRenderOperation: ...
    def select(
        self,
        frameContext: MFrameContext,
        selectInfo: MSelectionInfo,
        useDepth: bool,
        selectionList: MSelectionList,
        worldSpaceHitPts: MPointArray,
        /,
    ) -> bool: ...
    def setup(self, destination: str) -> Self: ...
    def startOperationIterator(self) -> bool: ...
    def supportedDrawAPIs(self) -> MRenderer.DrawAPI: ...
    def uiName(self) -> str: ...

class MSamplerState:
    TextureFilter: TypeAlias = Literal[0, 1, 4, 5, 16, 17, 20, 21, 85]
    kMinMagMipPoint: Literal[0]
    kMinMagPoint_MipLinear: Literal[1]
    kMinPoint_MagLinear_MipPoint: Literal[4]
    kMinPoint_MagMipLinear: Literal[5]
    kMinLinear_MagMipPoint: Literal[16]
    kMinLinear_MagPoint_MipLinear: Literal[17]
    kMinMagLinear_MipPoint: Literal[20]
    kMinMagMipLinear: Literal[21]
    kAnisotropic: Literal[85]
    TextureAddress: TypeAlias = Literal[1, 2, 3, 4]
    kTexWrap: Literal[1]
    kTexMirror: Literal[2]
    kTexClamp: Literal[3]
    kTexBorder: Literal[4]
    def desc(self) -> MSamplerStateDesc: ...
    def resourceHandle(self) -> int: ...

class MSceneRender(MRenderOperation):
    MObjectTypeExclusions: TypeAlias = Literal[
        1, 2, 4,
        8, 16, 32,
        64, 128, 256,
        512, 1024, 2048,
        4096, 8192, 16384,
        32768, 65536, 131072,
        262144, 524288, 1048576,
        2097152, 4194304, 8388608,
        16777216, 33554432, 67108864,
        134217728, 268435455, 536870912,
        1073741824,
        -2147483648, -1,
    ]  # fmt: off
    kExcludeNone: Literal[0]
    kExcludeNurbsCurves: Literal[1]
    kExcludeNurbsSurfaces: Literal[2]
    kExcludeMeshes: Literal[4]
    kExcludePlanes: Literal[8]
    kExcludeLights: Literal[16]
    kExcludeCameras: Literal[32]
    kExcludeJoints: Literal[64]
    kExcludeIkHandles: Literal[128]
    kExcludeDeformers: Literal[256]
    kExcludeDynamics: Literal[512]
    kExcludeParticleInstancers: Literal[1024]
    kExcludeLocators: Literal[2048]
    kExcludeDimensions: Literal[4096]
    kExcludeSelectHandles: Literal[8192]
    kExcludePivots: Literal[16384]
    kExcludeTextures: Literal[32768]
    kExcludeGrid: Literal[65536]
    kExcludeCVs: Literal[131072]
    kExcludeHulls: Literal[262144]
    kExcludeStrokes: Literal[524288]
    kExcludeSubdivSurfaces: Literal[1048576]
    kExcludeFluids: Literal[2097152]
    kExcludeFollicles: Literal[4194304]
    kExcludeHairSystems: Literal[8388608]
    kExcludeImagePlane: Literal[16777216]
    kExcludeNCloths: Literal[33554432]
    kExcludeNRigids: Literal[67108864]
    kExcludeDynamicConstraints: Literal[134217728]
    kExcludeManipulators: Literal[268435456]
    kExcludeNParticles: Literal[536870912]
    kExcludeMotionTrails: Literal[1073741824]
    kExcludeHoldOuts: Literal[-2147483648]
    kExcludeAll: Literal[-1]
    MSceneFilterOption: TypeAlias = Literal[0, 1, 2, 4, 6, 8, 9, -1]
    kNoSceneFilterOverride: Literal[0]
    kRenderPreSceneUIItems: Literal[1]
    kRenderOpaqueShadedItems: Literal[2]
    kRenderTransparentShadedItems: Literal[4]
    kRenderShadedItems: Literal[6]
    kRenderPostSceneUIItems: Literal[8]
    kRenderNonShadedItems: Literal[9]  # TODO(tga): undocumented
    kRenderUIItems: Literal[9]  # TODO(tga): deprecated ?
    kRenderAllItems: Literal[-1]
    MDisplayMode: TypeAlias = Literal[1, 2, 4, 8, 16, 32, 64]
    kNoDisplayModeOverride: Literal[0]
    kWireFrame: Literal[1]
    kShaded: Literal[2]
    kFlatShaded: Literal[4]
    kShadeActiveOnly: Literal[8]
    kBoundingBox: Literal[16]
    kDefaultMaterial: Literal[32]
    kTextured: Literal[64]
    MLightingMode: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
    kNoLightingModeOverride: Literal[0]
    kNoLight: Literal[1]
    kAmbientLight: Literal[2]
    kLightDefault: Literal[3]
    kSelectedLights: Literal[4]
    kSceneLights: Literal[5]
    MPostEffectsOverride: TypeAlias = Literal[0, 1, 2, 4, -1]
    kPostEffectDisableNone: Literal[0]
    kPostEffectDisableSSAO: Literal[1]
    kPostEffectDisableMotionBlur: Literal[2]
    kPostEffectDisableDOF: Literal[4]
    kPostEffectDisableAll: Literal[-1]
    MCullingOption: TypeAlias = Literal[0, 1, 2, 3]
    kNoCullingOverride: Literal[0]
    kCullNone: Literal[1]
    kCullBackFaces: Literal[2]
    kCullFrontFaces: Literal[3]
    @overload
    def __init__(self, name: str, /) -> None: ...
    @overload
    def __init__(self, name: str, fragmentName: str, /) -> None: ...
    def addPostUIDrawables(
        self, drawManager: MUIDrawManager, frameContext: MFrameContext, /
    ) -> Self: ...
    def addPreUIDrawables(
        self, drawManager: MUIDrawManager, frameContext: MFrameContext, /
    ) -> Self: ...
    def cameraOverride(self) -> MCameraOverride: ...
    def clearOperation(self) -> MClearOperation: ...
    def cullingOverride(self) -> MCullingOption: ...
    def displayModeOverride(self) -> MDisplayMode: ...
    def fragmentName(self) -> str: ...
    def getObjectTypeExclusions(self) -> MObjectTypeExclusions: ...
    def getParameters(self) -> MRenderParameters: ...
    def hasUIDrawables(self) -> bool: ...
    def lightModeOverride(self) -> MLightingMode: ...
    def objectSetOverride(self) -> MSelectionList: ...
    def objectTypeExclusions(self) -> MObjectTypeExclusions: ...
    def postEffectsOverride(self) -> MPostEffectsOverride: ...
    def postRender(self) -> Self: ...
    def postSceneRender(self, context: MDrawContext, /) -> Self: ...
    def preRender(self) -> Self: ...
    def preSceneRender(self, context: MDrawContext, /) -> Self: ...
    def renderFilterOverride(self) -> MSceneFilterOption: ...
    def shaderOverride(self) -> MShaderInstance: ...
    def shadowEnableOverride(self) -> bool | None: ...
    @property
    def mClearOperation(self) -> MClearOperation: ...

class MUIDrawManager:
    FontSize: TypeAlias = Literal[9, 12]
    kSmallFontSize: Literal[9]
    kDefaultFontSize: Literal[12]
    TextAlignment: TypeAlias = Literal[0, 1, 2]
    kLeft: Literal[0]
    kCenter: Literal[1]
    kRight: Literal[2]
    TextIncline: TypeAlias = Literal[0, 1, 2]
    kInclineNormal: Literal[0]
    kInclineItalic: Literal[1]
    kInclineOblique: Literal[2]
    TextWeight: TypeAlias = Literal[300, 400, 600, 700, 900]
    kWeightLight: Literal[300]
    kWeightNormal: Literal[400]
    kWeightDemiBold: Literal[600]
    kWeightBold: Literal[700]
    kWeightBlack: Literal[900]
    TextStretch: TypeAlias = Literal[50, 62, 75, 87, 100, 112, 125, 150, 200]
    kStretchUltraCondensed: Literal[50]
    kStretchExtraCondensed: Literal[62]
    kStretchCondensed: Literal[75]
    kStretchSemiCondensed: Literal[87]
    kStretchUnstretched: Literal[100]
    kStretchSemiExpanded: Literal[112]
    kStretchExpanded: Literal[125]
    kStretchExtraExpanded: Literal[150]
    kStretchUltraExpanded: Literal[200]
    TextLine: TypeAlias = Literal[0, 1, 2, 3]
    kLineNone: Literal[0]
    kLineOverline: Literal[1]
    kLineUnderline: Literal[2]
    kLineStrikeoutLine: Literal[3]
    LineStyle: TypeAlias = Literal[0, 1, 2, 3, 4]
    kSolid: Literal[0]
    kShortDotted: Literal[1]
    kShortDashed: Literal[2]
    kDashed: Literal[3]
    kDotted: Literal[4]
    PaintStyle: TypeAlias = Literal[0, 1, 2]
    kFlat: Literal[0]
    kStippled: Literal[1]
    kShaded: Literal[2]
    Primitive: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
    kPoints: Literal[0]
    kLines: Literal[1]
    kLineStrip: Literal[2]
    kClosedLine: Literal[3]
    kTriangles: Literal[4]
    kTriStrip: Literal[5]
    Selectability: TypeAlias = Literal[0, 1, 2]
    kNonSelectable: Literal[0]
    kSelectable: Literal[1]
    kAutomatic: Literal[2]
    def __init__(self) -> None: ...
    @overload
    def arc(
        self,
        center: MPoint,
        start: MVector,
        end: MVector,
        normal: MVector,
        radius: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def arc(
        self,
        center: MPoint,
        start: MVector,
        end: MVector,
        normal: MVector,
        radius: float,
        numSubdivisions: int,
        filled: bool,
        /,
    ) -> Self: ...
    @overload
    def arc2d(
        self,
        center: MPoint,
        start: MVector,
        end: MVector,
        radius: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def arc2d(
        self,
        center: MPoint,
        start: MVector,
        end: MVector,
        radius: float,
        numSubdivisions: int,
        filled: bool,
        /,
    ) -> Self: ...
    def beginDrawInXray(self) -> Self: ...
    def beginDrawable(
        self, selectability: Selectability = kAutomatic, selectionName: int = 0
    ) -> Self: ...
    def box(
        self,
        center: MPoint,
        up: MVector,
        right: MVector,
        /,
        scaleX: float = 1.0,
        scaleY: float = 1.0,
        scaleZ: float = 1.0,
        filled: bool = False,
    ) -> Self: ...
    def capsule(
        self,
        center: MPoint,
        up: MVector,
        radius: float,
        height: float,
        subdivisionsAxis: int,
        subdivisionsHeight: int,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def circle(
        self,
        center: MPoint,
        normal: MVector,
        radius: float,
        numSubdivision: int,
        /,
        filled: bool,
    ) -> Self: ...
    @overload
    def circle(
        self,
        center: MPoint,
        normal: MVector,
        radius: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def circle2d(
        self,
        center: MPoint,
        radius: float,
        numSubdivision: int,
        filled: bool,
        /,
    ) -> Self: ...
    @overload
    def circle2d(
        self,
        center: MPoint,
        radius: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def cone(
        self,
        base: MPoint,
        direction: MVector,
        radius: float,
        height: float,
        subdivisionsCap: int,
        filled: bool,
        /,
    ) -> Self: ...
    @overload
    def cone(
        self,
        base: MPoint,
        direction: MVector,
        radius: float,
        height: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    def cylinder(
        self,
        center: MPoint,
        up: MVector,
        radius: float,
        height: float,
        subdivisionsAxis: int,
        /,
        filled: bool = False,
    ) -> Self: ...
    def depthPriority(self) -> int: ...
    def endDrawInXray(self) -> Self: ...
    def endDrawable(self) -> Self: ...
    def icon(self, position: MPoint, name: str, scale: float, /) -> Self: ...
    def line(self, startPoint: MPoint, endPoint: MPoint, /) -> Self: ...
    def line2d(self, startPoint: MPoint, endPoint: MPoint, /) -> Self: ...
    def lineList(self, points: MPointArray, draw2D: bool, /) -> Self: ...
    def lineStrip(self, points: MPointArray, draw2D: bool, /) -> Self: ...
    def mesh(
        self,
        mode: Primitive,
        position: MPointArray,
        /,
        normal: MVectorArray | None = None,
        color: MColorArray | None = None,
        index: MUintArray | None = None,
        texcoord: MPointArray | None = None,
    ) -> Self: ...
    def mesh2d(
        self,
        mode: Primitive,
        position: MPointArray,
        /,
        color: MColorArray | None = None,
        index: MUintArray | None = None,
        texcoord: MPointArray | None = None,
    ) -> Self: ...
    def point(self, point: MPoint, /) -> Self: ...
    def point2d(self, point: MPoint, /) -> Self: ...
    def points(self, points: MPointArray, draw2D: bool, /) -> Self: ...
    def rect(
        self,
        center: MPoint,
        up: MVector,
        normal: MVector,
        scaleX: float,
        scaleY: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    def rect2d(
        self,
        center: MPoint,
        up: MVector,
        scaleX: float,
        scaleY: float,
        /,
        filled: bool = False,
    ) -> Self: ...
    def setColor(self, color: MColor, /) -> Self: ...
    def setColorIndex(self, index: int, /) -> Self: ...
    def setDepthPriority(self, priority: int, /) -> Self: ...
    def setFontIncline(self, fontIncline: int | TextIncline, /) -> Self: ...
    def setFontLine(self, fontLine: int | TextLine, /) -> Self: ...
    def setFontName(self, faceName: str, /) -> Self: ...
    def setFontSize(self, fontSize: int | FontSize, /) -> Self: ...
    def setFontStretch(self, fontStretch: int | TextStretch, /) -> Self: ...
    def setFontWeight(self, fontWeight: int | TextWeight, /) -> Self: ...
    @overload
    def setLineStyle(self, style: LineStyle, /) -> Self: ...
    @overload
    def setLineStyle(self, factor: int, pattern: int, /) -> Self: ...
    def setLineWidth(self, value: float, /) -> Self: ...
    def setPaintStyle(self, style: PaintStyle, /) -> Self: ...
    def setPointSize(self, value: float, /) -> Self: ...
    def setTexture(self, texture: MTexture, /) -> Self: ...
    def setTextureMask(
        self,
        mask: Annotated[
            MBlendState.ChannelMask,
            MBlendState.kRGBAChannels
            | MBlendState.kRGBChannels
            | MBlendState.kAlphaChannel,
        ],
        /,
    ) -> Self: ...
    def setTextureSampler(
        self,
        filter: Annotated[
            MSamplerState.TextureFilter,
            MSamplerState.kMinMagMipPoint | MSamplerState.kMinMagMipLinear,
        ],
        address: Annotated[
            MSamplerState.TextureAddress,
            MSamplerState.kTexWrap | MSamplerState.kTexClamp,
        ],
    ) -> Self: ...
    @overload
    def sphere(
        self,
        center: MPoint,
        radius: float,
        subdivisionsAxis: int,
        subdivisionsHeight: int,
        /,
        filled: bool = False,
    ) -> Self: ...
    @overload
    def sphere(
        self, center: MPoint, radius: float, /, filled: bool = False
    ) -> Self: ...
    def text(
        self,
        position: MPoint,
        text: str,
        /,
        alignment: TextAlignment = kLeft,
        backgroundSize: tuple[int, int] | None = None,
        backgroundColor: MColor | None = None,
        dynamic: bool = False,
    ) -> Self: ...
    def text2d(
        self,
        position: MPoint,
        text: str,
        /,
        alignment: TextAlignment = kLeft,
        backgroundSize: tuple[int, int] | None = None,
        backgroundColor: MColor | None = None,
        dynamic: bool = False,
    ) -> Self: ...
    @staticmethod
    def getFontList() -> list[str]: ...
    @staticmethod
    def getIconNames() -> list[str]: ...
