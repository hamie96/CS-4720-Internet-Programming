
from socket import socket

conn = socket()
conn.connect(('localhost', 12345))

print("connection made")

cmd = 'd200.30'
conn.sendall(cmd.encode('UTF-8'))
conn.shutdown(1)
reply_bytes = conn.recv()
reply_string = reply_bytes.decode('UTF-8')

print(reply_string)

conn.close()
