n = int(input("Please input a number and don't tell me: "))

digit = 0
while n >0:
    n= n//10
    digit+=1
print ("Your number has", digit, "digits")
