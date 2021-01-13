import RPi.GPIO as GPIO
from time import *

pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 300)
#GPIO.setwarings(False)

while True:
	GPIO.output(pin, True)
	p.start(100)
	p.ChangeDutyCycle(100)
	p.ChangeFrequency(100)
	sleep(0.5)
	p.stop()

	GPIO.output(pin, False)
	sleep(2)

GPIO.cleanup()
