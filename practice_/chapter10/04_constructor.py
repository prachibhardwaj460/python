class Employe:
    language = "Python"
    salary = 12

    def __init__(self): # dundar method which is automatically call 
         print("I am creating an object")


    def getInfo(self):
        print("The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
            print("Good morning")


prachi = Employe()
prachi.name = "Prachi"
print(prachi.name, prachi.salary, prachi.language)