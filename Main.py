from Server import Server
from logger import Logger, LogType
from Modules.modulemanager import ModuleManager

serverLogger = Logger("LogFile.txt")

with serverLogger:

    moduleManager = ModuleManager(serverLogger)

    server = Server(serverLogger)
    server.run()