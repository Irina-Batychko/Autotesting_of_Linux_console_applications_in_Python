""" Задание 2 *
• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
"""
from checkers import checkout, getout

Homework_2 = "/home/irina/PycharmProjects/Autotesting_of_Linux_console_applications_in_Python/Homework_2/"

def test_7z_h():
    crc32_hash = getout(f'cd {Homework_2}; crc32 checkers.py').upper()
    assert checkout(f'cd {Homework_2}; 7z h checkers.py', crc32_hash), "test_h FAIL"
