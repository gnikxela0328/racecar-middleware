# Imports
from flask import Flask
from flask_restful import Resource, Api, reqparse
#import qwiic_scmd

# Create API
app = Flask(__name__)
api = Api(app)

# Endpoints
class Control(Resource):

    def get(self):
        return {'message': 'post to control'}, 200
    pass

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('controlType', required=True)
        
        args = parser.parse_args()
        
        #print(args['controlType'])
        
        if(args['controlType'] == 'accel'):
            print('forward')
        if(args['controlType'] == 'stop'):
            print('stop')
        if(args['controlType'] == 'reverse'):
            print('back')
        if(args['controlType'] == 'left'):
            print('left')
        if(args['controlType'] == 'right'):
            print('right')
        
        
        
        return {'status': 'recieved'}, 200
    pass

# Add route
api.add_resource(Control, "/control")

# Start
if __name__ == '__main__':
    app.run()