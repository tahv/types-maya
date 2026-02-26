# Changelog

Versions follow [Semantic Versioning](https://semver.org) (`<major>.<minor>.<patch>`)
and the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## Unreleased

- Add `maya.cmds` unannotated.
- Add `maya.api.OpenMaya.M*Array` classes.
- Add `maya.api.OpenMaya.MCallbackId`.
- Add `maya.api.OpenMaya.MMessage`.
- Add `maya.api.OpenMaya.MCacheSchema`.
- Add `maya.api.OpenMaya.MBoundingBox`.
- Add `maya.api.OpenMaya.MAttributeSpec`.
- Add `maya.api.OpenMaya.MAttributePattern`.
- Add `maya.api.OpenMaya.MAttributeIndex`.
- Add `maya.api.OpenMaya.MArrayDataHandle`.
- Add `maya.api.OpenMaya.MArrayDataBuilder`.
- Add `maya.api.OpenMaya.MSyntax`.
- Add `Incomplete` to all missing `maya.api` classes.
- Add `Annotated` metadata to some properties.

## [0.2.0](https://github.com/tahv/types-maya/releases/tag/0.2.0) - 2025-09-26

- Supports Python >= 3.7
- Conform to [PEP 639](https://peps.python.org/pep-0639/)
- Fix `MFnDependencyNote.findPlug` returns a `MPlug`, instead of a `MObject`.
- Add `MQuaternion`, `MVector`, `MColor`, `MArgParser`, `MArgDatabase`, `MArgList`,
  `MDagPath`, `MFnDagNode` and `MSelectionList`.

## [0.1.1](https://github.com/tahv/types-maya/releases/tag/0.1.1) - 2025-02-25

- Add `maya.api.OpenMaya.MDagModifier`.
- Add incomplete `maya.OpenMaya*` modules.

## [0.1.0](https://github.com/tahv/types-maya/releases/tag/0.1.0) - 2025-02-23

- Initial release.
