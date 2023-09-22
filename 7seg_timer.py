from machine import Pin
import time
A = Pin(1, Pin.OUT)
B = Pin(2, Pin.OUT)
C = Pin(3, Pin.OUT)
D = Pin(4, Pin.OUT)
E = Pin(5, Pin.OUT)
F = Pin(6, Pin.OUT)
G = Pin(7, Pin.OUT)
def n0():
    A.toggle(1)
    B.toggle(1)
    C.toggle(1)
    D.toggle(1)
    E.toggle(1)
    F.toggle(1)
def n1():
    B.value(1)
    C.value(1)
def n2():
    A.value(1)
    B.value(1)
    D.value(1)
    E.value(1)
    G.value(1)
def n3():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    G.value(1)
def n4():
    B.value(1)
    C.value(1)
    F.value(1)
    G.value(1)
def n5():
    A.value(1)
    C.value(1)
    D.value(1)
    F.value(1)
    G.value(1)
def n6():
    A.value(1)
    C.value(1)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(1)
def n7():
    A.value(1)
    B.value(1)
    C.value(1)
def n8():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(1)
def n9():
    A.value(1)
    B.value(1)
    C.value(1)
    F.value(1)
    G.value(1)
D1 = Pin(8, Pin.OUT)
D2 = Pin(9, Pin.OUT)
D3 = Pin(10, Pin.OUT)
D4 = Pin(11, Pin.OUT)
Dot = Pin(12, Pin.OUT)
rest= machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
start= machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
stop= machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
Num=[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
D1.value(0)
D2.value(0)
D3.value(0)
D4.value(0)
def re():
    A.value(0)
    B.value(0)
    C.value(0)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
s=1
i=0
while True:
    if rest.value() ==1:
        re()
        s=1
        i=0
    if start.value() ==1:
        if s==9:
            s=0
        if i==9:
            i=0
        while i<=9:
            if stop.value() == 1:
                break
            Num[i]()
            time.sleep(0.1)
            Num[i]()
            i+=1
            if i==9:
                Num[s]()
                time.sleep(0)
                re()
                s+=1