from random import randint


#opens HangmanWord.txt with a list of 35 words for hangman
#puts those words into an array called 'words'
f = open("HangmanWord.txt")
words = []
for line in f:
    words.append(line)
f.close()

#makes an array to output a losing message for Mr.Gresh
file = open("LoseMessages.txt")
wrong = []
for line in file:
    wrong.append(line)
file.close()


guesses = 7
#generates random number to use as index in words
index = randint(0, len(words) -1)
word = words[index]

#print(word)
print ("Welcome to Hangman! Try to figure out the word with 7 lives.")
a = len(word)
for x in range(1, a):
    print("_", end = ' ')
    
print("")

letters = list(word)

#output is the word w/ the correct blanks (_) and guessed letters
output = ["_"]
for x in range(2, a):
    output.append("_")
#sets lose to false; when lose = true the game is over
#regardless if they won or lost
lose = False
while lose == False:
    letter = input("Guess a letter:")

    #player guessed correctly
    if letter in letters:
        print("Lucky guess...")
        for n,i in enumerate(letters):
            if i==letter:
                output[n] = letter
        print(' '.join(output))
        if "_" not in output:
            print('Congratulations! The word was '+word)
            print('Somehow you won... you probably cheated.')
            lose = True
    #player guessed letter incorrectly            
    else:
        guesses -= 1
        y = randint(0, len(wrong) -1)
        print(wrong[y])
        #player has one life left
        if guesses>1:
            print("You have ", guesses, " lives left.")
        else:
            print("You have 1 life left.")
        print(' '.join(output))

    #when player has lost game
    if guesses==0:
        lose = True
        print('The word was '+word)
        print("You lost. And you don't get to play again.")

            
        
    
    





