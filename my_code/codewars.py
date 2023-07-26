def cookie(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"  
    elif type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    elif type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    

print(cookie('sdf'))
print(cookie(3))
print(cookie(True))