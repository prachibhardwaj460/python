# A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file
def change():
            
    word = "Donkey"


    with open("R:\\Python\\practice_\\chapter9\\file.txt", "r") as f:
            content = f.read()
    contentNew = content.replace(word, "#######")

    with open("R:\\Python\\practice_\\chapter9\\file.txt", "w") as f:
            f.write(contentNew)

change()