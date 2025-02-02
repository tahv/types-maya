import typing

from _typeshed import Incomplete

MArgDatabase: Incomplete
MArgList: Incomplete
MArgParser: Incomplete
MArrayDataBuilder: Incomplete
MArrayDataHandle: Incomplete
MAttributeIndex: Incomplete
MAttributePattern: Incomplete
MAttributeSpec: Incomplete
MAttributeSpecArray: Incomplete
MBoundingBox: Incomplete
MCacheSchema: Incomplete
MCallbackId: Incomplete
MCallbackIdArray: Incomplete
MCameraMessage: Incomplete
MColor: Incomplete
MColorArray: Incomplete
MCommandMessage: Incomplete
MConditionMessage: Incomplete
MContainerMessage: Incomplete
MDAGDrawOverrideInfo: Incomplete
MDagMessage: Incomplete
MDagModifier: Incomplete
MDagPath: Incomplete
MDagPathArray: Incomplete
MDataBlock: Incomplete
MDataHandle: Incomplete
MDGContext: Incomplete
MDGMessage: Incomplete
MDGModifier: Incomplete
MDoubleArray: Incomplete
MEulerRotation: Incomplete
MEvaluationNode: Incomplete
MEvaluationNodeIterator: Incomplete
MEventMessage: Incomplete
MExternalContentInfoTable: Incomplete
MExternalContentLocationTable: Incomplete
MFileObject: Incomplete
MFloatArray: Incomplete
MFloatMatrix: Incomplete
MFloatPoint: Incomplete
MFloatPointArray: Incomplete
MFloatVector: Incomplete
MFloatVectorArray: Incomplete
MFn: Incomplete
MFnAssembly: Incomplete
MFnCamera: Incomplete
MFnComponent: Incomplete
MFnComponentListData: Incomplete
MFnCompoundAttribute: Incomplete
MFnContainerNode: Incomplete
MFnDagNode: Incomplete
MFnDependencyNode: Incomplete
MFnDisplayLayer: Incomplete
MFnDisplayLayerManager: Incomplete
MFnDoubleArrayData: Incomplete
MFnDoubleIndexedComponent: Incomplete
MFnEnumAttribute: Incomplete
MFnGenericAttribute: Incomplete
MFnGeometryData: Incomplete
MFnIntArrayData: Incomplete
MFnLightDataAttribute: Incomplete
MFnMatrixArrayData: Incomplete
MFnMatrixAttribute: Incomplete
MFnMatrixData: Incomplete
MFnMesh: Incomplete
MFnMeshData: Incomplete
MFnMessageAttribute: Incomplete
MFnNumericAttribute: Incomplete
MFnNumericData: Incomplete
MFnNurbsCurve: Incomplete
MFnNurbsCurveData: Incomplete
MFnNurbsSurface: Incomplete
MFnNurbsSurfaceData: Incomplete
MFnPlugin: Incomplete
MFnPluginData: Incomplete
MFnPointArrayData: Incomplete
MFnReference: Incomplete
MFnSet: Incomplete
MFnSingleIndexedComponent: Incomplete
MFnStringArrayData: Incomplete
MFnStringData: Incomplete
MFnTransform: Incomplete
MFnTripleIndexedComponent: Incomplete
MFnTypedAttribute: Incomplete
MFnUInt64ArrayData: Incomplete
MFnUnitAttribute: Incomplete
MFnVectorArrayData: Incomplete
MGlobal: Incomplete
MImage: Incomplete
MInt64Array: Incomplete
MIntArray: Incomplete
MItCurveCV: Incomplete
MItDag: Incomplete
MItDependencyGraph: Incomplete
MItDependencyNodes: Incomplete
MIteratorType: Incomplete
MItGeometry: Incomplete
MItMeshEdge: Incomplete
MItMeshFaceVertex: Incomplete
MItMeshPolygon: Incomplete
MItMeshVertex: Incomplete
MItSelectionList: Incomplete
MItSurfaceCV: Incomplete
MLockMessage: Incomplete
MMatrixArray: Incomplete
MMeshIntersector: Incomplete
MMeshIsectAccelParams: Incomplete
MMeshSmoothOptions: Incomplete
MMessage: Incomplete
MModelMessage: Incomplete
MNamespace: Incomplete
MNodeCacheDisablingInfo: Incomplete
MNodeCacheSetupInfo: Incomplete
MNodeClass: Incomplete
MNodeMessage: Incomplete
MObjectArray: Incomplete
MObjectHandle: Incomplete
MObjectSetMessage: Incomplete
MPlane: Incomplete
MPlug: Incomplete
MPlugArray: Incomplete
MPoint: Incomplete
MPointArray: Incomplete
MPointOnMesh: Incomplete
MPolyMessage: Incomplete
MPxAttributePatternFactory: Incomplete
MPxCommand: Incomplete
MPxData: Incomplete
MPxGeometryData: Incomplete
MPxGeometryIterator: Incomplete
MPxNode: Incomplete
MPxSurfaceShape: Incomplete
MQuaternion: Incomplete
MRampAttribute: Incomplete
MRichSelection: Incomplete
MSceneMessage: Incomplete
MSelectionList: Incomplete
MSelectionMask: Incomplete
MSyntax: Incomplete
MTimeArray: Incomplete
MTimeRange: Incomplete
MTimerMessage: Incomplete
MUint64Array: Incomplete
MUintArray: Incomplete
MURI: Incomplete
MUserData: Incomplete
MUserEventMessage: Incomplete
MUuid: Incomplete
MVector: Incomplete
MVectorArray: Incomplete
MWeight: Incomplete

