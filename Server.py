import socket

class Server:

    serverSocket: socket
    
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(("127.0.0.1", 1234))
        self.serverSocket.listen(5)

    def run(self):
        while True:
            conn, addr = self.serverSocket.accept()
            from_client: str

            while True:
                data = conn.recv(4096)
                if not data: break
                from_client = data.decode()
                print(from_client)
            conn.close()
            print("client disconnected")
