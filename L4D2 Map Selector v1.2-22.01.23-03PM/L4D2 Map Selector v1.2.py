#coding:utf-8
import tkinter
from tkinter import messagebox
from Py_folder.L4D2_presence import *
import webbrowser
import random
import pyautogui as gui
import pygetwindow as gw

def L4D2_State(*args):

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		messagebox.showinfo("Just checking...", "L4D2 is launched")
		print(cmd_detect_True)
		var_l4D2.set(l4D2_True)

	else:
		messagebox.showerror("Just checking...", "L4D2 is not launched =(")
		print(cmd_detect_False)
		var_l4D2.set(l4D2_False)

def Start_L4D2(Succes_start_cmd="\033[1;32mSucces detect: left4dead2.exe\n\033[1;32mleft4dead2.exe is succefully started\033[0;37m"):
	
	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		messagebox.showwarning("Just checking...", "L4D2 as already launched")
		print("\033[0;33mleft4dead2.exe: as already launched\033[0;37m")
		var_l4D2.set("L4D2: as already launched")

	else:
		CMD.restore()
		print("Whait... test if left4dead2.exe is launched in 20 tries")
		webbrowser.open("steam://rungameid/550")

		for i in range(20):
			L4D2_is_launched = os.popen(Wmic_comand).read()

			if L4D2_is_launched.find(Game) != -1:
				L4D2_launched = True
				print(Succes_start_cmd)
				var_l4D2.set(l4D2_True)
				time.sleep(5)
				CMD.minimize()
				Python_Ui.restore()
				break

			else:
				L4D2_launched = False
				print("left4dead2.exe not detect")

			time.sleep(2)

		if L4D2_launched == False:
			print("\033[0;31mLeft4Dead2 is not installed\033[0;37m")
			Python_Ui.activate()
			messagebox.showerror("Error !", "Left4Dead2 is not installed on your pc =(\nnot possible to start it")
			var_l4D2.set("L4D2: is not installed on your computer =(")

def Quit_L4D2():

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		os.system(Wmic_quit_comand)
		var_l4D2.set(l4D2_False)
		messagebox.showinfo("Quit L4D2", "left4dead2.exe sucess stopped")

	else:
		Finish_message = messagebox.askquestion("Can't Quit Game", "You can't Quit L4D2 L4D2 is not launched XD start the game ?")

		if Finish_message == "yes":
			Start_L4D2()

		else:
			print(cmd_detect_False)
			var_l4D2.set(l4D2_False)

def Spin(Pyautogui_input="down"):

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		var_l4D2.set(l4D2_True)

		if os.path.isfile(Folder_Time):
			with open(Folder_Time, "r" , encoding="utf-8") as Action_Time:
				Action_Time.seek(42)
				Time_Spin = float(Action_Time.readline())
				print("Time set on txt =",Time_Spin)

		else:
			messagebox.showwarning("Setting.txt as been deleted", "setting.txt file has been created or recreated with the time by default (5)")
			print("\033[0;33mThe setting.txt file has been created or recreated with the time by default (5)\033[0;37m")
			with open(Folder_Time, "a", encoding="utf-8") as Action_Time:
				Action_Time.write("Time for spin and return to games (Esc) = 5")

			with open(Folder_Time, "r", encoding="utf-8") as Action_Time:
				Action_Time.seek(42)
				Time_Spin = float(Action_Time.readline())
				print("Time set on txt =",Time_Spin)

		gui.moveTo(5000, 5000)
		L4D2_window.maximize()
		time.sleep(Time_Spin)

		maps = random.randrange(0, 91)
		maps_str = str(maps)
		print("Spin=",maps_str+"/90")

		gui.press("enter")

		if maps >= 20:
			maps_majority = int(maps / 1.3)
			maps_final = maps - maps_majority -3

			for i in range(maps_majority):
				gui.press(Pyautogui_input)

			for i in range(maps_final):
				time.sleep(0.050)
				gui.press(Pyautogui_input)

			for i in range(3):
				time.sleep(0.50)
				gui.press(Pyautogui_input)
						
		elif maps >= 10:
			maps_reduce = maps -3

			for i in range(maps_reduce):
				gui.press(Pyautogui_input)

			for i in range(3):
				time.sleep(0.50)
				gui.press(Pyautogui_input)

		elif maps < 10:
			for i in range(maps):
				time.sleep(0.50)
				gui.press(Pyautogui_input)
						
		#gui.hotkey("win", "prntscrn") #screen function for send to your friend disabled.
		gui.press("enter")

		time.sleep(2)
		Python_Ui.activate()

	else:
		Spin_message = messagebox.askquestion("Can't Spin", "You can't spin L4D2 is not launched start L4D2 ?")

		if Spin_message == "yes":
			Start_L4D2()

		else:
			print(cmd_detect_False)
			var_l4D2.set(l4D2_False)

def Return_to_game():

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		var_l4D2.set(l4D2_True)
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()

	else:
		Return_game_message = messagebox.askquestion("Can't Return To Game", "You can't return to game L4D2 is not launched start L4D2 ?")

		if Return_game_message == "yes":
			Start_L4D2()

		else:
			print(cmd_detect_False)
			var_l4D2.set(l4D2_False)