_MFnType: typing.TypeAlias = int

class MFnBase:
    @typing.overload
    def hasObj(self, type: _MFnType, /) -> bool: ...
    @typing.overload
    def hasObj(self, object: MObject, /) -> bool: ...
    def object(self) -> MObject: ...
    def setObject(self, object: MObject, /) -> typing.Self: ...
    def type(self) -> _MFnType: ...

class MObject:
    kNullObj: MObject

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MObject, /) -> None: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...
    def apiType(self) -> _MFnType: ...
    def hasFn(self, fn: _MFnType, /) -> bool: ...
    def isNull(self) -> bool: ...
    @property
    def apiTypeStr(self) -> str: ...

class MTypeId:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MTypeId, /) -> None: ...
    @typing.overload
    def __init__(self, id: int, /) -> None: ...
    @typing.overload
    def __init__(self, prefix: int, id: int, /) -> None: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...
    def id(self) -> int: ...

_DisconnectBehavior: typing.TypeAlias = typing.Literal[0, 1, 2]

class MFnAttribute(MFnBase):
    kDelete: typing.Literal[0]
    kReset: typing.Literal[1]
    kNothing: typing.Literal[2]

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, object: MObject, /) -> None: ...
    def accepts(self, type: MTypeId | _MFnType, /) -> bool: ...
    def acceptsAttribute(self, attr: MFnAttribute, /) -> bool: ...
    def addToCategory(self, category: str, /) -> bool: ...
    def getAddAttrCmd(self, longFlags: bool) -> str: ...
    def hasCategory(self, category: str, /) -> str: ...
    def pathName(self) -> str: ...
    def setNiceNameOverride(self, localizedName: str, /) -> None: ...
    @property
    def affectsAppearance(self) -> bool: ...
    @affectsAppearance.setter
    def affectsAppearance(self, value: bool) -> None: ...
    @property
    def affectsWorldSpace(self) -> bool: ...
    @affectsWorldSpace.setter
    def affectsWorldSpace(self, value: bool) -> None: ...
    @property
    def array(self) -> bool: ...
    @array.setter
    def array(self, value: bool) -> None: ...
    @property
    def cached(self) -> bool: ...
    @cached.setter
    def cached(self, value: bool) -> None: ...
    @property
    def channelBox(self) -> bool: ...
    @channelBox.setter
    def channelBox(self, value: bool) -> None: ...
    @property
    def connectable(self) -> bool: ...
    @connectable.setter
    def connectable(self, value: bool) -> None: ...
    @property
    def disconnectBehavior(self) -> _DisconnectBehavior: ...
    @disconnectBehavior.setter
    def disconnectBehavior(self, value: _DisconnectBehavior) -> None: ...
    @property
    def dynamic(self) -> bool: ...
    @property
    def enforcingUniqueName(self) -> bool: ...
    @property
    def extension(self) -> bool: ...
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool) -> None: ...
    @property
    def indeterminant(self) -> bool: ...
    @indeterminant.setter
    def indeterminant(self, value: bool) -> None: ...
    @property
    def indexMatters(self) -> bool: ...
    @indexMatters.setter
    def indexMatters(self, value: bool) -> None: ...
    @property
    def internal(self) -> bool: ...
    @internal.setter
    def internal(self, value: bool) -> None: ...
    @property
    def isProxyAttribute(self) -> bool: ...
    @property
    def keyable(self) -> bool: ...
    @keyable.setter
    def keyable(self, value: bool) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def parent(self) -> bool: ...
    @parent.setter
    def parent(self, value: MObject) -> None: ...
    @property
    def readable(self) -> bool: ...
    @readable.setter
    def readable(self, value: bool) -> None: ...
    @property
    def renderSource(self) -> bool: ...
    @renderSource.setter
    def renderSource(self, value: bool) -> None: ...
    @property
    def shortName(self) -> str: ...
    @property
    def storable(self) -> bool: ...
    @storable.setter
    def storable(self, value: bool) -> None: ...
    @property
    def usedAsColor(self) -> bool: ...
    @usedAsColor.setter
    def usedAsColor(self, value: bool) -> None: ...
    @property
    def usedAsFilename(self) -> bool: ...
    @usedAsFilename.setter
    def usedAsFilename(self, value: bool) -> None: ...
    @property
    def usesArrayDataBuilder(self) -> bool: ...
    @usesArrayDataBuilder.setter
    def usesArrayDataBuilder(self, value: bool) -> None: ...
    @property
    def worldSpace(self) -> bool: ...
    @worldSpace.setter
    def worldSpace(self, value: bool) -> None: ...
    @property
    def writable(self) -> bool: ...
    @writable.setter
    def writable(self, value: bool) -> None: ...

