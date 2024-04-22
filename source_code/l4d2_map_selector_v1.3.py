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
from py_folder.l4d2_presence import *

WMIC_COMAND : str ="wmic process get description"
GAME : str ="left4dead2.exe"
TIME_FILE : str  ="setting.txt"
CMD_DETECT_FALSE : str ="\033[0;31mleft4dead2.exe is not launched\033[0;37m"
L4D2_TRUE : str  ="L4D2: is launched =)"
L4D2_FALSE : str  ="L4D2: is not launched =("

def welcome_user(ver_file="ver.txt", build_version="v1.3-04.22.2024-08AM"):

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

class very_usseful_func:

    def os_popen_read(self, command):
        """Listing of executed program"""

        global is_launched
        is_launched = os.popen(command).read()

    def track_windows(self, name_of_window):
        """Fullscreen the desired window"""

        global window

        window = gw.getWindowsWithTitle(name_of_window)[0]
        window.activate()
        window.maximize()

    def l4d2_is_not_launched_messagebox(self, title, context):

        box = messagebox.askquestion(title, context)

        if box == "yes":
            l4d2_func().start_l4d2()

        else:
            var_l4D2.set(L4D2_FALSE)
            print(CMD_DETECT_FALSE)

class Generic_func:

    def restart_program():

        print("restart...")
        #os.popen("cd {}".format(os.getcwd()))
        #os.popen("python {}".format("l4d2_map_selector_v1.3.py"))
        os.execv(sys.executable, ["python l4d2_map_selector_v1.3.py"])
        os.popen("wmic process where processid='{}' call terminate".format(os.getpid()))

    def quitting_program():

        """Quitting main program"""

        quit_program = messagebox.askquestion("Quit...", "Are you sure ?")

        if quit_program == "yes":
            mainapp.destroy()

    def credits():
        """ Credits of the program"""
        messagebox.showinfo("L4D2 Map Selector Credits",
        "Made by NoNoDu88\nTested and corrected by NoNoDu88 and FoxTroT\nKef for this icon =)")

