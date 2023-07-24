#coding:utf-8
import os
import time
import tkinter
import sys
import webbrowser
import random
import getpass
import ctypes
from tkinter import ttk, messagebox, Frame
from time import perf_counter
import pyautogui as gui
import pygetwindow as gw
from py_folder.l4d2_presence import discord_Rpc

def welcome_user(ver_file="ver.txt", build_version="v1.3-21.07.2023-08PM"):

    """Say hello to user and show current build version"""

    if os.path.isfile(ver_file):
        with open(ver_file, "r", encoding="utf-8") as version_file:
            current_ver = version_file.readline()

    else:
        with open(ver_file, "a", encoding="utf-8") as version_file:
            version_file.write(build_version)

        with open(ver_file, "r", encoding="utf-8") as version_file:
            current_ver = version_file.readline()

    print("Welcome",getpass.getuser(),"to L4D2 Map Selector("+current_ver+")",
    "\n-------------------------------------------------\n")
    os.system("color")

welcome_user()
discord_Rpc()

def os_popen(comand):
    """Listing of executed program"""
    global is_launched
    is_launched = os.popen(comand).read()

def l4d2_state(*args):

    """Check at the starting of the program if the game are launched"""

    print("Check L4D2 is launched...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        print("\033[1;32mSucces detect: left4dead2.exe\033[0;37m")
        var_l4D2.set(L4D2_TRUE)
        messagebox.showinfo("Just checking...", "L4D2 is launched")

    else:
        print(CMD_DETECT_FALSE)
        var_l4D2.set(L4D2_FALSE)
        messagebox.showerror("Just checking...", "L4D2 is not launched")

def time_txt_read(*args, Time_file="setting.txt",
    File_not_found_message="The setting.txt file has been created with the time by default (5)",
    Wrong_setting_txt="is not correct input for setting.txt correct is number(in seconds)"+
                      "or number(in seconds).number(in milliseconds)",
    Default_time="Time for switching program to game (depend on your pc default is 5 seconds)"+
                 "= 5.0",
    Wrong_resolution="Setting.txt input has been changed with the time by default (5)"):

    '''
    Read setting.txt for checking the value and change Var_time_setting_txt label of gui
    if setting.txt contain "," replace to "."
    '''

    global TIME_FOR_ACTION

    try:
        if os.path.isfile(Time_file):

            with open(Time_file, "r" , encoding="utf-8") as action_time:
                verif_time_for_action = action_time.read()

            if verif_time_for_action.find(","):
                fix_time = verif_time_for_action.replace("," , ".")
                with open(Time_file, "w" , encoding="utf-8") as action_time:
                    action_time.write(fix_time)

            with open(Time_file, "r" , encoding="utf-8") as action_time:
                action_time.seek(77)
                TIME_FOR_ACTION = action_time.readline() #int or float number
                print("Time set on txt", TIME_FOR_ACTION)
                Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

        else:
            #If setting file as not in racine repertory
            messagebox.showwarning("Setting.txt as been deleted", File_not_found_message)
            print("\033[0;33m"+File_not_found_message+"\033[0;37m")

            with open(Time_file, "a", encoding="utf-8") as action_time:
                action_time.write(Default_time)

            with open(Time_file, "r", encoding="utf-8") as action_time:
                action_time.seek(77)
                TIME_FOR_ACTION = action_time.readline()
                print("Time set on txt", TIME_FOR_ACTION)
                Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

    except ValueError:
        #If setting.txt contain wrong argument
        with open(Time_file, "r" , encoding="utf-8") as action_time:
            action_time.seek(77)
            wrong_input = action_time.readline()

        print("\033[0;33mValueError in setting.txt:\033[0;37m"+wrong_input+"\033[0;33m",
        Wrong_setting_txt,"\033[0;37m\n"+Wrong_resolution)
        messagebox.showwarning("ValueError !",wrong_input+" "+Wrong_setting_txt+"\n\n"+
        Wrong_resolution)

        #Resolution of setting.txt
        with open(Time_file, "r+" , encoding="utf-8") as action_time:
            action_time.truncate()
            action_time.write(Default_time)

        #After resolution of setting.txt
        with open(Time_file, "r" , encoding="utf-8") as action_time:
            action_time.seek(77)
            TIME_FOR_ACTION = action_time.readline()
            print("Time set on txt", TIME_FOR_ACTION)
            Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

def set_time_gui():

    """Set the time on Setting.txt file for switching time of aplication to game"""

    with open("setting.txt", "r+", encoding="utf-8") as action_time:

        action_time.seek(77)
        action_time.truncate()
        action_time.write(txt_time_e.get())

        Var_time_setting_txt.set("(Txt)Setting= {}".format(txt_time_e.get()))
    time_txt_read()

def track_windows(name_of_window):

    """Fullscreen the desired window"""

    global window

    window = gw.getWindowsWithTitle(name_of_window)[0]
    window.maximize()
    window.activate()

def start_l4d2(succes_start_cmd="\033[1;32mSucces detect:"
    "\bleft4dead2.exe\n\033[1;32mleft4dead2.exe is succefully started\033[0;37m",
    steam_on="\033[1;32mSteam.exe is launched\033[0;37m",
    steam_off="\033[0;31mSteam.exe is not launched\033[0;37m"):

    """Start left4dead2.exe -> steam://rungameid/550"""

    print("Start L4D2...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        messagebox.showwarning("Just checking...", "L4D2 as already launched")
        print("\033[0;33mleft4dead2.exe: as already launched\033[0;37m")
        track_windows("Left 4 Dead 2")

    else:
        CMD.restore()
        steam_status = os.popen(WMIC_COMAND).read()

        if steam_status.find("steam.exe") != -1:
            print(steam_on,"\nWait... test if left4dead2.exe is launched in 10 tries:")
            webbrowser.open("steam://rungameid/550")

            for _ in range(10):
                os_popen(WMIC_COMAND)

                if is_launched.find(GAME) != -1:
                    l4d2_launched = True
                    print(succes_start_cmd)
                    var_l4D2.set(L4D2_TRUE)
                    time.sleep(5)
                    CMD.minimize()
                    Python_Ui.restore()
                    break

                l4d2_launched = False
                print("left4dead2.exe not detect")
                time.sleep(2)

            if l4d2_launched is False:
                print("\033[0;31mLeft4Dead2 is not installed\033[0;37m\n")
                time.sleep(2)
                Python_Ui.restore()
                messagebox.showerror("Error !", "Left4Dead2 is not installed on your pc =(")
                CMD.minimize()
                var_l4D2.set("L4D2: is not installed on your computer =(")

        else:
            print(steam_off,"\nWait... test if left4dead2.exe is launched in 20 tries:")
            webbrowser.open("steam://rungameid/550")

            for _ in range(20):
                os_popen(WMIC_COMAND)

                if is_launched.find(GAME) != -1:
                    l4d2_launched = True
                    print(succes_start_cmd)
                    var_l4D2.set(L4D2_TRUE)
                    time.sleep(5)
                    CMD.minimize()
                    Python_Ui.restore()
                    break

                l4d2_launched = False
                print("left4dead2.exe not detect")
                time.sleep(2)

            if l4d2_launched is False:
                print("\033[0;31mLeft4Dead2 is not installed\033[0;37m")
                time.sleep(2)
                Python_Ui.restore()
                messagebox.showerror("Error !", "Left4Dead2 is not installed on your pc =(")
                CMD.minimize()
                var_l4D2.set("L4D2: is not installed on your computer =(")

def quit_l4d2():

    """Stop left4dead2.exe process -> wmic process where name='left4dead2.exe' call terminate"""

    print("Quit L4D2...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        os.system("wmic process where name='left4dead2.exe' call terminate")
        var_l4D2.set(L4D2_FALSE)
        messagebox.showinfo("Quit L4D2", "left4dead2.exe sucess stopped")

    else:
        finish_message = messagebox.askquestion("Can't Quit Game",
        "You can't Quit L4D2 L4D2 is not launched XD start the game ?")

        if finish_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

def determine_spin_time(spin_time_determination="setting.txt"):

    """Counts the time for the game to go full screen"""

    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        time_spin_start = perf_counter()

        while True:
            track_windows("Left 4 Dead 2")
            maxi = window.isMaximized

            if maxi:
                time_spin_stop = perf_counter()
                good_time = time_spin_stop - time_spin_start

                with open(spin_time_determination, "a",
                          encoding="utf-8") as final_result_determination:

                    final_result_determination.seek(77)
                    final_result_determination.truncate()
                    final_result_determination.write("{:.2f}".format(good_time))
                    print("Time set on txt {:.2f}".format(good_time))
                    Var_time_setting_txt.set("Txt)Setting= {:.2f}".format(good_time))
                    Python_Ui.activate()
                    messagebox.showinfo("Switching time...",
                                        "Switching time are succefully apply into Settings.txt")
                break

    else:
        determine_message = messagebox.askquestion("Switching time determination impossible...",
        "Determination are impossible because your L4D2 is not launched start the game ?")

        if determine_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

def first_spin_gui(*args):
    """first value of random 0, 90"""
    Var_last_randrange_maps.set("(Spin)number= None")

def spin(pyautogui_input="down"):

    """Randomize map selection"""

    print("Spin...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:

        start = perf_counter()

        var_l4D2.set(L4D2_TRUE)
        time_txt_read()
        gui.moveTo(5000, 5000)

        maps = random.randrange(0, 91)
        print("Spin=",str(maps)+"/90")
        maps_result_gui = "(Spin)number=",str(maps)+"/90"
        Var_last_randrange_maps.set(maps_result_gui)

        track_windows("Left 4 Dead 2")
        stop = perf_counter()
        os_popen(WMIC_COMAND)

        if is_launched.find("NVIDIA") != -1:
            secure_time = stop - start
            time.sleep(float(TIME_FOR_ACTION) + secure_time)
            gui.press("enter")

        else:
            time.sleep(float(TIME_FOR_ACTION))
            gui.press("enter")

        if maps >= 20:

            for _ in range(round(maps / 1.3)):
                gui.press(pyautogui_input)

            for _ in range(maps - round(maps / 1.3) -3):
                time.sleep(0.050)
                gui.press(pyautogui_input)

            for _ in range(3):
                time.sleep(0.50)
                gui.press(pyautogui_input)

        elif maps >= 10:

            for _ in range(round(maps / 1.3)):
                gui.press(pyautogui_input)

            for _ in range(maps - round(maps / 1.3) -3):
                time.sleep(0.050)
                gui.press(pyautogui_input)

            for _ in range(3):
                time.sleep(0.50)
                gui.press(pyautogui_input)

        elif maps < 10:
            for _ in range(maps):
                time.sleep(0.50)
                gui.press(pyautogui_input)

        #gui.hotkey("win", "prntscrn") screen function for send to your friend disabled.
        gui.press("enter")
        time.sleep(1.5)
        Python_Ui.activate()
        user32 = ctypes.windll.user32
        center_res = user32.GetSystemMetrics(0)/2, user32.GetSystemMetrics(1)/2
        gui.moveTo(center_res)

    else:
        spin_message = messagebox.askquestion("Can't Spin",
        "You can't spin L4D2 is not launched start L4D2 ?")

        if spin_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

def return_to_game():

    """simpli return to game XD"""

    print("Return to game...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        var_l4D2.set(L4D2_TRUE)
        track_windows("Left 4 Dead 2")

    else:
        return_game_message = messagebox.askquestion("Can't Return To Game",
        "You can't return to game L4D2 is not launched start L4D2 ?")

        if return_game_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

def finish_random():

    """return to game and press escape button"""

    print("Return to game and press escape...")
    os_popen(WMIC_COMAND)

    if is_launched.find(GAME) != -1:
        var_l4D2.set(L4D2_TRUE)
        track_windows("Left 4 Dead 2")
        time.sleep(TIME_FOR_ACTION)
        gui.press("esc")

    else:
        finish_message = messagebox.askquestion("Can't Finish Spin",
        "You can't finish spin L4D2 is not launched start L4D2 ?")

        if finish_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

def hide_cmd():
    """Hide cmd prompt"""
    CMD.minimize()

def show_cmd():
    """Show cmd prompt"""
    CMD.restore()
    Python_Ui.activate()

def quitting_program():

    """Quitting main program"""

    quit_program = messagebox.askquestion("Quit", "Are you sure ?")

    if quit_program == "yes":

        os_popen(WMIC_COMAND)

        if is_launched.find(GAME) != -1:

            track_windows("Left 4 Dead 2")
            sys.exit()

        else:
            sys.exit()

def credits():
    """ Credits of the program"""
    messagebox.showinfo("L4D2 Map Selector Credits",
    "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")

WMIC_COMAND="wmic process get description"
GAME="left4dead2.exe"
CMD_DETECT_FALSE="\033[0;31mleft4dead2.exe is not launched\033[0;37m"
L4D2_TRUE ="L4D2: is launched =)"
L4D2_FALSE="L4D2: is not launched =("

gui.FAILSAFE = False

mainapp = tkinter.Tk()

s = ttk.Style()
s.theme_use("default")
s.configure("TNotebook",background="#333333")
s.configure("First.TButton",background="#B6FF03",font=("Arial", 10))
s.configure("Start_L4D2.TButton",background="#00ff00",font=("Arial", 10))
s.configure("Quit.TButton",background="#ff6f00",font=("Arial", 10))
s.configure("Quit_Program.TButton",background="#C81A1A",font=("Arial", 10))
s.configure("Credits.TButton",background="#1AC3C8",font=("Arial", 10))
s.configure("Set.TButton",background="#FFFFFF",font=("Arial", 10))
s.configure("Second.TButton",background="#FF3399",font=("Arial", 10))

tab_pages = ttk.Notebook(mainapp,style="TNotebook")
tab1 = Frame(tab_pages, bg="#333333")
tab2 = Frame(tab_pages, bg="#333333")
tab_pages.add(tab1,text="L4D2")
tab_pages.add(tab2,text="Settings")
tab_pages.pack()

photo = tkinter.PhotoImage(file = "pictures/icon.png")
mainapp.wm_iconphoto(False, photo)
mainapp.title("L4D2 Map Selector v1.3")
mainapp.eval("tk::PlaceWindow . center")
mainapp.resizable(False, False)

#Gui label and button
label_welcome = tkinter.Label(tab1, bg="#333333", fg="#EA1818",
text="Welcome to L4D2 Map Selector v1.3", font=("Arial"))
label_welcome.grid(row=0, column=0)

label_space = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="")
label_space.grid(row=1, column=0)

button_spin = ttk.Button(tab1, text="Spin", width=30, command=spin,
style="First.TButton")
button_spin.grid(row=2 ,column=0)

button_End = ttk.Button(tab1, text="Close choice (multi lobby)",
width=25, command=finish_random, style="First.TButton")
button_End.grid(row=3 ,column=0)

button_Return_Game = ttk.Button(tab1, text="Return to game",
width=20, command=return_to_game, style="First.TButton")
button_Return_Game.grid(row=4 ,column=0)

label_space3 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="---", font=("Arial", 10))
label_space3.grid(row=5 ,column=0)

button_Start_L4D2 = ttk.Button(tab1, text="Start L4D2",
width=30, command=start_l4d2, style="Start_L4D2.TButton")
button_Start_L4D2.grid(row=6 ,column=0)

button_Quit_L4D2 = ttk.Button(tab1, text="Quit L4D2",
width=25, command=quit_l4d2, style="Quit.TButton")
button_Quit_L4D2.grid(row=7 ,column=0)

button_quit_prog = ttk.Button(tab1, text="Quit Program",
width=20, command=quitting_program, style="Quit_Program.TButton")
button_quit_prog.grid(row=8 ,column=0)

button_Credits = ttk.Button(tab1, text="Credits", width=15, command=credits,
style="Credits.TButton")
button_Credits.grid(row=9 ,column=0)

label_space5 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="")
label_space5.grid(row=10, column=0)

label_space6 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
text="------------------------------------------------------------", font=("Arial", 10))
label_space6.grid(row=11 ,column=0)

Var_last_randrange_maps = tkinter.StringVar()
Var_last_randrange_maps.trace("r", first_spin_gui)

label_spin = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
textvariable=Var_last_randrange_maps, font=("Arial", 10))
label_spin.grid(row=13 ,column=0)

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", l4d2_state)

label_stat = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
textvariable=var_l4D2, font=("Arial", 10))
label_stat.grid(row=14 ,column=0)

label_space7 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
text="------------------------------------------------------------", font=("Arial", 10))
label_space7.grid(row=15 ,column=0)

