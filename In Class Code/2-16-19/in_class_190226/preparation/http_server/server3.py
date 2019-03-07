

# inspired by http.server documentation

from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler


class HelloServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write("<h1>Hello there!</h1>\n".encode("utf-8"))
        self.wfile.write(self.path.encode("utf-8"))


server_port = 12345


if __name__ == '__main__':
    server_address = ('', server_port)
    httpd = HTTPServer(server_address, HelloServer)
    httpd.serve_forever()



