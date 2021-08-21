from flask import Flask
from flask_restful import Api, Resource
import update
import json

app = Flask(__name__)
api = Api(app)

class topItemsList(Resource):
	def get(self):
		with open("database.json", "r") as file:
			response = file.read()
		return response

	def patch(self):
		Updater = update.updater()
		Updater.run()
		with open("database.json", "w") as file:
			json.dump(Updater.findBest(), file)

		return {"message", "successfully updated list"}, 201


api.add_resource(topItemsList, "/test")

if __name__ == "__main__":
	app.run()