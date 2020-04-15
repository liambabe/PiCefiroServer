#simple program to indepently run the temp guage

from Modules.oledcontroller import OledController
from Modules.radiatorfancontroller import RadiatorFanController
from time import sleep

oled = OledController()
fan = RadiatorFanController()

while True:
    value = fan.getState()
    oled.displayText(str(value))
    sleep(1)