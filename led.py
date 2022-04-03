import RPi.GPIO as GPIO
from time import sleep

led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
    GPIO.output(led, GPIO.HIGH)

    while True:
        sleep(101)
except KeyboardInterrupt:
    print("Exiting...")

GPIO.cleanup()

