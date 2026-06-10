import widget

ctx = widget.context
accent = widget.param.color("Accent", "#34D399")
count = widget.state.int("count", 0)

w = widget.Widget(background=("#F8FAFC", "#0B1220"), style="clean", padding=14)
w.text("Daily Progress", size=16, weight="semibold").line_limit(1).min_scale(0.72)
w.value(count, unit="done").content_transition("numericText").monospaced_digit()
w.progress(min(int(count), 10), total=10, color=accent, height=8)

if ctx.content_height >= 120:
    w.button("+1", action=count.increment(), background=accent, color="#FFFFFF")

w.render()
