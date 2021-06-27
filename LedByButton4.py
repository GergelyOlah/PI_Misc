import gpiozero as io
import time

led1 = io.LED(4)
led2 = io.LED(15)
button = io.Button(14)

led1.on()

def pressed():
	return led1.off()

def released():
	return led1.on()

while True:
	button.when_pressed = pressed
	button.when_released = released
