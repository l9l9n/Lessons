"""
Задача: Проверка аргументов функции.
Напишите декоратор который проверяет аргументы функции на тип и выводит предупреждение, 
если они не соответствуют ожидаемым типам. 
Пусть функция принимает два аргумента: x (целое число) и y (строка). 
Если типы аргументов не соответствуют ожидаемым, выведите предупреждение на экран.
"""

def checker(function):
    def wrapper(x, y):
        if not isinstance(x, int):
            print('"x" No match! Must be integer')
        else:
            print('"x" Match!!!')
        if not isinstance(y, str):
            print('"y" No match! Must be string')
        else:
            print('"y" Match')
        return function(x, y)
    return wrapper


@checker
def example(x, y):
    pass


# example(1, 'hello')
example('hello', 'hello')

