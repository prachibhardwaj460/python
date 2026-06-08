# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up?


d = {}
name = input("Enter freinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter freinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter freinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter freinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)