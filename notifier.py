import urllib2
import json
import RPi.GPIO as GPIO
import time

GET_LAST_MESSAGE_URL = 'https://slack.com/api/channels.history?token=xxxx&channel=C0PUJPG2E&count=1&pretty=1'
NOTIFY_CHANNEL_URL = 'https://slack.com/api/chat.postMessage?token=xxxx&channel=C0PUJPG2E&text=Notifying%20remote%20console...&pretty=1'

seq = [7, 11, 13, 15]  # Pin sequence
GPIO.setmode(GPIO.BOARD)

while True:
    print "Checking last message on slack channel"
    response = json.loads(urllib2.urlopen(GET_LAST_MESSAGE_URL).read())
    text = response['messages'][0]['text']

    if text == "Drink being poured!":
        print "Triggering party. Notifying channel. "
        urllib2.urlopen(NOTIFY_CHANNEL_URL).read()

        for j in seq:
            GPIO.setup(j, GPIO.OUT)

        for i in range(0, 8):
            print "Iteration: " + str(i)
            for j in seq:
                GPIO.output(j,True)
                time.sleep(1)
                GPIO.output(j,False)

        print "Done"
        GPIO.cleanup()

    else:
        print "Sleeping for 3 seconds"
        time.sleep(3)
