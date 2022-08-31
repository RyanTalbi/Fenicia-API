from flask import Flask, json
from flask_restful import Resource, Api, reqparse
from MySQLdb import *
import credentials

class Vehicles(Resource) :
	"""
	This class is used to handle any request towards the vehicles endpoint.
	
	GET and POST request are allowed.
	The answer to a GET request with no arguments is the full list of the cars.
	
	A POST request must specify each attribute value except "CheminImage"
	"""
	
	connection = connect(host=credentials.host,user=credentials.user,passwd=credentials.password,db="location")
	connectionCursor = connection.cursor()
	
	
	def buildSQLRequest(sqlTemplate, parsedArguments) :
		# Building concrete SQL request arguments ( replace each unspecified argument by a wildcard matching any corresponding column value ) 
		sqlArguments = []
		for attribute in parsedArguments :
			if parsedArguments[attribute] == None :
				sqlArguments.append(attribute) 
			else :
				sqlArguments.append("'"+parsedArguments[attribute]+"'")	
		return sqlTemplate.format(*sqlArguments)
	
	def get(self) :
		connectionCursor = self.connection.cursor()
		parser = reqparse.RequestParser()
		
		parser.add_argument("PlaqueVehicule",location='args',required=False)
		parser.add_argument("ModeleVehicule",location='args',required=False)
		parser.add_argument("NumCGVehicule",location='args',required=False)
		parser.add_argument("MarqueVehicule",location='args',required=False)
		parser.add_argument("AnneeVehicule",location='args',required=False)
		parser.add_argument("CouleurVehicule",location='args',required=False)
		parser.add_argument("LoyerVehicule",location='args',required=False)
		parser.add_argument("BoiteVitesse",location='args',required=False)
		parser.add_argument("NombrePlaces",location='args',required=False)
		parser.add_argument("NombrePortes",location='args',required=False)
		parser.add_argument("Carburant",location='args',required=False)
		parser.add_argument("Constructeur",location='args',required=False)
		parser.add_argument("Kilometrage",location='args',required=False)
		parser.add_argument("GPS",location='args',required=False)
		parser.add_argument("AirConditionne",location='args',required=False)
		parser.add_argument("Audio",location='args',required=False)
		
		parsedArguments = parser.parse_args()
		sqlRequest = buildSQLRequest("SELECT * FROM Voitures WHERE PlaqueVehicule LIKE {} AND ModeleVehicule LIKE {} AND NumCGVehicule LIKE {} AND MarqueVehicule LIKE {} AND AnneeVehicule = {} AND CouleurVehicule LIKE {} AND LoyerVehicule LIKE {} AND BoiteVitesse LIKE {} AND NombrePlaces = {} AND NombrePortes LIKE {} AND Carburant LIKE {} AND Constructeur LIKE {} AND Kilometrage <= {} AND GPS = {} AND AirConditionne = {} AND Audio = {} ",parsedArguments)
		connectionCursor.execute(sqlRequest)
		rows = connectionCursor.fetchall()
		columns = [column[0] for column in connectionCursor.description]
		jsonResult = []
		for row in rows :
			jsonResult.append(dict(zip(columns, row)))
		return json.jsonify(jsonResult)
		
	def post(self) :
		connectionCursor = self.connection.cursor()
		parser = reqparse.RequestParser()
		parser.add_argument("PlaqueVehicule",location='args',required=True)
		parser.add_argument("ModeleVehicule",location='args',required=True)
		parser.add_argument("NumCGVehicule",location='args',required=True)
		parser.add_argument("MarqueVehicule",location='args',required=True)
		parser.add_argument("AnneeVehicule",location='args',required=True)
		parser.add_argument("CouleurVehicule",location='args',required=True)
		parser.add_argument("LoyerVehicule",location='args',required=True)
		parser.add_argument("BoiteVitesse",location='args',required=True)
		parser.add_argument("NombrePlaces",location='args',required=True)
		parser.add_argument("NombrePortes",location='args',required=True)
		parser.add_argument("Carburant",location='args',required=True)
		parser.add_argument("Description",location='args',required=True)
		parser.add_argument("Constructeur",location='args',required=True)
		parser.add_argument("Kilometrage",location='args',required=True)
		parser.add_argument("GPS",location='args',required=True)
		parser.add_argument("AirConditionne",location='args',required=True)
		parser.add_argument("Audio",location='args',required=True)
		
		parsedArguments = parser.parse_args()
		connectionCursor.execute(buildSQLRequest("INSERT INTO Voitures VALUES({},{},{},{},{},{},{},'NULL',{},{},{},{},{},{},{},{},{},{})",parsedArguments)))
		self.connection.commit()		
		return 200	
	
