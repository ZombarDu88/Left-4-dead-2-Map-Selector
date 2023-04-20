#coding:utf-8
import tkinter
from tkinter import messagebox
from Py_folder.L4D2_presence import *
import webbrowser
import random
import getpass
import pyautogui as gui
import pygetwindow as gw

def L4D2_State(*args):

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		print(cmd_detect_True)
		var_l4D2.set(l4D2_True)
		messagebox.showinfo("Just checking...", "L4D2 is launched")

	else:
		print(cmd_detect_False)
		var_l4D2.set(l4D2_False)
		messagebox.showerror("Just checking...", "L4D2 is not launched")

def Time_txt_read(*args, File_not_found_message="The setting.txt file has been created or recreated with the time by default (5)",
	Time_file="setting.txt", Wrong_setting_txt="is not correct input for setting.txt correct is number(in seconds) or number(in seconds).number(in milliseconds)",
	Wrong_resolution="Setting.txt input has been changed with the time by default (5)", Default_time="Time for spin and return to games (Esc) = 5", Txt_seek=41):

	global Time_for_action

	try:
		'''Read setting.txt and change Var_time_setting_txt label of gui'''
		if os.path.isfile(Time_file):
			'''if setting.txt contain "," replace to "." '''
			with open(Time_file, "r" , encoding="utf-8") as Action_Time:
				Verif_Time_for_action = Action_Time.read()

			if Verif_Time_for_action.find(","):
				Fix_Time = Verif_Time_for_action.replace("," , ".")
				with open(Time_file, "w" , encoding="utf-8") as Action_Time: 
					Action_Time.write(Fix_Time)

			with open(Time_file, "r" , encoding="utf-8") as Action_Time:
				Action_Time.seek(Txt_seek)
				Time_for_action = float(Action_Time.readline()) #int or float number
				Time_txt_on_gui = "(Txt)setting=",Time_for_action
				print("Time set on txt", Time_for_action)
				Var_time_setting_txt.set(Time_txt_on_gui)

		else:
			'''If setting file as not in racine repertory'''
			messagebox.showwarning("Setting.txt as been deleted", File_not_found_message)
			print("\033[0;33m"+File_not_found_message+"\033[0;37m")

			with open(Time_file, "a", encoding="utf-8") as Action_Time:
				Action_Time.write(Default_time)

			with open(Time_file, "r", encoding="utf-8") as Action_Time:
				Action_Time.seek(Txt_seek)
				Time_for_action = float(Action_Time.readline())
				Time_txt_on_gui = "(Txt)Setting=",Time_for_action
				print("Time set on txt", Time_for_action)
				Var_time_setting_txt.set(Time_txt_on_gui)

	except ValueError:
		'''If setting.txt contain wrong argument'''
		with open(Time_file, "r" , encoding="utf-8") as Action_Time:
				Action_Time.seek(Txt_seek)
				Wrong_input = Action_Time.readline()

		print("\033[0;33mValueError in setting.txt:\033[0;37m",Wrong_input+"\033[0;33m",Wrong_setting_txt,"\033[0;37m")
		print(Wrong_resolution)
		messagebox.showwarning("ValueError !",Wrong_input+" "+Wrong_setting_txt+"\n\n"+Wrong_resolution)

		'''Resolution of setting.txt'''
		with open(Time_file, "r+" , encoding="utf-8") as Action_Time:
			Action_Time.truncate()
			Action_Time.write(Default_time)

		'''After resolution of setting.txt'''
		with open(Time_file, "r" , encoding="utf-8") as Action_Time: 
			Action_Time.seek(Txt_seek)
			Time_for_action = float(Action_Time.readline())
			Time_txt_on_gui = "(Txt)setting=",Time_for_action
			print("Time set on txt", Time_for_action)
			Var_time_setting_txt.set(Time_txt_on_gui)

def First_spin_gui(*args):
	Var_last_randrange_maps.set("(Spin)number= None")

def First_map_gui(*args):
	Var_Map_Selected.set("Map Selected= SOON")

def Start_L4D2(Succes_start_cmd="\033[1;32mSucces detect: left4dead2.exe\n\033[1;32mleft4dead2.exe is succefully started\033[0;37m", 
	Steam_ON="\033[1;32mSteam.exe is launched\033[0;37m", Steam_OFF="\033[0;31mSteam.exe is not launched\033[0;37m"):
	
	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		messagebox.showwarning("Just checking...", "L4D2 as already launched")
		print("\033[0;33mleft4dead2.exe: as already launched\033[0;37m")
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()
		L4D2_window.activate()

	else:
		CMD.restore()
		Steam_status = os.popen(Wmic_comand).read()

		if Steam_status.find(Laucher) != -1:
			print(Steam_ON,"\nWhait... test if left4dead2.exe is launched in 10 tries:")
			webbrowser.open("steam://rungameid/550")

			for i in range(10):
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
				time.sleep(2)
				Python_Ui.activate()
				messagebox.showerror("Error !", "Left4Dead2 is not installed on your pc =(\nnot possible to start it")
				var_l4D2.set("L4D2: is not installed on your computer =(")

		else:
			print(Steam_OFF,"\nWhait... test if left4dead2.exe is launched in 20 tries:")
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
				time.sleep(2)
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
			var_l4D2.set(l4D2_False)
			print(cmd_detect_False)

#def Maps_Selection(): #coming soon

