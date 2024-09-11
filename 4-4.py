from machine import Pin #Importerer Pin klassen fra machine modulet
from time import sleep #Importerer sleep klassen fra time modulet

red_led = Pin(26, Pin.OUT) # Laver variabel for Pin 26 som et output
yellow_led = Pin(12, Pin.OUT) # Laver variabel for Pin 12 som et output
green_led = Pin(13, Pin.OUT) # Laver variabel for Pin 13 som et output


while True:
    red_led.value(1) # Tænder rød LED
    yellow_led.value(0) # Tænder rød LED
    green_led.value(1) # Tænder rød LED
    sleep(1) # Venter 1 sekund
    red_led.value(0) # Slukker LED
    yellow_led.value(1) # Slukker LED
    green_led.value(0) # Slukker LED
    sleep(1) # Venter 1 sekund