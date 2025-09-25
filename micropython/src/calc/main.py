from waveshare_2in import LCD_2inch
from machine import Pin,SPI,PWM
import time

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9



if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(10000)#max 65535

    LCD = LCD_2inch()
    #color BRG
    LCD.fill(LCD.WHITE)

    

    LCD.show()