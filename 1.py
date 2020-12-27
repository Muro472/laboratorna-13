class TPTriangle:
    def __init__(self,a = 1,b = 1):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def s(self):
        return self.a * self.b / 2

    @a.setter
    def set_a(self,value):
        value = int(value)
        if value <= 0:
            raise Exception('error')
        else:
            self.__a = value

    @b.setter
    def set_b(self,value):
        if value <= 0:
            raise Exception('error')
        else:
            self.__b = value

    def square(self):
        return self.s

    def perrimeter(self):
        return self.a + self.b + (self.a ** 2 + self.b ** 2) ** 0.5

    def __add__(self, other):
        return self.a + other

    def __mul__(self, other):
        return self.a * other

    def __sub__(self, other):
        return self.a - other

    def __lt__(self, other):
        return self.s < other.s

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.s > other.s

    def __le__(self, other):
        return self.s <= other.s

    def __ge__(self, other):
        return self.s >= other.s

class TPPiramid(TPTriangle):
    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.h = h

    @property
    def v(self):
        return super().square() * self.h / 3

    @d.setter
    def set_d(self,value):
        if value <= 0:
            raise Exception('error')
        else:
            self.__d = value

    def volume(self):
        return self.v

    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v

    def __ne__(self, other):
        return self.v != other.v

    def __gt__(self, other):
        return self.v > other.v

    def __le__(self, other):
        return self.v <= other.v

    def __ge__(self, other):
        return self.v >= other.v
