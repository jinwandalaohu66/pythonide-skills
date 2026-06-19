# PythonIDE Native References

Machine-readable contracts and the full schema-backed routing table for `pythonide-native`.

## Canonical URLs

- [iOS native index](https://pythonide.xin/docs/pages/ios-native/)
- [Native capabilities schema](https://pythonide.xin/schemas/native_capabilities_schema.json)
- [llms-full.txt](https://pythonide.xin/llms-full.txt)
- [miniapp native capabilities](https://pythonide.xin/docs/pages/miniapp-native-capabilities/)

## Persistence Boundary

- Use `database` for queryable records, caches, favorites, history, playlists, and SQL transactions.
- Do not import CPython `sqlite3` directly in MiniApps; `database` is the supported host-backed SQLite bridge.
- Keep small non-secret preferences in `storage`, and credentials in `keychain`.

## Music Playback Preloading

- `music_player.set_queue(..., preload_count=N)`, `music_player.prefetch_next(N)`, and `music_player.prepare(song)` only work with songs that already contain a real audio `url`.
- Resolve provider IDs, search-result IDs, signed URLs, or aggregation-service records in the MiniApp/data layer first, cache the playable URL with an expiry, then hand the resolved song to `music_player`.
- Use `music_player.preload_state()` to inspect prepared items when next-track playback still feels slow.

## Entry Routing

Route by schema entry kind before importing.

<!-- BEGIN GENERATED: native-entry-routing -->
| Kind | Key | Import / component | Doc | Notes |
| --- | --- | --- | --- | --- |
| `module` | `alarm` | `import alarm` | [alarm-module](https://pythonide.xin/docs/pages/alarm-module/) | `api` |
| `module` | `assistant` | `import assistant` | [assistant-module](https://pythonide.xin/docs/pages/assistant-module/) | `api` |
| `module` | `audio_recorder` | `import audio_recorder` | [audio-recorder-module](https://pythonide.xin/docs/pages/audio-recorder-module/) | `api` |
| `module` | `audio_session` | `import audio_session` | [audio-session-module](https://pythonide.xin/docs/pages/audio-session-module/) | `api` |
| `module` | `avplayer` | `import avplayer` | [avplayer-module](https://pythonide.xin/docs/pages/avplayer-module/) | `api` |
| `module` | `background` | `import background` | [background-module](https://pythonide.xin/docs/pages/background-module/) | `api` |
| `module` | `background_download` | `import background_download` | [background-download-module](https://pythonide.xin/docs/pages/background-download-module/) | `api` |
| `module` | `biometric` | `import biometric` | [biometric-module](https://pythonide.xin/docs/pages/biometric-module/) | `blocking_sheet` |
| `module` | `ble_peripheral` | `import ble_peripheral` | [ble-peripheral-module](https://pythonide.xin/docs/pages/ble-peripheral-module/) | `api` |
| `module` | `bluetooth` | `import bluetooth` | [bluetooth-module](https://pythonide.xin/docs/pages/bluetooth-module/) | `api` |
| `module` | `c_extensions` | `import c_extensions` | [c-extensions-module](https://pythonide.xin/docs/pages/c-extensions-module/) | `reference` |
| `module` | `calendar_events` | `import calendar_events` | [calendar-events-module](https://pythonide.xin/docs/pages/calendar-events-module/) | `system_picker` |
| `module` | `clipboard` | `import clipboard` | [clipboard-module](https://pythonide.xin/docs/pages/clipboard-module/) | `api` |
| `module` | `console` | `import console` | [console-module](https://pythonide.xin/docs/pages/console-module/) | `blocking_sheet` |
| `module` | `contacts` | `import contacts` | [contacts-module](https://pythonide.xin/docs/pages/contacts-module/) | `system_picker` |
| `module` | `coreml` | `import coreml` | [coreml-module](https://pythonide.xin/docs/pages/coreml-module/) | `api` |
| `module` | `database` | `import database` | [database-module](https://pythonide.xin/docs/pages/database-module/) | `api` |
| `module` | `device` | `import device` | [device-module](https://pythonide.xin/docs/pages/device-module/) | `api` |
| `module` | `dialogs` | `import dialogs` | [dialogs-module](https://pythonide.xin/docs/pages/dialogs-module/) | `blocking_sheet` |
| `module` | `font_picker` | `import font_picker` | [font-picker-module](https://pythonide.xin/docs/pages/font-picker-module/) | `blocking_sheet` |
| `module` | `foundation_models` | `import foundation_models` | [foundation-models-module](https://pythonide.xin/docs/pages/foundation-models-module/) | `api` |
| `module` | `haptics` | `import haptics` | [haptics-module](https://pythonide.xin/docs/pages/haptics-module/) | `api` |
| `module` | `health` | `import health` | [health-module](https://pythonide.xin/docs/pages/health-module/) | `api` |
| `module` | `http_server` | `import http_server` | [http-server-module](https://pythonide.xin/docs/pages/http-server-module/) | `api` |
| `module` | `keyboard` | `import keyboard` | [keyboard-module](https://pythonide.xin/docs/pages/keyboard-module/) | `api` |
| `module` | `keychain` | `import keychain` | [keychain-module](https://pythonide.xin/docs/pages/keychain-module/) | `api` |
| `module` | `live_activity` | `import live_activity` | [live-activity-module](https://pythonide.xin/docs/pages/live-activity-module/) | `api` |
| `module` | `location` | `import location` | [location-module](https://pythonide.xin/docs/pages/location-module/) | `api` |
| `module` | `mail` | `import mail` | [mail-module](https://pythonide.xin/docs/pages/mail-module/) | `compose_sheet` |
| `module` | `media_composer` | `import media_composer` | [media-composer-module](https://pythonide.xin/docs/pages/media-composer-module/) | `api` |
| `module` | `message` | `import message` | [message-module](https://pythonide.xin/docs/pages/message-module/) | `compose_sheet` |
| `module` | `motion` | `import motion` | [motion-module](https://pythonide.xin/docs/pages/motion-module/) | `api` |
| `module` | `music` | `import music` | [music-module](https://pythonide.xin/docs/pages/music-module/) | `api` |
| `module` | `music_player` | `import music_player` | [music-player-module](https://pythonide.xin/docs/pages/music-player-module/) | `api` |
| `module` | `network` | `import network` | [network-module](https://pythonide.xin/docs/pages/network-module/) | `api` |
| `module` | `nfc` | `import nfc` | [nfc-module](https://pythonide.xin/docs/pages/nfc-module/) | `system_picker` |
| `module` | `notification` | `import notification` | [notification-module](https://pythonide.xin/docs/pages/notification-module/) | `api` |
| `module` | `now_playing` | `import now_playing` | [now-playing-module](https://pythonide.xin/docs/pages/now-playing-module/) | `api` |
| `module` | `objc_util` | `import objc_util` | [objc-util-module](https://pythonide.xin/docs/pages/objc-util-module/) | `api` |
| `module` | `pdf` | `import pdf` | [pdf-module](https://pythonide.xin/docs/pages/pdf-module/) | `api` |
| `module` | `permission` | `import permission` | [permission-module](https://pythonide.xin/docs/pages/permission-module/) | `api` |
| `module` | `photos` | `import photos` | [photos-module](https://pythonide.xin/docs/pages/photos-module/) | `api` |
| `module` | `qrcode` | `import qrcode` | [qrcode-module](https://pythonide.xin/docs/pages/qrcode-module/) | `api` |
| `module` | `shazam` | `import shazam` | [shazam-module](https://pythonide.xin/docs/pages/shazam-module/) | `api` |
| `module` | `shortcuts` | `import shortcuts` | [shortcuts-module](https://pythonide.xin/docs/pages/shortcuts-module/) | `api` |
| `module` | `sound` | `import sound` | [sound-module](https://pythonide.xin/docs/pages/sound-module/) | `api` |
| `module` | `speech` | `import speech` | [speech-module](https://pythonide.xin/docs/pages/speech-module/) | `api` |
| `module` | `speech_recognition` | `import speech_recognition` | [speech-recognition-module](https://pythonide.xin/docs/pages/speech-recognition-module/) | `api` |
| `module` | `ssh` | `import ssh` | [ssh-module](https://pythonide.xin/docs/pages/ssh-module/) | `api` |
| `module` | `storage` | `import storage` | [storage-module](https://pythonide.xin/docs/pages/storage-module/) | `api` |
| `module` | `storekit` | `import storekit` | [storekit-module](https://pythonide.xin/docs/pages/storekit-module/) | `api` |
| `module` | `translation` | `import translation` | [translation-module](https://pythonide.xin/docs/pages/translation-module/) | `api` |
| `module` | `video_recorder` | `import video_recorder` | [video-recorder-module](https://pythonide.xin/docs/pages/video-recorder-module/) | `api` |
| `module` | `vision` | `import vision` | [vision-module](https://pythonide.xin/docs/pages/vision-module/) | `api` |
| `module` | `vision_helper` | `import vision_helper` | [vision-helper-module](https://pythonide.xin/docs/pages/vision-helper-module/) | `api` |
| `module` | `weather` | `import weather` | [weather-module](https://pythonide.xin/docs/pages/weather-module/) | `api` |
| `module` | `websocket` | `import websocket` | [websocket-module](https://pythonide.xin/docs/pages/websocket-module/) | `api` |
| `appui_bridge` | `camera_picker` | `appui.CameraPicker` | [camera-module](https://pythonide.xin/docs/pages/camera-module/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `file_importer` | `appui.FileImporter` | [file-picker-module](https://pythonide.xin/docs/pages/file-picker-module/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `map_view` | `appui.MapView` | [location-module](https://pythonide.xin/docs/pages/location-module/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `photo_picker` | `appui.PhotoPicker` | [photos-module](https://pythonide.xin/docs/pages/photos-module/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `player_controller` | `appui.PlayerController` | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `share_link` | `appui.ShareLink` | [share-module](https://pythonide.xin/docs/pages/share-module/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `video_player` | `appui.VideoPlayer` | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/) | AppUI-first; see `pythonide-appui` |
| `appui_bridge` | `web_view` | `appui.WebView` | [appui-ref-media](https://pythonide.xin/docs/pages/appui-ref-media/) | AppUI-first; see `pythonide-appui` |
| `topic` | `camera` | photos | [camera-module](https://pythonide.xin/docs/pages/camera-module/) | Camera capture via photos.capture_image or AppUI CameraPicker. |
| `topic` | `file_picker` | appui | [file-picker-module](https://pythonide.xin/docs/pages/file-picker-module/) | File selection has no import module; use AppUI FileImporter. |
| `topic` | `share` | appui | [share-module](https://pythonide.xin/docs/pages/share-module/) | System share sheet has no import module; use AppUI ShareLink. |
<!-- END GENERATED: native-entry-routing -->
