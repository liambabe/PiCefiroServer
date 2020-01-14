"""

Base class for car module items to inherit from

"""

class CarModule:
    
    __moduleName: str

    def __init__(self, name: str):
        self.__moduleName = name

    def getName(self) -> str:
        return self.__moduleName
