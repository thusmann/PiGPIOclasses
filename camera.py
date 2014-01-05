import RPi.GPIO as GPIO
from subprocess import call

CameraLedPin = 5

class Camera:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(CameraLedPin, GPIO.OUT, initial = False)

	def led_on(self):
		GPIO.output(CameraLedPin, True)

	def lead_off(self):
		GPIO.output(CamerLedPin, False)


	def take_photo(self, filename):
		call(['raspistill -n -t 0 -hf -o {0}'.format(filename)], shell = True)

	def timelapse(self, filenames, interval, duration):
		call(['raspistill -n -o {0} -tl {1} -t {2}'.format(filnames, interval, duration)], shell = True)
