

import http.server
import socketserver

PORT = 8000

# Found this at
# https://stackoverflow.com/questions/39801718/how-to-run-a-http-server-which-serve-a-specific-path
#
# Change the base directory for the simple server by intercepting the constructor
#       for SimpleHTTPRequestHandler

DIRECTORY = "web"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


# Handler = http.server.SimpleHTTPRequestHandler
# Handler.directory = "/Users"



with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
