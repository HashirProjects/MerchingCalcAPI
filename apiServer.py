from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class test(Resource):
	def get(self):
		return {"message":"HI"}

api.add_resource(test, "/test")

if __name__ == "__main__":
	app.run()