class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)
        
        return Point(self.x + other.x , self.y + other.y)
    
    def __str__(self):
        return f'x: {self.x} y: {self.y}'
    
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __gt__(self, other):
        if isinstance(other, Point):
            return self.x > other.x and self.y > other.y


    def __lt__(self, other):
        if isinstance(other, Point):
            return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        if isinstance(other, Point):
            return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        if isinstance(other, Point):
            return self.x <= other.x and self.y <= other.y

    # def __mul_(self, other):
    #     return Point()
    


point1 = Point(10, 10)
point2 = Point(20, 20)

print(point1 < point2)






# import math

# class Complex:

#     def __init__(self, re=0, im=0):

#         self.re = re

#         self.im = im

#     def __add__(self, other):

#         # If Int or Float Added, return a Complex number where float/int is added to the real part

#         if isinstance(other, int) or isinstance(other, float):

#             return Complex(self.re + other,self.im)

#         # If Complex Number added return a new complex number having a real and complex part

#         elif  isinstance(other, Complex):

#             return Complex(self.re + other.re , self.im + other.im)

#         else:

#             raise TypeError



# a = Complex(12)

# b = Complex(4)

# print(a / b)