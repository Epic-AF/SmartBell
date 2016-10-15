import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.IN)

while True:
    input_state = GPIO.input(24)
    if input_state == True:
        print 'hello'
    else:
        print 'nothing'
GPIO.cleanup()
