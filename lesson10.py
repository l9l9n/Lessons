# Decorators

# def my_decorator(func):
#     def wrapper():
#         print('До вызова функции')

#         func()

#         print('После фызова фунции')
#     return wrapper


# @my_decorator
# def hello():
#     print('Привет, это между вызовами!')


# hello()


# Пример декоратора с аргументами

def in_num(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
    
@in_num(5)
def hello(name):
    print('Hello', name)

hello('Tilek')


