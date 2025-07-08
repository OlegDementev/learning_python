# Словари в Python

# Словарь - это изменяемы тип данных. Структура < dict = {ключ: значение} >
# Может содержать в ключах - только хешируемые объекты, в значених - любые объекты


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
