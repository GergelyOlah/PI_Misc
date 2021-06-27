import gpiozero as io
from signal import pause

led1 = io.LED(25)
led2 = io.LED(8)
button = io.Button(4)

def top():
	led1.on()
	led2.off()
def bottom():
	led1.off()
	led2.on()

bottom()
button.when_pressed = top
button.when_released = 	bottom

pause()
