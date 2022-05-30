from gpiozero import LED, Button
import requests

from flask import Flask
app = Flask(__name__)

# TODO

list_in = [4,17,27,22]
list_out = [2]
list_out_http =  ["http://192.168.0.100:8091/hitthebell"]
# add in status 
# check in is in the list and loop outs 
#[1,2,3].index(2) # => 1
#[1,2,3].index(4) # => ValueError

sw1 = LED(4)
sw2 = LED(17)
sw2 = LED(27)
sw2 = LED(22)

bt1 = Button(2)

URL = "http://192.168.0.100:8091/hitthebell"

def button_callback_bt1():
    print("Button was pushed!")
    try:
       requests.get(URL)
    except requests.exceptions.RequestException as e:  print(e)
   

bt1.when_pressed = button_callback_bt1


@app.route('/sw1/on')
def turn_led_on(gpionum):
    sw1.on()
    return "OK"

@app.route('/sw1/off')
def turn_led_off(gpionum):
    sw1.off()
    return "OK"


@app.route('/ha/sw1')
def haled(gpionum):
    if(sw1().is_lit):
      return  '{"active": "true"}'
    return  '{"active": "false"}'


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)
