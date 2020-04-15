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
        self.TRANSISTOR = DigitalOutputDevice(self.TRANSISTOR_PIN)

    def getState(self) -> bool:
        return self.TRANSISTOR_STATE

    #turn transistor on and off
    def setState(self, state: str): 
        if (state.strip().lower() == "on"):
            self.TRANSISTOR_STATE = True
            self.TRANSISTOR.on()
        elif (state.strip().lower() == "off"):
            self.TRANSISTOR_STATE = False
            self.TRANSISTOR.off()
        else:
            #TODO implement error here
            pass

