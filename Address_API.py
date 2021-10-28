from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# To run the API run the python file and open the browser/postman app and paste the following URL:
# http://127.0.0.1:5000?addr=132, My Street, Kingston, New York 12401.

class Raw_Data(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('addr', required=True, type=str)  # add args

        args = parser.parse_args()

        return args, 200  # return args with 200 OK

api.add_resource(Raw_Data, '/')  # endpoint of api


if __name__ == '__main__':
    app.run(debug=True)  # run the flask app