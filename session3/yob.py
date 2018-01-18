count = 0
while count < 5:
    yob = int(input("input year born: "))
    age = 2018 - yob

    if age < 10:
        print ("Baby")
    elif age < 18:
        print ("Teenager")
    else:
        print ("Adult")
    count +=1
