---
name: pythonide-automation
description: Build PythonIDE automation scripts with shortcuts, keyboard snippets, legacy ui views, plain Python batch tools, and extension-facing workflows. Use when the user wants Shortcut handoff, editor keyboard helpers, Pythonista-style ui, or non-AppUI scripts without a full MiniApp shell.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE Automation

Rules for scripts and automation surfaces that are not AppUI MiniApps or widgets.

## Read Before Coding

1. [Shortcuts guide](https://pythonide.xin/docs/pages/shortcuts-guide/)
2. [shortcuts module](https://pythonide.xin/docs/pages/shortcuts-module/)
3. [keyboard module](https://pythonide.xin/docs/pages/keyboard-module/)
4. [ui module](https://pythonide.xin/docs/pages/ui-module/) for legacy imperative UI
5. [Automation extension index](https://pythonide.xin/docs/pages/automation-extension/)
6. Load `pythonide-native` when the script imports iOS modules

## Use When

- Run an existing iOS Shortcut by name
- Open URL handoff or app settings through `shortcuts`
- Add editor keyboard buttons/snippets
- Build Pythonista-compatible `ui` scripts
- Plain Python utilities with optional native module calls
- JS/extension workflows referenced in [js-api](https://pythonide.xin/docs/pages/js-api/)

## Do Not Use When

- The user wants a native MiniApp with navigation and forms → `pythonide-appui`
- The user wants a Home Screen widget → `pythonide-widget`
- The user wants a game or frame loop → `pythonide-scene`
- PythonIDE can solve the task with only stdlib and no iOS integration

## Shortcuts Pattern

```python
import shortcuts


def open_daily_log():
    return shortcuts.run_shortcut("Daily Log")
```

### Shortcuts Rules

- Use only Shortcut names the user provided
- Call `run_shortcut`, `open_url`, or `open_settings` from user-triggered actions
- Treat `False` or empty results as failure; do not claim success without evidence
- Do not invent installed Shortcuts
- Do not launch shortcuts at import time or from AppUI `body()`

## Keyboard Pattern

Use [keyboard module](https://pythonide.xin/docs/pages/keyboard-module/) for editor buttons, groups, snippets, and cursor insertion. Keep handlers short and user-triggered.

## Legacy `ui` Pattern

```python
import ui


class DemoView(ui.View):
    def __init__(self):
        super().__init__()
        self.frame = (0, 0, 320, 240)
        button = ui.Button(title="Tap")
        button.frame = (20, 20, 120, 40)
        button.action = self.tapped
        self.add_subview(button)

    def tapped(self, sender):
        ui.hud_alert("Tapped")


DemoView().present("sheet")
```

### `ui` Rules

- Frame-based UIKit-style hierarchy with explicit frames
- Assign callable handlers; do not invoke callbacks while building controls
- Present once with `.present("sheet")` or `.present("fullscreen")`
- Do not mix `ui` and `appui` unless repairing an existing hybrid with explicit user consent
- Not for new MiniApps; prefer `pythonide-appui`

## Plain Python Scripts

- Use stdlib when sufficient
- Import native modules only when iOS integration is required; follow `pythonide-native`
- Print or file output is acceptable when the user does not want preview UI
- Do not wrap side-effect-only code in AppUI

## Hard Stops

- No AppUI navigation for Shortcut-only tasks unless the user asked for a launcher UI
- No guessed Swift App Intent names without source inspection
- No `objc_util` unless the user explicitly needs advanced runtime bridging
- `c_extensions` is reference-only; do not import as runtime code

## Runtime Choice

| Outcome | Runtime |
| --- | --- |
| Editor helper / Shortcut / batch script | this skill |
| Pythonista-style view | `ui` |
| Native iOS capability only | `pythonide-native` |
| Interactive product UI | `pythonide-appui` |

## Examples

- `examples/run_shortcut/` — named Shortcut launcher function
