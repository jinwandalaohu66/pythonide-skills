---
name: pythonide-widget
description: Create or repair PythonIDE iOS Home Screen widgets using widget.Widget(), widget.param, widget.state, charts, tables, canvas layouts, and family branching. Use when the user asks for a WidgetKit widget, desktop widget script, or widget preview — not an AppUI MiniApp.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE Widget

Execution rulebook for Python-first iOS Home Screen widgets.

## Read Before Coding

1. [Widget module](https://pythonide.xin/docs/pages/widget-module/)
2. [Widget schema](https://pythonide.xin/schemas/widget_api_schema.json) and [widget.pyi](https://pythonide.xin/stubs/widget.pyi)
3. [llms-full.txt](https://pythonide.xin/llms-full.txt) widget surface
4. Focused guides: [layout](https://pythonide.xin/docs/pages/widget-layout/), [parameters](https://pythonide.xin/docs/pages/widget-parameters/), [interaction](https://pythonide.xin/docs/pages/widget-interaction/), [timeline](https://pythonide.xin/docs/pages/widget-timeline/)

Do not use AppUI, SwiftUI, TSX, HTML, or undocumented widget helpers.

## Workflow

1. Confirm the user wants a **widget**, not an AppUI MiniApp (`pythonide` router).
2. Write one runnable Python file: `import widget`, one `widget.Widget(...)`, documented primitives, `w.render()`.
3. Default target family: **medium** Home Screen unless the user asks otherwise.
4. Use `widget.param` for preview-sheet tunables; use `widget.state` for desktop interactions.
5. Branch with `widget.family`, `widget.family_value(...)`, `w.when(...)`, or `w.unless(...)` only when supporting multiple families.
6. Repair layout issues before claiming completion.

## Default Pattern

```python
import widget

ctx = widget.context
accent = widget.param.color("Accent", "#34D399")
count = widget.state.int("count", 0)

w = widget.Widget(background=("#F8FAFC", "#0B1220"), style="clean")
w.text("Today", size=16, weight="semibold").line_limit(1).min_scale(0.72)
w.value(count, unit="x").content_transition("numericText").monospaced_digit()
w.progress(min(int(count), 10), total=10, color=accent, height=8)

if ctx.content_height >= 120:
    w.button("+1", action=count.increment(), background=accent, color="#FFFFFF")

w.render()
```

## Generation Rules

- One `widget.Widget()` entry per script
- Prefer documented primitives: `text`, `rich_text`, `value`, `symbol`, `svg`, `image`, `shape`, `rect`, `circle`, `path`, `table`, `line_chart`, `bar_chart`, `ring_chart`, `progress`, `row`, `column`, `layer`, `grid`, `region`, `canvas`, `button`, `link`, `toggle`
- `widget.param.color/slider/number/text/bool/choice/file` for preview-editable values
- `widget.state` actions: `increment()`, `decrement()`, `set(value)`, `toggle()`, `toggle_item(value)`
- Layout containers use `with` blocks: `with w.row(spacing=8):` then child calls on indented lines
- Use `ctx = widget.context` for size-aware composition inside `ctx.content_width` / `ctx.content_height`
- Add `.line_limit(...)` and `.min_scale(...)` to long text
- Widget animations are timeline/state-update animations, not continuous 60fps app loops

## Family Policy

| Request | Target |
| --- | --- |
| Unspecified | `medium` only |
| Explicit `small` | one title, one value, one compact visual |
| Explicit `large` | add real extra content, do not stretch medium |
| All Home Screen sizes | branch per family |
| Accessory families | only when explicitly requested |

## Hard Stops

- No `appui`, `scene`, or `ui` in widget deliverables
- No invented APIs or compatibility aliases omitted from public schema
- No claiming gradients, network data, charts, or interaction unless coded with documented APIs
- No `w.row(w.text(...), spacing=8)` — use `with w.row(...)`

## Repair Hints

| Issue | Fix |
| --- | --- |
| Blank widget | restore `w.render()` |
| Cropped text | shorten, branch by family, add `.line_limit(1).min_scale(0.6)` |
| Crowded medium | remove optional metrics or reduce chart density |
| Table lines too heavy | `line_width="hairline"` |
| Tap no effect | use `widget.state` action reference |
| Network failure | `cache_json(..., default=...)` fallback |

## Examples

- `examples/progress/` — medium widget with param, state, and progress bar

## Boundary

Widgets are not MiniApps. If the user wants in-app navigation, forms, or multi-screen tools, switch to `pythonide-appui`.
