from random import randint

playAgain = "y"

while (playAgain == "y"):
    num = randint(1,100)
    guess = int(input("Guess my number from 1 to 100:"))
    while (guess!=num):
        if guess>num:
            guess = int(input("Your guess is too high... try again:"))
        elif guess<num:
            guess = int(input("Your guess is too low... try again:"))

    print("Correct! My number was %s. Thanks for playing." % guess)
    guess = 0
    playAgain = input("Do you want to play again? y/n:")
    

