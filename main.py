from flask import Flask
from flask_restful import Resource, Api, reqparse
from Vehicles import Vehicles
from Locations import Locations
from Users import Users
app = Flask(__name__)
api = Api(app)
api.add_resource(Vehicles,'/vehicles')
api.add_resource(Locations,'/locations')
api.add_resource(Users,'/users')
if __name__ == '__main__' :
	app.run()