_MFnDataType: typing.TypeAlias = typing.Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26,
]  # fmt: off

class MFnData:
    kInvalid: typing.Literal[0]
    kNumeric: typing.Literal[1]
    kPlugin: typing.Literal[2]
    kPluginGeometry: typing.Literal[3]
    kString: typing.Literal[4]
    kMatrix: typing.Literal[5]
    kStringArray: typing.Literal[6]
    kDoubleArray: typing.Literal[7]
    kFloatArray: typing.Literal[8]
    kIntArray: typing.Literal[9]
    kPointArray: typing.Literal[10]
    kVectorArray: typing.Literal[11]
    kMatrixArray: typing.Literal[12]
    kComponentList: typing.Literal[13]
    kMesh: typing.Literal[14]
    kLattice: typing.Literal[15]
    kNurbsCurve: typing.Literal[16]
    kNurbsSurface: typing.Literal[17]
    kSphere: typing.Literal[18]
    kDynArrayAttrs: typing.Literal[19]
    kDynSweptGeometry: typing.Literal[20]
    kSubdSurface: typing.Literal[21]
    kNObject: typing.Literal[22]
    kNId: typing.Literal[23]
    kAny: typing.Literal[24]
    kFalloffFunction: typing.Literal[25]
    kLast: typing.Literal[26]

class MMatrix:
    kTolerance: float = 1e-10
    kIdentity: MMatrix

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MMatrix, /) -> None: ...
    @typing.overload
    def __init__(self, values: typing.Iterable[float], /) -> None: ...  # 16 floats
    @typing.overload
    def __init__(
        self,
        values: typing.Sequence[typing.Sequence[float]],
        /,
    ) -> None: ...  # 4 sequences of 4 float
    def __add__(self, value: MMatrix, /) -> MMatrix: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __getitem__(self, key: int, /) -> float: ...
    def __iadd__(self, value: MMatrix, /) -> MMatrix: ...
    def __imul__(self, value: MMatrix | float, /) -> MMatrix: ...
    def __isub__(self, value: MMatrix, /) -> MMatrix: ...
    def __len__(self) -> typing.Literal[16]: ...
    def __mul__(self, value: MMatrix | float, /) -> MMatrix: ...
    def __ne__(self, value: object, /) -> bool: ...
    def __rmul__(self, value: MMatrix | float, /) -> MMatrix: ...
    def __setitem__(self, key: int, value: float, /) -> None: ...
    def __sub__(self, value: MMatrix, /) -> MMatrix: ...
    def adjoint(self) -> MMatrix: ...
    def det3x3(self) -> float: ...
    def det4x4(self) -> float: ...
    def getElement(self, row: int, col: int, /) -> float: ...
    def homogenize(self) -> MMatrix: ...
    def inverse(self) -> MMatrix: ...
    def isEquivalent(
        self,
        other: MMatrix,
        /,
        tolerance: float = kTolerance,
    ) -> bool: ...
    def isSingular(self) -> bool: ...
    def setElement(self, row: int, col: int, value: float, /) -> typing.Self: ...
    def setToIdentity(self) -> typing.Self: ...
    def setToProduct(self, left: MMatrix, right: MMatrix, /) -> typing.Self: ...
    def transpose(self) -> MMatrix: ...

