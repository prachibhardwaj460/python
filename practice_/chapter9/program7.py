#  Write a program to find out the line number where python is present from ques 



with open("R:\\Python\\practice_\\chapter9\\log.txt") as f:
    lines = f.readlines()

lineno = 1 

for line in lines:
    if("python" in line):
        print(f"Yes pyhton is present.  Line no:{line}")
        break
        lineno += 1

    else:
        print("No python is not present: ")

