# types-maya

[![Typed](https://img.shields.io/pypi/types/types-maya?logo=python&logoColor=white)](https://pypi.org/project/types-maya/)
[![Version](https://img.shields.io/pypi/v/types-maya?logo=pypi&logoColor=white)](https://pypi.org/project/types-maya/)
[![License](https://img.shields.io/github/license/tahv/types-maya)](https://github.com/tahv/types-maya/blob/main/LICENSE)
[![CI Tests](https://img.shields.io/github/actions/workflow/status/tahv/types-maya/tests.yml?logo=github&logoColor=white&label=tests)](https://github.com/tahv/types-maya/actions/workflows/tests.yml)

External type annotations for Autodesk Maya Python API.

The goal is to provide stubs for [Pyright](https://github.com/microsoft/pyright)
or [ty](https://github.com/astral-sh/ty) language servers.

## Installation

Install with [pip](https://pip.pypa.io/en/stable/topics/vcs-support/#git)
or [uv pip](https://docs.astral.sh/uv/pip/packages/#installing-a-package).

```bash
pip install types-maya
```

## Available stubs

The stubs are maintained manually and will likely remain incomplete for a long time.
I update the stubs based on my needs and mostly use Maya Python API 2.0 (`maya.api`).

| Import name               | Status               |
|---------------------------|----------------------|
| `maya.api.OpenMaya`       | 🟠 Incomplete (~41%) |
| `maya.api.OpenMayaAnim`   | 🔴 Not Covered       |
| `maya.api.OpenMayaRender` | 🔴 Not Covered       |
| `maya.api.OpenMayaUI`     | 🔴 Not Covered       |
| `maya.cmds`               | 🟠 Unannotated       |
| `maya.mel`                | 🟢 Complete          |
| `maya.standalone`         | 🟢 Complete          |
| `maya.OpenMaya`           | 🔴 Not Covered       |
| `maya.OpenMayaAnim`       | 🔴 Not Covered       |
| `maya.OpenMayaFX`         | 🔴 Not Covered       |
| `maya.OpenMayaMPx`        | 🔴 Not Covered       |
| `maya.OpenMayaRender`     | 🔴 Not Covered       |
| `maya.OpenMayaUI`         | 🔴 Not Covered       |

The stubs are written from the
[Maya 2025 Reference](https://help.autodesk.com/view/MAYADEV/2025/ENU/).

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
Please open an issue or a submit pull request.
