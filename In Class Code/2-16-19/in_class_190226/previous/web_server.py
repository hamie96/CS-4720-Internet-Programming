
from http.server import HTTPServer, SimpleHTTPRequestHandler


PORT = 8080

if __name__ == "__main__":
    server_address = ("", PORT)
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    server.serve_forever()
