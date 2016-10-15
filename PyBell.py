from pushbullet import Pushbullet

import datetime
import RPi.GPIO as GPIO

GPIO.setup(23,GPIO.IN)
GPIO.setup(7,GPIO.out)

apiKey = "o.giFKbcb02CDCluBRGLZ9q5VwSXC6fWGz"
pb = Pushbullet(apiKey)

push = pb.push_note('System is live')

while True:
    if GIPO.input(23):
        push = pb.push_note('Door bell at ',str(datetime.datetime.now())[:16])
        GPIO.output(7,1)
    else:
        print 'nothing'
        GPIO.output(7,0)
GPIO.cleanup()
