from typing import Type
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

from Modules.carmodule import CarModule

class OledController(CarModule):

    WIDTH: int
    HEIGHT: int
    BORDER: int
    
    def __init__(self):
        super(OledController, self).__init__("Oled Controller")
        self.WIDTH = 128
        self.HEIGHT = 64
        self.BORDER = 4

        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, self.i2c, addr=0x3c)
        self.font = ImageFont.load_default()

        self.clear()
        self.initScreen()
        self.displayText("test")
     
    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def initScreen(self):
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.image = Image.new('1', (self.oled.width, self.oled.height))
     
        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)
     
        # Draw a white background
        self.draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)
     
        # Draw a smaller inner rectangle
        self.draw.rectangle((self.BORDER, self.BORDER, self.oled.width - self.BORDER - 1, self.oled.height - self.BORDER - 1),
                   outline=0, fill=0)

    def displayText(self, displayText: str):
        # Draw Some Text
        text = displayText
        (font_width, font_height) = self.font.getsize(text)
        self.draw.text((self.oled.width//2 - font_width//2, self.oled.height//2 - font_height//2),
        text, font=self.font, fill=255)
     
        # Display image
        self.oled.image(self.image)
        self.oled.show()