_MTransformationMatrixRotationOrder: typing.TypeAlias = typing.Literal[
    0, 1, 2, 3, 4, 5, 6, 7,
]  # fmt: skip

class MTransformationMatrix:
    kTolerance: float = 1e-10
    kIdentity: MTransformationMatrix
    kInvalid: typing.Literal[0]
    kXYZ: typing.Literal[1]
    kYZX: typing.Literal[2]
    kZXY: typing.Literal[3]
    kXZY: typing.Literal[4]
    kYXZ: typing.Literal[5]
    kZYX: typing.Literal[6]
    kLast: typing.Literal[7]

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MTransformationMatrix | MMatrix, /) -> None: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __ne__(self, value: object, /) -> bool: ...
    def asMatrix(self, interp: float = 1.0) -> MMatrix: ...
    def asMatrixInverse(self) -> MMatrix: ...
    def asRotateMatrix(self) -> MMatrix: ...
    def asScaleMatrix(self) -> MMatrix: ...
    def isEquivalent(
        self, other: MTransformationMatrix, /, tolerance: float = kTolerance
    ) -> bool: ...
    def reorderRotation(
        self, order: _MTransformationMatrixRotationOrder, /
    ) -> typing.Self: ...
    def rotateBy(
        self, rot: MQuaternion | MEulerRotation, space: _MSpaceSpace, /
    ) -> typing.Self: ...
    def rotateByComponents(
        self,
        seq: typing.Sequence[float],
        space: _MSpaceSpace,
        asQuaternion: bool = False,
        /,
    ) -> typing.Self: ...
    def rotatePivot(self, space: _MSpaceSpace, /) -> MPoint: ...
    def rotatePivotTranslation(self, space: _MSpaceSpace, /) -> MVector: ...
    @typing.overload
    def rotation(
        self, asQuaternion: typing.Literal[False] = False
    ) -> MEulerRotation: ...
    @typing.overload
    def rotation(self, asQuaternion: typing.Literal[True]) -> MQuaternion: ...
    @typing.overload
    def rotationComponents(
        self, asQuaternion: typing.Literal[False] = False
    ) -> list[int]: ...  # [x, y, z, order]
    @typing.overload
    def rotationComponents(
        self, asQuaternion: typing.Literal[True]
    ) -> list[int]: ...  # [x, y, z, w]
    def rotationOrder(self) -> _MTransformationMatrixRotationOrder: ...
    def rotationOrientation(self) -> MQuaternion: ...
    def scale(self, space: _MSpaceSpace, /) -> list[float]: ...  # [sx, sy, sz]
    def scaleBy(
        self,
        seq: typing.Sequence[float],  # [sx, sy, sz]
        space: _MSpaceSpace,
        /,
    ) -> typing.Self: ...
    def scalePivot(self, space: _MSpaceSpace, /) -> MPoint: ...
    def scalePivotTranslation(self, space: _MSpaceSpace, /) -> MVector: ...
    def setRotatePivot(
        self, trans: MPoint, space: _MSpaceSpace, balance: bool, /
    ) -> typing.Self: ...
    def setRotatePivotTranslation(
        self, trans: MVector, space: _MSpaceSpace, /
    ) -> typing.Self: ...
    def setRotation(self, rot: MQuaternion | MEulerRotation, /) -> typing.Self: ...
    @typing.overload
    def setRotationComponents(
        self,
        seq: typing.Sequence[float],  # [rx, ry, rz, order]
        asQuaternion: typing.Literal[False] = False,
        /,
    ) -> typing.Self: ...
    @typing.overload
    def setRotationComponents(
        self,
        seq: typing.Sequence[float],  # [qx, qy, qz, qw]
        /,
        asQuaternion: typing.Literal[True],
    ) -> typing.Self: ...
    def setRotationOrientation(self, rot: MQuaternion, /) -> typing.Self: ...
    def setScale(
        self,
        seq: typing.Sequence[float],  # [sx, sy, sz]
        space: _MSpaceSpace,
        /,
    ) -> typing.Self: ...
    def setScalePivot(
        self, pivot: MPoint, space: _MSpaceSpace, balance: bool, /
    ) -> typing.Self: ...
    def setScalePivotTranslation(
        self, trans: MVector, space: _MSpaceSpace, /
    ) -> typing.Self: ...
    def setShear(
        self,
        seq: typing.Sequence[float],  # [x, y, z]
        space: _MSpaceSpace,
        /,
    ) -> typing.Self: ...
    def setToRotationAxis(self, axis: MVector, rot: float, /) -> typing.Self: ...
    def setTranslation(self, trans: MVector, space: _MSpaceSpace, /) -> typing.Self: ...
    def shear(self, space: _MSpaceSpace, /) -> list[float]: ...
    def shearBy(
        self,
        seq: typing.Sequence[float],  # [x, y, z]
        space: _MSpaceSpace,
        /,
    ) -> typing.Self: ...
    def translateBy(self, vec: MVector, space: _MSpaceSpace, /) -> typing.Self: ...
    def translation(self, space: _MSpaceSpace, /) -> MVector: ...

