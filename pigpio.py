import RPi.GPIO as GPIO
import requests

from flask import Flask
app = Flask(__name__)

# TODO
# list of in [1,2,3]
# list of out , [1,2,3]
# list of outhttpcalls [https://1,https://2,https://3]
# add out http call
# add in status 
# check in is in the list and loop outs 
#[1,2,3].index(2) # => 1
#[1,2,3].index(4) # => ValueError


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 3 to be an input pin and set initial value to be pulled low (off)
URL = "http://192.168.0.100:8091/hitthebell"
def button_callback(channel):
    print("Button was pushed!" + str(channel))
    try:
       requests.get(URL,timeout=0.0000000001)
    except requests.exceptions.RequestException as e:  print(e)
   

GPIO.add_event_detect(3,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge





@app.route('/on')
def turn_led_on():
    GPIO.output(13, GPIO.HIGH)
    return "OK"

@app.route('/off')
def turn_led_off():
    GPIO.output(13, GPIO.LOW)
    return "OK"


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)

