print ("Welcome! Let's print star and x(s) in rectangle")

length = int(input("Please insert your length of star and x (s): "))
width =  int(input("Please insert your width of star and x (s): "))

for u in range (width):
    for i in range (length):
        if u%2 == 0:
            print ("*", end ="")
            print ("x", end ="")
        else:
            print ("x", end ="")
            print ("*", end ="")
    print()