class l4d2_func:

    def __init__(self,

                steam_on : str ="\033[1;32mSteam.exe is launched\033[0;37m"
                "\nWait... test if left4dead2.exe is launched in 10 tries:",

                succes_start_cmd : str ="\033[1;32mSucces detect:"
                "\bleft4dead2.exe\n\033[1;32mleft4dead2.exe is succefully started\033[0;37m",

                steam_off : str ="\033[0;31mSteam.exe is not launched\033[0;37m"
                "\nWait... test if left4dead2.exe is launched in 20 tries:"):

        self.steam_on = steam_on
        self.succes_start_cmd = succes_start_cmd
        self.steam_off = steam_off

    def l4d2_state(*args):

        """Check at the starting of the program if the game are launched"""

        print("Check L4D2 is launched...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            print("\033[1;32mSucces detect: left4dead2.exe\033[0;37m")
            var_l4D2.set(L4D2_TRUE)
            messagebox.showinfo("Just checking...", "L4D2 is launched")

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Just checking...",
            "L4D2 is not launched start the game ?")

    @staticmethod
    def start_l4d2():

        """Start left4dead2.exe -> steam://rungameid/550"""

        print("Start L4D2...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            messagebox.showwarning("Just checking...", "L4D2 as already launched")
            print("\033[0;33mleft4dead2.exe: as already launched\033[0;37m")
            very_usseful_func().track_windows("Left 4 Dead 2")

        else:
            l4d2_launched = False
            retry : int = 10
            very_usseful_func().os_popen_read(WMIC_COMAND)

            if is_launched.find("steam.exe") != -1:
                print(l4d2_func().steam_on)
            else:
                retry + 10
                print(l4d2_func().steam_off)

            webbrowser.open("steam://rungameid/550")

            for _ in range(retry):
                very_usseful_func().os_popen_read(WMIC_COMAND)

                if is_launched.find(GAME) != -1:
                    l4d2_launched = True
                    print(l4d2_func().succes_start_cmd)
                    var_l4D2.set(L4D2_TRUE)
                    break

                print("left4dead2.exe not detect")
                time.sleep(2)

            if not l4d2_launched:
                print("\033[0;31mLeft4Dead2 is not installed\033[0;37m\n")
                time.sleep(2)
                Python_Ui.restore()
                messagebox.showerror("Error !", "Left4Dead2 is not installed on your pc =(")
                var_l4D2.set("L4D2: is not installed on your computer =(")
                webbrowser.open("https://store.steampowered.com/app/550/Left_4_Dead_2/")

    def return_to_game():

        """simpli return to game XD"""

        print("Return to game...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            var_l4D2.set(L4D2_TRUE)
            very_usseful_func().track_windows("Left 4 Dead 2")

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Can't Return To game...",
            "You can't return to game L4D2 is not launched start the game ?")

    def quit_l4d2():

        """Stop left4dead2.exe process -> wmic process where name='left4dead2.exe' call terminate"""

        print("Quit L4D2...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            os.popen("wmic process where name='left4dead2.exe' call terminate")
            var_l4D2.set(L4D2_FALSE)
            messagebox.showinfo("Quit L4D2", "left4dead2.exe sucess stopped")

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Can't quit game...",
            "You can't Quit L4D2 is not launched XD start the game ?")

class spin_return_txt:

    def __init__(self,

                File_not_found_message : str ="The setting.txt file has been created"
                " with the time by default (5)",

                Wrong_setting_txt : str ="is not correct input for setting.txt correct is x(in seconds)"
                "or x(in seconds).x(in milliseconds)",

                Default_time : str ="Time for switching program to game"
                "(depend on your pc default is 5 seconds) = 5",

                Wrong_resolution : str ="Setting.txt input has been changed with the time by default (5)",

                pyautogui_input : str ="down"):

        self.File_not_found_message = File_not_found_message
        self.Wrong_setting_txt = Wrong_setting_txt
        self.Default_time = Default_time
        self.Wrong_resolution = Wrong_resolution
        self.pyautogui_input = pyautogui_input

    def time_txt_read(*args):

        '''
        Read setting.txt for checking the value and change Var_time_setting_txt label of gui
        if setting.txt contain "," replace to "."
        '''

        global TIME_FOR_ACTION

        try:
            if os.path.isfile(TIME_FILE):

                with open(TIME_FILE, "r" , encoding="utf-8") as action_time:
                    verif_time_for_action = action_time.read()

                if verif_time_for_action.find(","):
                    fix_time = verif_time_for_action.replace("," , ".")
                    with open(TIME_FILE, "w" , encoding="utf-8") as action_time:
                        action_time.write(fix_time)

                with open(TIME_FILE, "r" , encoding="utf-8") as action_time:
                    action_time.seek(77)
                    TIME_FOR_ACTION = float(action_time.readline()) #int or float number
                    print("Time set on txt", TIME_FOR_ACTION)
                    Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

            else:
                #If setting file as not in racine repertory
                messagebox.showwarning("Setting.txt as been deleted",spin_return_txt().File_not_found_message)
                print("\033[0;33m{}\033[0;37m".format(spin_return_txt().File_not_found_message))

                with open(TIME_FILE, "w", encoding="utf-8") as action_time:
                    action_time.write(spin_return_txt().Default_time)

                with open(TIME_FILE, "r", encoding="utf-8") as action_time:
                    action_time.seek(77)
                    TIME_FOR_ACTION = float(action_time.readline())
                    print("Time set on txt", TIME_FOR_ACTION)
                    Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

        except ValueError:
            #If setting.txt contain wrong argument
            with open(TIME_FILE, "r" , encoding="utf-8") as action_time:
                action_time.seek(77)
                wrong_input = action_time.readline()

            print("\033[0;33mValueError in setting.txt:\033[0;37m {}\033[0;33m {}"
            "\033[0;37m\n{}".format(wrong_input,spin_return_txt().Wrong_setting_txt, 
            spin_return_txt().Wrong_resolution))
            messagebox.showwarning("ValueError !", "{} {} \n\n{}".format(wrong_input,
            spin_return_txt().Wrong_setting_txt, spin_return_txt().Wrong_resolution))

            #Resolution of setting.txt
            with open(TIME_FILE, "r+" , encoding="utf-8") as action_time:
                action_time.truncate()
                action_time.write(spin_return_txt().Default_time)

            #After resolution of setting.txt
            with open(TIME_FILE, "r" , encoding="utf-8") as action_time:
                action_time.seek(77)
                TIME_FOR_ACTION = float(action_time.readline())
                print("Time set on txt", TIME_FOR_ACTION)
                Var_time_setting_txt.set("(Txt)Setting= {}".format(TIME_FOR_ACTION))

    def first_spin_gui(*args):
        """first value of random 0, 90"""
        Var_last_randrange_maps.set("(Spin)number= None")

    def determine_spin_time():

        """Counts the time for the game to go full screen"""

        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            time_spin_start = perf_counter()

            while True:
                very_usseful_func().track_windows("Left 4 Dead 2")

                if window.isMaximized == True:
                    time_spin_stop = perf_counter()
                    good_time = time_spin_stop - time_spin_start + 0.1

                    with open(TIME_FILE, "a",
                              encoding="utf-8") as final_result_determination:

                        final_result_determination.seek(77)
                        final_result_determination.truncate()
                        final_result_determination.write("{:.2f}".format(good_time))
                        print("Time set on txt {:.2f}".format(good_time))
                        Var_time_setting_txt.set("(Txt)Setting= {:.2f}".format(good_time))
                        Python_Ui.activate()
                        messagebox.showinfo("Switching time...",
                                            "Switching time are succefully apply into Settings.txt")
                    break

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Switching time determination impossible...",
            "Determination are impossible because your L4D2 is not launched start the game ?")

    #def spin_roulette(number_of_times, whait_s=0):
        #for _ in range(number_of_times):
            #time.sleep(whait_s)
            #gui.press(spin_return_txt().pyautogui_input)

    def spin():

        """Randomize map selection"""

        print("Spin...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:

            var_l4D2.set(L4D2_TRUE)
            spin_return_txt().time_txt_read()

            maps = random.randrange(0, 91)
            print("Spin= {}{}".format(str(maps), "/90"))
            Var_last_randrange_maps.set("(Spin)number= {}{}".format(str(maps), "/90"))

            very_usseful_func().track_windows("Left 4 Dead 2")
            time.sleep(float(TIME_FOR_ACTION))
            game = gw.getWindowsWithTitle("Left 4 Dead 2")[0]
            l4d2 = round(window.width * 0.2442), round(window.height * 0.4796)
            print("Your game resolution= {}x{}\nmap button location= {}".format(window.width, window.height, l4d2))
            gui.moveTo(l4d2)
            gui.press("enter")
            gui.moveTo(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

            if maps >= 10:

                #75% of maps
                for _ in range(round(maps * 0.75)):
                    gui.press(spin_return_txt().pyautogui_input)
                #15 % of maps
                for _ in range(round(maps * 0.20)):
                    time.sleep(0.050)
                    gui.press(spin_return_txt().pyautogui_input)
                #5 % of maps
                for _ in range(round(maps * 0.05)):
                    time.sleep(0.50)
                    gui.press(spin_return_txt().pyautogui_input)

            elif maps < 10:
                for _ in range(maps):
                    time.sleep(0.50)
                    gui.press(spin_return_txt().pyautogui_input)

            #gui.hotkey("win", "prntscrn") screen function for send to your friend disabled.
            gui.press("enter")
            time.sleep(1.5)
            Python_Ui.activate()
            gui.moveTo(ctypes.windll.user32.GetSystemMetrics(0)/2, ctypes.windll.user32.GetSystemMetrics(1)/2)

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Can't spin...",
            "You can't spin L4D2 is not launched start the game ?")

    def finish_random():

        """return to game and press escape button for multiplayer lobby"""

        print("Return to game and press escape...")
        very_usseful_func().os_popen_read(WMIC_COMAND)

        if is_launched.find(GAME) != -1:
            var_l4D2.set(L4D2_TRUE)
            spin_return_txt().time_txt_read()
            very_usseful_func().track_windows("Left 4 Dead 2")
            time.sleep(float(TIME_FOR_ACTION))
            gui.press("esc")

        else:
            very_usseful_func().l4d2_is_not_launched_messagebox("Can't finish Spin...",
            "You can't finish spin L4D2 is not launched start the game ?")

def set_time_gui():

    """Set the time on Setting.txt file for switching time of aplication to game"""

    with open(TIME_FILE, "r+", encoding="utf-8") as action_time:

        action_time.seek(77)
        action_time.truncate()
        action_time.write(txt_time_e.get())

        Var_time_setting_txt.set("(Txt)Setting= {}".format(txt_time_e.get()))
    spin_return_txt().time_txt_read()

def hide_cmd():
    """Hide cmd prompt"""
    CMD.minimize()
    print("goodbye =(")

def show_cmd():
    """Show cmd prompt"""
    CMD.restore()
    print("hi =)")
    Python_Ui.activate()

welcome_user()
discord_rpc().connect()

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
mainapp.geometry("+{}+{}".format(round(ctypes.windll.user32.GetSystemMetrics(0)/2), round(ctypes.windll.user32.GetSystemMetrics(1)/2)))
mainapp.resizable(False, False)

try:
    CMD = gw.getWindowsWithTitle("py.exe")[0]
except IndexError:
    CMD = gw.getWindowsWithTitle("l4d2_map_selector_v1.3.py")[0]

CMD.minimize()

Python_Ui = gw.getWindowsWithTitle("L4D2 Map Selector v1.3")[0]

#Gui label and button
label_welcome = tkinter.Label(tab1, bg="#333333", fg="#EA1818",
text="Welcome to L4D2 Map Selector v1.3", font=("Arial"))
label_welcome.grid(row=0, column=0)

label_space = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="")
label_space.grid(row=1, column=0)

button_spin = ttk.Button(tab1, text="Spin", width=30, command=spin_return_txt.spin,
style="First.TButton")
button_spin.grid(row=2 ,column=0)

button_End = ttk.Button(tab1, text="Close choice (multi lobby)",
width=25, command=spin_return_txt.finish_random, style="First.TButton")
button_End.grid(row=3 ,column=0)

button_Return_Game = ttk.Button(tab1, text="Return to game",
width=20, command=l4d2_func.return_to_game, style="First.TButton")
button_Return_Game.grid(row=4 ,column=0)

label_space2 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="---", font=("Arial", 10))
label_space2.grid(row=5 ,column=0)

button_Start_L4D2 = ttk.Button(tab1, text="Start L4D2",
width=30, command=l4d2_func.start_l4d2, style="Start_L4D2.TButton")
button_Start_L4D2.grid(row=6 ,column=0)

button_Quit_L4D2 = ttk.Button(tab1, text="Quit L4D2",
width=25, command=l4d2_func.quit_l4d2, style="Quit.TButton")
button_Quit_L4D2.grid(row=7 ,column=0)

label_space3 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="---", font=("Arial", 10))
label_space3.grid(row=8 ,column=0)

