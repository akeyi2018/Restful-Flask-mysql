from flask import Flask, request, send_from_directory
from flask_restful import Resource, Api
from mysql_test import WORD_POOL
import os

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        ins = WORD_POOL()
        res = ins.get_rec()
        return res
    def post(self):
        json = request.get_json()
        return {'you post' : json}, 200

api.add_resource(HelloWorld,'/')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
