import pyperclip
import pyautogui
import time

# Esperar 3 segundos
time.sleep(3)

# Obtener el texto del portapapeles
text = pyperclip.paste()

# Presionar cada tecla del texto
pyautogui.write(text)
