from random import randrange

def getGuess():
    return int(input("Enter your guess from 1 to 100: "))

def main():
    print("Welcome to the guessing game!")
    print("I have chosen a number from 1 to 100.")
    print("You have seven guesses to find it. Good luck!")
    print()
    
    #computer picks the number
    secretNumber = randrange(1,100) +1
    
    guess = getGuess()
    guesses = 1
    
    while(guess != secretNumber and guesses < 7):
        guess = getGuess()
        guesses += 1
        
    if guesses < 7:
        print("You Got it!")
    else:
        print("You didn't guess it! The number waas {}".format(secretNumber))
        
main()
        