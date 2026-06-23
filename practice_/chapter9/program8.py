# Write a program to make a copy of a text file “this.txt”.




with open("R:\\Python\\practice_\\chapter9\\this.txt",'r') as f:
    data = f.read()

print(data)
with open("R:\\Python\\practice_\\chapter9\\this1.txt","w") as f:
  f.write(data)