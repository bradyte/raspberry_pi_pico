# I2C Scanner MicroPython
from machine import Pin, SoftI2C
from time import sleep, sleep_ms
from keypad import Keypad
import ssd1306
import framebuf
from calc_glyphs import *



class Calculator:
    MAX_VALUE = 255  # Maximum value for 8-bit representation
    BASES = ['dec', 'hex', 'bin']
    ROW_PINS = [Pin(2), Pin(3), Pin(4), Pin(5)]
    COL_PINS = [Pin(6), Pin(7), Pin(8), Pin(9), Pin(10), Pin(11), Pin(12), Pin(13)]
    KEYS = [
    ['C', 'D', 'E', 'F', 'ce', 'ac', 'dec', 'and'],
    ['8', '9', 'A', 'B', '*', '/', 'hex', 'or'],
    ['4', '5', '6', '7', '+', '-', 'bin', 'not'],
    ['0', '1', '2', '3', 'on', '=', 'rs', 'ls']]
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(17), sda=Pin(16))
        self.oled_width = 128
        self.oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(self.oled_width, self.oled_height, self.i2c)
        self.entered_digit = 0
        self.current_value = 0
        self.input_string = ''
        self.keypad = Keypad(self.ROW_PINS, self.COL_PINS, self.KEYS)
        self.key_pressed = 0
        self.current_base = 'dec'  # can be 'dec', 'hex', or 'bin'
        self.last_base = self.current_base
        self._reset_display()
        self.update_display()

    def update_display(self):
        self._clear_display()
        self._reset_display()
        self._update_base()
        self._update_base_numbers() 
        self._update_input_text()

          
        
        self.oled.show()

    def read_keypad(self):
        self.key_pressed = self.keypad.read_keypad()
        if self.key_pressed:  
            if self.key_pressed in '0123456789ABCDEF':
                if (self.current_base == 'dec') and (self.key_pressed in '0123456789'):
                    self.input_string += self.key_pressed
                    self.entered_digit = int(self.key_pressed)
                elif (self.current_base == 'hex') and (self.key_pressed in '0123456789ABCDEF'):
                    self.input_string += self.key_pressed
                    self.entered_digit = int(self.key_pressed, 16)
                elif (self.current_base == 'bin') and (self.key_pressed in '01'):
                    self.input_string += self.key_pressed
                    self.entered_digit = int(self.key_pressed, 2)
            if self.key_pressed == 'ce':  
                self.current_value = 0
                self.entered_digit = 0
                self.input_string = ''
            if self.key_pressed in self.BASES:
                self.current_base = self.key_pressed
            self.update_display()
                
            
    def _clear_display(self):
        self.oled.fill(0)

    def _reset_display(self):
        self.oled.text(f'DEC:', 0, 0)
        self.oled.text(f'HEX:', 64, 0)
        self.oled.text(f'BIN:', 0, 8)

    def _update_base(self):
        if (self.current_base == 'dec'):
            fb = framebuf.FrameBuffer(c_glyphs['DEC_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 0, 0)
        elif (self.current_base == 'hex'):
            fb = framebuf.FrameBuffer(c_glyphs['HEX_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 64, 0) 
        elif (self.current_base == 'bin'):
            fb = framebuf.FrameBuffer(c_glyphs['BIN_INV'], 24, 8, framebuf.MONO_HLSB) 
            self.oled.blit(fb, 0, 8)
        self.last_base = self.current_base

    def _update_input_text(self):
        self.oled.text(f'{self.input_string}', 
                       self.oled_width - len(self.input_string) * 8, 
                       self.oled_height - 8)
        print(f'{self.input_string}')

    def _update_base_numbers(self):
        temp = self.current_value * 10 + self.entered_digit
        if temp < self.MAX_VALUE:
            self.current_value = temp
        self.oled.text(f'{self.current_value:>3d}', 32, 0)
        self.oled.text(f'{self.current_value:02X}', 96, 0)
        self.oled.text(f'{self.current_value:08b}', 32, 8)

def main():
    calc = Calculator()
    while True:
        calc.read_keypad()
        sleep(0.15)  # debounce and delay


if __name__ == '__main__':
    main()
