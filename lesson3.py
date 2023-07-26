# a = 1
# b = 2
# c = 13.6

# print(max(a, b, c))
# print(min(a, b, c))

# print(type(c))

# name = 'Jhon Doe'
# repl_name = name.replace('Doe', 'Carter')
# up_case = name.upper()
# low_case = name.lower()
# length = len(name)


list() # Изменяемый
a = ['Apple', 'Malon', 'Orange']
tuple() # Не изменяемый
b = ('Apple', 'Malon', 'Orange', 'Banana', 'Kivy', 'Apple')
dict() # Изменяемый key: value
c = {'Apple': 2, 'Malon': 1, 'Orange': 3, 'Banana': 5, 'keyses': [1, 2, 3, 4, 5]}
set() # Изменяемый каждый элемент уникальный
d = {'Apple', 'Malon', 'Orange' }

# print(a)
# print(b)

# a.append('Cherry') # Add item
# a.remove() # Delet item
# aa = a.pop(1) # Delet last item
# print(aa)
# ab = a.index('Apple') # Show position item index
# print(ab)
# a.reverse() # Reversed list
# a2  = a.copy()
# print(a)
# print(a2)


# index = b.index('Banana') # Узнаем индек элемента

# keys = c.keys() # Вывод только ключей
# print(keys)

# values = c.values() # Вывод только значений
# print(values)

# itemss = c.items() # Вывод всех значений
# print(itemss)

# name = c.get('keyses') # Получение значения по ключю
# print(name)

# name = c.pop('Banana') # Удаления значеня по ключю
# print(name)
# print(c)

# c.clear() # Очистка списка либо словоря
# print(c)

# cnt = b.count('Apple') # Считает количество одинаковых элементов
# print(cnt)

# d.add('water') # for tupple
# print(d)
a = [3, 3, 9, 10, 33, 1, 8, 4]
a.sort() # for list, tuple
print(a)