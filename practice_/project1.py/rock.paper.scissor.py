# We all have player rock , paper, scissor game in our childhood. write the game by giving the  username 

'''
rock = 0 
scissor = 1
paper = -1
'''


computer = 0
you = int(input("Enter your choice: "))
youDict = {1 : "s",  0 : "r", -1 : "p"}



if(computer == 0 and you == 1):
    print("computer win")
    

elif(computer == 0 and you == -1):
    print("you win")

elif(computer == -1 and you == 1):
    print("computer win")

elif(computer == -1 and you == 0):
    print("computer win")

elif(computer == 0 and you == 1):
    print("computer win")

elif(computer == 0 and you == -1):
    print("you win")

else:
    print("Something went wrong")