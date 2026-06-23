# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year-old.


def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}/n"

    with open(f"R:\\Python\\practice_\\chapter9\\tables")as f:
        f.write(table)



for i in range(2, 23):
    generateTable(i)



# next 

for i in range(0, 21):
    file_path = ("R:\\Python\\practice_\\chapter9\\tables")
    f = open(file_path, "w")
    f.write(f"Multiplication Table of {i}\n")
    f.write("=" * 25 + "\n")
    for j in range(1, 11):
        line = f"{i} x {j} = {i * j}\n"
        f.write(line)
    f.close()

print("All tables from 0 to 20 are created successfully in your folder!")


'''
This for loop repeats from 2 to 20 (including 20). first line


'''