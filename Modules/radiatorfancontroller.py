from typing import Type

from Modules.carmodule import CarModule

class PIController:
    P = 0
    I = 0

class RadiatorFanController(CarModule):

    piController: Type[PIController]
    
    def __init__(self):
        super(RadiatorFanController, self).__init__("Radiator Fan Controller")

        self.piController = PIController()