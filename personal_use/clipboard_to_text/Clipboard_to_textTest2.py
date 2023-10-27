import pyperclip
import pydirectinput
import time

# Esperar 3 segundos
time.sleep(3)

# Obtener el texto del portapapeles
text = pyperclip.paste()

# Presionar cada tecla del texto rápidamente
for char in text:
    pydirectinput.press(char)
    time.sleep(0.01)  # delay between key presses