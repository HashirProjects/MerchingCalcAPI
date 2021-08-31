import requests
import threading
import pickle

class updater():
	headers = {
		'User-Agent': 'GE price forcasting project',
	}
	URL = "https://prices.runescape.wiki/api/v1/osrs/6h"
	def __init__(self):
		with open("itemList.txt" , "rb") as f:
			self.itemList = pickle.load(f)

	def run(self):
		self.dataSet = []

		r = requests.get(self.URL, headers=self.headers)
		itemID = 0

		for name, i, limit in self.itemList:

			itemID = str(i)
			try:
				score = r.json()["data"][itemID]["avgHighPrice"] - r.json()["data"][itemID]["avgLowPrice"]

				if score < 0:
					score = 0
				else:
					score *= min([(r.json()["data"][itemID]["highPriceVolume"] - r.json()["data"][itemID]["lowPriceVolume"]),limit])

				self.dataSet.append([score, name])

			except KeyError:
				pass

			except TypeError:
				self.dataSet.append([0,name + " (data missing)"])


	def getData(self):

		self.dataSet.sort(key=lambda x: x[0], reverse=True)

		return self.dataSet







