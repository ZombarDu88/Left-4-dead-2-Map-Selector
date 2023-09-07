#coding:utf-8
import os
import time
import webbrowser
import zipfile
import tkinter
from tkinter import ttk, messagebox

def libs_installer():

    try:
        pip_packages = os.popen("pip list").read()

    except Exception:
            messagebox.showerror("ERROR...", "pip is not installed")
            webbrowser.open("https://phoenixnap.com/kb/install-pip-windows")
            os.system("start cmd")
            quit()

    if pip_packages.find("pyautogui" and "pygetwindow" and "pypresence" and "requests") != -1:
        messagebox.showinfo("Install libs...",
        "Required libs are alerty installed you can launch the program =)")

    else:
        os.system("pip install pyautogui pygetwindow pypresence requests")
        messagebox.showinfo("Install libs...",
        "Required libs are installed you can launch the program =)")

def current_version_file(*args, ver_file="ver.txt", current_ver_file="v1.3-02.09.2023-10AM"):

    if os.path.isfile(ver_file):
        with open("ver.txt", "r", encoding="utf-8") as ver_indicator:
            current = ver_indicator.readline()
            gui_build = "Current build:"+" "+current
            var_build.set(gui_build)

    else:
        with open(ver_file, "a", encoding="utf-8") as ver_indicator:
            ver_indicator.write(current_ver_file)

        with open(ver_file, "r", encoding="utf-8") as ver_indicator:
            current = ver_indicator.readline()
            gui_build = "Current build:"+" "+current
            var_build.set(gui_build)

def updater(url="https://github.com/ZombarDu88/Left-4-dead-2-Map-Selector/archive/refs/heads/updater_folder.zip", 
    name_folder="L4D2.Map.Selector.v1.3.zip"):
    
    try:
        os.system("pip install requests")
        import requests

    except Exception:
         messagebox.showerror("ERROR...", "pip is not installed")
         webbrowser.open("https://phoenixnap.com/kb/install-pip-windows")
         os.system("start cmd")
         quit()

    update = requests.get(url)
    open(name_folder, "wb").write(update.content)
    messagebox.showinfo("Download update...", "{}\n\n{}\n\n{}".format("Updated files are succesfully installed in ->",
    os.getcwd(), "you can extract and replace files install"))

mainapp = tkinter.Tk()
mainapp.title("Libs installer and updater")
mainapp.eval("tk::PlaceWindow . center")
mainapp.resizable(False, False)

first_labbel = ttk.Label(mainapp, text="Libs installer and updater v1.0")
first_labbel.pack()

label_space = ttk.Label(mainapp, text="---")
label_space.pack()

libs_button = ttk.Button(mainapp, text="Install libs", width=30, command=libs_installer)
libs_button.pack()

updatter_button = ttk.Button(mainapp, text="Download update", width=25, command=updater)
updatter_button.pack()

label_space2 = ttk.Label(mainapp, text="---")
label_space2.pack()

var_build = tkinter.StringVar()
var_build.trace("r", current_version_file)
label_build = ttk.Label(mainapp, textvariable=var_build)
label_build.pack()

mainapp.mainloop()