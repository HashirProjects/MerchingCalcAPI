import update
import findMargins
import threading
import json
import time

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

def startUpdateThreads():
	def targetfuncDB():
		while True:
			updateDB()
			time.sleep(3600)

	def targetfuncM():
		while True:
			updateM()
			time.sleep(120)


	updateDB_thread = threading.Thread(target = targetfuncDB)
	updateDB_thread.start()

	updateM_thread = threading.Thread(target = targetfuncM)
	updateM_thread.start()
