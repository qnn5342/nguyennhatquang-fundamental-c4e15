print ("Welcome! Let's print star(s) in rectangle")

length = int(input("Please insert your length of stars: "))
width =  int(input("Please insert your width of stars: "))

for i in range (width):
    for i in range (length):
        print ("*", end ="")
    print()
