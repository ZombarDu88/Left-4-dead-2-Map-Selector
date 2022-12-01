#coding:utf-8
import pyautogui
import os
import time
import random
import getpass
import tkinter
import pygetwindow as gw
from tkinter import messagebox

def Start_L4D2():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:

		print("left4dead2.exe: as already launched")
		var_l4D2.set("L4D2: as already launched")

	else:		
		Partition = os.popen("wmic logicaldisk where drivetype=3 get description ,deviceid ,volumename").read()
		User = getpass.getuser()

		if Partition.find("C:"):
			direction = os.startfile("C:/Users/"+User+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Left 4 Dead 2.url")
			time.sleep(5)
			print("\033[1;32mleft4dead2.exe is succefully started\033[0;37m")
			L4D2_State()

		elif Partition.find("D:"):
			direction = os.startfile("D:/Users/"+User+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Left 4 Dead 2.url")
			time.sleep(5)
			print("\033[1;32mleft4dead2.exe is succefully started\033[0;37m")
			L4D2_State()

		else:
			print("Left4Dead2 is not installed on data or ssd =(")
			L4D2_State()

def only_selection():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:

		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		Python = gw.getActiveWindow()

		pyautogui.moveTo(5000, 5000)
		maps = random.randrange(0, 90)
		L4D2_window.maximize()

		time.sleep(5.5)
		pyautogui.press("enter")

		for i in range(maps):
			pyautogui.press("down")

		#pyautogui.hotkey("win", "prntscrn")
		pyautogui.press("enter")
		time.sleep(2)

		var_l4D2.set("L4D2: is launched =)")
		Python.activate()
		
	else:
		var_l4D2.set("You can't spin L4D2: is not launched")

def L4D2_State(*args):

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:
		print("\033[1;32msucces detect: left4dead2.exe\033[0;37m")
		var_l4D2.set("L4D2: is launched =)")

	else:
		print("\033[0;31mleft4dead2.exe is not launched or not installed =(\033[0;37m")
		var_l4D2.set("L4D2: is not launched =(")

def Finish_random():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:

		pyautogui.moveTo(5000, 5000)
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]

		L4D2_window.maximize()
		time.sleep(3)
		pyautogui.press("esc")
		var_l4D2.set("L4D2: is launched =)")

	else:
		var_l4D2.set("You can't finish spin L4D2: is not launched")
		
def Quitting_Program():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()
		quit()
	
	else:
		quit()

def Credits():

	messagebox.showinfo("L4D2 Map Selector Credits", "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT")

mainapp = tkinter.Tk()
os.system("color")

pyautogui.FAILSAFE = False

photo = tkinter.PhotoImage(file = "Pictures/icon.png")
mainapp.wm_iconphoto(False, photo)

mainapp.title("L4D2 Map Selector v1.1")
#mainapp.geometry("300x250+200+200")

label_welcome = tkinter.Label(mainapp, text="Welcome to L4D2 Map Selector v1.1")
label_welcome.pack()

label_space = tkinter.Label(mainapp, text="---")
label_space.pack()

buttom_spin = tkinter.Button(mainapp, text="Spin", width=25, command=only_selection)
buttom_spin.pack()

button_End = tkinter.Button(mainapp, text="Finish", width=17, command=Finish_random)
button_End.pack()

button_Credits = tkinter.Button(mainapp, text="Credits", width=10, command=Credits)
button_Credits.pack()

label_space2 = tkinter.Label(mainapp, text="---")
label_space2.pack()

buttom_check = tkinter.Button(mainapp, text="Check L4D2 is launched", width=25, command=L4D2_State)
buttom_check.pack()

buttom_Start_L4D2 = tkinter.Button(mainapp, text="Start L4D2", width=17, command=Start_L4D2)
buttom_Start_L4D2.pack()

buttom_quit = tkinter.Button(mainapp, text="Quit Program", command=Quitting_Program)
buttom_quit.pack()

label_space3 = tkinter.Label(mainapp, text="")
label_space3.pack()

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", L4D2_State)
label_stat = tkinter.Label(mainapp, textvariable=var_l4D2)
label_stat.pack()

mainapp.mainloop()