# We all have played snake, water gun game in our childhood. write the game by giving the  username 

'''
1 = snake
2 = water 
3 = gun

'''

computer = 3 
you = int(input("Enter your choice: "))
youDict = {1 : "s",  2 : "w", 3 : "g"}

if(computer == 1 and you == 2):
    print("you win")
    

elif(computer == 1 and you == 3):
    print("you win")

elif(computer == 2 and you == 1):
    print("you win")

elif(computer == 2 and you == 3):
    print("computer win")

elif(computer == 3 and you == 1):
    print("computer win")

elif(computer == 3 and you == 2):
    print("you win")

else:
    print("Something went wrong")