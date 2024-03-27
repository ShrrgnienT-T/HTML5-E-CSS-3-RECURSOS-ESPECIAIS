import pyautogui
import keyboard
import time

def toggle_video():
    pyautogui.hotkey('ctrl', 'shift', ',')

# Atalho global
keyboard.add_hotkey('ctrl+shift+tab', toggle_video)

# Mantém o script em execução
while True:
    time.sleep(1)