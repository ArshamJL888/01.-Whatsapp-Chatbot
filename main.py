import random
import pyautogui
import time
texts = ["Hello", 'Whats up?', "How are you?", "What happened?", 'I am a Robot', 'Hello From Python!']
pyautogui.click('textbox.png')
for i in range(5):
    pyautogui.write(random.choice(texts), interval=0.1)
    pyautogui.hotkey('shift', 'enter')
    time.sleep(1)
pyautogui.press('enter')