_MSpaceSpace: typing.TypeAlias = typing.Literal[0, 1, 2, 3, 4, 5]

class MSpace:
    kInvalid: typing.Literal[0]
    kTransform: typing.Literal[1]
    kPreTransform: typing.Literal[2]
    kObject: typing.Literal[2]
    kPostTransform: typing.Literal[3]
    kWorld: typing.Literal[4]
    kLast: typing.Literal[5]

_MAngleUnit: typing.TypeAlias = typing.Literal[0, 1, 2, 3, 4, 5]

class MAngle:
    kInvalid: typing.Literal[0]
    kRadians: typing.Literal[1]
    kDegrees: typing.Literal[2]
    kAngMinutes: typing.Literal[3]
    kAngSeconds: typing.Literal[4]
    kLast: typing.Literal[5]

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MAngle) -> None: ...
    @typing.overload
    def __init__(self, value: float, unit: _MAngleUnit = kRadians) -> None: ...
    def asAngMinutes(self) -> float: ...
    def asAngSeconds(self) -> float: ...
    def asDegrees(self) -> float: ...
    def asRadians(self) -> float: ...
    def asUnits(self, unit: _MAngleUnit, /) -> float: ...
    @staticmethod
    def internalToUI(internalValue: float, /) -> float: ...
    @staticmethod
    def internalUnit() -> _MAngleUnit: ...
    @staticmethod
    def setUIUnit(newUnit: _MAngleUnit, /) -> None: ...
    @staticmethod
    def uiToInternal(uiValue: float, /) -> float: ...
    @staticmethod
    def uiUnit() -> _MAngleUnit: ...
    @property
    def unit(self) -> _MAngleUnit: ...
    @unit.setter
    def unit(self, value: _MAngleUnit) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, value: float) -> None: ...

_MDistanceUnit: typing.TypeAlias = typing.Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class MDistance:
    kInvalid: typing.Literal[0]
    kInches: typing.Literal[1]
    kFeet: typing.Literal[2]
    kYards: typing.Literal[3]
    kMiles: typing.Literal[4]
    kMillimeters: typing.Literal[5]
    kCentimeters: typing.Literal[6]
    kKilometers: typing.Literal[7]
    kMeters: typing.Literal[8]
    kLast: typing.Literal[9]

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MDistance) -> None: ...
    @typing.overload
    def __init__(self, value: float, unit: _MDistanceUnit = kCentimeters) -> None: ...
    def asFeet(self) -> float: ...
    def asInches(self) -> float: ...
    def asKilometers(self) -> float: ...
    def asMeters(self) -> float: ...
    def asMiles(self) -> float: ...
    def asMillimeters(self) -> float: ...
    def asUnits(self, unit: _MDistanceUnit, /) -> float: ...
    def asYards(self) -> float: ...
    @staticmethod
    def internalToUI(internalValue: float, /) -> float: ...
    @staticmethod
    def internalUnit() -> _MDistanceUnit: ...
    @staticmethod
    def setUIUnit(newUnit: _MDistanceUnit, /) -> None: ...
    @staticmethod
    def uiToInternal(uiValue: float, /) -> float: ...
    @staticmethod
    def uiUnit() -> _MDistanceUnit: ...
    @property
    def unit(self) -> _MDistanceUnit: ...
    @unit.setter
    def unit(self, value: _MDistanceUnit) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, value: float) -> None: ...

_MTimeUnit: typing.TypeAlias = typing.Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
]  # fmt: skip

