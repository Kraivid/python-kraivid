from machine import Pin, Timer
import time
ledG1 = Pin(3, Pin.OUT)
ledY1 = Pin(4, Pin.OUT)
ledR1 = Pin(5, Pin.OUT)
ledG2 = Pin(12, Pin.OUT)
ledY2 = Pin(13, Pin.OUT)
ledR2 = Pin(14, Pin.OUT)
led1 = Pin(7, Pin.OUT)
led2 = Pin(8, Pin.OUT)
led3 = Pin(9, Pin.OUT)
ledrail = [led1,led2,led3]
        
timer = Timer()

def blink(timer):
    ledG1.toggle()
    ledY1.toggle()
    ledR1.toggle()
    
def rail(timer):
    i=0
    while i < 3:
        ledrail[i].toggle()
        time.sleep(1)
        ledrail[i].toggle()
        i += 1
        
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=rail)