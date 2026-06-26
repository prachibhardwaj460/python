#  Create a class “Programmer” for storing information of few programmers working at Microsoft.


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, company):
        self.company = company
        self.name = name
        self.salary = salary



p = Programmer("Prachi", 1200, "Microsoft")
print(p.name, p.company, p.salary)

o = Programmer("Prachii", 1200, "Microsoft")
print(o.name, o.company, o.salary)


i = Programmer("Prachiii", 1200, "Microsoft")
print(i.name, i.company, i.salary)
