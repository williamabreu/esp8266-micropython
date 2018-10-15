from machine import Pin
from time import sleep

led = Pin(16, Pin.OUT)

while True:
	led.off()
	sleep(1)
	led.on()
	sleep(1)

