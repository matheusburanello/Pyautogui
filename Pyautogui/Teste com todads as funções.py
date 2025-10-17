#atividade minimizar as telas
import pyautogui
import time
import subprocess

pyautogui.hotkey('win', 'm')
time.sleep(1)

# criar uma nova pasta na area de trabalho
pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.write("Teste atividade", interval=0.1)
pyautogui.press('enter')

# Entra na pasta
pyautogui.doubleClick(x=350, y=70)
time.sleep(2)

# Criar um arquivo de texto
pyautogui.rightClick(x=500,y=300)
pyautogui.click(x=600,y=560)
pyautogui.click(x=600,y=620)
pyautogui.moveTo(x=750,y=840)
pyautogui.click(x=750,y=840)

# Nomeando o arquivo
pyautogui.write("Arquivo", interval=0.1)
pyautogui.press('enter')

# Trablhando no arquivo texto
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=750,y=700)
pyautogui.write("Codigo funcionando", interval=0.1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
