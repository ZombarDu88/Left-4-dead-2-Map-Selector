#coding:utf-8
import os
import zipfile

def Current_version_file(ver_file="ver.txt", current_ver_file="v1.2-19.04.2023-08PM"):

	if os.path.isfile(ver_file):
		with open("ver.txt", "r", encoding="utf-8") as ver_indicator:
			current = str(ver_indicator.readline())
			print("current version:", current)

	else:
		with open(ver_file, "a", encoding="utf-8") as ver_indicator:
			ver_indicator.write(current_ver_file)

		with open(ver_file, "r", encoding="utf-8") as ver_indicator:
			current = str(ver_indicator.readline())
			print("current version:", current)

def Updater(url="https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/updater_folder.zip", 
	name_folder="L4D2.Map.Selector.v1.2.zip"):

	try:
		import requests

		Current_version_file()

		update = requests.get(url)
		open(name_folder, "wb").write(update.content)
		input("Updated files are succesfully installed in -> "+os.getcwd()+"\nyou can extract and replace files install (press enter to quit):")

	except:
		print("Installing requests lib...")

		try:
			os.system("pip install requests")
			import requests

			Current_version_file()

			update = requests.get(url)
			open(name_folder, "wb").write(update.content)
			input("installing lib and updated file are succesfully installed in -> "+os.getcwd()+"\nyou can extract and replace files install (press enter to quit):")

		except:
			print("ERROR: pip is not installed or idk")
			input("")

Updater()