def Spin(Pyautogui_input="down"):

	Time_txt_read()
	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		var_l4D2.set(l4D2_True)

		gui.moveTo(5000, 5000)

		maps = random.randrange(0, 91)
		maps_majority = int(maps / 1.3)
		maps_final = maps - maps_majority -3
		maps_result = print("Spin=",str(maps)+"/90")
		maps_result_gui = "(Spin)number=",str(maps)+"/90"
		Var_last_randrange_maps.set(maps_result_gui)
		
		L4D2_window.maximize()
		L4D2_window.activate()
		time.sleep(Time_for_action)
		gui.press("enter")

		if maps >= 20:

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
			var_l4D2.set(l4D2_False)
			print(cmd_detect_False)

def Return_to_game():

	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		var_l4D2.set(l4D2_True)
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		L4D2_window.maximize()
		L4D2_window.activate()

	else:
		Return_game_message = messagebox.askquestion("Can't Return To Game", "You can't return to game L4D2 is not launched start L4D2 ?")

		if Return_game_message == "yes":
			Start_L4D2()

		else:
			var_l4D2.set(l4D2_False)
			print(cmd_detect_False)

def Finish_random():

	Time_txt_read()
	L4D2_is_launched = os.popen(Wmic_comand).read()

	if L4D2_is_launched.find(Game) != -1:
		L4D2_window = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
		var_l4D2.set(l4D2_True)

		L4D2_window.maximize()
		L4D2_window.activate()
		time.sleep(Time_for_action)
		gui.press("esc")

	else:
		Finish_message = messagebox.askquestion("Can't Finish Spin", "You can't finish spin L4D2 is not launched start L4D2 ?")

		if Finish_message == "yes":
			Start_L4D2()

		else:
			var_l4D2.set(l4D2_False)
			print(cmd_detect_False)

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
			L4D2_window.activate()
			quit()
	
		else:
			quit()

def Credits():
	messagebox.showinfo("L4D2 Map Selector Credits", "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")

ver_file = "ver.txt"
Build_version = "v1.2-20.04.2023-05PM"

if os.path.isfile(ver_file):
	with open("ver.txt", "r", encoding="utf-8") as version_file:
		current_ver = version_file.readline()

else:
	with open(ver_file, "a", encoding="utf-8") as version_file:
		version_file.write(Build_version)

	with open(ver_file, "r", encoding="utf-8") as version_file:
		current_ver = version_file.readline()

print("Welcome",getpass.getuser(),"to L4D2 Map Selector("+current_ver+")\n-------------------------------------------------\n")
os.system("color")

Wmic_comand="wmic process get description"
Laucher="steam.exe"
Game="left4dead2.exe"
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
mainapp.eval("tk::PlaceWindow . center")
mainapp.resizable(False, False)
mainapp.configure(bg="grey")

'''Gui label and button'''
label_welcome = tkinter.Label(mainapp, bg="grey", text="Welcome to L4D2 Map Selector v1.2")
label_welcome.pack()

label_space = tkinter.Label(mainapp, bg="grey", text="---")
label_space.pack()

button_spin = tkinter.Button(mainapp, text="Spin", width=30, command=Spin)
button_spin.pack()

button_End = tkinter.Button(mainapp, text="Return to game and press Esc", width=25, command=Finish_random)
button_End.pack()

button_Return_Game = tkinter.Button(mainapp, text="Return to game", width=20, command=Return_to_game)
button_Return_Game.pack()

space = tkinter.Label(mainapp, bg="grey", text="---")
space.pack()

button_check = tkinter.Button(mainapp, text="Check L4D2 is launched", width=25, command=L4D2_State)
button_check.pack()

button_minimize_cmd = tkinter.Button(mainapp, text="Minimize cmd", width=20, command=Hide_cmd)
button_minimize_cmd.pack()

button_show_cmd = tkinter.Button(mainapp, text="Show cmd", width=15, command=Show_cmd)
button_show_cmd.pack()

label_space2 = tkinter.Label(mainapp, bg="grey", text="---")
label_space2.pack()

button_Start_L4D2 = tkinter.Button(mainapp, text="Start L4D2", width=25, bg="#00ff00", command=Start_L4D2)
button_Start_L4D2.pack()

button_Quit_L4D2 = tkinter.Button(mainapp, text="Quit L4D2", width=20, bg="#ff6f00", command=Quit_L4D2)
button_Quit_L4D2.pack()

button_Credits = tkinter.Button(mainapp, text="Credits", width=15, command=Credits)
button_Credits.pack()

button_quit_prog = tkinter.Button(mainapp, text="Quit Program", width=10, bg="#ff0000", command=Quitting_Program)
button_quit_prog.pack()

label_space3 = tkinter.Label(mainapp, bg="grey", text="---------------------------------------")
label_space3.pack()

Var_time_setting_txt = tkinter.StringVar()
Var_time_setting_txt.trace("r", Time_txt_read)
label_setting = tkinter.Label(mainapp, bg="grey", textvariable=Var_time_setting_txt)
label_setting.pack()

Var_last_randrange_maps = tkinter.StringVar()
Var_last_randrange_maps.trace("r", First_spin_gui)
label_spin = tkinter.Label(mainapp, bg="grey", textvariable=Var_last_randrange_maps)
label_spin.pack()

Var_Map_Selected = tkinter.StringVar()
Var_Map_Selected.trace("r", First_map_gui)
label_map = tkinter.Label(mainapp, bg="grey", textvariable=Var_Map_Selected)
label_map.pack()

label_space4 = tkinter.Label(mainapp, bg="grey", text="---------------------------------------")
label_space4.pack()

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", L4D2_State)
label_stat = tkinter.Label(mainapp, bg="grey", textvariable=var_l4D2)
label_stat.pack()

CMD = gw.getWindowsWithTitle("py.exe")[0]
Python_Ui = gw.getWindowsWithTitle("L4D2 Map Selector")[0]
CMD.minimize()

mainapp.mainloop()