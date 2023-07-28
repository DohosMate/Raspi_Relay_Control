from flask import Flask, request
from datetime import datetime
from os.path import isfile
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for i in range(1,9):
    GPIO.setup(int(i), GPIO.OUT)
    GPIO.output(int(i), GPIO.HIGH)



# create database to store the states of relay and log previous state
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# wrape it to CORS avoid frontend problems
CORS(app)
# configure the SQLite database, relative to the app folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# initialize the app with the extension
db.init_app(app)

class Relay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    state = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.id} . {self.state}'
    
if not isfile('instance\database.db'):
    print('First activation! Create database.db')
    with app.app_context():
        db.create_all()

@app.route('/')
def welcome():
    return 'A am the backend of Raspi Relay Controller'


@app.route('/<id>/on')
def relay_on(id):
    GPIO.output(int(id), GPIO.LOW)
    return {'relay on': str(id)}

@app.route('/<id>/off')
def relay_off(id):
    GPIO.output(int(id), GPIO.HIGH)
    return {'relay off': str(id)}


if __name__== '__main__':
    app.run()