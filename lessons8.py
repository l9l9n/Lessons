# files Работа с файлами

# file = open(filename, режим доступа к файлу)
# 'r' - read() за чтение файла
# 'w' - write() запись с удалением существующих данных 
# 'a' - append() запись с добавлением новой строки
# 'x' - создание файла если его не существует

# rb, wb -- чтение и запись в бинарном виде

# file = open('text.txt', 'w')
# text = file.write("Hello world")
# print(text)
# file.close()

# file = open('text.txt', 'a')
# text = file.write("\tAnny\nBanny\nManny")
# print(text)
# file.close()


# with open('ttextr.txt', 'x') as file:
#     text = file.write('PICHACHU')

# with open('image.jpeg', 'rb') as file:
#     data = file.read()

# print(data)