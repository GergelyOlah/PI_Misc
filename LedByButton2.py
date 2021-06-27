import gpiozero as io
import time

led1 = io.LED(4)
led2 = io.LED(15)
button = io.Button(14)

led1.blink()
led2.blink()
#led1.on()
#led2.off()

def pressed():
	led1.off()
	led2.on()

def released():
	led1.on()
	led2.off()

while True:
	button.when_pressed = pressed
	button.when_released = released #No () used! It would return None.
