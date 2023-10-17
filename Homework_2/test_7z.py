""" Задание 1
Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x)."""

from checkers import checkout

folder_out = "/home/irina/folder_out/"
folder_ext = "/home/irina/folder_ext/"


# показать файлы в папке не запуская
def test_7z_l():
    assert checkout(f'cd {folder_out}; 7z l ./archiv.7z', "Listing archive: ./archiv.7z"), "test_l FAIL"


# разархивировать файлы из папки
def test_7z_x():
    assert checkout(f'cd {folder_ext}; 7z x {folder_out}archiv.7z', "Everything is Ok"), "test_x FAIL"