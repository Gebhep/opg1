from machine import Pin
from time import sleep

button = Pin(4, Pin.IN)
b_val = 0

while True:
    if button.value() == 0:
        b_val = b_val + 1
        sleep(0.2)
    print (b_val)
    sleep(0.1)