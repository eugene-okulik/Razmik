class Flowers:
    def __init__(self, title, svejest, color, len_steble, price, life_time):
        self.__title = title
        self.__svejest = svejest
        self.__color = color
        self.__len_steble = len_steble
        self.__price = price
        self.__life_time = life_time

    @property
    def title(self):
        return self.__title

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
        super().__init__(svejest, "Rose", color, len_steble, price, life_time)


class Tulip(Flowers):
    def __init__(self, svejest, color, len_steble, price, life_time):
        super().__init__(svejest, "Tulip", color, len_steble, price, life_time)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def __add__(self, obj):
        return [self.flowers, obj]

    def avg_life_time(self):
        total_life_time = sum(f.avg_life_time for f in self.flowers)
        return total_life_time / len(self.flowers)

    def sort_svejest(self):
        return sorted(self.flowers.svejest)

    def sort_color(self):
        return sorted(self.flowers.color)

    def sort_len_steble(self):
        return sorted(self.flowers.len_steble)

    def sort_price(self):
        return sorted(self.flowers.price)

    def sort_life_time(self):
        return sorted(self.flowers.life_time)

    def find_flower(self, obj):
        for flower in self.flowers:
            if flower == obj:
                return flower
        return None
