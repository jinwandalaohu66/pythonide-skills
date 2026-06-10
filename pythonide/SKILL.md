---
name: pythonide
description: Route PythonIDE tasks to the correct runtime and companion skill (AppUI MiniApp, widget, scene, native modules, automation). Use when the user asks to build, fix, or choose a PythonIDE app, script, widget, game, or iOS capability workflow.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE Router

Thin routing skill for external coding agents. Load a focused companion skill before generating code.

## Read First

1. [AI one-page guide](https://pythonide.xin/docs/ai/)
2. [llms-full.txt](https://pythonide.xin/llms-full.txt) for hard rules and public API surfaces
3. [Native capabilities schema](https://pythonide.xin/schemas/native_capabilities_schema.json) before any `import` of iOS modules
4. Focused module page on [pythonide.xin/docs](https://pythonide.xin/docs/) when examples or Chinese scenario text help

Do not invent APIs from SwiftUI, UIKit, React, browser, tkinter, PyQt, Flask, or Streamlit memory.

## Runtime Routing

<!-- BEGIN GENERATED: runtime-routing-table -->
| Runtime | Import | Skill | Doc |
| --- | --- | --- | --- |
| AppUI MiniApp | `import appui` | `pythonide-appui` | [appui-module](https://pythonide.xin/docs/pages/appui-module/) |
| Home Screen widget | `import widget` | `pythonide-widget` | [widget-module](https://pythonide.xin/docs/pages/widget-module/) |
| 2D game / scene | `import scene` | `pythonide-scene` | [scene-module](https://pythonide.xin/docs/pages/scene-module/) |
| Legacy UI script | `import ui` | `pythonide-automation` | [ui-module](https://pythonide.xin/docs/pages/ui-module/) |
| Turtle graphics | `import turtle` | `pythonide-scene` | [turtle-module](https://pythonide.xin/docs/pages/turtle-module/) |
| Plain Python / shortcuts | stdlib + native modules | `pythonide-automation` / `pythonide-native` | [ios-native](https://pythonide.xin/docs/pages/ios-native/) |
<!-- END GENERATED: runtime-routing-table -->

## Companion Skills

| Skill | Load when |
| --- | --- |
| `pythonide-appui` | Forms, lists, tabs, navigation, dashboards, AppUI media controls |
| `pythonide-native` | Permissions, sensors, photos, location, notifications, networking, keychain, device APIs |
| `pythonide-widget` | WidgetKit home screen widgets |
| `pythonide-scene` | Games, sprites, physics, frame loops, turtle |
| `pythonide-automation` | Shortcuts, keyboard snippets, legacy `ui`, batch scripts |

## Decision Rules

1. **Default interactive app** → `pythonide-appui`
2. **Home Screen widget** → `pythonide-widget` (never AppUI)
3. **Continuous animation / game loop** → `pythonide-scene` (never AppUI navigation)
4. **Needs iOS capability behind UI** → `pythonide-appui` + `pythonide-native`
5. **Only scripts / Shortcut / editor helper** → `pythonide-automation` or `pythonide-native`
6. **Pythonista-compatible imperative UI** → `pythonide-automation` (`ui` runtime)

## AppUI + Native Pairing

When a MiniApp needs camera, photos, location, files, share, notifications, storage, or device state:

1. Build the shell with `pythonide-appui`
2. Load `pythonide-native` for module choice, permissions, and callback-side effects
3. Prefer AppUI bridge components (`PhotoPicker`, `CameraPicker`, `MapView`, `FileImporter`, `ShareLink`, `VideoPlayer`) before imperative modules when the UI is inline
4. Never call native APIs from AppUI `body()`

## Schema Entry Kinds

Route from [native capabilities schema](https://pythonide.xin/schemas/native_capabilities_schema.json):

| Kind | Meaning | Action |
| --- | --- | --- |
| `module` | `import <name>` | Read module doc + `pythonide-native` |
| `appui_bridge` | `appui.<Component>` | Read `pythonide-appui` bridge table |
| `topic` | No direct import | Follow topic doc; often AppUI-first |
| `reference` | Docs only | Do not import |

## Output Contract

- Deliver runnable Python for PythonIDE unless the user asks for explanation only
- One primary runtime per artifact
- JSON-safe data in `storage` / `database`; secrets only in `keychain`
- Say when hardware, permission, or preview validation cannot be proven from editor context
