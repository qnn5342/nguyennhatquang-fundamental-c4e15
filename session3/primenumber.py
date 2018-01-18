n = int(input("please insert a number: "))

test = 1
count = 0
while test < n:
    test +=1
    if n % test == 0:
        count += 1
if count > 2:
    print ("N is not a prime number")
else:
    print ("N is prime number")