button_restart = ttk.Button(tab1, text="Restart program", width=30,
style="Start_L4D2.TButton", command=Generic_func.restart_program)
button_restart.grid(row=9 ,column=0)

button_quit_prog = ttk.Button(tab1, text="Quit Program",
width=25, command=Generic_func.quitting_program, style="Quit_Program.TButton")
button_quit_prog.grid(row=10 ,column=0)

button_Credits = ttk.Button(tab1, text="Credits", width=20, command=Generic_func.credits,
style="Credits.TButton")
button_Credits.grid(row=11 ,column=0)

label_space4 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF", text="")
label_space4.grid(row=12, column=0)

label_space5 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
text="------------------------------------------------------------", font=("Arial", 10))
label_space5.grid(row=13 ,column=0)

Var_last_randrange_maps = tkinter.StringVar()
Var_last_randrange_maps.trace("r", spin_return_txt.first_spin_gui)

label_spin = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
textvariable=Var_last_randrange_maps, font=("Arial", 10))
label_spin.grid(row=14 ,column=0)

var_l4D2 = tkinter.StringVar()
var_l4D2.trace("r", l4d2_func.l4d2_state)

label_stat = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
textvariable=var_l4D2, font=("Arial", 10))
label_stat.grid(row=15 ,column=0)

