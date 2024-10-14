# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_5.py' и напишите весь код в нём.
# Заменил 'module_1_5.py' на '6-PZ-Izmenayemie-I-Neizmenayemie-Obiekti-Kortegi.py'.

# 2. Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# Выполните операции вывода кортежа immutable_var на экран.
immutable_var = (7, 5, "привет", 8, True, 6, "45", False) # Создал переменную типа кортеж с разными типами данных
print(immutable_var) # Вывел на экран целиком
print(immutable_var[2][0:6:1], immutable_var[1], immutable_var[4]) # Вывел на экран с обращением по индексу кортежа
print()

# 3. Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
print(immutable_var)
print(immutable_var[::], immutable_var[0]+3, immutable_var[6][::]+"68") # Кортеж не изменился. immutable_var[0] = 2 не возможно изменить! immutable_var[6][::] = "68" не возможно изменить.
# Объяснение: кортеж хранит ссылки на элементы. Строка уже создана и не изменяется! Числовое значение тоже создано и не изменяется.
# НО ВЫЗОВИ ИХ ПО ОТДЕЛЬНОСТИ НАД НИМИ МОЖНО СОВЕРШИТЬ ОПЕРАЦИИ
print()

# 4. Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.
mutable_list = [1, 2, "пока", "мне 45", 78]
print(mutable_list)
mutable_list[0]=15
mutable_list[1]=5
mutable_list[3]= "мне нет 45-ти"
print(mutable_list)


