import requests
import threading

class updater():
	headers = {
		'User-Agent': 'GE price forcasting project',
	}
	URL = "https://prices.runescape.wiki/api/v1/osrs/1h"

	def run(self):
		self.dataSet = []

		r = requests.get(self.URL, headers=self.headers)
		itemID = 0

		for itemID in range(25849):

			try:
				Currentpricediff = r.json()["data"][itemID]["avgHighPrice"] - r.json()["data"][itemID]["avgLowPrice"]
				Currentpricediff = Currentpricediff * (r.json()["data"][itemID]["avgHighVolume"] - r.json()["data"][itemID]["avgLowVolume"])

				self.dataSet.append([Currentpricediff, itemID])
			except:
				pass

	def findBest(self):

		sorted(self.dataSet, key=lambda x: x[0], reverse=True)

		return self.dataSet







