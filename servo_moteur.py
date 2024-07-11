from machine import Pin,PWM
import time
sg90 = PWM(Pin(22, mode=Pin.OUT))
sg90.freq(50)

def  lock():
    sg90.duty(105)
def unlock():
    sg90.duty(58)

