from Server import Server
from logger import Logger, LogType

serverLogger = Logger("LogFile.txt")

with serverLogger:
    server = Server(serverLogger)
    server.run()