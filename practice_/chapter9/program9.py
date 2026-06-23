
# 9. Write a program to find out whether a file is identical and matches the content of another


with open("R:\\Python\\practice_\\chapter9\\file.txt") as f:
    content1 = f.read()


with open("R:\\Python\\practice_\\chapter9\\this.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")