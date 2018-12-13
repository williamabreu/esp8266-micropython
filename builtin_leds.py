# MICROPYTHON BUILT-IN LEDS NODEMCU
# - Pin 2
# - Pin 16

from machine import Pin
from time import sleep

led_1 = Pin(2, Pin.OUT)
led_2 = Pin(16, Pin.OUT)

while True:
    led_1.on()
    led_2.off()
    sleep(0.3)
    led_1.off()
    led_2.on()
    sleep(0.3)
