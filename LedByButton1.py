import gpiozero as io
import time

led1 = io.LED(4)
led2 = io.LED(15)
button = io.Button(14)

led1.on()
led2.off()

while True:
	if button.is_pressed:
		led1.off()
		led2.on()
