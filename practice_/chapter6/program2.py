#  Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user


a1 = int(input("Enter your marks 1: "))
a2 = int(input("Enter your marks 2:"))
a3 = int(input("Enter your marks 3: "))

total_percentage = 100*(a1 + a2 )/300

if(total_percentage>=40):
    print("You are pass")


else:
    print("you are fail")