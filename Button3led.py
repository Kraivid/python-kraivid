from machine import Pin
import time

led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)
led3 = Pin(8, Pin.OUT)
but1= machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
but2= machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
but3= machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if but1.value() == 1:
        led1.value(0)
        time.sleep(0.5)
        led1.value(1)
    if but2.value() == 1:
        led2.value(0)
        time.sleep(0.5)
        led2.value(1)
    if but3.value() == 1:
        led3.value(0)
        time.sleep(0.5)
        led3.value(1)