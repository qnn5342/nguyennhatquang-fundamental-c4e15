list = [942,423,394,435,543,504]
insert = int(input('can you insert a number here?: '))

#1. Assumption:

found_index = -1 # Not found

#2. Create a for loop to test assumption:

for index, num in enumerate(list):
    if num == insert:
        found_index = index # update assumption
        break

# print resilt
if found_index == -1:
    print  ("Not found")
else:
    print ("Found at index", insert)
