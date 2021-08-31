from flask import Flask
from flask_restful import Api, Resource
import update
import json
import threading

app = Flask(__name__)
api = Api(app)

def updateDB():
	Updater = update.updater()
	Updater.run()
	with open("database.json", "w") as file:
		json.dump(Updater.getData(), file)


class topItemsList(Resource):
	def get(self):
		with open("database.json", "r") as file:
			response = json.load(file)
		return response

	def patch(self):
		updateDB()

		return {"message", "successfully updated list"}, 201


api.add_resource(topItemsList, "/ItemScores")

if __name__ == "__main__":
	import time

	def targetfunc():
		while True:
			updateDB()
			time.sleep(3600)

	update_thread = threading.Thread(target = targetfunc)
	update_thread.start()

	app.run()