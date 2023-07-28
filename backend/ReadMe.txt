pip freeze > requirements.txt

install apache2 
https://www.youtube.com/watch?v=Oy52MqsWQdM&list=PLDvInfB8ki_IuB1yuDEZMaCmau50qrVzD&index=12&t=89s

deploy a Flask app on Raspi
https://www.youtube.com/watch?v=w0QDAg85Oow&list=PLDvInfB8ki_IuB1yuDEZMaCmau50qrVzD&index=11
Solution:
    RPi.GPIO: RuntimeError: No access to /dev/mem. Try running as root!
    User getting removed from group after reboot --> run sudo chmod 777 in rc.local startup
pi@raspberrypi:~ $ sudo nano /etc/rc.local
pi@raspberrypi:~ $ sudo chmod 777 /dev/gpiomem
pi@raspberrypi:~ $ sudo chmod 777 /dev/mem
