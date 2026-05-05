# types-maya

[![Source](https://img.shields.io/badge/source-%23fc6d25?logo=gitlab&logoColor=white)](https://gitlab.com/tahv/types-maya)
[![PyPI](https://img.shields.io/pypi/v/types-maya?logo=python&logoColor=white)](https://pypi.org/project/types-maya)
[![Typed](https://img.shields.io/pypi/types/types-maya?logo=python&logoColor=white)](https://pypi.org/project/types-maya/)

External type annotations for Autodesk Maya Python API.

Provide stubs for language servers such a
[Pyright](https://github.com/microsoft/pyright)
or [ty](https://github.com/astral-sh/ty).

## Project Information

- [**PyPI**](https://pypi.org/project/types-maya)
- [**Source Code**](https://gitlab.com/tahv/types-maya)
- [**Changelog**](https://gitlab.com/tahv/types-maya/-/blob/main/CHANGELOG.md)
- [**GitHub Mirror**](https://github.com/tahv/types-maya)

## Installation

Install with [pip](https://pip.pypa.io/en/stable/topics/vcs-support/#git)
or [uv pip](https://docs.astral.sh/uv/pip/packages/#installing-a-package).

```bash
pip install types-maya
```

## Stubs status

- `maya.api.*`: maintained manually
  and will likely remain incomplete for some time.
  Stubs are written from the
  [Maya 2025 Reference](https://help.autodesk.com/view/MAYADEV/2025/ENU/).
- `maya.cmds`: generated from Maya Commands documentation
  using [cmdsgen](https://gitlab.com/tahv/cmdsgen).
- `maya.OpenMaya*`: not something I'm focusing on, but contributions are welcome.

| Import name               | Status               |
|---------------------------|----------------------|
| `maya.api.OpenMaya`       | 🟠 Incomplete (~45%) |
| `maya.api.OpenMayaAnim`   | 🟠 Unannotated       |
| `maya.api.OpenMayaRender` | 🟠 Incomplete (~12%) |
| `maya.api.OpenMayaUI`     | 🟠 Unannotated       |
| `maya.cmds`               | 🟢 Complete          |
| `maya.mel`                | 🟢 Complete          |
| `maya.standalone`         | 🟢 Complete          |
| `maya.OpenMaya`           | 🔴 Not Covered       |
| `maya.OpenMayaAnim`       | 🔴 Not Covered       |
| `maya.OpenMayaFX`         | 🔴 Not Covered       |
| `maya.OpenMayaMPx`        | 🔴 Not Covered       |
| `maya.OpenMayaRender`     | 🔴 Not Covered       |
| `maya.OpenMayaUI`         | 🔴 Not Covered       |

## Notes

[`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated)
is used to add context to some annotations. Some examples:

A sequence of 16 floats.

```python
Annotated[Sequence[float], "[16]"]
```

A sequence of 4 sequences of 4 floats.

```python
Annotated[Sequence[Sequence[float]], "[4[4]]"]
```

A sequence of 1 to 6 floats.

```python
Annotated[Sequence[MArgType], "[1..6]"],
```

A list of 4 int, the `x`, `y`, `x` and `w` axis.

```python
Annotated[list[int], "[x, y, z, w]"]
```

Deprecated property.

```python
Annotated[Literal[5], "deprecated"]
```

## Contributing

Contributions of any kind are welcome.
Please [open an issue](https://gitlab.com/tahv/types-maya/-/issues)
or open a [merge request](https://gitlab.com/tahv/types-maya/-/merge_requests).
