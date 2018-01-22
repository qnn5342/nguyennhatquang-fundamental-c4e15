print("Hello, this is Quang and here are all sizes of my flock")
sheepflock = [10,93,1001,39,59,945,534,58]

print (sheepflock)

month = int(input("Please insert number of months you would like to raise sheep: "))

#Month print

for i in range(month):
    print("MONTH {}".format(i+1))
    print ("One month has passed, now here is my flock")


# Print new sheepflock

    value = 0
    for x in range(len(sheepflock)):
        sheepflock[x] = sheepflock[x] + 50
    print(sheepflock)


# Finding sheep with biggest size


    max_value = 0
    for i in sheepflock:
        if i > max_value:
            max_value = i

    print ("Now my biggest sheep has size {0} and let's shear it".format(max_value))


# Print new sheepflock after shearing

    position = 0
    while sheepflock[position] < max_value:
        position+=1
    sheepflock[position] = 8
    print ("After shearing, here is my flock \n{0}".format(sheepflock))

# Finding total sheepflock

total = 0
for x in sheepflock:
    total = x + total
print ("My flock has size in total: {0}".format(total))
print (total)
print ("I would get {0} * {1}$ = {2}$".format(total,2,total *2))
