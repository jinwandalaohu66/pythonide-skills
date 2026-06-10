"""Native module sample. Pair with pythonide-appui when presenting results in a MiniApp."""

import device
import permission
import storage

SNAPSHOT_KEY = "native.device_snapshot"


def refresh_snapshot():
    notification_status = permission.status("notifications")
    snapshot = {
        "device": device.model(),
        "system": f"{device.system_name()} {device.system_version()}",
        "battery": device.battery_level(),
        "notification": notification_status.get("status", "unknown"),
    }
    storage.set_json(SNAPSHOT_KEY, snapshot)
    return snapshot


if __name__ == "__main__":
    print(refresh_snapshot())
