print ("welcome to factorial")

n = int(input("Please enter the number for factorial:"))

e = 1
for i in range (1,n+1):
    e = i *e
print ("Factorial of",n, "is: ",e)
