print ("Welcome to the Greatest Clothing Shop!!")
shoplist = ['T-shirt','Sweater', "Pants"]

answer = (input("What do you want? (C,R,U,D): ")).lower()
if answer == "r":
    print("Our items: ", end ="")
    print(*shoplist, sep =", ")

if answer == "c":
    new_item = input("Please enter your new item?: ")
    shoplist.append(new_item)
    print("Our items: ", end ="")
    print(*shoplist, sep =", ")

loop = True
if answer == "u":
    while loop:
        position = int(input("Please enter your position to update:  (only within 1 and {})".format(len(shoplist))))
        if 0 > position or position > len(shoplist):
            print ("sorry! it's out of range. Please re-enter")
        else:
            loop = False
    else:
        new_item = input("Please enter your new item: ")
        shoplist[position-1] = new_item
        print("Our items: ", end ="")
    print(*shoplist, sep =", ")
#to handle out-of-range later

if answer == "d":
    while loop:
        position = int(input("Please enter your position to delete: (only within 1 and {})".format(len(shoplist))))
        if 0 > position or position > len(shoplist):
            print ("sorry! it's out of range. Please re-enter")
        else:
            loop = False
    else:
        shoplist.pop(position-1)
        print("Our items: ", end ="")
    print(*shoplist, sep =", ")
