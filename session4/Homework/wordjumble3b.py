listx=[]

a = ['awesome', 'great', 'football', 'messi', 'Cristiano Ronaldo']

import random
listx.append(random.choice(a).lower())

from random import shuffle
y = [i for i in listx[0]]
shuffle(y)
print(*y)

answer = (input("Please input your guess for the word about: ")).lower()

if answer == listx[0].lower():
    print ("Yay ^^!")
else:
    print ("Sorry, :( try better next time")
