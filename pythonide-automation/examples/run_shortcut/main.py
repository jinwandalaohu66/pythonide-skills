import shortcuts

# Replace with a Shortcut name the user already has on device.
SHORTCUT_NAME = "Daily Log"


def run_daily_log():
    result = shortcuts.run_shortcut(SHORTCUT_NAME)
    if not result:
        print(f"Shortcut '{SHORTCUT_NAME}' did not run successfully.")
        return False
    print("Shortcut launched.")
    return True


if __name__ == "__main__":
    run_daily_log()
