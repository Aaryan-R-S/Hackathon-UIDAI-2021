from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import declutter

app = Flask(__name__)
api = Api(app)

# To run the API, run the python file and open the browser/postman app and paste the following URL:
# http://127.0.0.1:5000/?raw=A Block, 108, Nawada, Gulab Bagh, Nawada, Uttam Nagar, West Delhi, Delhi, Delhi - 110059

all_cities = []         # stores all cities of India
all_districts = []      # stores all districts of India
all_states = []         # stores all states of India

def readData():
    global all_cities
    global all_districts
    global all_states
    
    f1 = open('data/allCities.json')
    all_cities = json.load(f1)
    f1.close()
    
    f1 = open('data/allDistricts.json')
    all_districts = json.load(f1)
    f1.close()

    f1 = open('data/allStates.json')
    all_states = json.load(f1)
    f1.close()

    return

class Raw_Data(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        
        # taking raw address as input in the API
        myArgName = 'raw'
        parser.add_argument(myArgName, required=True, type=str)  # add args
        args = parser.parse_args()
        
        # out is the final formatted address or error message to show
        out = dict()
        out['Raw Address'] = args[myArgName]
        addr_or_error, verdict = declutter.declutter(all_cities, all_districts, all_states, args[myArgName])

        if verdict == -1:
            out['Error message'] = addr_or_error
        else:
            out['Formatted Address'] = addr_or_error
            
        return out, 200  # return args with 200 OK

api.add_resource(Raw_Data, '/')  # endpoint of api

if __name__ == '__main__':
    readData()           # read json files in data folder
    app.run(debug=True)  # run the flask app