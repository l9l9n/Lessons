# Zadania

name = input('Введите имя: ')
print('Привет', name, 'как дела?')

################################################

dlina = int(input('Длина: '))
shirina = int(input('Ширина: '))
s = dlina * shirina
print('Площадь', s)

################################################

temp = int(input('Введите температуру: '))
res = (temp * 9/5) + 32
print('В цельсиях', res)

################################################

a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))
res = (a + b + c) / 3
print('Result: ', res)

################################################

ves = int(input('Вес: '))
rost = float(input('Рост: '))
rost2 = rost*2
res = ves / rost2
print(f'Индекс массы тела: ', res)