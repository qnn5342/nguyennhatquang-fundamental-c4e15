print("Hello, this is Quang and here are all sizes of my flock")
sheepflock = [10,93,1001,39,59,945,534,58]
sheepflock2 = []


#2.1
print (sheepflock)

#2.2
max_value = 0
for i in sheepflock:
    if i > max_value:
        max_value = i

print ("Now my biggest sheep has size {0} and let's shear it".format(max_value))

#2.3
position = 0
while sheepflock[position] < max_value:
    position+=1
sheepflock[position] = 8
print ("After shearing, here is my flock \n{0}".format(sheepflock))
#2.4
value = 0
for x in sheepflock:
    value = x + 50
    sheepflock2.append((value))

print ("One month has passed, now here is my flock")
print (sheepflock2)
