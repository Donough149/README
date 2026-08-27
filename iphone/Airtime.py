# Airtime.py — serves the radio from this iPhone, for the Airtime shortcut.
#
# The shortcut runs grab3.py, then this, then opens http://127.0.0.1:8787/.
# Port 8787 must match the shortcut's last step.
#
# Written for Pythonista's Python 3.6: no `directory=` kwarg on the request
# handler (that landed in 3.7), so the handler resolves paths itself.

import os
import wave
import threading
import http.server
import socketserver

PORT = 8787
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "airtime.html")
SILENCE = os.path.join(HERE, "_silence.wav")


def make_silence(path):
    """One second of silence, so there's something to loop if the file is gone."""
    with wave.open(path, "wb") as fh:
        fh.setnchannels(1)
        fh.setsampwidth(2)
        fh.setframerate(44100)
        fh.writeframes(b"\x00\x00" * 44100)


def keep_awake():
    """Loop silent audio so iOS keeps Pythonista running in the background.

    Without this, opening Safari backgrounds Pythonista, iOS suspends it, and
    the server dies before Safari can load the page — which is what produced
    "Safari can't open the page because it couldn't connect to the server".
    An active audio session is what earns the app background time.
    """
    try:
        import sound
    except ImportError:
        return None                      # not on Pythonista; nothing to do
    if not os.path.exists(SILENCE):
        make_silence(SILENCE)
    player = sound.Player(SILENCE)
    player.number_of_loops = -1
    player.play()
    return player


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        """Serve airtime.html at the root, everything else from this folder."""
        clean = path.split("?", 1)[0].split("#", 1)[0]
        if clean in ("/", "/index.html", "/airtime.html"):
            return PAGE
        return os.path.join(HERE, clean.lstrip("/"))

    def log_message(self, *args):
        pass                             # keep the Pythonista console clean


if __name__ == "__main__":
    if not os.path.exists(PAGE):
        raise SystemExit("airtime.html missing from {} — run grab3.py".format(HERE))

    holder = keep_awake()                # keep a reference so it isn't collected
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print("Radio serving on http://127.0.0.1:{}/".format(PORT))
    print("Silent audio is holding Pythonista awake — leave this running.")

    try:
        threading.Event().wait()         # stay alive for the shortcut's handoff
    except KeyboardInterrupt:
        server.shutdown()
        if holder:
            holder.stop()
