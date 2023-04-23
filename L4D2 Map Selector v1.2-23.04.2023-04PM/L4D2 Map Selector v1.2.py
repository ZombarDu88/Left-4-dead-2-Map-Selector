#coding:utf-8
import tkinter
import sys
import webbrowser
import random
import getpass
from tkinter import messagebox
import pyautogui as gui
import pygetwindow as gw
from Py_folder.L4D2_presence import *

def welcome_user():

    ver_file = "ver.txt"
    build_version = "v1.2-23.04.2023-04PM"

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
    global l4d2_is_launched
    l4d2_is_launched = os.popen(comand).read()

def l4d2_state(*args):

    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:
        print(CMD_DETECT_TRUE)
        var_l4D2.set(L4D2_TRUE)
        messagebox.showinfo("Just checking...", "L4D2 is launched")

    else:
        print(CMD_DETECT_FALSE)
        var_l4D2.set(L4D2_FALSE)
        messagebox.showerror("Just checking...", "L4D2 is not launched")

def time_txt_read(*args, Time_file="setting.txt", Txt_seek=41,
    File_not_found_message="The setting.txt file has been created with the time by default (5)",
    Wrong_setting_txt="is not correct input for setting.txt correct is number(in seconds)"+
    "or number(in seconds).number(in milliseconds)",
    Default_time="Time for spin and return to games (Esc) = 5.0",
    Wrong_resolution="Setting.txt input has been changed with the time by default (5)"):

    global TIME_FOR_ACTION

    try:
        #Read setting.txt and change Var_time_setting_txt label of gui
        if os.path.isfile(Time_file):
            '''if setting.txt contain "," replace to "." '''
            with open(Time_file, "r" , encoding="utf-8") as action_time:
                verif_time_for_action = action_time.read()

            if verif_time_for_action.find(","):
                fix_time = verif_time_for_action.replace("," , ".")
                with open(Time_file, "w" , encoding="utf-8") as action_time:
                    action_time.write(fix_time)

            with open(Time_file, "r" , encoding="utf-8") as action_time:
                action_time.seek(Txt_seek)
                TIME_FOR_ACTION = float(action_time.readline()) #int or float number
                time_txt_on_gui = "(Txt)setting=",TIME_FOR_ACTION
                print("Time set on txt", TIME_FOR_ACTION)
                Var_time_setting_txt.set(time_txt_on_gui)

        else:
            #If setting file as not in racine repertory
            messagebox.showwarning("Setting.txt as been deleted", File_not_found_message)
            print("\033[0;33m"+File_not_found_message+"\033[0;37m")

            with open(Time_file, "a", encoding="utf-8") as action_time:
                action_time.write(Default_time)

            with open(Time_file, "r", encoding="utf-8") as action_time:
                action_time.seek(Txt_seek)
                TIME_FOR_ACTION = float(action_time.readline())
                time_txt_on_gui = "(Txt)Setting=",TIME_FOR_ACTION
                print("Time set on txt", TIME_FOR_ACTION)
                Var_time_setting_txt.set(time_txt_on_gui)

    except ValueError:
        #If setting.txt contain wrong argument
        with open(Time_file, "r" , encoding="utf-8") as action_time:
            action_time.seek(Txt_seek)
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
            action_time.seek(Txt_seek)
            TIME_FOR_ACTION = float(action_time.readline())
            time_txt_on_gui = "(Txt)setting=",TIME_FOR_ACTION
            print("Time set on txt", TIME_FOR_ACTION)
            Var_time_setting_txt.set(time_txt_on_gui)

def set_time_gui():

    with open("setting.txt", "r+", encoding="utf-8") as action_time:
        action_time.seek(42)
        action_time.truncate()
        action_time.write(txt_time_e.get())
        time_txt_on_gui = "(Txt)setting=",txt_time_e.get()
        Var_time_setting_txt.set(time_txt_on_gui)
    time_txt_read()

def track_l4d2_windows(name_of_window):

    l4d2_window = gw.getWindowsWithTitle(name_of_window)[0]
    l4d2_window.maximize()
    l4d2_window.activate()

