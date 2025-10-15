import pyautogui
import time

pyautogui.hotkey('win', 'd')
time.sleep(1)

time.sleep(2)
pyautogui.rightClick(x=500,y=300)
pyautogui.click(x=502,y=320)
pyautogui.doubleClick(x=510,y=350)