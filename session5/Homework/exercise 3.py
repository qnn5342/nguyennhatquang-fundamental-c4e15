n = int(input("please insert a number: "))

test = 1
count = 0
while test < n:
    test +=1
    if n % test == 0:
        count += 1
if count > 2:
    print ("{0} is not a prime number".format(n))
else:
    print ("{0} is a prime number".format(n))
