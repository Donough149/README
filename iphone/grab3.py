# grab3.py — fetches the radio from GitHub instead of the Mac.
#
# The old version pulled from http://192.168.0.30:8642/ (the Mac on home
# Wi-Fi), which is why the radio only worked at home. This works anywhere.

import os
import urllib.request

BASE = "https://raw.githubusercontent.com/Donough149/README/main/iphone/"
DEST = os.path.dirname(os.path.abspath(__file__))

for name in ("airtime.html", "Airtime.py"):
    urllib.request.urlretrieve(BASE + name, os.path.join(DEST, name))

print("LOCAL OK")