label_Time = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF", text="Switch Time :", font=("Arial", 12))
label_Time.pack()

txt_time_e = ttk.Entry(tab2, width=10)
txt_time_e.insert(0, "5.0")
txt_time_e.pack()

txt_time_button = ttk.Button(tab2, text="Set", width=5, command=set_time_gui,
style="Set.TButton")
txt_time_button.pack()

label_space = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF", text="")
label_space.pack()

button_check = ttk.Button(tab2, text="Check L4D2 is launched", width=30, command=l4d2_state,
style="Second.TButton")
button_check.pack()

button_determine_spin = ttk.Button(tab2, text="Determine switching time", width=25,
command=determine_spin_time, style="Second.TButton")
button_determine_spin.pack()

button_minimize_cmd = ttk.Button(tab2, text="Minimize cmd", width=20, command=hide_cmd,
style="Second.TButton")
button_minimize_cmd.pack()

button_show_cmd = ttk.Button(tab2, text="Show cmd", width=15, command=show_cmd,
style="Second.TButton")
button_show_cmd.pack()

label_space2 = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF", text="")
label_space2.pack()

Var_time_setting_txt = tkinter.StringVar()
Var_time_setting_txt.trace("r", time_txt_read)

label_setting = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF",
textvariable=Var_time_setting_txt, font=("Arial", 10))
label_setting.pack()

try:
    CMD = gw.getWindowsWithTitle("py.exe")[0]
except IndexError:
    CMD = gw.getWindowsWithTitle("l4d2_map_selector_v1.3.py")[0]

Python_Ui = gw.getWindowsWithTitle("L4D2 Map Selector")[0]
CMD.minimize()

mainapp.mainloop()
