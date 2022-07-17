from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from mysql_test import WORD_POOL
import settings

NM = settings.NM
KEY = settings.KEY
PD = settings.PD
   
app = Flask(__name__)
api = Api(app)


class HelloWorld_1(Resource):
    def get(self):
        # ins = WORD_POOL()
        # res = ins.get_rec()
        return 'OK'
    def post(self):
        json = request.get_json()
        return {'you post' : json}, 200

class HelloWorld_2(Resource):
    def get(self):
        # ins = WORD_POOL()
        # res = ins.get_rec()
        return 'OK'
    def post(self):
        json = request.get_json()
        return {'you post' : json}, 200

api.add_resource(HelloWorld_2,'/s_1')

api.add_resource(HelloWorld_1,'/s_2')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
