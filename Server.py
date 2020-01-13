import socket
from logger import Logger, LogType
from typing import Type

class Server:

    serverSocket: socket
    serverLogger: Type[Logger]
    
    def __init__(self, logger: Type[Logger]):
        self.serverLogger = logger
        
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind(("127.0.0.1", 1234))
        self.serverSocket.listen(5)

    def run(self):
        self.serverLogger.log(LogType.ServerAction, "Server Starting")

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
