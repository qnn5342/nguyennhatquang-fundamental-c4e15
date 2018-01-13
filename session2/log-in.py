from getpass import getpass
user = input("Please input username:")
pass_word = getpass ("please input password:")
if user == "c4e":
    if pass_word == "codethechange":
        print ("Welcome, do anything to me master!")
    else:
        print("Wrong pass")

else:
        print ("re-enter your username")
