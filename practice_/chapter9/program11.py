# 11. Write a python program to rename a file to “renamed_by_python.txt”.



with open("hiscore.txt") as f:
    content = f.read()



with open("hiscore.txt", "w") as f:
    f.write("")