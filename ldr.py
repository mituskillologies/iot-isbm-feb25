import RPi.GPIO as GPIO				# VCC -> 3.3V
import time							# GND -> GND
GPIO.setmode(GPIO.BCM)				# D0  -> GPIO18
LDR_PIN = 18
GPIO.setup(LDR_PIN, GPIO.IN)
try:
	while True:
		data= GPIO.input(LDR_PIN)
		if data == 0:
			print('Light Present!')
		else:
			print('NO Light.')
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Program Ended')
	exit(0)
