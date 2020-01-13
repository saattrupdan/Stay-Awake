def stay_awake(interval: int = 3, failsafe: bool = False):
    ''' Keeps the computer awake.

    INPUT
        interval: int = 3
            How often the movement should occur, in minutes
        failsafe: bool = False
            Enable PyAutoGUI's failsafe, which disables the GUI if the mouse
            is moved to the top left corner
    '''
    import pyautogui
    from time import sleep
    from datetime import datetime
    from itertools import cycle

    pyautogui.FAILSAFE = failsafe
    for even in cycle([True, False]):
        sleep(interval * 60)
        pyautogui.press('shift')

        # Move cursor one pixel down or up
        vertical_change = 1 if even else -1
        pyautogui.move(0, vertical_change)
        
        print(f"Movement made at {datetime.now().time()}")

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-i', '--interval', type = int, default = 3)
    parser.add_argument('-f', '--failsafe', type = bool, default = False)
    args = vars(parser.parse_args())

    stay_awake(**args)
