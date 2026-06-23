f = open("R:\\Python\\practice\\file.txt")

print(f.read())
f.close

with open("R:\\Python\\practice\\file.txt") as f:
    print(f.read())