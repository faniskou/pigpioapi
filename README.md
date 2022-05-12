# pigpioapi
pigpioapi

run the app
 propably run on 5001  
you can run the api by running python3 pigpiopi.py

run on rasbian as a service
Use the above commands to install
sudo cp pigpiopi.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/pigpiopi.service
sudo systemctl daemon-reload
sudo systemctl enable pigpiopi.service
sudo systemctl start pigpiopi.service
sudo systemctl status pigpiopi.service
