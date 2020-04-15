from typing import Type
import gpiozero
from Modules.carmodule import CarModule

class RadiatorFanController(CarModule):

    TRANSISTOR_STATE: bool
    TRANSISTOR_PIN: int

    def __init__(self):
        super(RadiatorFanController, self).__init__("Radiator Fan Controller")

        self.TRANSISTOR_PIN = 21
        self.TRANSISTOR_STATE = False

    def getState(self) -> bool:
        return self.TRANSISTOR_STATE

