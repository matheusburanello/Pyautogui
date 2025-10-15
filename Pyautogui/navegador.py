import pyautogui
import time

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)

pyautogui.write('https://www.google.com/')
pyautogui.press('enter')