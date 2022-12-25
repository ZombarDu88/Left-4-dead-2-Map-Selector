#coding:utf-8
import pyautogui
import os
import time
import random
import getpass
import tkinter
import pygetwindow as gw
from tkinter import messagebox
from pypresence import Presence

def L4D2_State(*args):

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:
		messagebox.showinfo("Just checking...", "L4D2 is launched")
		print("\033[1;32msucces detect: left4dead2.exe\033[0;37m")
		var_l4D2.set(l4D2_True)

	else:
		messagebox.showerror("Just checking...", "L4D2 is not launched =(")
		print("\033[0;31mleft4dead2.exe is not launched\033[0;37m")
		var_l4D2.set(l4D2_False)

def Start_L4D2(Succes_cmd="\033[1;32mleft4dead2.exe is succefully started\033[0;37m", Detect_cmd="\033[1;32msucces detect: left4dead2.exe\033[0;37m"):

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:

		messagebox.showwarning("Just checking...", "L4D2 as already launched")
		print("left4dead2.exe: as already launched")
		var_l4D2.set("L4D2: as already launched")

	else:		
		Partition = os.popen("wmic logicaldisk where drivetype=3 get description ,deviceid ,volumename").read()
		User = getpass.getuser()

		try:
			if Partition.find("C:"):
				direction = os.startfile("C:/Users/"+User+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Left 4 Dead 2.url")
				time.sleep(15)
				print(Succes_cmd,"\n"+Detect_cmd)
				var_l4D2.set(l4D2_True)

			elif Partition.find("D:"):
				direction = os.startfile("D:/Users/"+User+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Left 4 Dead 2.url")
				time.sleep(15)
				print(Succes_cmd,"\n"+Detect_cmd)
				var_l4D2.set(l4D2_False)

		except:
			print("Left4Dead2 is not installed on data or ssd =(")
			var_l4D2.set("L4D2: is not installed on your computer =(")
			messagebox.showerror("Error !", "Left4Dead2 is not installed on data or ssd =(\nnot possible to start it")
			print("\033[0;31mleft4dead2.exe is not launched\033[0;37m")
			var_l4D2.set(l4D2_False)

def Spin():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:
		Python = gw.getActiveWindow()

		with open("setting.txt", "r" , encoding="utf-8") as Action_Time:
			Action_Time.seek(45)
			Time_Spin = float(Action_Time.readline())

		pyautogui.moveTo(5000, 5000)

		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()
		time.sleep(Time_Spin)

		maps = random.randrange(0, 90)
		maps_str = str(maps)
		print("Spin=",maps_str+"/90")

		pyautogui.moveTo(5000, 5000)
		pyautogui.press("enter")

		if maps >= 20:
			maps_majority = int(maps / 1.3)
			maps_final = maps - maps_majority -3

			for i in range(maps_majority):
				pyautogui.press("down")

			for i in range(maps_final):
				time.sleep(0.050)
				pyautogui.press("down")

			for i in range(3):
				time.sleep(0.50)
				pyautogui.press("down")
						
		elif maps <= 19:
			maps_reduce = maps -3

			for i in range(maps_reduce):
				pyautogui.press("down")

			for i in range(3):
				time.sleep(0.50)
				pyautogui.press("down")

		elif maps <= 5:

			for i in range(maps):
				time.sleep(0.50)
				pyautogui.press("down")
						
		#pyautogui.hotkey("win", "prntscrn") #screen function for send to your friend disabled.
		pyautogui.press("enter")
		var_l4D2.set(l4D2_True)
		time.sleep(2)
		
		Python.activate()

	else:
		Spin_message = messagebox.askquestion("Can't Spin", "You can't spin L4D2 is not launched start L4D2 ?")

		if Spin_message == "yes":
			Start_L4D2()

		else:
			print("\033[0;31mleft4dead2.exe is not launched\033[0;37m")
			var_l4D2.set("You can't spin L4D2: is not launched")

def Return_to_game():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()

	else:
		Return_game_message = messagebox.askquestion("Can't Return To Game", "You can't return to game L4D2 is not launched start L4D2 ?")

		if Return_game_message == "yes":
			Start_L4D2()

		else:
			print("\033[0;31mleft4dead2.exe is not launched\033[0;37m")
			var_l4D2.set("You can't return to game L4D2: is not launched")

def Finish_random():

	L4D2_is_launched = os.popen("wmic process get description").read()

	if L4D2_is_launched.find("left4dead2.exe") != -1:

		with open("setting.txt", "r" , encoding="utf-8") as Action_Time:
			Action_Time.seek(45)
			Time_End = float(Action_Time.readline())

		pyautogui.moveTo(5000, 5000)
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]

		L4D2_window.maximize()
		time.sleep(Time_End)
		pyautogui.press("esc")
		var_l4D2.set(l4D2_True)

	else:
		Spin_message = messagebox.askquestion("Can't Finish Spin", "You can't finish spin L4D2 is not launched start L4D2 ?")

		if Spin_message == "yes":
			Start_L4D2()

		else:
			print("\033[0;31mleft4dead2.exe is not launched\033[0;37m")
			var_l4D2.set("You can't finish spin L4D2: is not launched")

def Discord_Rpc():

	epoch_time = int(time.time())
	output_discord = os.popen("wmic process get description").read()

	if output_discord.find("Discord.exe") != -1:

		client_id = "No XD"
		Rpc = Presence(client_id)
		Rpc.connect()

		Rpc.update()

	else:
		print("\033[0;31mDiscord is not launched no rpc\033[0;37m")

def Quitting_Program():

	Quit_Program = messagebox.askquestion("Quit", "Are you sure ?")

	if Quit_Program == "yes":

		L4D2_is_launched = os.popen("wmic process get description").read()

		if L4D2_is_launched.find("left4dead2.exe") != -1:
			
			L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
			L4D2_window.maximize()
			quit()
	
		else:
			quit()

def Credits():
	messagebox.showinfo("L4D2 Map Selector Credits", "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")

l4D2_True="L4D2: is launched =)" 
l4D2_False="L4D2: is not launched =("

Discord_Rpc()
mainapp = tkinter.Tk()

os.system("color")
pyautogui.FAILSAFE = False

photo = tkinter.PhotoImage(file = "Pictures/icon.png")
mainapp.wm_iconphoto(False, photo)

mainapp.title("L4D2 Map Selector v1.1.5")
mainapp.geometry("+300+300")
mainapp.configure(bg="grey")

with open("setting.txt", "r" , encoding="utf-8") as Action_Time:
	Action_Time.seek(45)
	Time_Spin_End = Action_Time.readline()

label_welcome = tkinter.Label(mainapp, bg="grey", text="Welcome to L4D2 Map Selector v1.1.5")
label_welcome.pack()

label_space = tkinter.Label(mainapp, bg="grey", text="---")
label_space.pack()

buttom_spin = tkinter.Button(mainapp, text="Spin", width=25, command=Spin)
buttom_spin.pack()

button_Return_Game = tkinter.Button(mainapp, text="Return to game", width=20, command=Return_to_game)
button_Return_Game.pack()

space = tkinter.Label(mainapp, bg="grey", text="---")
space.pack()

button_End = tkinter.Button(mainapp, text="Finish Esc", width=17, command=Finish_random)
button_End.pack()

button_Credits = tkinter.Button(mainapp, text="Credits", width=10, command=Credits)
button_Credits.pack()

label_space2 = tkinter.Label(mainapp, bg="grey", text="---")
label_space2.pack()

buttom_check = tkinter.Button(mainapp, text="Check L4D2 is launched", width=25, command=L4D2_State)
buttom_check.pack()

buttom_Start_L4D2 = tkinter.Button(mainapp, text="Start L4D2", width=17, bg="#00ff00", command=Start_L4D2)
buttom_Start_L4D2.pack()

buttom_quit = tkinter.Button(mainapp, text="Quit Program", bg="#ff0000", command=Quitting_Program)
buttom_quit.pack()

label_space3 = tkinter.Label(mainapp, bg="grey", text="")
label_space3.pack()

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", L4D2_State)
label_stat = tkinter.Label(mainapp, bg="grey", textvariable=var_l4D2)
label_stat.pack()

mainapp.mainloop()
