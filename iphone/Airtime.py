# Airtime.py — runs the radio entirely on this iPhone. No Mac, no home Wi-Fi.
#
# The old setup fetched everything from a Mac at 192.168.0.30:8642, which is why
# it only worked at home. This version serves the app from the phone itself, so
# it works on Wi-Fi, 5G, or a plane.
#
# Put this file and airtime.html in the same folder (~/Documents) and run it.

import os
import sys
import threading
import functools
import http.server
import socketserver

PORT = 8642
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "airtime.html")
URL = "http://127.0.0.1:{}/airtime.html".format(PORT)


def start_server():
    """Serve this folder on the phone's own loopback address."""
    if not os.path.exists(PAGE):
        sys.exit("airtime.html is missing from {} — run grab.py first.".format(HERE))
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=HERE)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def run_in_pythonista(httpd):
    """Preferred path: keep the page inside Pythonista's own web view.

    Handing off to Safari would background this script, and iOS suspends
    background processes — which kills the server the page is loading from.
    Staying in-app keeps the server alive for as long as the radio is open.
    """
    import ui

    view = ui.WebView(name="Airtime")
    view.load_url(URL)
    view.present("fullscreen", hide_title_bar=False)
    view.wait_modal()          # blocks here while you listen
    httpd.shutdown()


def run_anywhere(httpd):
    """Fallback for a-Shell/Pyto/desktop: open a browser and hold the server up."""
    import time
    import webbrowser

    webbrowser.open(URL)
    print("Serving {} — leave this running while you listen.".format(URL))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == "__main__":
    server = start_server()
    try:
        run_in_pythonista(server)
    except ImportError:
        run_anywhere(server)
