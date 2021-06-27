import gpiozero as io
import time

led1 = io.LED(4)
led2 = io.LED(15)
button = io.Button(14)

led1.on()
led2.off()

print ("Program is running.")

button.wait_for_press()
print ("Button is pressed, program terminates.")
