# _________________ТИП ДАННЫХ СЛОВАРЬ (dict)_________________________
print()
# Есть особый вид коллекции (dict - словарь), где элементы хранятся парами ключ+значение
phone_book = {"Alexei": 88005553535, "Danil": 88005553534} # Alexei - ключ, 88005553535 - значение.
print(phone_book)
# Следует отметить, что КЛЮЧОМ может быть не изменяемый объект. Т.е. в качестве ключа нельзя указать список к примеру.
# phone_book = {["Alexei"]: 88005553535, "Danil": 88005553534} # ["Alexei"] - список не может быть ключом. Ошибка (TypeError: unhashable type: 'list') - не хешируемый тип "список" (не хешируемый объект - тоже самое, что и не изменяемый)
print()
# МЕТОДЫ ДЛЯ РАБОТЫ СО СЛОВАРЕМ

# 1. Для обращения к объекту (подобие индекса, только по ключу):
print(phone_book["Alexei"])

# 2. Можно изменить значение:
phone_book["Alexei"] = 89997681122 # Изменили значение в элементе с ключём "Alexei".
print(phone_book) # вывели измененный словарь
# Словарь является изменяемой структурой
print()

# 3. Взятие не существующего ключа в словаре:
phone_book["Anton"] = 85993473472
print(phone_book) # программа добавляет его автоматически в словарь
print()

# 4. Удаление по ключу:
del phone_book["Danil"]
print(phone_book)
print()

# 5. Обновление нескольких пар сразу
phone_book.update({"Sasha": 89149995050,
                   "Alex": 89145678921}) # Метод .update принимает другой словарь
print(phone_book) # порядок может нарушиться (это его особенность)
print()
# СЛОВАРЬ ЯВЛЯЕТСЯ НЕ УПОРЯДОЧЕННОЙ ПОСЛЕДОВАТЕЛЬНОСТЬЮ!!!

# 6. Метод возвращения значения по ключу
print(phone_book.get("Danil")) # не вернет значение так, как оно удалено 'None'
print(phone_book.get("Sasha")) # вернет значение по ключу "Sasha" - 89149995050
print(phone_book.get("Danil", "Такого значения не существует в словаре")) # указывает значение по умолчанию, которое возвращается вместо 'None', если такого ключа в словаре нет.
print()

# 7. Метод .pop удаляет ключ и возвращает соответствующее ему значение
# print(phone_book) # словарь до вывода
# phone_book.pop("Anton") # взяли ключ из словаря (как бы в память по типу "ножницы", но с удалением ключа)
# print(phone_book) # вывели словарь без "Anton"

print(phone_book) # словарь до вывода
a = phone_book.pop("Anton") # взяли ключ из словаря (как бы в память по типу "ножницы", но с удалением ключа)
print(phone_book) # вывели словарь без "Anton"
print(a) # вывели вырезанное значение 85993473472
print()
# _______ *** так же работает и для списков по индексу можно вынимать значение *** _________
list_ = [1, 2, 3, 4] # создали
print(list_) # посмотрели до вынимания
list_.pop(2) # вынули индекс 2 (значение его в списки = 3)
print(list_) # посмотрели после вынимания
print()

# 8. Метод .keys возвращает коллекцию из ключей нашего словаря
print(phone_book.keys()) # dict_keys(['Alexei', 'Sasha', 'Alex'])
print()


# 9. Метод .values возвращает коллекцию из значений нашего словаря
print(phone_book.values()) # dict_values([89997681122, 89149995050, 89145678921])
print()

# 10. Метод .items возвращает коллекцию из пар (ключ + значений) нашего словаря
print(phone_book.items()) # dict_items([('Alexei', 89997681122), ('Sasha', 89149995050), ('Alex', 89145678921)])
print()

# _____ПРИМЕЧАНИЕ________
# НА МЕСТЕ КЛЮЧА ИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ НАХОДИТЬСЯ НЕ МОГУТ !!! НО НА МЕСТЕ ЗНАЧЕНИЙ МОГУТ !!!
phone_book_new = {"Alexei": [88005553535, 2, 4], "Danil": 88005553534}
print(phone_book_new)
# Еще так может реализовываться система логин пароль
print()

# 11. Множества
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print(set_) # особенность МНОЖЕСТВ в том, что они хранят только уникальные значения. (удаляет повторы) # ***На работе выгрузки фильтровать***
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, "String", True, (1,2,3)} # множество хранит в себе элементы различных типов данных (числовые значения, строка, логическое значение, кортеж)
print(set_)
print()
# ДЛЯ ПЕРЕВОДА ВО МНОЖЕСТВО ИЛИ ПОЛУЧИТЬ МНОЖЕСТВО ИЗ СПИСКА, ТОГДА ИСПОЛЬЗУЕТСЯ КОМАНДА set()
list_ = [1, 1, 1, 1, 2, 3, 4, 5,]
print("Есть некий список типа: ", list_, type(list_))
# print(set(list_)) # создал (перевел его) из списка (во) множество
# print(type(list_))
list_ = set(list_) # перевел во множество
print("Перевел его во множество: ", list_, type(list_))
# ОСОБЕННОСТЬ МНОЖЕСТВ, ЧТО ОНИ НЕ ХРАНЯТ ПОВТОРЯЮЩИЕСЯ ЭЛЕМЕНТЫ !!!
# ____ *** В списках можно обращаться по имени (индексу), то во множествах НЕЛЬЗЯ !!! *** ____ Но можно будет в циклах перебирать каждый элемент.
# print(list_[0]) # TypeError: 'set' object is not subscriptable
print()

# 11.1 Метод удаления .discard
print(list_)
print(list_.discard(1), list_.discard(2), list_.discard(3)) # В методе можно указать только одно значение! Но через запятую метод можно вызвать несколько раз !!! ***(Как бы удалил потому и None None None)
print(list_)
print()

# 11.2 Метод удаления .remove
print(list_)
print(list_.remove(4), list_.discard(2), list_.discard(3)) # В методе можно указать только одно значение! Но через запятую метод можно вызвать несколько раз !!! ***(Как бы удалил потому и None None None)
print(list_)
print()
# Отличия в том, что .discard не будет выдавать ошибку, если элемент не был найден во множестве.

# 11.3 Метод .pop вынимает значение
list_.add(1000000), list_.add(15), list_.add(13), list_.add(5)
print(list_)
print(list_, list_.add(1000000), list_.add(15), list_.add(13), list_.add(5))
# list_.pop(5) # НЕ ПОЛУЧАЕТСЯ ВЫРЕЗАТЬ ЭЛЕМЕНТ !!! (НА 14.10.2024)
print()

# 11.4 Метод .add добавляет значение в конец множества
print("11.4 Метод .add добавляет значение в конец множества")
print(list_.add("90"), list_.add(15), list_.add(13), list_.add(5), list_.add("GitHub"))
print(list_)
print(list_)

