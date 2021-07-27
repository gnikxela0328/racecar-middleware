from flask_restful import Resource, reqparse
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

# Endpoints
class Control(Resource):

    def get(self):
        return {'message': 'post to control'}, 200
    pass

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('controlType', required=True)

        args = parser.parse_args()

        # print(args['controlType'])

        if(args['controlType'] == 'accel'):
            myMotor.set_drive(1, 0, 100)
            myMotor.set_drive(0, 0, 100)
        if(args['controlType'] == 'reverse'):
            myMotor.set_drive(1, 1, 100)
            myMotor.set_drive(0, 1, 100)
        if(args['controlType'] == 'left'):
            myMotor.set_drive(1, 1, 100)
            myMotor.set_drive(0, 0, 100)
        if(args['controlType'] == 'right'):
            myMotor.set_drive(1, 0, 100)
            myMotor.set_drive(0, 1, 100)
        if(args['controlType'] == 'stop'):
            myMotor.set_drive(1, 0, 0)
            myMotor.set_drive(0, 0, 0)

        return {'status': 'recieved'}, 200
    pass
    