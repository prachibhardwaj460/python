#  Write a program to mine a log file and find out whether it contains ‘pythonʼ.

with open("R:\\Python\\practice_\\chapter9\\log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes pyhton is present: ")

else:
    print("No python is not present: ")



