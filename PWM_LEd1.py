import gpiozero as io
from time import sleep

led1 = io.PWMLED(25)
led2 = io.LED(8)
ldr = io.LightSensor(15)

led2.source = ldr

while True:
    for i in range(5):
        led1.value = i/10
        print (i, ldr.value)
        sleep(0.3)

    for i in range(3,0, -1):
        led1.value = i/10
        print (i, ldr.value)
        sleep(0.3)
