class Whore:
    def __init__(self, name: str, age: float, price: float) -> None:
        self._name = name
        self.__age = age
        self.__price = price

    def get_age(self):
        return self.__age

    def set_age(self, new_age: float):
        self.__age = new_age

natasha = Whore('Наташа', 56, 1350.4)
# natasha.__age == 18
print(natasha._Whore__age)