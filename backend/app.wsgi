import sys
sys.path.insert(0, '/var/www/relay-flask-app')

activate_this = '/home/pi/.local/share/virtualenvs/relay-flask-app-xFPDQV2m/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application