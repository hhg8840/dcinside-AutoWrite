import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
    print(pyautogui.position())
    time.sleep(1)