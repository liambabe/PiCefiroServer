from Modules.carmodule import CarModule

class PIController:
    P = 0
    I = 0

class RadiatorFanController(CarModule):
    
    def __init__(self):
        super(RadiatorFanController, self).__init__("Radiator Fan Controller")