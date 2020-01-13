from enum import Enum
from typing import TextIO
import datetime

#enum to catagorize log types
class LogType(Enum):
    ClientRequest = 1
    ClientResponce = 2
    ServerRequest = 3
    ServerResponce = 4
    ServerAction = 5
    Error = 6

class Logger:

    __logFileName: str
    __logFileWriter: TextIO

    def __init__(self, FileName: str):
        self.__logFileName = FileName

    def __enter__(self):
        self.__logFileWriter = open(self.__logFileName, "a")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__logFileWriter.close()
    
    def log(self, type: LogType, text: str):
        logString = str(datetime.datetime.now()) + ", " + type._name_ + ", " + text + "\n"
        self.__logFileWriter.write(logString)