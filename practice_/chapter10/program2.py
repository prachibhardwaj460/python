#  Write a class “Calculator” capable of finding square, cube and square root of a number.



class calculator:
    def __init__(self, m):
        self.m = m
    def square(self):
        print(f"The square is {self.m*self.m}")

    def cube(self):
        print(f"The cube is {self.m*self.m*self.m}")

    def squareroot(self):
        print(f"The squareroot is {self.m**1/2}")



a = calculator(9)
a.square()
a.squareroot()
a.cube()