import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
IR_PIN = 18
BUZZ_PIN = 17
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(BUZZ_PIN, GPIO.OUT)
try:
	while True:
		data= GPIO.input(IR_PIN)
		if data == 0:
			GPIO.output(BUZZ_PIN, GPIO.HIGH)
		else:
			GPIO.output(BUZZ_PIN, GPIO.LOW)
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Program Ended')
	exit(0)
