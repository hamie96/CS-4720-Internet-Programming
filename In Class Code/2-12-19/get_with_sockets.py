from socket import socket



path = "/~bsetzer/4720sp19/nanoc/output/index.html"

host = "ksuweb.kennesaw.edu"

PORT = 80



conn = socket()

conn.connect((host,PORT))



try:

	first_line = "GET " + path + " HTTP/1.1\r\n"

	header1 = "Host: " + host + "\r\n"

	black_line = "\r\n"



	message = first_line + header1 + blank_line



	conn.sendall(message.encode("UTF-8))

	conn.shutdown(1)



	response_bytes = b""

	gbytes = conn.recv(4096)

	while len(gbytes) > 0:

		response_bytes += gbytes

		gbytes = conn.recv(4096)



	print(response_bytes.decode("UTF-8"))





finally:

	conn.shutdown(0)

	conn.close()



