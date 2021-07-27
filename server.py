# Imports
import time
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import qwiic_scmd
#import socketcontrol

myMotor = qwiic_scmd.QwiicScmd()

# Create API
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.event
def control(movement):
    if (movement == '0001'):
        #myMotor.set_drive(1, 0, 100)
        #myMotor.set_drive(0, 0, 100)
        print("forward")
    if(movement == '0010'):
        #myMotor.set_drive(1, 1, 100)
        #myMotor.set_drive(0, 1, 100)
        print("backward")
    if(movement == '0011'):
        #myMotor.set_drive(1, 1, 100)
        #myMotor.set_drive(0, 0, 100)
        print("left")
    if(movement == '0100'):
        #myMotor.set_drive(1, 0, 100)
        #myMotor.set_drive(0, 1, 100)
        print("right")
    if(movement == '0101'):
        #myMotor.set_drive(1, 0, 0)
        #myMotor.set_drive(0, 0, 0)
        print("stop")


def init_motor():
    if myMotor.connected == False:
        print("Controller not connected")
        return
    myMotor.begin()
    print("Controller initialized")
    time.sleep(.250)

    myMotor.set_drive(0, 0, 0)
    myMotor.set_drive(1, 0, 0)

    myMotor.enable()
    print("Controller enabled")
    time.sleep(.250)

# Start
if __name__ == '__main__':
    # init_motor()
    socketio.on_event('move', control)
    socketio.run(app, host="0.0.0.0")
