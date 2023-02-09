#coding:utf-8
import os

def Libs_installer(Enter_message="press enter:"):
	try:	
		import pyautogui
		import pygetwindow
		import requests
		from pypresence import Presence

		print("Required libs are alerty installed you can launch the program =)")
		input(Enter_message)
	
	except:
		print("Installing libs...")

		try:
			os.system("pip install pyautogui")
			os.system("pip install pygetwindow")
			os.system("pip install pypresence")
			os.system("pip install requests")

			print("Required libs are installed you can launch the program =)")
			input(Enter_message)

		except:
			print("ERROR: pip is not installed or idk")
			input(Enter_message)

Libs_installer()