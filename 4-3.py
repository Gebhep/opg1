from machine import Pin #Importerer Pin klassen fra machine modulet
from time import sleep #Importerer sleep klassen fra time modulet

red_led = Pin(26, Pin.OUT) # Laver variabel for Pin 26 som et output

while True:
    red_led.value(1) # Tænder LED
    sleep(0.016) # Venter 1 sekund
    red_led.value(0) # Slukker LED
    sleep(0.016) # Venter 1 sekund