numbers = [1,3,4,5,6,7,4,2,4,5,7,8,3,8,9]

check = int(input("Please enter a number: "))

print ("Print occurence without count function")
#without count
count = 0
for item in numbers:
    if item == check:
        count+=1
print ("{0} appears {1} times in my list".format(check, count))


print ("Print occurence without function")
#with count

print ("{0} appears {1} times in my list".format(check, numbers.count(check)))
