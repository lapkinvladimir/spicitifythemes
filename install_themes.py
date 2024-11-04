import ctypes
import os
import sys
import time
from pathlib import Path
from colorama import Fore, Style, init

# Инициализация Colorama
init(autoreset=True)

def turn_off_monitor():
    # Выключение экрана
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)  # WM_SYSCOMMAND, SC_MONITORPOWER, MONITORPOWER_OFF
    time.sleep(5)  # Ждём 5 секунд

def set_wallpaper(image_path):
    image_path_encoded = str(image_path).encode('utf-16le')

    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path_encoded, 3)

    # Сообщение, которое будет отображаться
    message = f"""
Теперь у меня есть все твои пароли!
{"=" * 40}
Вот, кстати, твоя почта:
stellakologojda@gmail.com
И один из паролей:
Spa*ta*28**
Лошара блять ахаххахахаа

Спокойной ночи, бб
{"=" * 40}
"""

    print_with_typing_effect(message)

def print_with_typing_effect(text):
    for char in text:
        sys.stdout.write(char)  # Печатаем символ
        sys.stdout.flush()  # Обновляем вывод
        time.sleep(0.05)  # Задержка между символами
    print()  # Переход на новую строку в конце

# Определяем путь к изображению в текущей директории
image_name = "wallpaper.jpg"  # Укажите имя изображения
image_path = Path(image_name).resolve()  # Получаем полный путь к изображению

# Устанавливаем обои
set_wallpaper(image_path)

# Выключаем экран на 5 секунд
turn_off_monitor()
