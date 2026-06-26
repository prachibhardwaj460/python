class employe:
    lang = "Python" # this is a class attribute
    salary = 0

# intence attribute take preferance intence>object

Prachi = employe()
Prachi.lang = "JavaScript" # intence attribute
print(Prachi.lang, Prachi.salary)