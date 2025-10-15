import pyautogui
import time
import pyperclip

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)

pyperclip.copy('https://www.youtube.com/')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(450, 150)

pyperclip.copy('Dados')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')