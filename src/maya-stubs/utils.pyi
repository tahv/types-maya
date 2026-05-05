from typing import Any, Callable, TypeVar

from typing_extensions import ParamSpec, overload

_P = ParamSpec("_P")
_R = TypeVar("_R")

def processIdleEvents() -> None: ...
@overload
def executeInMainThreadWithResult(script: str, /) -> Any: ...
@overload
def executeInMainThreadWithResult(
    fn: Callable[_P, _R], /, *args: _P.args, **kwargs: _P.kwargs
) -> _R: ...
@overload
def executeDeferred(script: str, /) -> None: ...
@overload
def executeDeferred(
    fn: Callable[_P, Any], /, *args: _P.args, **kwargs: _P.kwargs
) -> None: ...
