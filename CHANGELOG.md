# Changelog

Versions follow [Semantic Versioning](https://semver.org) (`<major>.<minor>.<patch>`)
and the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## Unreleased

- Add `maya.api.OpenMaya.MConditionMessage`
- Add `maya.api.OpenMaya.MContainerMessage`
- Add `maya.api.OpenMaya.MDAGDrawOverrideInfo`
- Add `maya.api.OpenMaya.MDagMessage`
- Add `maya.api.OpenMaya.MDataBlock`
- Add `maya.api.OpenMaya.MDataHandle`
- Add `maya.api.OpenMaya.MDGMessage`
- Add `maya.api.OpenMayaRender.MClearOperation`
- Add `maya.api.OpenMayaRender.MPresentTarget`
- Add `maya.api.OpenMayaRender.MRenderer`
- Add `maya.api.OpenMayaRender.MRenderOperation`
- Add `maya.api.OpenMayaRender.MRenderOverride`
- Add `maya.api.OpenMayaRender.MSceneRender`
- Add `maya.api.OpenMayaRender.MFrameContext`
- Add `maya.api.OpenMayaRender.MUIDrawManager`
- Add `maya.api.OpenMayaRender.MBlendState`
- Add `maya.api.OpenMayaRender.MSamplerState`

## [0.3.0](https://github.com/tahv/types-maya/releases/tag/0.3.0) - 2026-02-27

- Add `maya.api.OpenMaya.MMessage`.
- Add `maya.api.OpenMaya.MCallbackId`.
- Add `maya.api.OpenMaya.MCameraMessage`.
- Add `maya.api.OpenMaya.MCommandMessage`.
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
