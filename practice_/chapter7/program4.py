#  Write a program to find whether a given number is prime or not



o = int(input("Enter your number: "))

for i in range(2, o):
 if(o%i) == 0:
        print("Number is prime: ")
        break

else:
    print("Number is not prime: ")

    
