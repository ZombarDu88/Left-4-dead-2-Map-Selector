#coding:utf-8
import os

def Updater(url="https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/updater_folder.zip", 
	name_folder="L4D2.Map.Selector.v1.2.zip"):

	try:
		import requests

		update = requests.get(url)
		open(name_folder, "wb").write(update.content)
		input("Updated files are succesfully installed you can extract and replace files install (press enter to quit)")

	except:
		print("Installing requests lib...")

		try:
			os.system("pip install requests")
			import requests

			update = requests.get(url)
			open(name_folder, "wb").write(update.content)
			input("installing libs and updated file are succesfully installed you can extract and replace files install (press enter to quit)")

		except:
			print("ERROR: pip is not installed or idk")
			input("")

Updater()