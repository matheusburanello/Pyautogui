import pyautogui
import time 
import subprocess

subprocess.Popen('notepad')
time.sleep(2)

pyautogui.write("Ola, este e um teste automatizado", interval=0.1)
