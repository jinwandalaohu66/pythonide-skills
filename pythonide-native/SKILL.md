---
name: pythonide-native
description: Choose and implement PythonIDE iOS native modules for permissions, device state, sensors, storage, keychain, photos, camera, location, notifications, networking, Bluetooth, health, speech, media, and system actions. Use with pythonide-appui when a MiniApp needs native capability behind user-triggered callbacks.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE Native

Discovery and implementation rules for iOS native Python modules. This skill does not replace `pythonide-appui`; pair both when building MiniApps that call system capabilities.

## Read Before Coding

1. [iOS native index](https://pythonide.xin/docs/pages/ios-native/)
2. [Native capabilities schema](https://pythonide.xin/schemas/native_capabilities_schema.json)
3. [llms-full.txt](https://pythonide.xin/llms-full.txt) native module table
4. Focused module page: `https://pythonide.xin/docs/pages/<module-id>/`
5. [references.md](references.md) in this skill for the full entry routing table
6. When the UI shell is AppUI, also load `pythonide-appui`

Chinese module docs are authoritative for scenarios; schema and stubs are authoritative for API names.

## Use When

- The task needs permissions, device facts, sensors, storage, secrets, user content, networking, peripherals, notifications, speech, audio/video, shortcuts, Live Activities, or Core ML
- You must choose the correct module before writing `import` statements
- An AppUI MiniApp needs callback-side native work beyond bridge components

## Do Not Use When

- The task is only AppUI layout, navigation, controls, or inline bridge components with no extra module logic
- The runtime is `widget`, `scene`, or plain stdlib Python with no iOS integration
- The app name mentions a capability but the code never calls it

## Required Flow

1. Route by schema entry kind: `module`, `appui_bridge`, `topic`, `reference`
2. Import only modules whose APIs are called
3. Check availability or authorization before sensitive operations
4. Request permission only from a named user-triggered callback
5. Handle denied, restricted, unavailable, cancelled, empty, offline, timeout, and error outcomes visibly
6. Persist small non-secret state with `storage`, queryable records with `database`, secrets with `keychain`
7. Keep native side effects out of AppUI `body()`

## AppUI Pairing

| UI need | Start here | Then |
| --- | --- | --- |
| Inline picker/camera/map/share/video | `pythonide-appui` bridge table | Add native module only for post-processing |
| Button-triggered GPS, notification, save-to-photos | `pythonide-appui` shell | `import location` / `notification` / `photos` in callback |
| Device status dashboard | `pythonide-appui` | `import device`, `permission`, `storage` |
| Script-only automation | this skill only | plain Python file |

## Permission Pattern

```python
import permission
import storage


def ensure_photos_access():
    status = permission.status("photos")
    if status.get("status") not in {"authorized", "limited"}:
        status = permission.request("photos")
    storage.set_json("native.photos_status", status)
    return status
```

## Module Categories

<!-- BEGIN GENERATED: native-module-categories -->
### Foundation & persistence

`clipboard`, `console`, `database`, `dialogs`, `keychain`, `permission`, `storage`

### Device & sensors

`biometric`, `device`, `haptics`, `health`, `location`, `motion`

### System & comms

`calendar_events`, `contacts`, `font_picker`, `live_activity`, `mail`, `message`, `notification`

### Media & vision

`audio_recorder`, `audio_session`, `avplayer`, `coreml`, `media_composer`, `music`, `music_player`, `now_playing`, `pdf`, `photos`, `qrcode`, `shazam`, `sound`, `speech`, `speech_recognition`, `video_recorder`, `vision`, `vision_helper`

### Connectivity & background

`background`, `background_download`, `ble_peripheral`, `bluetooth`, `http_server`, `network`, `nfc`, `ssh`, `weather`, `websocket`

### Automation & advanced

`alarm`, `assistant`, `c_extensions` (reference), `foundation_models`, `keyboard`, `objc_util`, `shortcuts`, `storekit`, `translation`
<!-- END GENERATED: native-module-categories -->

## High-Signal Routing

| User intent | Module / bridge |
| --- | --- |
| Pick or save photos | `photos`; inline UI → `appui.PhotoPicker` |
| Take photo in AppUI form | `appui.CameraPicker`; processing → `photos` |
| Current location / map | `location`; inline map → `appui.MapView` |
| Local notification | `notification` (permission key is `notifications`) |
| Network fetch | `network` |
| Live socket | `websocket` |
| Clipboard | `clipboard` |
| Share sheet in AppUI | `appui.ShareLink` (topic `share` has no import) |
| File picker in AppUI | `appui.FileImporter` (topic `file_picker` has no import) |
| Embedded AppUI video | `appui.PlayerController` + `appui.VideoPlayer` |
| Custom music queue player | `music_player` |
| Script-only media playback | `avplayer` |
| On-device ML | `coreml`, `vision`, `vision_helper`, `foundation_models` |

Full key-by-key routing: [references.md](references.md).

## Hard Stops

- Do not guess APIs from UIKit, Swift, browser, or Pythonista memory
- Do not use `permission.status("notification")`; use `notifications`
- Do not prompt permissions, scan hardware, or schedule notifications at import time or from AppUI `body()`
- Do not store secrets in `storage`
- Do not use `avplayer` for AppUI embedded video controls
- Do not hide denied, cancelled, or offline outcomes
- Do not import `c_extensions` as runtime code; it is reference-only

## Persistence Rules

| Data | Use |
| --- | --- |
| User settings, small JSON state | `storage` |
| Queryable records / caches | `database` |
| Tokens, passwords, API keys | `keychain` |

## Repair Hints

- Inert native button → move call into named callback; surface result in `State` or output
- Wrong module → re-check [references.md](references.md) and schema `kind`
- Offline failures → `network.is_connected`, `network.connection_type` before expensive work
- Missing authorization → module `authorization_status` / `request_access`, else `permission.status` / `permission.request`

## Examples

- `examples/device_snapshot/` — `device` + `permission` + `storage` with AppUI shell in comments
