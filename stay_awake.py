import pyautogui # used to move cursor
import time # used for sleep()
from datetime import datetime # used to display current time
import itertools as it # provides tools for iterators, like count()

# disable pyautogui's default failsafe
pyautogui.FAILSAFE = False

# set how often movement should occur, in minutes
interval = 3

# infinite loop
for i in it.count():

    # wait interval many minutes
    time.sleep(interval * 60)
    
    # move cursor one pixel down when i is even, and one pixel
    # up when i is odd
    if i % 2 == 0:
        pyautogui.move(0, 1)
    else:
        pyautogui.move(0, -1)
    
    print(f"Movement made at {datetime.now().time()}")
