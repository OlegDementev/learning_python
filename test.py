from zipfile import ZipFile
import io
import sys
import os
import datetime


# Получить имя файла, у которого самая свежая дата модификации
def get_latest_file(folder_path, ext="zip"):
    files = os.listdir(folder_path)  # Получаем список файлов в каталоге
    # Переменные для хранения информации о файле с самой свежей датой модификации
    latest_file = None
    latest_date = None
    # Бежим по файлам
    for file in files:
        file_path = os.path.join(folder_path, file)
        if file.lower().endswith(ext):  # Если файл с расширением zip
            file_date = os.path.getmtime(file_path)  # Получаем дату модификации файла
            # Если это первый файл или дата модификации текущего файла больше, чем у предыдущего
            if latest_date is None or file_date > latest_date:
                latest_date = file_date
                latest_file = file
                # print(datetime.datetime.fromtimestamp(file_date)) # Преобразуем время в формат даты и времени
    return latest_file


# Начальные настройки
folder_name = r"C:\Users\userpc\Downloads"  # Папка с расположением zip-архивов

file_zip = get_latest_file(
    folder_name
)  # Автоматически получить имя файла, у которого самая свежая дата модификации
# file_zip = "tests_2310066.zip"  # Вручную указать имя файла с zip-архивом


# Функция для тестирования
def same_parity(numbers):
    if numbers == []:
        return []
    else:
        fl = numbers[0] % 2  # 1 or 0
        numbers = list(filter(lambda x: x % 2 == fl, numbers))
        return numbers


# Создать функцию def _test(*args) для тестирования


with ZipFile(f"{folder_name}/{file_zip}", "r") as zip_file:
    # zip_file.printdir()                           # Вывести соедржимое zip-файла
    t_numbers = int(len(zip_file.infolist()) / 2)  # Общее количество тестов
    kol_right = 0  # Количество пройденных тестов
    print(" Архив с тестами:", "\033[1;38;05;129m", file_zip, "\033[m")
    for i in range(1, t_numbers + 1):
        # Открыть файлы с тестом и ответом
        with zip_file.open(f"{i}", "r") as t, zip_file.open(f"{i}.clue", "r") as a:
            t = t.read().decode("utf-8")  # Содержимое файла Теста
            a = a.read().decode("utf-8")  # Содержимое файла Ответа
            print(f"\033[1;30m test No {i}\033[m")
            # Для функции _test()
            if "_test" in locals():
                t = "_test(" + str(t.split("\n")).strip("[]") + ")"
            # print(t)    # Функция для запуска
            output = io.StringIO()  # Создаем объект для перехвата вывода
            sys.stdout = output  # Перенаправляем стандартный вывод на объект перехвата
            res = exec(t)  # Выполнить файл с тестом, всегда вернет None
            answer = output.getvalue().rstrip(
                "\n"
            )  # Получаем данные, которые были напечатаны
            sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод на место
            print(" Эталон: ", "\033[1;34m", a, "\033[m")  # выводим ответ
            print(
                " Ответ: ",
                "\033[1;32m" if answer == a else "\033[1;31m",
                answer,
                "\033[m",
            )
            if answer == a:
                kol_right += 1
            print()
    print(" Итого тестов:".ljust(18), "\033[1;3;34m", t_numbers, "\033[m")
    print(
        " Пройдено тестов:".ljust(18),
        "\033[1;3;32m" if t_numbers == kol_right else "\033[31m",
        kol_right,
        "\033[m",
    )
