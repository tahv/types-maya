# types-maya

External type annotations for Autodesk Maya Python API.

The main goal is to provide helper for [Pyright](https://github.com/microsoft/pyright)
language server to offer better autocompletion.

## Available stubs

These stubs are manually maintained and updated as needed for my projects,
which means they are currently far from complete.

| Import name               | Status         |
|---------------------------|----------------|
| `maya.api.OpenMaya`       | 🟠 Incomplete  |
| `maya.api.OpenMayaAnim`   | 🔴 Not Covered |
| `maya.api.OpenMayaRender` | 🔴 Not Covered |
| `maya.api.OpenMayaUI`     | 🔴 Not Covered |
| `maya.cmds`               | 🔴 Not Covered |
| `maya.mel`                | 🟢 Complete    |
| `maya.standalone`         | 🟢 Complete    |
| `maya.OpenMaya`           | 🔴 Not Covered |
| `maya.OpenMayaAnim`       | 🔴 Not Covered |
| `maya.OpenMayaFX`         | 🔴 Not Covered |
| `maya.OpenMayaMPx`        | 🔴 Not Covered |
| `maya.OpenMayaRender`     | 🔴 Not Covered |
| `maya.OpenMayaUI`         | 🔴 Not Covered |

## Installation

<!--
`types-maya` is current not available on PyPI.
Although the package [is listed on PyPI](https://pypi.org/project/types-maya/)
it is empty and only serves to reserve the name.
-->

Install from vcs with [pip](https://pip.pypa.io/en/stable/topics/vcs-support/#git)
or [uv pip](https://docs.astral.sh/uv/pip/packages/#installing-a-package).

```bash
pip install git+https://github.com/tahv/types-maya@main
```

## Contributing

Contributions of any kind are welcome.
Please open an issue or a send pull request.
