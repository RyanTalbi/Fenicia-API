from flask import Flask, json
from flask_restful import Resource, Api, reqparse
from MySQLdb import *
import credentials


class Locations(Resource) : 
	"""
	This class is used to handle any request towards the locations endpoint.
	
	GET and POST request are allowed.
	The answer to a GET request with no arguments is the full list of the locations since the beginning of the service.
	"""
	connection = connect(host=credentials.host,user=credentials.user,passwd=credentials.password,db="location")
		
	def get(self) :
		connectionCursor = self.connection.cursor()
		parser = reqparse.RequestParser()
		parser.add_argument("PlaqueVehicule",location='args',required=False)
		parser.add_argument("DebutLocation",location='args',required=False)
		parser.add_argument("FinLocation",location='args',required=False)
		parser.add_argument("DureeLocation",location='args',required=False)
		parser.add_argument("TypeParking",location='args',required=False)
		
		parsedArguments = parser.parse_args()
		sqlArguments = []
		for attribute in parsedArguments :
			if parsedArguments[attribute] == None :
				sqlArguments.append(attribute) 
			else :
				sqlArguments.append("'"+parsedArguments[attribute]+"'")
				
				
		connectionCursor.execute("SELECT * FROM Locations WHERE PlaqueVehicule LIKE {} AND DebutLocation >= {} AND FinLocation <= {} AND DureeLocation = {}".format(*sqlArguments))
		rows = connectionCursor.fetchall()
		columns = [column[0] for column in connectionCursor.description]
		jsonResult = []
		for row in rows :
			jsonResult.append(dict(zip(columns, row)))
		return json.jsonify(jsonResult)	
