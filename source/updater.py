#coding:utf-8
import os

try:
	import requests

	update = requests.get("https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/master.zip")
	open("L4D2.Map.Selector.v1.2.zip", "wb").write(update.content)
	input("Updated files are succesfully installed you can extract and replace files install (press enter to quit)")

except:
	print("Installing requests lib...")

	try:
		os.system("pip install requests")
		import requests

		update = requests.get("https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/master.zip")
		open("L4D2.Map.Selector.v1.2.zip", "wb").write(update.content)
		input("instaling libs and updated file are succesfully installed you can extract and replace files install (press enter to quit)")

	except:
		print("ERROR: pip is not installed or idk")
		input("")