def start_l4d2(succes_start_cmd="\033[1;32mSucces detect:"
    "\bleft4dead2.exe\n\033[1;32mleft4dead2.exe is succefully started\033[0;37m",
    steam_on="\033[1;32mSteam.exe is launched\033[0;37m",
    steam_off="\033[0;31mSteam.exe is not launched\033[0;37m"):

    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:
        messagebox.showwarning("Just checking...", "L4D2 as already launched")
        print("\033[0;33mleft4dead2.exe: as already launched\033[0;37m")
        track_l4d2_windows("Left 4 Dead 2")

    else:
        CMD.restore()
        steam_status = os.popen(WMIC_COMAND).read()

        if steam_status.find(LAUCHER) != -1:
            print(steam_on,"\nWait... test if left4dead2.exe is launched in 10 tries:")
            webbrowser.open("steam://rungameid/550")

            for _ in range(10):
                os_popen(WMIC_COMAND)

                if l4d2_is_launched.find(GAME) != -1:
                    l4d2_launched = True
                    print(succes_start_cmd)
                    var_l4D2.set(L4D2_TRUE)
                    time.sleep(5)
                    CMD.minimize()
                    Python_Ui.restore()
                    break

                else:
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

                if l4d2_is_launched.find(GAME) != -1:
                    l4d2_launched = True
                    print(succes_start_cmd)
                    var_l4D2.set(L4D2_TRUE)
                    time.sleep(5)
                    CMD.minimize()
                    Python_Ui.restore()
                    break

                else:
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

    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:
        os.system(WMIC_QUIT_COMAND)
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

def first_spin_gui(*args):
    Var_last_randrange_maps.set("(Spin)number= None")

def spin(pyautogui_input="down"):

    time_txt_read()
    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:

        var_l4D2.set(L4D2_TRUE)
        gui.moveTo(5000, 5000)

        maps = random.randrange(0, 91)
        maps_majority = int(maps / 1.3)
        maps_final = maps - maps_majority -3
        print("Spin=",str(maps)+"/90")
        maps_result_gui = "(Spin)number=",str(maps)+"/90"
        Var_last_randrange_maps.set(maps_result_gui)

        track_l4d2_windows("Left 4 Dead 2")
        time.sleep(TIME_FOR_ACTION)
        gui.press("enter")

        if maps >= 20:

            for _ in range(maps_majority):
                gui.press(pyautogui_input)

            for _ in range(maps_final):
                time.sleep(0.050)
                gui.press(pyautogui_input)

            for _ in range(3):
                time.sleep(0.50)
                gui.press(pyautogui_input)

        elif maps >= 10:
            maps_reduce = maps -3

            for _ in range(maps_reduce):
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
        time.sleep(2)
        Python_Ui.activate()

    else:
        spin_message = messagebox.askquestion("Can't Spin",
        "You can't spin L4D2 is not launched start L4D2 ?")

        if spin_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

#simpli return to game XD
def return_to_game():

    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:
        var_l4D2.set(L4D2_TRUE)
        track_l4d2_windows("Left 4 Dead 2")

    else:
        return_game_message = messagebox.askquestion("Can't Return To Game",
        "You can't return to game L4D2 is not launched start L4D2 ?")

        if return_game_message == "yes":
            start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

#return to game and press ecape button
def finish_random():

    print("Return to game and press escape...")
    time_txt_read()
    os_popen(WMIC_COMAND)

    if l4d2_is_launched.find(GAME) != -1:
        var_l4D2.set(L4D2_TRUE)
        track_l4d2_windows("Left 4 Dead 2")
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
    CMD.minimize()

def show_cmd():
    CMD.restore()
    Python_Ui.activate()

def quitting_program():

    quit_program = messagebox.askquestion("Quit", "Are you sure ?")

    if quit_program == "yes":

        os_popen(WMIC_COMAND)

        if l4d2_is_launched.find(GAME) != -1:

            track_l4d2_windows("Left 4 Dead 2")
            sys.exit()

        else:
            sys.exit()

#credits
def credits():
    messagebox.showinfo("L4D2 Map Selector Credits",
    "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")

