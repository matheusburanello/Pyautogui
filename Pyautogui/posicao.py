import pyautogui
import time

print("Pressione Ctrl+C para parar!")
while True:
    x, y = pyautogui.position()
    print(f"Posição do mouse: X={x} Y={y}")
    time.sleep(0.1)
