class Employe:
        lang = "Python"
        salary = 10

        def getInfo(self):
                print(f"The lang is {self.lang}. The salary is {self.salary}")

        def greet(self):
                print("Good morning")

prachi = Employe()
    # prachi.lang = "JavaScript"
prachi.greet()
prachi.getInfo()