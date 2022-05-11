
try:
    from flask import Flask
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask import request
    from gpiozero import LED, Button
    from signal import pause
    import time
    import datetime
    import json
    import threading


led = LED(17)
button = Button(2)

# button.when_pressed = led.on
# button.when_released = led.off

