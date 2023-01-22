#coding:utf-8
import os
import zipfile

def Updater(url="https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/updater_folder.zip", 
	name_folder="L4D2.Map.Selector.v1.2.zip", current_version_folder="ver.txt", current_version_to_folder="v1.2-21.01.23-05PM"):

	try:
		import requests

		if os.path.isfile(current_version_folder):
			with open("ver.txt", "r", encoding="utf-8") as ver_indicator:
				current = str(ver_indicator.readline())
				print("current version:", current)

		else:
			with open(current_version_folder, "a", encoding="utf-8") as ver_indicator:
				ver_indicator.write(current_version_to_folder)

			with open(current_version_folder, "r", encoding="utf-8") as ver_indicator:
				current = str(ver_indicator.readline())
				print("current version:", current)

		update = requests.get(url)
		open(name_folder, "wb").write(update.content)
		input("Updated files are succesfully installed you can extract and replace files install (press enter to quit):")

	except:
		print("Installing requests lib...")

		try:
			os.system("pip install requests")
			import requests

			if os.path.isfile(current_version_folder):
				with open(current_version_folder, "r", encoding="utf-8") as ver_indicator:
					current = str(ver_indicator.readline())
					print("current version:", current)

			else:
				with open(current_version_folder, "a", encoding="utf-8") as ver_indicator:
					ver_indicator.write(current_version_to_folder)
				
				with open(current_version_folder, "r", encoding="utf-8") as ver_indicator:
					current = str(ver_indicator.readline())
					print("current version:", current)

			update = requests.get(url)
			open(name_folder, "wb").write(update.content)
			input("installing lib and updated file are succesfully installed you can extract and replace files install (press enter to quit):")

		except:
			print("ERROR: pip is not installed or idk")
			input("")

Updater()