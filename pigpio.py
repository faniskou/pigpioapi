import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(4, GPIO.OUT 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)



GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge



def button_callback(channel):
    print("Button was pushed!")

@app.route('/on')
def turn_led_on():
    GPIO.output(4, GPIO.HIGH)
    return "OK"

@app.route('/off')
def turn_led_off():
    GPIO.output(4, GPIO.LOW)
    return "OK"

if __name__ == '__main__':
    app.run()
