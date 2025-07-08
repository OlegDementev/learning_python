# Словари в Python

# Словарь - это изменяемы тип данных. Структура < dict = {ключ: значение} >
# Может содержать в ключах - только хэшируемые объекты, в значениях - любые объекты


prime_dict_00 = {}
print(f"Пустой словарь: {prime_dict_00}")

prime_dict_01 = dict()
print(f"Пустой словарь: {prime_dict_01}")

prime_dict_02 = dict(name="OLE_GG", age=29, job="teacher")
print(f"Словарь через функцию dict(): {prime_dict_02}")

prime_dict_03 = dict(((12, "O"), (15, "L"), (17, "E")))
prime_dict_04 = dict([(12, "G"), (15, "D"), (17, "O")])
prime_dict_05 = dict([[12, "V"], [15, "CH"], [17, "OH"]])
print(
    f"Через списки и кортежи и функцию dict():\n{prime_dict_03}\n{prime_dict_04}\n{prime_dict_05}"
)

prime_dict_06 = dict().fromkeys((1, 2), "Press_f5")
print(f"Словарь через метод fromkeys: {prime_dict_06}")

elem_dict = prime_dict_02["name"]
print(f"Доступ к значению через ключ 'name': {elem_dict}")


keys = ["name", "age", "job"]
values = ["Timur", 28, "Teacher"]
dict_as_zip = dict(zip(keys, values))
print(f"Создание словаря с помощью генератора через функцию zip(): {dict_as_zip}")

# оператор in проверяет, содержит ли словарь искомы ключ
print("name" in dict_as_zip, f", если содержит")

# функции min, max, sum
dct_dgt = {1: "1", 2.5: "2", 3: "3"}

print(
    f"Sum {sum(dct_dgt)}  Min {min(dct_dgt)} Max {max(dct_dgt)} только для словарей с цифровыми ключами"
)

# методы словарей keys() values() items()
# Словарные методы items(), keys(), values() возвращают не совсем обычные списки.
# Тип этих списков –  dict_keys в отличие от обычных списков  list.
# Методы обычных списков недоступны для списков типа dict_keys.
capitals = {"Россия": "Москва", "Франция": "Париж", "Чехия": "Прага"}
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())

# распаковка словаря

print(*capitals)

# оператор in для проверки ключа
if "Россия" in capitals:
    print("В словаре есть ключ Россия")
# оператор in для проверки значения
if "Париж" in capitals.values():
    print("В словаре есть значение Париж")

# Добавление и изменение элементов в словаре
info = {"name": "Sam", "age": 28, "job": "Teacher"}

info["name"] = "Timur"  # изменяем значение по ключу name
info["email"] = "timyr-guev@yandex.ru"  # добавляем в словарь элемент с ключом email

print(info)

# Метод get()
print(info.get("name", 0))
print(info.get("name1", "выводить если не нашли такой ключ"))

# Метод update()
# операторы | и |= реализуют операцию конкатенации словарей.
info1 = {"name": "Bob", "age": 25, "job": "Dev"}
info2 = {"age": 30, "city": "New York", "email": "bob@web.com"}
info3 = {"name": "Bob", "age": 25, "job": "Dev"}
info4 = {"age": 30, "city": "New York", "email": "bob@web.com"}
info1.update(info2)
info3 |= info4
print(info1)
print(info3)

# Метод setdefault(key, default) позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
# Аргументы
# key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать пару ключ: значение
# default: значение, которое будет использовано при добавлении нового элемента в словарь.
info = {"name": "Bob", "age": 25}

name1 = info.setdefault("name")  # параметр default не задан
name2 = info.setdefault("name", "Max")  # параметр default задан

print(name1)
print(name2)

info = {"name": "Bob", "age": 25}

job = info.setdefault("job", "Dev")
print(info)
print(job)

# С помощью оператора del можно удалять элементы словаря по определенному ключу.

info = {"name": "Sam", "age": 28, "job": "Teacher", "email": "timyr-guev@yandex.ru"}

del info["email"]  # удаляем элемент имеющий ключ email
del info["job"]  # удаляем элемент имеющий ключ job

print(info)

# Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением.
#  Если требуется получить само значение удаляемого элемента, то нужен метод pop().

info = {"name": "Sam", "age": 28, "job": "Teacher", "email": "timyr-guev@yandex.ru"}

email = info.pop("email")  # удаляем элемент по ключу email, возвращая его значение
job = info.pop("job")  # удаляем элемент по ключу job, возвращая его значение

print(email)
print(job)
print(info)

# Единственное отличие этого способа удаления от оператора del — он возвращает удаленное значение.
#  В остальном этот способ идентичен оператору del.
# В частности, если удаляемого ключа в словаре нет, возникнет ошибка KeyError.
# ​Чтобы ошибка не появлялась, этому методу можно передать второй аргумент.
# Он будет возвращен, если указанного ключа в словаре нет.
# Это позволяет реализовать безопасное удаление элемента из словаря:
# surname = info.pop('surname', None)
# Если ключа surname в словаре нет, то в переменной surname будет храниться значение None.

# Метод popitem()
# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).

info = {"name": "Bob", "age": 25, "job": "Dev"}

info["surname"] = "Sinclar"

item = info.popitem()

print(item)
print(info)

# Метод clear()
# Метод clear() удаляет все элементы из словаря.

info = {"name": "Bob", "age": 25, "job": "Dev"}

info.clear()

print(info)

# Метод copy()
# Метод copy() создает поверхностную копию словаря.


info = {"name": "Bob", "age": 25, "job": "Dev"}

info_copy = info.copy()
info_copy["name"] = "Olegg"

print(info_copy)
