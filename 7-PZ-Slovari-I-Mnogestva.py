# 1. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#   - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.

my_dict = {"Alexei id: ":555, "Denis id: ": 567, "Nikolay id ": 752, "Номер в очереди ": 0000}
print(my_dict)
print(my_dict["Nikolay id "]) # вывод по существующему
my_dict["Количество обращений "] = 15
print(my_dict.get("Sasha")) # вывод по не существующему ключу
my_dict.update({"Обращений сегодня ": 2,
                "Обращений вчера ": 5})
print(my_dict)
print()
print()

new_dict = my_dict.pop("Nikolay id ")
print(new_dict)
print(my_dict, type(my_dict))
print()


# 2. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.

my_set = {15, 18, 18, 23, True, 6, True, "лево", "лево", (3,3,8), (3,3,8)}
print(my_set)
my_set.add("право")
my_set.add("право")
my_set.add("право") # примечание - добавилось только одно "право" за счет уникальности
my_set.add((2,1))
print(my_set)
my_set.remove(18)
print(my_set)
print()

print("Ссылка на GitHub - https://github.com/Alexei-DergiLink/module-1-PracticGIT-BaseStructureDate/blob/main/7-PZ-Slovari-I-Mnogestva.py")

print()
print("Больше о методах словарей - https://docs.python.org/3/library/stdtypes.html#dict")
print("Больше о методах множеств - https://docs.python.org/3/library/stdtypes.html#set")
