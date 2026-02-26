from typing import Any, Callable

def eval(string: str, /) -> Any: ...
def createMelWrapper(
    fn: Callable[..., Any],
    types: list[str] = [],
    retType: str = "void",
    ignoreDefaultArgs: bool = True,
    returnCmd: bool = False,
    outDir: str | None = None,
) -> str: ...
