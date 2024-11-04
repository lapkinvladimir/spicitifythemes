import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import time
from pathlib import Path


def open_image(image_path):
    # Создаем новое окно
    window = tk.Toplevel()
    window.title("Изображение")

    # Загружаем изображение
    img = Image.open(image_path)

    # Изменяем размер изображения, чтобы оно поместилось в маленькое окно
    img.thumbnail((200, 200))  # Измените размеры по вашему желанию
    img_tk = ImageTk.PhotoImage(img)

    # Создаем метку для отображения изображения
    label = tk.Label(window, image=img_tk)
    label.image = img_tk  # сохраняем ссылку на изображение
    label.pack()

    # Устанавливаем размер окна
    window.geometry("220x220")  # Размеры окна (включая заголовок)


def turn_off_monitor():
    # Выключение экрана
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)  # WM_SYSCOMMAND, SC_MONITORPOWER, MONITORPOWER_OFF
    time.sleep(10)  # Ждём 10 секунд
    # Включение экрана (вызываем событие мыши, чтобы включить экран)
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)  # Включаем монитор


def main():
    # Укажите путь к изображению
    image_path = Path("wallpaper.jpg").resolve()  # Замените на путь к вашему изображению

    # Создаем главное окно
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Открываем изображение 100 раз
    for _ in range(100):
        open_image(image_path)

    root.mainloop()

    # Выключаем экран на 10 секунд после открытия всех окон
    turn_off_monitor()


if __name__ == "__main__":
    main()