class MTime:
    kInvalid: typing.Literal[0]
    kHours: typing.Literal[1]
    kMinutes: typing.Literal[2]
    kSeconds: typing.Literal[3]
    kMilliseconds: typing.Literal[4]
    kGames: typing.Literal[5]  # NOTE: deprecated
    k15FPS: typing.Literal[5]
    kFilm: typing.Literal[6]  # NOTE: deprecated
    k24FPS: typing.Literal[6]
    kPALFrame: typing.Literal[7]  # NOTE: deprecated
    k25FPS: typing.Literal[7]
    kNTSCFrame: typing.Literal[8]  # NOTE: deprecated
    k30FPS: typing.Literal[8]
    kShowScan: typing.Literal[9]  # NOTE: deprecated
    k48FPS: typing.Literal[9]
    kPALField: typing.Literal[10]  # NOTE: deprecated
    k50FPS: typing.Literal[10]
    kNTSCField: typing.Literal[11]  # NOTE: deprecated
    k60FPS: typing.Literal[11]
    k2FPS: typing.Literal[12]
    k3FPS: typing.Literal[13]
    k4FPS: typing.Literal[14]
    k5FPS: typing.Literal[15]
    k6FPS: typing.Literal[16]
    k8FPS: typing.Literal[17]
    k10FPS: typing.Literal[18]
    k12FPS: typing.Literal[19]
    k16FPS: typing.Literal[20]
    k20FPS: typing.Literal[21]
    k40FPS: typing.Literal[22]
    k75FPS: typing.Literal[23]
    k80FPS: typing.Literal[24]
    k100FPS: typing.Literal[25]
    k120FPS: typing.Literal[26]
    k125FPS: typing.Literal[27]
    k150FPS: typing.Literal[28]
    k200FPS: typing.Literal[29]
    k240FPS: typing.Literal[30]
    k250FPS: typing.Literal[31]
    k300FPS: typing.Literal[32]
    k375FPS: typing.Literal[33]
    k400FPS: typing.Literal[34]
    k500FPS: typing.Literal[35]
    k600FPS: typing.Literal[36]
    k750FPS: typing.Literal[37]
    k1200FPS: typing.Literal[38]
    k1500FPS: typing.Literal[39]
    k2000FPS: typing.Literal[40]
    k3000FPS: typing.Literal[41]
    k6000FPS: typing.Literal[42]
    k23_976FPS: typing.Literal[43]
    k29_97FPS: typing.Literal[44]
    k29_97DF: typing.Literal[45]
    k47_952FPS: typing.Literal[46]
    k59_94FPS: typing.Literal[47]
    k44100FPS: typing.Literal[48]
    k48000FPS: typing.Literal[49]
    k90FPS: typing.Literal[50]
    k119_88FPS: typing.Literal[51]
    kUserDef: typing.Literal[52]
    kLast: typing.Literal[53]

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: MTime) -> None: ...
    @typing.overload
    def __init__(self, value: float, unit: _MTimeUnit = k24FPS) -> None: ...
    def __add__(self, value: MTime, /) -> MTime: ...
    def __eq__(self, value: object, /) -> bool: ...
    def __qe__(self, value: MTime, /) -> bool: ...
    def __gt__(self, value: MTime, /) -> bool: ...
    def __iadd__(self, value: MTime, /) -> MTime: ...
    def __imul__(self, value: MTime, /) -> MTime: ...
    def __isub__(self, value: MTime, /) -> MTime: ...
    def __itruediv__(self, value: MTime, /) -> MTime: ...
    def __le__(self, value: MTime, /) -> bool: ...
    def __lt__(self, value: MTime, /) -> bool: ...
    def __mul__(self, value: MTime, /) -> MTime: ...
    def __ne__(self, value: object, /) -> bool: ...
    def __radd__(self, value: MTime, /) -> MTime: ...
    def __rmul__(self, value: MTime, /) -> MTime: ...
    def __rsub__(self, value: MTime, /) -> MTime: ...
    def __rtruediv__(self, value: MTime, /) -> MTime: ...
    def __sub__(self, value: MTime, /) -> MTime: ...
    def __truediv__(self, value: MTime, /) -> MTime: ...
    def asUnits(self, unit: _MTimeUnit, /) -> float: ...
    @staticmethod
    def setUIUnit(newUnit: _MTimeUnit, /) -> None: ...
    @staticmethod
    def ticksPerSecond() -> int: ...
    @staticmethod
    def uiUnit() -> _MTimeUnit: ...
    @property
    def unit(self) -> _MTimeUnit: ...
    @unit.setter
    def unit(self, value: _MTimeUnit) -> None: ...
    @property
    def value(self) -> float: ...
    @value.setter
    def value(self, value: float) -> None: ...
