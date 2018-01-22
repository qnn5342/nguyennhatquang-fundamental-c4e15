listx=[]

a = "awesome"

from random import shuffle
listx = [i for i in a]
shuffle(listx)
print(*listx)

answer = (input("Please input your guess for the word about: ")).lower()

if answer == a:
    print ("Yay ^^!")
else:
    print ("Sorry, :( try better next time")
