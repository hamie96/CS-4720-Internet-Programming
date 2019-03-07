
from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("ContentType", "text/html")
        self.end_headers()
        self.wfile.write("<h1><b>Hello World!</b></h1>\n".encode("UTF-8"))
        self.wfile.write("<b><blink>DAVID KIM IS THE WORST PROFESSOR AT KSU</blink></b>".encode("UTF-8"))


PORT = 8080

if __name__ == "__main__":
    server_address = ("",PORT)
    server = HTTPServer(server_address, HelloHandler)
    server.serve_forever()
    
