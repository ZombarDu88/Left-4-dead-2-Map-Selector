#coding:utf-8
import os

def libs_installer(enter_message="press enter:"):
    try:
        import pyautogui
        import pygetwindow
        import requests
        from pypresence import Presence

        print("Required libs are alerty installed you can launch the program =)")
        input(enter_message)

    except ModuleNotFoundError:
        print("Installing libs...")

        try:
            os.system("pip install pyautogui pygetwindow pypresence requests")
            print("Required libs are installed you can launch the program =)")
            input(enter_message)

        except:
            print("ERROR: pip is not installed or idk")
            input(enter_message)

libs_installer()
