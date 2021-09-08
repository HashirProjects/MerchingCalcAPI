from flask import Flask
from flask_restful import Api, Resource
import update
import json
import threading
import findMargins

app = Flask(__name__)
api = Api(app)

def updateDB():
	Updater = update.updater()
	Updater.run()
	with open("database.json", "w") as file:
		json.dump(Updater.getData(), file)
	print("Updated Prices")

def updateM():
	marginsfinder = findMargins.marginfinder()
	marginsfinder.run()

	with open("margins.json", "w") as file:
		json.dump(marginsfinder.getData(), file)
	print("Updated Margins")


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


api.add_resource(topItemsList, "/ItemScores")
api.add_resource(getMargins, "/getMargin/<string:name>")
api.add_resource(updateMargins, "/findLatestMargins")

if __name__ == "__main__":
	import time

	def targetfuncDB():
		while True:
			updateDB()
			time.sleep(21600)

	def targetfuncM():
		while True:
			updateM()
			time.sleep(120)


	updateDB_thread = threading.Thread(target = targetfuncDB)
	updateDB_thread.start()

	updateM_thread = threading.Thread(target = targetfuncM)
	updateM_thread.start()

	app.run()