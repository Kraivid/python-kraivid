from machine import Pin
import time

led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)
led3 = Pin(8, Pin.OUT)
led = [led1,led2,led3]
but1= machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
but2= machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if but1.value() == 1:
        i=0
        while i <= 2:
            led[i].toggle()
            time.sleep(1)
            led[i].toggle()
            i += 1
        
    if but2.value() == 1:
        b=2
        while b  >= 0:
            led[b].toggle()
            time.sleep(1)
            led[b].toggle()
            b -= 1