# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Предисловие:
# Сложность подобных задач заключается в:
# Отсутствии чёткого алгоритма решения. Его вы должны придумать сами на основе полученных ранее знаний (синтаксиса и инструментов).
# Объединении большинства тем изученного модуля.
# Предполагаемом большом объёме решения.
# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
from gc import garbage
from tkinter.font import names


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 4], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
sorted_students = sorted(students)
itog_dict = {sorted_students[0]:grades[0], sorted_students[1]:grades[1], sorted_students[2]:grades[2], sorted_students[3]:grades[3], sorted_students[4]:grades[4]}
itog_dict ["Aaron"] = sum (itog_dict ["Aaron"]) / len(itog_dict ["Aaron"])
itog_dict ["Bilbo"] = sum (itog_dict ["Bilbo"]) / len(itog_dict ["Bilbo"])
itog_dict ["Johnny"] = sum (itog_dict ["Johnny"]) / len(itog_dict ["Johnny"])
itog_dict ["Khendrik"] = sum (itog_dict ["Khendrik"]) / len(itog_dict ["Khendrik"])
itog_dict ["Steve"] = sum (itog_dict ["Steve"]) / len(itog_dict ["Steve"])
print(sorted_students [0], itog_dict ["Aaron"], sorted_students [1], itog_dict ["Bilbo"], sorted_students [2], itog_dict ["Johnny"], sorted_students [3], itog_dict ["Khendrik"],sorted_students [4], itog_dict ["Steve"])
# дополнительно - реализовать вывод по ключу
vvod_zaprosa_name = input("Введите ключ студента: ")
a = vvod_zaprosa_name
print(a, itog_dict.get(a))
# print(a, type(a))
# print(itog_dict.get(a))






