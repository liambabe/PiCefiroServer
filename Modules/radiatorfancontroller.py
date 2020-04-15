from typing import Type

from Modules.carmodule import CarModule

class RadiatorFanController(CarModule):

    state: bool
    
    def __init__(self):
        super(RadiatorFanController, self).__init__("Radiator Fan Controller")

        self.state = False

    def getState(self) -> bool:
        return self.state