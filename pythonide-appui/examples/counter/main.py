import appui

state = appui.State(count=0, status="Ready")


def increment():
    state.count += 1
    state.status = f"Count is {state.count}"


def reset():
    state.batch_update(count=0, status="Reset")


def body():
    return appui.NavigationStack(
        appui.Form([
            appui.Section("Counter", [
                appui.LabeledContent("Value", value=str(state.count)),
                appui.HStack([
                    appui.Button("Reset", action=reset).button_style("bordered"),
                    appui.Button("+1", action=increment).button_style("bordered_prominent"),
                ], spacing=12),
            ], footer=state.status),
        ]).navigation_title("Counter")
    )


appui.run(body, state=state, presentation="fullscreen_with_close")
