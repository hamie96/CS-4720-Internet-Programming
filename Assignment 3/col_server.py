#  Hamilton Bradford
#  CS 4720
#  Assignment 3

from socket import socket
from collector import Collector

PORT = 12345

collector = Collector()
listener = socket()
listener.bind(('', PORT))

listener.listen(0)

while True:
    
    (conn, address) = listener.accept()

    data_bytes = b""

    receivedB = conn.recv(2048)
    while len(receivedB) > 0:
        data_bytes += receivedB
        receivedB = conn.recv(2048)

    data_string = data_bytes.decode("UTF-8")

    print("data_string", data_string)

    if len(data_string) == 0:
        reply = "Error: null command"
    else:
        cmd = data_string[0]            
        parameter = data_string[1:]     
        
        if cmd == 'A':
            try:
                v = float(parameter)
                collector.add(v)
                reply = "OK " + parameter + " added"
            except ValueError as ve:
                reply = "Error"
        
        elif cmd == 'a':
            reply = str(collector.average())
        elif cmd == 'c':
            reply = str(collector.count())
        elif cmd == 'd':
            reply = str(collector.standard_deviation())
        elif cmd == 'q':
            reply = str(collector.sum_squares())
        elif cmd == 's':
            reply = str(collector.sum())
        elif cmd == 'v':
            reply = str(collector.variance())
        elif cmd == 'z':
            collector = Collector()
            reply = "Collector Reset"
        else:
            reply = "Error"

    conn.sendall(reply.encode("UTF-8"))
    conn.shutdown(1)

conn.close()

listener.close()
