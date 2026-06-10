---
name: pythonide-appui
description: Build or modify PythonIDE AppUI MiniApps with native navigation, forms, lists, search, tabs, toolbars, presentation, storage, and AppUI media bridges. Use when the user wants an interactive iOS MiniApp, settings screen, list/detail app, or native UI that may also need photos, camera, location, maps, video, or share.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE AppUI

Execution rulebook for native AppUI MiniApps. Pair with `pythonide-native` whenever the workflow touches iOS permissions, sensors, media capture, networking side effects, or secure storage.

## Read Before Coding

1. [appui quickstart](https://pythonide.xin/docs/pages/appui-quickstart/)
2. [AppUI module](https://pythonide.xin/docs/pages/appui-module/)
3. [UI patterns](https://pythonide.xin/docs/pages/miniapp-appui-ui-patterns/)
4. [AppUI schema](https://pythonide.xin/schemas/appui_api_schema.json) and [appui.pyi](https://pythonide.xin/stubs/appui.pyi) for signatures
5. [llms-full.txt](https://pythonide.xin/llms-full.txt) when unsure about exported symbols
6. Load `pythonide-native` before importing any `photos`, `location`, `permission`, `notification`, etc.

Chinese module pages on pythonide.xin are valid deep references for scenarios and examples.

## Workflow

1. Confirm AppUI is the right runtime (`pythonide` router). Do not use AppUI for widgets or frame-loop games.
2. Choose structure first: `Form`, `List`, `TabView`, `NavigationStack`, dashboard `ScrollView`.
3. Define module-level `appui.State` or `ReactiveState`.
4. Write named zero-argument callbacks; callbacks mutate state or call native APIs.
5. Keep `body()` pure: return a view tree only. No permissions, network, storage writes, notifications, timers started, or navigation side effects inside `body()`.
6. End with exactly one `appui.run(body, state=state, presentation=...)`.
7. For editable business data, load with `storage.get_json(..., default)` at startup and persist after mutations.

## Entry Pattern

```python
import appui

state = appui.State(count=0, status="Ready")


def increment():
    state.count += 1
    state.status = "Updated"


def body():
    return appui.NavigationStack(
        appui.Form([
            appui.Section("Counter", [
                appui.LabeledContent("Value", value=str(state.count)),
                appui.Button("+1", action=increment).button_style("bordered_prominent"),
            ], footer=state.status),
        ]).navigation_title("Counter")
    )


appui.run(body, state=state, presentation="fullscreen_with_close")
```

## Presentation

| Use case | `presentation` |
| --- | --- |
| Full app / tool with close affordance | `fullscreen_with_close` |
| Lightweight utility | `sheet` |
| Default when unsure for a real app | `fullscreen_with_close` |

## Structure Rules

- Settings, account, checkout, profile: `Form + Section`
- Dynamic rows: `List + ForEach` with stable `key`
- Master-detail: `NavigationStack + NavigationLink`
- Product areas: `TabView + Tab`, each tab owns a `NavigationStack`
- Search: native `.searchable(...)`; do not hand-roll search bars
- Toolbar actions in fullscreen apps; `fullscreen_with_close` already provides close
- Stable item IDs; mutate by id, never by filtered index
- Do not nest `List` inside `ScrollView`, `Section`, or another scrolling container

## Layout And Styling

- Target iPhone width ~390 pt; avoid fixed widths above 360 pt
- Padding usually 8–20 pt
- Use semantic system colors: `systemBackground`, `label`, `secondaryLabel`, `systemBlue`, etc.
- Do not hard-code hex/RGB unless the API requires it
- Ordinary rows/settings/todos should stay `List`/`Form` native-first; reserve custom dashboard layouts for true dashboard/media surfaces

## Native Integration

**Also load `pythonide-native` for any capability below.**

### Hard Rules

- `nativeCallsStayOutOfAppUIBody`: permission prompts, GPS, capture, notifications, and network side effects belong in named callbacks, `.refreshable`, or `.task` — never in `body()`
- Prefer AppUI bridge components before imperative modules when the control is inline in the UI
- AppUI embedded video: `PlayerController` + `VideoPlayer`; do not use `import avplayer` unless the user explicitly wants script-level playback
- Secrets → `keychain`; small settings → `storage`; queryable records → `database`

### AppUI Bridge Components

<!-- BEGIN GENERATED: appui-bridge-table -->
| Bridge | AppUI component | Related modules | Doc |
| --- | --- | --- | --- |
| `camera_picker` | `appui.CameraPicker` | `photos` | [camera-module](https://pythonide.xin/docs/pages/camera-module/#appui-camera-picker) |
| `file_importer` | `appui.FileImporter` | - | [file-picker-module](https://pythonide.xin/docs/pages/file-picker-module/#file-importer) |
| `map_view` | `appui.MapView` | `location`, `permission` | [location-module](https://pythonide.xin/docs/pages/location-module/#map-view) |
| `photo_picker` | `appui.PhotoPicker` | `photos` | [photos-module](https://pythonide.xin/docs/pages/photos-module/#appui-photo-picker) |
| `player_controller` | `appui.PlayerController` | `avplayer` | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/#player-controller) |
| `share_link` | `appui.ShareLink` | - | [share-module](https://pythonide.xin/docs/pages/share-module/#share-link) |
| `video_player` | `appui.VideoPlayer` | `avplayer` | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/#video-player) |
| `web_view` | `appui.WebView` | - | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/#webview) |
<!-- END GENERATED: appui-bridge-table -->

### Bridge Vs Module

| Need | Prefer |
| --- | --- |
| Inline photo pick in a form | `appui.PhotoPicker` |
| Inline camera capture button | `appui.CameraPicker` |
| Map preview in a screen | `appui.MapView` + `pythonide-native` for `location` callbacks |
| Share a file or text | `appui.ShareLink` |
| Batch asset processing, save to library, background fetch | `import photos` in callback |
| GPS updates, geocoding, heading | `import location` in callback |
| Local notifications | `import notification` in callback |

## Callbacks And Runtime

- Prefer named zero-argument callbacks
- Wrong: `Button(action=open(item))` or `row.on_tap(save(i))` — runs during view construction
- Row callbacks should capture stable item IDs
- Timers at module scope with `action=` at construction; never `Timer(action=None)` then assign later
- High-frequency sensors, camera streams, waveforms → consider Aurora realtime docs; do not rebuild the whole tree every frame in a tight loop

## Hard Stops

- No HTML/WebView unless the user explicitly needs web content
- No `lambda` callbacks in deliverable code
- No `children=` for `VStack`/`HStack`; pass child lists positionally
- No `NavigationStack([...])`; one root view only
- No `ScrollView(VStack(...))` for ordinary lists → use `List(ForEach(...))`
- No `Image(...).on_tap(...)` as a button → use `Button`
- No guessed SwiftUI-only APIs; verify against schema/stubs
- No tkinter, PyQt, Flask, Streamlit, or browser frameworks

## Common Mistakes

| Symptom | Fix |
| --- | --- |
| Dead button | Named zero-arg callback instead of eager invocation |
| Wrong row after search/filter | Stable ids + `ForEach(..., key=...)` |
| Permission dialog on launch | Move native call into button callback |
| Blank preview | Ensure `body()` returns a View and `appui.run(...)` is present |
| Shared search across tabs | Separate per-tab query state |

## Examples

- `examples/counter/` — minimal `Form` + persistence-ready structure
- `examples/photo_notes/` — AppUI shell + `PhotoPicker` + `storage`

## Validation

Done means: runnable AppUI code, documented APIs only, `appui.run(...)` present, named callbacks for side effects, and honest reporting if editor-side preview cannot be executed.
