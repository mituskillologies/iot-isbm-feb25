import RPi.GPIO as GPIO				# VCC ->  5V
import time							# GND ->  GND
GPIO.setmode(GPIO.BCM)				# OUT ->  GPIO18
SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)
p = GPIO.PWM(SERVO_PIN, 50)
p.start(0)
try:
	while True:
		p.ChangeDutyCycle(2.5)
		time.sleep(0.3)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.3)
		p.ChangeDutyCycle(12.5)
		time.sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
	p.stop()
	print('Program Ended')
