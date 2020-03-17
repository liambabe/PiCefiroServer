#simple program to indepently run the temp guage

from Data.tempreader import TempReader
from Modules.oledcontroller import OledController
from time import sleep

tempReader = TempReader()
oled = OledController()

while True:
    value = tempReader.read()
    print(value)
    #oled.displayText(value)
    time.sleep(1)