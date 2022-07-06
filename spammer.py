message = "hello, this is a simple spammer"

import time
import pyautogui

def spambot():
    time.sleep(5)
    
    text = message
    for i in text:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        
spambot()