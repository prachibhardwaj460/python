# write a program to print multiplication table of n using for loops in reversed order.


a = int(input("Enter the number: "))

for i in range(1,10):
    print(f"{a} x {i} == {a*i}")

