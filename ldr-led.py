import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LDR_PIN = 18
LED_PIN = 17
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
	while True:
		data= GPIO.input(LDR_PIN)
		if data == 0:
			GPIO.output(LED_PIN, GPIO.HIGH)
		else:
			GPIO.output(LED_PIN, GPIO.LOW)
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Program Ended')
	exit(0)
