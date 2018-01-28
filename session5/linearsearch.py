list = [942,423,394,435,543,504]
insert = int(input('can you insert a number here?: '))


#2. Create a for loop to test assumption:

for index, num in enumerate(list):
    if num == insert:
        print ("Found")
        break
else:
    print ("Not found")
