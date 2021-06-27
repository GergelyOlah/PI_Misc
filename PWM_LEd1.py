import gpiozero as io
from time import sleep

led = io.PWMLED(25)

while True:
    for i in range(5):
        led.value = i/10
        print (i)
        sleep(0.3)

    for i in range(3,0, -1):
        led.value = i/10
        print (i)
        sleep(0.3)
