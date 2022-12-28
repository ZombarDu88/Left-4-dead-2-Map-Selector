#coding:utf-8
import os

try:	
	import pyautogui
	import pygetwindow
	from pypresence import Presence

	sucess = print("Required lib are alerty installed you can launch the program =)")
	input("")
	
except:
	fail = print("Installing libs...")

	os.system("pip install pyautogui")
	os.system("pip install pygetwindow")
	os.system("pip install pypresence")

	print("Required lib are installed you can launch the program =)")
	input("")