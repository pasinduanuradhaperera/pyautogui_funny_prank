# pyautogui for funny prank
# developed by paecho

import pyautogui as gui
import time

time.sleep(10)

# Go to Desktop
gui.keyDown("win")
gui.press("d")
gui.keyUp("win")

# open start menue
gui.press("win")

time.sleep(2)
# search notepad
gui.write("notepad")
gui.press("enter")

# wait to open
time.sleep(10)

# type you messege
for i in range(100):
    gui.write("your messege here")
    gui.press("enter")
