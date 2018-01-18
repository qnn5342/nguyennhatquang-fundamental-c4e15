print ("Welcome to the guessing game!")
n = int (input("Please think & enter a number from 1 to 100 and don't tell me: "))
guess = n//2
if n > 100 or n <1:
    print ("please enter number in range above")
else:
    print ("Now I begin to guess")

    print ("is it",guess, "?")

    """Please tell me the following:
    C if i was correct
    S if I guessed too big
    L if i guessed too small"""

    reply = input("Did I guess it right? Enter answer as instructed above. C or S or L?")
    while reply == "C":
        if 
