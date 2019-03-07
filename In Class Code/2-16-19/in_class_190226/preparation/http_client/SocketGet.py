
from socket import socket


sock = socket()
sock.connect(('localhost', 80))

try:
    # request = "GET /pub/4720sp19/nanoc/output/style/style.css HTTP/1.1\r\n"
    # request = "GET /index.html HTTP/1.1\r\n"
    request = "GET / HTTP/1.1\r\n"
    headers = {"Host": "localhost"}
    # sock.sendall(request.encode())
    # for k in headers:
    #     sock.sendall((k + ": " + headers[k] + "\n").encode())

    rq = request
    for k in headers:
        rq += k + ": " + headers[k] + "\r\n"
    rq += "\r\n"

    print(rq)
    print("=" * 20)

    sock.sendall(rq.encode("UTF-8"))
    sock.shutdown(1)

    responseB = b""
    rcvd = sock.recv(1024)
    while len(rcvd) > 0:
        responseB += rcvd
        rcvd = sock.recv(1024)
    print(responseB.decode("UTF-8"))


finally:
    sock.close()
