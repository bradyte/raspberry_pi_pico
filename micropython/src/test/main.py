# I2C Scanner MicroPython
from machine import Pin, SoftI2C
import ssd1306

# You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(17), sda=Pin(16))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


oled.text('Hello, World !', 0, 0)

oled.show()