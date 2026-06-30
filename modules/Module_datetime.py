from datetime import datetime
import time

# time.sleep(5)
# current=datetime.now().strftime("%d/%B/%Y, %H:%M:%S")
# print(current)


import pyautogui
import time
time.sleep(4)
pyautogui.typewrite("hey",interval=0.05)
for i in range(3):
    print(pyautogui.typewrite(" hey bro ",interval=0.05))