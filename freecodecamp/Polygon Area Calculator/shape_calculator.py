class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        pass

    def get_amount_inside(self):
        pass


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = self.width

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
        self.side = new_side

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width
        self.side = new_width

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height
        self.side = new_height


s = Square(7)
s.set_height(6)
print(s.side)
print(s.height)
print(s.width)
print(s)
print((s.get_area()))
print((s.get_perimeter()))