WMIC_COMAND="wmic process get description"
LAUCHER="steam.exe"
GAME="left4dead2.exe"
CMD_DETECT_TRUE="\033[1;32mSucces detect: left4dead2.exe\033[0;37m"
CMD_DETECT_FALSE="\033[0;31mleft4dead2.exe is not launched\033[0;37m"
L4D2_TRUE ="L4D2: is launched =)"
L4D2_FALSE="L4D2: is not launched =("
WMIC_QUIT_COMAND="wmic process where name='left4dead2.exe' call terminate"

gui.FAILSAFE = False

mainapp = tkinter.Tk()
photo = tkinter.PhotoImage(file = "Pictures/icon.png")
mainapp.wm_iconphoto(False, photo)
mainapp.title("L4D2 Map Selector v1.2")
mainapp.eval("tk::PlaceWindow . center")
mainapp.resizable(False, False)
mainapp.configure(bg="grey")

#Gui label and button
label_welcome = tkinter.Label(mainapp, bg="grey", text="Welcome to L4D2 Map Selector v1.2")
label_welcome.pack()

label_space = tkinter.Label(mainapp, bg="grey", text="---")
label_space.pack()

label_space = tkinter.Label(mainapp, bg="grey", text="Time")
label_space.place(x=30, y=40)

txt_time_e = tkinter.Entry(mainapp, width=10)
txt_time_e.pack()
txt_time_e.insert(0, "5.0")

txt_time_button = tkinter.Button(mainapp, text="Set", width=5, command=set_time_gui)
txt_time_button.place(x=150, y=40)

label_space2 = tkinter.Label(mainapp, bg="grey", text="")
label_space2.pack()

button_spin = tkinter.Button(mainapp, text="Spin", width=30, command=spin)
button_spin.pack()

button_End = tkinter.Button(mainapp, text="Return to game and press Esc",
width=25, command=finish_random)
button_End.pack()

button_Return_Game = tkinter.Button(mainapp, text="Return to game",
width=20, command=return_to_game)
button_Return_Game.pack()

label_space3 = tkinter.Label(mainapp, bg="grey", text="---")
label_space3.pack()

button_check = tkinter.Button(mainapp, text="Check L4D2 is launched", width=25, command=l4d2_state)
button_check.pack()

button_minimize_cmd = tkinter.Button(mainapp, text="Minimize cmd", width=20, command=hide_cmd)
button_minimize_cmd.pack()

button_show_cmd = tkinter.Button(mainapp, text="Show cmd", width=15, command=show_cmd)
button_show_cmd.pack()

label_space4 = tkinter.Label(mainapp, bg="grey", text="---")
label_space4.pack()

button_Start_L4D2 = tkinter.Button(mainapp, text="Start L4D2",
width=25, bg="#00ff00", command=start_l4d2)
button_Start_L4D2.pack()

button_Quit_L4D2 = tkinter.Button(mainapp, text="Quit L4D2",
width=20, bg="#ff6f00", command=quit_l4d2)
button_Quit_L4D2.pack()

button_Credits = tkinter.Button(mainapp, text="Credits", width=15, command=credits)
button_Credits.pack()

button_quit_prog = tkinter.Button(mainapp, text="Quit Program",
width=10, bg="#ff0000", command=quitting_program)
button_quit_prog.pack()

label_space5 = tkinter.Label(mainapp, bg="grey", text="---------------------------------------")
label_space5.pack()

Var_time_setting_txt = tkinter.StringVar()
Var_time_setting_txt.trace("r", time_txt_read)
label_setting = tkinter.Label(mainapp, bg="grey", textvariable=Var_time_setting_txt)
label_setting.pack()

Var_last_randrange_maps = tkinter.StringVar()
Var_last_randrange_maps.trace("r", first_spin_gui)
label_spin = tkinter.Label(mainapp, bg="grey", textvariable=Var_last_randrange_maps)
label_spin.pack()

label_space6 = tkinter.Label(mainapp, bg="grey", text="---------------------------------------")
label_space6.pack()

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", l4d2_state)
label_stat = tkinter.Label(mainapp, bg="grey", textvariable=var_l4D2)
label_stat.pack()

CMD = gw.getWindowsWithTitle("py.exe")[0]
Python_Ui = gw.getWindowsWithTitle("L4D2 Map Selector")[0]
CMD.minimize()

mainapp.mainloop()