def Finish_random():

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		var_l4D2.set(l4D2_True)

		if os.path.isfile(Folder_Time):
			with open(Folder_Time, "r" , encoding="utf-8") as Action_Time:
				Action_Time.seek(42)
				Time_End = float(Action_Time.readline())
				print("Time set on txt =",Time_End)

		else:
			messagebox.showwarning("Setting.txt as been deleted", "setting.txt file has been created or recreated with the time by default (5)")
			print("\033[0;33mThe setting.txt file has been created or recreated with the time by default (5)\033[0;37m")
			with open(Folder_Time, "a", encoding="utf-8") as Action_Time:
				Action_Time.write("Time for spin and return to games (Esc) = 5")

			with open(Folder_Time, "r", encoding="utf-8") as Action_Time:
				Action_Time.seek(42)
				Time_End = float(Action_Time.readline())
				print("Time set on txt =",Time_End)

		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()

		time.sleep(Time_End)
		gui.press("esc")

	else:
		Finish_message = messagebox.askquestion("Can't Finish Spin", "You can't finish spin L4D2 is not launched start L4D2 ?")

		if Finish_message == "yes":
			Start_L4D2()

		else:
			print(cmd_detect_False)
			var_l4D2.set(l4D2_False)

def Hide_cmd():
	CMD.minimize()

def Show_cmd():
	CMD.restore()
	Python_Ui.activate()

def Quitting_Program():

	Quit_Program = messagebox.askquestion("Quit", "Are you sure ?")

	if Quit_Program == "yes":
		
		L4D2_is_launched = os.popen(Wmic_comand).read()

		if L4D2_is_launched.find(Game) != -1:
			
			L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
			L4D2_window.maximize()
			quit()
	
		else:
			quit()

def Credits():
	messagebox.showinfo("L4D2 Map Selector Credits", "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")
	
os.system("color")

Wmic_comand="wmic process get description"
Game="left4dead2.exe"
Folder_Time="setting.txt"
cmd_detect_True="\033[1;32mSucces detect: left4dead2.exe\033[0;37m"
cmd_detect_False="\033[0;31mleft4dead2.exe is not launched\033[0;37m"
l4D2_True ="L4D2: is launched =)" 
l4D2_False="L4D2: is not launched =("
Wmic_quit_comand="wmic process where name='left4dead2.exe' call terminate"

Discord_Rpc()
gui.FAILSAFE = False

mainapp = tkinter.Tk()
photo = tkinter.PhotoImage(file = "Pictures/icon.png")
mainapp.wm_iconphoto(False, photo)
mainapp.title("L4D2 Map Selector v1.2")
mainapp.geometry("+300+300")
mainapp.configure(bg="grey")

label_welcome = tkinter.Label(mainapp, bg="grey", text="Welcome to L4D2 Map Selector v1.2")
label_welcome.pack()

label_space = tkinter.Label(mainapp, bg="grey", text="---")
label_space.pack()

buttom_spin = tkinter.Button(mainapp, text="Spin", width=28, command=Spin)
buttom_spin.pack()

button_End = tkinter.Button(mainapp, text="Return to game and press Esc", width=25, command=Finish_random)
button_End.pack()

button_Return_Game = tkinter.Button(mainapp, text="Return to game", width=20, command=Return_to_game)
button_Return_Game.pack()

space = tkinter.Label(mainapp, bg="grey", text="---")
space.pack()

buttom_check = tkinter.Button(mainapp, text="Check L4D2 is launched", width=25, command=L4D2_State)
buttom_check.pack()

buttom_minimize_cmd = tkinter.Button(mainapp, text="Minimize cmd", width=20, command=Hide_cmd)
buttom_minimize_cmd.pack()

buttom_show_cmd = tkinter.Button(mainapp, text="Show cmd", width=15, command=Show_cmd)
buttom_show_cmd.pack()

label_space2 = tkinter.Label(mainapp, bg="grey", text="---")
label_space2.pack()

buttom_Start_L4D2 = tkinter.Button(mainapp, text="Start L4D2", width=25, bg="#00ff00", command=Start_L4D2)
buttom_Start_L4D2.pack()

buttom_Quit_L4D2 = tkinter.Button(mainapp, text="Quit L4D2", width=20, bg="#ff6f00", command=Quit_L4D2)
buttom_Quit_L4D2.pack()

button_Credits = tkinter.Button(mainapp, text="Credits", width=15, command=Credits)
button_Credits.pack()

buttom_quit_prog = tkinter.Button(mainapp, text="Quit Program", width=10, bg="#ff0000", command=Quitting_Program)
buttom_quit_prog.pack()

label_space3 = tkinter.Label(mainapp, bg="grey", text="")
label_space3.pack()

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", L4D2_State)
label_stat = tkinter.Label(mainapp, bg="grey", textvariable=var_l4D2)
label_stat.pack()

CMD = gw.getWindowsWithTitle("py.exe")[0]
Python_Ui = gw.getWindowsWithTitle("L4D2 Map Selector")[0]
CMD.minimize()

mainapp.mainloop()