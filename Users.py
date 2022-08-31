from flask import Flask, json
from flask_restful import Resource, Api, reqparse
from MySQLdb import *
import credentials

class Users(Resource) :
	connection = connect(host=credentials.host,user=credentials.user,passwd=credentials.password,db="location")
	def get(self) : 
		connectionCursor = self.connection.cursor()
		parser = reqparse.RequestParser()
		parser.add_argument("Email",location='args',required=False)
		parser.add_argument("Nom",location='args',required=False)
		parser.add_argument("Prenom",location='args',required=False)
		parser.add_argument("Rue",location='args',required=False)
		parser.add_argument("Ville",location='args',required=False)
		parser.add_argument("NumPermis",location='args',required=False)
		parser.add_argument("Telephone",location='args',required=False)
		parser.add_argument("SIREN",location='args',required=False)
		parser.add_argument("Administrateur",location='args',required=False)
		parser.add_argument("Approuve",location='args',required=False)
		
		parsedArguments = parser.parse_args()
		sqlArguments = []
		for attribute in parsedArguments :
			if parsedArguments[attribute] == None :
				sqlArguments.append(attribute) 
			else :
				sqlArguments.append("'"+parsedArguments[attribute]+"'")
		print(sqlArguments)		
		connectionCursor.execute("SELECT Email, Nom, Prenom, Rue, Ville, NumPermis, SIREN, Telephone, Administrateur, Approuve FROM Clients WHERE Email LIKE {} AND Nom >= {} AND Prenom <= {} AND Rue = {} AND Ville = {} AND Telephone = {} AND Administrateur = {} AND Approuve = {}".format(*sqlArguments))
		rows = connectionCursor.fetchall()
		columns = [column[0] for column in connectionCursor.description]
		jsonResult = []
		for row in rows :
			jsonResult.append(dict(zip(columns, row)))
		return json.jsonify(jsonResult)					
	
	def post(self) :
		connectionCursor = self.connection.cursor()
		parser = reqparse.RequestParser()
		parser.add_argument("Email",location='args',required=True)
		parser.add_argument("Nom",location='args',required=True)
		parser.add_argument("Prenom",location='args',required=True)
		parser.add_argument("Rue",location='args',required=True)
		parser.add_argument("Ville",location='args',required=True)
		parser.add_argument("NumPermis",location='args',required=True)
		parser.add_argument("Telephone",location='args',required=True)
		parser.add_argument("MOTDEPASSE",location='args',required=True)
		parser.add_argument("SIREN",location='args',required=True)
		parser.add_argument("Administrateur",location='args',required=True)
		parser.add_argument("Approuve",location='args',required=True)
		
		parsedArguments = parser.parse_args()
		sqlArguments = []
		for attribute in parsedArguments :
			if parsedArguments[attribute] == None :
				sqlArguments.append(attribute) 
			else :
				sqlArguments.append("'"+parsedArguments[attribute]+"'")
				
		connectionCursor.execute("INSERT INTO Clients VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(*sqlArguments))		
		return 200
		
