from typing import Type
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy

class TempReader():

    #values for resistance calculation
    INPUTVOLTAGE: float
    RESISTANCE: float

    #values for steinhart-hart calculation
    A: float
    B: float
    C: float
    
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)

        self.INPUTVOLTAGE = 3.3 #3.3 volts
        self.RESISTANCE = 1000 #1k ohms

        self.A = 1.250175945e-3
        self.B = 2.698384119e-4
        self.C = 1.040158027e-7

        
    def read(self) -> float:
        chan = AnalogIn(self.ads, ADS.P0)
        resistance = self.calculateResistance(chan.voltage)
        KelvinTemp = self.calculateTemp(resistance)
        return self.kelvinToCelcius(KelvinTemp)


    def calculateResistance(self, measuredVoltage: float) -> float:
        return self.RESISTANCE*((self.INPUTVOLTAGE/measuredVoltage)-1)

    def calculateTemp(self, resistance: float) -> float:
        return 1.0/((self.A)+(self.B*numpy.log(resistance))+(self.C*numpy.power(numpy.log(resistance),3)))

    def kelvinToCelcius(self, temp: float) -> float:
        return temp-273.15