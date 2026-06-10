---
name: pythonide-scene
description: Build or repair PythonIDE 2D scene scripts, SpriteKit-style games, touch demos, physics samples, and turtle graphics using scene.run or turtle. Use when the user wants continuous drawing, sprites, collisions, frame loops, or game-style interaction — not AppUI forms or widgets.
license: MIT
version: "1.0.0"
last_updated: "2026-06-10"
user_invocable: true
---

# PythonIDE Scene

Execution rulebook for `scene` and `turtle` runtimes.

## Read Before Coding

1. [Scene module](https://pythonide.xin/docs/pages/scene-module/)
2. [Scene API reference](https://pythonide.xin/docs/pages/scene-api-reference/)
3. [scene.pyi](https://pythonide.xin/stubs/scene.pyi)
4. [Turtle module](https://pythonide.xin/docs/pages/turtle-module/) for teaching graphics

Do not generate AppUI or widget code for a scene/game request.

## Use When

- Continuous drawing, sprite movement, collisions, physics, touch loops, or shaders
- Existing code imports `scene` and needs repair
- Turtle teaching demos

## Do Not Use When

- The UI is a form, list, settings screen, or AppUI MiniApp
- The user wants imperative UIKit controls → `pythonide-automation` (`ui`)
- Static charts or business apps → `pythonide-appui`

## Workflow

1. Subclass `scene.Scene`
2. Create retained nodes in `setup()` after `self.size` is valid
3. Per-frame logic in `update()`; immediate drawing only in `draw()`
4. Touch in `touch_began` / `touch_moved` / `touch_ended`
5. End with exactly one `scene.run(MyScene(), ...)`
6. Keep assets optional unless the user provides them

## Correct Pattern

```python
import scene


class Demo(scene.Scene):
    def setup(self):
        self.background_color = "#111827"
        self.ball = scene.SpriteNode(
            color="#2f80ed",
            size=(44, 44),
            position=(self.size.w / 2, self.size.h / 2),
            parent=self,
        )
        self.label = scene.LabelNode(
            "Tap to move",
            font=("Helvetica", 18),
            position=(self.size.w / 2, 80),
            parent=self,
        )

    def touch_began(self, touch):
        self.ball.run_action(
            scene.Action.move_to(touch.location.x, touch.location.y, 0.25)
        )
        self.label.text = f"{touch.location.x:.0f}, {touch.location.y:.0f}"


scene.run(Demo(), show_fps=True)
```

## Hard Stops

- No AppUI (`Button`, `VStack`, `NavigationStack`, etc.) inside a `Scene`
- No blocking `while True` animation loops; use `update()` or `Action`
- No `rect`, `fill`, `text`, etc. outside `draw()`
- `SpriteNode("red")` treats `"red"` as a texture name — use `SpriteNode(color="red", ...)`
- Do not omit `scene.run(...)`
- `image_quad` / `triangle_strip` are not implemented

## Physics And Gameplay

- Use physics bodies only when collisions matter
- Retain sprites, labels, and game state on `self`
- Use `node.run_action(...)` for motion; calling `Action.move_to(...)` alone does nothing

## Turtle Runtime

- Use `import turtle` only for teaching/simple vector drawing
- Do not mix turtle and scene in one deliverable unless repairing existing code

## Repair Hints

| Issue | Fix |
| --- | --- |
| Blank scene | verify `scene.run(...)` and `setup()` does not crash |
| Node at origin | set explicit `position` from `self.size` |
| No motion | `node.run_action(...)`, not bare `Action` |
| Dead touch | implement `touch_began(self, touch)` |

## Examples

- `examples/tap_ball/` — tap-to-move sprite demo
