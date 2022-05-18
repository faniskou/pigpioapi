from gpiozero import LED, Button
import requests

from flask import Flask
app = Flask(__name__)

# TODO

list_in = {4:LED(4),17:LED(17),27:LED(27),22:LED(22)}
list_out = {2:"http://192.168.0.100:8091/hitthebell"}
list_out_http =  []
# add in status 
# check in is in the list and loop outs 
#[1,2,3].index(2) # => 1
#[1,2,3].index(4) # => ValueError


bt1 = Button(2)

URL = "http://192.168.0.100:8091/hitthebell"

def button_callback_bt1():
    print("Button was pushed!")
    try:
       requests.get(list_out[2])
    except requests.exceptions.RequestException as e:  print(e)
   

bt1.when_pressed = button_callback_bt1


@app.route('/<gpionum>/on')
def turn_led_on(gpionum: int):
    list_in[4].on()
    return "OK"

@app.route('/<gpionum>/off')
def turn_led_off(gpionum: int):
    ist_in[4].off()
    return "OK"


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)
