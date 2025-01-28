import typing

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
