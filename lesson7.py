# function

# def hello(args):
#     pass
#     #block your code

#     return # RETURN result


# def hello(a, b): # Positonals args
#     c = a + b
#     print('Hello World')
#     return c

# print(hello(2, 4))

# def hello(a=3, b=4): # Named args
#     c = a + b
#     print("Hello World")
#     return c

# print(hello(4))

# def hello(*args): #
#     result = 0

#     for i in args:
#         result += i

#     return result

# print(hello(1,2,3,4))

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ':', value)

# hello(name = 'Tilek', age = '22', male='men')


# def hello(**kwargs):  # Переменная которая принимает в себя неограниченное колл-во именнованных аргуметов
#     for key, value in kwargs.items():
#         print(value**2)

# hello(n=3, b=4, c=5)

# a = 'Ne hello'

# def hello():
#     a = 'hello'
#     return a

# def ne_hello(a):
#     return a

# print(hello())
# print(ne_hello(a))

# Anonimus function
# num = lambda x,y: x+y
# print(num(1,3))

# num = lambda n : n % 2 == 0
# print(num(4))

def fak(u):
    if u == 0:
        return 1
    else:
        return fak(u - 1) * u
    
print(fak(5))
