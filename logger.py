from enum import Enum
from typing import TextIO
import datetime

class LogType(Enum):
    """ Enum to catagorize log types """

    ClientRequest = 1
    ClientResponce = 2
    ServerRequest = 3
    ServerResponce = 4
    ServerAction = 5
    Error = 6
    LoggerStart = 7
    LoggerEnd = 8
    ModuleAction = 9

class Logger:

    __logFileName: str
    __logFileWriter: TextIO

    def __init__(self, FileName: str):
        self.__logFileName = FileName

    def __enter__(self):
        self.__logFileWriter = open(self.__logFileName, "a")
        self.__logClearStartLine()
        self.log(LogType.LoggerStart, "Start Of Server Session")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log(LogType.LoggerEnd, "End Of Server Session")
        self.__logFileWriter.close()
    
    def log(self, type: LogType, text: str):
        logString = str(datetime.datetime.now()) + ", " + type._name_ + ", " + text + "\n"
        self.__logFileWriter.write(logString)

    def __logClearStartLine(self):
        """  """
        
        self.__logFileWriter.write("\n")
        self.__logFileWriter.write("============================")