from flask import Flask
from flask_restful import Resource, Api, reqparse
from MySQLdb import *

import credentials

class Vehicles(Resource) :
	"""
	This class is used to handle any request towards the vehicles endpoint.
	
	GET and POST request are allowed.
	The answer to a GET request with no arguments is the full list of the cars.
	"""
	connection = connect(host=credentials.host,user=credentials.user,passwd=credentials.passwd)
	def get(self) :
		pass
		
	def post(self) :
		pass	
