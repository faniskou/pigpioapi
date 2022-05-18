from gpiozero import LED, Button
import requests

from flask import Flask
app = Flask(__name__)

# TODO

list_in = [LED(4),LED(17),LED(27),LED(22)]
list_out = [Button(2)]
list_out_http =  ["http://192.168.0.100:8091/hitthebell"]
# add in status 
# check in is in the list and loop outs 
#[1,2,3].index(2) # => 1
#[1,2,3].index(4) # => ValueError

def button_callback_bt1(i =0):
    print("Button was pushed!")
    try:
       requests.get(list_out_http(i))
    except requests.exceptions.RequestException as e:  print(e)
   

list_out[0].when_pressed = button_callbackbt(0)


@app.route('/sw1/on')
def turn_led_on():
    list_in[0].on()
    return "OK"

@app.route('/sw1/off')
def turn_led_off():
    list_in[0].off()
    return "OK"


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)

