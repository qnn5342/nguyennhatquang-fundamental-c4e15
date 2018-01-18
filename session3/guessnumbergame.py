print ("Welcome to the guessing game!")
print ("Please wait a bit for me to think of a number from 1 to 100")
import random
select = random.randint(1,101)
print ("Done! Can you guess my number?")
LOOP = True
while LOOP:
    guess = int(input("Please input your guess here: "))

    if select < guess:
        print ("TOO BIG FOR ME!!!")
    elif select > guess:
        print ("Guess bigger")
    else:
        print ("YOU GOT ME!!!")
        LOOP = False
