"""
Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""
import subprocess


def find_text_in_command_output(command, text):
    result = subprocess.run(command, capture_output=True, shell=True, text=True, encoding='utf-8')
    output = result.stdout
    if result.returncode == 0:
        output = result.stdout.split()
        if text in output:
            print("Команда выполнена успешно и текст найден.")
            return True
        print("Команда не выполнена и текст не найден.")
        return False


if __name__ == "__main__":
    find_text_in_command_output("cat /etc/os-release", "jammy")
