import pyperclip
import pyautogui
import time

# Wait for 3 seconds
time.sleep(3)

# Get the text from the clipboard
text = pyperclip.paste()

# Split the text into lines
#lines = text.split('\n')
# Split the text into lines
lines = text.splitlines()

import pdb
#pdb.set_trace()
print(lines)
# Type each line individually
for line in lines:
    pyautogui.typewrite(line)
    time.sleep(0.2)
    pyautogui.press('enter')
