import ctypes
import time

def turn_off_monitor():
    # Выключение экрана
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)  # WM_SYSCOMMAND, SC_MONITORPOWER, MONITORPOWER_OFF
    time.sleep(10)  # Ждём 10 секунд

# Выключаем экран на 10 секунд
turn_off_monitor()
