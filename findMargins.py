import requests
import pickle

class marginfinder():
	headers = {
		'User-Agent': 'GE price forcasting project',
	}
	URL = "https://prices.runescape.wiki/api/v1/osrs/latest"
	def __init__(self):
		with open("itemList.txt" , "rb") as f:
			self.itemList = pickle.load(f)

	def run(self):
		self.dataSet = []

		r = requests.get(self.URL, headers=self.headers)
		itemID = ""

		for name, i, limit in self.itemList:	
			try:
				itemID = str(i)
				self.dataSet.append([r.json()["data"][itemID]["high"],r.json()["data"][itemID]["low"],name])
					
			except KeyError:
				pass

		
	def getData(self):

		return self.dataSet

