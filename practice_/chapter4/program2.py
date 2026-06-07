# Write a program to accept marks of 6 students and display them in a sorted manner

mark = []

g1 = input("Enter your marks: ")
mark.append(g1)
g2 = input("Enter your marks: ")
mark.append(g2)

mark.sort(reverse=True)

print(mark)