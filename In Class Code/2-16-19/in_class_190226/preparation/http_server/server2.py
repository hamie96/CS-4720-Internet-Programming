

# from http.server documentation

from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(handler_class=SimpleHTTPRequestHandler)



