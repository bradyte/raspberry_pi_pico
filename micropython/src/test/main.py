# I2C Scanner MicroPython
from machine import Pin, SoftI2C
from time import sleep, sleep_ms
import ssd1306
import framebuf
from calc_glyphs import *



class Calculator:
    MAX_VALUE = 255  # Maximum value for 8-bit representation
    BASES = ['dec', 'hex', 'bin']
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(17), sda=Pin(16))
        self.oled_width = 128
        self.oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(self.oled_width, self.oled_height, self.i2c)
        self.entered_value = 0
        self.current_base = 'dec'  # can be 'dec', 'hex', or 'bin'
        self.last_base = self.current_base
        self._init_display()
        self.update_display()

    def _init_display(self):
        self.oled.fill(0)
        self.oled.text(f'DEC:{self.entered_value:>3d} HEX:0x{self.entered_value:02X}', 0, 0)
        self.oled.text(f'BIN:0b{self.entered_value:08b}', 0, 8)
        self.oled.show()

    def reset_display(self):
        self.oled.text(f'{self.entered_value:03d}', 32, 0)
        self.oled.text(f'0x{self.entered_value:02X}', 96, 0)
        self.oled.text(f'0b{self.entered_value:08b}', 32, 8)
        self.oled.show()

    def update_display(self):
        if self.current_base != self.last_base:
            self.last_base = self.current_base
        self.reset_display()

        if (self.current_base == 'dec'):
            fb = framebuf.FrameBuffer(c_glyphs['DEC_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 0, 0)
        elif (self.current_base == 'hex'):
            fb = framebuf.FrameBuffer(c_glyphs['HEX_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 65, 0) 
        elif (self.current_base == 'bin'):
            fb = framebuf.FrameBuffer(c_glyphs['BIN_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 0, 8)




        self.oled.show()

def main():
    calc = Calculator()
    while True:
        for i in range(calc.MAX_VALUE + 1):
            calc.entered_value = i
            calc.update_display()
            sleep_ms(100)


if __name__ == '__main__':
    main()
