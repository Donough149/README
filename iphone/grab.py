# grab.py — replaces grab3.py. Downloads the radio app from GitHub instead of
# from the Mac at 192.168.0.30, so it updates from anywhere (Wi-Fi, 5G, abroad).

import os
import urllib.request

BASE = "https://raw.githubusercontent.com/Donough149/README/main/iphone/"
DEST = os.path.expanduser("~/Documents")

for name in ("airtime.html", "Airtime.py"):
    urllib.request.urlretrieve(BASE + name, os.path.join(DEST, name))
    print("got", name)

print("OK — now run Airtime.py")
