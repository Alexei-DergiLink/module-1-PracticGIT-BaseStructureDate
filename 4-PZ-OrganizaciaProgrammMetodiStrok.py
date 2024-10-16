# Практическая работа по уроку "Организация программ и методы строк"
#
# Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_4.py' и напишите весь код в нём.
#
# 2. Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
from idlelib.colorizer import color_config
from queue import PriorityQueue

# 3. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.
#
# Примечания:
# Для вывода значений на экран используйте функцию print().
# Для вызова методов строк используйте операцию точки '.'.
# Дополнительно о всех методах строк можно узнать здесь.
# Пример результата выполнения программы:
#
# Код:
# name = input()
# print(name.upper())

# Ввод в консоль:
# Urban
# Вывод на консоль:
# URBAN

print()
print("Напишите текс с новой строки: ")
my_strig = input()
# my_strig = "Я сегодня научился новому"
leng = len(my_strig)
print(my_strig, " = ", leng, "символов")
print("Выведите его верхним регистром: ", my_strig.upper())
print("Выведите его нижним регистром: ", my_strig.lower())
print("Удалите все пробелы: ", my_strig.replace(" ", ""))
print("Выведите первый символ: ", my_strig[0:1])
print("Выведите крайний символ: ", my_strig[-1])
# print(my_strig[24:25]) # это когда известно количество символов и индексы (в данном случае их 25).
print()
print("Конец задания.")


