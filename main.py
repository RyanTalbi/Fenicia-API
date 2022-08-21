from flask import Flask
from flask_restful import Resource, Api, reqparse
from Vehicles import Vehicles


app = Flask(__name__)
api = Api(app)
api.add_resource(Vehicles,'/vehicles')

if __name__ == '__main__' :
	app.run()
