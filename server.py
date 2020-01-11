import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 1234))

serverSocket.listen(5)

while True:

    conn, addr = serverSocket.accept()
    from_client: str

    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
        conn.send("connection sucessful\n")
    conn.close()
    print("client disconnected")