import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

class Control():

    def forward():
        myMotor.set_drive(1, 0, 100)
        myMotor.set_drive(0, 0, 100)
        print("move forward")

    def backward():
        myMotor.set_drive(1, 1, 100)
        myMotor.set_drive(0, 1, 100)
        print("move forward")

    def left():
        myMotor.set_drive(1, 1, 100)
        myMotor.set_drive(0, 0, 100)
        print("move forward")

    def right():
        myMotor.set_drive(1, 0, 100)
        myMotor.set_drive(0, 1, 100)
        print("move forward")

    def stop():
        myMotor.set_drive(1, 0, 0)
        myMotor.set_drive(0, 0, 0)
        print("move forward")
