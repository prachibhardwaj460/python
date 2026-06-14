# Write a program using functions to find greatest of three numbers

a = 5
b= 9
c = 12

def greatest(a, b, c):
    if(a>b and a>c):
        return(a)
    elif(c>a and c>b):
        return(c)
    elif(b>a and b>c):
        return(b)
    
print(greatest(a, b, c))
