# Write a python function to print multiplication table of a given number

i = int(input("Enter your number: "))

def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiply(i) 

