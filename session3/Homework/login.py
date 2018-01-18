print ("Welcome to Log-in")

# Insert username and password

n = 3
p = 3
while n != 0 and p !=0:
    username = input("Please input username: ")
    if username == "c4e":
        pass_word = input("please input password: ")
        if pass_word == "yay":
            #print("You Got me!")
            break
        else:
            print ("Wrong password")
            p-=1
            continue #### still go back to username
    else:
        print("Wrong username")
        n-=1
