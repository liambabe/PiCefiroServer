from typing import Type

from logger import Logger, LogType
from Modules.carmodule import CarModule
from Modules.intercoolerspray import IntercoolerSpray
from Modules.radiatorfancontroller import RadiatorFanController

class ModuleManager:

    serverLogger: Type[Logger]

    InterCoolerSprayModule: Type[CarModule]
    RadiatorFanControllerModule: Type[CarModule]

    def __init__(self, logger: Type[Logger]):
        self.serverLogger = logger

        self.serverLogger.log(LogType.ModuleAction, "Module manager Starting")
        self.InterCoolerSprayModule = IntercoolerSpray()
        self.RadiatorFanControllerModule = RadiatorFanController()