label_space6 = tkinter.Label(tab1, bg="#333333", fg="#FFFFFF",
text="------------------------------------------------------------", font=("Arial", 10))
label_space6.grid(row=16 ,column=0)

label_Time = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF",
                           text="Switch Time :", font=("Arial", 12))
label_Time.pack()

txt_time_e = ttk.Entry(tab2, width=10)
txt_time_e.insert(0, "5.0")
txt_time_e.pack()

txt_time_button = ttk.Button(tab2, text="Set", width=5, command=set_time_gui,
style="Set.TButton")
txt_time_button.pack()

label_space = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF", text="")
label_space.pack()

button_check = ttk.Button(tab2, text="Check L4D2 is launched", width=30, command=l4d2_func.l4d2_state,
style="Second.TButton")
button_check.pack()

button_determine_spin = ttk.Button(tab2, text="Determine switching time", width=25,
command=spin_return_txt.determine_spin_time, style="Second.TButton")
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
Var_time_setting_txt.trace("r", spin_return_txt.time_txt_read)

label_setting = tkinter.Label(tab2, bg="#333333", fg="#FFFFFF",
textvariable=Var_time_setting_txt, font=("Arial", 10))
label_setting.pack()

mainapp.protocol("WM_DELETE_WINDOW", Generic_func.quitting_program)
mainapp.mainloop()