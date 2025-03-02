import RPi.GPIO as GPIO				# VCC ->  5V
import time							# GND ->  GND
GPIO.setmode(GPIO.BCM)				# OUT ->  GPIO18
SERVO_PIN = 18
IR_PIN = 17
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(IR_PIN, GPIO.IN)
p = GPIO.PWM(SERVO_PIN, 50)
p.start(0)
try:
	while True:
		data = GPIO.input(IR_PIN)
		if data == 0:
			p.ChangeDutyCycle(7.5)
		else:
			p.ChangeDutyCycle(12.5)
		time.sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
	p.stop()
	print('Program Ended')
