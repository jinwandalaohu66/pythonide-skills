import scene


class TapBall(scene.Scene):
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
        self.ball.run_action(scene.Action.move_to(touch.location.x, touch.location.y, 0.25))
        self.label.text = f"{touch.location.x:.0f}, {touch.location.y:.0f}"


scene.run(TapBall(), show_fps=True)
