import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 1234))

sock.send("test message from client".encode())

sock.close()