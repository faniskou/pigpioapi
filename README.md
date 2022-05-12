# pigpioapi
pigpioapi

run the app
 propably run on 5001  
you can run the api by running python3 pigpio.py

run on rasbian as a service
Use the above commands to install
sudo cp pigpio.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/pigpio.service
sudo systemctl daemon-reload
sudo systemctl enable pigpio.service
sudo systemctl start pigpio.service
sudo systemctl status pigpio.service
