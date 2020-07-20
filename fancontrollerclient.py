#simple program to indepently run the temp guage
#NOTE: TO BE USED IN TESTING PURPOSES ONLY

from Modules.oledcontroller import OledController
from Modules.radiatorfancontroller import RadiatorFanController
from time import sleep
import threading

oled = OledController()
fan = RadiatorFanController()

def thread_Display(name):
    while True:
        value = fan.getState()
        oled.displayText(str(value))
        sleep(1)

displayThread = threading.Thread(target=thread_Display, args=(1,))
displayThread.start()

while True:
    print("Value is currently: " + str(fan.getState()))
    userInput = input('set on or off: ')
    fan.setState(userInput)

