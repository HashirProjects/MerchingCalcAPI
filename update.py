import requests
import pickle
import numpy as np

class updater():
	headers = {
		'User-Agent': 'GE price forcasting project',
	}
	URL = "https://prices.runescape.wiki/api/v1/osrs/1h"
	def __init__(self):
		with open("itemList.txt" , "rb") as f:
			self.itemList = pickle.load(f)

	def run(self):

		def gaussian(x):
			return np.exp(-np.power(x - 1.75, 2.) / (2 * np.power(0.25, 2.)))

		self.dataSet = []

		r = requests.get(self.URL, headers=self.headers)
		itemID = ""

		for name, i, limit in self.itemList:

			itemID = str(i)
			try:#filter using the avg low price
				score = (r.json()["data"][itemID]["avgHighPrice"] - r.json()["data"][itemID]["avgLowPrice"])

				highPriceVolume = r.json()["data"][itemID]["highPriceVolume"]
				lowPriceVolume = r.json()["data"][itemID]["lowPriceVolume"]

				multiplier = 1 + gaussian(highPriceVolume / lowPriceVolume) * np.log(min([highPriceVolume,limit])) # maybe ln(highpricevolume) would be better so that high values dont skew
				
				score *= multiplier

				self.dataSet.append([score, name, highPriceVolume, lowPriceVolume])

			except KeyError:
				pass

			except TypeError:
				self.dataSet.append([0,name + " (data missing)"])


	def getData(self):

		self.dataSet.sort(key=lambda x: x[0], reverse=True)

		return self.dataSet







