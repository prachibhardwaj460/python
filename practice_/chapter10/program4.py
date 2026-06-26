#  Add a static method in problem 2, to greet the user with hello




class calculator:
    
    def __init__(self, m):
        self.m = m

    def square(self):
        print(f"The square is {self.m*self.m}")

    def cube(self):
        print(f"The cube is {self.m*self.m*self.m}")

    def squareroot(self):
        print(f"The squareroot is {self.m**(1/2)}")

    @staticmethod
    def hello():
            print("Hello there!")



a = calculator(9)
a.square()
a.hello()
a.squareroot()
a.cube()

