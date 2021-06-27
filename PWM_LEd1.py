import gpiozero as io

led = io.PWMLED(4)

while True:
    for i in range(5):
        led.value(i)