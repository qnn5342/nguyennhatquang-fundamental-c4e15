# Log-in username , if correct and then password
print ("Welcome to Log-in")

# Insert username and password
loop = True
n = 0
p = 0
while n < 3 and p<3 and loop == True:
    username = input("Please input username: ")
    if username == "c4e":
        while p < 3:
            pass_word = input("please input password: ")
            if pass_word == "yay":
                loop = False
            else:
                print ("Wrong pass, enter again")
                p+=1
                
    else:
        print ("Wrong username, enter again")
        n+=1
if p == 3:
    print ("Wait, you entered pass wrong 3 times, go away")
elif n ==3:
    print ("Wait, you entered user wrong 3 times, go away")
else:
    print ("Do anything to me, master!!!")
