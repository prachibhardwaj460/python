#  Repeat program 4 for a list of such words to be censored



words = ["Donkey", "ganda"]

with open("R:\\Python\\practice_\\chapter9\\file.txt", "r") as f:
                content = f.read()

for word in words:
            content = content.replace(word, "#" * len(word))

with open("R:\\Python\\practice_\\chapter9\\file.txt", "w") as f:
                f.write(content)


