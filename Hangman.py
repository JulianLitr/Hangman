#Hangman with preset word

word = list("apple")
strWord = "apple"
guesses = 3
winner = False
incorrectLetters = []
guess = [""] * len(word)
print(guess)
def wrong():
    global guesses
    guesses -= 1

def score():
    print("Guesses left: " + str(guesses))
    print("Incorrect Letters: ", end ="")
    for x in range(len(incorrectLetters)):
        if x == len(incorrectLetters) - 1:
            print(incorrectLetters[x], end ="")
        else:
            print(incorrectLetters[x], end =", ")
    print("")
    for x in range(len(guess)):
        if x == len(guess) - 1:
            print(guess[x], end ="_")
        else:
            print(guess[x], end ="_,")
    print("")
            
def ask():
    letter = input("Please guess a letter: ")
    #letterguess = letter
    for i in range(len(strWord)):
        if letter == word[i]:
            print("")
            
            

    
print("Let's play Hangman. You have 10 Guesses to guess the word")
while guesses > 0 and winner == False:
    score()

    ask()
    
    guesses -= 1

if guesses == 0:
    print("You lost. The word is " + strWord)
else:
    print("Great job! You won with " + str(guesses) + " guesses left!")
