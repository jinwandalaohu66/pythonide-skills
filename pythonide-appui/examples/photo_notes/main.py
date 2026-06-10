import appui
import storage

NOTES_KEY = "photo_notes.items"


def load_notes():
    return storage.get_json(NOTES_KEY, [])


state = appui.State(items=load_notes(), status="Pick a photo to attach a note")


def on_photo_picked(paths):
    if not paths:
        state.status = "No photo selected"
        return
    items = list(state.items)
    items.append({"id": f"note-{len(items) + 1}", "path": paths[0], "note": ""})
    state.items = items
    state.status = f"Saved {len(items)} item(s)"
    storage.set_json(NOTES_KEY, items)


def note_row(item):
    return appui.LabeledContent(item["id"], value=item["path"])


def note_key(item):
    return item["id"]


def saved_section():
    if not state.items:
        return appui.Section("Saved", [appui.Text("No items yet")])
    return appui.Section("Saved", [
        appui.ForEach(state.items, row_builder=note_row, key=note_key),
    ])


def body():
    return appui.NavigationStack(
        appui.Form([
            appui.Section("Capture", [
                appui.PhotoPicker(
                    selection_limit=1,
                    filter="images",
                    on_picked=on_photo_picked,
                    label="Choose Photo",
                ),
            ], footer=state.status),
            saved_section(),
        ]).navigation_title("Photo Notes")
    )


appui.run(body, state=state, presentation="fullscreen_with_close")
