from flask import Flask
from flask_restful import Api, Resource
import json
import time
from main import updateM, startUpdateThreads

app = Flask(__name__)
api = Api(app)

class topItemsList(Resource):
	def get(self):
		try:
			with open("database.json", "r") as file:
				response = json.load(file)
		except json.decoder.JSONDecodeError:
			return {"message": "Margins are currently being updated, please wait"}
		return response


class getMargins(Resource):
	def get(self, name):
		try:	
			with open("margins.json", "r") as file:
				response = json.load(file) # json decoder error
		except json.decoder.JSONDecodeError:
			return {"message": "Margins are currently being updated, please wait"}

		print(name)
		margin = [0,0,"Item Not Found"]

		for item in response:
			if item[2] == name:
				margin = item

		return margin
		
class updateMargins(Resource):
	def patch(self):
		updateM()

		return {"message":"Successfully Patched"}, 201


api.add_resource(topItemsList, "/getItemScores")
api.add_resource(getMargins, "/getMargin/<string:name>")
api.add_resource(updateMargins, "/findLatestMargins")

if __name__ == "__main__":

	startUpdateThreads()

	app.run()