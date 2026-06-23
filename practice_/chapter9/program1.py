#  Write a program to read the text from a given file ‘poems.txtʼ and find out whether it contains the word ‘twinkleʼ

f = open("R:\\Python\\practice_\\chapter9\\poem.txt")

data = f.read()


if("Twinkle" in data):
      print("Twinkle is present in the data")
else:
    print("Not")
# print(data)
f.close
