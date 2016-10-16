import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    input_state = GPIO.input(24)
    if input_state == True:
        print 'hello'
        time.sleep(0.3)
    else:
        time.sleep(0.3)
        print 'nothing'
GPIO.cleanup()
