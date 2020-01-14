from typing import Type

from Modules.carmodule import CarModule
from Modules.intercoolerspray import IntercoolerSpray


class ModuleManager:

    InterCoolerSprayModule: Type[CarModule]


    def __init__(self):
        self.InterCoolerSprayModule = IntercoolerSpray()