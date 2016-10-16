from pushbullet import Pushbullet
import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.OUT)

count = 0.0

apiKey = "o.giFKbcb02CDCluBRGLZ9q5VwSXC6fWGz"
pb = Pushbullet(apiKey)

push = pb.push_note('System is live', "Working...")

while True:
    input_state = GPIO.input(24)
    if input_state == True:
        if count < 1:
            push = pb.push_note('Door bell at ', str(datetime.datetime.now())[:16])
            count -= 0.3
         elif count > 4:
            count = 2
        GPIO.output(7,1)
        time.sleep(.1)
        count += 1
    else:
        GPIO.output(7,0)
        time.sleep(.1)
GPIO.cleanup()


