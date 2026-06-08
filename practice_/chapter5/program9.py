#  Can you change the values inside a list which is contained in set S?



s = {8, 7, 12, "Harry", (1,2)}

print(type(s)) # it can happen 



s = {8, 7, 12, "Harry", [1,2]}

print(type(s)) # but it will not because (1,2) are tuples and tuples are immutable
