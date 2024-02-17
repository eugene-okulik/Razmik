class Flowers:
    def __init__(self, svejest, color, len_steble, price, life_time):
        self.__svejest = svejest
        self.__color = color
        self.__len_steble = len_steble
        self.__price = price
        self.__life_time = life_time

    @property
    def svejest(self):
        return self.__svejest

    @property
    def color(self):
        return self.__color

    @property
    def len_steble(self):
        return self.__len_steble

    @property
    def price(self):
        return self.__price

    @property
    def life_time(self):
        return self.__life_time


class Roses(Flowers):
    def __init__(self, svejest, color, len_steble, price, life_time):
        super().__init__(svejest, color, len_steble, price, life_time)


class Tulip(Flowers):
    def __init__(self, svejest, color, len_steble, price, life_time):
        super().__init__(svejest, color, len_steble, price, life_time)


class Bouquet:
    def __init__(self):
        self.flowers = flowers

    def __add__(self, obj):
        return self.flowers + obj

    def avg_life_time(self):
        total_life_time = sum(f.avg_life_time for f in self.flowers)
        return total_life_time / len(self.flowers)

    def find_flower(self):
        return self if self.svejest or self.color or self.len_steble or self.price or self.life_time else None
