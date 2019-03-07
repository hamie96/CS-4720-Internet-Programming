

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<h1>Hello World!</h1>\n".encode("UTF-8"))
        self.wfile.write("     Rainy day today".encode("UTF-8"))




PORT = 8080

if __name__ == "__main__":
    server_address = ("", PORT)
    server = HTTPServer(server_address, HelloHandler)
    server.serve_forever()


