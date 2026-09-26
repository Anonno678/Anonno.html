class Rectangle():
    def __init__(self, l, w):
        self.lenght = l
        self.width = w
    def rectangle_area(self):
        return self.lenght*self.width
newRectangle = Rectangle(12, 10)
print("Dimension of Rectangle - Lenght : %d width :n%d" % (newRectangle.lenght,newRectangle.width))
print("Area of Rectangle :", newRectangle.rectangle_area())       